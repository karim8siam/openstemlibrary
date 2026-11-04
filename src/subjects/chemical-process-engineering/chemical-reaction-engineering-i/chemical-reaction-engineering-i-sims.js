/* Chemical Reaction Engineering I Interactive Simulation Suite */
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
