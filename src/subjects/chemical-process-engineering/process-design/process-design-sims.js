/* Process Design Interactive Simulation Suite */
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
              '<div class="control-group"><label>Design Maturity <span><output id="v-pid">Class 3 (±15%)</output></span></label><input type="range" id="s-pid" min="1" max="3" step="1" value="2"></div>' +
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
        var sM = card.querySelector('#s-pid'), vM = card.querySelector('#v-pid');
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
