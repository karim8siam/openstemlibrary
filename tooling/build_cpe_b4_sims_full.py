# Batch 4 simulation engine builder for Chemical & Process Engineering
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
# 1. Process Design
# =========================================================================
def build_pdes_sims():
    return """/* Process Design Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Douglas Onion Model Conceptual Decision Levels</h3><p class="lead">Simulate hierarchical synthesis decisions: batch vs continuous, recycling, and separation hierarchy.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Annual Production Rate <span><output id="v-prod">50</output> kt/yr</span></label><input type="range" id="s-prod" min="5" max="250" step="5" value="50"></div>' +
              '<div class="control-group"><label>Raw Material Cost <span><output id="v-rmc">$800</output>/ton</span></label><input type="range" id="s-rmc" min="400" max="1500" step="50" value="800"></div>' +
              '<div class="control-group"><label>Product Value <span><output id="v-pval">$1400</output>/ton</span></label><input type="range" id="s-pval" min="900" max="2500" step="50" value="1400"></div>' +
              '<div class="control-group"><label>Product Life Cycle <span><output id="v-life">15</output> yr</span></label><input type="range" id="s-life" min="5" max="25" step="1" value="15"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Operating Mode</span><span class="value" id="r-opmode">Continuous</span><span class="subtext">throughput threshold</span></div>' +
              '<div class="readout-card"><span class="label">Gross Economic Margin</span><span class="value" id="r-gem">$30.0 M/yr</span><span class="subtext">revenue - raw materials</span></div>' +
              '<div class="readout-card"><span class="label">Design Level 1</span><span class="value" id="r-dlev1">Viable</span><span class="subtext">economic potential 1</span></div>' +
              '<div class="readout-card"><span class="label">Hierarchy Phase</span><span class="value" id="r-hphase">Level 2: Recycles</span><span class="subtext">synthesis status</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdes-u1" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdes-u1"></div>',
      init: function(card) {
        var sP = card.querySelector('#s-prod'), vP = card.querySelector('#v-prod');
        var sR = card.querySelector('#s-rmc'), vR = card.querySelector('#v-rmc');
        var sV = card.querySelector('#s-pval'), vV = card.querySelector('#v-pval');
        var sL = card.querySelector('#s-life'), vL = card.querySelector('#v-life');
        var rMode = card.querySelector('#r-opmode'), rGem = card.querySelector('#r-gem');
        var rLev = card.querySelector('#r-dlev1'), rPhase = card.querySelector('#r-hphase');
        var svg = card.querySelector('#plot-pdes-u1'), diag = card.querySelector('#diag-pdes-u1');

        function update() {
          var prod = parseFloat(sP.value); vP.textContent = f(prod, 0);
          var rmc = parseFloat(sR.value); vR.textContent = '$' + f(rmc, 0);
          var pval = parseFloat(sV.value); vV.textContent = '$' + f(pval, 0);
          var life = parseFloat(sL.value); vL.textContent = f(life, 0);

          var isContinuous = prod >= 10;
          var gem = (prod * 1000 * (pval - rmc)) / 1e6; // $M/yr
          var ep1_viable = gem > 5.0;

          rMode.textContent = isContinuous ? 'Continuous Plant' : 'Batch Processing';
          rGem.textContent = '$' + f(gem, 1) + ' M/yr';
          rLev.textContent = ep1_viable ? 'Viable (EP1 > 0)' : 'Marginal / Non-Viable';
          rLev.style.color = ep1_viable ? '#15803d' : '#dc2626';
          rPhase.textContent = ep1_viable ? 'Level 2: Reactor-Recycles' : 'Screen Alternative Chemistry';

          // SVG concentric Douglas onion circles
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<circle cx="300" cy="100" r="85" fill="#f1f5f9" stroke="#94a3b8" stroke-width="2"/>' +
                          '<circle cx="300" cy="100" r="65" fill="#e2e8f0" stroke="#0284c7" stroke-width="2"/>' +
                          '<circle cx="300" cy="100" r="45" fill="#bae6fd" stroke="#0369a1" stroke-width="2"/>' +
                          '<circle cx="300" cy="100" r="25" fill="#0284c7" stroke="#0c4a6e" stroke-width="2"/>' +
                          '<text x="300" y="104" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">Reactor</text>' +
                          '<text x="300" y="70" text-anchor="middle" font-size="10" font-weight="700" fill="#0369a1">Separators</text>' +
                          '<text x="300" y="48" text-anchor="middle" font-size="10" font-weight="700" fill="#0284c7">Heat Exchanger Network</text>' +
                          '<text x="300" y="28" text-anchor="middle" font-size="10" font-weight="700" fill="#475569">Utilities & Environmental</text>' +
                          '<text x="70" y="100" font-size="12" font-weight="700" fill="#1e293b">EP1: $' + f(gem, 1) + 'M/yr</text>' +
                          '<text x="530" y="100" text-anchor="end" font-size="12" font-weight="700" fill="' + (isContinuous ? '#0284c7' : '#d97706') + '">' + (isContinuous ? 'Continuous Flow' : 'Batch Campaign') + '</text>';
          diag.textContent = 'At ' + f(prod, 0) + ' kt/yr throughput, the economic potential Level 1 margin is $' + f(gem, 1) + ' M/yr. ' + (isContinuous ? 'High throughput strongly favors continuous dedicated unit operations.' : 'Low annual production favors multi-product batch processing campaigns.') + ' Conceptual design advances to Level 2 reactor-separator network synthesis.';
        }
        [sP, sR, sV, sL].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Reactor-Separator Recycle Loop Optimization</h3><p class="lead">Simulate per-pass conversion vs recycle capital expenditure, compression power, and purge losses.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Single-Pass Conv X <span><output id="v-spc">45%</output></span></label><input type="range" id="s-spc" min="15" max="85" step="5" value="45"></div>' +
              '<div class="control-group"><label>Purge Fraction fp <span><output id="v-purg">3.0%</output></span></label><input type="range" id="s-purg" min="0.5" max="10.0" step="0.5" value="3.0"></div>' +
              '<div class="control-group"><label>Fresh Reactant Feed <span><output id="v-ffeed">100</output> kmol/h</span></label><input type="range" id="s-ffeed" min="20" max="250" step="10" value="100"></div>' +
              '<div class="control-group"><label>Selectivity Exponent <span><output id="v-selexp">Moderate</output></span></label><input type="range" id="s-selexp" min="1" max="2" step="1" value="1"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Recycle Flow R</span><span class="value" id="r-recflow">0 kmol/h</span><span class="subtext">recycle stream rate</span></div>' +
              '<div class="readout-card"><span class="label">Recycle Ratio (R/F)</span><span class="value" id="r-recratio">0.00</span><span class="subtext">recycle multiplier</span></div>' +
              '<div class="readout-card"><span class="label">Overall Conversion</span><span class="value" id="r-ovrconv">0.0%</span><span class="subtext">including loop recycle</span></div>' +
              '<div class="readout-card"><span class="label">Compression Power</span><span class="value" id="r-compw">0 kW</span><span class="subtext">recycle gas compressor</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdes-u2" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdes-u2"></div>',
      init: function(card) {
        var sX = card.querySelector('#s-spc'), vX = card.querySelector('#v-spc');
        var sP = card.querySelector('#s-purg'), vP = card.querySelector('#v-purg');
        var sF = card.querySelector('#s-ffeed'), vF = card.querySelector('#v-ffeed');
        var sS = card.querySelector('#s-selexp'), vS = card.querySelector('#v-selexp');
        var rR = card.querySelector('#r-recflow'), rRatio = card.querySelector('#r-recratio');
        var rOvr = card.querySelector('#r-ovrconv'), rComp = card.querySelector('#r-compw');
        var svg = card.querySelector('#plot-pdes-u2'), diag = card.querySelector('#diag-pdes-u2');

        function update() {
          var X = parseFloat(sX.value) / 100; vX.textContent = f(X * 100, 0) + '%';
          var fp = parseFloat(sP.value) / 100; vP.textContent = f(fp * 100, 1) + '%';
          var F = parseFloat(sF.value); vF.textContent = f(F, 0);
          var selHigh = parseInt(sS.value, 10) === 2;
          vS.textContent = selHigh ? 'High Selectivity' : 'Standard Yield';

          var unreacted = 1 - X;
          var R = F * (unreacted / (X + fp * unreacted));
          var recRatio = R / F;
          var ovrConv = 1.0 - (fp * unreacted) / (X + fp * unreacted);
          var compPwr = R * 2.8; // kW approx

          rR.textContent = f(R, 1) + ' kmol/h';
          rRatio.textContent = f(recRatio, 2);
          rOvr.textContent = f(ovrConv * 100, 1) + ' %';
          rComp.textContent = f(compPwr, 0) + ' kW';

          // Flowsheet block schematic
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="180" y="70" width="90" height="60" fill="#dbeafe" stroke="#2563eb" stroke-width="2" rx="4"/>' +
                          '<text x="225" y="105" text-anchor="middle" font-size="11" font-weight="700" fill="#1e40af">Reactor</text>' +
                          '<rect x="340" y="70" width="90" height="60" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="4"/>' +
                          '<text x="385" y="105" text-anchor="middle" font-size="11" font-weight="700" fill="#92400e">Separator</text>' +
                          '<line x1="80" y1="100" x2="180" y2="100" stroke="#334155" stroke-width="3"/>' +
                          '<text x="130" y="90" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">Feed ' + f(F,0) + '</text>' +
                          '<line x1="270" y1="100" x2="340" y2="100" stroke="#334155" stroke-width="3"/>' +
                          '<line x1="430" y1="100" x2="530" y2="100" stroke="#10b981" stroke-width="3"/>' +
                          '<text x="480" y="90" text-anchor="middle" font-size="10" font-weight="700" fill="#047857">Product</text>' +
                          '<path d="M 385 70 L 385 35 L 225 35 L 225 70" fill="none" stroke="#dc2626" stroke-width="3"/>' +
                          '<text x="305" y="27" text-anchor="middle" font-size="10" font-weight="700" fill="#dc2626">Recycle R = ' + f(R,1) + ' kmol/h</text>' +
                          '<text x="300" y="180" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Reactor-Separator-Recycle Loop: Overall Conversion ' + f(ovrConv*100, 1) + '%</text>';
          diag.textContent = 'At per-pass conversion X = ' + f(X * 100, 0) + '% and purge fraction fp = ' + f(fp * 100, 1) + '%, recycle stream flow is ' + f(R, 1) + ' kmol/h (recycle ratio R/F = ' + f(recRatio, 2) + '). Loop achieves overall conversion of ' + f(ovrConv * 100, 1) + '% with recycle compression duty of ' + f(compPwr, 0) + ' kW.';
        }
        [sX, sP, sF, sS].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Pinch Technology & Heat Exchanger Network Synthesis</h3><p class="lead">Simulate minimum approach ΔTmin and derive minimum hot & cold utility targets.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Approach ΔTmin <span><output id="v-dtp">10</output> K</span></label><input type="range" id="s-dtp" min="5" max="35" step="5" value="10"></div>' +
              '<div class="control-group"><label>Process Heat Load <span><output id="v-hload">2400</output> kW</span></label><input type="range" id="s-hload" min="1000" max="5000" step="200" value="2400"></div>' +
              '<div class="control-group"><label>Steam Cost <span><output id="v-scost">$18</output>/GJ</span></label><input type="range" id="s-scost" min="10" max="30" step="2" value="18"></div>' +
              '<div class="control-group"><label>HEX Capital Exponent <span><output id="v-hexexp">0.65</output></span></label><input type="range" id="s-hexexp" min="0.55" max="0.75" step="0.05" value="0.65"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Hot Utility Target QH</span><span class="value" id="r-qhp">0 kW</span><span class="subtext">steam requirement</span></div>' +
              '<div class="readout-card"><span class="label">Cold Utility Target QC</span><span class="value" id="r-qcp">0 kW</span><span class="subtext">cooling water duty</span></div>' +
              '<div class="readout-card"><span class="label">Interchanged Heat Qrec</span><span class="value" id="r-qrecp">0 kW</span><span class="subtext">internal energy recovery</span></div>' +
              '<div class="readout-card"><span class="label">Annual Utility Cost</span><span class="value" id="r-ucost">$0 k/yr</span><span class="subtext">operating steam expense</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdes-u3" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdes-u3"></div>',
      init: function(card) {
        var sDt = card.querySelector('#s-dtp'), vDt = card.querySelector('#v-dtp');
        var sLoad = card.querySelector('#s-hload'), vLoad = card.querySelector('#v-hload');
        var sCost = card.querySelector('#s-scost'), vCost = card.querySelector('#v-scost');
        var sExp = card.querySelector('#s-hexexp'), vExp = card.querySelector('#v-hexexp');
        var rQh = card.querySelector('#r-qhp'), rQc = card.querySelector('#r-qcp');
        var rQrec = card.querySelector('#r-qrecp'), rUcost = card.querySelector('#r-ucost');
        var svg = card.querySelector('#plot-pdes-u3'), diag = card.querySelector('#diag-pdes-u3');

        function update() {
          var dtMin = parseFloat(sDt.value); vDt.textContent = f(dtMin, 0);
          var hload = parseFloat(sLoad.value); vLoad.textContent = f(hload, 0);
          var scost = parseFloat(sCost.value); vCost.textContent = '$' + f(scost, 0);
          var hexexp = parseFloat(sExp.value); vExp.textContent = f(hexexp, 2);

          var recRatio = Math.max(0.2, 0.88 - dtMin * 0.015);
          var Qrec = hload * recRatio;
          var Qh = Math.max(80, (hload - Qrec) * 1.15);
          var Qc = Math.max(80, (hload - Qrec) * 0.85);
          var uCost = (Qh * 3600 * 8000 / 1e6) * (scost / 1e3); // $k/yr

          rQh.textContent = f(Qh, 0) + ' kW';
          rQc.textContent = f(Qc, 0) + ' kW';
          rQrec.textContent = f(Qrec, 0) + ' kW';
          rUcost.textContent = '$' + f(uCost, 0) + ' k/yr';

          // SVG composite curves
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<path d="M 60 50 L 320 130 L 520 155" fill="none" stroke="#ef4444" stroke-width="3"/>' +
                          '<path d="M 100 80 L 360 155 L 560 170" fill="none" stroke="#3b82f6" stroke-width="3"/>' +
                          '<line x1="320" y1="130" x2="320" y2="' + (130 + dtMin * 1.8).toFixed(1) + '" stroke="#d97706" stroke-width="2"/>' +
                          '<text x="330" y="140" font-size="10" font-weight="700" fill="#d97706">ΔTmin = ' + f(dtMin, 0) + ' K</text>' +
                          '<text x="60" y="40" font-size="11" font-weight="700" fill="#ef4444">Hot Composite</text>' +
                          '<text x="560" y="160" text-anchor="end" font-size="11" font-weight="700" fill="#3b82f6">Cold Composite</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Pinch Synthesis: Energy Recovery = ' + f(Qrec, 0) + ' kW (' + f(recRatio*100, 1) + '%)</text>';
          diag.textContent = 'Minimum approach ΔTmin = ' + f(dtMin, 0) + ' K yields maximum heat recovery of ' + f(Qrec, 0) + ' kW. External steam target is ' + f(Qh, 0) + ' kW ($' + f(uCost, 0) + ' k/yr) and cooling water requirement is ' + f(Qc, 0) + ' kW. Narrowing ΔTmin lowers utility cost at the expense of additional heat exchanger area.';
        }
        [sDt, sLoad, sCost, sExp].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Shell-and-Tube Heat Exchanger Preliminary Sizing</h3><p class="lead">Simulate thermal duty Q, LMTD, overall heat transfer coefficient U, and tube area.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Duty Q <span><output id="v-hexq">850</output> kW</span></label><input type="range" id="s-hexq" min="200" max="3000" step="50" value="850"></div>' +
              '<div class="control-group"><label>Overall Coeff U <span><output id="v-hexu">450</output> W/m²·K</span></label><input type="range" id="s-hexu" min="150" max="1200" step="50" value="450"></div>' +
              '<div class="control-group"><label>Log Mean Temp LMTD <span><output id="v-lmtd">28</output> K</span></label><input type="range" id="s-lmtd" min="10" max="80" step="2" value="28"></div>' +
              '<div class="control-group"><label>Tube Diameter dt <span><output id="v-dtube">19.05</output> mm (3/4")</span></label><input type="range" id="s-dtube" min="1" max="2" step="1" value="1"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Required Area A</span><span class="value" id="r-hexarea">0 m²</span><span class="subtext">Q / (U · LMTD)</span></div>' +
              '<div class="readout-card"><span class="label">Tube Count Nt</span><span class="value" id="r-tcount">0 Tubes</span><span class="subtext">4.88 m (16 ft) tubes</span></div>' +
              '<div class="readout-card"><span class="label">Shell Diameter Ds</span><span class="value" id="r-shellds">0 mm</span><span class="subtext">TEMA standard bundle</span></div>' +
              '<div class="readout-card"><span class="label">TEMA Exchanger Class</span><span class="value" id="r-temaclass">BEM Shell</span><span class="subtext">fixed tubesheet</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdes-u4" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdes-u4"></div>',
      init: function(card) {
        var sQ = card.querySelector('#s-hexq'), vQ = card.querySelector('#v-hexq');
        var sU = card.querySelector('#s-hexu'), vU = card.querySelector('#v-hexu');
        var sL = card.querySelector('#s-lmtd'), vL = card.querySelector('#v-lmtd');
        var sD = card.querySelector('#s-dtube'), vD = card.querySelector('#v-dtube');
        var rA = card.querySelector('#r-hexarea'), rNt = card.querySelector('#r-tcount');
        var rDs = card.querySelector('#r-shellds'), rTEMA = card.querySelector('#r-temaclass');
        var svg = card.querySelector('#plot-pdes-u4'), diag = card.querySelector('#diag-pdes-u4');

        function update() {
          var Q = parseFloat(sQ.value) * 1e3; vQ.textContent = f(Q / 1e3, 0);
          var U = parseFloat(sU.value); vU.textContent = f(U, 0);
          var lmtd = parseFloat(sL.value); vL.textContent = f(lmtd, 0);
          var isSmallTube = parseInt(sD.value, 10) === 1;
          vD.textContent = isSmallTube ? '19.05 mm (3/4")' : '25.40 mm (1")';

          var area = Q / (U * lmtd);
          var tubeOD = isSmallTube ? 0.01905 : 0.0254;
          var tubeLen = 4.88; // m
          var tubeArea = Math.PI * tubeOD * tubeLen;
          var Nt = Math.ceil(area / tubeArea);
          var Ds = Math.round(Math.sqrt((Nt * 1.25 * tubeOD * tubeOD) / 0.785) * 1000 * 1.1);

          rA.textContent = f(area, 1) + ' m²';
          rNt.textContent = Nt + ' Tubes';
          rDs.textContent = Ds + ' mm';
          rTEMA.textContent = Ds > 600 ? 'AES (Floating Head)' : 'BEM (Fixed Tubesheet)';

          // SVG shell & tube bundle schematic
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="140" y="50" width="320" height="100" fill="#e2e8f0" stroke="#334155" stroke-width="2" rx="12"/>' +
                          '<rect x="170" y="65" width="260" height="70" fill="#bae6fd" opacity="0.6" stroke="#0284c7" stroke-width="1.5"/>' +
                          '<line x1="170" y1="80" x2="430" y2="80" stroke="#0284c7" stroke-width="2"/>' +
                          '<line x1="170" y1="100" x2="430" y2="100" stroke="#0284c7" stroke-width="2"/>' +
                          '<line x1="170" y1="120" x2="430" y2="120" stroke="#0284c7" stroke-width="2"/>' +
                          '<rect x="230" y="50" width="8" height="60" fill="#64748b"/>' +
                          '<rect x="310" y="90" width="8" height="60" fill="#64748b"/>' +
                          '<rect x="390" y="50" width="8" height="60" fill="#64748b"/>' +
                          '<text x="300" y="30" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Shell-and-Tube Exchanger: Area = ' + f(area,1) + ' m² (Ds = ' + Ds + ' mm)</text>' +
                          '<text x="300" y="175" text-anchor="middle" font-size="11" fill="#475569">Bundle: ' + Nt + ' Tubes (' + (isSmallTube ? '3/4"' : '1"') + ' OD × 4.88 m)</text>';
          diag.textContent = 'For thermal duty Q = ' + f(Q / 1e3, 0) + ' kW with U = ' + f(U, 0) + ' W/m²·K and LMTD = ' + f(lmtd, 0) + ' K, required heat transfer area is ' + f(area, 1) + ' m². Preliminary mechanical bundle requires ' + Nt + ' tubes inside an estimated shell diameter of Ds = ' + Ds + ' mm.';
        }
        [sQ, sU, sL, sD].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Plant Equipment Layout & Safety Separation Spacing</h3><p class="lead">Simulate safe separation distances, pipe rack corridors, and flare exclusion zones.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Storage Tank Capacity <span><output id="v-stcap">5000</output> m³</span></label><input type="range" id="s-stcap" min="1000" max="25000" step="1000" value="5000"></div>' +
              '<div class="control-group"><label>Process Fluid Hazard <span><output id="v-fldhaz">Flammable (Cat 1)</output></span></label><input type="range" id="s-fldhaz" min="1" max="2" step="1" value="1"></div>' +
              '<div class="control-group"><label>Flare Heat Radiation <span><output id="v-flhrad">4.73</output> kW/m²</span></label><input type="range" id="s-flhrad" min="1.58" max="9.46" step="1.0" value="4.73"></div>' +
              '<div class="control-group"><label>Pipe Rack Width <span><output id="v-prwidth">6.0</output> m</span></label><input type="range" id="s-prwidth" min="3.0" max="12.0" step="1.0" value="6.0"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Tank Spacing (D)</span><span class="value" id="r-tanksp">30 m</span><span class="subtext">NFPA 30 requirement</span></div>' +
              '<div class="readout-card"><span class="label">Flare Exclusion R</span><span class="value" id="r-flarer">120 m</span><span class="subtext">sterile radius limit</span></div>' +
              '<div class="readout-card"><span class="label">Control Room Buffer</span><span class="value" id="r-crbuff">60 m</span><span class="subtext">blast wall setback</span></div>' +
              '<div class="readout-card"><span class="label">Plot Area Footprint</span><span class="value" id="r-plotarea">2.5 ha</span><span class="subtext">total battery limits</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdes-u5" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdes-u5"></div>',
      init: function(card) {
        var sCap = card.querySelector('#s-stcap'), vCap = card.querySelector('#v-stcap');
        var sHaz = card.querySelector('#s-fldhaz'), vHaz = card.querySelector('#v-fldhaz');
        var sRad = card.querySelector('#s-flhrad'), vRad = card.querySelector('#v-flhrad');
        var sW = card.querySelector('#s-prwidth'), vW = card.querySelector('#v-prwidth');
        var rSp = card.querySelector('#r-tanksp'), rFl = card.querySelector('#r-flarer');
        var rCr = card.querySelector('#r-crbuff'), rPlot = card.querySelector('#r-plotarea');
        var svg = card.querySelector('#plot-pdes-u5'), diag = card.querySelector('#diag-pdes-u5');

        function update() {
          var cap = parseFloat(sCap.value); vCap.textContent = f(cap, 0);
          var isFlam = parseInt(sHaz.value, 10) === 1;
          vHaz.textContent = isFlam ? 'Flammable (Cat 1)' : 'Combustible (Cat 3)';
          var rad = parseFloat(sRad.value); vRad.textContent = f(rad, 2);
          var prw = parseFloat(sW.value); vW.textContent = f(prw, 1);

          var tankDiam = Math.pow((4 * cap) / (Math.PI * 12), 0.5);
          var spacing = isFlam ? tankDiam * 1.0 : tankDiam * 0.5;
          var flareR = Math.sqrt((15000) / (4 * Math.PI * rad));
          var crBuffer = isFlam ? 60 : 30;
          var plotHa = (cap / 2000) * 0.8 + 1.2;

          rSp.textContent = f(spacing, 0) + ' m';
          rFl.textContent = f(flareR, 0) + ' m';
          rCr.textContent = f(crBuffer, 0) + ' m';
          rPlot.textContent = f(plotHa, 1) + ' ha';

          // SVG Plot Layout Map
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="60" y="50" width="100" height="90" fill="#fed7aa" stroke="#ea580c" stroke-width="2" rx="4"/>' +
                          '<text x="110" y="95" text-anchor="middle" font-size="11" font-weight="700" fill="#9a3412">Process Unit</text>' +
                          '<circle cx="270" cy="95" r="35" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>' +
                          '<circle cx="370" cy="95" r="35" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>' +
                          '<line x1="305" y1="95" x2="335" y2="95" stroke="#ef4444" stroke-width="2"/>' +
                          '<text x="320" y="90" text-anchor="middle" font-size="9" fill="#dc2626">' + f(spacing, 0) + 'm</text>' +
                          '<circle cx="510" cy="95" r="8" fill="#ef4444"/>' +
                          '<circle cx="510" cy="95" r="45" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4"/>' +
                          '<text x="510" y="160" text-anchor="middle" font-size="10" font-weight="700" fill="#dc2626">Flare Sterile Radius: ' + f(flareR, 0) + 'm</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Plant Layout & Safety Separation Spacing (Plot: ' + f(plotHa, 1) + ' ha)</text>';
          diag.textContent = 'Safety spacing audit: Storage tank diameter is ' + f(tankDiam, 1) + ' m; NFPA separation distance is ' + f(spacing, 0) + ' m. Flare exclusion zone radius is ' + f(flareR, 0) + ' m at maximum thermal flux threshold. Total inside-battery-limits plot footprint is ' + f(plotHa, 1) + ' hectares.';
        }
        [sCap, sHaz, sRad, sW].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Guthrie Bare-Module Factorial Capital Cost Estimation</h3><p class="lead">Simulate base equipment purchase cost Cp0, bare-module factor FBM, and total CAPEX.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Major Equipment Base Cp0 <span><output id="v-cp0">$12.0</output> M</span></label><input type="range" id="s-cp0" min="2.0" max="40.0" step="1.0" value="12.0"></div>' +
              '<div class="control-group"><label>Alloy MOC Factor <span><output id="v-fmat">Carbon Steel (1.0)</output></span></label><input type="range" id="s-fmat" min="1.0" max="2.8" step="0.2" value="1.0"></div>' +
              '<div class="control-group"><label>Design Pressure Factor <span><output id="v-fp">1.0 bar (1.0)</output></span></label><input type="range" id="s-fp" min="1.0" max="2.2" step="0.2" value="1.0"></div>' +
              '<div class="control-group"><label>Contingency & OSBL <span><output id="v-cont">40%</output></span></label><input type="range" id="s-cont" min="20" max="60" step="5" value="40"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Bare Module CBM</span><span class="value" id="r-cbm">$0 M</span><span class="subtext">installed direct + indirect</span></div>' +
              '<div class="readout-card"><span class="label">Bare Module FBM</span><span class="value" id="r-fbm">0.00</span><span class="subtext">CBM / Cp0 factor</span></div>' +
              '<div class="readout-card"><span class="label">Total CAPEX (CTM)</span><span class="value" id="r-ctm">$0 M</span><span class="subtext">total module cost</span></div>' +
              '<div class="readout-card"><span class="label">Grassroots Cost</span><span class="value" id="r-cgr">$0 M</span><span class="subtext">greenfield site multiplier</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdes-u6" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdes-u6"></div>',
      init: function(card) {
        var sCp = card.querySelector('#s-cp0'), vCp = card.querySelector('#v-cp0');
        var sM = card.querySelector('#s-fmat'), vM = card.querySelector('#v-fmat');
        var sP = card.querySelector('#s-fp'), vP = card.querySelector('#v-fp');
        var sC = card.querySelector('#s-cont'), vC = card.querySelector('#v-cont');
        var rCbm = card.querySelector('#r-cbm'), rFbm = card.querySelector('#r-fbm');
        var rCtm = card.querySelector('#r-ctm'), rCgr = card.querySelector('#r-cgr');
        var svg = card.querySelector('#plot-pdes-u6'), diag = card.querySelector('#diag-pdes-u6');

        function update() {
          var cp0 = parseFloat(sCp.value); vCp.textContent = '$' + f(cp0, 1) + ' M';
          var fmat = parseFloat(sM.value);
          vM.textContent = fmat > 2.0 ? 'Hastelloy/Titanium (' + f(fmat, 1) + ')' : (fmat > 1.2 ? 'SS316 (' + f(fmat, 1) + ')' : 'Carbon Steel (1.0)');
          var fp = parseFloat(sP.value);
          vP.textContent = fp > 1.6 ? 'High P >50 bar (' + f(fp, 1) + ')' : (fp > 1.1 ? 'Medium P 15 bar (' + f(fp, 1) + ')' : 'Near Atm (1.0)');
          var cont = parseFloat(sC.value) / 100; vC.textContent = f(cont * 100, 0) + '%';

          var baseFBM = 3.3;
          var fbm = baseFBM * (0.6 + 0.25 * fmat + 0.15 * fp);
          var cbm = cp0 * fbm;
          var ctm = cbm * (1.0 + cont);
          var cgr = ctm * 1.35;

          rCbm.textContent = '$' + f(cbm, 1) + ' M';
          rFbm.textContent = f(fbm, 2);
          rCtm.textContent = '$' + f(ctm, 1) + ' M';
          rCgr.textContent = '$' + f(cgr, 1) + ' M';

          // SVG Cost Stack Bar Chart
          var barW = 440;
          var pEquip = (cp0 / cgr) * barW;
          var pModule = ((cbm - cp0) / cgr) * barW;
          var pCont = ((ctm - cbm) / cgr) * barW;
          var pGrass = ((cgr - ctm) / cgr) * barW;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="60" width="' + pEquip.toFixed(1) + '" height="35" fill="#3b82f6" rx="2"/>' +
                          '<rect x="' + (80 + pEquip).toFixed(1) + '" y="60" width="' + pModule.toFixed(1) + '" height="35" fill="#0284c7" rx="2"/>' +
                          '<rect x="' + (80 + pEquip + pModule).toFixed(1) + '" y="60" width="' + pCont.toFixed(1) + '" height="35" fill="#f59e0b" rx="2"/>' +
                          '<rect x="' + (80 + pEquip + pModule + pCont).toFixed(1) + '" y="60" width="' + pGrass.toFixed(1) + '" height="35" fill="#10b981" rx="2"/>' +
                          '<text x="80" y="125" font-size="10" fill="#1e40af">Purchased Cp0: $' + f(cp0,1) + 'M</text>' +
                          '<text x="210" y="125" font-size="10" fill="#0369a1">Module Piping & Inst</text>' +
                          '<text x="360" y="125" font-size="10" fill="#b45309">Contingency</text>' +
                          '<text x="470" y="125" font-size="10" fill="#047857">Site & OSBL</text>' +
                          '<text x="300" y="30" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Guthrie Factorial Cost Breakdown: Total Grassroots = $' + f(cgr, 1) + ' M</text>';
          diag.textContent = 'Guthrie bare module factorial scaling: Major equipment purchase cost of $' + f(cp0, 1) + ' M with composite module factor FBM = ' + f(fbm, 2) + ' yields bare-module installed cost CBM = $' + f(cbm, 1) + ' M. Total grass-roots capital expenditure is estimated at $' + f(cgr, 1) + ' M.';
        }
        [sCp, sM, sP, sC].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>10-Year Discounted Cash Flow NPV & Sensitivity Analysis</h3><p class="lead">Simulate plant cash flows, discount rate hurdle, Net Present Value, and payback period.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Capital Investment CAPEX <span><output id="v-dcfcap">$35</output> M</span></label><input type="range" id="s-dcfcap" min="10" max="80" step="5" value="35"></div>' +
              '<div class="control-group"><label>Net Annual Revenue <span><output id="v-dcfrev">$14.0</output> M/yr</span></label><input type="range" id="s-dcfrev" min="4.0" max="30.0" step="1.0" value="14.0"></div>' +
              '<div class="control-group"><label>Discount Rate r <span><output id="v-dcfr">10%</output></span></label><input type="range" id="s-dcfr" min="6" max="20" step="1" value="10"></div>' +
              '<div class="control-group"><label>Tax Rate <span><output id="v-dcftax">25%</output></span></label><input type="range" id="s-dcftax" min="15" max="35" step="5" value="25"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">10-Year NPV</span><span class="value" id="r-dcfnpv">$0 M</span><span class="subtext">discounted net worth</span></div>' +
              '<div class="readout-card"><span class="label">Internal Rate (IRR)</span><span class="value" id="r-dcfirr">0.0%</span><span class="subtext">discount rate for NPV=0</span></div>' +
              '<div class="readout-card"><span class="label">Payback Period</span><span class="value" id="r-dcfpay">0.0 yr</span><span class="subtext">undiscounted capital return</span></div>' +
              '<div class="readout-card"><span class="label">Project Decision</span><span class="value" id="r-dcfdec">Approved</span><span class="subtext">hurdle rate check</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdes-u7" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdes-u7"></div>',
      init: function(card) {
        var sC = card.querySelector('#s-dcfcap'), vC = card.querySelector('#v-dcfcap');
        var sR = card.querySelector('#s-dcfrev'), vR = card.querySelector('#v-dcfrev');
        var sDisc = card.querySelector('#s-dcfr'), vDisc = card.querySelector('#v-dcfr');
        var sT = card.querySelector('#s-dcftax'), vT = card.querySelector('#v-dcftax');
        var rNpv = card.querySelector('#r-dcfnpv'), rIrr = card.querySelector('#r-dcfirr');
        var rPay = card.querySelector('#r-dcfpay'), rDec = card.querySelector('#r-dcfdec');
        var svg = card.querySelector('#plot-pdes-u7'), diag = card.querySelector('#diag-pdes-u7');

        function update() {
          var capex = parseFloat(sC.value); vC.textContent = '$' + f(capex, 0) + ' M';
          var rev = parseFloat(sR.value); vR.textContent = '$' + f(rev, 1) + ' M/yr';
          var r = parseFloat(sDisc.value) / 100; vDisc.textContent = f(r * 100, 0) + '%';
          var tax = parseFloat(sT.value) / 100; vT.textContent = f(tax * 100, 0) + '%';

          var afterTaxCF = rev * (1 - tax) + (capex / 10) * tax; // with straight-line depreciation
          var npv = -capex;
          for (var yr = 1; yr <= 10; yr++) {
            npv += afterTaxCF / Math.pow(1 + r, yr);
          }
          var irr = (afterTaxCF / capex) * 100 * 0.75; // approx IRR
          var payback = capex / afterTaxCF;

          rNpv.textContent = '$' + f(npv, 1) + ' M';
          rNpv.style.color = npv > 0 ? '#15803d' : '#dc2626';
          rIrr.textContent = f(irr, 1) + ' %';
          rPay.textContent = payback < 15 ? f(payback, 1) + ' yr' : '>15 yr';
          var approved = npv > 0 && irr > r * 100;
          rDec.textContent = approved ? 'Proceed (NPV > 0)' : 'Reject / Redesign';
          rDec.style.color = approved ? '#15803d' : '#dc2626';

          // SVG cash flow curve
          var dPath = 'M 60 ' + (170 - ((-capex + 60) / 140) * 130).toFixed(1) + ' ';
          var cum = -capex;
          for (var yr = 1; yr <= 10; yr++) {
            cum += afterTaxCF;
            var x_px = 60 + (yr / 10.0) * 480;
            var y_px = 170 - ((cum + 60) / 140) * 130;
            y_px = Math.min(170, Math.max(20, y_px));
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          var zero_y = 170 - (60 / 140) * 130;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="' + zero_y.toFixed(1) + '" x2="540" y2="' + zero_y.toFixed(1) + '" stroke="#94a3b8" stroke-dasharray="4"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="' + (npv > 0 ? '#059669' : '#dc2626') + '" stroke-width="3"/>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Operating Year (0 to 10)</text>' +
                          '<text x="60" y="30" font-size="11" fill="#64748b">Cumulative Cash ($M)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Cumulative DCF: 10-Yr NPV = $' + f(npv, 1) + ' M (Payback: ' + f(payback, 1) + ' yr)</text>';
          diag.textContent = 'Discounted cash flow profitability: At ' + f(r * 100, 0) + '% hurdle rate, 10-year Net Present Value is $' + f(npv, 1) + ' M with an estimated IRR of ' + f(irr, 1) + '%. Undiscounted capital recovery occurs in ' + f(payback, 1) + ' years.';
        }
        [sC, sR, sDisc, sT].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Stage-Gate Engineering Milestone & Deliverables Schedule</h3><p class="lead">Simulate Front-End Engineering Design (FEED), FEL stage-gates, and EPC expenditure curves.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Project Schedule <span><output id="v-sched">36</output> Months</span></label><input type="range" id="s-sched" min="18" max="60" step="3" value="36"></div>' +
              '<div class="control-group"><label>Gate Review Status <span><output id="v-gatestat">Gate 3 (FEED Approved)</output></span></label><input type="range" id="s-gatestat" min="1" max="4" step="1" value="3"></div>' +
              '<div class="control-group"><label>Design Maturity <span><output id="v-p&id">Class 3 (±15%)</output></span></label><input type="range" id="s-p&id" min="1" max="3" step="1" value="2"></div>' +
              '<div class="control-group"><label>Contingency Buffer <span><output id="v-buf">15%</output></span></label><input type="range" id="s-buf" min="5" max="30" step="5" value="15"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Current Phase</span><span class="value" id="r-cphase">Detailed EPC</span><span class="subtext">execution status</span></div>' +
              '<div class="readout-card"><span class="label">Spent to Date</span><span class="value" id="r-spent">18%</span><span class="subtext">cumulative spend</span></div>' +
              '<div class="readout-card"><span class="label">Estimate Class</span><span class="value" id="r-estclass">AACE Class 3</span><span class="subtext">accuracy band</span></div>' +
              '<div class="readout-card"><span class="label">Major Deliverable</span><span class="value" id="r-deliv">P&IDs & MTO</span><span class="subtext">current work package</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdes-u8" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdes-u8"></div>',
      init: function(card) {
        var sS = card.querySelector('#s-sched'), vS = card.querySelector('#v-sched');
        var sG = card.querySelector('#s-gatestat'), vG = card.querySelector('#v-gatestat');
        var sM = card.querySelector('#s-p&id'), vM = card.querySelector('#v-p&id');
        var sB = card.querySelector('#s-buf'), vB = card.querySelector('#v-buf');
        var rP = card.querySelector('#r-cphase'), rSp = card.querySelector('#r-spent');
        var rCl = card.querySelector('#r-estclass'), rDel = card.querySelector('#r-deliv');
        var svg = card.querySelector('#plot-pdes-u8'), diag = card.querySelector('#diag-pdes-u8');

        function update() {
          var months = parseInt(sS.value, 10); vS.textContent = months;
          var gate = parseInt(sG.value, 10);
          var gateNames = ['Gate 1 (Concept FEL-1)', 'Gate 2 (Feasibility FEL-2)', 'Gate 3 (FEED Approved)', 'Gate 4 (EPC Construction)'];
          vG.textContent = gateNames[gate - 1];
          var mat = parseInt(sM.value, 10);
          vM.textContent = mat === 1 ? 'Class 4 (±30%)' : (mat === 2 ? 'Class 3 (±15%)' : 'Class 2 (±10%)');
          var buf = parseFloat(sB.value); vB.textContent = buf + '%';

          var spent = gate === 1 ? 3 : (gate === 2 ? 8 : (gate === 3 ? 18 : 65));
          rP.textContent = gate === 4 ? 'EPC Construction' : (gate === 3 ? 'Detailed EPC' : 'Front-End Study');
          rSp.textContent = spent + ' %';
          rCl.textContent = 'AACE Class ' + (5 - gate);
          rDel.textContent = gate === 1 ? 'Block Flow & Feasibility' : (gate === 2 ? 'PFD & Utility Balance' : (gate === 3 ? 'P&IDs & Equipment Datasheets' : 'Fabrication & Commissioning'));

          // SVG S-curve for EPC expenditure
          var dPath = 'M 60 170 ';
          for (var m = 0; m <= months; m += months / 30) {
            var frac = m / months;
            var cumSpend = 100 / (1 + Math.exp(-8 * (frac - 0.5)));
            var x_px = 60 + (m / months) * 480;
            var y_px = 170 - (cumSpend / 100) * 140;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<circle cx="' + (60 + (spent / 100) * 480).toFixed(1) + '" cy="' + (170 - (spent / 100) * 140).toFixed(1) + '" r="6" fill="#ef4444"/>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Project Month (0 to ' + months + ')</text>' +
                          '<text x="60" y="25" font-size="11" fill="#64748b">Cumulative Spend S-Curve (%)</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Capital Stage-Gate Milestone Progression: ' + gateNames[gate-1] + '</text>';
          diag.textContent = 'Engineering execution milestone: Project is at ' + gateNames[gate - 1] + '. Cumulative expenditure to date is ' + spent + '%. Primary deliverables include ' + (gate === 3 ? 'approved piping and instrumentation diagrams (P&IDs) and procurement datasheets.' : 'process flow diagrams and mass/energy balances.');
        }
        [sS, sG, sM, sB].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    }
  ];
""" + get_engine_footer(8)

# =========================================================================
# 2. Process Safety
# =========================================================================
def build_psafe_sims():
    return """/* Process Safety Interactive Simulation Suite */
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
""" + get_engine_footer(8)

# =========================================================================
# 3. Biochemical Engineering
# =========================================================================
def build_bio_sims():
    return """/* Biochemical Engineering Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Microbial Cell Mass Yield & Elemental Stoichiometry</h3><p class="lead">Simulate substrate-to-biomass yield YX/S, respiratory quotient RQ, and theoretical metabolic limits.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Glucose Substrate S0 <span><output id="v-sub0">25.0</output> g/L</span></label><input type="range" id="s-sub0" min="5.0" max="80.0" step="5.0" value="25.0"></div>' +
              '<div class="control-group"><label>Biomass Yield YX/S <span><output id="v-yxs">0.48</output> g/g</span></label><input type="range" id="s-yxs" min="0.25" max="0.65" step="0.01" value="0.48"></div>' +
              '<div class="control-group"><label>Nitrogen Source <span><output id="v-nsource">Ammonia (NH3)</output></span></label><input type="range" id="s-nsource" min="1" max="2" step="1" value="1"></div>' +
              '<div class="control-group"><label>Maintenance Coeff ms <span><output id="v-ms">0.02</output> g/g·h</span></label><input type="range" id="s-ms" min="0.01" max="0.08" step="0.01" value="0.02"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Final Biomass X</span><span class="value" id="r-bioX">0.0 g/L</span><span class="subtext">dry cell weight</span></div>' +
              '<div class="readout-card"><span class="label">Respiratory Quotient RQ</span><span class="value" id="r-bioRQ">1.05</span><span class="subtext">CO2 produced / O2 consumed</span></div>' +
              '<div class="readout-card"><span class="label">Oxygen Demand YO2</span><span class="value" id="r-bioO2">0.0 g/g</span><span class="subtext">O2 per g biomass</span></div>' +
              '<div class="readout-card"><span class="label">Carbon Recovery</span><span class="value" id="r-bioC">98.5%</span><span class="subtext">elemental closure</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-bio-u1" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-bio-u1"></div>',
      init: function(card) {
        var sS = card.querySelector('#s-sub0'), vS = card.querySelector('#v-sub0');
        var sY = card.querySelector('#s-yxs'), vY = card.querySelector('#v-yxs');
        var sN = card.querySelector('#s-nsource'), vN = card.querySelector('#v-nsource');
        var sM = card.querySelector('#s-ms'), vM = card.querySelector('#v-ms');
        var rX = card.querySelector('#r-bioX'), rRQ = card.querySelector('#r-bioRQ');
        var rO2 = card.querySelector('#r-bioO2'), rC = card.querySelector('#r-bioC');
        var svg = card.querySelector('#plot-bio-u1'), diag = card.querySelector('#diag-bio-u1');

        function update() {
          var S0 = parseFloat(sS.value); vS.textContent = f(S0, 1);
          var Yxs = parseFloat(sY.value); vY.textContent = f(Yxs, 2);
          var isNH3 = parseInt(sN.value, 10) === 1;
          vN.textContent = isNH3 ? 'Ammonia (NH3)' : 'Nitrate (NO3-)';
          var ms = parseFloat(sM.value); vM.textContent = f(ms, 2);

          var X_final = S0 * Yxs * 0.94;
          var YO2 = (1.07 / Yxs) - 0.45;
          YO2 = Math.max(0.2, YO2);
          var RQ = isNH3 ? (1.0 + (0.5 - Yxs) * 0.3) : (0.85 + (0.5 - Yxs) * 0.2);

          rX.textContent = f(X_final, 1) + ' g/L';
          rRQ.textContent = f(RQ, 2);
          rO2.textContent = f(YO2, 2) + ' g O2/g X';
          rC.textContent = '99.1%';

          // SVG Metabolic carbon allocation bar
          var cBiomass = Yxs * 0.48 * 100;
          var cCO2 = (1.0 - Yxs * 0.48) * 0.85 * 100;
          var cByprod = 100 - cBiomass - cCO2;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="60" width="' + (cBiomass * 4.4).toFixed(1) + '" height="35" fill="#10b981" rx="2"/>' +
                          '<rect x="' + (80 + cBiomass * 4.4).toFixed(1) + '" y="60" width="' + (cCO2 * 4.4).toFixed(1) + '" height="35" fill="#3b82f6" rx="2"/>' +
                          '<rect x="' + (80 + (cBiomass + cCO2) * 4.4).toFixed(1) + '" y="60" width="' + (cByprod * 4.4).toFixed(1) + '" height="35" fill="#f59e0b" rx="2"/>' +
                          '<text x="80" y="125" font-size="11" fill="#047857">Biomass Carbon: ' + f(cBiomass, 1) + '%</text>' +
                          '<text x="280" y="125" font-size="11" fill="#1e40af">Respiration CO2: ' + f(cCO2, 1) + '%</text>' +
                          '<text x="520" y="125" text-anchor="end" font-size="11" fill="#b45309">Metabolites: ' + f(cByprod, 1) + '%</text>' +
                          '<text x="300" y="30" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Elemental Carbon Balance: Biomass Yield YX/S = ' + f(Yxs, 2) + ' g/g</text>';
          diag.textContent = 'From ' + f(S0, 1) + ' g/L glucose substrate, the stoichiometric biomass yield of ' + f(Yxs, 2) + ' g/g produces ' + f(X_final, 1) + ' g/L dry cell weight. Respiratory quotient RQ is ' + f(RQ, 2) + ' with specific oxygen demand of ' + f(YO2, 2) + ' g O2/g cells.';
        }
        [sS, sY, sN, sM].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Michaelis-Menten Enzyme Kinetics & Inhibition</h3><p class="lead">Simulate maximum velocity Vmax, Michaelis constant Km, and competitive/non-competitive inhibition.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Substrate Conc [S] <span><output id="v-enzs">5.0</output> mM</span></label><input type="range" id="s-enzs" min="0.2" max="30.0" step="0.5" value="5.0"></div>' +
              '<div class="control-group"><label>Max Velocity Vmax <span><output id="v-vmax">12.0</output> μmol/min</span></label><input type="range" id="s-vmax" min="2.0" max="30.0" step="1.0" value="12.0"></div>' +
              '<div class="control-group"><label>Michaelis Constant Km <span><output id="v-km">2.5</output> mM</span></label><input type="range" id="s-km" min="0.5" max="10.0" step="0.5" value="2.5"></div>' +
              '<div class="control-group"><label>Inhibitor Type <span><output id="v-inhtype">No Inhibitor</output></span></label><input type="range" id="s-inhtype" min="0" max="2" step="1" value="0"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Reaction Velocity V</span><span class="value" id="r-enzv">0.0 μmol/min</span><span class="subtext">instantaneous rate</span></div>' +
              '<div class="readout-card"><span class="label">Apparent Km,app</span><span class="value" id="r-kmapp">0.0 mM</span><span class="subtext">inhibition modulated</span></div>' +
              '<div class="readout-card"><span class="label">Apparent Vmax,app</span><span class="value" id="r-vmaxapp">0.0</span><span class="subtext">active catalytic limit</span></div>' +
              '<div class="readout-card"><span class="label">Site Saturation</span><span class="value" id="r-enzsat">0%</span><span class="subtext">ES complex fraction</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-bio-u2" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-bio-u2"></div>',
      init: function(card) {
        var sS = card.querySelector('#s-enzs'), vS = card.querySelector('#v-enzs');
        var sV = card.querySelector('#s-vmax'), vV = card.querySelector('#v-vmax');
        var sKm = card.querySelector('#s-km'), vKm = card.querySelector('#v-km');
        var sInh = card.querySelector('#s-inhtype'), vInh = card.querySelector('#v-inhtype');
        var rV = card.querySelector('#r-enzv'), rKm = card.querySelector('#r-kmapp');
        var rVapp = card.querySelector('#r-vmaxapp'), rSat = card.querySelector('#r-enzsat');
        var svg = card.querySelector('#plot-bio-u2'), diag = card.querySelector('#diag-bio-u2');

        function update() {
          var S = parseFloat(sS.value); vS.textContent = f(S, 1);
          var Vmax = parseFloat(sV.value); vV.textContent = f(Vmax, 1);
          var Km = parseFloat(sKm.value); vKm.textContent = f(Km, 1);
          var inh = parseInt(sInh.value, 10);
          vInh.textContent = inh === 0 ? 'No Inhibitor' : (inh === 1 ? 'Competitive (Km Shifts)' : 'Non-Competitive (Vmax Drops)');

          var I = 2.0; var Ki = 1.5;
          var Km_app = Km;
          var Vmax_app = Vmax;

          if (inh === 1) { // Competitive
            Km_app = Km * (1 + I / Ki);
          } else if (inh === 2) { // Non-competitive
            Vmax_app = Vmax / (1 + I / Ki);
          }

          var V = (Vmax_app * S) / (Km_app + S);
          var sat = (S / (Km_app + S)) * 100;

          rV.textContent = f(V, 2) + ' μmol/min';
          rKm.textContent = f(Km_app, 2) + ' mM';
          rVapp.textContent = f(Vmax_app, 1) + ' μmol/min';
          rSat.textContent = f(sat, 1) + ' %';

          // SVG Michaelis-Menten Rate Curve
          var dPath = 'M 60 170 ';
          for (var s_i = 0.2; s_i <= 30; s_i += 0.8) {
            var v_i = (Vmax_app * s_i) / (Km_app + s_i);
            var x_px = 60 + ((s_i - 0.2) / 29.8) * 480;
            var y_px = 170 - (v_i / (Vmax * 1.1)) * 140;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          var cur_x = 60 + ((S - 0.2) / 29.8) * 480;
          var cur_y = 170 - (V / (Vmax * 1.1)) * 140;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="60" y1="30" x2="60" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="60" y1="' + (170 - (Vmax_app / (Vmax * 1.1)) * 140).toFixed(1) + '" x2="540" y2="' + (170 - (Vmax_app / (Vmax * 1.1)) * 140).toFixed(1) + '" stroke="#cbd5e1" stroke-dasharray="4"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<circle cx="' + cur_x.toFixed(1) + '" cy="' + cur_y.toFixed(1) + '" r="6" fill="#ef4444" stroke="#fff" stroke-width="2"/>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Substrate Concentration [S] (mM)</text>' +
                          '<text x="50" y="30" font-size="11" fill="#64748b">Velocity V (μmol/min)</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Michaelis-Menten Kinetics: V = ' + f(V, 2) + ' μmol/min (Km,app = ' + f(Km_app, 2) + ' mM)</text>';
          diag.textContent = 'Enzyme kinetics: At [S] = ' + f(S, 1) + ' mM, reaction velocity is ' + f(V, 2) + ' μmol/min (' + f(sat, 1) + '% active site saturation). ' + (inh === 1 ? 'Competitive inhibitor increases Km,app to ' + f(Km_app, 2) + ' mM without lowering true Vmax.' : (inh === 2 ? 'Non-competitive inhibitor lowers Vmax,app to ' + f(Vmax_app, 1) + ' μmol/min.' : 'Uninhibited hyperbolic saturation profile.'));
        }
        [sS, sV, sKm, sInh].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Monod Microbial Growth & Continuous Chemostat Washout</h3><p class="lead">Simulate dilution rate D, specific growth rate μ(S), and identify critical washout Dcrit.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Dilution Rate D <span><output id="v-dil">0.25</output> h⁻¹</span></label><input type="range" id="s-dil" min="0.05" max="0.80" step="0.02" value="0.25"></div>' +
              '<div class="control-group"><label>Max Growth Rate μmax <span><output id="v-mumax">0.50</output> h⁻¹</span></label><input type="range" id="s-mumax" min="0.20" max="0.90" step="0.05" value="0.50"></div>' +
              '<div class="control-group"><label>Monod Constant Ks <span><output id="v-monodks">0.15</output> g/L</span></label><input type="range" id="s-monodks" min="0.02" max="0.50" step="0.02" value="0.15"></div>' +
              '<div class="control-group"><label>Feed Substrate Sin <span><output id="v-sin">20.0</output> g/L</span></label><input type="range" id="s-sin" min="5.0" max="50.0" step="5.0" value="20.0"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Biomass Output X</span><span class="value" id="r-chemoX">0.0 g/L</span><span class="subtext">chemostat density</span></div>' +
              '<div class="readout-card"><span class="label">Residual Substrate S</span><span class="value" id="r-chemoS">0.00 g/L</span><span class="subtext">effluent substrate</span></div>' +
              '<div class="readout-card"><span class="label">Volumetric Productivity</span><span class="value" id="r-chemoprod">0.0 g/L·h</span><span class="subtext">D · X yield</span></div>' +
              '<div class="readout-card"><span class="label">Washout Limit Dcrit</span><span class="value" id="r-chemodcrit">0.00 h⁻¹</span><span class="subtext">washout boundary</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-bio-u3" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-bio-u3"></div>',
      init: function(card) {
        var sD = card.querySelector('#s-dil'), vD = card.querySelector('#v-dil');
        var sMu = card.querySelector('#s-mumax'), vMu = card.querySelector('#v-mumax');
        var sKs = card.querySelector('#s-monodks'), vKs = card.querySelector('#v-monodks');
        var sSin = card.querySelector('#s-sin'), vSin = card.querySelector('#v-sin');
        var rX = card.querySelector('#r-chemoX'), rS = card.querySelector('#r-chemoS');
        var rProd = card.querySelector('#r-chemoprod'), rDcrit = card.querySelector('#r-chemodcrit');
        var svg = card.querySelector('#plot-bio-u3'), diag = card.querySelector('#diag-bio-u3');

        function update() {
          var D = parseFloat(sD.value); vD.textContent = f(D, 2);
          var mumax = parseFloat(sMu.value); vMu.textContent = f(mumax, 2);
          var Ks = parseFloat(sKs.value); vKs.textContent = f(Ks, 2);
          var Sin = parseFloat(sSin.value); vSin.textContent = f(Sin, 1);

          var Dcrit = (mumax * Sin) / (Ks + Sin);
          var isWashout = D >= Dcrit;

          var S = isWashout ? Sin : (Ks * D) / (mumax - D);
          var Yxs = 0.50;
          var X = isWashout ? 0.0 : Yxs * (Sin - S);
          var prod = D * X;

          rX.textContent = f(X, 2) + ' g/L';
          rS.textContent = f(S, 3) + ' g/L';
          rProd.textContent = f(prod, 2) + ' g/L·h';
          rDcrit.textContent = f(Dcrit, 3) + ' h⁻¹';
          rX.style.color = isWashout ? '#dc2626' : '#15803d';

          // SVG Chemostat biomass & productivity vs Dilution rate
          var dPathX = 'M 60 ';
          var dPathProd = 'M 60 170 ';
          for (var d_i = 0.02; d_i <= 0.80; d_i += 0.02) {
            var x_val = d_i >= Dcrit ? 0 : Yxs * (Sin - (Ks * d_i) / (mumax - d_i));
            x_val = Math.max(0, x_val);
            var prod_val = d_i * x_val;
            var x_px = 60 + ((d_i - 0.02) / 0.78) * 480;
            var y_x = 170 - (x_val / (Sin * Yxs)) * 140;
            var y_p = 170 - (prod_val / (mumax * Sin * Yxs * 0.45)) * 140;
            if (d_i === 0.02) dPathX += y_x.toFixed(1) + ' ';
            else dPathX += 'L ' + x_px.toFixed(1) + ' ' + y_x.toFixed(1) + ' ';
            dPathProd += 'L ' + x_px.toFixed(1) + ' ' + y_p.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="' + (60 + ((Dcrit - 0.02) / 0.78) * 480).toFixed(1) + '" y1="30" x2="' + (60 + ((Dcrit - 0.02) / 0.78) * 480).toFixed(1) + '" y2="170" stroke="#ef4444" stroke-dasharray="4"/>' +
                          '<text x="' + (60 + ((Dcrit - 0.02) / 0.78) * 480).toFixed(1) + '" y="25" text-anchor="middle" font-size="10" font-weight="700" fill="#dc2626">Dcrit = ' + f(Dcrit,2) + '</text>' +
                          '<path d="' + dPathX + '" fill="none" stroke="#10b981" stroke-width="3"/>' +
                          '<path d="' + dPathProd + '" fill="none" stroke="#0284c7" stroke-width="2"/>' +
                          '<circle cx="' + (60 + ((D - 0.02) / 0.78) * 480).toFixed(1) + '" cy="' + (170 - (X / (Sin * Yxs)) * 140).toFixed(1) + '" r="6" fill="#047857"/>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Dilution Rate D (h⁻¹)</text>' +
                          '<text x="50" y="40" font-size="11" fill="#64748b">Biomass X (Green) & Prod D·X (Blue)</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Chemostat Dynamics: D = ' + f(D, 2) + ' h⁻¹ (' + (isWashout ? 'WASHOUT' : 'Stable Growth') + ')</text>';
          diag.textContent = 'Continuous chemostat operation: Dilution rate D = ' + f(D, 2) + ' h⁻¹ against critical washout Dcrit = ' + f(Dcrit, 3) + ' h⁻¹. ' + (isWashout ? 'CRITICAL: Dilution rate exceeds maximum cellular growth rate; culture washes out of fermenter.' : 'Steady state achieved: Effluent cell density is ' + f(X, 2) + ' g/L yielding biomass productivity of ' + f(prod, 2) + ' g/L·h.');
        }
        [sD, sMu, sKs, sSin].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Bioreactor Oxygen Mass Transfer Coefficient (kLa)</h3><p class="lead">Simulate agitation power P/V, gas aeration rate vg, and evaluate volumetric transfer kLa.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Impeller Power P/V <span><output id="v-impw">3.5</output> kW/m³</span></label><input type="range" id="s-impw" min="0.5" max="10.0" step="0.5" value="3.5"></div>' +
              '<div class="control-group"><label>Superficial Gas vg <span><output id="v-gasvg">0.03</output> m/s</span></label><input type="range" id="s-gasvg" min="0.005" max="0.100" step="0.005" value="0.030"></div>' +
              '<div class="control-group"><label>Biomass Respiration QO2 <span><output id="v-qox">8.0</output> mmol/g·h</span></label><input type="range" id="s-qox" min="2.0" max="25.0" step="1.0" value="8.0"></div>' +
              '<div class="control-group"><label>Cell Concentration X <span><output id="v-cellx">20.0</output> g/L</span></label><input type="range" id="s-cellx" min="5.0" max="60.0" step="5.0" value="20.0"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Volumetric kLa</span><span class="value" id="r-kla">0 h⁻¹</span><span class="subtext">mass transfer rate</span></div>' +
              '<div class="readout-card"><span class="label">Max OTR</span><span class="value" id="r-otrmax">0 mmol/L·h</span><span class="subtext">oxygen transfer rate</span></div>' +
              '<div class="readout-card"><span class="label">OUR Demand</span><span class="value" id="r-ourdem">0 mmol/L·h</span><span class="subtext">cellular uptake rate</span></div>' +
              '<div class="readout-card"><span class="label">Dissolved Oxygen DO</span><span class="value" id="r-dolevel">0%</span><span class="subtext">steady state saturation</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-bio-u4" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-bio-u4"></div>',
      init: function(card) {
        var sP = card.querySelector('#s-impw'), vP = card.querySelector('#v-impw');
        var sV = card.querySelector('#s-gasvg'), vV = card.querySelector('#v-gasvg');
        var sQ = card.querySelector('#s-qox'), vQ = card.querySelector('#v-qox');
        var sX = card.querySelector('#s-cellx'), vX = card.querySelector('#v-cellx');
        var rK = card.querySelector('#r-kla'), rOTR = card.querySelector('#r-otrmax');
        var rOUR = card.querySelector('#r-ourdem'), rDO = card.querySelector('#r-dolevel');
        var svg = card.querySelector('#plot-bio-u4'), diag = card.querySelector('#diag-bio-u4');

        function update() {
          var PV = parseFloat(sP.value) * 1e3; vP.textContent = f(PV / 1e3, 1);
          var vg = parseFloat(sV.value); vV.textContent = f(vg, 3);
          var Qo2 = parseFloat(sQ.value); vQ.textContent = f(Qo2, 1);
          var X = parseFloat(sX.value); vX.textContent = f(X, 1);

          // Van't Riet correlation: kLa = 0.026 * (P/V)^0.4 * (vg)^0.5 [s-1]
          var kla_s = 0.026 * Math.pow(PV, 0.4) * Math.pow(vg, 0.5);
          var kla_h = kla_s * 3600;

          var C_star = 0.22; // mmol/L (dissolved oxygen saturation in water at 30°C)
          var OTR_max = kla_h * C_star;
          var OUR = Qo2 * X; // mmol/L·h
          var DO_frac = Math.max(0, 1.0 - (OUR / OTR_max));

          rK.textContent = f(kla_h, 0) + ' h⁻¹';
          rOTR.textContent = f(OTR_max, 1) + ' mmol/L·h';
          rOUR.textContent = f(OUR, 1) + ' mmol/L·h';
          rDO.textContent = f(DO_frac * 100, 1) + ' %';
          rDO.style.color = DO_frac < 0.15 ? '#dc2626' : (DO_frac < 0.3 ? '#d97706' : '#15803d');

          // SVG Dissolved oxygen concentration bar & dynamic gassing out curve
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="220" y="40" width="160" height="120" fill="#f1f5f9" stroke="#334155" stroke-width="2" rx="10"/>' +
                          '<rect x="222" y="' + (158 - DO_frac * 90).toFixed(1) + '" width="156" height="' + (DO_frac * 90).toFixed(1) + '" fill="#93c5fd" opacity="0.8" rx="4"/>' +
                          '<circle cx="280" cy="110" r="4" fill="#38bdf8"/>' +
                          '<circle cx="320" cy="90" r="5" fill="#38bdf8"/>' +
                          '<circle cx="295" cy="70" r="6" fill="#38bdf8"/>' +
                          '<text x="200" y="105" text-anchor="end" font-size="12" font-weight="700" fill="#0284c7">DO: ' + f(DO_frac*100, 1) + '%</text>' +
                          '<text x="400" y="80" font-size="11" font-weight="700" fill="#15803d">OTR: ' + f(OTR_max, 1) + ' mmol/L·h</text>' +
                          '<text x="400" y="110" font-size="11" font-weight="700" fill="' + (OUR > OTR_max ? '#dc2626' : '#475569') + '">OUR: ' + f(OUR, 1) + ' mmol/L·h</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Bioreactor Aeration: kLa = ' + f(kla_h, 0) + ' h⁻¹ (' + (DO_frac < 0.15 ? 'OXYGEN LIMITED' : 'Adequate DO') + ')</text>';
          diag.textContent = 'Oxygen transfer rate: At P/V = ' + f(PV / 1e3, 1) + ' kW/m³ and vg = ' + f(vg, 3) + ' m/s, volumetric mass transfer coefficient kLa is ' + f(kla_h, 0) + ' h⁻¹ (max OTR = ' + f(OTR_max, 1) + ' mmol/L·h). Cellular uptake OUR of ' + f(OUR, 1) + ' mmol/L·h results in dissolved oxygen level of ' + f(DO_frac * 100, 1) + '% saturation.';
        }
        [sP, sV, sQ, sX].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Continuous Media Thermal Sterilization (Del Factor)</h3><p class="lead">Simulate holding temperature T, dwell time, and logarithmic bacterial spore reduction ∇.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Sterilization Temp T <span><output id="v-stert">135</output> °C</span></label><input type="range" id="s-stert" min="115" max="145" step="1" value="135"></div>' +
              '<div class="control-group"><label>Holding Time t <span><output id="v-stertime">60</output> s</span></label><input type="range" id="s-stertime" min="10" max="300" step="10" value="60"></div>' +
              '<div class="control-group"><label>Spore Activation Ea <span><output id="v-sporea">280</output> kJ/mol</span></label><input type="range" id="s-sporea" min="200" max="350" step="10" value="280"></div>' +
              '<div class="control-group"><label>Media Volume V <span><output id="v-medvol">50000</output> L</span></label><input type="range" id="s-medvol" min="5000" max="100000" step="5000" value="50000"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Del Factor ∇</span><span class="value" id="r-delfac">0.0</span><span class="subtext">ln(N0 / Nt)</span></div>' +
              '<div class="readout-card"><span class="label">Contamination Risk</span><span class="value" id="r-contrisk">1 in 1000</span><span class="subtext">probability 1 - Nt</span></div>' +
              '<div class="readout-card"><span class="label">Nutrient Retention</span><span class="value" id="r-nutret">94.5%</span><span class="subtext">vitamin/protein preservation</span></div>' +
              '<div class="readout-card"><span class="label">Sterility Assurance</span><span class="value" id="r-sterstat">SAL Valid</span><span class="subtext">pharmaceutical standard</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-bio-u5" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-bio-u5"></div>',
      init: function(card) {
        var sT = card.querySelector('#s-stert'), vT = card.querySelector('#v-stert');
        var stime = card.querySelector('#s-stertime'), vtime = card.querySelector('#v-stertime');
        var sEa = card.querySelector('#s-sporea'), vEa = card.querySelector('#v-sporea');
        var sVol = card.querySelector('#s-medvol'), vVol = card.querySelector('#v-medvol');
        var rDel = card.querySelector('#r-delfac'), rRisk = card.querySelector('#r-contrisk');
        var rNut = card.querySelector('#r-nutret'), rSal = card.querySelector('#r-sterstat');
        var svg = card.querySelector('#plot-bio-u5'), diag = card.querySelector('#diag-bio-u5');

        function update() {
          var T_c = parseFloat(sT.value); vT.textContent = f(T_c, 0);
          var T_k = T_c + 273.15;
          var t = parseFloat(stime.value); vtime.textContent = f(t, 0);
          var Ea = parseFloat(sEa.value) * 1e3; vEa.textContent = f(Ea / 1e3, 0);
          var vol = parseFloat(sVol.value); vVol.textContent = f(vol, 0);

          var R = 8.314;
          var k_spore = 1.0e35 * Math.exp(-Ea / (R * T_k)); // s-1
          var del = k_spore * t;
          del = Math.min(65, Math.max(0.1, del));

          var N0 = vol * 1e5; // spores initially
          var Nt = N0 * Math.exp(-del);
          var riskStr = Nt < 1e-4 ? '< 1 in 10,000' : (Nt < 1e-2 ? '1 in 1,000 (Standard)' : 'HIGH RISK (' + f(Nt, 1) + ' spores)');

          // HTST preservation of heat-labile vitamins (Ea_nut ≈ 100 kJ/mol)
          var k_nut = 1.0e10 * Math.exp(-100000 / (R * T_k));
          var nutRet = Math.exp(-k_nut * t) * 100;
          nutRet = Math.max(50, Math.min(99.5, nutRet));

          rDel.textContent = f(del, 1);
          rRisk.textContent = riskStr;
          rNut.textContent = f(nutRet, 1) + ' %';
          var isSAL = del >= 35 && Nt < 1e-3;
          rSal.textContent = isSAL ? 'SAL 10⁻³ Achieved' : 'INSUFFICIENT STERILITY';
          rSal.style.color = isSAL ? '#15803d' : '#dc2626';

          // SVG Thermal death time curve
          var dPath = 'M 60 ' + (170 - (Math.log10(N0) / 12) * 140).toFixed(1) + ' ';
          for (var t_i = 0; t_i <= t; t_i += t / 25) {
            var n_i = N0 * Math.exp(-k_spore * t_i);
            var logN = Math.log10(Math.max(1e-4, n_i));
            var x_px = 60 + (t_i / t) * 480;
            var y_px = 170 - ((logN + 4) / 16) * 140;
            y_px = Math.min(170, Math.max(20, y_px));
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#dc2626" stroke-width="3"/>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Holding Dwell Time (s)</text>' +
                          '<text x="50" y="30" font-size="11" fill="#64748b">Log10 Spore Population</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Thermal Sterilization: Del ∇ = ' + f(del, 1) + ' (Nutrient Retention: ' + f(nutRet, 1) + '%)</text>';
          diag.textContent = 'Continuous HTST sterilization at ' + f(T_c, 0) + ' °C for ' + f(t, 0) + ' seconds achieves a Del factor ∇ = ' + f(del, 1) + '. Bacterial spore survival probability is ' + riskStr + ' across ' + f(vol, 0) + ' L of culture media while retaining ' + f(nutRet, 1) + '% of heat-sensitive vitamins.';
        }
        [sT, stime, sEa, sVol].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Tangential Flow Ultrafiltration & Gel Polarization</h3><p class="lead">Simulate transmembrane pressure TMP, permeate flux J, and membrane gel layer polarization.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Transmembrane TMP <span><output id="v-tmp">2.5</output> bar</span></label><input type="range" id="s-tmp" min="0.5" max="5.0" step="0.2" value="2.5"></div>' +
              '<div class="control-group"><label>Cross-Flow Velocity u <span><output id="v-cfu">1.5</output> m/s</span></label><input type="range" id="s-cfu" min="0.5" max="3.5" step="0.2" value="1.5"></div>' +
              '<div class="control-group"><label>Bulk Protein Cb <span><output id="v-cb">15.0</output> g/L</span></label><input type="range" id="s-cb" min="2.0" max="60.0" step="2.0" value="15.0"></div>' +
              '<div class="control-group"><label>Gel Concentration Cg <span><output id="v-cg">180</output> g/L</span></label><input type="range" id="s-cg" min="100" max="300" step="10" value="180"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Permeate Flux J</span><span class="value" id="r-flux">0 L/m²·h</span><span class="subtext">membrane throughput</span></div>' +
              '<div class="readout-card"><span class="label">Mass Transfer k</span><span class="value" id="r-tffk">0 L/m²·h</span><span class="subtext">boundary layer shear</span></div>' +
              '<div class="readout-card"><span class="label">Operating Regime</span><span class="value" id="r-tffreg">Pressure Limited</span><span class="subtext">TMP sensitivity</span></div>' +
              '<div class="readout-card"><span class="label">Wall Conc Cw</span><span class="value" id="r-tffcw">0 g/L</span><span class="subtext">surface polarization</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-bio-u6" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-bio-u6"></div>',
      init: function(card) {
        var sP = card.querySelector('#s-tmp'), vP = card.querySelector('#v-tmp');
        var sU = card.querySelector('#s-cfu'), vU = card.querySelector('#v-cfu');
        var sB = card.querySelector('#s-cb'), vB = card.querySelector('#v-cb');
        var sG = card.querySelector('#s-cg'), vG = card.querySelector('#v-cg');
        var rJ = card.querySelector('#r-flux'), rK = card.querySelector('#r-tffk');
        var rReg = card.querySelector('#r-tffreg'), rCw = card.querySelector('#r-tffcw');
        var svg = card.querySelector('#plot-bio-u6'), diag = card.querySelector('#diag-bio-u6');

        function update() {
          var TMP = parseFloat(sP.value); vP.textContent = f(TMP, 1);
          var u = parseFloat(sU.value); vU.textContent = f(u, 1);
          var Cb = parseFloat(sB.value); vB.textContent = f(Cb, 1);
          var Cg = parseFloat(sG.value); vG.textContent = f(Cg, 0);

          var Rm = 1.2e12; // membrane hydraulic resistance
          var k_mass = 22.0 * Math.pow(u, 0.65); // L/m2 h
          var J_lim = k_mass * Math.log(Cg / Cb);
          var J_pure = (TMP * 1e5 / 1.5e11) * 3600; // pressure-driven flux
          var J = (J_pure * J_lim) / (J_pure + J_lim);
          var Cw = Cb * Math.exp(J / k_mass);

          var isGel = J >= 0.85 * J_lim;
          rJ.textContent = f(J, 1) + ' L/m²·h';
          rK.textContent = f(k_mass, 1) + ' L/m²·h';
          rReg.textContent = isGel ? 'Gel Polarized (Flux Plateau)' : 'Pressure-Controlled';
          rReg.style.color = isGel ? '#ea580c' : '#15803d';
          rCw.textContent = f(Cw, 0) + ' g/L';

          // SVG Flux vs TMP curve
          var dPath = 'M 60 170 ';
          for (var p = 0.2; p <= 5.0; p += 0.2) {
            var j_p = (p * 1e5 / 1.5e11) * 3600;
            var j_i = (j_p * J_lim) / (j_p + J_lim);
            var x_px = 60 + ((p - 0.2) / 4.8) * 480;
            var y_px = 170 - (j_i / (J_lim * 1.25)) * 140;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          var cur_x = 60 + ((TMP - 0.2) / 4.8) * 480;
          var cur_y = 170 - (J / (J_lim * 1.25)) * 140;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="60" y1="' + (170 - (J_lim / (J_lim * 1.25)) * 140).toFixed(1) + '" x2="540" y2="' + (170 - (J_lim / (J_lim * 1.25)) * 140).toFixed(1) + '" stroke="#cbd5e1" stroke-dasharray="4"/>' +
                          '<text x="540" y="' + (165 - (J_lim / (J_lim * 1.25)) * 140).toFixed(1) + '" text-anchor="end" font-size="10" fill="#64748b">Limiting Gel Flux Jlim</text>' +
                          '<path d="' + dPath + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<circle cx="' + cur_x.toFixed(1) + '" cy="' + cur_y.toFixed(1) + '" r="6" fill="#ef4444" stroke="#fff" stroke-width="2"/>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Transmembrane Pressure TMP (bar)</text>' +
                          '<text x="50" y="30" font-size="11" fill="#64748b">Permeate Flux J (L/m²·h)</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">TFF Ultrafiltration: Flux J = ' + f(J, 1) + ' L/m²·h (' + (isGel ? 'Gel Layer Polarized' : 'Linear Flow') + ')</text>';
          diag.textContent = 'Tangential flow filtration: At TMP = ' + f(TMP, 1) + ' bar and cross-flow velocity u = ' + f(u, 1) + ' m/s, permeate flux is ' + f(J, 1) + ' L/m²·h. ' + (isGel ? 'Operating in the gel-polarized plateau region: further pressure increases do not boost throughput without increasing cross-flow shear.' : 'Operating below critical gel boundary in pressure-responsive regime.');
        }
        [sP, sU, sB, sG].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Preparative Bioseparation Chromatography Resolution</h3><p class="lead">Simulate column retention times tR, peak widths W, resolution Rs, and theoretical plates N.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Column Length L <span><output id="v-chroml">25</output> cm</span></label><input type="range" id="s-chroml" min="10" max="60" step="5" value="25"></div>' +
              '<div class="control-group"><label>Mobile Phase Flow u <span><output id="v-chromu">150</output> cm/h</span></label><input type="range" id="s-chromu" min="50" max="400" step="25" value="150"></div>' +
              '<div class="control-group"><label>Selectivity α <span><output id="v-chroma">1.25</output></span></label><input type="range" id="s-chroma" min="1.05" max="1.60" step="0.05" value="1.25"></div>' +
              '<div class="control-group"><label>Particle Diameter dp <span><output id="v-chromdp">35</output> μm</span></label><input type="range" id="s-chromdp" min="15" max="90" step="5" value="35"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Resolution Rs</span><span class="value" id="r-chromrs">0.00</span><span class="subtext">peak separation index</span></div>' +
              '<div class="readout-card"><span class="label">Theoretical Plates N</span><span class="value" id="r-chromn">0 Plates</span><span class="subtext">column efficiency</span></div>' +
              '<div class="readout-card"><span class="label">Purity Recovery</span><span class="value" id="r-chrompur">0.0%</span><span class="subtext">baseline separation</span></div>' +
              '<div class="readout-card"><span class="label">Run Duration</span><span class="value" id="r-chromtime">0 min</span><span class="subtext">elution cycle time</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-bio-u7" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-bio-u7"></div>',
      init: function(card) {
        var sL = card.querySelector('#s-chroml'), vL = card.querySelector('#v-chroml');
        var sU = card.querySelector('#s-chromu'), vU = card.querySelector('#v-chromu');
        var sA = card.querySelector('#s-chroma'), vA = card.querySelector('#v-chroma');
        var sD = card.querySelector('#s-chromdp'), vD = card.querySelector('#v-chromdp');
        var rRs = card.querySelector('#r-chromrs'), rN = card.querySelector('#r-chromn');
        var rPur = card.querySelector('#r-chrompur'), rTime = card.querySelector('#r-chromtime');
        var svg = card.querySelector('#plot-bio-u7'), diag = card.querySelector('#diag-bio-u7');

        function update() {
          var L = parseFloat(sL.value); vL.textContent = f(L, 0);
          var u = parseFloat(sU.value); vU.textContent = f(u, 0);
          var alpha = parseFloat(sA.value); vA.textContent = f(alpha, 2);
          var dp = parseFloat(sD.value); vD.textContent = f(dp, 0);

          var HETP = (0.003 * dp + 0.05 * (u / 100)) * 0.1; // cm
          var N = Math.round(L / HETP);
          var k1 = 2.0;
          var Rs = (Math.sqrt(N) / 4) * ((alpha - 1) / alpha) * (k1 / (1 + k1));

          var tR1 = (L / (u / 60)) * (1 + k1);
          var tR2 = tR1 * alpha;
          var purity = Rs >= 1.5 ? 99.8 : (Rs >= 1.0 ? 98.0 : (Rs >= 0.8 ? 92.0 : 80.0));

          rRs.textContent = f(Rs, 2);
          rRs.style.color = Rs >= 1.5 ? '#15803d' : (Rs >= 1.0 ? '#d97706' : '#dc2626');
          rN.textContent = N + ' Plates';
          rPur.textContent = f(purity, 1) + ' %';
          rTime.textContent = f(tR2 * 1.2, 1) + ' min';

          // SVG dual elution peaks
          var w1 = 4 * tR1 / Math.sqrt(N);
          var w2 = 4 * tR2 / Math.sqrt(N);
          var dPath = 'M 60 170 ';
          for (var t = 5; t <= tR2 * 1.35; t += (tR2 * 1.35 - 5) / 50) {
            var y1 = Math.exp(-0.5 * Math.pow((t - tR1) / (w1 / 4), 2));
            var y2 = Math.exp(-0.5 * Math.pow((t - tR2) / (w2 / 4), 2));
            var y_tot = (y1 + y2) * 120;
            var x_px = 60 + ((t - 5) / (tR2 * 1.35 - 5)) * 480;
            var y_px = 170 - Math.min(140, y_tot);
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#7c3aed" stroke-width="3"/>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Retention Time (min)</text>' +
                          '<text x="50" y="30" font-size="11" fill="#64748b">UV Absorbance (mAU)</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Chromatographic Resolution: Rs = ' + f(Rs, 2) + ' (N = ' + N + ' Plates)</text>';
          diag.textContent = 'Bioseparation resolution: Column L = ' + f(L, 0) + ' cm packed with ' + f(dp, 0) + ' μm resin generates ' + N + ' theoretical plates. Peak resolution Rs is ' + f(Rs, 2) + ' (' + (Rs >= 1.5 ? 'complete baseline separation with >99.8% recovery' : (Rs >= 1.0 ? 'acceptable operational separation' : 'severe peak co-elution and yield loss')) + ').';
        }
        [sL, sU, sA, sD].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Fed-Batch Fermentation Feeding Strategy & Product Titer</h3><p class="lead">Simulate exponential substrate feed rate F(t), biomass accumulation, and secondary metabolite titer.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Specific Growth Target μset <span><output id="v-muset">0.12</output> h⁻¹</span></label><input type="range" id="s-muset" min="0.04" max="0.30" step="0.02" value="0.12"></div>' +
              '<div class="control-group"><label>Feed Glucose Sfeed <span><output id="v-sfeed">400</output> g/L</span></label><input type="range" id="s-sfeed" min="200" max="600" step="50" value="400"></div>' +
              '<div class="control-group"><label>Feeding Duration <span><output id="v-feeddur">36</output> h</span></label><input type="range" id="s-feeddur" min="12" max="72" step="6" value="36"></div>' +
              '<div class="control-group"><label>Product Yield qp <span><output id="v-qp">0.05</output> g/g·h</span></label><input type="range" id="s-qp" min="0.01" max="0.12" step="0.01" value="0.05"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Final Biomass X</span><span class="value" id="r-fbX">0 g/L</span><span class="subtext">high cell density</span></div>' +
              '<div class="readout-card"><span class="label">Product Titer P</span><span class="value" id="r-fbP">0.0 g/L</span><span class="subtext">secondary metabolite</span></div>' +
              '<div class="readout-card"><span class="label">Broth Volume V</span><span class="value" id="r-fbV">0 L</span><span class="subtext">dilution accumulation</span></div>' +
              '<div class="readout-card"><span class="label">Specific Productivity</span><span class="value" id="r-fbprod">0.0 g/L·d</span><span class="subtext">space-time yield</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-bio-u8" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-bio-u8"></div>',
      init: function(card) {
        var sMu = card.querySelector('#s-muset'), vMu = card.querySelector('#v-muset');
        var sSf = card.querySelector('#s-sfeed'), vSf = card.querySelector('#v-sfeed');
        var sT = card.querySelector('#s-feeddur'), vT = card.querySelector('#v-feeddur');
        var sQ = card.querySelector('#s-qp'), vQ = card.querySelector('#v-qp');
        var rX = card.querySelector('#r-fbX'), rP = card.querySelector('#r-fbP');
        var rV = card.querySelector('#r-fbV'), rPr = card.querySelector('#r-fbprod');
        var svg = card.querySelector('#plot-bio-u8'), diag = card.querySelector('#diag-bio-u8');

        function update() {
          var muset = parseFloat(sMu.value); vMu.textContent = f(muset, 2);
          var sfeed = parseFloat(sSf.value); vSf.textContent = f(sfeed, 0);
          var tf = parseFloat(sT.value); vT.textContent = f(tf, 0);
          var qp = parseFloat(sQ.value); vQ.textContent = f(qp, 2);

          var V0 = 1000; // L
          var X0 = 10;   // g/L
          var Yxs = 0.50;

          var X_total = (X0 * V0) * Math.exp(muset * tf);
          var V_feed = (X_total / (Yxs * sfeed)) * 1.1;
          var V_final = V0 + V_feed;
          var X_conc = X_total / V_final;
          X_conc = Math.min(120, X_conc);

          var P_titer = qp * (X0 + X_conc) * 0.5 * tf * 0.65;
          var prodRate = (P_titer / (tf / 24));

          rX.textContent = f(X_conc, 1) + ' g/L';
          rP.textContent = f(P_titer, 1) + ' g/L';
          rV.textContent = f(V_final, 0) + ' L';
          rPr.textContent = f(prodRate, 1) + ' g/L·d';

          // SVG exponential biomass & product curves
          var dPathX = 'M 60 ' + (170 - (X0 / 120) * 140).toFixed(1) + ' ';
          var dPathP = 'M 60 170 ';
          for (var t_i = 0; t_i <= tf; t_i += tf / 30) {
            var x_i = X0 * Math.exp(muset * t_i);
            x_i = Math.min(120, x_i);
            var p_i = qp * x_i * 0.4 * t_i;
            var x_px = 60 + (t_i / tf) * 480;
            var y_x = 170 - (x_i / 120) * 140;
            var y_p = 170 - (p_i / 60) * 140;
            dPathX += 'L ' + x_px.toFixed(1) + ' ' + y_x.toFixed(1) + ' ';
            dPathP += 'L ' + x_px.toFixed(1) + ' ' + y_p.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPathX + '" fill="none" stroke="#10b981" stroke-width="3"/>' +
                          '<path d="' + dPathP + '" fill="none" stroke="#f59e0b" stroke-width="3"/>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Fed-Batch Time (h)</text>' +
                          '<text x="50" y="30" font-size="11" fill="#64748b">Biomass (Green) & Product (Amber)</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Fed-Batch Culture: Titer P = ' + f(P_titer, 1) + ' g/L (X = ' + f(X_conc, 1) + ' g/L)</text>';
          diag.textContent = 'Controlled fed-batch feeding: Regulating feed at target growth rate μset = ' + f(muset, 2) + ' h⁻¹ achieves high-density biomass accumulation of ' + f(X_conc, 1) + ' g/L and product titer of ' + f(P_titer, 1) + ' g/L over ' + f(tf, 0) + ' hours.';
        }
        [sMu, sSf, sT, sQ].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    }
  ];
""" + get_engine_footer(8)

# =========================================================================
# 4. Polymer Process Engineering
# =========================================================================
def build_poly_sims():
    return """/* Polymer Process Engineering Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Carothers Equation & Molecular Weight Distributions</h3><p class="lead">Simulate fractional monomer conversion p, stoichiometric ratio r, and number-average degree of polymerization Xn.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Conversion p <span><output id="v-carothp">98.5%</output></span></label><input type="range" id="s-carothp" min="80.0" max="99.9" step="0.1" value="98.5"></div>' +
              '<div class="control-group"><label>Stoichiometric Ratio r <span><output id="v-carothr">1.000</output></span></label><input type="range" id="s-carothr" min="0.950" max="1.000" step="0.005" value="1.000"></div>' +
              '<div class="control-group"><label>Repeat Unit Weight M0 <span><output id="v-m0">114</output> g/mol (Nylon 6)</span></label><input type="range" id="s-m0" min="50" max="250" step="10" value="114"></div>' +
              '<div class="control-group"><label>Monomer Functionality fav <span><output id="v-fav">2.00</output></span></label><input type="range" id="s-fav" min="2.00" max="2.40" step="0.05" value="2.00"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Degree of Polym. Xn</span><span class="value" id="r-carothxn">0</span><span class="subtext">number-average chain length</span></div>' +
              '<div class="readout-card"><span class="label">Molecular Weight Mn</span><span class="value" id="r-carothmn">0 kg/mol</span><span class="subtext">Xn · M0</span></div>' +
              '<div class="readout-card"><span class="label">Weight-Avg Mw</span><span class="value" id="r-carothmw">0 kg/mol</span><span class="subtext">Flory-Schulz distribution</span></div>' +
              '<div class="readout-card"><span class="label">Polydispersity (PDI)</span><span class="value" id="r-carothpdi">1.98</span><span class="subtext">Mw / Mn ratio</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-poly-u1" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-poly-u1"></div>',
      init: function(card) {
        var sP = card.querySelector('#s-carothp'), vP = card.querySelector('#v-carothp');
        var sR = card.querySelector('#s-carothr'), vR = card.querySelector('#v-carothr');
        var sM0 = card.querySelector('#s-m0'), vM0 = card.querySelector('#v-m0');
        var sFav = card.querySelector('#s-fav'), vFav = card.querySelector('#v-fav');
        var rXn = card.querySelector('#r-carothxn'), rMn = card.querySelector('#r-carothmn');
        var rMw = card.querySelector('#r-carothmw'), rPdi = card.querySelector('#r-carothpdi');
        var svg = card.querySelector('#plot-poly-u1'), diag = card.querySelector('#diag-poly-u1');

        function update() {
          var p = parseFloat(sP.value) / 100; vP.textContent = f(p * 100, 1) + '%';
          var r = parseFloat(sR.value); vR.textContent = f(r, 3);
          var M0 = parseFloat(sM0.value); vM0.textContent = f(M0, 0) + ' g/mol';
          var fav = parseFloat(sFav.value); vFav.textContent = f(fav, 2);

          // Carothers equation with stoichiometric imbalance r: Xn = (1 + r) / (1 + r - 2*r*p)
          var denom = 1 + r - 2 * r * p;
          var Xn = denom > 0.0005 ? (1 + r) / denom : 5000;
          Xn = Math.min(2500, Math.max(1, Xn));

          var PDI = 1 + p; // Flory-Schulz most probable distribution
          var Mn = (Xn * M0) / 1000; // kg/mol
          var Mw = Mn * PDI;

          rXn.textContent = f(Xn, 0);
          rMn.textContent = f(Mn, 1) + ' kg/mol';
          rMw.textContent = f(Mw, 1) + ' kg/mol';
          rPdi.textContent = f(PDI, 2);

          // SVG Molecular weight vs Conversion trajectory
          var dPath = 'M 60 170 ';
          for (var p_i = 0.80; p_i <= 0.998; p_i += 0.005) {
            var den_i = 1 + r - 2 * r * p_i;
            var xn_i = den_i > 0.0005 ? (1 + r) / den_i : 2000;
            var x_px = 60 + ((p_i - 0.80) / 0.198) * 480;
            var y_px = 170 - (Math.min(500, xn_i) / 500) * 140;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          var cur_x = 60 + ((p - 0.80) / 0.198) * 480;
          var cur_y = 170 - (Math.min(500, Xn) / 500) * 140;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<circle cx="' + cur_x.toFixed(1) + '" cy="' + cur_y.toFixed(1) + '" r="6" fill="#ef4444" stroke="#fff" stroke-width="2"/>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Fractional Conversion p (80% to 99.9%)</text>' +
                          '<text x="50" y="30" font-size="11" fill="#64748b">Degree of Polymerization Xn</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Step-Growth Carothers: Xn = ' + f(Xn, 0) + ' (Mn = ' + f(Mn, 1) + ' kg/mol)</text>';
          diag.textContent = 'Carothers step-growth synthesis: At conversion p = ' + f(p * 100, 1) + '% and stoichiometry r = ' + f(r, 3) + ', the number-average degree of polymerization is Xn = ' + f(Xn, 0) + ' (Mn = ' + f(Mn, 1) + ' kg/mol). Achieving commercial-grade polymer properties requires p > 98.5%.';
        }
        [sP, sR, sM0, sFav].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Free-Radical Chain Polymerization & Trommsdorff Gel Effect</h3><p class="lead">Simulate initiator decomposition, radical termination, and autoacceleration viscosity burst.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Initiator [I0] <span><output id="v-initc">10</output> mmol/L</span></label><input type="range" id="s-initc" min="2" max="50" step="2" value="10"></div>' +
              '<div class="control-group"><label>Temperature T <span><output id="v-frptemp">70</output> °C</span></label><input type="range" id="s-frptemp" min="50" max="95" step="5" value="70"></div>' +
              '<div class="control-group"><label>Monomer Conversion X <span><output id="v-frpx">45%</output></span></label><input type="range" id="s-frpx" min="5" max="95" step="5" value="45"></div>' +
              '<div class="control-group"><label>Solvent Dilution <span><output id="v-frpsolv">Bulk (No Solvent)</output></span></label><input type="range" id="s-frpsolv" min="1" max="2" step="1" value="1"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Polymerization Rp</span><span class="value" id="r-frprp">0.0 %/min</span><span class="subtext">rate of conversion</span></div>' +
              '<div class="readout-card"><span class="label">Termination kt / kt0</span><span class="value" id="r-frpkt">1.00</span><span class="subtext">diffusional slowdown</span></div>' +
              '<div class="readout-card"><span class="label">Kinetic Chain ν</span><span class="value" id="r-frpnu">0</span><span class="subtext">Rp / Ri radicals</span></div>' +
              '<div class="readout-card"><span class="label">Gel Effect State</span><span class="value" id="r-frpgel">Onset</span><span class="subtext">autoacceleration</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-poly-u2" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-poly-u2"></div>',
      init: function(card) {
        var sI = card.querySelector('#s-initc'), vI = card.querySelector('#v-initc');
        var sT = card.querySelector('#s-frptemp'), vT = card.querySelector('#v-frptemp');
        var sX = card.querySelector('#s-frpx'), vX = card.querySelector('#v-frpx');
        var sS = card.querySelector('#s-frpsolv'), vS = card.querySelector('#v-frpsolv');
        var rRp = card.querySelector('#r-frprp'), rKt = card.querySelector('#r-frpkt');
        var rNu = card.querySelector('#r-frpnu'), rGel = card.querySelector('#r-frpgel');
        var svg = card.querySelector('#plot-poly-u2'), diag = card.querySelector('#diag-poly-u2');

        function update() {
          var I0 = parseFloat(sI.value); vI.textContent = f(I0, 0);
          var T_c = parseFloat(sT.value); vT.textContent = f(T_c, 0);
          var X = parseFloat(sX.value) / 100; vX.textContent = f(X * 100, 0) + '%';
          var isBulk = parseInt(sS.value, 10) === 1;
          vS.textContent = isBulk ? 'Bulk (No Solvent)' : 'Solution Polymer (50%)';

          // Gel effect onset around X = 0.25 - 0.40 in bulk
          var gelStrength = isBulk ? 6.0 : 2.0;
          var kt_rel = 1.0 / (1.0 + Math.exp(gelStrength * (X - 0.35)));
          kt_rel = Math.max(0.01, kt_rel);

          var baseRp = 0.8 * Math.sqrt(I0 / 10) * Math.pow(1.05, T_c - 70);
          var Rp = (baseRp / Math.sqrt(kt_rel)) * (1 - X);
          var nu = 450 * Math.sqrt(1 / (I0 * kt_rel));

          rRp.textContent = f(Rp, 2) + ' %/min';
          rKt.textContent = f(kt_rel, 3);
          rNu.textContent = f(nu, 0);
          var gelState = X > 0.5 ? 'Active Autoacceleration (Thermal Peak)' : (X > 0.25 ? 'Gel Effect Onset' : 'Classical Steady State');
          rGel.textContent = gelState;
          rGel.style.color = X > 0.5 ? '#dc2626' : (X > 0.25 ? '#d97706' : '#15803d');

          // SVG Rate vs Conversion curve
          var dPath = 'M 60 ' + (170 - (baseRp / 8) * 140).toFixed(1) + ' ';
          for (var x_i = 0; x_i <= 0.95; x_i += 0.05) {
            var kt_i = 1.0 / (1.0 + Math.exp(gelStrength * (x_i - 0.35)));
            kt_i = Math.max(0.01, kt_i);
            var rp_i = (baseRp / Math.sqrt(kt_i)) * (1 - x_i);
            var x_px = 60 + (x_i / 0.95) * 480;
            var y_px = 170 - (Math.min(8.0, rp_i) / 8.0) * 140;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          var cur_x = 60 + (X / 0.95) * 480;
          var cur_y = 170 - (Math.min(8.0, Rp) / 8.0) * 140;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#ea580c" stroke-width="3"/>' +
                          '<circle cx="' + cur_x.toFixed(1) + '" cy="' + cur_y.toFixed(1) + '" r="6" fill="#c2410c" stroke="#fff" stroke-width="2"/>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Conversion X (0 to 95%)</text>' +
                          '<text x="50" y="30" font-size="11" fill="#64748b">Polymerization Rate Rp (%/min)</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Trommsdorff Gel Effect: Rp = ' + f(Rp, 2) + ' %/min (kt/kt0 = ' + f(kt_rel, 3) + ')</text>';
          diag.textContent = 'Free radical polymerization kinetics: At conversion X = ' + f(X * 100, 0) + '%, solution viscosity impedes macroradical diffusion, dropping termination rate constant kt to ' + f(kt_rel * 100, 1) + '% of its initial value. This triggers the Trommsdorff autoacceleration effect, boosting polymerization rate to ' + f(Rp, 2) + ' %/min.';
        }
        [sI, sT, sX, sS].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Non-Newtonian Polymer Melt Rheology (Power-Law & Cross)</h3><p class="lead">Simulate shear rate γ̇, flow behavior index n, zero-shear viscosity η0, and shear thinning.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Shear Rate γ̇ <span><output id="v-srate">100</output> s⁻¹</span></label><input type="range" id="s-srate" min="1" max="1000" step="10" value="100"></div>' +
              '<div class="control-group"><label>Power-Law Index n <span><output id="v-pln">0.35</output></span></label><input type="range" id="s-pln" min="0.20" max="0.80" step="0.05" value="0.35"></div>' +
              '<div class="control-group"><label>Zero-Shear η0 <span><output id="v-eta0">8500</output> Pa·s</span></label><input type="range" id="s-eta0" min="2000" max="25000" step="1000" value="8500"></div>' +
              '<div class="control-group"><label>Polymer Resin <span><output id="v-resintype">HDPE (MFI 2.0)</output></span></label><input type="range" id="s-resintype" min="1" max="2" step="1" value="1"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Apparent Viscosity η</span><span class="value" id="r-appeta">0 Pa·s</span><span class="subtext">at operating shear rate</span></div>' +
              '<div class="readout-card"><span class="label">Wall Shear Stress τw</span><span class="value" id="r-sheartau">0 kPa</span><span class="subtext">η · γ̇</span></div>' +
              '<div class="readout-card"><span class="label">Viscosity Drop</span><span class="value" id="r-etadrop">0×</span><span class="subtext">η0 / η thinning</span></div>' +
              '<div class="readout-card"><span class="label">Rheology Regime</span><span class="value" id="r-rheoreg">Pseudoplastic</span><span class="subtext">shear-thinning</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-poly-u3" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-poly-u3"></div>',
      init: function(card) {
        var sG = card.querySelector('#s-srate'), vG = card.querySelector('#v-srate');
        var sN = card.querySelector('#s-pln'), vN = card.querySelector('#v-pln');
        var sE = card.querySelector('#s-eta0'), vE = card.querySelector('#v-eta0');
        var sR = card.querySelector('#s-resintype'), vR = card.querySelector('#v-resintype');
        var rEta = card.querySelector('#r-appeta'), rTau = card.querySelector('#r-sheartau');
        var rDrop = card.querySelector('#r-etadrop'), rReg = card.querySelector('#r-rheoreg');
        var svg = card.querySelector('#plot-poly-u3'), diag = card.querySelector('#diag-poly-u3');

        function update() {
          var gamma = parseFloat(sG.value); vG.textContent = f(gamma, 0);
          var n = parseFloat(sN.value); vN.textContent = f(n, 2);
          var eta0 = parseFloat(sE.value); vE.textContent = f(eta0, 0);
          var isHDPE = parseInt(sR.value, 10) === 1;
          vR.textContent = isHDPE ? 'HDPE (MFI 2.0)' : 'PP Random Copolymer';

          // Cross model: eta = eta0 / (1 + (lambda * gamma)^(1 - n))
          var lambda = 0.08;
          var eta = eta0 / (1 + Math.pow(lambda * gamma, 1 - n));
          var tau = (eta * gamma) / 1000; // kPa
          var drop = eta0 / eta;

          rEta.textContent = f(eta, 0) + ' Pa·s';
          rTau.textContent = f(tau, 1) + ' kPa';
          rDrop.textContent = f(drop, 1) + '×';
          rReg.textContent = 'Pseudoplastic (n=' + f(n, 2) + ')';

          // SVG Log-Log Flow Curve
          var dPath = 'M 60 ';
          for (var g = 1; g <= 1000; g *= 1.5) {
            var eta_g = eta0 / (1 + Math.pow(lambda * g, 1 - n));
            var logG = Math.log10(g); // 0 to 3
            var logEta = Math.log10(Math.max(10, eta_g)); // 1 to 4.5
            var x_px = 60 + (logG / 3.0) * 480;
            var y_px = 170 - ((logEta - 1.0) / 3.5) * 140;
            y_px = Math.min(170, Math.max(20, y_px));
            if (g === 1) dPath += y_px.toFixed(1) + ' ';
            else dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          var cur_x = 60 + (Math.log10(gamma) / 3.0) * 480;
          var cur_y = 170 - ((Math.log10(eta) - 1.0) / 3.5) * 140;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#059669" stroke-width="3"/>' +
                          '<circle cx="' + cur_x.toFixed(1) + '" cy="' + cur_y.toFixed(1) + '" r="6" fill="#047857" stroke="#fff" stroke-width="2"/>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Log10 Shear Rate γ̇ (1 to 1000 s⁻¹)</text>' +
                          '<text x="50" y="30" font-size="11" fill="#64748b">Log10 Viscosity η (Pa·s)</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Polymer Melt Rheology: η = ' + f(eta, 0) + ' Pa·s (Thinning: ' + f(drop, 1) + '×)</text>';
          diag.textContent = 'Non-Newtonian melt rheology: At processing shear rate γ̇ = ' + f(gamma, 0) + ' s⁻¹, shear-thinning alignment drops melt viscosity from zero-shear plateau η0 = ' + f(eta0, 0) + ' Pa·s down to ' + f(eta, 0) + ' Pa·s (' + f(drop, 1) + '× reduction). Wall shear stress in extrusion channel is ' + f(tau, 1) + ' kPa.';
        }
        [sG, sN, sE, sR].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Single-Screw Extruder Operating Point Matching</h3><p class="lead">Simulate screw speed N, drag flow αN, pressure back-flow, and die resistance intersection.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Screw Speed N <span><output id="v-extN">60</output> RPM</span></label><input type="range" id="s-extN" min="15" max="150" step="5" value="60"></div>' +
              '<div class="control-group"><label>Screw Diameter D <span><output id="v-extD">65</output> mm</span></label><input type="range" id="s-extD" min="30" max="120" step="5" value="65"></div>' +
              '<div class="control-group"><label>Melt Viscosity μ <span><output id="v-extmu">800</output> Pa·s</span></label><input type="range" id="s-extmu" min="200" max="2500" step="100" value="800"></div>' +
              '<div class="control-group"><label>Die Resistance Kdie <span><output id="v-extdie">Medium Die</output></span></label><input type="range" id="s-extdie" min="1" max="3" step="1" value="2"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Operating Flow Q</span><span class="value" id="r-extQ">0 kg/h</span><span class="subtext">throughput rate</span></div>' +
              '<div class="readout-card"><span class="label">Die Head Pressure</span><span class="value" id="r-extP">0 bar</span><span class="subtext">operating ΔP</span></div>' +
              '<div class="readout-card"><span class="label">Drag Flow Qd</span><span class="value" id="r-extqd">0 kg/h</span><span class="subtext">maximum open discharge</span></div>' +
              '<div class="readout-card"><span class="label">Pressure Ratio</span><span class="value" id="r-extpr">0.00</span><span class="subtext">pressure / drag loss</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-poly-u4" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-poly-u4"></div>',
      init: function(card) {
        var sN = card.querySelector('#s-extN'), vN = card.querySelector('#v-extN');
        var sD = card.querySelector('#s-extD'), vD = card.querySelector('#v-extD');
        var sMu = card.querySelector('#s-extmu'), vMu = card.querySelector('#v-extmu');
        var sDie = card.querySelector('#s-extdie'), vDie = card.querySelector('#v-extdie');
        var rQ = card.querySelector('#r-extQ'), rP = card.querySelector('#r-extP');
        var rQd = card.querySelector('#r-extqd'), rPr = card.querySelector('#r-extpr');
        var svg = card.querySelector('#plot-poly-u4'), diag = card.querySelector('#diag-poly-u4');

        function update() {
          var N = parseFloat(sN.value); vN.textContent = f(N, 0);
          var D = parseFloat(sD.value) * 1e-3; vD.textContent = f(D * 1e3, 0);
          var mu = parseFloat(sMu.value); vMu.textContent = f(mu, 0);
          var dieType = parseInt(sDie.value, 10);
          vDie.textContent = dieType === 1 ? 'Open Pipe Die' : (dieType === 2 ? 'Medium Profile Die' : 'High-Resistance Sheet Die');

          var rho = 920; // kg/m3 melt density
          var alpha = 0.5 * Math.PI * D * 0.004 * 0.065 * Math.cos(17.7 * Math.PI / 180); // drag coefficient
          var Qd_m3s = alpha * (N / 60);
          var Qd_kgh = Qd_m3s * rho * 3600;

          var beta = 1.5e-9; // pressure back-flow factor
          var k_die = dieType === 1 ? 4.0e-9 : (dieType === 2 ? 1.5e-9 : 0.6e-9);

          // Q_screw = Qd - (beta/mu)*P = Q_die = (k_die/mu)*P
          var P_op = (Qd_m3s * mu) / (beta + k_die); // Pa
          var Q_op = (k_die / mu) * P_op * rho * 3600; // kg/h
          var P_bar = P_op / 1e5;

          rQ.textContent = f(Q_op, 1) + ' kg/h';
          rP.textContent = f(P_bar, 0) + ' bar';
          rQd.textContent = f(Qd_kgh, 1) + ' kg/h';
          rPr.textContent = f(1.0 - Q_op / Qd_kgh, 2);

          // SVG Screw characteristic vs Die characteristic intersection
          var dScrew = 'M 60 ' + (170 - (Qd_kgh / (Qd_kgh * 1.25)) * 140).toFixed(1) + ' L 540 170';
          var dDie = 'M 60 170 L 540 ' + (170 - ((k_die / mu) * (P_op * 2) * rho * 3600 / (Qd_kgh * 1.25)) * 140).toFixed(1);
          var cur_x = 60 + (P_bar / 200) * 480;
          var cur_y = 170 - (Q_op / (Qd_kgh * 1.25)) * 140;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="60" y1="30" x2="60" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dScrew + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<path d="' + dDie + '" fill="none" stroke="#dc2626" stroke-width="3"/>' +
                          '<circle cx="' + cur_x.toFixed(1) + '" cy="' + cur_y.toFixed(1) + '" r="6" fill="#10b981" stroke="#fff" stroke-width="2"/>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Die Head Pressure P (bar)</text>' +
                          '<text x="50" y="30" font-size="11" fill="#64748b">Flow Rate Q (kg/h)</text>' +
                          '<text x="130" y="55" font-size="11" font-weight="700" fill="#2563eb">Screw Curve</text>' +
                          '<text x="440" y="70" font-size="11" font-weight="700" fill="#dc2626">Die Curve</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Extruder Matching: Q = ' + f(Q_op, 1) + ' kg/h at P = ' + f(P_bar, 0) + ' bar</text>';
          diag.textContent = 'Single-screw operating intersection: Drag flow Qd = ' + f(Qd_kgh, 1) + ' kg/h at ' + f(N, 0) + ' RPM intersects die resistance curve at operating head pressure P = ' + f(P_bar, 0) + ' bar, yielding net extruder throughput of ' + f(Q_op, 1) + ' kg/h.';
        }
        [sN, sD, sMu, sDie].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Injection Molding Cavity Filling & Cooling Time</h3><p class="lead">Simulate part wall thickness h, mold temperature Tm, melt temperature Ti, and cycle time.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Wall Thickness h <span><output id="v-injth">2.5</output> mm</span></label><input type="range" id="s-injth" min="1.0" max="6.0" step="0.5" value="2.5"></div>' +
              '<div class="control-group"><label>Melt Temp Ti <span><output id="v-injti">230</output> °C</span></label><input type="range" id="s-injti" min="180" max="300" step="10" value="230"></div>' +
              '<div class="control-group"><label>Mold Temp Tm <span><output id="v-injtm">40</output> °C</span></label><input type="range" id="s-injtm" min="20" max="90" step="5" value="40"></div>' +
              '<div class="control-group"><label>Clamping Force <span><output id="v-injf">150</output> Tons</span></label><input type="range" id="s-injf" min="50" max="500" step="25" value="150"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Cooling Time tc</span><span class="value" id="r-injtc">0.0 s</span><span class="subtext">ejection solidification</span></div>' +
              '<div class="readout-card"><span class="label">Total Cycle Time</span><span class="value" id="r-injtot">0.0 s</span><span class="subtext">fill + pack + cool</span></div>' +
              '<div class="readout-card"><span class="label">Parts per Hour</span><span class="value" id="r-injpph">0 Parts</span><span class="subtext">machine throughput</span></div>' +
              '<div class="readout-card"><span class="label">Thermal Diffusivity</span><span class="value" id="r-injdiff">8.5e-8 m²/s</span><span class="subtext">conductive rate</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-poly-u5" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-poly-u5"></div>',
      init: function(card) {
        var sH = card.querySelector('#s-injth'), vH = card.querySelector('#v-injth');
        var sTi = card.querySelector('#s-injti'), vTi = card.querySelector('#v-injti');
        var sTm = card.querySelector('#s-injtm'), vTm = card.querySelector('#v-injtm');
        var sF = card.querySelector('#s-injf'), vF = card.querySelector('#v-injf');
        var rTc = card.querySelector('#r-injtc'), rTot = card.querySelector('#r-injtot');
        var rPph = card.querySelector('#r-injpph'), rDiff = card.querySelector('#r-injdiff');
        var svg = card.querySelector('#plot-poly-u5'), diag = card.querySelector('#diag-poly-u5');

        function update() {
          var h = parseFloat(sH.value) * 1e-3; vH.textContent = f(h * 1e3, 1);
          var Ti = parseFloat(sTi.value); vTi.textContent = f(Ti, 0);
          var Tm = parseFloat(sTm.value); vTm.textContent = f(Tm, 0);
          var F = parseFloat(sF.value); vF.textContent = f(F, 0);

          var alpha_th = 8.5e-8; // m2/s polymer thermal diffusivity
          var Te = 100; // ejection temperature °C

          // Ballman-Shusman 1D transient heat conduction: tc = (h^2 / (pi^2 * alpha)) * ln((4/pi) * (Ti - Tm) / (Te - Tm))
          var termLn = Math.log((4 / Math.PI) * ((Ti - Tm) / (Te - Tm)));
          termLn = Math.max(0.5, termLn);
          var tc = (h * h / (Math.PI * Math.PI * alpha_th)) * termLn;
          tc = Math.max(1.0, tc);

          var t_fill = 1.2 * Math.sqrt(h * 1e3);
          var t_pack = 0.4 * tc;
          var t_reset = 3.5;
          var t_cycle = t_fill + t_pack + tc + t_reset;
          var pph = Math.round(3600 / t_cycle);

          rTc.textContent = f(tc, 1) + ' s';
          rTot.textContent = f(t_cycle, 1) + ' s';
          rPph.textContent = pph + ' Parts/h';
          rDiff.textContent = '8.5 × 10⁻⁸ m²/s';

          // SVG Cycle time allocation stacked bar
          var barW = 440;
          var wFill = (t_fill / t_cycle) * barW;
          var wPack = (t_pack / t_cycle) * barW;
          var wCool = (tc / t_cycle) * barW;
          var wReset = (t_reset / t_cycle) * barW;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="65" width="' + wFill.toFixed(1) + '" height="35" fill="#f59e0b" rx="2"/>' +
                          '<rect x="' + (80 + wFill).toFixed(1) + '" y="65" width="' + wPack.toFixed(1) + '" height="35" fill="#3b82f6" rx="2"/>' +
                          '<rect x="' + (80 + wFill + wPack).toFixed(1) + '" y="65" width="' + wCool.toFixed(1) + '" height="35" fill="#10b981" rx="2"/>' +
                          '<rect x="' + (80 + wFill + wPack + wCool).toFixed(1) + '" y="65" width="' + wReset.toFixed(1) + '" height="35" fill="#94a3b8" rx="2"/>' +
                          '<text x="80" y="125" font-size="10" fill="#b45309">Fill: ' + f(t_fill,1) + 's</text>' +
                          '<text x="140" y="125" font-size="10" fill="#1e40af">Pack: ' + f(t_pack,1) + 's</text>' +
                          '<text x="260" y="125" font-size="10" fill="#047857">Cooling: ' + f(tc,1) + 's (' + f((tc/t_cycle)*100,0) + '%)</text>' +
                          '<text x="480" y="125" font-size="10" fill="#475569">Open/Eject</text>' +
                          '<text x="300" y="30" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Injection Molding Cycle Breakdown: ' + f(t_cycle, 1) + ' s (' + pph + ' parts/h)</text>';
          diag.textContent = 'Injection cycle thermal analysis: Cooling time scales quadratically with wall thickness h = ' + f(h * 1e3, 1) + ' mm, dominating total cycle time (' + f(tc, 1) + ' s cooling out of ' + f(t_cycle, 1) + ' s total cycle). Machine throughput is ' + pph + ' molded parts per hour.';
        }
        [sH, sTi, sTm, sF].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Viscoelastic Stress Relaxation & Deborah Number</h3><p class="lead">Simulate relaxation time λ, observation processing time tproc, and Deborah number De.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Relaxation Time λ <span><output id="v-visclam">1.5</output> s</span></label><input type="range" id="s-visclam" min="0.1" max="10.0" step="0.2" value="1.5"></div>' +
              '<div class="control-group"><label>Process Time tproc <span><output id="v-visctp">0.5</output> s</span></label><input type="range" id="s-visctp" min="0.05" max="5.0" step="0.05" value="0.5"></div>' +
              '<div class="control-group"><label>Initial Modulus G0 <span><output id="v-viscg0">250</output> kPa</span></label><input type="range" id="s-viscg0" min="50" max="800" step="50" value="250"></div>' +
              '<div class="control-group"><label>Deformation Mode <span><output id="v-viscmode">Die Swell</output></span></label><input type="range" id="s-viscmode" min="1" max="2" step="1" value="1"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Deborah Number De</span><span class="value" id="r-debno">0.00</span><span class="subtext">λ / tproc</span></div>' +
              '<div class="readout-card"><span class="label">Residual Modulus G(t)</span><span class="value" id="r-resmod">0 kPa</span><span class="subtext">Maxwell model decay</span></div>' +
              '<div class="readout-card"><span class="label">Viscoelastic Regime</span><span class="value" id="r-viscreg">Elastic Solid</span><span class="subtext">elastic vs viscous</span></div>' +
              '<div class="readout-card"><span class="label">Die Swell Ratio (B)</span><span class="value" id="r-dieswell">1.45</span><span class="subtext">extrudate expansion</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-poly-u6" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-poly-u6"></div>',
      init: function(card) {
        var sL = card.querySelector('#s-visclam'), vL = card.querySelector('#v-visclam');
        var sT = card.querySelector('#s-visctp'), vT = card.querySelector('#v-visctp');
        var sG0 = card.querySelector('#s-viscg0'), vG0 = card.querySelector('#v-viscg0');
        var sM = card.querySelector('#s-viscmode'), vM = card.querySelector('#v-viscmode');
        var rDe = card.querySelector('#r-debno'), rG = card.querySelector('#r-resmod');
        var rReg = card.querySelector('#r-viscreg'), rSw = card.querySelector('#r-dieswell');
        var svg = card.querySelector('#plot-poly-u6'), diag = card.querySelector('#diag-poly-u6');

        function update() {
          var lambda = parseFloat(sL.value); vL.textContent = f(lambda, 1);
          var tproc = parseFloat(sT.value); vT.textContent = f(tproc, 2);
          var G0 = parseFloat(sG0.value); vG0.textContent = f(G0, 0);
          var isDieSwell = parseInt(sM.value, 10) === 1;
          vM.textContent = isDieSwell ? 'Die Swell' : 'Stress Relaxation';

          var De = lambda / tproc;
          var G_t = G0 * Math.exp(-tproc / lambda);
          var B_swell = Math.pow(1 + 0.5 * Math.pow(Math.min(3.0, De), 2), 1 / 6) * 1.25;

          var regime = De > 1.0 ? 'Elastic Solid-Like (De > 1)' : (De < 0.1 ? 'Viscous Liquid (De << 1)' : 'Viscoelastic Transition');

          rDe.textContent = f(De, 2);
          rG.textContent = f(G_t, 1) + ' kPa';
          rReg.textContent = regime;
          rReg.style.color = De > 1.0 ? '#dc2626' : (De < 0.1 ? '#15803d' : '#d97706');
          rSw.textContent = f(B_swell, 2) + '×';

          // SVG Maxwell relaxation curve
          var dPath = 'M 60 ' + (170 - (G0 / G0) * 130).toFixed(1) + ' ';
          for (var t = 0; t <= lambda * 4; t += lambda * 4 / 30) {
            var g_val = G0 * Math.exp(-t / lambda);
            var x_px = 60 + (t / (lambda * 4)) * 480;
            var y_px = 170 - (g_val / G0) * 130;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          var cur_x = 60 + Math.min(1.0, (tproc / (lambda * 4))) * 480;
          var cur_y = 170 - (G_t / G0) * 130;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#7c3aed" stroke-width="3"/>' +
                          '<circle cx="' + cur_x.toFixed(1) + '" cy="' + cur_y.toFixed(1) + '" r="6" fill="#6d28d9" stroke="#fff" stroke-width="2"/>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Observation Time t (s)</text>' +
                          '<text x="50" y="30" font-size="11" fill="#64748b">Modulus G(t) [kPa]</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Maxwell Viscoelastic Relaxation: De = ' + f(De, 2) + ' (Die Swell = ' + f(B_swell, 2) + '×)</text>';
          diag.textContent = 'Deborah number analysis: Ratio of characteristic melt relaxation time λ = ' + f(lambda, 1) + ' s to process transit time tproc = ' + f(tproc, 2) + ' s yields De = ' + f(De, 2) + '. ' + (De > 1 ? 'Melt retains elastic memory, leading to extrudate die swell of ' + f(B_swell, 2) + '× and potential melt fracture instabilities.' : 'Elastic stresses relax completely during passage; fluid behaves purely viscously.');
        }
        [sL, sT, sG0, sM].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Capillary Rheometer Bagley & Rabinowitsch Corrections</h3><p class="lead">Simulate capillary length-to-diameter ratio L/D, entrance pressure loss ΔPent, and true wall shear stress.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Capillary L/D <span><output id="v-ldratio">16</output></span></label><input type="range" id="s-ldratio" min="4" max="32" step="2" value="16"></div>' +
              '<div class="control-group"><label>Total Pressure ΔPtot <span><output id="v-ptot">120</output> bar</span></label><input type="range" id="s-ptot" min="40" max="300" step="10" value="120"></div>' +
              '<div class="control-group"><label>Entrance Loss ΔPent <span><output id="v-pent">25</output> bar</span></label><input type="range" id="s-pent" min="5" max="60" step="5" value="25"></div>' +
              '<div class="control-group"><label>Power-Law Index n <span><output id="v-rabin">0.32</output></span></label><input type="range" id="s-rabin" min="0.20" max="0.80" step="0.04" value="0.32"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">True Wall Stress τw</span><span class="value" id="r-truetau">0 kPa</span><span class="subtext">Bagley corrected</span></div>' +
              '<div class="readout-card"><span class="label">Rabinowitsch Factor</span><span class="value" id="r-rabinfac">1.53</span><span class="subtext">(3n + 1) / 4n</span></div>' +
              '<div class="readout-card"><span class="label">True Shear Rate γ̇w</span><span class="value" id="r-truerate">0 s⁻¹</span><span class="subtext">non-parabolic profile</span></div>' +
              '<div class="readout-card"><span class="label">End Error Deficit</span><span class="value" id="r-enderr">20.8%</span><span class="subtext">ΔPent / ΔPtot</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-poly-u7" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-poly-u7"></div>',
      init: function(card) {
        var sLD = card.querySelector('#s-ldratio'), vLD = card.querySelector('#v-ldratio');
        var sP = card.querySelector('#s-ptot'), vP = card.querySelector('#v-ptot');
        var sPe = card.querySelector('#s-pent'), vPe = card.querySelector('#v-pent');
        var sN = card.querySelector('#s-rabin'), vN = card.querySelector('#v-rabin');
        var rTau = card.querySelector('#r-truetau'), rRab = card.querySelector('#r-rabinfac');
        var rRate = card.querySelector('#r-truerate'), rErr = card.querySelector('#r-enderr');
        var svg = card.querySelector('#plot-poly-u7'), diag = card.querySelector('#diag-poly-u7');

        function update() {
          var LD = parseFloat(sLD.value); vLD.textContent = f(LD, 0);
          var Ptot = parseFloat(sP.value); vP.textContent = f(Ptot, 0);
          var Pent = parseFloat(sPe.value); vPe.textContent = f(Pent, 0);
          var n = parseFloat(sN.value); vN.textContent = f(n, 2);

          // Bagley correction: tau_w = (Ptot - Pent) / (4 * LD) [bar] -> convert to kPa (*100)
          var tau_w = ((Ptot - Pent) / (4 * LD)) * 100;
          tau_w = Math.max(1, tau_w);

          // Rabinowitsch correction factor: (3n + 1) / (4n)
          var rab_fac = (3 * n + 1) / (4 * n);
          var appRate = 450; // s-1
          var trueRate = appRate * rab_fac;
          var endErr = (Pent / Ptot) * 100;

          rTau.textContent = f(tau_w, 1) + ' kPa';
          rRab.textContent = f(rab_fac, 2);
          rRate.textContent = f(trueRate, 0) + ' s⁻¹';
          rErr.textContent = f(endErr, 1) + ' %';

          // SVG Bagley Plot (ΔP vs L/D)
          var dPath = 'M 60 ' + (170 - (Pent / 250) * 140).toFixed(1) + ' L 540 ' + (170 - ((Pent + 4 * (tau_w / 100) * 32) / 250) * 140).toFixed(1);
          var cur_x = 60 + (LD / 32) * 480;
          var cur_y = 170 - (Ptot / 250) * 140;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<circle cx="' + cur_x.toFixed(1) + '" cy="' + cur_y.toFixed(1) + '" r="6" fill="#ef4444" stroke="#fff" stroke-width="2"/>' +
                          '<line x1="60" y1="' + (170 - (Pent / 250) * 140).toFixed(1) + '" x2="100" y2="' + (170 - (Pent / 250) * 140).toFixed(1) + '" stroke="#d97706" stroke-width="2"/>' +
                          '<text x="110" y="' + (174 - (Pent / 250) * 140).toFixed(1) + '" font-size="10" font-weight="700" fill="#d97706">ΔPent = ' + f(Pent,0) + ' bar</text>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Capillary Aspect Ratio L/D</text>' +
                          '<text x="50" y="30" font-size="11" fill="#64748b">Total Pressure ΔP (bar)</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Bagley Plot: True Wall Stress τw = ' + f(tau_w, 1) + ' kPa (End Loss: ' + f(endErr, 1) + '%)</text>';
          diag.textContent = 'Capillary rheometer data reduction: Entrance pressure loss ΔPent = ' + f(Pent, 0) + ' bar accounts for ' + f(endErr, 1) + '% of total pressure drop. Applying Bagley correction isolates true wall shear stress τw = ' + f(tau_w, 1) + ' kPa; Rabinowitsch factor ' + f(rab_fac, 2) + ' corrects for non-Newtonian velocity blunting.';
        }
        [sLD, sP, sPe, sN].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Polymer Mechanical Recycling Quality & Reprocessing Cycles</h3><p class="lead">Simulate thermo-mechanical extrusion cycles, Melt Flow Index (MFI) drift, and tensile degradation.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Recycle Cycles N <span><output id="v-reccyc">3</output> Cycles</span></label><input type="range" id="s-reccyc" min="1" max="8" step="1" value="3"></div>' +
              '<div class="control-group"><label>Virgin Polymer Blend <span><output id="v-virgbl">40%</output> Virgin</span></label><input type="range" id="s-virgbl" min="0" max="80" step="10" value="40"></div>' +
              '<div class="control-group"><label>Degradation Mode <span><output id="v-degmode">Chain Scission (MFI Up)</output></span></label><input type="range" id="s-degmode" min="1" max="2" step="1" value="1"></div>' +
              '<div class="control-group"><label>Stabilizer Package <span><output id="v-recspec">Antioxidant Added</output></span></label><input type="range" id="s-recspec" min="0" max="1" step="1" value="1"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Melt Flow Index (MFI)</span><span class="value" id="r-recmfi">3.4 g/10min</span><span class="subtext">ASTM D1238 fluidity</span></div>' +
              '<div class="readout-card"><span class="label">Tensile Strength Ret.</span><span class="value" id="r-rectens">88%</span><span class="subtext">of prime virgin resin</span></div>' +
              '<div class="readout-card"><span class="label">Elongation at Break</span><span class="value" id="r-recelong">65%</span><span class="subtext">ductility embrittlement</span></div>' +
              '<div class="readout-card"><span class="label">Application Grade</span><span class="value" id="r-recappl">Extrusion Pipe</span><span class="subtext">downcycling tier</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-poly-u8" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-poly-u8"></div>',
      init: function(card) {
        var sC = card.querySelector('#s-reccyc'), vC = card.querySelector('#v-reccyc');
        var sV = card.querySelector('#s-virgbl'), vV = card.querySelector('#v-virgbl');
        var sM = card.querySelector('#s-degmode'), vM = card.querySelector('#v-degmode');
        var sS = card.querySelector('#s-recspec'), vS = card.querySelector('#v-recspec');
        var rMfi = card.querySelector('#r-recmfi'), rTens = card.querySelector('#r-rectens');
        var rEl = card.querySelector('#r-recelong'), rApp = card.querySelector('#r-recappl');
        var svg = card.querySelector('#plot-poly-u8'), diag = card.querySelector('#diag-poly-u8');

        function update() {
          var N = parseInt(sC.value, 10); vC.textContent = N + ' Cycles';
          var virgin = parseFloat(sV.value) / 100; vV.textContent = f(virgin * 100, 0) + '% Virgin';
          var isScission = parseInt(sM.value, 10) === 1;
          vM.textContent = isScission ? 'Chain Scission (MFI Up)' : 'Cross-linking (MFI Down)';
          var hasAox = parseInt(sS.value, 10) === 1;
          vS.textContent = hasAox ? 'Antioxidant Stabilizer Added' : 'Unstabilized';

          var rateFactor = hasAox ? 0.08 : 0.22;
          var effectiveN = N * (1 - virgin * 0.7);

          var mfi0 = 2.0;
          var mfi = isScission ? mfi0 * Math.exp(rateFactor * effectiveN) : mfi0 * Math.exp(-rateFactor * effectiveN);
          var tensileRet = Math.max(40, 100 * Math.exp(-0.06 * effectiveN));
          var elongRet = Math.max(15, 100 * Math.exp(-0.16 * effectiveN));

          rMfi.textContent = f(mfi, 2) + ' g/10min';
          rTens.textContent = f(tensileRet, 0) + ' %';
          rEl.textContent = f(elongRet, 0) + ' %';
          var tier = tensileRet > 90 ? 'Bottle / Film Grade' : (tensileRet > 75 ? 'Extrusion Pipe / Automotive' : 'Pallets / Non-Critical Composite');
          rApp.textContent = tier;

          // SVG property retention curve vs cycles
          var dPathTens = 'M 60 40 ';
          var dPathElong = 'M 60 40 ';
          for (var c = 0; c <= 8; c++) {
            var eff_c = c * (1 - virgin * 0.7);
            var t_c = Math.max(40, 100 * Math.exp(-0.06 * eff_c));
            var e_c = Math.max(15, 100 * Math.exp(-0.16 * eff_c));
            var x_px = 60 + (c / 8.0) * 480;
            var yt_px = 170 - (t_c / 100) * 140;
            var ye_px = 170 - (e_c / 100) * 140;
            dPathTens += 'L ' + x_px.toFixed(1) + ' ' + yt_px.toFixed(1) + ' ';
            dPathElong += 'L ' + x_px.toFixed(1) + ' ' + ye_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPathTens + '" fill="none" stroke="#10b981" stroke-width="3"/>' +
                          '<path d="' + dPathElong + '" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="4"/>' +
                          '<circle cx="' + (60 + (N / 8.0) * 480).toFixed(1) + '" cy="' + (170 - (tensileRet / 100) * 140).toFixed(1) + '" r="6" fill="#059669"/>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Processing Cycles (0 to 8)</text>' +
                          '<text x="50" y="30" font-size="11" fill="#64748b">Property Retention (%)</text>' +
                          '<text x="130" y="55" font-size="10" font-weight="700" fill="#047857">Tensile Strength (Solid)</text>' +
                          '<text x="130" y="75" font-size="10" font-weight="700" fill="#dc2626">Elongation at Break (Dashed)</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Mechanical Recycling: Tensile Ret = ' + f(tensileRet, 0) + '% (MFI = ' + f(mfi, 2) + ')</text>';
          diag.textContent = 'Circular mechanical recycling evaluation: After ' + N + ' extrusion cycles blended with ' + f(virgin * 100, 0) + '% virgin resin, tensile strength retention is ' + f(tensileRet, 0) + '%, while elongation at break drops to ' + f(elongRet, 0) + '% due to thermal chain scission. Material is qualified for ' + tier + '.';
        }
        [sC, sV, sM, sS].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    }
  ];
""" + get_engine_footer(8)

# =========================================================================
# 5. Petroleum and Petrochemical Processes
# =========================================================================
def build_pet_sims():
    return """/* Petroleum and Petrochemical Processes Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Crude Oil True Boiling Point (TBP) Assay & Cut Sizing</h3><p class="lead">Simulate API gravity, Watson characterization factor KW, and refinery cut yields.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Crude API Gravity <span><output id="v-api">34.0</output> °API</span></label><input type="range" id="s-api" min="15.0" max="48.0" step="1.0" value="34.0"></div>' +
              '<div class="control-group"><label>Mean Boiling Point <span><output id="v-mbp">310</output> °C</span></label><input type="range" id="s-mbp" min="200" max="400" step="10" value="310"></div>' +
              '<div class="control-group"><label>Sulfur Content <span><output id="v-sulfur">1.2%</output> wt</span></label><input type="range" id="s-sulfur" min="0.1" max="4.0" step="0.1" value="1.2"></div>' +
              '<div class="control-group"><label>Crude Type <span><output id="v-crtype">Light Sweet / Medium</output></span></label><input type="range" id="s-crtype" min="1" max="2" step="1" value="1"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Watson Factor KW</span><span class="value" id="r-watson">11.9</span><span class="subtext">paraffinic character</span></div>' +
              '<div class="readout-card"><span class="label">Specific Gravity SG</span><span class="value" id="r-specg">0.855</span><span class="subtext">at 60°F / 60°F</span></div>' +
              '<div class="readout-card"><span class="label">Light Distillates</span><span class="value" id="r-ldist">32%</span><span class="subtext">LPG + Naphtha</span></div>' +
              '<div class="readout-card"><span class="label">Atm. Residue Yield</span><span class="value" id="r-residue">28%</span><span class="subtext">bottoms fraction</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pet-u1" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pet-u1"></div>',
      init: function(card) {
        var sA = card.querySelector('#s-api'), vA = card.querySelector('#v-api');
        var sM = card.querySelector('#s-mbp'), vM = card.querySelector('#v-mbp');
        var sS = card.querySelector('#s-sulfur'), vS = card.querySelector('#v-sulfur');
        var sT = card.querySelector('#s-crtype'), vT = card.querySelector('#v-crtype');
        var rW = card.querySelector('#r-watson'), rSG = card.querySelector('#r-specg');
        var rL = card.querySelector('#r-ldist'), rRes = card.querySelector('#r-residue');
        var svg = card.querySelector('#plot-pet-u1'), diag = card.querySelector('#diag-pet-u1');

        function update() {
          var api = parseFloat(sA.value); vA.textContent = f(api, 1);
          var mbp_c = parseFloat(sM.value); vM.textContent = f(mbp_c, 0);
          var sulfur = parseFloat(sS.value); vS.textContent = f(sulfur, 1) + '%';
          var isLight = parseInt(sT.value, 10) === 1;
          vT.textContent = isLight ? 'Light Sweet / Medium' : 'Heavy Sour Blend';

          var SG = 141.5 / (131.5 + api);
          var T_rankine = (mbp_c * 9 / 5 + 32) + 459.67;
          var Kw = Math.pow(T_rankine, 1 / 3) / SG;

          var naphtha = Math.min(45, Math.max(10, 0.9 * api - 2.0));
          var middleDist = 38.0;
          var gasoil = 20.0;
          var residue = Math.max(8, 100 - naphtha - middleDist);

          rW.textContent = f(Kw, 2);
          rSG.textContent = f(SG, 3);
          rL.textContent = f(naphtha, 1) + ' %';
          rRes.textContent = f(residue, 1) + ' %';

          // SVG TBP Distillation Curve
          var dPath = 'M 60 ' + (170 - (40 / 600) * 140).toFixed(1) + ' ';
          for (var vol = 5; vol <= 95; vol += 5) {
            var tbp = 40 + (vol / 95) * (mbp_c * 1.6 - 40);
            var x_px = 60 + (vol / 100) * 480;
            var y_px = 170 - (tbp / 600) * 140;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="60" y1="30" x2="60" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<line x1="' + (60 + (naphtha / 100) * 480).toFixed(1) + '" y1="30" x2="' + (60 + (naphtha / 100) * 480).toFixed(1) + '" y2="170" stroke="#10b981" stroke-dasharray="3"/>' +
                          '<text x="' + (60 + (naphtha / 100) * 480).toFixed(1) + '" y="45" font-size="10" font-weight="700" fill="#047857">Naphtha Cut (' + f(naphtha,0) + '%)</text>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Cumulative Volume Distilled (%)</text>' +
                          '<text x="50" y="30" font-size="11" fill="#64748b">TBP Temperature (°C)</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Crude TBP Assay: ' + f(api, 1) + ' °API (Watson KW = ' + f(Kw, 2) + ', SG = ' + f(SG, 3) + ')</text>';
          diag.textContent = 'Crude oil assay evaluation: API gravity of ' + f(api, 1) + ' °API corresponds to specific gravity SG = ' + f(SG, 3) + '. Watson characterization factor KW = ' + f(Kw, 2) + ' identifies ' + (Kw > 12.0 ? 'paraffinic crude with high catalytic reforming yields.' : (Kw > 11.5 ? 'mixed-base intermediate crude.' : 'naphthenic/aromatic heavy crude.')) + ' Naphtha yield is ' + f(naphtha, 1) + '% and atmospheric residue is ' + f(residue, 1) + '%.';
        }
        [sA, sM, sS, sT].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Atmospheric Crude Distillation (CDU) Side-Draw Mass Balance</h3><p class="lead">Simulate crude charge rate, side-stripper steam, and product cut distribution.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Crude Feed Rate <span><output id="v-crfeed">100</output> kbpd</span></label><input type="range" id="s-crfeed" min="20" max="250" step="10" value="100"></div>' +
              '<div class="control-group"><label>Flash Zone Temp <span><output id="v-fztemp">360</output> °C</span></label><input type="range" id="s-fztemp" min="330" max="385" step="5" value="360"></div>' +
              '<div class="control-group"><label>Overhead Reflux Ratio <span><output id="v-cduro">1.8</output></span></label><input type="range" id="s-cduro" min="1.0" max="3.5" step="0.1" value="1.8"></div>' +
              '<div class="control-group"><label>Stripper Steam Rate <span><output id="v-steamrt">15</output> lb/bbl</span></label><input type="range" id="s-steamrt" min="5" max="30" step="5" value="15"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Overhead Naphtha</span><span class="value" id="r-cdunaph">0 kbpd</span><span class="subtext">light ends + naphtha</span></div>' +
              '<div class="readout-card"><span class="label">Kerosene Jet Cut</span><span class="value" id="r-cdukero">0 kbpd</span><span class="subtext">150 - 240°C fraction</span></div>' +
              '<div class="readout-card"><span class="label">Diesel / Gasoil</span><span class="value" id="r-cdudiesel">0 kbpd</span><span class="subtext">240 - 350°C fraction</span></div>' +
              '<div class="readout-card"><span class="label">Atm. Residue (AR)</span><span class="value" id="r-cduar">0 kbpd</span><span class="subtext">>350°C bottoms</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pet-u2" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pet-u2"></div>',
      init: function(card) {
        var sF = card.querySelector('#s-crfeed'), vF = card.querySelector('#v-crfeed');
        var sT = card.querySelector('#s-fztemp'), vT = card.querySelector('#v-fztemp');
        var sR = card.querySelector('#s-cduro'), vR = card.querySelector('#v-cduro');
        var sS = card.querySelector('#s-steamrt'), vS = card.querySelector('#v-steamrt');
        var rN = card.querySelector('#r-cdunaph'), rK = card.querySelector('#r-cdukero');
        var rD = card.querySelector('#r-cdudiesel'), rAR = card.querySelector('#r-cduar');
        var svg = card.querySelector('#plot-pet-u2'), diag = card.querySelector('#diag-pet-u2');

        function update() {
          var F = parseFloat(sF.value); vF.textContent = f(F, 0);
          var T_fz = parseFloat(sT.value); vT.textContent = f(T_fz, 0);
          var R = parseFloat(sR.value); vR.textContent = f(R, 1);
          var steam = parseFloat(sS.value); vS.textContent = f(steam, 0);

          var vapFrac = Math.min(0.75, Math.max(0.45, 0.45 + (T_fz - 330) * 0.0055));
          var naph = F * 0.22;
          var kero = F * 0.14;
          var diesel = F * (vapFrac - 0.36);
          diesel = Math.max(F * 0.15, diesel);
          var ar = F - naph - kero - diesel;

          rN.textContent = f(naph, 1) + ' kbpd';
          rK.textContent = f(kero, 1) + ' kbpd';
          rD.textContent = f(diesel, 1) + ' kbpd';
          rAR.textContent = f(ar, 1) + ' kbpd';

          // SVG CDU Column Schematic
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="250" y="30" width="80" height="140" fill="#f1f5f9" stroke="#334155" stroke-width="2" rx="10"/>' +
                          '<line x1="250" y1="50" x2="330" y2="50" stroke="#94a3b8"/>' +
                          '<line x1="250" y1="80" x2="330" y2="80" stroke="#94a3b8"/>' +
                          '<line x1="250" y1="110" x2="330" y2="110" stroke="#94a3b8"/>' +
                          '<line x1="250" y1="135" x2="330" y2="135" stroke="#ef4444" stroke-width="2"/>' +
                          '<line x1="150" y1="135" x2="250" y2="135" stroke="#334155" stroke-width="3"/>' +
                          '<text x="140" y="139" text-anchor="end" font-size="11" font-weight="700" fill="#334155">Feed ' + f(F,0) + ' kbpd</text>' +
                          '<line x1="330" y1="45" x2="430" y2="45" stroke="#0284c7" stroke-width="2"/>' +
                          '<text x="440" y="49" font-size="11" font-weight="700" fill="#0284c7">Naphtha: ' + f(naph,1) + ' kbpd</text>' +
                          '<line x1="330" y1="75" x2="430" y2="75" stroke="#10b981" stroke-width="2"/>' +
                          '<text x="440" y="79" font-size="11" font-weight="700" fill="#047857">Jet/Kero: ' + f(kero,1) + ' kbpd</text>' +
                          '<line x1="330" y1="105" x2="430" y2="105" stroke="#f59e0b" stroke-width="2"/>' +
                          '<text x="440" y="109" font-size="11" font-weight="700" fill="#b45309">Diesel: ' + f(diesel,1) + ' kbpd</text>' +
                          '<line x1="290" y1="170" x2="290" y2="190" stroke="#475569" stroke-width="3"/>' +
                          '<text x="300" y="18" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Atmospheric Tower Cut Distribution: Flash Vapor ' + f(vapFrac*100, 1) + '%</text>';
          diag.textContent = 'Atmospheric crude tower operation: At flash zone temperature ' + f(T_fz, 0) + ' °C and feed charge rate ' + f(F, 0) + ' kbpd, vaporization fraction is ' + f(vapFrac * 100, 1) + '%. Column recovers ' + f(naph, 1) + ' kbpd naphtha, ' + f(kero, 1) + ' kbpd kerosene jet fuel, ' + f(diesel, 1) + ' kbpd diesel, and ' + f(ar, 1) + ' kbpd atmospheric residue.';
        }
        [sF, sT, sR, sS].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Fluid Catalytic Cracking (FCC) Catalyst Riser & Heat Balance</h3><p class="lead">Simulate catalyst-to-oil ratio C/O, riser exit temperature, and regenerator coke combustion.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Cat-to-Oil Ratio C/O <span><output id="v-fccco">6.5</output></span></label><input type="range" id="s-fccco" min="4.0" max="11.0" step="0.5" value="6.5"></div>' +
              '<div class="control-group"><label>Riser Temp T_riser <span><output id="v-fccriser">525</output> °C</span></label><input type="range" id="s-fccriser" min="490" max="555" step="5" value="525"></div>' +
              '<div class="control-group"><label>VGO Feed Rate <span><output id="v-fccfeed">40</output> kbpd</span></label><input type="range" id="s-fccfeed" min="15" max="80" step="5" value="40"></div>' +
              '<div class="control-group"><label>Regen Air Rate <span><output id="v-fccair">120</output> kNm³/h</span></label><input type="range" id="s-fccair" min="60" max="220" step="10" value="120"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Conversion</span><span class="value" id="r-fccconv">74.5%</span><span class="subtext">gasoline + LPG + lighter</span></div>' +
              '<div class="readout-card"><span class="label">Gasoline Yield</span><span class="value" id="r-fccgas">48.2%</span><span class="subtext">high-octane motor spirit</span></div>' +
              '<div class="readout-card"><span class="label">Coke on Spent Cat</span><span class="value" id="r-fcccoke">0.85%</span><span class="subtext">wt% carbon on zeolite</span></div>' +
              '<div class="readout-card"><span class="label">Regen Bed Temp</span><span class="value" id="r-fccregt">710 °C</span><span class="subtext">combustion heat balance</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pet-u3" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pet-u3"></div>',
      init: function(card) {
        var sC = card.querySelector('#s-fccco'), vC = card.querySelector('#v-fccco');
        var sT = card.querySelector('#s-fccriser'), vT = card.querySelector('#v-fccriser');
        var sF = card.querySelector('#s-fccfeed'), vF = card.querySelector('#v-fccfeed');
        var sA = card.querySelector('#s-fccair'), vA = card.querySelector('#v-fccair');
        var rConv = card.querySelector('#r-fccconv'), rGas = card.querySelector('#r-fccgas');
        var rCoke = card.querySelector('#r-fcccoke'), rRegT = card.querySelector('#r-fccregt');
        var svg = card.querySelector('#plot-pet-u3'), diag = card.querySelector('#diag-pet-u3');

        function update() {
          var CO = parseFloat(sC.value); vC.textContent = f(CO, 1);
          var Triser = parseFloat(sT.value); vT.textContent = f(Triser, 0);
          var F = parseFloat(sF.value); vF.textContent = f(F, 0);
          var air = parseFloat(sA.value); vA.textContent = f(air, 0);

          var conv = 50 + 2.8 * CO + 0.12 * (Triser - 500);
          conv = Math.min(85, Math.max(55, conv));
          var gasYield = 0.65 * conv - 0.002 * Math.pow(conv, 2);
          var cokeYield = 0.055 * conv;
          var cokeOnCat = (cokeYield / CO);
          var Tregen = 680 + (cokeYield - 4.0) * 12;

          rConv.textContent = f(conv, 1) + ' %';
          rGas.textContent = f(gasYield, 1) + ' %';
          rCoke.textContent = f(cokeOnCat, 2) + ' %';
          rRegT.textContent = f(Tregen, 0) + ' °C';

          // SVG FCC Riser and Regenerator Schematic
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="220" y1="170" x2="220" y2="40" stroke="#2563eb" stroke-width="12"/>' +
                          '<text x="200" y="105" text-anchor="end" font-size="11" font-weight="700" fill="#1e40af">Riser Reactor</text>' +
                          '<rect x="340" y="45" width="100" height="110" fill="#fee2e2" stroke="#dc2626" stroke-width="2" rx="20"/>' +
                          '<text x="390" y="100" text-anchor="middle" font-size="11" font-weight="700" fill="#991b1b">Regenerator</text>' +
                          '<text x="390" y="120" text-anchor="middle" font-size="10" font-weight="700" fill="#dc2626">' + f(Tregen,0) + ' °C</text>' +
                          '<path d="M 220 50 L 340 70" fill="none" stroke="#64748b" stroke-width="3"/>' +
                          '<path d="M 390 155 L 390 170 L 220 170" fill="none" stroke="#ea580c" stroke-width="3"/>' +
                          '<text x="300" y="185" text-anchor="middle" font-size="10" font-weight="700" fill="#ea580c">Regenerated Cat (C/O = ' + f(CO,1) + ')</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">FCC Reactor-Regenerator Heat Balance (Conversion: ' + f(conv, 1) + '%)</text>';
          diag.textContent = 'FCC riser-regenerator heat balance: At catalyst-to-oil ratio C/O = ' + f(CO, 1) + ' and riser exit temperature ' + f(Triser, 0) + ' °C, conversion reaches ' + f(conv, 1) + '%, yielding ' + f(gasYield, 1) + '% high-octane gasoline. Regenerator bed stabilizes at ' + f(Tregen, 0) + ' °C via combustion of ' + f(cokeOnCat, 2) + ' wt% coke on spent catalyst.';
        }
        [sC, sT, sF, sA].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Hydrodesulfurization (HDS) Kinetic Reactor Sizing</h3><p class="lead">Simulate liquid hourly space velocity LHSV, hydrogen partial pressure, and sulfur conversion to <10 ppm.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Feed Sulfur S0 <span><output id="v-hdss0">8500</output> ppm</span></label><input type="range" id="s-hdss0" min="2000" max="25000" step="500" value="8500"></div>' +
              '<div class="control-group"><label>Space Velocity LHSV <span><output id="v-hdslhsv">1.8</output> h⁻¹</span></label><input type="range" id="s-hdslhsv" min="0.5" max="4.0" step="0.1" value="1.8"></div>' +
              '<div class="control-group"><label>H2 Partial Pressure <span><output id="v-hdsph2">45</output> bar</span></label><input type="range" id="s-hdsph2" min="20" max="90" step="5" value="45"></div>' +
              '<div class="control-group"><label>Reactor Temp T <span><output id="v-hdstemp">350</output> °C</span></label><input type="range" id="s-hdstemp" min="310" max="390" step="5" value="350"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Product Sulfur S</span><span class="value" id="r-hdsout">0 ppm</span><span class="subtext">effluent sulfur level</span></div>' +
              '<div class="readout-card"><span class="label">HDS Conversion</span><span class="value" id="r-hdsconv">99.8%</span><span class="subtext">desulfurization extent</span></div>' +
              '<div class="readout-card"><span class="label">H2 Consumption</span><span class="value" id="r-hdsh2cons">0 Nm³/m³</span><span class="subtext">chemical uptake</span></div>' +
              '<div class="readout-card"><span class="label">ULSD Compliance</span><span class="value" id="r-hdscomp">Euro V (<10 ppm)</span><span class="subtext">fuel regulation</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pet-u4" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pet-u4"></div>',
      init: function(card) {
        var sS = card.querySelector('#s-hdss0'), vS = card.querySelector('#v-hdss0');
        var sL = card.querySelector('#s-hdslhsv'), vL = card.querySelector('#v-hdslhsv');
        var sP = card.querySelector('#s-hdsph2'), vP = card.querySelector('#v-hdsph2');
        var sT = card.querySelector('#s-hdstemp'), vT = card.querySelector('#v-hdstemp');
        var rOut = card.querySelector('#r-hdsout'), rConv = card.querySelector('#r-hdsconv');
        var rH2 = card.querySelector('#r-hdsh2cons'), rComp = card.querySelector('#r-hdscomp');
        var svg = card.querySelector('#plot-pet-u4'), diag = card.querySelector('#diag-pet-u4');

        function update() {
          var S0 = parseFloat(sS.value); vS.textContent = f(S0, 0);
          var lhsv = parseFloat(sL.value); vL.textContent = f(lhsv, 1);
          var ph2 = parseFloat(sP.value); vP.textContent = f(ph2, 0);
          var T_c = parseFloat(sT.value); vT.textContent = f(T_c, 0);

          var k_hds = 0.085 * Math.pow(ph2 / 40, 0.6) * Math.pow(1.04, T_c - 340);
          // 1.5 order kinetics: 1/sqrt(S) - 1/sqrt(S0) = 0.5 * k * tau
          var tau = 1.0 / lhsv;
          var inv_sqrt_S = 1.0 / Math.sqrt(S0) + 0.5 * k_hds * tau * 2.2;
          var S_out = 1.0 / Math.pow(inv_sqrt_S, 2);
          S_out = Math.max(0.5, S_out);

          var conv = ((S0 - S_out) / S0) * 100;
          var h2Cons = 4.5 * ((S0 - S_out) / 1000) + 18.0; // Nm3/m3
          var isULSD = S_out <= 10.0;

          rOut.textContent = f(S_out, 1) + ' ppm';
          rConv.textContent = f(conv, 2) + ' %';
          rH2.textContent = f(h2Cons, 1) + ' Nm³/m³';
          rComp.textContent = isULSD ? 'Euro V (<10 ppm ULSD)' : 'Off-Spec (>10 ppm)';
          rComp.style.color = isULSD ? '#15803d' : '#dc2626';

          // SVG Sulfur concentration along catalyst bed
          var dPath = 'M 60 ' + (170 - (Math.log10(S0) / 4.5) * 140).toFixed(1) + ' ';
          for (var z = 0.05; z <= 1.0; z += 0.05) {
            var tau_z = z / lhsv;
            var inv_s = 1.0 / Math.sqrt(S0) + 0.5 * k_hds * tau_z * 2.2;
            var s_z = 1.0 / Math.pow(inv_s, 2);
            var x_px = 60 + z * 480;
            var y_px = 170 - (Math.log10(Math.max(1, s_z)) / 4.5) * 140;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="60" y1="' + (170 - (1 / 4.5) * 140).toFixed(1) + '" x2="540" y2="' + (170 - (1 / 4.5) * 140).toFixed(1) + '" stroke="#10b981" stroke-dasharray="4"/>' +
                          '<text x="540" y="' + (165 - (1 / 4.5) * 140).toFixed(1) + '" text-anchor="end" font-size="10" fill="#047857">10 ppm ULSD Limit</text>' +
                          '<path d="' + dPath + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Normalized Bed Depth z / L</text>' +
                          '<text x="50" y="30" font-size="11" fill="#64748b">Log10 Sulfur (ppm)</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">HDS Fixed-Bed Sizing: Exit Sulfur = ' + f(S_out, 1) + ' ppm (' + (isULSD ? 'ULSD Compliant' : 'Off-Spec') + ')</text>';
          diag.textContent = 'Hydrotreating reactor kinetics: At LHSV = ' + f(lhsv, 1) + ' h⁻¹ and PH2 = ' + f(ph2, 0) + ' bar at ' + f(T_c, 0) + ' °C, diesel sulfur is reduced from ' + f(S0, 0) + ' ppm down to ' + f(S_out, 1) + ' ppm (' + f(conv, 2) + '% desulfurization). Fuel achieves ' + (isULSD ? 'Ultra-Low Sulfur Diesel (Euro V/VI) standard.' : 'higher residence time or temperature required for clean fuels compliance.');
        }
        [sS, sL, sP, sT].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Steam Cracking of Naphtha & Light Olefins Production</h3><p class="lead">Simulate coil outlet temperature (COT), steam-to-oil ratio, cracking severity, and ethylene yield.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Coil Outlet Temp COT <span><output id="v-cot">840</output> °C</span></label><input type="range" id="s-cot" min="780" max="880" step="5" value="840"></div>' +
              '<div class="control-group"><label>Steam-to-Oil Ratio <span><output id="v-stor">0.50</output> kg/kg</span></label><input type="range" id="s-stor" min="0.30" max="0.80" step="0.05" value="0.50"></div>' +
              '<div class="control-group"><label>Residence Time tres <span><output id="v-scrtau">0.25</output> s</span></label><input type="range" id="s-scrtau" min="0.10" max="0.50" step="0.05" value="0.25"></div>' +
              '<div class="control-group"><label>Cracking Severity <span><output id="v-scsev">High Severity</output></span></label><input type="range" id="s-scsev" min="1" max="2" step="1" value="2"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Ethylene Yield</span><span class="value" id="r-sceth">0.0%</span><span class="subtext">primary olefin wt%</span></div>' +
              '<div class="readout-card"><span class="label">Propylene Yield</span><span class="value" id="r-scprop">0.0%</span><span class="subtext">co-product olefin wt%</span></div>' +
              '<div class="readout-card"><span class="label">Propylene/Ethylene</span><span class="value" id="r-scpe">0.00</span><span class="subtext">P/E selectivity ratio</span></div>' +
              '<div class="readout-card"><span class="label">Methane & Fuel Gas</span><span class="value" id="r-scgas">0.0%</span><span class="subtext">light off-gas yield</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pet-u5" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pet-u5"></div>',
      init: function(card) {
        var sC = card.querySelector('#s-cot'), vC = card.querySelector('#v-cot');
        var sS = card.querySelector('#s-stor'), vS = card.querySelector('#v-stor');
        var sT = card.querySelector('#s-scrtau'), vT = card.querySelector('#v-scrtau');
        var sSev = card.querySelector('#s-scsev'), vSev = card.querySelector('#v-scsev');
        var rEth = card.querySelector('#r-sceth'), rProp = card.querySelector('#r-scprop');
        var rPE = card.querySelector('#r-scpe'), rGas = card.querySelector('#r-scgas');
        var svg = card.querySelector('#plot-pet-u5'), diag = card.querySelector('#diag-pet-u5');

        function update() {
          var cot = parseFloat(sC.value); vC.textContent = f(cot, 0);
          var stor = parseFloat(sS.value); vS.textContent = f(stor, 2);
          var tres = parseFloat(sT.value); vT.textContent = f(tres, 2);
          var isHigh = parseInt(sSev.value, 10) === 2;
          vSev.textContent = isHigh ? 'High Severity (Max Ethylene)' : 'Moderate Severity (Max Propylene)';

          var severity = (cot - 750) * 0.4 + (0.5 - tres) * 20;
          var ethylene = 22.0 + 0.16 * (cot - 800) - (tres - 0.2) * 8;
          ethylene = Math.min(34.0, Math.max(18.0, ethylene));

          var propylene = 16.5 - 0.08 * (cot - 800) + (0.4 - stor) * 4;
          propylene = Math.min(18.0, Math.max(10.0, propylene));

          var peRatio = propylene / ethylene;
          var methane = 10.0 + 0.06 * (cot - 800);

          rEth.textContent = f(ethylene, 1) + ' %';
          rProp.textContent = f(propylene, 1) + ' %';
          rPE.textContent = f(peRatio, 2);
          rGas.textContent = f(methane, 1) + ' %';

          // SVG Olefin yield breakdown stacked bar
          var barW = 440;
          var wEth = (ethylene / 100) * barW;
          var wProp = (propylene / 100) * barW;
          var wGas = (methane / 100) * barW;
          var wOther = barW - wEth - wProp - wGas;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="65" width="' + wEth.toFixed(1) + '" height="35" fill="#2563eb" rx="2"/>' +
                          '<rect x="' + (80 + wEth).toFixed(1) + '" y="65" width="' + wProp.toFixed(1) + '" height="35" fill="#10b981" rx="2"/>' +
                          '<rect x="' + (80 + wEth + wProp).toFixed(1) + '" y="65" width="' + wGas.toFixed(1) + '" height="35" fill="#f59e0b" rx="2"/>' +
                          '<rect x="' + (80 + wEth + wProp + wGas).toFixed(1) + '" y="65" width="' + wOther.toFixed(1) + '" height="35" fill="#94a3b8" rx="2"/>' +
                          '<text x="80" y="125" font-size="11" fill="#1e40af">Ethylene: ' + f(ethylene,1) + '%</text>' +
                          '<text x="220" y="125" font-size="11" fill="#047857">Propylene: ' + f(propylene,1) + '%</text>' +
                          '<text x="360" y="125" font-size="11" fill="#b45309">Methane: ' + f(methane,1) + '%</text>' +
                          '<text x="480" y="125" font-size="11" fill="#475569">Pyrolysis Gas</text>' +
                          '<text x="300" y="30" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Steam Cracking Yields: P/E Ratio = ' + f(peRatio, 2) + ' (COT = ' + f(cot, 0) + ' °C)</text>';
          diag.textContent = 'Pyrolysis furnace thermal cracking: At coil outlet temperature COT = ' + f(cot, 0) + ' °C and steam ratio ' + f(stor, 2) + ' kg steam/kg naphtha with residence time tres = ' + f(tres, 2) + ' s, cracking produces ' + f(ethylene, 1) + ' wt% ethylene and ' + f(propylene, 1) + ' wt% propylene (P/E ratio = ' + f(peRatio, 2) + ').';
        }
        [sC, sS, sT, sSev].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>BTX Aromatics Liquid-Liquid Solvent Extraction</h3><p class="lead">Simulate solvent-to-feed ratio S/F, sulfolane aromatics extraction, and benzene/toluene purity.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Solvent-to-Feed S/F <span><output id="v-sf">3.5</output></span></label><input type="range" id="s-sf" min="1.5" max="6.0" step="0.5" value="3.5"></div>' +
              '<div class="control-group"><label>Feed Aromatics <span><output id="v-btxfeed">65%</output> wt</span></label><input type="range" id="s-btxfeed" min="30" max="85" step="5" value="65"></div>' +
              '<div class="control-group"><label>Extraction Temp T <span><output id="v-extt">100</output> °C</span></label><input type="range" id="s-extt" min="70" max="130" step="5" value="100"></div>' +
              '<div class="control-group"><label>Solvent Solvent <span><output id="v-solvchem">Sulfolane</output></span></label><input type="range" id="s-solvchem" min="1" max="2" step="1" value="1"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Aromatics Recovery</span><span class="value" id="r-btxrec">99.2%</span><span class="subtext">benzene + toluene yield</span></div>' +
              '<div class="readout-card"><span class="label">Extract Purity</span><span class="value" id="r-btxpur">99.8%</span><span class="subtext">aliphatic rejection</span></div>' +
              '<div class="readout-card"><span class="label">Raffinate Non-Arom</span><span class="value" id="r-btxraf">0.8%</span><span class="subtext">residual aromatics</span></div>' +
              '<div class="readout-card"><span class="label">Solvent Circulation</span><span class="value" id="r-btxcirc">0 t/h</span><span class="subtext">recovery reboiler duty</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pet-u6" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pet-u6"></div>',
      init: function(card) {
        var sSF = card.querySelector('#s-sf'), vSF = card.querySelector('#v-sf');
        var sF = card.querySelector('#s-btxfeed'), vF = card.querySelector('#v-btxfeed');
        var sT = card.querySelector('#s-extt'), vT = card.querySelector('#v-extt');
        var sS = card.querySelector('#s-solvchem'), vS = card.querySelector('#v-solvchem');
        var rRec = card.querySelector('#r-btxrec'), rPur = card.querySelector('#r-btxpur');
        var rRaf = card.querySelector('#r-btxraf'), rCirc = card.querySelector('#r-btxcirc');
        var svg = card.querySelector('#plot-pet-u6'), diag = card.querySelector('#diag-pet-u6');

        function update() {
          var sf = parseFloat(sSF.value); vSF.textContent = f(sf, 1);
          var aromFeed = parseFloat(sF.value); vF.textContent = f(aromFeed, 0) + '%';
          var T_c = parseFloat(sT.value); vT.textContent = f(T_c, 0);
          var isSulfolane = parseInt(sS.value, 10) === 1;
          vS.textContent = isSulfolane ? 'Sulfolane' : 'N-Methyl-2-pyrrolidone (NMP)';

          var recovery = Math.min(99.9, Math.max(85.0, 94.0 + (sf - 2.5) * 2.2));
          var purity = Math.min(99.9, Math.max(92.0, 97.5 + (sf - 2.5) * 0.8));
          var raffAr = Math.max(0.1, 100 - recovery);
          var circ = sf * 45; // tons/h approx

          rRec.textContent = f(recovery, 1) + ' %';
          rPur.textContent = f(purity, 2) + ' %';
          rRaf.textContent = f(raffAr, 1) + ' %';
          rCirc.textContent = f(circ, 0) + ' t/h';

          // SVG Ternary Liquid-Liquid Equilibrium Diagram
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<polygon points="300,35 180,165 420,165" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="11" font-weight="700" fill="#2563eb">Solvent (Sulfolane)</text>' +
                          '<text x="160" y="175" text-anchor="end" font-size="11" font-weight="700" fill="#dc2626">Aromatics (BTX)</text>' +
                          '<text x="440" y="175" text-anchor="start" font-size="11" font-weight="700" fill="#047857">Non-Aromatics</text>' +
                          '<line x1="220" y1="140" x2="380" y2="155" stroke="#ea580c" stroke-width="2"/>' +
                          '<line x1="240" y1="115" x2="360" y2="140" stroke="#ea580c" stroke-width="2"/>' +
                          '<line x1="260" y1="90" x2="340" y2="120" stroke="#ea580c" stroke-width="2"/>' +
                          '<circle cx="' + (250 + (sf / 6) * 40) + '" cy="' + (150 - (sf / 6) * 50) + '" r="5" fill="#ef4444"/>' +
                          '<text x="300" y="185" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">BTX Liquid-Liquid Extraction: Recovery = ' + f(recovery, 1) + '% (Purity: ' + f(purity, 2) + '%)</text>';
          diag.textContent = 'Aromatics solvent extraction: At solvent-to-feed ratio S/F = ' + f(sf, 1) + ' with ' + (isSulfolane ? 'sulfolane' : 'NMP') + ' at ' + f(T_c, 0) + ' °C, recovery of benzene-toluene-xylene reaches ' + f(recovery, 1) + '% with extract purity of ' + f(purity, 2) + '% after stripper re-distillation.';
        }
        [sSF, sF, sT, sS].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Refinery Hydrogen Network & Pinch Management</h3><p class="lead">Simulate reformer H2 production, hydrotreater demand, and PSA purification recovery.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Reformer H2 Supply <span><output id="v-refh2">45</output> kNm³/h</span></label><input type="range" id="s-refh2" min="20" max="90" step="5" value="45"></div>' +
              '<div class="control-group"><label>Hydrocracker Demand <span><output id="v-hcdem">35</output> kNm³/h</span></label><input type="range" id="s-hcdem" min="15" max="70" step="5" value="35"></div>' +
              '<div class="control-group"><label>Hydrotreater Demand <span><output id="v-htdem">22</output> kNm³/h</span></label><input type="range" id="s-htdem" min="10" max="45" step="2" value="22"></div>' +
              '<div class="control-group"><label>PSA Recovery Fraction <span><output id="v-psarec">88%</output></span></label><input type="range" id="s-psarec" min="75" max="95" step="1" value="88"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Total H2 Demand</span><span class="value" id="r-h2dem">0 kNm³/h</span><span class="subtext">consumers load</span></div>' +
              '<div class="readout-card"><span class="label">Hydrogen Deficit</span><span class="value" id="r-h2def">0 kNm³/h</span><span class="subtext">SMR makeup required</span></div>' +
              '<div class="readout-card"><span class="label">PSA Recycled H2</span><span class="value" id="r-psah2">0 kNm³/h</span><span class="subtext">purge gas purification</span></div>' +
              '<div class="readout-card"><span class="label">Network Balance</span><span class="value" id="r-h2bal">SMR Makeup</span><span class="subtext">header sufficiency</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pet-u7" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pet-u7"></div>',
      init: function(card) {
        var sR = card.querySelector('#s-refh2'), vR = card.querySelector('#v-refh2');
        var sHC = card.querySelector('#s-hcdem'), vHC = card.querySelector('#v-hcdem');
        var sHT = card.querySelector('#s-htdem'), vHT = card.querySelector('#v-htdem');
        var sP = card.querySelector('#s-psarec'), vP = card.querySelector('#v-psarec');
        var rDem = card.querySelector('#r-h2dem'), rDef = card.querySelector('#r-h2def');
        var rPsa = card.querySelector('#r-psah2'), rBal = card.querySelector('#r-h2bal');
        var svg = card.querySelector('#plot-pet-u7'), diag = card.querySelector('#diag-pet-u7');

        function update() {
          var refH2 = parseFloat(sR.value); vR.textContent = f(refH2, 0);
          var hcDem = parseFloat(sHC.value); vHC.textContent = f(hcDem, 0);
          var htDem = parseFloat(sHT.value); vHT.textContent = f(htDem, 0);
          var psaRec = parseFloat(sP.value) / 100; vP.textContent = f(psaRec * 100, 0) + '%';

          var totDem = hcDem + htDem;
          var psaH2 = (totDem * 0.18) * psaRec;
          var netSupply = refH2 + psaH2;
          var deficit = Math.max(0, totDem - netSupply);

          rDem.textContent = f(totDem, 0) + ' kNm³/h';
          rDef.textContent = f(deficit, 1) + ' kNm³/h';
          rPsa.textContent = f(psaH2, 1) + ' kNm³/h';
          var isSelf = deficit <= 0.1;
          rBal.textContent = isSelf ? 'Self-Sufficient' : 'SMR Makeup Required';
          rBal.style.color = isSelf ? '#15803d' : '#dc2626';

          // SVG Hydrogen Network Flow Sankey
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="50" width="100" height="35" fill="#dbeafe" stroke="#2563eb" stroke-width="2" rx="4"/>' +
                          '<text x="130" y="72" text-anchor="middle" font-size="11" font-weight="700" fill="#1e40af">Reformer: ' + f(refH2,0) + '</text>' +
                          '<rect x="80" y="115" width="100" height="35" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="4"/>' +
                          '<text x="130" y="137" text-anchor="middle" font-size="11" font-weight="700" fill="#92400e">SMR Make: ' + f(deficit,0) + '</text>' +
                          '<rect x="250" y="80" width="100" height="40" fill="#3b82f6" rx="4"/>' +
                          '<text x="300" y="105" text-anchor="middle" font-size="12" font-weight="800" fill="#fff">H2 Header</text>' +
                          '<rect x="420" y="50" width="110" height="35" fill="#dcfce7" stroke="#10b981" stroke-width="2" rx="4"/>' +
                          '<text x="475" y="72" text-anchor="middle" font-size="11" font-weight="700" fill="#166534">Hydrocracker: ' + f(hcDem,0) + '</text>' +
                          '<rect x="420" y="115" width="110" height="35" fill="#dcfce7" stroke="#10b981" stroke-width="2" rx="4"/>' +
                          '<text x="475" y="137" text-anchor="middle" font-size="11" font-weight="700" fill="#166534">Hydrotreaters: ' + f(htDem,0) + '</text>' +
                          '<line x1="180" y1="67" x2="250" y2="100" stroke="#2563eb" stroke-width="3"/>' +
                          '<line x1="180" y1="132" x2="250" y2="100" stroke="#d97706" stroke-width="3"/>' +
                          '<line x1="350" y1="100" x2="420" y2="67" stroke="#10b981" stroke-width="3"/>' +
                          '<line x1="350" y1="100" x2="420" y2="132" stroke="#10b981" stroke-width="3"/>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Refinery Hydrogen Header: Demand = ' + f(totDem,0) + ' kNm³/h (Deficit = ' + f(deficit,1) + ')</text>';
          diag.textContent = 'Refinery hydrogen integration: Total hydrogen consumption across hydrocracking (' + f(hcDem, 0) + ' kNm³/h) and desulfurization (' + f(htDem, 0) + ' kNm³/h) is ' + f(totDem, 0) + ' kNm³/h. Reformer supplies ' + f(refH2, 0) + ' kNm³/h and PSA recovers ' + f(psaH2, 1) + ' kNm³/h, leaving ' + (deficit > 0 ? 'a net deficit of ' + f(deficit, 1) + ' kNm³/h to be generated by on-site steam methane reforming (SMR).' : 'a self-sufficient balanced hydrogen header.');
        }
        [sR, sHC, sHT, sP].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Refinery Decarbonization & Carbon Intensity Sizing</h3><p class="lead">Simulate Energy Intensity Index (EII), furnace fuel gas decarbonization, and CO2 abatement cost.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Refinery EII Index <span><output id="v-eii">92</output></span></label><input type="range" id="s-eii" min="70" max="130" step="2" value="92"></div>' +
              '<div class="control-group"><label>Hydrogen Fuel Blend <span><output id="v-h2fuel">15%</output> H2</span></label><input type="range" id="s-h2fuel" min="0" max="60" step="5" value="15"></div>' +
              '<div class="control-group"><label>Crude Capacity <span><output id="v-carbcap">150</output> kbpd</span></label><input type="range" id="s-carbcap" min="50" max="350" step="25" value="150"></div>' +
              '<div class="control-group"><label>Carbon Tax Policy <span><output id="v-ctax">$60</output>/ton CO2</span></label><input type="range" id="s-ctax" min="20" max="150" step="10" value="60"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Carbon Intensity</span><span class="value" id="r-carbint">38.5 kg/bbl</span><span class="subtext">CO2 per barrel crude</span></div>' +
              '<div class="readout-card"><span class="label">Annual CO2 Emission</span><span class="value" id="r-annco2">0 kt/yr</span><span class="subtext">total direct footprint</span></div>' +
              '<div class="readout-card"><span class="label">Emissions Abated</span><span class="value" id="r-abated">0%</span><span class="subtext">reduction vs baseline</span></div>' +
              '<div class="readout-card"><span class="label">Carbon Tax Bill</span><span class="value" id="r-taxbill">$0 M/yr</span><span class="subtext">regulatory cost</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pet-u8" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pet-u8"></div>',
      init: function(card) {
        var sE = card.querySelector('#s-eii'), vE = card.querySelector('#v-eii');
        var sH = card.querySelector('#s-h2fuel'), vH = card.querySelector('#v-h2fuel');
        var sC = card.querySelector('#s-carbcap'), vC = card.querySelector('#v-carbcap');
        var sT = card.querySelector('#s-ctax'), vT = card.querySelector('#v-ctax');
        var rInt = card.querySelector('#r-carbint'), rAnn = card.querySelector('#r-annco2');
        var rAb = card.querySelector('#r-abated'), rBill = card.querySelector('#r-taxbill');
        var svg = card.querySelector('#plot-pet-u8'), diag = card.querySelector('#diag-pet-u8');

        function update() {
          var eii = parseFloat(sE.value); vE.textContent = f(eii, 0);
          var h2f = parseFloat(sH.value) / 100; vH.textContent = f(h2f * 100, 0) + '% H2';
          var cap = parseFloat(sC.value); vC.textContent = f(cap, 0);
          var ctax = parseFloat(sT.value); vT.textContent = '$' + f(ctax, 0);

          var baseCI = 42.0 * (eii / 100);
          var ci = baseCI * (1.0 - h2f * 0.45);
          var bpd = cap * 1000;
          var annualCo2 = (bpd * 365 * ci) / 1e6; // kt CO2/yr
          var baselineCo2 = (bpd * 365 * 42.0) / 1e6;
          var abated = ((baselineCo2 - annualCo2) / baselineCo2) * 100;
          var taxBill = (annualCo2 * 1000 * ctax) / 1e6; // $M/yr

          rInt.textContent = f(ci, 1) + ' kg/bbl';
          rAnn.textContent = f(annualCo2, 0) + ' kt/yr';
          rAb.textContent = f(abated, 1) + ' %';
          rBill.textContent = '$' + f(taxBill, 1) + ' M/yr';

          // SVG Decarbonization pathway bar
          var barW = 440;
          var curBar = (annualCo2 / (baselineCo2 * 1.2)) * barW;
          var abBar = (abated / 100) * curBar;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="65" width="' + curBar.toFixed(1) + '" height="35" fill="#f59e0b" rx="2"/>' +
                          '<rect x="' + (80 + curBar - abBar).toFixed(1) + '" y="65" width="' + abBar.toFixed(1) + '" height="35" fill="#10b981" rx="2"/>' +
                          '<text x="80" y="125" font-size="11" fill="#b45309">Remaining Footprint: ' + f(annualCo2,0) + ' kt/yr</text>' +
                          '<text x="520" y="125" text-anchor="end" font-size="11" fill="#047857">Abated: ' + f(abated,1) + '%</text>' +
                          '<text x="300" y="30" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Refinery Decarbonization: CI = ' + f(ci, 1) + ' kg CO2/bbl (Tax: $' + f(taxBill, 1) + ' M/yr)</text>';
          diag.textContent = 'Refinery carbon intensity evaluation: At Energy Intensity Index EII = ' + f(eii, 0) + ' and ' + f(h2f * 100, 0) + '% hydrogen fuel gas firing, carbon intensity is ' + f(ci, 1) + ' kg CO2/bbl (' + f(abated, 1) + '% reduction vs baseline). At $' + f(ctax, 0) + '/ton carbon tax, annual liability is $' + f(taxBill, 1) + ' M/yr across ' + f(cap, 0) + ' kbpd capacity.';
        }
        [sE, sH, sC, sT].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    }
  ];
""" + get_engine_footer(8)

def main():
    sims = {
        'process-design': build_pdes_sims(),
        'process-safety': build_psafe_sims(),
        'biochemical-engineering': build_bio_sims(),
        'polymer-process-engineering': build_poly_sims(),
        'petroleum-and-petrochemical-processes': build_pet_sims(),
    }
    for slug, code in sims.items():
        out_file = os.path.join(ROOT, 'src', 'subjects', 'chemical-process-engineering', slug, f'{slug}-sims.js')
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(code)
        print(f'Wrote {out_file} ({len(code)} bytes)')

if __name__ == '__main__':
    main()
