import os

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
# 2. Mass Transfer
# =========================================================================
def build_mt_sims():
    return """/* Mass Transfer Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Stefan Tube Diffusion: EMD vs. Unimolecular Drift</h3><p class="lead">Simulate molecular diffusion across a stagnant gas film and compare Stefan convective drift against equimolar counterdiffusion.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Diffusion Distance z <span><output id="v-z1">10.0</output> mm</span></label><input type="range" id="s-z1" min="1.0" max="50.0" step="1.0" value="10.0"></div>' +
              '<div class="control-group"><label>Diffusivity DAB <span><output id="v-dab">0.24</output> cm²/s</span></label><input type="range" id="s-dab" min="0.05" max="1.00" step="0.01" value="0.24"></div>' +
              '<div class="control-group"><label>Vapor Pressure PA1 <span><output id="v-pa1">20.0</output> kPa</span></label><input type="range" id="s-pa1" min="2.0" max="60.0" step="1.0" value="20.0"></div>' +
              '<div class="control-group"><label>Total Pressure P <span><output id="v-ptot">101.3</output> kPa</span></label><input type="range" id="s-ptot" min="50.0" max="300.0" step="5.0" value="101.3"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">EMD Flux NA,emd</div><div class="readout-value" id="r-nemd">1.90 mmol/m²·s</div></div>' +
              '<div class="readout-card"><div class="readout-label">Log-Mean Inert yB,lm</div><div class="readout-value" id="r-yblm">0.895</div></div>' +
              '<div class="readout-card"><div class="readout-label">Stefan Flux NA,stefan</div><div class="readout-value" id="r-nstefan">2.12 mmol/m²·s</div></div>' +
              '<div class="readout-card"><div class="readout-label">Convective Drift Boost</div><div class="readout-value" id="r-boost">+11.7 %</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-mt1" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-mt1"></p>',
      init: function(el) {
        var sZ1 = el.querySelector('#s-z1'), vZ1 = el.querySelector('#v-z1');
        var sDab = el.querySelector('#s-dab'), vDab = el.querySelector('#v-dab');
        var sPa1 = el.querySelector('#s-pa1'), vPa1 = el.querySelector('#v-pa1');
        var sPtot = el.querySelector('#s-ptot'), vPtot = el.querySelector('#v-ptot');
        var rNemd = el.querySelector('#r-nemd'), rYblm = el.querySelector('#r-yblm');
        var rNstefan = el.querySelector('#r-nstefan'), rBoost = el.querySelector('#r-boost');
        var svg = el.querySelector('#svg-mt1'), diag = el.querySelector('#diag-mt1');

        var R = 8.314, T = 298.15; // 25 C

        function update() {
          var z_mm = parseFloat(sZ1.value); vZ1.textContent = f(z_mm, 1);
          var Dab_cm = parseFloat(sDab.value); vDab.textContent = f(Dab_cm, 2);
          var Pa1 = parseFloat(sPa1.value); vPa1.textContent = f(Pa1, 1);
          var P = parseFloat(sPtot.value); vPtot.textContent = f(P, 1);

          if (Pa1 >= P) Pa1 = P * 0.95;

          var z = z_mm / 1000;
          var Dab = Dab_cm * 1e-4; // m2/s
          var cTot = (P * 1000) / (R * T); // mol/m3
          var yA1 = Pa1 / P;
          var yB1 = 1 - yA1;
          var yB2 = 1.0; // pure air at top

          var yB_lm = (yB2 === yB1) ? yB1 : (yB2 - yB1) / Math.log(yB2 / yB1);
          var N_emd = (cTot * Dab / z) * yA1 * 1000; // mmol/m2 s
          var N_stefan = (cTot * Dab / (z * yB_lm)) * yA1 * 1000; // mmol/m2 s
          var boost = ((N_stefan - N_emd) / Math.max(0.001, N_emd)) * 100;

          rNemd.textContent = f(N_emd, 2) + ' mmol/m²·s';
          rYblm.textContent = f(yB_lm, 3);
          rNstefan.textContent = f(N_stefan, 2) + ' mmol/m²·s';
          rBoost.textContent = '+' + f(boost, 1) + ' %';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="230" y="30" width="140" height="140" fill="#f1f5f9" stroke="#334155" stroke-width="2" rx="4"/>' +
                          '<rect x="230" y="130" width="140" height="40" fill="#0284c7" fill-opacity="0.3" stroke="#0284c7" stroke-width="1"/>' +
                          '<text x="300" y="155" text-anchor="middle" font-size="12" font-weight="700" fill="#0369a1">Volatile Liquid A</text>' +
                          '<line x1="230" y1="30" x2="370" y2="30" stroke="#16a34a" stroke-width="3"/>' +
                          '<text x="300" y="24" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">Flowing Gas (yA=0)</text>' +
                          '<line x1="390" y1="30" x2="390" y2="130" stroke="#ef4444" stroke-width="2"/>' +
                          '<text x="400" y="85" font-size="11" fill="#dc2626" font-weight="700">z = ' + f(z_mm,1) + ' mm</text>' +
                          '<text x="110" y="70" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Stefan Diffusion Tube</text>' +
                          '<text x="110" y="95" text-anchor="middle" font-size="11" fill="#64748b">PA1 = ' + f(Pa1,1) + ' kPa</text>' +
                          '<text x="110" y="115" text-anchor="middle" font-size="11" fill="#64748b">P = ' + f(P,1) + ' kPa</text>' +
                          '<text x="110" y="140" text-anchor="middle" font-size="11" font-weight="700" fill="#0284c7">Flux = ' + f(N_stefan,2) + ' mmol/m²·s</text>';
          diag.textContent = 'Diffusion through stagnant gas: Stefan drift increases flux by ' + f(boost, 1) + '% over equimolar counterdiffusion (yB,lm = ' + f(yB_lm, 3) + ').';
        }
        [sZ1, sDab, sPa1, sPtot].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Boundary Layer Mass Transfer & Chilton-Colburn Analogy</h3><p class="lead">Evaluate convective mass transfer coefficient kc and Sherwood number Sh across laminar and turbulent boundary regimes.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Gas Velocity u <span><output id="v-vel2">3.5</output> m/s</span></label><input type="range" id="s-vel2" min="0.5" max="20.0" step="0.5" value="3.5"></div>' +
              '<div class="control-group"><label>Surface Length L <span><output id="v-len2">0.50</output> m</span></label><input type="range" id="s-len2" min="0.10" max="2.00" step="0.05" value="0.50"></div>' +
              '<div class="control-group"><label>Schmidt Number Sc <span><output id="v-sc">1.20</output></span></label><input type="range" id="s-sc" min="0.20" max="5.00" step="0.10" value="1.20"></div>' +
              '<div class="control-group"><label>Gas Diffusivity DAB <span><output id="v-dab2">2.50e-5</output> m²/s</span></label><input type="range" id="s-dab2" min="1.00e-5" max="8.00e-5" step="0.25e-5" value="2.50e-5"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Reynolds Number ReL</div><div class="readout-value" id="r-re2">116,667</div></div>' +
              '<div class="readout-card"><div class="readout-label">Sherwood Number ShL</div><div class="readout-value" id="r-sh2">242.0</div></div>' +
              '<div class="readout-card"><div class="readout-label">Mass Transfer Coeff kc</div><div class="readout-value" id="r-kc">0.0121 m/s</div></div>' +
              '<div class="readout-card"><div class="readout-label">Colburn jD Factor</div><div class="readout-value" id="r-jd">0.0019</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-mt2" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-mt2"></p>',
      init: function(el) {
        var sVel = el.querySelector('#s-vel2'), vVel = el.querySelector('#v-vel2');
        var sLen = el.querySelector('#s-len2'), vLen = el.querySelector('#v-len2');
        var sSc = el.querySelector('#s-sc'), vSc = el.querySelector('#v-sc');
        var sDab = el.querySelector('#s-dab2'), vDab = el.querySelector('#v-dab2');
        var rRe = el.querySelector('#r-re2'), rSh = el.querySelector('#r-sh2');
        var rKc = el.querySelector('#r-kc'), rJd = el.querySelector('#r-jd');
        var svg = el.querySelector('#svg-mt2'), diag = el.querySelector('#diag-mt2');

        var nuGas = 1.5e-5; // m2/s kinematic viscosity of air

        function update() {
          var u = parseFloat(sVel.value); vVel.textContent = f(u, 1);
          var L = parseFloat(sLen.value); vLen.textContent = f(L, 2);
          var Sc = parseFloat(sSc.value); vSc.textContent = f(Sc, 2);
          var Dab = parseFloat(sDab.value); vDab.textContent = Dab.toExponential(2);

          var Re = (u * L) / nuGas;
          var Sh = 0;
          if (Re < 5e5) {
            Sh = 0.664 * Math.pow(Re, 0.5) * Math.pow(Sc, 0.333); // Laminar
          } else {
            Sh = 0.037 * Math.pow(Re, 0.8) * Math.pow(Sc, 0.333); // Turbulent
          }

          var kc = (Sh * Dab) / L;
          var jD = (Sh / (Re * Math.pow(Sc, 1/3)));

          rRe.textContent = f(Re, 0);
          rSh.textContent = f(Sh, 1);
          rKc.textContent = f(kc, 4) + ' m/s';
          rJd.textContent = f(jD, 4);

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="60" y="140" width="480" height="20" fill="#334155" rx="2"/>' +
                          '<text x="300" y="155" text-anchor="middle" font-size="11" font-weight="700" fill="#f8fafc">Evaporating Plate Surface (L = ' + f(L,2) + ' m)</text>' +
                          '<path d="M 60 140 Q 240 60 540 60" fill="none" stroke="#0284c7" stroke-width="3"/>' +
                          '<text x="545" y="65" font-size="10" font-weight="700" fill="#0284c7">δc (Conc BL)</text>' +
                          '<line x1="20" y1="90" x2="60" y2="90" stroke="#16a34a" stroke-width="3"/>' +
                          '<text x="15" y="80" font-size="11" font-weight="700" fill="#15803d">u = ' + f(u,1) + ' m/s</text>' +
                          '<text x="300" y="30" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Boundary Layer: ReL = ' + f(Re,0) + ' (' + (Re < 5e5 ? 'Laminar' : 'Turbulent') + ')</text>' +
                          '<text x="300" y="180" text-anchor="middle" font-size="11" fill="#475569">kc = ' + f(kc,4) + ' m/s | ShL = ' + f(Sh,1) + ' | jD = ' + f(jD,4) + '</text>';
          diag.textContent = 'Chilton-Colburn transport analogy: Sherwood number ShL = ' + f(Sh, 1) + '. Convective mass transfer coefficient kc = ' + f(kc, 4) + ' m/s.';
        }
        [sVel, sLen, sSc, sDab].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Two-Film Interphase Mass Transfer & Resistance Allocation</h3><p class="lead">Simulate gas-liquid interfacial transport, partition equilibria, and identify the rate-controlling phase resistance.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Gas-Film Coeff ky <span><output id="v-ky">0.050</output> mol/m²·s</span></label><input type="range" id="s-ky" min="0.005" max="0.250" step="0.005" value="0.050"></div>' +
              '<div class="control-group"><label>Liquid-Film Coeff kx <span><output id="v-kx">0.80</output> mol/m²·s</span></label><input type="range" id="s-kx" min="0.10" max="4.00" step="0.10" value="0.80"></div>' +
              '<div class="control-group"><label>Henry\'s Slope m <span><output id="v-hm">1.50</output></span></label><input type="range" id="s-hm" min="0.10" max="10.00" step="0.10" value="1.50"></div>' +
              '<div class="control-group"><label>Bulk Driving Force Δy <span><output id="v-dy">0.040</output></span></label><input type="range" id="s-dy" min="0.005" max="0.100" step="0.005" value="0.040"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Overall Coeff Ky</div><div class="readout-value" id="r-kyov">0.0457 mol/m²·s</div></div>' +
              '<div class="readout-card"><div class="readout-label">Gas-Film Resistance</div><div class="readout-value" id="r-gasres">91.4 %</div></div>' +
              '<div class="readout-card"><div class="readout-label">Liquid-Film Resistance</div><div class="readout-value" id="r-liqres">8.6 %</div></div>' +
              '<div class="readout-card"><div class="readout-label">Controlling Phase</div><div class="readout-value" id="r-ctrl">Gas Film Controlling</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-mt3" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-mt3"></p>',
      init: function(el) {
        var sKy = el.querySelector('#s-ky'), vKy = el.querySelector('#v-ky');
        var sKx = el.querySelector('#s-kx'), vKx = el.querySelector('#v-kx');
        var sHm = el.querySelector('#s-hm'), vHm = el.querySelector('#v-hm');
        var sDy = el.querySelector('#s-dy'), vDy = el.querySelector('#v-dy');
        var rKyov = el.querySelector('#r-kyov'), rGasres = el.querySelector('#r-gasres');
        var rLiqres = el.querySelector('#r-liqres'), rCtrl = el.querySelector('#r-ctrl');
        var svg = el.querySelector('#svg-mt3'), diag = el.querySelector('#diag-mt3');

        function update() {
          var ky = parseFloat(sKy.value); vKy.textContent = f(ky, 3);
          var kx = parseFloat(sKx.value); vKx.textContent = f(kx, 2);
          var m = parseFloat(sHm.value); vHm.textContent = f(m, 2);
          var dy = parseFloat(sDy.value); vDy.textContent = f(dy, 3);

          var R_gas = 1 / ky;
          var R_liq = m / kx;
          var R_tot = R_gas + R_liq;
          var Ky = 1 / R_tot;
          var gasPct = (R_gas / R_tot) * 100;
          var liqPct = (R_liq / R_tot) * 100;

          rKyov.textContent = f(Ky, 4) + ' mol/m²·s';
          rGasres.textContent = f(gasPct, 1) + ' %';
          rLiqres.textContent = f(liqPct, 1) + ' %';
          rCtrl.textContent = gasPct > 70 ? 'Gas Film Controlling' : (liqPct > 70 ? 'Liquid Film Controlling' : 'Mixed Dual Resistance');

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="40" width="220" height="120" fill="#fef08a" fill-opacity="0.25" stroke="#ca8a04" stroke-width="1"/>' +
                          '<text x="190" y="70" text-anchor="middle" font-size="13" font-weight="700" fill="#854d0e">Gas Film (y)</text>' +
                          '<text x="190" y="95" text-anchor="middle" font-size="12" fill="#a16207">Resistance: ' + f(gasPct,1) + '%</text>' +
                          '<line x1="300" y1="30" x2="300" y2="170" stroke="#0f172a" stroke-width="3"/>' +
                          '<text x="300" y="24" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">Interface (yi = m·xi)</text>' +
                          '<rect x="300" y="40" width="220" height="120" fill="#dbeafe" fill-opacity="0.3" stroke="#2563eb" stroke-width="1"/>' +
                          '<text x="410" y="70" text-anchor="middle" font-size="13" font-weight="700" fill="#1e40af">Liquid Film (x)</text>' +
                          '<text x="410" y="95" text-anchor="middle" font-size="12" fill="#2563eb">Resistance: ' + f(liqPct,1) + '%</text>' +
                          '<path d="M 100 80 L 300 120 L 500 140" fill="none" stroke="#dc2626" stroke-width="3"/>' +
                          '<text x="300" y="188" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">Overall Ky = ' + f(Ky,4) + ' mol/m²·s | ' + rCtrl.textContent + '</text>';
          diag.textContent = 'Two-film resistance addition: 1/Ky = 1/ky + m/kx = ' + f(R_gas, 2) + ' + ' + f(R_liq, 2) + ' = ' + f(R_tot, 2) + ' m²·s/mol. ' + rCtrl.textContent + '.';
        }
        [sKy, sKx, sHm, sDy].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Packed Absorption Tower Kremser Solver (NTU & Height Sizing)</h3><p class="lead">Simulate countercurrent dilute gas absorption in packed towers: determine absorption factor A, NTU, and packed bed height.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Liquid-to-Gas Ratio L/G <span><output id="v-lg">1.80</output></span></label><input type="range" id="s-lg" min="0.80" max="4.00" step="0.10" value="1.80"></div>' +
              '<div class="control-group"><label>Henry Law Constant m <span><output id="v-hm4">1.20</output></span></label><input type="range" id="s-hm4" min="0.30" max="2.50" step="0.10" value="1.20"></div>' +
              '<div class="control-group"><label>Solute Recovery Req <span><output id="v-recov">95.0</output> %</span></label><input type="range" id="s-recov" min="70.0" max="99.5" step="0.5" value="95.0"></div>' +
              '<div class="control-group"><label>Transfer Unit Height HOG <span><output id="v-hog">0.65</output> m</span></label><input type="range" id="s-hog" min="0.25" max="1.50" step="0.05" value="0.65"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Absorption Factor A</div><div class="readout-value" id="r-afact">1.50</div></div>' +
              '<div class="readout-card"><div class="readout-label">Number Transfer Units NOG</div><div class="readout-value" id="r-nog">4.82</div></div>' +
              '<div class="readout-card"><div class="readout-label">Required Packed Height Z</div><div class="readout-value" id="r-zpack">3.13 m</div></div>' +
              '<div class="readout-card"><div class="readout-label">Min Solvent Margin</div><div class="readout-value" id="r-smarg">+25.0 %</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-mt4" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-mt4"></p>',
      init: function(el) {
        var sLg = el.querySelector('#s-lg'), vLg = el.querySelector('#v-lg');
        var sHm = el.querySelector('#s-hm4'), vHm = el.querySelector('#v-hm4');
        var sRecov = el.querySelector('#s-recov'), vRecov = el.querySelector('#v-recov');
        var sHog = el.querySelector('#s-hog'), vHog = el.querySelector('#v-hog');
        var rAfact = el.querySelector('#r-afact'), rNog = el.querySelector('#r-nog');
        var rZpack = el.querySelector('#r-zpack'), rSmarg = el.querySelector('#r-smarg');
        var svg = el.querySelector('#svg-mt4'), diag = el.querySelector('#diag-mt4');

        function update() {
          var LG = parseFloat(sLg.value); vLg.textContent = f(LG, 2);
          var m = parseFloat(sHm.value); vHm.textContent = f(m, 2);
          var rec = parseFloat(sRecov.value) / 100; vRecov.textContent = f(rec * 100, 1);
          var Hog = parseFloat(sHog.value); vHog.textContent = f(Hog, 2);

          var A = LG / m;
          var fracRem = 1 - rec; // y_out / y_in

          // Kremser equation for dilute absorption:
          var Nog = 0;
          if (Math.abs(A - 1.0) < 0.02) {
            Nog = rec / Math.max(0.01, 1 - rec);
          } else {
            var num = Math.log(((1 - 1/A) / (1 - rec)) + (1/A));
            var denom = 1 - 1/A;
            Nog = num / denom;
          }
          Nog = Math.max(0.5, Math.min(25, Nog));
          var Z = Nog * Hog;
          var minLG = m * rec;
          var margin = ((LG - minLG) / Math.max(0.1, minLG)) * 100;

          rAfact.textContent = f(A, 2);
          rNog.textContent = f(Nog, 2);
          rZpack.textContent = f(Z, 2) + ' m';
          rSmarg.textContent = (margin >= 0 ? '+' : '') + f(margin, 1) + ' %';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="250" y="30" width="100" height="140" fill="#e2e8f0" stroke="#475569" stroke-width="2" rx="10"/>' +
                          '<line x1="250" y1="50" x2="350" y2="150" stroke="#94a3b8" stroke-dasharray="3 3"/>' +
                          '<line x1="350" y1="50" x2="250" y2="150" stroke="#94a3b8" stroke-dasharray="3 3"/>' +
                          '<text x="300" y="105" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">Packed Bed Z=' + f(Z,1) + 'm</text>' +
                          '<line x1="300" y1="10" x2="300" y2="30" stroke="#0284c7" stroke-width="3"/>' +
                          '<text x="300" y="8" text-anchor="middle" font-size="10" font-weight="700" fill="#0284c7">Liquid Solvent In</text>' +
                          '<line x1="300" y1="170" x2="300" y2="190" stroke="#0284c7" stroke-width="3"/>' +
                          '<text x="300" y="198" text-anchor="middle" font-size="10" fill="#0284c7">Liquid Out</text>' +
                          '<line x1="220" y1="150" x2="250" y2="150" stroke="#16a34a" stroke-width="3"/>' +
                          '<text x="210" y="153" text-anchor="end" font-size="10" font-weight="700" fill="#15803d">Gas Feed</text>' +
                          '<line x1="350" y1="50" x2="380" y2="50" stroke="#16a34a" stroke-width="3"/>' +
                          '<text x="385" y="53" text-anchor="start" font-size="10" font-weight="700" fill="#15803d">Clean Gas (' + f(rec*100,0) + '% removed)</text>' +
                          '<text x="110" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Kremser Rating</text>' +
                          '<text x="110" y="105" text-anchor="middle" font-size="11" fill="#475569">A = L/(m·G) = ' + f(A,2) + '</text>' +
                          '<text x="110" y="125" text-anchor="middle" font-size="11" fill="#475569">NOG = ' + f(Nog,2) + '</text>';
          diag.textContent = 'Packed tower absorption sizing: Absorption factor A = ' + f(A, 2) + '. Required transfer units NOG = ' + f(Nog, 2) + '. Total packed bed depth Z = ' + f(Z, 2) + ' m.';
        }
        [sLg, sHm, sRecov, sHog].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Industrial Batch Drying Kinetics & Critical Moisture Content</h3><p class="lead">Simulate constant and falling-rate drying periods: calculate surface evaporation flux and total drying cycle duration.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Initial Moisture X0 <span><output id="v-x0">0.35</output> kg/kg</span></label><input type="range" id="s-x0" min="0.20" max="0.60" step="0.02" value="0.35"></div>' +
              '<div class="control-group"><label>Critical Moisture Xc <span><output id="v-xc">0.15</output> kg/kg</span></label><input type="range" id="s-xc" min="0.08" max="0.25" step="0.01" value="0.15"></div>' +
              '<div class="control-group"><label>Equilibrium Moisture Xeq <span><output id="v-xeq">0.03</output> kg/kg</span></label><input type="range" id="s-xeq" min="0.01" max="0.06" step="0.005" value="0.03"></div>' +
              '<div class="control-group"><label>Constant Drying Rate Rc <span><output id="v-rc">1.80</output> kg/(m²·h)</span></label><input type="range" id="s-rc" min="0.50" max="4.00" step="0.10" value="1.80"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Constant Period t1</div><div class="readout-value" id="r-t1">2.22 h</div></div>' +
              '<div class="readout-card"><div class="readout-label">Falling Period t2</div><div class="readout-value" id="r-t2">1.83 h</div></div>' +
              '<div class="readout-card"><div class="readout-label">Total Drying Time</div><div class="readout-value" id="r-ttot">4.06 h</div></div>' +
              '<div class="readout-card"><div class="readout-label">Final Target Xf</div><div class="readout-value" id="r-xf">0.05 kg/kg</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-mt5" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-mt5"></p>',
      init: function(el) {
        var sX0 = el.querySelector('#s-x0'), vX0 = el.querySelector('#v-x0');
        var sXc = el.querySelector('#s-xc'), vXc = el.querySelector('#v-xc');
        var sXeq = el.querySelector('#s-xeq'), vXeq = el.querySelector('#v-xeq');
        var sRc = el.querySelector('#s-rc'), vRc = el.querySelector('#v-rc');
        var rT1 = el.querySelector('#r-t1'), rT2 = el.querySelector('#r-t2');
        var rTtot = el.querySelector('#r-ttot'), rXf = el.querySelector('#r-xf');
        var svg = el.querySelector('#svg-mt5'), diag = el.querySelector('#diag-mt5');

        var Ls_A = 20; // kg dry solid per m2 tray area
        var Xf = 0.05; // target final moisture

        function update() {
          var X0 = parseFloat(sX0.value); vX0.textContent = f(X0, 2);
          var Xc = parseFloat(sXc.value); vXc.textContent = f(Xc, 2);
          var Xeq = parseFloat(sXeq.value); vXeq.textContent = f(Xeq, 3);
          var Rc = parseFloat(sRc.value); vRc.textContent = f(Rc, 2);

          var t_const = (Ls_A / Rc) * Math.max(0, X0 - Xc);
          var t_falling = (Ls_A * (Xc - Xeq) / Rc) * Math.log(Math.max(0.001, (Xc - Xeq)) / Math.max(0.001, (Xf - Xeq)));
          var t_tot = t_const + t_falling;

          rT1.textContent = f(t_const, 2) + ' h';
          rT2.textContent = f(t_falling, 2) + ' h';
          rTtot.textContent = f(t_tot, 2) + ' h';
          rXf.textContent = f(Xf, 2) + ' kg/kg';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<polyline points="80,60 300,60 520,160" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<line x1="300" y1="60" x2="300" y2="160" stroke="#dc2626" stroke-dasharray="4 4" stroke-width="2"/>' +
                          '<text x="300" y="50" text-anchor="middle" font-size="11" font-weight="700" fill="#dc2626">Xc = ' + f(Xc,2) + '</text>' +
                          '<text x="180" y="45" text-anchor="middle" font-size="11" font-weight="700" fill="#2563eb">Constant Rate (Rc=' + f(Rc,1) + ')</text>' +
                          '<text x="420" y="90" text-anchor="middle" font-size="11" font-weight="700" fill="#d97706">Falling Rate Period</text>' +
                          '<text x="80" y="180" font-size="10" fill="#64748b">X0 = ' + f(X0,2) + '</text>' +
                          '<text x="520" y="180" text-anchor="end" font-size="10" fill="#64748b">Xeq = ' + f(Xeq,3) + '</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Drying Rate Curve: Total Time = ' + f(t_tot,2) + ' h</text>';
          diag.textContent = 'Drying kinetics: Constant rate duration t1 = ' + f(t_const, 2) + ' h; Falling rate duration t2 = ' + f(t_falling, 2) + ' h. Total drying time = ' + f(t_tot, 2) + ' h.';
        }
        [sX0, sXc, sXeq, sRc].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Gas Separation Membrane Permeation & Selectivity</h3><p class="lead">Simulate solution-diffusion transport in cross-flow membrane modules: evaluate permeate purity and stage-cut trade-off.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Feed Pressure Phigh <span><output id="v-phigh">25.0</output> bar</span></label><input type="range" id="s-phigh" min="5.0" max="60.0" step="2.5" value="25.0"></div>' +
              '<div class="control-group"><label>Permeate Pressure Plow <span><output id="v-plow">1.2</output> bar</span></label><input type="range" id="s-plow" min="1.0" max="5.0" step="0.2" value="1.2"></div>' +
              '<div class="control-group"><label>Membrane Selectivity α <span><output id="v-alpha6">25.0</output></span></label><input type="range" id="s-alpha6" min="5.0" max="60.0" step="1.0" value="25.0"></div>' +
              '<div class="control-group"><label>Feed Mole Fraction zF <span><output id="v-zf">0.30</output></span></label><input type="range" id="s-zf" min="0.05" max="0.80" step="0.05" value="0.30"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Pressure Ratio rP</div><div class="readout-value" id="r-rp">20.8</div></div>' +
              '<div class="readout-card"><div class="readout-label">Permeate Purity yp</div><div class="readout-value" id="r-yp">88.4 mol%</div></div>' +
              '<div class="readout-card"><div class="readout-label">Enrichment Factor</div><div class="readout-value" id="r-enrich">2.95x</div></div>' +
              '<div class="readout-card"><div class="readout-label">Separation Limit</div><div class="readout-value" id="r-seplim">Selectivity Limited</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-mt6" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-mt6"></p>',
      init: function(el) {
        var sPhigh = el.querySelector('#s-phigh'), vPhigh = el.querySelector('#v-phigh');
        var sPlow = el.querySelector('#s-plow'), vPlow = el.querySelector('#v-plow');
        var sAlpha = el.querySelector('#s-alpha6'), vAlpha = el.querySelector('#v-alpha6');
        var sZf = el.querySelector('#s-zf'), vZf = el.querySelector('#v-zf');
        var rRp = el.querySelector('#r-rp'), rYp = el.querySelector('#r-yp');
        var rEnrich = el.querySelector('#r-enrich'), rSeplim = el.querySelector('#r-seplim');
        var svg = el.querySelector('#svg-mt6'), diag = el.querySelector('#diag-mt6');

        function update() {
          var Ph = parseFloat(sPhigh.value); vPhigh.textContent = f(Ph, 1);
          var Pl = parseFloat(sPlow.value); vPlow.textContent = f(Pl, 1);
          var alpha = parseFloat(sAlpha.value); vAlpha.textContent = f(alpha, 1);
          var zF = parseFloat(sZf.value); vZf.textContent = f(zF, 2);

          var rP = Ph / Pl;
          // Solution-diffusion binary crossflow permeate purity:
          // Quadratic solution for yp:
          var b = -(1 + (alpha - 1) * (1/rP + zF));
          var c = alpha * zF;
          // Simplified well-known membrane permeate equation:
          var yp = (alpha * zF) / (1 + (alpha - 1) * zF);
          // Attenuation by pressure ratio:
          var maxByPressure = (Ph - Pl) / Ph;
          yp = Math.min(0.99, yp * (1 - 1 / rP));

          var enrich = yp / zF;
          var sepLim = rP > alpha ? 'Selectivity Limited' : 'Pressure-Ratio Limited';

          rRp.textContent = f(rP, 1);
          rYp.textContent = f(yp * 100, 1) + ' mol%';
          rEnrich.textContent = f(enrich, 2) + 'x';
          rSeplim.textContent = sepLim;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="150" y="60" width="300" height="80" fill="#e0f2fe" stroke="#0284c7" stroke-width="2" rx="6"/>' +
                          '<line x1="150" y1="100" x2="450" y2="100" stroke="#0284c7" stroke-dasharray="6 3" stroke-width="3"/>' +
                          '<text x="300" y="90" text-anchor="middle" font-size="11" font-weight="700" fill="#0369a1">Selective Membrane (α = ' + f(alpha,0) + ')</text>' +
                          '<line x1="50" y1="80" x2="150" y2="80" stroke="#334155" stroke-width="4"/>' +
                          '<text x="100" y="70" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">Feed zF=' + f(zF,2) + '</text>' +
                          '<line x1="450" y1="80" x2="550" y2="80" stroke="#64748b" stroke-width="3"/>' +
                          '<text x="500" y="70" text-anchor="middle" font-size="11" fill="#475569">Retentate</text>' +
                          '<line x1="300" y1="140" x2="300" y2="180" stroke="#16a34a" stroke-width="4"/>' +
                          '<text x="300" y="195" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">Permeate yp = ' + f(yp*100,1) + ' mol%</text>' +
                          '<text x="300" y="35" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Membrane Module: ' + sepLim + '</text>';
          diag.textContent = 'Membrane gas separation: Transmembrane pressure ratio rP = ' + f(rP, 1) + '. Permeate purity = ' + f(yp * 100, 1) + ' mol% (Enrichment ' + f(enrich, 2) + 'x).';
        }
        [sPhigh, sPlow, sAlpha, sZf].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Particle Dissolution Kinetics & Leaching Mass Transfer</h3><p class="lead">Simulate solid-liquid dissolution (Noyes-Whitney model) and evaluate shrinking core particle lifetime in agitated leaching.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Particle Radius r0 <span><output id="v-rad">200</output> μm</span></label><input type="range" id="s-rad" min="50" max="800" step="25" value="200"></div>' +
              '<div class="control-group"><label>Solubility Cs <span><output id="v-cs">45.0</output> g/L</span></label><input type="range" id="s-cs" min="10.0" max="150.0" step="5.0" value="45.0"></div>' +
              '<div class="control-group"><label>Liquid Film Coeff kL <span><output id="v-kl">5.0e-5</output> m/s</span></label><input type="range" id="s-kl" min="1.0e-5" max="15.0e-5" step="0.5e-5" value="5.0e-5"></div>' +
              '<div class="control-group"><label>Bulk Conc Cb <span><output id="v-cb">5.0</output> g/L</span></label><input type="range" id="s-cb" min="0.0" max="35.0" step="2.5" value="5.0"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Driving Gradient ΔC</div><div class="readout-value" id="r-dc">40.0 g/L</div></div>' +
              '<div class="readout-card"><div class="readout-label">Dissolution Flux JA</div><div class="readout-value" id="r-ja">2.00 g/m²·s</div></div>' +
              '<div class="readout-card"><div class="readout-label">Dissolution Time ttot</div><div class="readout-value" id="r-tdiss">26.7 min</div></div>' +
              '<div class="readout-card"><div class="readout-label">Mass Transfer Regime</div><div class="readout-value" id="r-mreg">External Film Limited</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-mt7" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-mt7"></p>',
      init: function(el) {
        var sRad = el.querySelector('#s-rad'), vRad = el.querySelector('#v-rad');
        var sCs = el.querySelector('#s-cs'), vCs = el.querySelector('#v-cs');
        var sKl = el.querySelector('#s-kl'), vKl = el.querySelector('#v-kl');
        var sCb = el.querySelector('#s-cb'), vCb = el.querySelector('#v-cb');
        var rDc = el.querySelector('#r-dc'), rJa = el.querySelector('#r-ja');
        var rTdiss = el.querySelector('#r-tdiss'), rMreg = el.querySelector('#r-mreg');
        var svg = el.querySelector('#svg-mt7'), diag = el.querySelector('#diag-mt7');

        var rhoSolid = 1600; // kg/m3

        function update() {
          var r0_um = parseFloat(sRad.value); vRad.textContent = f(r0_um, 0);
          var Cs = parseFloat(sCs.value); vCs.textContent = f(Cs, 1);
          var kL = parseFloat(sKl.value); vKl.textContent = kL.toExponential(1);
          var Cb = parseFloat(sCb.value); vCb.textContent = f(Cb, 1);

          if (Cb >= Cs) Cb = Cs * 0.95;

          var r0 = r0_um * 1e-6; // m
          var dC = (Cs - Cb); // kg/m3 (g/L is same as kg/m3)
          var JA = kL * dC * 1000; // g/m2 s
          // Shrinking core dissolution time: t_tot = (rho * r0) / (kL * dC)
          var tSec = (rhoSolid * r0) / (kL * dC);
          var tMin = tSec / 60;

          rDc.textContent = f(dC, 1) + ' g/L';
          rJa.textContent = f(JA, 2) + ' g/m²·s';
          rTdiss.textContent = f(tMin, 1) + ' min';
          rMreg.textContent = 'External Film Limited';

          var pRad = Math.min(65, (r0_um / 800) * 65);

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<circle cx="300" cy="100" r="' + (pRad + 25) + '" fill="#bfdbfe" fill-opacity="0.3" stroke="#3b82f6" stroke-dasharray="4 4"/>' +
                          '<circle cx="300" cy="100" r="' + pRad + '" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>' +
                          '<text x="300" y="105" text-anchor="middle" font-size="11" font-weight="700" fill="#ffffff">Solid r0=' + f(r0_um,0) + 'μm</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Shrinking Core Dissolution Kinetics</text>' +
                          '<text x="300" y="180" text-anchor="middle" font-size="11" fill="#475569">Complete Dissolution Time = ' + f(tMin,1) + ' minutes | Flux = ' + f(JA,2) + ' g/m²·s</text>' +
                          '<text x="120" y="90" text-anchor="middle" font-size="11" fill="#64748b">Film ΔC = ' + f(dC,1) + ' g/L</text>' +
                          '<text x="480" y="90" text-anchor="middle" font-size="11" fill="#0284c7">kL = ' + kL.toExponential(1) + ' m/s</text>';
          diag.textContent = 'Solid dissolution model: Driving concentration gradient ΔC = ' + f(dC, 1) + ' g/L. Particle dissolution complete in ' + f(tMin, 1) + ' minutes.';
        }
        [sRad, sCs, sKl, sCb].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Packed Column Hydraulics & Generalized Flooding Limit</h3><p class="lead">Evaluate column diameter and pressure drop using the Generalized Pressure Drop Correlation (GPDC) at 70% flood.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Gas Mass Flow G <span><output id="v-gflow">2500</output> kg/h</span></label><input type="range" id="s-gflow" min="500" max="10000" step="250" value="2500"></div>' +
              '<div class="control-group"><label>Liquid Flow L <span><output id="v-lflow">8000</output> kg/h</span></label><input type="range" id="s-lflow" min="1000" max="30000" step="500" value="8000"></div>' +
              '<div class="control-group"><label>Packing Factor Fp <span><output id="v-fp8">65</output> m⁻¹</span></label><input type="range" id="s-fp8" min="20" max="250" step="5" value="65"></div>' +
              '<div class="control-group"><label>Gas Density ρG <span><output id="v-rhog">1.20</output> kg/m³</span></label><input type="range" id="s-rhog" min="0.80" max="3.00" step="0.10" value="1.20"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Flow Parameter FLV</div><div class="readout-value" id="r-flv">0.111</div></div>' +
              '<div class="readout-card"><div class="readout-label">Flooding Velocity</div><div class="readout-value" id="r-uflood">2.14 m/s</div></div>' +
              '<div class="readout-card"><div class="readout-label">Column Diameter D</div><div class="readout-value" id="r-dcol">0.70 m</div></div>' +
              '<div class="readout-card"><div class="readout-label">Pressure Drop ΔP/Z</div><div class="readout-value" id="r-dpz">325 Pa/m</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-mt8" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-mt8"></p>',
      init: function(el) {
        var sGflow = el.querySelector('#s-gflow'), vGflow = el.querySelector('#v-gflow');
        var sLflow = el.querySelector('#s-lflow'), vLflow = el.querySelector('#v-lflow');
        var sFp8 = el.querySelector('#s-fp8'), vFp8 = el.querySelector('#v-fp8');
        var sRhog = el.querySelector('#s-rhog'), vRhog = el.querySelector('#v-rhog');
        var rFlv = el.querySelector('#r-flv'), rUflood = el.querySelector('#r-uflood');
        var rDcol = el.querySelector('#r-dcol'), rDpz = el.querySelector('#r-dpz');
        var svg = el.querySelector('#svg-mt8'), diag = el.querySelector('#diag-mt8');

        var rhoL = 1000; // kg/m3

        function update() {
          var G_kgh = parseFloat(sGflow.value); vGflow.textContent = f(G_kgh, 0);
          var L_kgh = parseFloat(sLflow.value); vLflow.textContent = f(L_kgh, 0);
          var Fp = parseFloat(sFp8.value); vFp8.textContent = f(Fp, 0);
          var rhoG = parseFloat(sRhog.value); vRhog.textContent = f(rhoG, 2);

          var G = G_kgh / 3600; // kg/s
          var L = L_kgh / 3600; // kg/s
          var FLV = (L / G) * Math.sqrt(rhoG / rhoL);

          // Eckert GPDC approximation for flooding:
          var C_s_flood = 0.12 * Math.exp(-1.4 * Math.sqrt(FLV)) / Math.sqrt(Fp / 65);
          var u_flood = C_s_flood / Math.sqrt(rhoG / (rhoL - rhoG));
          u_flood = Math.max(0.5, Math.min(6.0, u_flood));

          var u_op = 0.70 * u_flood;
          var Q_gas = G / rhoG; // m3/s
          var Area = Q_gas / u_op;
          var Dcol = Math.sqrt((4 * Area) / Math.PI);
          var dP_Z = 200 + 150 * (u_op / u_flood); // Pa/m

          rFlv.textContent = f(FLV, 3);
          rUflood.textContent = f(u_flood, 2) + ' m/s';
          rDcol.textContent = f(Dcol, 2) + ' m';
          rDpz.textContent = f(dP_Z, 0) + ' Pa/m';

          var gaugeX = Math.min(480, Math.max(40, (0.70) * 480));

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="230" y="30" width="140" height="140" fill="#e2e8f0" stroke="#334155" stroke-width="2" rx="6"/>' +
                          '<text x="300" y="90" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Dcol = ' + f(Dcol,2) + ' m</text>' +
                          '<text x="300" y="115" text-anchor="middle" font-size="11" fill="#475569">uop = ' + f(u_op,2) + ' m/s (70% flood)</text>' +
                          '<text x="300" y="135" text-anchor="middle" font-size="11" font-weight="700" fill="#0284c7">ΔP = ' + f(dP_Z,0) + ' Pa/m</text>' +
                          '<text x="110" y="70" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Packed Tower</text>' +
                          '<text x="110" y="95" text-anchor="middle" font-size="11" fill="#64748b">G = ' + f(G_kgh,0) + ' kg/h</text>' +
                          '<text x="110" y="115" text-anchor="middle" font-size="11" fill="#64748b">L = ' + f(L_kgh,0) + ' kg/h</text>' +
                          '<text x="480" y="70" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Flooding Limit</text>' +
                          '<text x="480" y="95" text-anchor="middle" font-size="11" fill="#dc2626">uflood = ' + f(u_flood,2) + ' m/s</text>' +
                          '<text x="480" y="115" text-anchor="middle" font-size="11" fill="#15803d">Safety Margin: 30%</text>';
          diag.textContent = 'Column hydraulic design: Flow parameter FLV = ' + f(FLV, 3) + '. Operating at 70% flooding yields required column diameter D = ' + f(Dcol, 2) + ' m.';
        }
        [sGflow, sLflow, sFp8, sRhog].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    }
  ];
""" + get_engine_footer(8)

# =========================================================================
# 3. Separation Processes I
# =========================================================================
def build_sp1_sims():
    return """/* Separation Processes I Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Binary Vapor-Liquid Equilibrium (VLE) & Relative Volatility</h3><p class="lead">Simulate ideal and non-ideal binary VLE x-y curves and evaluate relative volatility α across liquid compositions.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Relative Volatility α <span><output id="v-alpha1">2.40</output></span></label><input type="range" id="s-alpha1" min="1.10" max="6.00" step="0.10" value="2.40"></div>' +
              '<div class="control-group"><label>Liquid Mole Fraction x <span><output id="v-xval">0.40</output></span></label><input type="range" id="s-xval" min="0.02" max="0.98" step="0.02" value="0.40"></div>' +
              '<div class="control-group"><label>Total Pressure P <span><output id="v-pvle">1.01</output> bar</span></label><input type="range" id="s-pvle" min="0.50" max="5.00" step="0.25" value="1.01"></div>' +
              '<div class="control-group"><label>Margules Non-Ideality A12 <span><output id="v-marga">0.00</output></span></label><input type="range" id="s-marga" min="-0.50" max="1.50" step="0.05" value="0.00"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Vapor Fraction y</div><div class="readout-value" id="r-yval">0.615</div></div>' +
              '<div class="readout-card"><div class="readout-label">Separation Spread y - x</div><div class="readout-value" id="r-spread">+0.215</div></div>' +
              '<div class="readout-card"><div class="readout-label">Azeotrope Check</div><div class="readout-value" id="r-azeo">Zeotropic (No Pinch)</div></div>' +
              '<div class="readout-card"><div class="readout-label">Separation Difficulty</div><div class="readout-value" id="r-diff">Moderate Distillation</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp11" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp11"></p>',
      init: function(el) {
        var sAlpha = el.querySelector('#s-alpha1'), vAlpha = el.querySelector('#v-alpha1');
        var sX = el.querySelector('#s-xval'), vX = el.querySelector('#v-xval');
        var sP = el.querySelector('#s-pvle'), vP = el.querySelector('#v-pvle');
        var sA = el.querySelector('#s-marga'), vA = el.querySelector('#v-marga');
        var rY = el.querySelector('#r-yval'), rSpread = el.querySelector('#r-spread');
        var rAzeo = el.querySelector('#r-azeo'), rDiff = el.querySelector('#r-diff');
        var svg = el.querySelector('#svg-sp11'), diag = el.querySelector('#diag-sp11');

        function update() {
          var alpha = parseFloat(sAlpha.value); vAlpha.textContent = f(alpha, 2);
          var x = parseFloat(sX.value); vX.textContent = f(x, 2);
          var P = parseFloat(sP.value); vP.textContent = f(P, 2);
          var A12 = parseFloat(sA.value); vA.textContent = f(A12, 2);

          // Compute y with Margules non-ideality correction
          var gamma1 = Math.exp(A12 * Math.pow(1 - x, 2));
          var gamma2 = Math.exp(A12 * Math.pow(x, 2));
          var effAlpha = alpha * (gamma1 / gamma2);

          var y = (effAlpha * x) / (1 + (effAlpha - 1) * x);
          y = Math.min(0.999, Math.max(0.001, y));
          var spread = y - x;

          var isAzeo = (A12 > 0.8 && alpha < 1.8);
          rY.textContent = f(y, 3);
          rSpread.textContent = (spread >= 0 ? '+' : '') + f(spread, 3);
          rAzeo.textContent = isAzeo ? 'Azeotropic Pinch' : 'Zeotropic (Clean Split)';
          rDiff.textContent = alpha > 3.0 ? 'Easy Separation' : (alpha > 1.5 ? 'Moderate Distillation' : 'Close-Boiling System');

          // Render x-y diagram
          var pts = [];
          for (var xStep = 0; xStep <= 1.0; xStep += 0.05) {
            var g1 = Math.exp(A12 * Math.pow(1 - xStep, 2));
            var g2 = Math.exp(A12 * Math.pow(xStep, 2));
            var aEff = alpha * (g1 / g2);
            var yS = (aEff * xStep) / (1 + (aEff - 1) * xStep);
            var px = 180 + xStep * 240;
            var py = 170 - yS * 130;
            pts.push(f(px,1) + ',' + f(py,1));
          }

          var curPx = 180 + x * 240;
          var curPy = 170 - y * 130;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="180" y="40" width="240" height="130" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>' +
                          '<line x1="180" y1="170" x2="420" y2="40" stroke="#cbd5e1" stroke-width="2"/>' +
                          '<polyline points="' + pts.join(' ') + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<circle cx="' + curPx + '" cy="' + curPy + '" r="6" fill="#dc2626"/>' +
                          '<text x="180" y="32" font-size="11" font-weight="700" fill="#0f172a">VLE x-y Diagram (α = ' + f(alpha,2) + ')</text>' +
                          '<text x="420" y="185" text-anchor="end" font-size="10" fill="#64748b">Liquid x →</text>' +
                          '<text x="175" y="45" text-anchor="end" font-size="10" fill="#64748b">Vapor y ↑</text>' +
                          '<text x="500" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="#dc2626">x = ' + f(x,2) + '</text>' +
                          '<text x="500" y="115" text-anchor="middle" font-size="12" font-weight="700" fill="#2563eb">y = ' + f(y,3) + '</text>';
          diag.textContent = 'VLE equilibrium: For liquid fraction x = ' + f(x, 2) + ', vapor mole fraction y = ' + f(y, 3) + ' (Driving spread y - x = ' + f(spread, 3) + ').';
        }
        [sAlpha, sX, sP, sA].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Rachford-Rice Single-Stage Equilibrium Flash Drum</h3><p class="lead">Solve the Rachford-Rice equation for vapor fraction V/F, vapor product yD, and liquid bottoms xB in flash distillation.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Feed Vapor Fraction V/F <span><output id="v-vf">0.45</output></span></label><input type="range" id="s-vf" min="0.05" max="0.95" step="0.05" value="0.45"></div>' +
              '<div class="control-group"><label>Relative Volatility α <span><output id="v-alpha2">3.00</output></span></label><input type="range" id="s-alpha2" min="1.20" max="6.00" step="0.10" value="3.00"></div>' +
              '<div class="control-group"><label>Feed Composition zF <span><output id="v-zf2">0.50</output></span></label><input type="range" id="s-zf2" min="0.10" max="0.90" step="0.05" value="0.50"></div>' +
              '<div class="control-group"><label>Feed Flow Rate F <span><output id="v-fflow">100</output> kmol/h</span></label><input type="range" id="s-fflow" min="20" max="500" step="10" value="100"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Vapor Product yD</div><div class="readout-value" id="r-yd">0.710</div></div>' +
              '<div class="readout-card"><div class="readout-label">Liquid Bottoms xB</div><div class="readout-value" id="r-xb">0.328</div></div>' +
              '<div class="readout-card"><div class="readout-label">Light Key Recovery</div><div class="readout-value" id="r-rec2">63.9 %</div></div>' +
              '<div class="readout-card"><div class="readout-label">Vapor Overhead V</div><div class="readout-value" id="r-vflow">45.0 kmol/h</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp12" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp12"></p>',
      init: function(el) {
        var sVf = el.querySelector('#s-vf'), vVf = el.querySelector('#v-vf');
        var sAlpha = el.querySelector('#s-alpha2'), vAlpha = el.querySelector('#v-alpha2');
        var sZf = el.querySelector('#s-zf2'), vZf = el.querySelector('#v-zf2');
        var sF = el.querySelector('#s-fflow'), vF = el.querySelector('#v-fflow');
        var rYd = el.querySelector('#r-yd'), rXb = el.querySelector('#r-xb');
        var rRec = el.querySelector('#r-rec2'), rVflow = el.querySelector('#r-vflow');
        var svg = el.querySelector('#svg-sp12'), diag = el.querySelector('#diag-sp12');

        function update() {
          var psi = parseFloat(sVf.value); vVf.textContent = f(psi, 2);
          var alpha = parseFloat(sAlpha.value); vAlpha.textContent = f(alpha, 2);
          var zF = parseFloat(sZf.value); vZf.textContent = f(zF, 2);
          var F = parseFloat(sF.value); vF.textContent = f(F, 0);

          // Rachford-Rice analytical solution for binary flash:
          // xB = zF / (1 + psi * (alpha - 1)), yD = alpha * xB / (1 + (alpha - 1)*xB)
          // Exact binary material balance with V/F = psi:
          // zF = psi * yD + (1 - psi) * xB, where yD = alpha*xB / (1 + (alpha-1)*xB)
          // Solved for xB:
          var A_q = (1 - psi) * (alpha - 1);
          var B_q = 1 + psi * (alpha - 1) - zF * (alpha - 1);
          var C_q = -zF;

          var xB = (-B_q + Math.sqrt(Math.max(0.001, B_q * B_q - 4 * A_q * C_q))) / (2 * Math.max(0.001, A_q));
          xB = Math.min(0.99, Math.max(0.01, xB));
          var yD = (alpha * xB) / (1 + (alpha - 1) * xB);
          var V = psi * F;
          var L = (1 - psi) * F;
          var recovery = (V * yD) / (F * zF) * 100;

          rYd.textContent = f(yD, 3);
          rXb.textContent = f(xB, 3);
          rRec.textContent = f(recovery, 1) + ' %';
          rVflow.textContent = f(V, 1) + ' kmol/h';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="240" y="40" width="120" height="120" fill="#e2e8f0" stroke="#334155" stroke-width="2" rx="20"/>' +
                          '<rect x="240" y="100" width="120" height="60" fill="#0284c7" fill-opacity="0.25" rx="0 0 20 20"/>' +
                          '<line x1="80" y1="90" x2="240" y2="90" stroke="#0f172a" stroke-width="4"/>' +
                          '<text x="150" y="80" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">Feed F=' + f(F,0) + ' (z=' + f(zF,2) + ')</text>' +
                          '<line x1="300" y1="40" x2="300" y2="15" stroke="#ef4444" stroke-width="3"/>' +
                          '<text x="310" y="25" font-size="11" font-weight="700" fill="#dc2626">Vapor V=' + f(V,1) + ' (y=' + f(yD,3) + ')</text>' +
                          '<line x1="300" y1="160" x2="300" y2="185" stroke="#2563eb" stroke-width="3"/>' +
                          '<text x="310" y="180" font-size="11" font-weight="700" fill="#1e40af">Bottoms L=' + f(L,1) + ' (x=' + f(xB,3) + ')</text>' +
                          '<text x="110" y="150" text-anchor="middle" font-size="12" font-weight="700" fill="#15803d">Recovery: ' + f(recovery,1) + '%</text>';
          diag.textContent = 'Flash balance: V/F = ' + f(psi, 2) + '. Overhead vapor yD = ' + f(yD, 3) + ' (' + f(V, 1) + ' kmol/h); Bottoms liquid xB = ' + f(xB, 3) + ' (' + f(L, 1) + ' kmol/h).';
        }
        [sVf, sAlpha, sZf, sF].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>McCabe-Thiele Binary Distillation Graphical Solver</h3><p class="lead">Interactively compute theoretical stage count, minimum reflux Rmin, and feed tray location across reflux ratios.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Reflux Ratio R = L/D <span><output id="v-rr">2.50</output></span></label><input type="range" id="s-rr" min="0.80" max="8.00" step="0.10" value="2.50"></div>' +
              '<div class="control-group"><label>Distillate Purity xD <span><output id="v-xd">0.95</output></span></label><input type="range" id="s-xd" min="0.85" max="0.99" step="0.01" value="0.95"></div>' +
              '<div class="control-group"><label>Bottoms Purity xB <span><output id="v-xb3">0.05</output></span></label><input type="range" id="s-xb3" min="0.01" max="0.15" step="0.01" value="0.05"></div>' +
              '<div class="control-group"><label>Feed Quality q <span><output id="v-qval">1.00</output></span></label><input type="range" id="s-qval" min="0.50" max="1.50" step="0.05" value="1.00"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Min Reflux Rmin</div><div class="readout-value" id="r-rmin">1.28</div></div>' +
              '<div class="readout-card"><div class="readout-label">Operating R/Rmin</div><div class="readout-value" id="r-rovr">1.95</div></div>' +
              '<div class="readout-card"><div class="readout-label">Theoretical Stages</div><div class="readout-value" id="r-nstages">9 Stages</div></div>' +
              '<div class="readout-card"><div class="readout-label">Optimum Feed Stage</div><div class="readout-value" id="r-feedtray">Stage 5</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp13" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp13"></p>',
      init: function(el) {
        var sRr = el.querySelector('#s-rr'), vRr = el.querySelector('#v-rr');
        var sXd = el.querySelector('#s-xd'), vXd = el.querySelector('#v-xd');
        var sXb = el.querySelector('#s-xb3'), vXb = el.querySelector('#v-xb3');
        var sQ = el.querySelector('#s-qval'), vQ = el.querySelector('#v-qval');
        var rRmin = el.querySelector('#r-rmin'), rRovr = el.querySelector('#r-rovr');
        var rNstages = el.querySelector('#r-nstages'), rFeedtray = el.querySelector('#r-feedtray');
        var svg = el.querySelector('#svg-sp13'), diag = el.querySelector('#diag-sp13');

        var alpha = 2.5; // binary relative volatility
        var zF = 0.50;

        function update() {
          var R = parseFloat(sRr.value); vRr.textContent = f(R, 2);
          var xD = parseFloat(sXd.value); vXd.textContent = f(xD, 2);
          var xB = parseFloat(sXb.value); vXb.textContent = f(xB, 2);
          var q = parseFloat(sQ.value); vQ.textContent = f(q, 2);

          // Pinch calculation for Rmin:
          var xPinch = zF;
          var yPinch = (alpha * xPinch) / (1 + (alpha - 1) * xPinch);
          var Rmin = (xD - yPinch) / Math.max(0.01, (yPinch - xPinch));
          Rmin = Math.max(0.5, Rmin);
          var rOvr = R / Rmin;

          // Empirical Gilliland-style stage count:
          var Nmin = Math.log((xD / (1 - xD)) * ((1 - xB) / xB)) / Math.log(alpha);
          var N = Math.ceil(Nmin / (1 - Math.exp(-1.2 * (rOvr - 1) / Math.max(0.1, rOvr))) + 1);
          N = Math.min(30, Math.max(Math.ceil(Nmin), N));
          var feedTray = Math.ceil(N * 0.55);

          rRmin.textContent = f(Rmin, 2);
          rRovr.textContent = f(rOvr, 2);
          rNstages.textContent = N + ' Stages';
          rFeedtray.textContent = 'Stage ' + feedTray;

          // Plot McCabe-Thiele construction
          var pts = [];
          for (var xS = 0; xS <= 1.0; xS += 0.05) {
            var yS = (alpha * xS) / (1 + (alpha - 1) * xS);
            pts.push(f(180 + xS * 240, 1) + ',' + f(170 - yS * 130, 1));
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="180" y="40" width="240" height="130" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>' +
                          '<line x1="180" y1="170" x2="420" y2="40" stroke="#cbd5e1" stroke-width="2"/>' +
                          '<polyline points="' + pts.join(' ') + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<line x1="' + (180 + xD*240) + '" y1="' + (170 - xD*130) + '" x2="' + (180 + zF*240) + '" y2="' + (170 - (R/(R+1)*zF + xD/(R+1))*130) + '" stroke="#ef4444" stroke-width="2"/>' +
                          '<text x="180" y="30" font-size="12" font-weight="700" fill="#0f172a">McCabe-Thiele: ' + N + ' Stages (R = ' + f(R,2) + ')</text>' +
                          '<text x="500" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="#dc2626">Rmin = ' + f(Rmin,2) + '</text>' +
                          '<text x="500" y="105" text-anchor="middle" font-size="11" fill="#475569">R/Rmin = ' + f(rOvr,2) + '</text>' +
                          '<text x="500" y="130" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">Feed: Tray ' + feedTray + '</text>';
          diag.textContent = 'McCabe-Thiele staging: Minimum reflux Rmin = ' + f(Rmin, 2) + '. At operating R = ' + f(R, 2) + ', system requires ' + N + ' theoretical equilibrium stages.';
        }
        [sRr, sXd, sXb, sQ].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Sieve Tray Hydraulic Envelope (Flooding, Weeping, Pressure Drop)</h3><p class="lead">Simulate distillation column internal hydraulics: assess weeping, jet flooding, downcomer backup, and allowable operating window.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Vapor Velocity uv <span><output id="v-uv">1.10</output> m/s</span></label><input type="range" id="s-uv" min="0.30" max="2.50" step="0.05" value="1.10"></div>' +
              '<div class="control-group"><label>Liquid Loading QL/W <span><output id="v-qlw">25.0</output> m³/h·m</span></label><input type="range" id="s-qlw" min="5.0" max="70.0" step="2.5" value="25.0"></div>' +
              '<div class="control-group"><label>Tray Spacing Ht <span><output id="v-ht">500</output> mm</span></label><input type="range" id="s-ht" min="300" max="800" step="50" value="500"></div>' +
              '<div class="control-group"><label>Weir Height hw <span><output id="v-hw">50</output> mm</span></label><input type="range" id="s-hw" min="25" max="80" step="5" value="50"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Tray Total ΔP</div><div class="readout-value" id="r-dptray">78 mm liq</div></div>' +
              '<div class="readout-card"><div class="readout-label">Downcomer Backup</div><div class="readout-value" id="r-dcback">185 mm</div></div>' +
              '<div class="readout-card"><div class="readout-label">Jet Flooding %</div><div class="readout-value" id="r-jetf">68.2 %</div></div>' +
              '<div class="readout-card"><div class="readout-label">Hydraulic Regime</div><div class="readout-value" id="r-hreg">Stable Operation</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp14" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp14"></p>',
      init: function(el) {
        var sUv = el.querySelector('#s-uv'), vUv = el.querySelector('#v-uv');
        var sQlw = el.querySelector('#s-qlw'), vQlw = el.querySelector('#v-qlw');
        var sHt = el.querySelector('#s-ht'), vHt = el.querySelector('#v-ht');
        var sHw = el.querySelector('#s-hw'), vHw = el.querySelector('#v-hw');
        var rDptray = el.querySelector('#r-dptray'), rDcback = el.querySelector('#r-dcback');
        var rJetf = el.querySelector('#r-jetf'), rHreg = el.querySelector('#r-hreg');
        var svg = el.querySelector('#svg-sp14'), diag = el.querySelector('#diag-sp14');

        function update() {
          var uv = parseFloat(sUv.value); vUv.textContent = f(uv, 2);
          var qL = parseFloat(sQlw.value); vQlw.textContent = f(qL, 1);
          var Ht = parseFloat(sHt.value); vHt.textContent = f(Ht, 0);
          var hw = parseFloat(sHw.value); vHw.textContent = f(hw, 0);

          var h_dry = 25 * Math.pow(uv, 2); // mm liquid
          var h_ow = 1.2 * Math.pow(qL, 0.67); // crest over weir
          var h_liq = 0.5 * (hw + h_ow);
          var h_total = h_dry + h_liq;
          var h_dc = 2 * h_total + 10;
          var jetFlood = (uv / (0.07 * Math.sqrt(Ht))) * 100;
          jetFlood = Math.min(130, Math.max(10, jetFlood));

          var regime = 'Stable Operation';
          if (uv < 0.50) regime = 'Weeping Detected';
          else if (jetFlood > 85) regime = 'Entrainment / Jet Flooding';
          else if (h_dc > 0.5 * Ht) regime = 'Downcomer Choking';

          rDptray.textContent = f(h_total, 0) + ' mm liq';
          rDcback.textContent = f(h_dc, 0) + ' mm';
          rJetf.textContent = f(jetFlood, 1) + ' %';
          rHreg.textContent = regime;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="160" y="40" width="280" height="120" fill="#f1f5f9" stroke="#334155" stroke-width="2" rx="4"/>' +
                          '<line x1="160" y1="110" x2="400" y2="110" stroke="#0284c7" stroke-width="4"/>' +
                          '<rect x="400" y="80" width="10" height="30" fill="#0369a1"/>' +
                          '<rect x="410" y="60" width="30" height="90" fill="#bfdbfe" stroke="#3b82f6" stroke-width="1"/>' +
                          '<text x="425" y="105" text-anchor="middle" font-size="9" fill="#1e40af" transform="rotate(-90 425 105)">Downcomer</text>' +
                          '<text x="280" y="85" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Active Tray Floor</text>' +
                          '<text x="280" y="140" text-anchor="middle" font-size="11" font-weight="700" fill="' + (regime === 'Stable Operation' ? '#15803d' : '#dc2626') + '">' + regime + '</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Tray Hydraulics (Jet Flood = ' + f(jetFlood,1) + '%)</text>';
          diag.textContent = 'Hydraulic status: Tray total pressure drop = ' + f(h_total, 0) + ' mm liquid. Downcomer backup = ' + f(h_dc, 0) + ' mm (' + f(h_dc / Ht * 100, 1) + '% of tray spacing). ' + regime + '.';
        }
        [sUv, sQlw, sHt, sHw].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Multicomponent Distillation Fenske-Underwood-Gilliland Solver</h3><p class="lead">Simulate multicomponent fractionation: calculate minimum stages Nmin, minimum reflux Rmin, and actual tray count.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Light Key Volatility αLK <span><output id="v-alk">2.20</output></span></label><input type="range" id="s-alk" min="1.30" max="4.00" step="0.10" value="2.20"></div>' +
              '<div class="control-group"><label>LK Recovery in Overhead <span><output id="v-lrec">98.0</output> %</span></label><input type="range" id="s-lrec" min="90.0" max="99.9" step="0.5" value="98.0"></div>' +
              '<div class="control-group"><label>HK Recovery in Bottoms <span><output id="v-hrec">98.0</output> %</span></label><input type="range" id="s-hrec" min="90.0" max="99.9" step="0.5" value="98.0"></div>' +
              '<div class="control-group"><label>Reflux Factor R/Rmin <span><output id="v-rf5">1.30</output></span></label><input type="range" id="s-rf5" min="1.05" max="2.50" step="0.05" value="1.30"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Fenske Nmin</div><div class="readout-value" id="r-nmin">9.8 Stages</div></div>' +
              '<div class="readout-card"><div class="readout-label">Underwood Rmin</div><div class="readout-value" id="r-umin">1.45</div></div>' +
              '<div class="readout-card"><div class="readout-label">Operating Reflux R</div><div class="readout-value" id="r-ropt">1.89</div></div>' +
              '<div class="readout-card"><div class="readout-label">Actual Gilliland N</div><div class="readout-value" id="r-nact">18 Stages</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp15" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp15"></p>',
      init: function(el) {
        var sAlk = el.querySelector('#s-alk'), vAlk = el.querySelector('#v-alk');
        var sLrec = el.querySelector('#s-lrec'), vLrec = el.querySelector('#v-lrec');
        var sHrec = el.querySelector('#s-hrec'), vHrec = el.querySelector('#v-hrec');
        var sRf = el.querySelector('#s-rf5'), vRf = el.querySelector('#v-rf5');
        var rNmin = el.querySelector('#r-nmin'), rUmin = el.querySelector('#r-umin');
        var rRopt = el.querySelector('#r-ropt'), rNact = el.querySelector('#r-nact');
        var svg = el.querySelector('#svg-sp15'), diag = el.querySelector('#diag-sp15');

        function update() {
          var aLK = parseFloat(sAlk.value); vAlk.textContent = f(aLK, 2);
          var recL = parseFloat(sLrec.value) / 100; vLrec.textContent = f(recL * 100, 1);
          var recH = parseFloat(sHrec.value) / 100; vHrec.textContent = f(recH * 100, 1);
          var rf = parseFloat(sRf.value); vRf.textContent = f(rf, 2);

          // Fenske minimum stages:
          var d_b_LK = recL / (1 - recL);
          var b_d_HK = recH / (1 - recH);
          var Nmin = Math.log(d_b_LK * b_d_HK) / Math.log(aLK);

          // Underwood minimum reflux (approximate for typical equimolar feed):
          var Rmin = 1 / (aLK - 1) * 1.5;
          var R = rf * Rmin;

          // Gilliland correlation:
          var Xg = (R - Rmin) / (R + 1);
          var Yg = 1 - Math.exp((1 + 54.4 * Xg) / (11 + 117.2 * Xg) * (Xg - 1) / Math.sqrt(Xg));
          var N = Math.ceil(Nmin + Yg * Nmin * 1.8);
          N = Math.max(Math.ceil(Nmin) + 1, N);

          rNmin.textContent = f(Nmin, 1) + ' Stages';
          rUmin.textContent = f(Rmin, 2);
          rRopt.textContent = f(R, 2);
          rNact.textContent = N + ' Stages';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="250" y="30" width="100" height="140" fill="#f1f5f9" stroke="#334155" stroke-width="2" rx="10"/>' +
                          '<text x="300" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">FUG Sizing</text>' +
                          '<text x="300" y="105" text-anchor="middle" font-size="14" font-weight="800" fill="#0284c7">' + N + ' Stages</text>' +
                          '<text x="300" y="130" text-anchor="middle" font-size="11" fill="#475569">R = ' + f(R,2) + '</text>' +
                          '<line x1="160" y1="100" x2="250" y2="100" stroke="#0f172a" stroke-width="3"/>' +
                          '<text x="140" y="105" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a">Multicomponent Feed</text>' +
                          '<text x="110" y="45" font-size="12" font-weight="700" fill="#dc2626">Fenske Nmin: ' + f(Nmin,1) + '</text>' +
                          '<text x="110" y="65" font-size="12" font-weight="700" fill="#2563eb">Underwood Rmin: ' + f(Rmin,2) + '</text>' +
                          '<text x="430" y="45" font-size="11" fill="#64748b">LK Split: ' + f(recL*100,1) + '%</text>' +
                          '<text x="430" y="65" font-size="11" fill="#64748b">HK Split: ' + f(recH*100,1) + '%</text>';
          diag.textContent = 'FUG shortcut distillation: Minimum stages Nmin = ' + f(Nmin, 1) + '. Minimum reflux Rmin = ' + f(Rmin, 2) + '. At R/Rmin = ' + f(rf, 2) + ', total actual trays = ' + N + '.';
        }
        [sAlk, sLrec, sHrec, sRf].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Staged Countercurrent Absorption & Stripping Column</h3><p class="lead">Simulate stage-by-stage gas absorption using Kremser algebraic analysis: evaluate recovery and solvent usage.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Inlet Gas Mole Frac y1 <span><output id="v-y1">0.060</output></span></label><input type="range" id="s-y1" min="0.010" max="0.150" step="0.005" value="0.060"></div>' +
              '<div class="control-group"><label>Liquid Flow L <span><output id="v-l6">120</output> kmol/h</span></label><input type="range" id="s-l6" min="30" max="400" step="10" value="120"></div>' +
              '<div class="control-group"><label>Gas Flow G <span><output id="v-g6">80</output> kmol/h</span></label><input type="range" id="s-g6" min="20" max="300" step="10" value="80"></div>' +
              '<div class="control-group"><label>Number of Trays N <span><output id="v-ntrays">6</output></span></label><input type="range" id="s-ntrays" min="2" max="15" step="1" value="6"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Absorption Factor A</div><div class="readout-value" id="r-a6">1.50</div></div>' +
              '<div class="readout-card"><div class="readout-label">Clean Gas yN+1</div><div class="readout-value" id="r-yexit">0.0031</div></div>' +
              '<div class="readout-card"><div class="readout-label">Solute Absorption %</div><div class="readout-value" id="r-abs6">94.8 %</div></div>' +
              '<div class="readout-card"><div class="readout-label">Rich Solvent x1</div><div class="readout-value" id="r-xrich">0.038</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp16" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp16"></p>',
      init: function(el) {
        var sY1 = el.querySelector('#s-y1'), vY1 = el.querySelector('#v-y1');
        var sL = el.querySelector('#s-l6'), vL = el.querySelector('#v-l6');
        var sG = el.querySelector('#s-g6'), vG = el.querySelector('#v-g6');
        var sN = el.querySelector('#s-ntrays'), vN = el.querySelector('#v-ntrays');
        var rA = el.querySelector('#r-a6'), rYexit = el.querySelector('#r-yexit');
        var rAbs = el.querySelector('#r-abs6'), rXrich = el.querySelector('#r-xrich');
        var svg = el.querySelector('#svg-sp16'), diag = el.querySelector('#diag-sp16');

        var m = 1.0; // Henry equilibrium constant

        function update() {
          var y1 = parseFloat(sY1.value); vY1.textContent = f(y1, 3);
          var L = parseFloat(sL.value); vL.textContent = f(L, 0);
          var G = parseFloat(sG.value); vG.textContent = f(G, 0);
          var N = parseInt(sN.value, 10); vN.textContent = N;

          var A = L / (m * G);
          var recovery = 0;
          if (Math.abs(A - 1.0) < 0.01) {
            recovery = N / (N + 1);
          } else {
            recovery = (Math.pow(A, N + 1) - A) / (Math.pow(A, N + 1) - 1);
          }
          recovery = Math.max(0.01, Math.min(0.999, recovery));

          var y_exit = y1 * (1 - recovery);
          var absorbed = G * (y1 - y_exit);
          var x_rich = absorbed / L;

          rA.textContent = f(A, 2);
          rYexit.textContent = f(y_exit, 4);
          rAbs.textContent = f(recovery * 100, 1) + ' %';
          rXrich.textContent = f(x_rich, 3);

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="230" y="30" width="140" height="140" fill="#e0f2fe" stroke="#0284c7" stroke-width="2" rx="8"/>' +
                          '<text x="300" y="70" text-anchor="middle" font-size="13" font-weight="700" fill="#0369a1">Tray Absorber</text>' +
                          '<text x="300" y="95" text-anchor="middle" font-size="15" font-weight="800" fill="#0284c7">' + N + ' Equilibrium Trays</text>' +
                          '<text x="300" y="125" text-anchor="middle" font-size="12" font-weight="700" fill="#15803d">Recovery: ' + f(recovery*100,1) + '%</text>' +
                          '<line x1="120" y1="150" x2="230" y2="150" stroke="#334155" stroke-width="3"/>' +
                          '<text x="110" y="145" text-anchor="end" font-size="10" font-weight="700" fill="#334155">Inlet Gas y1=' + f(y1,3) + '</text>' +
                          '<line x1="370" y1="50" x2="480" y2="50" stroke="#16a34a" stroke-width="3"/>' +
                          '<text x="485" y="55" font-size="10" font-weight="700" fill="#15803d">Clean Gas y=' + f(y_exit,4) + '</text>';
          diag.textContent = 'Staged column Kremser equation: Absorption factor A = ' + f(A, 2) + '. With ' + N + ' trays, solute removal is ' + f(recovery * 100, 1) + '%.';
        }
        [sY1, sL, sG, sN].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Liquid-Liquid Extraction (LLE) & Solvent-to-Feed Ratio</h3><p class="lead">Simulate staged countercurrent extraction: evaluate solute recovery and raffinate purity across solvent flow rates.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Solvent-to-Feed Ratio S/F <span><output id="v-sf">1.20</output></span></label><input type="range" id="s-sf" min="0.30" max="3.50" step="0.10" value="1.20"></div>' +
              '<div class="control-group"><label>Distribution Coeff KD <span><output id="v-kd">2.50</output></span></label><input type="range" id="s-kd" min="0.50" max="8.00" step="0.25" value="2.50"></div>' +
              '<div class="control-group"><label>Extraction Stages N <span><output id="v-nstg">4</output></span></label><input type="range" id="s-nstg" min="1" max="8" step="1" value="4"></div>' +
              '<div class="control-group"><label>Feed Solute Conc xF <span><output id="v-xf7">0.12</output> wt%</span></label><input type="range" id="s-xf7" min="0.02" max="0.30" step="0.01" value="0.12"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Extraction Factor E</div><div class="readout-value" id="r-efact">3.00</div></div>' +
              '<div class="readout-card"><div class="readout-label">Raffinate Conc xN</div><div class="readout-value" id="r-xraf">0.0015 wt%</div></div>' +
              '<div class="readout-card"><div class="readout-label">Extraction Recovery</div><div class="readout-value" id="r-extrec">98.8 %</div></div>' +
              '<div class="readout-card"><div class="readout-label">Extract Purity y1</div><div class="readout-value" id="r-yext">0.099 wt%</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp17" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp17"></p>',
      init: function(el) {
        var sSf = el.querySelector('#s-sf'), vSf = el.querySelector('#v-sf');
        var sKd = el.querySelector('#s-kd'), vKd = el.querySelector('#v-kd');
        var sN = el.querySelector('#s-nstg'), vN = el.querySelector('#v-nstg');
        var sXf = el.querySelector('#s-xf7'), vXf = el.querySelector('#v-xf7');
        var rE = el.querySelector('#r-efact'), rXraf = el.querySelector('#r-xraf');
        var rRec = el.querySelector('#r-extrec'), rYext = el.querySelector('#r-yext');
        var svg = el.querySelector('#svg-sp17'), diag = el.querySelector('#diag-sp17');

        function update() {
          var SF = parseFloat(sSf.value); vSf.textContent = f(SF, 2);
          var KD = parseFloat(sKd.value); vKd.textContent = f(KD, 2);
          var N = parseInt(sN.value, 10); vN.textContent = N;
          var xF = parseFloat(sXf.value); vXf.textContent = f(xF, 3);

          var E = KD * SF;
          var unrecovered = 0;
          if (Math.abs(E - 1.0) < 0.01) {
            unrecovered = 1 / (N + 1);
          } else {
            unrecovered = (E - 1) / (Math.pow(E, N + 1) - 1);
          }
          unrecovered = Math.max(0.001, Math.min(0.999, unrecovered));
          var rec = (1 - unrecovered) * 100;
          var xN = xF * unrecovered;
          var y1 = (xF - xN) / SF;

          rE.textContent = f(E, 2);
          rXraf.textContent = f(xN, 4) + ' wt%';
          rRec.textContent = f(rec, 1) + ' %';
          rYext.textContent = f(y1, 3) + ' wt%';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="180" y="50" width="240" height="100" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="8"/>' +
                          '<text x="300" y="85" text-anchor="middle" font-size="13" font-weight="700" fill="#92400e">LLE Cascade (' + N + ' Stages)</text>' +
                          '<text x="300" y="110" text-anchor="middle" font-size="12" fill="#b45309">Extraction Factor E = ' + f(E,2) + '</text>' +
                          '<text x="300" y="130" text-anchor="middle" font-size="12" font-weight="800" fill="#15803d">Recovery: ' + f(rec,1) + '%</text>' +
                          '<line x1="60" y1="80" x2="180" y2="80" stroke="#0284c7" stroke-width="4"/>' +
                          '<text x="120" y="70" text-anchor="middle" font-size="11" font-weight="700" fill="#0369a1">Feed xF=' + f(xF,2) + '</text>' +
                          '<line x1="420" y1="80" x2="540" y2="80" stroke="#059669" stroke-width="3"/>' +
                          '<text x="480" y="70" text-anchor="middle" font-size="11" fill="#047857">Raffinate xN=' + f(xN,4) + '</text>';
          diag.textContent = 'Countercurrent liquid extraction: Extraction factor E = KD·(S/F) = ' + f(E, 2) + '. Solute extraction recovery = ' + f(rec, 1) + '% across ' + N + ' stages.';
        }
        [sSf, sKd, sN, sXf].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Distillation Sequence Synthesis & Energy Minimization</h3><p class="lead">Compare Direct vs. Indirect separation sequences for ternary mixtures and quantify vapor recompression energy savings.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Feed Comp A (Light) <span><output id="v-za">0.40</output></span></label><input type="range" id="s-za" min="0.10" max="0.70" step="0.05" value="0.40"></div>' +
              '<div class="control-group"><label>Feed Comp B (Middle) <span><output id="v-zb">0.35</output></span></label><input type="range" id="s-zb" min="0.10" max="0.60" step="0.05" value="0.35"></div>' +
              '<div class="control-group"><label>Energy Price <span><output id="v-eprice">12.0</output> $/GJ</span></label><input type="range" id="s-eprice" min="4.0" max="25.0" step="1.0" value="12.0"></div>' +
              '<div class="control-group"><label>Vapor Recompression <span><output id="v-vrecomp">Enabled</output></span></label><input type="range" id="s-vrecomp" min="0" max="1" step="1" value="1"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Direct Sequence Duty</div><div class="readout-value" id="r-qdir">5.80 MW</div></div>' +
              '<div class="readout-card"><div class="readout-label">Indirect Sequence Duty</div><div class="readout-value" id="r-qindir">6.45 MW</div></div>' +
              '<div class="readout-card"><div class="readout-label">Optimal Sequence</div><div class="readout-value" id="r-optseq">Direct Train Optimal</div></div>' +
              '<div class="readout-card"><div class="readout-label">Annual Savings</div><div class="readout-value" id="r-asave">$482,000 /yr</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp18" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp18"></p>',
      init: function(el) {
        var sZa = el.querySelector('#s-za'), vZa = el.querySelector('#v-za');
        var sZb = el.querySelector('#s-zb'), vZb = el.querySelector('#v-zb');
        var sEp = el.querySelector('#s-eprice'), vEp = el.querySelector('#v-eprice');
        var sVr = el.querySelector('#s-vrecomp'), vVr = el.querySelector('#v-vrecomp');
        var rQdir = el.querySelector('#r-qdir'), rQindir = el.querySelector('#r-qindir');
        var rOptseq = el.querySelector('#r-optseq'), rAsave = el.querySelector('#r-asave');
        var svg = el.querySelector('#svg-sp18'), diag = el.querySelector('#diag-sp18');

        function update() {
          var zA = parseFloat(sZa.value); vZa.textContent = f(zA, 2);
          var zB = parseFloat(sZb.value); vZb.textContent = f(zB, 2);
          var ep = parseFloat(sEp.value); vEp.textContent = f(ep, 1);
          var vr = parseInt(sVr.value, 10); vVr.textContent = vr ? 'Enabled' : 'Disabled';

          var zC = Math.max(0.05, 1 - zA - zB);

          // Energy heuristics: Direct takes A off first; Indirect takes C off first
          var qDir = 4.0 * zA + 6.0 * (zB + zC);
          var qIndir = 4.0 * zC + 6.0 * (zA + zB);

          var vrcFactor = vr ? 0.65 : 1.0;
          qDir *= vrcFactor;
          qIndir *= vrcFactor;

          var opt = qDir <= qIndir ? 'Direct Sequence Optimal' : 'Indirect Sequence Optimal';
          var bestQ = Math.min(qDir, qIndir);
          var annualCost = bestQ * 3600 * 8000 * 1e-3 * ep; // $ / yr
          var savings = vr ? (bestQ / 0.65 - bestQ) * 3600 * 8000 * 1e-3 * ep : 0;

          rQdir.textContent = f(qDir, 2) + ' MW';
          rQindir.textContent = f(qIndir, 2) + ' MW';
          rOptseq.textContent = opt;
          rAsave.textContent = '$' + f(savings, 0) + ' /yr';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="100" y="50" width="160" height="90" fill="#dbeafe" stroke="#2563eb" stroke-width="2" rx="6"/>' +
                          '<text x="180" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="#1e40af">Direct Sequence</text>' +
                          '<text x="180" y="105" text-anchor="middle" font-size="13" font-weight="800" fill="#0284c7">' + f(qDir,2) + ' MW</text>' +
                          '<rect x="340" y="50" width="160" height="90" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="6"/>' +
                          '<text x="420" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="#92400e">Indirect Sequence</text>' +
                          '<text x="420" y="105" text-anchor="middle" font-size="13" font-weight="800" fill="#b45309">' + f(qIndir,2) + ' MW</text>' +
                          '<text x="300" y="30" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">' + opt + '</text>' +
                          '<text x="300" y="175" text-anchor="middle" font-size="11" fill="#475569">Vapor Recompression: ' + (vr ? 'Active (35% power reduction)' : 'Off') + '</text>';
          diag.textContent = 'Sequence optimization: Direct duty = ' + f(qDir, 2) + ' MW; Indirect duty = ' + f(qIndir, 2) + ' MW. ' + opt + ' saves ' + (vr ? '$' + f(savings, 0) + '/year.' : 'standard utility heat.');
        }
        [sZa, sZb, sEp, sVr].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    }
  ];
""" + get_engine_footer(8)

# =========================================================================
# 4. Separation Processes II
# =========================================================================
def build_sp2_sims():
    return """/* Separation Processes II Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Reverse Osmosis (RO) Flux & Concentration Polarization</h3><p class="lead">Simulate membrane desalination: evaluate water flux Jw, osmotic pressure Δπ, and concentration polarization modulus CP.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Feed Pressure ΔP <span><output id="v-delp">55.0</output> bar</span></label><input type="range" id="s-delp" min="15.0" max="80.0" step="2.5" value="55.0"></div>' +
              '<div class="control-group"><label>Feed Salinity Cb <span><output id="v-salin">32.0</output> g/L</span></label><input type="range" id="s-salin" min="2.0" max="65.0" step="1.0" value="32.0"></div>' +
              '<div class="control-group"><label>Water Permeability A <span><output id="v-perma">1.80</output> LMH/bar</span></label><input type="range" id="s-perma" min="0.50" max="4.00" step="0.10" value="1.80"></div>' +
              '<div class="control-group"><label>Crossflow Mass Coeff kcp <span><output id="v-kcp">20.0</output> μm/s</span></label><input type="range" id="s-kcp" min="5.0" max="60.0" step="2.5" value="20.0"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Bulk Osmotic Press πb</div><div class="readout-value" id="r-pib">25.6 bar</div></div>' +
              '<div class="readout-card"><div class="readout-label">Polarization Modulus CP</div><div class="readout-value" id="r-cpmod">1.28</div></div>' +
              '<div class="readout-card"><div class="readout-label">Net Driving NDP</div><div class="readout-value" id="r-ndp">22.2 bar</div></div>' +
              '<div class="readout-card"><div class="readout-label">Water Flux Jw</div><div class="readout-value" id="r-jw">40.0 LMH</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp21" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp21"></p>',
      init: function(el) {
        var sDelp = el.querySelector('#s-delp'), vDelp = el.querySelector('#v-delp');
        var sSalin = el.querySelector('#s-salin'), vSalin = el.querySelector('#v-salin');
        var sPerma = el.querySelector('#s-perma'), vPerma = el.querySelector('#v-perma');
        var sKcp = el.querySelector('#s-kcp'), vKcp = el.querySelector('#v-kcp');
        var rPib = el.querySelector('#r-pib'), rCpmod = el.querySelector('#r-cpmod');
        var rNdp = el.querySelector('#r-ndp'), rJw = el.querySelector('#r-jw');
        var svg = el.querySelector('#svg-sp21'), diag = el.querySelector('#diag-sp21');

        function update() {
          var dP = parseFloat(sDelp.value); vDelp.textContent = f(dP, 1);
          var Cb = parseFloat(sSalin.value); vSalin.textContent = f(Cb, 1);
          var A = parseFloat(sPerma.value); vPerma.textContent = f(A, 2);
          var kcp_um = parseFloat(sKcp.value); vKcp.textContent = f(kcp_um, 1);

          var pi_b = 0.80 * Cb; // approx 0.80 bar per g/L NaCl
          var kcp = kcp_um * 1e-6; // m/s
          var kcp_LMH = kcp * 3.6e6; // L/(m2 h)

          // Coupled solution for Jw and CP:
          var Jw = Math.max(1.0, A * (dP - pi_b));
          var CP = Math.exp(Jw / Math.max(10, kcp_LMH));
          CP = Math.min(2.5, Math.max(1.05, CP));
          var pi_m = pi_b * CP;
          var NDP = Math.max(0.5, dP - pi_m);
          Jw = A * NDP;

          rPib.textContent = f(pi_b, 1) + ' bar';
          rCpmod.textContent = f(CP, 2);
          rNdp.textContent = f(NDP, 1) + ' bar';
          rJw.textContent = f(Jw, 1) + ' LMH';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="280" y="30" width="20" height="140" fill="#0284c7" rx="3"/>' +
                          '<text x="290" y="105" text-anchor="middle" font-size="10" font-weight="700" fill="#ffffff" transform="rotate(-90 290 105)">RO Membrane</text>' +
                          '<rect x="80" y="40" width="200" height="120" fill="#dbeafe" fill-opacity="0.3"/>' +
                          '<text x="180" y="65" text-anchor="middle" font-size="12" font-weight="700" fill="#1e40af">Feed/Retentate Channel</text>' +
                          '<path d="M 120 120 Q 240 120 280 60" fill="none" stroke="#dc2626" stroke-width="3"/>' +
                          '<text x="270" y="55" text-anchor="end" font-size="10" font-weight="700" fill="#dc2626">Cm = ' + f(Cb*CP,1) + ' g/L</text>' +
                          '<line x1="300" y1="100" x2="480" y2="100" stroke="#16a34a" stroke-width="4"/>' +
                          '<text x="400" y="90" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">Permeate Jw = ' + f(Jw,1) + ' LMH</text>' +
                          '<text x="300" y="24" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">RO Transport: NDP = ' + f(NDP,1) + ' bar (CP = ' + f(CP,2) + ')</text>';
          diag.textContent = 'Reverse osmosis: Bulk osmotic pressure = ' + f(pi_b, 1) + ' bar. Concentration polarization increases membrane surface salt by ' + f((CP - 1) * 100, 1) + '%. Net flux = ' + f(Jw, 1) + ' LMH.';
        }
        [sDelp, sSalin, sPerma, sKcp].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Hollow-Fiber Gas Permeation Module & Stage-Cut Selectivity</h3><p class="lead">Simulate industrial gas separation in hollow-fiber bundles: evaluate permeate stage cut θ and membrane area requirements.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Stage Cut θ <span><output id="v-theta">0.25</output></span></label><input type="range" id="s-theta" min="0.05" max="0.50" step="0.05" value="0.25"></div>' +
              '<div class="control-group"><label>Membrane Selectivity α <span><output id="v-alpha22">30.0</output></span></label><input type="range" id="s-alpha22" min="5.0" max="60.0" step="2.5" value="30.0"></div>' +
              '<div class="control-group"><label>Feed Fast Gas zF <span><output id="v-zf22">0.20</output></span></label><input type="range" id="s-zf22" min="0.05" max="0.60" step="0.05" value="0.20"></div>' +
              '<div class="control-group"><label>Fiber Count <span><output id="v-fibers">5000</output></span></label><input type="range" id="s-fibers" min="1000" max="20000" step="1000" value="5000"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Permeate Purity yp</div><div class="readout-value" id="r-yp2">82.5 mol%</div></div>' +
              '<div class="readout-card"><div class="readout-label">Retentate Loss xr</div><div class="readout-value" id="r-xr2">0.058</div></div>' +
              '<div class="readout-card"><div class="readout-label">Recovery of Fast Gas</div><div class="readout-value" id="r-rec22">78.3 %</div></div>' +
              '<div class="readout-card"><div class="readout-label">Total Membrane Area</div><div class="readout-value" id="r-aream">15.7 m²</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp22" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp22"></p>',
      init: function(el) {
        var sTheta = el.querySelector('#s-theta'), vTheta = el.querySelector('#v-theta');
        var sAlpha = el.querySelector('#s-alpha22'), vAlpha = el.querySelector('#v-alpha22');
        var sZf = el.querySelector('#s-zf22'), vZf = el.querySelector('#v-zf22');
        var sFibers = el.querySelector('#s-fibers'), vFibers = el.querySelector('#v-fibers');
        var rYp = el.querySelector('#r-yp2'), rXr = el.querySelector('#r-xr2');
        var rRec = el.querySelector('#r-rec22'), rArea = el.querySelector('#r-aream');
        var svg = el.querySelector('#svg-sp22'), diag = el.querySelector('#diag-sp22');

        function update() {
          var theta = parseFloat(sTheta.value); vTheta.textContent = f(theta, 2);
          var alpha = parseFloat(sAlpha.value); vAlpha.textContent = f(alpha, 1);
          var zF = parseFloat(sZf.value); vZf.textContent = f(zF, 2);
          var fibers = parseInt(sFibers.value, 10); vFibers.textContent = fibers;

          var yp = (alpha * zF) / (1 + (alpha - 1) * zF);
          // Attenuation by stage-cut:
          yp = Math.max(zF * 1.1, yp * (1 - 0.45 * theta));
          var xr = (zF - theta * yp) / Math.max(0.01, (1 - theta));
          xr = Math.max(0.005, xr);
          var recovery = (theta * yp / zF) * 100;
          var area = fibers * Math.PI * 0.0005 * 2.0; // 0.5mm OD, 2m length

          rYp.textContent = f(yp * 100, 1) + ' mol%';
          rXr.textContent = f(xr, 3);
          rRec.textContent = f(recovery, 1) + ' %';
          rArea.textContent = f(area, 1) + ' m²';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="160" y="55" width="280" height="90" fill="#f1f5f9" stroke="#334155" stroke-width="2" rx="10"/>' +
                          '<line x1="170" y1="80" x2="430" y2="80" stroke="#0284c7" stroke-width="2" stroke-dasharray="3 3"/>' +
                          '<line x1="170" y1="100" x2="430" y2="100" stroke="#0284c7" stroke-width="2" stroke-dasharray="3 3"/>' +
                          '<line x1="170" y1="120" x2="430" y2="120" stroke="#0284c7" stroke-width="2" stroke-dasharray="3 3"/>' +
                          '<text x="300" y="45" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Hollow-Fiber Bundle (' + fibers + ' fibers)</text>' +
                          '<line x1="60" y1="100" x2="160" y2="100" stroke="#334155" stroke-width="4"/>' +
                          '<text x="110" y="90" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a">Feed zF=' + f(zF,2) + '</text>' +
                          '<line x1="440" y1="100" x2="540" y2="100" stroke="#64748b" stroke-width="3"/>' +
                          '<text x="490" y="90" text-anchor="middle" font-size="10" fill="#475569">Retentate xr=' + f(xr,3) + '</text>' +
                          '<line x1="300" y1="145" x2="300" y2="180" stroke="#16a34a" stroke-width="4"/>' +
                          '<text x="300" y="195" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">Permeate yp = ' + f(yp*100,1) + ' mol% (θ=' + f(theta,2) + ')</text>';
          diag.textContent = 'Gas permeation module: Stage cut θ = ' + f(theta, 2) + '. Permeate fast gas purity = ' + f(yp * 100, 1) + ' mol% with ' + f(recovery, 1) + '% component recovery.';
        }
        [sTheta, sAlpha, sZf, sFibers].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Fixed-Bed Adsorption Dynamics & Breakthrough Front Simulator</h3><p class="lead">Simulate breakthrough front propagation in activated carbon / zeolite beds: calculate breakthrough time tb and bed utilization.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Bed Length L <span><output id="v-blen">1.20</output> m</span></label><input type="range" id="s-blen" min="0.40" max="3.00" step="0.10" value="1.20"></div>' +
              '<div class="control-group"><label>Interstitial Velocity v <span><output id="v-intv">4.0</output> cm/s</span></label><input type="range" id="s-intv" min="1.0" max="15.0" step="0.5" value="4.0"></div>' +
              '<div class="control-group"><label>Adsorption Capacity qm <span><output id="v-qm">120</output> mg/g</span></label><input type="range" id="s-qm" min="30" max="300" step="10" value="120"></div>' +
              '<div class="control-group"><label>Inlet Concentration C0 <span><output id="v-cin3">1.50</output> g/m³</span></label><input type="range" id="s-cin3" min="0.20" max="5.00" step="0.10" value="1.50"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Breakthrough Time tb</div><div class="readout-value" id="r-tb">38.4 h</div></div>' +
              '<div class="readout-card"><div class="readout-label">Stoichiometric Time ts</div><div class="readout-value" id="r-ts">48.0 h</div></div>' +
              '<div class="readout-card"><div class="readout-label">Bed Utilization %</div><div class="readout-value" id="r-util">80.0 %</div></div>' +
              '<div class="readout-card"><div class="readout-label">MTZ Length</div><div class="readout-value" id="r-mtz">0.24 m</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp23" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp23"></p>',
      init: function(el) {
        var sBlen = el.querySelector('#s-blen'), vBlen = el.querySelector('#v-blen');
        var sIntv = el.querySelector('#s-intv'), vIntv = el.querySelector('#v-intv');
        var sQm = el.querySelector('#s-qm'), vQm = el.querySelector('#v-qm');
        var sCin = el.querySelector('#s-cin3'), vCin = el.querySelector('#v-cin3');
        var rTb = el.querySelector('#r-tb'), rTs = el.querySelector('#r-ts');
        var rUtil = el.querySelector('#r-util'), rMtz = el.querySelector('#r-mtz');
        var svg = el.querySelector('#svg-sp23'), diag = el.querySelector('#diag-sp23');

        var rhoBed = 600; // kg/m3

        function update() {
          var L = parseFloat(sBlen.value); vBlen.textContent = f(L, 2);
          var v_cms = parseFloat(sIntv.value); vIntv.textContent = f(v_cms, 1);
          var qm = parseFloat(sQm.value); vQm.textContent = f(qm, 0);
          var C0 = parseFloat(sCin.value); vCin.textContent = f(C0, 2);

          var v = v_cms * 0.01; // m/s
          var q0_kg = (qm * 1e-3) * rhoBed; // kg adsorbate per m3 bed
          var C0_kg = C0 * 1e-3; // kg/m3

          var uWave = (v * C0_kg) / (q0_kg + C0_kg); // wave velocity m/s
          var t_stoich = (L / Math.max(1e-8, uWave)) / 3600; // hours
          var t_break = t_stoich * 0.80;
          var L_mtz = L * 0.20;
          var util = (t_break / t_stoich) * 100;

          rTb.textContent = f(t_break, 1) + ' h';
          rTs.textContent = f(t_stoich, 1) + ' h';
          rUtil.textContent = f(util, 1) + ' %';
          rMtz.textContent = f(L_mtz, 2) + ' m';

          // S-curve points
          var pts = [];
          for (var tS = 0; tS <= t_stoich * 1.5; tS += t_stoich * 0.05) {
            var px = 100 + (tS / (t_stoich * 1.5)) * 400;
            var c_ratio = 1 / (1 + Math.exp(-8 * (tS - t_stoich) / t_stoich));
            var py = 160 - c_ratio * 110;
            pts.push(f(px,1) + ',' + f(py,1));
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="100" y="40" width="400" height="120" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>' +
                          '<polyline points="' + pts.join(' ') + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<line x1="' + (100 + (t_break/(t_stoich*1.5))*400) + '" y1="40" x2="' + (100 + (t_break/(t_stoich*1.5))*400) + '" y2="160" stroke="#dc2626" stroke-dasharray="3 3"/>' +
                          '<text x="' + (100 + (t_break/(t_stoich*1.5))*400) + '" y="32" text-anchor="middle" font-size="10" font-weight="700" fill="#dc2626">tb = ' + f(t_break,1) + 'h</text>' +
                          '<text x="300" y="22" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Breakthrough Curve C/C0 (L = ' + f(L,2) + 'm)</text>' +
                          '<text x="510" y="55" font-size="10" fill="#64748b">C/C0 = 1.0</text>' +
                          '<text x="510" y="160" font-size="10" fill="#64748b">C/C0 = 0.0</text>' +
                          '<text x="300" y="185" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">Bed Utilization: ' + f(util,1) + '% | MTZ = ' + f(L_mtz,2) + ' m</text>';
          diag.textContent = 'Fixed-bed breakthrough: Breakthrough time tb = ' + f(t_break, 1) + ' h. Bed saturation utilization = ' + f(util, 1) + '% (Mass transfer zone length = ' + f(L_mtz, 2) + ' m).';
        }
        [sBlen, sIntv, sQm, sCin].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Preparative Chromatography Van Deemter Plate Height & Resolution</h3><p class="lead">Simulate chromatographic column dispersion: optimize mobile phase linear velocity u and compute resolution Rs between peak pairs.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Mobile Phase Velocity u <span><output id="v-uvel">2.50</output> mm/s</span></label><input type="range" id="s-uvel" min="0.50" max="10.00" step="0.25" value="2.50"></div>' +
              '<div class="control-group"><label>Packing Particle dp <span><output id="v-dp4">25</output> μm</span></label><input type="range" id="s-dp4" min="5" max="80" step="5" value="25"></div>' +
              '<div class="control-group"><label>Column Length L <span><output id="v-clen">25.0</output> cm</span></label><input type="range" id="s-clen" min="10.0" max="100.0" step="5.0" value="25.0"></div>' +
              '<div class="control-group"><label>Selectivity α <span><output id="v-alphac">1.18</output></span></label><input type="range" id="s-alphac" min="1.05" max="1.60" step="0.02" value="1.18"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Plate Height HETP</div><div class="readout-value" id="r-hetp">54.2 μm</div></div>' +
              '<div class="readout-card"><div class="readout-label">Plate Count N</div><div class="readout-value" id="r-pcount">4,612 plates</div></div>' +
              '<div class="readout-card"><div class="readout-label">Optimum Velocity uopt</div><div class="readout-value" id="r-uopt">2.12 mm/s</div></div>' +
              '<div class="readout-card"><div class="readout-label">Peak Resolution Rs</div><div class="readout-value" id="r-resol">1.82 (Baseline)</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp24" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp24"></p>',
      init: function(el) {
        var sU = el.querySelector('#s-uvel'), vU = el.querySelector('#v-uvel');
        var sDp = el.querySelector('#s-dp4'), vDp = el.querySelector('#v-dp4');
        var sClen = el.querySelector('#s-clen'), vClen = el.querySelector('#v-clen');
        var sAl = el.querySelector('#s-alphac'), vAl = el.querySelector('#v-alphac');
        var rHetp = el.querySelector('#r-hetp'), rPcount = el.querySelector('#r-pcount');
        var rUopt = el.querySelector('#r-uopt'), rResol = el.querySelector('#r-resol');
        var svg = el.querySelector('#svg-sp24'), diag = el.querySelector('#diag-sp24');

        function update() {
          var u = parseFloat(sU.value); vU.textContent = f(u, 2);
          var dp_um = parseFloat(sDp.value); vDp.textContent = f(dp_um, 0);
          var L_cm = parseFloat(sClen.value); vClen.textContent = f(L_cm, 1);
          var alpha = parseFloat(sAl.value); vAl.textContent = f(alpha, 2);

          // Van Deemter: H = A + B/u + C*u
          var A = 1.5 * dp_um; // um
          var B = 35.0; // um * mm/s
          var C = 0.035 * Math.pow(dp_um, 2) / 10; // um / (mm/s)

          var H = A + B / u + C * u; // um
          var u_opt = Math.sqrt(B / Math.max(0.001, C));
          var L_um = L_cm * 10000;
          var N = Math.round(L_um / H);

          var kPrime = 3.0; // average capacity factor
          var Rs = 0.25 * Math.sqrt(N) * ((alpha - 1) / alpha) * (kPrime / (1 + kPrime));

          rHetp.textContent = f(H, 1) + ' μm';
          rPcount.textContent = f(N, 0) + ' plates';
          rUopt.textContent = f(u_opt, 2) + ' mm/s';
          rResol.textContent = f(Rs, 2) + (Rs >= 1.5 ? ' (Baseline)' : ' (Overlap)');

          // Chromatogram twin Gaussian peaks
          var p1_cx = 280, p2_cx = 280 + (alpha - 1) * 200;
          var sigma = Math.max(8, 60 / Math.sqrt(N / 1000));

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="80" y1="160" x2="520" y2="160" stroke="#334155" stroke-width="2"/>' +
                          '<path d="M ' + (p1_cx - 3*sigma) + ' 160 Q ' + p1_cx + ' 50 ' + (p1_cx + 3*sigma) + ' 160" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<path d="M ' + (p2_cx - 3*sigma) + ' 160 Q ' + p2_cx + ' 50 ' + (p2_cx + 3*sigma) + ' 160" fill="none" stroke="#dc2626" stroke-width="3"/>' +
                          '<text x="' + p1_cx + '" y="40" text-anchor="middle" font-size="11" font-weight="700" fill="#2563eb">Peak A</text>' +
                          '<text x="' + p2_cx + '" y="40" text-anchor="middle" font-size="11" font-weight="700" fill="#dc2626">Peak B</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Chromatogram Resolution: Rs = ' + f(Rs,2) + '</text>' +
                          '<text x="300" y="185" text-anchor="middle" font-size="11" fill="#475569">HETP = ' + f(H,1) + ' μm | N = ' + f(N,0) + ' | uopt = ' + f(u_opt,2) + ' mm/s</text>';
          diag.textContent = 'Van Deemter chromatography: Plate height H = ' + f(H, 1) + ' μm (N = ' + f(N, 0) + ' plates). Twin peak resolution Rs = ' + f(Rs, 2) + '.';
        }
        [sU, sDp, sClen, sAl].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>MSMPR Crystallizer Supersaturation & Crystal Size Distribution</h3><p class="lead">Simulate continuous solution crystallization: evaluate primary nucleation rate B0, crystal growth rate G, and dominant size LD.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Supersaturation S <span><output id="v-ssat">1.12</output></span></label><input type="range" id="s-ssat" min="1.02" max="1.30" step="0.01" value="1.12"></div>' +
              '<div class="control-group"><label>Residence Time τ <span><output id="v-tau5">45.0</output> min</span></label><input type="range" id="s-tau5" min="15.0" max="120.0" step="5.0" value="45.0"></div>' +
              '<div class="control-group"><label>Growth Constant kg <span><output id="v-kg5">1.20</output> μm/min</span></label><input type="range" id="s-kg5" min="0.20" max="3.00" step="0.10" value="1.20"></div>' +
              '<div class="control-group"><label>Nucleation Order b <span><output id="v-nord">2.5</output></span></label><input type="range" id="s-nord" min="1.0" max="4.0" step="0.5" value="2.5"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Linear Growth Rate G</div><div class="readout-value" id="r-grate">1.44 μm/min</div></div>' +
              '<div class="readout-card"><div class="readout-label">Dominant Size LD</div><div class="readout-value" id="r-ldom">194.4 μm</div></div>' +
              '<div class="readout-card"><div class="readout-label">Nucleation Rate B0</div><div class="readout-value" id="r-nrate">8.4e6 #/m³·s</div></div>' +
              '<div class="readout-card"><div class="readout-label">Product Quality</div><div class="readout-value" id="r-cqual">Coarse Free-Flowing</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp25" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp25"></p>',
      init: function(el) {
        var sS = el.querySelector('#s-ssat'), vS = el.querySelector('#v-ssat');
        var sTau = el.querySelector('#s-tau5'), vTau = el.querySelector('#v-tau5');
        var sKg = el.querySelector('#s-kg5'), vKg = el.querySelector('#v-kg5');
        var sNord = el.querySelector('#s-nord'), vNord = el.querySelector('#v-nord');
        var rGrate = el.querySelector('#r-grate'), rLdom = el.querySelector('#r-ldom');
        var rNrate = el.querySelector('#r-nrate'), rCqual = el.querySelector('#r-cqual');
        var svg = el.querySelector('#svg-sp25'), diag = el.querySelector('#diag-sp25');

        function update() {
          var S = parseFloat(sS.value); vS.textContent = f(S, 2);
          var tau = parseFloat(sTau.value); vTau.textContent = f(tau, 1);
          var kg = parseFloat(sKg.value); vKg.textContent = f(kg, 2);
          var b = parseFloat(sNord.value); vNord.textContent = f(b, 1);

          var sigma = S - 1.0; // relative supersaturation
          var G = kg * Math.pow(sigma, 1.0); // um/min
          var B0 = 5e7 * Math.pow(sigma, b); // #/m3 s
          var L_D = 3 * G * tau; // um dominant size in MSMPR

          rGrate.textContent = f(G, 2) + ' μm/min';
          rLdom.textContent = f(L_D, 1) + ' μm';
          rNrate.textContent = B0.toExponential(1) + ' #/m³·s';
          rCqual.textContent = L_D > 150 ? 'Coarse Free-Flowing' : (L_D > 60 ? 'Medium Crystals' : 'Fine / Fines Problem');

          // Population density exponential distribution n(L) = n0 * exp(-L / G*tau)
          var pts = [];
          for (var Ls = 0; Ls <= 500; Ls += 10) {
            var px = 80 + (Ls / 500) * 440;
            var frac = Math.exp(-Ls / Math.max(1, G * tau));
            var py = 160 - frac * 120;
            pts.push(f(px,1) + ',' + f(py,1));
          }

          var curX = 80 + (Math.min(500, L_D) / 500) * 440;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="40" width="440" height="120" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>' +
                          '<polyline points="' + pts.join(' ') + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<line x1="' + curX + '" y1="40" x2="' + curX + '" y2="160" stroke="#dc2626" stroke-width="2"/>' +
                          '<text x="' + curX + '" y="32" text-anchor="middle" font-size="11" font-weight="700" fill="#dc2626">LD = ' + f(L_D,0) + ' μm</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Population Balance n(L) in MSMPR (S = ' + f(S,2) + ')</text>' +
                          '<text x="300" y="185" text-anchor="middle" font-size="11" fill="#475569">G = ' + f(G,2) + ' μm/min | B0 = ' + B0.toExponential(1) + ' #/m³·s | ' + rCqual.textContent + '</text>';
          diag.textContent = 'Continuous MSMPR crystallization: Supersaturation ratio S = ' + f(S, 2) + '. Dominant product crystal size LD = 3·G·τ = ' + f(L_D, 1) + ' μm.';
        }
        [sS, sTau, sKg, sNord].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Constant-Pressure Cake Filtration (Ruth Equation)</h3><p class="lead">Simulate solid-liquid slurry filtration: calculate specific cake resistance α, filter medium resistance Rm, and wash cycle.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Filtration Pressure ΔP <span><output id="v-dp6">2.5</output> bar</span></label><input type="range" id="s-dp6" min="0.5" max="6.0" step="0.5" value="2.5"></div>' +
              '<div class="control-group"><label>Slurry Solids Conc c <span><output id="v-cslur">40</output> kg/m³</span></label><input type="range" id="s-cslur" min="10" max="120" step="5" value="40"></div>' +
              '<div class="control-group"><label>Filter Area A <span><output id="v-farea">2.0</output> m²</span></label><input type="range" id="s-farea" min="0.5" max="10.0" step="0.5" value="2.0"></div>' +
              '<div class="control-group"><label>Filtration Time t <span><output id="v-ftime">20.0</output> min</span></label><input type="range" id="s-ftime" min="2.0" max="60.0" step="2.0" value="20.0"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Filtrate Volume V</div><div class="readout-value" id="r-vfilt">3.12 m³</div></div>' +
              '<div class="readout-card"><div class="readout-label">Cake Thickness Lc</div><div class="readout-value" id="r-thick">41.6 mm</div></div>' +
              '<div class="readout-card"><div class="readout-label">Terminal Flow dV/dt</div><div class="readout-value" id="r-termflow">1.30 L/s</div></div>' +
              '<div class="readout-card"><div class="readout-label">Cake Solids Mass</div><div class="readout-value" id="r-smass">124.8 kg</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp26" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp26"></p>',
      init: function(el) {
        var sDp = el.querySelector('#s-dp6'), vDp = el.querySelector('#v-dp6');
        var sCslur = el.querySelector('#s-cslur'), vCslur = el.querySelector('#v-cslur');
        var sFarea = el.querySelector('#s-farea'), vFarea = el.querySelector('#v-farea');
        var sFtime = el.querySelector('#s-ftime'), vFtime = el.querySelector('#v-ftime');
        var rVfilt = el.querySelector('#r-vfilt'), rThick = el.querySelector('#r-thick');
        var rTermflow = el.querySelector('#r-termflow'), rSmass = el.querySelector('#r-smass');
        var svg = el.querySelector('#svg-sp26'), diag = el.querySelector('#diag-sp26');

        var mu = 0.001; // Pa s water
        var alpha = 1.8e11; // m/kg specific cake resistance
        var Rm = 5e10; // 1/m medium resistance

        function update() {
          var dP_bar = parseFloat(sDp.value); vDp.textContent = f(dP_bar, 1);
          var c = parseFloat(sCslur.value); vCslur.textContent = f(c, 0);
          var A = parseFloat(sFarea.value); vFarea.textContent = f(A, 1);
          var t_min = parseFloat(sFtime.value); vFtime.textContent = f(t_min, 1);

          var dP = dP_bar * 1e5; // Pa
          var t_sec = t_min * 60;

          // Ruth parabolic filtration: t / V = (mu * alpha * c) / (2 * A^2 * dP) * V + (mu * Rm) / (A * dP)
          var K_p = (mu * alpha * c) / (2 * A * A * dP);
          var B_p = (mu * Rm) / (A * dP);

          // Solve quadratic: K_p * V^2 + B_p * V - t_sec = 0
          var V = (-B_p + Math.sqrt(B_p * B_p + 4 * K_p * t_sec)) / (2 * K_p);
          var solids = V * c; // kg
          var Lc_mm = (solids / (1500 * A)) * 1000; // 1500 kg/m3 wet cake
          var dV_dt = (A * dP) / (mu * (alpha * c * (V / A) + Rm)) * 1000; // L/s

          rVfilt.textContent = f(V, 2) + ' m³';
          rThick.textContent = f(Lc_mm, 1) + ' mm';
          rTermflow.textContent = f(dV_dt, 2) + ' L/s';
          rSmass.textContent = f(solids, 1) + ' kg';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="180" y="40" width="240" height="120" fill="#f1f5f9" stroke="#334155" stroke-width="2" rx="4"/>' +
                          '<rect x="180" y="110" width="240" height="20" fill="#cbd5e1" stroke="#475569" stroke-width="1"/>' +
                          '<text x="300" y="125" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">Filter Medium Septum</text>' +
                          '<rect x="180" y="' + (110 - Math.min(60, Lc_mm)) + '" width="240" height="' + Math.min(60, Lc_mm) + '" fill="#ca8a04" fill-opacity="0.3" stroke="#ca8a04" stroke-width="1"/>' +
                          '<text x="300" y="' + (100 - Math.min(45, Lc_mm/2)) + '" text-anchor="middle" font-size="11" font-weight="700" fill="#854d0e">Filter Cake Lc=' + f(Lc_mm,1) + 'mm</text>' +
                          '<line x1="300" y1="130" x2="300" y2="180" stroke="#0284c7" stroke-width="3"/>' +
                          '<text x="300" y="195" text-anchor="middle" font-size="11" font-weight="700" fill="#0369a1">Filtrate V = ' + f(V,2) + ' m³ (Rate ' + f(dV_dt,2) + ' L/s)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Constant-Pressure Filtration (ΔP = ' + f(dP_bar,1) + ' bar)</text>';
          diag.textContent = 'Cake filtration: At ΔP = ' + f(dP_bar, 1) + ' bar over ' + f(t_min, 1) + ' min, filtrate volume = ' + f(V, 2) + ' m³ with a ' + f(Lc_mm, 1) + ' mm cake.';
        }
        [sDp, sCslur, sFarea, sFtime].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Rotary Drum Vacuum Filter Continuous Throughput</h3><p class="lead">Simulate industrial continuous filtration on rotating vacuum drums: evaluate cycle submergence and solids throughput.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Drum Speed N <span><output id="v-drumn">0.50</output> RPM</span></label><input type="range" id="s-drumn" min="0.10" max="2.50" step="0.05" value="0.50"></div>' +
              '<div class="control-group"><label>Submergence Fraction f <span><output id="v-subm">35.0</output> %</span></label><input type="range" id="s-subm" min="20.0" max="50.0" step="2.5" value="35.0"></div>' +
              '<div class="control-group"><label>Drum Area A <span><output id="v-darea">15.0</output> m²</span></label><input type="range" id="s-darea" min="5.0" max="50.0" step="2.5" value="15.0"></div>' +
              '<div class="control-group"><label>Vacuum Pressure ΔP <span><output id="v-vac">0.60</output> bar</span></label><input type="range" id="s-vac" min="0.20" max="0.85" step="0.05" value="0.60"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Cake Form Time tf</div><div class="readout-value" id="r-tform">42.0 s</div></div>' +
              '<div class="readout-card"><div class="readout-label">Drum Cycle Time tc</div><div class="readout-value" id="r-tcycl">120.0 s</div></div>' +
              '<div class="readout-card"><div class="readout-label">Solids Production</div><div class="readout-value" id="r-prod7">2.45 ton/h</div></div>' +
              '<div class="readout-card"><div class="readout-label">Discharge Thickness</div><div class="readout-value" id="r-dthick">14.2 mm</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp27" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp27"></p>',
      init: function(el) {
        var sN = el.querySelector('#s-drumn'), vN = el.querySelector('#v-drumn');
        var sSubm = el.querySelector('#s-subm'), vSubm = el.querySelector('#v-subm');
        var sA = el.querySelector('#s-darea'), vA = el.querySelector('#v-darea');
        var sVac = el.querySelector('#s-vac'), vVac = el.querySelector('#v-vac');
        var rTform = el.querySelector('#r-tform'), rTcycl = el.querySelector('#r-tcycl');
        var rProd = el.querySelector('#r-prod7'), rDthick = el.querySelector('#r-dthick');
        var svg = el.querySelector('#svg-sp27'), diag = el.querySelector('#diag-sp27');

        function update() {
          var N_rpm = parseFloat(sN.value); vN.textContent = f(N_rpm, 2);
          var subm = parseFloat(sSubm.value) / 100; vSubm.textContent = f(subm * 100, 1);
          var A = parseFloat(sA.value); vA.textContent = f(A, 1);
          var vac = parseFloat(sVac.value); vVac.textContent = f(vac, 2);

          var tc = 60 / Math.max(0.01, N_rpm); // cycle time seconds
          var tf = tc * subm; // formation time seconds

          // Production rate scales with sqrt(f * N * dP):
          var prod = 1.4 * Math.sqrt(subm * N_rpm * (vac / 0.5)) * (A / 10); // ton/h
          var Lc = (prod * 1000 / (N_rpm * 60 * A * 1.5)); // mm approx

          rTform.textContent = f(tf, 1) + ' s';
          rTcycl.textContent = f(tc, 1) + ' s';
          rProd.textContent = f(prod, 2) + ' ton/h';
          rDthick.textContent = f(Lc, 1) + ' mm';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<circle cx="300" cy="100" r="65" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>' +
                          '<path d="M 235 100 A 65 65 0 0 0 365 100 Z" fill="#ca8a04" fill-opacity="0.25"/>' +
                          '<rect x="210" y="90" width="180" height="50" fill="#bfdbfe" fill-opacity="0.3" stroke="#3b82f6" stroke-width="1"/>' +
                          '<text x="300" y="125" text-anchor="middle" font-size="11" font-weight="700" fill="#1e40af">Slurry Trough (' + f(subm*100,0) + '% subm)</text>' +
                          '<text x="300" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Rotary Drum (N=' + f(N_rpm,2) + ' RPM)</text>' +
                          '<line x1="365" y1="90" x2="420" y2="70" stroke="#ef4444" stroke-width="3"/>' +
                          '<text x="425" y="70" font-size="11" font-weight="700" fill="#dc2626">Knife Discharge (' + f(prod,2) + ' t/h)</text>' +
                          '<text x="300" y="24" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Continuous Vacuum Drum Filtration</text>';
          diag.textContent = 'Rotary drum throughput: Speed = ' + f(N_rpm, 2) + ' RPM (Cycle time = ' + f(tc, 1) + ' s). Solids cake discharge rate = ' + f(prod, 2) + ' ton/h.';
        }
        [sN, sSubm, sA, sVac].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Hybrid Membrane-Distillation Energy & Exergy Optimization</h3><p class="lead">Simulate integrated separation flowsheets: evaluate steam consumption reduction and thermodynamic exergy savings.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Azeotrope Feed Conc <span><output id="v-azfeed">85.0</output> wt%</span></label><input type="range" id="s-azfeed" min="70.0" max="95.0" step="1.0" value="85.0"></div>' +
              '<div class="control-group"><label>Membrane Cut Recovery <span><output id="v-mcut">60.0</output> %</span></label><input type="range" id="s-mcut" min="20.0" max="90.0" step="5.0" value="60.0"></div>' +
              '<div class="control-group"><label>Feed Throughput <span><output id="v-tfthroughput">15.0</output> ton/h</span></label><input type="range" id="s-tfthroughput" min="5.0" max="50.0" step="2.5" value="15.0"></div>' +
              '<div class="control-group"><label>Steam Cost <span><output id="v-scost">22.0</output> $/ton</span></label><input type="range" id="s-scost" min="10.0" max="45.0" step="1.0" value="22.0"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Standalone Column Duty</div><div class="readout-value" id="r-qstand">7.40 MW</div></div>' +
              '<div class="readout-card"><div class="readout-label">Hybrid Flowsheet Duty</div><div class="readout-value" id="r-qhyb">3.85 MW</div></div>' +
              '<div class="readout-card"><div class="readout-label">Thermal Energy Reduction</div><div class="readout-value" id="r-ereduc">48.0 %</div></div>' +
              '<div class="readout-card"><div class="readout-label">Annual Operating Savings</div><div class="readout-value" id="r-opcost">$492,000 /yr</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp28" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp28"></p>',
      init: function(el) {
        var sAz = el.querySelector('#s-azfeed'), vAz = el.querySelector('#v-azfeed');
        var sCut = el.querySelector('#s-mcut'), vCut = el.querySelector('#v-mcut');
        var sFeed = el.querySelector('#s-tfthroughput'), vFeed = el.querySelector('#v-tfthroughput');
        var sSc = el.querySelector('#s-scost'), vSc = el.querySelector('#v-scost');
        var rQstand = el.querySelector('#r-qstand'), rQhyb = el.querySelector('#r-qhyb');
        var rEreduc = el.querySelector('#r-ereduc'), rOpcost = el.querySelector('#r-opcost');
        var svg = el.querySelector('#svg-sp28'), diag = el.querySelector('#diag-sp28');

        function update() {
          var az = parseFloat(sAz.value); vAz.textContent = f(az, 1);
          var cut = parseFloat(sCut.value) / 100; vCut.textContent = f(cut * 100, 1);
          var feed = parseFloat(sFeed.value); vFeed.textContent = f(feed, 1);
          var sc = parseFloat(sSc.value); vSc.textContent = f(sc, 1);

          var qStand = feed * 0.49; // MW
          var qHyb = qStand * (1 - 0.70 * cut); // Membrane pre-concentrates
          var reduc = ((qStand - qHyb) / qStand) * 100;
          var steamSavedTons = (qStand - qHyb) * 3600 * 8000 / 2200; // tons steam / yr
          var savDollars = steamSavedTons * sc;

          rQstand.textContent = f(qStand, 2) + ' MW';
          rQhyb.textContent = f(qHyb, 2) + ' MW';
          rEreduc.textContent = f(reduc, 1) + ' %';
          rOpcost.textContent = '$' + f(savDollars, 0) + ' /yr';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="55" width="100" height="70" fill="#e0f2fe" stroke="#0284c7" stroke-width="2" rx="4"/>' +
                          '<text x="130" y="90" text-anchor="middle" font-size="11" font-weight="700" fill="#0369a1">Membrane Unit</text>' +
                          '<line x1="180" y1="90" x2="260" y2="90" stroke="#0284c7" stroke-width="3"/>' +
                          '<rect x="260" y="40" width="90" height="100" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="6"/>' +
                          '<text x="305" y="90" text-anchor="middle" font-size="11" font-weight="700" fill="#92400e">Distillation</text>' +
                          '<rect x="420" y="50" width="140" height="80" fill="#dcfce7" stroke="#16a34a" stroke-width="2" rx="6"/>' +
                          '<text x="490" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="#15803d">Energy Savings</text>' +
                          '<text x="490" y="105" text-anchor="middle" font-size="14" font-weight="800" fill="#16a34a">' + f(reduc,1) + '% Saved</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Hybrid Membrane-Distillation System</text>' +
                          '<text x="300" y="180" text-anchor="middle" font-size="11" fill="#475569">Reboiler Steam Reduced from ' + f(qStand,2) + ' MW to ' + f(qHyb,2) + ' MW (Savings: $' + f(savDollars,0) + '/yr)</text>';
          diag.textContent = 'Hybrid separation: Membrane dewatering pre-cut reduces reboiler duty by ' + f(reduc, 1) + '%, saving $' + f(savDollars, 0) + ' annually in utility steam.';
        }
        [sAz, sCut, sFeed, sSc].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    }
  ];
""" + get_engine_footer(8)

books = [
    ('mass-transfer', build_mt_sims),
    ('separation-processes-i', build_sp1_sims),
    ('separation-processes-ii', build_sp2_sims)
]

for slug, builder in books:
    dest_dir = os.path.join(ROOT, 'src', 'subjects', 'chemical-process-engineering', slug)
    os.makedirs(dest_dir, exist_ok=True)
    out_file = os.path.join(dest_dir, f"{slug}-sims.js")
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(builder())
    print(f"Wrote {out_file}")

print("Batch 2 remaining simulation suites generated successfully!")
