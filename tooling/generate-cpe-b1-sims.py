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
# 2. material-and-energy-balances
# =========================================================================
def build_meb_sims():
    sim_js = """/* Material and Energy Balances Interactive Simulation Suite */
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
              '<div class="control-group"><label>Purge Fraction \\u03B8 <span><output id="v-purg">0.10</output></span></label><input type="range" id="s-purg" min="0.02" max="0.30" step="0.01" value="0.10"></div>' +
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
""" + get_engine_footer(8)
    return sim_js

# =========================================================================
# 3. chemical-engineering-thermodynamics
# =========================================================================
def build_cet_sims():
    sim_js = """/* Chemical Engineering Thermodynamics Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Ideal Gas Isothermal & Isobaric State Explorer</h3><p class="lead">Evaluate state functions, exact differentials, and PVT paths across pure gas phases.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Temperature T <span><output id="v-t1">350</output> K</span></label><input type="range" id="s-t1" min="200" max="600" step="10" value="350"></div>' +
              '<div class="control-group"><label>Molar Volume Vm <span><output id="v-vm1">4.0</output> m³/kmol</span></label><input type="range" id="s-vm1" min="0.5" max="15.0" step="0.5" value="4.0"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>System Pressure P</small><output id="out-p1">727.5</output> kPa</div>' +
              '<div class="stat-box"><small>Enthalpy Departure</small><output id="out-dh1">0.00</output> kJ/kmol</div>' +
              '<div class="stat-box"><small>Compressibility Z</small><output id="out-z1">1.000</output></div>' +
            '</div>' +
            '<svg id="svg-cet1" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-cet1">Ideal gas equation of state: P = R * T / Vm; state functions depend solely on endpoints.</div>',
      init: function(card) {
        var sT = card.querySelector('#s-t1'), sVm = card.querySelector('#s-vm1');
        var vT = card.querySelector('#v-t1'), vVm = card.querySelector('#v-vm1');
        var outP = card.querySelector('#out-p1'), outDh = card.querySelector('#out-dh1'), outZ = card.querySelector('#out-z1');
        var svg = card.querySelector('#svg-cet1'), diag = card.querySelector('#diag-cet1');

        function update() {
          var T = parseFloat(sT.value), Vm = parseFloat(sVm.value);
          vT.textContent = f(T, 0); vVm.textContent = f(Vm, 1);
          var R = 8.314462;
          var P = (R * T) / Vm; // kPa

          outP.textContent = f(P, 1); outDh.textContent = '0.00'; outZ.textContent = '1.000';

          var pts = '';
          for (var v = 1.0; v <= 15.0; v += 0.5) {
            var p_pt = (R * T) / v;
            var xP = 60 + ((v - 1.0) / 14.0) * 360;
            var yP = 135 - Math.min(105, (p_pt / 2500.0) * 105);
            pts += (pts ? ' ' : '') + xP.toFixed(1) + ',' + yP.toFixed(1);
          }
          var curX = 60 + ((Vm - 1.0) / 14.0) * 360;
          var curY = 135 - Math.min(105, (P / 2500.0) * 105);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="125" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<polyline points="' + pts + '" fill="none" stroke="#0284c7" stroke-width="2.5"/>' +
                          '<circle cx="' + curX + '" cy="' + curY + '" r="5" fill="#ef4444"/>' +
                          '<text x="60" y="38" font-size="11" fill="#0369a1" font-weight="700">Isotherm at T = ' + f(T, 0) + ' K (P vs Vm)</text>' +
                          '<text x="' + Math.min(320, curX + 10) + '" y="' + curY + '" font-size="11" fill="#b91c1c" font-weight="700">P = ' + f(P, 1) + ' kPa</text>' +
                          '<text x="210" y="142" font-size="10" fill="#64748b">Molar Volume (m³/kmol)</text>';
          diag.textContent = 'Thermodynamic state verified: P = ' + f(P, 1) + ' kPa at Vm = ' + f(Vm, 1) + ' m³/kmol.';
        }
        [sT, sVm].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Peng-Robinson Cubic Equation of State</h3><p class="lead">Solve real fluid compressibility factor Z, vapor-liquid cubic roots, and volume departures.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Reduced Temp Tr <span><output id="v-tr">1.10</output></span></label><input type="range" id="s-tr" min="0.60" max="2.00" step="0.05" value="1.10"></div>' +
              '<div class="control-group"><label>Reduced Press Pr <span><output id="v-pr">0.80</output></span></label><input type="range" id="s-pr" min="0.10" max="4.00" step="0.10" value="0.80"></div>' +
              '<div class="control-group"><label>Acentric Factor \\u03C9 <span><output id="v-om">0.15</output></span></label><input type="range" id="s-om" min="0.0" max="0.50" step="0.05" value="0.15"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Vapor Factor Zv</small><output id="out-zv">0.785</output></div>' +
              '<div class="stat-box"><small>Liquid Factor Zl</small><output id="out-zl">0.092</output></div>' +
              '<div class="stat-box"><small>Departure (1-Z)</small><output id="out-dz">0.215</output></div>' +
            '</div>' +
            '<svg id="svg-cet2" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-cet2">Peng-Robinson cubic form: Z³ - (1-B)Z² + (A - 3B² - 2B)Z - (AB - B² - B³) = 0.</div>',
      init: function(card) {
        var sTr = card.querySelector('#s-tr'), sPr = card.querySelector('#s-pr'), sOm = card.querySelector('#s-om');
        var vTr = card.querySelector('#v-tr'), vPr = card.querySelector('#v-pr'), vOm = card.querySelector('#v-om');
        var outZv = card.querySelector('#out-zv'), outZl = card.querySelector('#out-zl'), outDz = card.querySelector('#out-dz');
        var svg = card.querySelector('#svg-cet2'), diag = card.querySelector('#diag-cet2');

        function update() {
          var Tr = parseFloat(sTr.value), Pr = parseFloat(sPr.value), om = parseFloat(sOm.value);
          vTr.textContent = f(Tr, 2); vPr.textContent = f(Pr, 2); vOm.textContent = f(om, 2);

          var kappa = 0.37464 + 1.54226 * om - 0.26992 * Math.pow(om, 2);
          var alpha = Math.pow(1.0 + kappa * (1.0 - Math.sqrt(Tr)), 2);
          var A = 0.45724 * alpha * Pr / Math.pow(Tr, 2);
          var B = 0.07780 * Pr / Tr;

          // Solve cubic: Z^3 - (1-B)Z^2 + (A - 3B^2 - 2B)Z - (AB - B^2 - B^3) = 0
          var c2 = -(1.0 - B);
          var c1 = A - 3.0 * Math.pow(B, 2) - 2.0 * B;
          var c0 = -(A * B - Math.pow(B, 2) - Math.pow(B, 3));

          // Newton solver for vapor root (start high Z=1)
          var Zv = 1.0;
          for (var i = 0; i < 20; i++) {
            var fZ = Math.pow(Zv, 3) + c2 * Math.pow(Zv, 2) + c1 * Zv + c0;
            var dfZ = 3.0 * Math.pow(Zv, 2) + 2.0 * c2 * Zv + c1;
            Zv = Zv - fZ / dfZ;
          }
          // Liquid root (start near B)
          var Zl = B + 0.001;
          for (var j = 0; j < 20; j++) {
            var fZ2 = Math.pow(Zl, 3) + c2 * Math.pow(Zl, 2) + c1 * Zl + c0;
            var dfZ2 = 3.0 * Math.pow(Zl, 2) + 2.0 * c2 * Zl + c1;
            Zl = Zl - fZ2 / dfZ2;
          }
          Zv = Math.max(0.1, Math.min(1.5, Zv));
          Zl = Math.max(B, Math.min(0.4, Zl));
          var dZ = Math.abs(1.0 - Zv);

          outZv.textContent = f(Zv, 3); outZl.textContent = f(Zl, 3); outDz.textContent = f(dZ, 3);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<rect x="60" y="50" width="' + (Zv * 200) + '" height="30" fill="#0284c7" rx="4"/>' +
                          '<rect x="60" y="90" width="' + (Zl * 200) + '" height="30" fill="#10b981" rx="4"/>' +
                          '<text x="65" y="42" font-size="11" fill="#0369a1" font-weight="700">Vapor Compressibility Zv = ' + f(Zv, 3) + '</text>' +
                          '<text x="65" y="130" font-size="11" fill="#047857" font-weight="700">Liquid Compressibility Zl = ' + f(Zl, 3) + '</text>' +
                          '<text x="280" y="70" font-size="11" fill="#475569">Parameters: A = ' + f(A, 3) + ', B = ' + f(B, 3) + '</text>';
          diag.textContent = 'Real gas solution: Vapor deviation (1-Z) is ' + f(dZ * 100, 1) + '%; cubic EOS roots stable.';
        }
        [sTr, sPr, sOm].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Heat of Reaction Temperature Dependence (Kirchhoff)</h3><p class="lead">Simulate standard reaction enthalpy shift Delta H(T) = Delta H(T0) + Integral Delta Cp dT.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Reaction Temp T <span><output id="v-tr3">500</output> K</span></label><input type="range" id="s-tr3" min="298" max="900" step="20" value="500"></div>' +
              '<div class="control-group"><label>Base \\u0394H°(298) <span><output id="v-dh0">-50.0</output> kJ/mol</span></label><input type="range" id="s-dh0" min="-120" max="60" step="5" value="-50"></div>' +
              '<div class="control-group"><label>\\u0394Cp <span><output id="v-dcp">15.0</output> J/mol·K</span></label><input type="range" id="s-dcp" min="-30" max="40" step="5" value="15"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Actual \\u0394H°(T)</small><output id="out-dht">-46.97</output> kJ/mol</div>' +
              '<div class="stat-box"><small>Heat Capacity Shift</small><output id="out-dcpterm">3.03</output> kJ/mol</div>' +
              '<div class="stat-box"><small>Reaction Type</small><output id="out-rxtype">Exothermic</output></div>' +
            '</div>' +
            '<svg id="svg-cet3" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-cet3">Kirchhoff relation: d(\\u0394H)/dT = \\u0394Cp; endothermicity increases with positive \\u0394Cp.</div>',
      init: function(card) {
        var sT = card.querySelector('#s-tr3'), sDh0 = card.querySelector('#s-dh0'), sDcp = card.querySelector('#s-dcp');
        var vT = card.querySelector('#v-tr3'), vDh0 = card.querySelector('#v-dh0'), vDcp = card.querySelector('#v-dcp');
        var outDht = card.querySelector('#out-dht'), outDcpterm = card.querySelector('#out-dcpterm'), outRxtype = card.querySelector('#out-rxtype');
        var svg = card.querySelector('#svg-cet3'), diag = card.querySelector('#diag-cet3');

        function update() {
          var T = parseFloat(sT.value), dh0 = parseFloat(sDh0.value), dcp = parseFloat(sDcp.value);
          vT.textContent = f(T, 0); vDh0.textContent = f(dh0, 1); vDcp.textContent = f(dcp, 1);

          var dCpTerm = (dcp * (T - 298.15)) / 1000.0; // kJ/mol
          var dhT = dh0 + dCpTerm;
          var rxType = dhT < 0 ? 'Exothermic' : 'Endothermic';

          outDht.textContent = f(dhT, 2); outDcpterm.textContent = f(dCpTerm, 2); outRxtype.textContent = rxType;

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<line x1="60" y1="80" x2="420" y2="80" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="2"/>' +
                          '<line x1="60" y1="' + (80 - dh0) + '" x2="420" y2="' + (80 - (dh0 + dcp * 600 / 1000.0)) + '" stroke="#0284c7" stroke-width="3"/>' +
                          '<circle cx="' + (60 + ((T - 298) / 600.0) * 360) + '" cy="' + (80 - dhT) + '" r="5" fill="#ef4444"/>' +
                          '<text x="60" y="38" font-size="12" fill="#0369a1" font-weight="700">\\u0394H° at ' + f(T,0) + ' K = ' + f(dhT, 2) + ' kJ/mol (' + rxType + ')</text>' +
                          '<text x="240" y="115" font-size="11" fill="#475569">\\u0394Cp correction = ' + f(dCpTerm, 2) + ' kJ/mol</text>';
          diag.textContent = 'Kirchhoff energy integral verified: Standard enthalpy of reaction is ' + f(dhT, 2) + ' kJ/mol at ' + f(T, 0) + ' K.';
        }
        [sT, sDh0, sDcp].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Carnot Efficiency & Entropy Generation</h3><p class="lead">Simulate maximum thermal conversion efficiency, heat rejection, and lost work.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Hot Reservoir Th <span><output id="v-th4">600</output> K</span></label><input type="range" id="s-th4" min="400" max="1000" step="20" value="600"></div>' +
              '<div class="control-group"><label>Cold Reservoir Tc <span><output id="v-tc4">300</output> K</span></label><input type="range" id="s-tc4" min="280" max="400" step="10" value="300"></div>' +
              '<div class="control-group"><label>Heat Addition Qh <span><output id="v-qh4">100</output> kW</span></label><input type="range" id="s-qh4" min="20" max="250" step="10" value="100"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Carnot Efficiency</small><output id="out-eta">50.0</output> %</div>' +
              '<div class="stat-box"><small>Maximum Work W</small><output id="out-wmax">50.0</output> kW</div>' +
              '<div class="stat-box"><small>Rejected Heat Qc</small><output id="out-qc">50.0</output> kW</div>' +
            '</div>' +
            '<svg id="svg-cet4" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-cet4">Carnot efficiency eta = 1 - Tc/Th represents the thermodynamic upper bound on power generation.</div>',
      init: function(card) {
        var sTh = card.querySelector('#s-th4'), sTc = card.querySelector('#s-tc4'), sQh = card.querySelector('#s-qh4');
        var vTh = card.querySelector('#v-th4'), vTc = card.querySelector('#v-tc4'), vQh = card.querySelector('#v-qh4');
        var outEta = card.querySelector('#out-eta'), outWmax = card.querySelector('#out-wmax'), outQc = card.querySelector('#out-qc');
        var svg = card.querySelector('#svg-cet4'), diag = card.querySelector('#diag-cet4');

        function update() {
          var th = parseFloat(sTh.value), tc = parseFloat(sTc.value), qh = parseFloat(sQh.value);
          vTh.textContent = f(th, 0); vTc.textContent = f(tc, 0); vQh.textContent = f(qh, 0);

          var eta = 1.0 - tc / th;
          var wMax = qh * eta;
          var qc = qh - wMax;

          outEta.textContent = f(eta * 100.0, 1); outWmax.textContent = f(wMax, 1); outQc.textContent = f(qc, 1);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<rect x="60" y="30" width="100" height="30" rx="4" fill="#ef4444"/>' +
                          '<text x="75" y="50" font-size="11" fill="#fff" font-weight="700">Th = ' + f(th,0) + ' K</text>' +
                          '<rect x="60" y="95" width="100" height="30" rx="4" fill="#0284c7"/>' +
                          '<text x="75" y="115" font-size="11" fill="#fff" font-weight="700">Tc = ' + f(tc,0) + ' K</text>' +
                          '<circle cx="230" cy="77" r="25" fill="#f59e0b"/>' +
                          '<text x="215" y="82" font-size="12" fill="#fff" font-weight="700">HE</text>' +
                          '<line x1="160" y1="45" x2="210" y2="65" stroke="#ef4444" stroke-width="2"/>' +
                          '<line x1="210" y1="90" x2="160" y2="110" stroke="#0284c7" stroke-width="2"/>' +
                          '<line x1="255" y1="77" x2="340" y2="77" stroke="#10b981" stroke-width="4"/>' +
                          '<text x="350" y="82" font-size="13" fill="#047857" font-weight="700">W = ' + f(wMax,1) + ' kW</text>';
          diag.textContent = 'Second law limit: Maximum Carnot efficiency is ' + f(eta * 100, 1) + '%; reversible work output = ' + f(wMax, 1) + ' kW.';
        }
        [sTh, sTc, sQh].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Fugacity & Residual Enthalpy Departures</h3><p class="lead">Calculate real fluid fugacity coefficient phi and enthalpy departure H - H_ig.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Pressure P <span><output id="v-p5">5.0</output> MPa</span></label><input type="range" id="s-p5" min="0.5" max="25.0" step="0.5" value="5.0"></div>' +
              '<div class="control-group"><label>Temperature T <span><output id="v-t5">400</output> K</span></label><input type="range" id="s-t5" min="250" max="650" step="10" value="400"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Fugacity Coeff \\u03C6</small><output id="out-phi">0.892</output></div>' +
              '<div class="stat-box"><small>Fugacity f</small><output id="out-fug">4.46</output> MPa</div>' +
              '<div class="stat-box"><small>Residual H^R</small><output id="out-hr">-450</output> kJ/kmol</div>' +
            '</div>' +
            '<svg id="svg-cet5" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-cet5">Fugacity represents effective thermodynamic chemical pressure: ln(phi) = Integral (Z-1)/P dP.</div>',
      init: function(card) {
        var sP = card.querySelector('#s-p5'), sT = card.querySelector('#s-t5');
        var vP = card.querySelector('#v-p5'), vT = card.querySelector('#v-t5');
        var outPhi = card.querySelector('#out-phi'), outFug = card.querySelector('#out-fug'), outHr = card.querySelector('#out-hr');
        var svg = card.querySelector('#svg-cet5'), diag = card.querySelector('#diag-cet5');

        function update() {
          var P = parseFloat(sP.value), T = parseFloat(sT.value);
          vP.textContent = f(P, 1); vT.textContent = f(T, 0);

          // Simplified virial/departure: B = b0 - b1/T
          var B_vir = 0.04 - 25.0 / T;
          var R = 8.314e-3; // MPa m3 / kmol K
          var phi = Math.exp((B_vir * P) / (R * T));
          phi = Math.max(0.1, Math.min(1.5, phi));
          var fug = phi * P;
          var HR = -50.0 * P * (300.0 / T);

          outPhi.textContent = f(phi, 3); outFug.textContent = f(fug, 2); outHr.textContent = f(HR, 0);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<rect x="60" y="50" width="' + (phi * 200) + '" height="35" rx="4" fill="#0284c7"/>' +
                          '<text x="65" y="42" font-size="11" fill="#0369a1" font-weight="700">Fugacity Coefficient \\u03C6 = ' + f(phi, 3) + '</text>' +
                          '<text x="280" y="65" font-size="12" fill="#0f172a" font-weight="700">f = ' + f(fug, 2) + ' MPa</text>' +
                          '<text x="280" y="90" font-size="11" fill="#475569">Enthalpy departure H^R = ' + f(HR, 0) + ' kJ/kmol</text>';
          diag.textContent = 'Non-ideality quantified: Chemical fugacity is ' + f(fug, 2) + ' MPa at ' + f(P, 1) + ' MPa total pressure.';
        }
        [sP, sT].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Binary Vapor-Liquid Equilibrium (Raoult Law)</h3><p class="lead">Simulate T-x-y bubble and dew point envelopes for ideal binary solutions.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Liquid Mole Frac xA <span><output id="v-xa6">0.40</output></span></label><input type="range" id="s-xa6" min="0.05" max="0.95" step="0.05" value="0.40"></div>' +
              '<div class="control-group"><label>Total Pressure P <span><output id="v-ptot">101.3</output> kPa</span></label><input type="range" id="s-ptot" min="50" max="300" step="10" value="101.3"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Vapor Mole Frac yA</small><output id="out-ya6">0.625</output></div>' +
              '<div class="stat-box"><small>Bubble Temp T_bub</small><output id="out-tbub">92.4</output> °C</div>' +
              '<div class="stat-box"><small>Relative Volatility</small><output id="out-relvol">2.50</output></div>' +
            '</div>' +
            '<svg id="svg-cet6" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-cet6">Raoult law: P = xA * P_sat,A + xB * P_sat,B; yA = (xA * P_sat,A) / P.</div>',
      init: function(card) {
        var sXa = card.querySelector('#s-xa6'), sPtot = card.querySelector('#s-ptot');
        var vXa = card.querySelector('#v-xa6'), vPtot = card.querySelector('#v-ptot');
        var outYa = card.querySelector('#out-ya6'), outTbub = card.querySelector('#out-tbub'), outRelvol = card.querySelector('#out-relvol');
        var svg = card.querySelector('#svg-cet6'), diag = card.querySelector('#diag-cet6');

        function update() {
          var xA = parseFloat(sXa.value), P = parseFloat(sPtot.value);
          vXa.textContent = f(xA, 2); vPtot.textContent = f(P, 1);

          var alpha = 2.5;
          var yA = (alpha * xA) / (1.0 + (alpha - 1.0) * xA);
          // Pure component boiling points: Ta=80, Tb=110
          var tBub = 110.0 - (110.0 - 80.0) * (xA * alpha) / (1.0 + (alpha - 1.0) * xA);

          outYa.textContent = f(yA, 3); outTbub.textContent = f(tBub, 1); outRelvol.textContent = f(alpha, 2);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<path d="M 60 120 Q 200 70 420 30" fill="none" stroke="#0284c7" stroke-width="2.5"/>' +
                          '<path d="M 60 120 Q 280 90 420 30" fill="none" stroke="#f59e0b" stroke-width="2.5"/>' +
                          '<circle cx="' + (60 + xA * 360) + '" cy="' + (120 - (tBub - 80) * 2.5) + '" r="5" fill="#ef4444"/>' +
                          '<text x="60" y="35" font-size="11" fill="#0369a1" font-weight="700">T-x-y Phase Diagram (P = ' + f(P,0) + ' kPa)</text>' +
                          '<text x="240" y="75" font-size="11" fill="#b91c1c" font-weight="700">xA = ' + f(xA,2) + ' \\u2192 yA = ' + f(yA,3) + '</text>' +
                          '<text x="240" y="95" font-size="11" fill="#475569">Bubble point = ' + f(tBub,1) + ' °C</text>';
          diag.textContent = 'Phase equilibrium confirmed: Liquid xA = ' + f(xA, 2) + ' coexists with equilibrium vapor yA = ' + f(yA, 3) + '.';
        }
        [sXa, sPtot].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>NRTL Activity Coefficient & Excess Gibbs Free Energy</h3><p class="lead">Simulate non-ideal liquid activity coefficients gamma_i and G_E/RT.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Mole Fraction x1 <span><output id="v-x7">0.50</output></span></label><input type="range" id="s-x7" min="0.05" max="0.95" step="0.05" value="0.50"></div>' +
              '<div class="control-group"><label>Interaction \\u03C412 <span><output id="v-tau12">0.80</output></span></label><input type="range" id="s-tau12" min="-1.50" max="2.50" step="0.10" value="0.80"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Activity Coeff \\u03B31</small><output id="out-gam1">1.25</output></div>' +
              '<div class="stat-box"><small>Activity Coeff \\u03B32</small><output id="out-gam2">1.22</output></div>' +
              '<div class="stat-box"><small>Excess Gibbs G_E/RT</small><output id="out-gert">0.21</output></div>' +
            '</div>' +
            '<svg id="svg-cet7" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-cet7">NRTL local composition model captures positive and negative deviations from Raoult law.</div>',
      init: function(card) {
        var sX = card.querySelector('#s-x7'), sTau = card.querySelector('#s-tau12');
        var vX = card.querySelector('#v-x7'), vTau = card.querySelector('#v-tau12');
        var outGam1 = card.querySelector('#out-gam1'), outGam2 = card.querySelector('#out-gam2'), outGert = card.querySelector('#out-gert');
        var svg = card.querySelector('#svg-cet7'), diag = card.querySelector('#diag-cet7');

        function update() {
          var x1 = parseFloat(sX.value), tau12 = parseFloat(sTau.value);
          vX.textContent = f(x1, 2); vTau.textContent = f(tau12, 2);

          var x2 = 1.0 - x1;
          var alpha = 0.3;
          var G12 = Math.exp(-alpha * tau12);
          var lnGam1 = Math.pow(x2, 2) * (tau12 * Math.pow(G12 / (x1 + x2 * G12), 2));
          var lnGam2 = Math.pow(x1, 2) * (tau12 * Math.pow(1.0 / (x2 + x1 * G12), 2));
          var gam1 = Math.exp(lnGam1);
          var gam2 = Math.exp(lnGam2);
          var gERT = x1 * lnGam1 + x2 * lnGam2;

          outGam1.textContent = f(gam1, 2); outGam2.textContent = f(gam2, 2); outGert.textContent = f(gERT, 2);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<rect x="60" y="45" width="' + (gam1 * 100) + '" height="30" fill="#0284c7" rx="4"/>' +
                          '<rect x="60" y="85" width="' + (gam2 * 100) + '" height="30" fill="#10b981" rx="4"/>' +
                          '<text x="65" y="38" font-size="11" fill="#0369a1" font-weight="700">\\u03B31 = ' + f(gam1, 2) + '</text>' +
                          '<text x="65" y="125" font-size="11" fill="#047857" font-weight="700">\\u03B32 = ' + f(gam2, 2) + '</text>' +
                          '<text x="240" y="70" font-size="12" fill="#0f172a" font-weight="700">Excess Gibbs G_E/RT = ' + f(gERT, 3) + '</text>' +
                          '<text x="240" y="95" font-size="11" fill="#475569">Local composition factor G12 = ' + f(G12, 3) + '</text>';
          diag.textContent = 'Non-ideal solution thermodynamics: Activity coefficients \\u03B31 = ' + f(gam1, 2) + ', \\u03B32 = ' + f(gam2, 2) + '.';
        }
        [sX, sTau].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Chemical Reaction Equilibrium Constant K(T)</h3><p class="lead">Simulate Van \\'t Hoff equilibrium conversion and temperature sensitivity.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Temperature T <span><output id="v-teq">600</output> K</span></label><input type="range" id="s-teq" min="300" max="1000" step="25" value="600"></div>' +
              '<div class="control-group"><label>\\u0394H°rxn <span><output id="v-dh8">-45</output> kJ/mol</span></label><input type="range" id="s-dh8" min="-100" max="60" step="5" value="-45"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Equilibrium K</small><output id="out-keq">8.42</output></div>' +
              '<div class="stat-box"><small>Equilibrium Conversion</small><output id="out-xeq">89.4</output> %</div>' +
              '<div class="stat-box"><small>Van \\\'t Hoff dlnK/dT</small><output id="out-dlnk">-0.015</output> K⁻¹</div>' +
            '</div>' +
            '<svg id="svg-cet8" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-cet8">Van \\\'t Hoff equation: d(ln K)/dT = \\u0394H° / (R * T²). Exothermic reactions show decreasing K with temperature.</div>',
      init: function(card) {
        var sT = card.querySelector('#s-teq'), sDh = card.querySelector('#s-dh8');
        var vT = card.querySelector('#v-teq'), vDh = card.querySelector('#v-dh8');
        var outKeq = card.querySelector('#out-keq'), outXeq = card.querySelector('#out-xeq'), outDlnk = card.querySelector('#out-dlnk');
        var svg = card.querySelector('#svg-cet8'), diag = card.querySelector('#diag-cet8');

        function update() {
          var T = parseFloat(sT.value), dH = parseFloat(sDh.value);
          vT.textContent = f(T, 0); vDh.textContent = f(dH, 0);

          var R = 8.314e-3; // kJ/mol K
          var dG0 = 5.0; // at 298
          var lnK = -(dH / (R * T)) + (dH - dG0) / (R * 298.15);
          var K = Math.exp(Math.max(-8, Math.min(8, lnK)));
          // A <-> B: K = x / (1-x) => x_eq = K / (1 + K)
          var xEq = (K / (1.0 + K)) * 100.0;
          var dlnK = dH / (8.314e-3 * Math.pow(T, 2));

          outKeq.textContent = f(K, 2); outXeq.textContent = f(xEq, 1); outDlnk.textContent = f(dlnK, 4);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<rect x="60" y="55" width="' + (xEq * 3.4) + '" height="35" rx="4" fill="#0284c7"/>' +
                          '<text x="65" y="45" font-size="12" fill="#0369a1" font-weight="700">Equilibrium Conversion X_eq = ' + f(xEq, 1) + '%</text>' +
                          '<text x="60" y="115" font-size="11" fill="#475569">Equilibrium constant K = ' + f(K, 2) + ' at T = ' + f(T, 0) + ' K</text>' +
                          '<text x="280" y="115" font-size="11" fill="#0f172a">d(ln K)/dT = ' + f(dlnK, 4) + ' K⁻¹</text>';
          diag.textContent = 'Reaction equilibrium closed: Equilibrium conversion reaches ' + f(xEq, 1) + '% at ' + f(T, 0) + ' K.';
        }
        [sT, sDh].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    }
  ];
""" + get_engine_footer(8)
    return sim_js

# =========================================================================
# 4. transport-phenomena
# =========================================================================
def build_tp_sims():
    sim_js = """/* Transport Phenomena Interactive Simulation Suite */
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
              '<div class="stat-box"><small>Space Time \\u03C4</small><output id="out-tau1">30.0</output> s</div>' +
              '<div class="stat-box"><small>95% Response Time</small><output id="out-t95">89.9</output> s</div>' +
              '<div class="stat-box"><small>Steady Outlet c_inf</small><output id="out-cinf">50.0</output> mol/m³</div>' +
            '</div>' +
            '<svg id="svg-tp1" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-tp1">First-order dynamic response: c(t) = cin * (1 - exp(-t/\\u03C4)) starting from zero initial holdup.</div>',
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
                          '<text x="320" y="70" font-size="11" fill="#b91c1c" font-weight="700">\\u03C4 = ' + f(tau,1) + ' s</text>';
          diag.textContent = 'Well-mixed reactor dynamic response: Hydraulic space time \\u03C4 = ' + f(tau, 1) + ' s.';
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
              '<div class="control-group"><label>Viscosity \\u03BC <span><output id="v-mu2">10.0</output> mPa·s</span></label><input type="range" id="s-mu2" min="1.0" max="50.0" step="1.0" value="10.0"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Centerline Velocity vmax</small><output id="out-vmax2">7.81</output> m/s</div>' +
              '<div class="stat-box"><small>Average Velocity v_avg</small><output id="out-vavg2">3.91</output> m/s</div>' +
              '<div class="stat-box"><small>Volumetric Flow Q</small><output id="out-flow2">7.67</output> L/s</div>' +
            '</div>' +
            '<svg id="svg-tp2" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-tp2">Navier-Stokes solution: vz(r) = (dP/L) * (R² - r²) / (4*\\u03BC); vmax = 2 * v_avg.</div>',
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
              '<div class="control-group"><label>Kinematic Viscosity \\u03BD <span><output id="v-nu3">1.0</output> mm²/s</span></label><input type="range" id="s-nu3" min="0.5" max="10.0" step="0.5" value="1.0"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Plate End Thickness \\u03B4(L)</small><output id="out-del3">3.54</output> mm</div>' +
              '<div class="stat-box"><small>Reynolds Re_L</small><output id="out-rel">2.00e5</output></div>' +
              '<div class="stat-box"><small>Skin Friction Cf</small><output id="out-cf3">0.0015</output></div>' +
            '</div>' +
            '<svg id="svg-tp3" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-tp3">Blasius exact boundary layer solution: \\u03B4(x) = 5.0 * sqrt(\\u03BD * x / U_inf); Cf = 0.664 / sqrt(Re_x).</div>',
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
                          '<text x="65" y="38" font-size="11" fill="#0369a1" font-weight="700">Boundary Layer Thickness \\u03B4(x)</text>' +
                          '<text x="260" y="75" font-size="11" fill="#b91c1c" font-weight="700">\\u03B4(L) = ' + f(delta_L_mm, 2) + ' mm</text>' +
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
              '<div class="stat-box"><small>Temp Rise \\u0394T</small><output id="out-delt4">2.50</output> °C</div>' +
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
          diag.textContent = 'Fourier conduction solved: Internal heat generation elevates slab center to ' + f(T0, 2) + ' °C (\\u0394T = ' + f(deltaT, 2) + ' °C).';
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
              '<div class="stat-box"><small>Molar Flux JA</small><output id="out-ja6">16.0</output> \\u03BCmol/m²·s</div>' +
              '<div class="stat-box"><small>Counter Flux JB</small><output id="out-jb6">-16.0</output> \\u03BCmol/m²·s</div>' +
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
                          '<text x="210" y="70" font-size="12" fill="#047857" font-weight="700">JA = ' + f(JA_umol, 1) + ' \\u03BCmol/m²·s</text>';
          diag.textContent = 'Fickian diffusion balance: Molar flux JA = ' + f(JA_umol, 1) + ' \\u03BCmol/m²·s; equimolar condition JB = -JA holds.';
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
""" + get_engine_footer(8)
    return sim_js

# =========================================================================
# 5. fluid-flow-in-processes
# =========================================================================
def build_ffp_sims():
    sim_js = """/* Fluid Flow in Processes Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Non-Newtonian Power-Law Apparent Viscosity</h3><p class="lead">Simulate pseudoplastic (shear-thinning) and dilatant fluid viscosity curves.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Shear Rate \\u03B3_dot <span><output id="v-gdot">100</output> s⁻¹</span></label><input type="range" id="s-gdot" min="5" max="500" step="5" value="100"></div>' +
              '<div class="control-group"><label>Consistency Index K <span><output id="v-k1">2.0</output> Pa·s^n</span></label><input type="range" id="s-k1" min="0.2" max="10.0" step="0.2" value="2.0"></div>' +
              '<div class="control-group"><label>Flow Index n <span><output id="v-n1">0.60</output></span></label><input type="range" id="s-n1" min="0.20" max="1.50" step="0.05" value="0.60"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Apparent Viscosity</small><output id="out-eta1">0.317</output> Pa·s</div>' +
              '<div class="stat-box"><small>Shear Stress \\u03C4</small><output id="out-tau1">31.7</output> Pa</div>' +
              '<div class="stat-box"><small>Rheology Class</small><output id="out-rheoclass">Shear-Thinning</output></div>' +
            '</div>' +
            '<svg id="svg-ffp1" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-ffp1">Ostwald-de Waele power law: \\u03C4 = K * (\\u03B3_dot)^n; apparent viscosity \\u03B7 = K * (\\u03B3_dot)^(n-1).</div>',
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
                          '<text x="60" y="35" font-size="11" fill="#0369a1" font-weight="700">Apparent Viscosity \\u03B7 vs Shear Rate (n = ' + f(n,2) + ')</text>' +
                          '<text x="240" y="148" font-size="10" fill="#64748b">Shear Rate \\u03B3_dot (s⁻¹)</text>' +
                          '<text x="290" y="65" font-size="11" fill="#b91c1c" font-weight="700">\\u03B7 = ' + f(eta, 3) + ' Pa·s</text>';
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
              '<div class="stat-box"><small>Differential \\u0394P</small><output id="out-dpman">24.7</output> kPa</div>' +
              '<div class="stat-box"><small>Water Head</small><output id="out-wh">2.52</output> m H2O</div>' +
              '<div class="stat-box"><small>Bar</small><output id="out-barman">0.247</output> bar</div>' +
            '</div>' +
            '<svg id="svg-ffp2" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-ffp2">Manometer equation: \\u0394P = (\\u03C1_m - \\u03C1_p) * g * h.</div>',
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
                          '<text x="240" y="55" font-size="14" fill="#0284c7" font-weight="700">\\u0394P = ' + f(dP_kPa, 2) + ' kPa</text>' +
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
              '<div class="control-group"><label>Differential Head \\u0394h <span><output id="v-dhv">0.80</output> m</span></label><input type="range" id="s-dhv" min="0.10" max="3.00" step="0.10" value="0.80"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Volumetric Flow Q</small><output id="out-qv">7.72</output> L/s</div>' +
              '<div class="stat-box"><small>Throat Velocity v2</small><output id="out-v2">3.93</output> m/s</div>' +
              '<div class="stat-box"><small>Diameter Ratio \\u03B2</small><output id="out-beta">0.50</output></div>' +
            '</div>' +
            '<svg id="svg-ffp3" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-ffp3">Bernoulli discharge equation: Q = Cd * A2 * sqrt(2*g*\\u0394h / (1 - \\u03B2⁴)).</div>',
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
                          '<text x="290" y="100" font-size="11" fill="#475569">Diameter ratio \\u03B2 = ' + f(beta, 2) + '</text>';
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
              '<div class="control-group"><label>Relative Roughness \\u03B5/D <span><output id="v-ed4">0.0010</output></span></label><input type="range" id="s-ed4" min="0.00005" max="0.010" step="0.0005" value="0.0010"></div>' +
              '<div class="control-group"><label>Pipe Length L <span><output id="v-len4">50</output> m</span></label><input type="range" id="s-len4" min="10" max="200" step="10" value="50"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Darcy Friction f</small><output id="out-f4">0.0248</output></div>' +
              '<div class="stat-box"><small>Head Loss hf</small><output id="out-hf4">3.16</output> m</div>' +
              '<div class="stat-box"><small>Pressure Drop \\u0394P</small><output id="out-dp4">31.0</output> kPa</div>' +
            '</div>' +
            '<svg id="svg-ffp4" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-ffp4">Swamee-Jain explicit formula: f = 0.25 / [log10(\\u03B5/3.7D + 5.74/Re^0.9)]².</div>',
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
                          '<text x="60" y="115" font-size="11" fill="#475569">Head loss hf = ' + f(hf, 2) + ' m | Pipe \\u0394P = ' + f(dP_kPa, 1) + ' kPa across ' + f(L,0) + ' m</text>' +
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
              '<div class="control-group"><label>Static Lift \\u0394z <span><output id="v-dz">15.0</output> m</span></label><input type="range" id="s-dz" min="5" max="30" step="1" value="15"></div>' +
              '<div class="control-group"><label>System Resistance K <span><output id="v-ksys">0.008</output></span></label><input type="range" id="s-ksys" min="0.003" max="0.025" step="0.001" value="0.008"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Operating Flow Q_op</small><output id="out-qop">51.2</output> m³/h</div>' +
              '<div class="stat-box"><small>Operating Head H_op</small><output id="out-hop">36.0</output> m</div>' +
              '<div class="stat-box"><small>Hydraulic Power</small><output id="out-pw">5.02</output> kW</div>' +
            '</div>' +
            '<svg id="svg-ffp5" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-ffp5">Pump curve H = H0 - a*Q² intersects system resistance H = \\u0394z + K*Q² at operating point.</div>',
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
              '<div class="control-group"><label>Liquid Alone \\u0394P_L <span><output id="v-dpl6">10.0</output> kPa</span></label><input type="range" id="s-dpl6" min="2.0" max="40.0" step="1.0" value="10.0"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Multiplier \\u03A6_L²</small><output id="out-phi6">5.16</output></div>' +
              '<div class="stat-box"><small>Two-Phase \\u0394P_TP</small><output id="out-dptp">51.6</output> kPa</div>' +
              '<div class="stat-box"><small>Flow Regime</small><output id="out-tpreg">Slug / Wavy</output></div>' +
            '</div>' +
            '<svg id="svg-ffp6" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-ffp6">Chisholm correlation: \\u03A6_L² = 1 + C/X + 1/X² with C = 20 for turbulent-turbulent flow.</div>',
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
                          '<text x="60" y="45" font-size="12" fill="#0369a1" font-weight="700">Two-Phase Pressure Drop \\u0394P_TP = ' + f(dpTP, 1) + ' kPa</text>' +
                          '<text x="60" y="115" font-size="11" fill="#475569">Multiplier \\u03A6_L² = ' + f(phiSq, 2) + ' | Regime: ' + regime + '</text>';
          diag.textContent = 'Lockhart-Martinelli two-phase multiplier \\u03A6_L² = ' + f(phiSq, 2) + ' amplifies single-phase friction.';
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
              '<div class="control-group"><label>Differential \\u0394P <span><output id="v-dp7">25.0</output> kPa</span></label><input type="range" id="s-dp7" min="5" max="80" step="5" value="25"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Measured Flow Q</small><output id="out-qorf">5.23</output> L/s</div>' +
              '<div class="stat-box"><small>Permanent Loss</small><output id="out-permloss">18.5</output> kPa</div>' +
              '<div class="stat-box"><small>Orifice Beta \\u03B2</small><output id="out-beta7">0.40</output></div>' +
            '</div>' +
            '<svg id="svg-ffp7" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-ffp7">Standard concentric orifice: Q = C0 * A0 / sqrt(1 - \\u03B2⁴) * sqrt(2*\\u0394P/\\u03C1).</div>',
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
            '<div class="diagnostic-note" id="diag-ffp8">Hydraulic law: Total flow Q = Q1 + Q2 with equal head loss \\u0394h1 = \\u0394h2 across parallel paths.</div>',
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
""" + get_engine_footer(8)
    return sim_js

# Generate simulation engines for all 5 books
books = [
    ('material-and-energy-balances', build_meb_sims),
    ('chemical-engineering-thermodynamics', build_cet_sims),
    ('transport-phenomena', build_tp_sims),
    ('fluid-flow-in-processes', build_ffp_sims)
]

for slug, builder in books:
    dest_dir = os.path.join(ROOT, 'src', 'subjects', 'chemical-process-engineering', slug)
    os.makedirs(dest_dir, exist_ok=True)
    out_file = os.path.join(dest_dir, f"{slug}-sims.js")
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(builder())
    print(f"Wrote {out_file}")

print("Batch 1 simulation suites generated successfully!")
