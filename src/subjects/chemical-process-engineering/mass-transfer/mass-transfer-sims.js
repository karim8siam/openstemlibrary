/* Mass Transfer Interactive Simulation Suite */
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
              '<div class="control-group"><label>Henrys Slope m <span><output id="v-hm">1.50</output></span></label><input type="range" id="s-hm" min="0.10" max="10.00" step="0.10" value="1.50"></div>' +
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
