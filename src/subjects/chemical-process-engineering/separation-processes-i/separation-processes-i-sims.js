/* Separation Processes I Interactive Simulation Suite */
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
