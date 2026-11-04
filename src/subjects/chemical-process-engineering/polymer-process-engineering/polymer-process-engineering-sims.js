/* Polymer Process Engineering Interactive Simulation Suite */
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
