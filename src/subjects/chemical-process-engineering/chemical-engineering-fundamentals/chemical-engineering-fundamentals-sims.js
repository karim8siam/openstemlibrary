/* Chemical Engineering Fundamentals Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Chemical Manufacturing Economic Mass Balance</h3><p class="lead">Simulate plant production throughput, conversion yield, operating revenues, and net economic value addition.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Feedstock Rate <span><output id="v-feed">500</output> ton/day</span></label><input type="range" id="s-feed" min="100" max="2000" step="50" value="500"></div>' +
              '<div class="control-group"><label>Conversion Yield <span><output id="v-yield">85.0</output> %</span></label><input type="range" id="s-yield" min="50.0" max="98.0" step="0.5" value="85.0"></div>' +
              '<div class="control-group"><label>Feedstock Cost <span><output id="v-feedcost">450</output> $/ton</span></label><input type="range" id="s-feedcost" min="100" max="1200" step="25" value="450"></div>' +
              '<div class="control-group"><label>Product Selling Price <span><output id="v-prodprice">950</output> $/ton</span></label><input type="range" id="s-prodprice" min="500" max="2500" step="50" value="950"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Product Output</div><div class="readout-value" id="r-out">425.00 ton/day</div></div>' +
              '<div class="readout-card"><div class="readout-label">Gross Daily Revenue</div><div class="readout-value" id="r-rev">$403,750</div></div>' +
              '<div class="readout-card"><div class="readout-label">Feedstock Daily Cost</div><div class="readout-value" id="r-cost">$225,000</div></div>' +
              '<div class="readout-card"><div class="readout-label">Daily Operating Margin</div><div class="readout-value" id="r-margin">$178,750</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-cef1" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-cef1"></p>',
      init: function(el) {
        var sFeed = el.querySelector('#s-feed'), vFeed = el.querySelector('#v-feed');
        var sYield = el.querySelector('#s-yield'), vYield = el.querySelector('#v-yield');
        var sFeedCost = el.querySelector('#s-feedcost'), vFeedCost = el.querySelector('#v-feedcost');
        var sProdPrice = el.querySelector('#s-prodprice'), vProdPrice = el.querySelector('#v-prodprice');
        var rOut = el.querySelector('#r-out'), rRev = el.querySelector('#r-rev');
        var rCost = el.querySelector('#r-cost'), rMargin = el.querySelector('#r-margin');
        var svg = el.querySelector('#svg-cef1'), diag = el.querySelector('#diag-cef1');

        function update() {
          var feed = parseFloat(sFeed.value); vFeed.textContent = f(feed, 0);
          var y = parseFloat(sYield.value) / 100; vYield.textContent = f(y * 100, 1);
          var cFeed = parseFloat(sFeedCost.value); vFeedCost.textContent = f(cFeed, 0);
          var pPrice = parseFloat(sProdPrice.value); vProdPrice.textContent = f(pPrice, 0);

          var prod = feed * y;
          var rev = prod * pPrice;
          var cost = feed * cFeed;
          var margin = rev - cost;
          var ratio = cost > 0 ? (rev / cost) : 1;

          rOut.textContent = f(prod, 1) + ' ton/day';
          rRev.textContent = '$' + f(rev, 0);
          rCost.textContent = '$' + f(cost, 0);
          rMargin.textContent = '$' + f(margin, 0);

          var barW = Math.min(260, Math.max(20, (prod / 2000) * 260));
          var byprodW = Math.max(10, ((feed - prod) / 2000) * 260);

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="40" y="70" width="100" height="60" fill="#e2e8f0" stroke="#475569" stroke-width="2" rx="4"/>' +
                          '<text x="90" y="105" text-anchor="middle" font-size="12" font-weight="700" fill="#1e293b">Raw Feed</text>' +
                          '<text x="90" y="120" text-anchor="middle" font-size="10" fill="#64748b">' + f(feed,0) + ' t/d</text>' +
                          '<line x1="140" y1="100" x2="220" y2="100" stroke="#0284c7" stroke-width="4" marker-end="url(#arrow)"/>' +
                          '<rect x="220" y="55" width="140" height="90" fill="#0284c7" fill-opacity="0.1" stroke="#0284c7" stroke-width="2" rx="6"/>' +
                          '<text x="290" y="95" text-anchor="middle" font-size="13" font-weight="700" fill="#0369a1">Chemical Plant</text>' +
                          '<text x="290" y="115" text-anchor="middle" font-size="11" fill="#0284c7">Yield: ' + f(y*100, 1) + '%</text>' +
                          '<line x1="360" y1="80" x2="440" y2="80" stroke="#16a34a" stroke-width="4"/>' +
                          '<rect x="440" y="50" width="' + barW + '" height="50" fill="#22c55e" fill-opacity="0.2" stroke="#16a34a" stroke-width="2" rx="4"/>' +
                          '<text x="' + (440 + barW/2) + '" y="80" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">Product: ' + f(prod,0) + ' t/d</text>' +
                          '<line x1="360" y1="120" x2="440" y2="150" stroke="#eab308" stroke-width="3"/>' +
                          '<rect x="440" y="130" width="' + byprodW + '" height="35" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5" rx="4"/>' +
                          '<text x="' + (440 + byprodW/2) + '" y="152" text-anchor="middle" font-size="10" fill="#854d0e">Byproduct/Loss</text>';
          diag.textContent = 'Value addition factor: ' + f(ratio, 2) + 'x raw materials cost. Net daily economic generation: $' + f(margin, 0) + '.';
        }
        [sFeed, sYield, sFeedCost, sProdPrice].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Dimensional Analysis & Reynolds Number Simulator</h3><p class="lead">Simulate flow regime, dynamic Reynolds number Re, and friction factor in process piping across fluid property variations.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Pipe Diameter D <span><output id="v-d">0.100</output> m</span></label><input type="range" id="s-d" min="0.02" max="0.50" step="0.01" value="0.10"></div>' +
              '<div class="control-group"><label>Fluid Velocity v <span><output id="v-vel">1.50</output> m/s</span></label><input type="range" id="s-vel" min="0.1" max="10.0" step="0.1" value="1.5"></div>' +
              '<div class="control-group"><label>Fluid Density ρ <span><output id="v-rho">1000</output> kg/m³</span></label><input type="range" id="s-rho" min="600" max="1600" step="50" value="1000"></div>' +
              '<div class="control-group"><label>Dynamic Viscosity μ <span><output id="v-mu">0.0010</output> Pa·s</span></label><input type="range" id="s-mu" min="0.0005" max="0.0500" step="0.0005" value="0.0010"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Reynolds Number (Re)</div><div class="readout-value" id="r-re">150,000</div></div>' +
              '<div class="readout-card"><div class="readout-label">Flow Regime</div><div class="readout-value" id="r-regime">Turbulent Flow</div></div>' +
              '<div class="readout-card"><div class="readout-label">Darcy Friction Factor</div><div class="readout-value" id="r-f">0.0168</div></div>' +
              '<div class="readout-card"><div class="readout-label">Pressure Gradient ΔP/L</div><div class="readout-value" id="r-dpl">189.0 Pa/m</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-cef2" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-cef2"></p>',
      init: function(el) {
        var sD = el.querySelector('#s-d'), vD = el.querySelector('#v-d');
        var sVel = el.querySelector('#s-vel'), vVel = el.querySelector('#v-vel');
        var sRho = el.querySelector('#s-rho'), vRho = el.querySelector('#v-rho');
        var sMu = el.querySelector('#s-mu'), vMu = el.querySelector('#v-mu');
        var rRe = el.querySelector('#r-re'), rRegime = el.querySelector('#r-regime');
        var rF = el.querySelector('#r-f'), rDpl = el.querySelector('#r-dpl');
        var svg = el.querySelector('#svg-cef2'), diag = el.querySelector('#diag-cef2');

        function update() {
          var D = parseFloat(sD.value); vD.textContent = f(D, 3);
          var v = parseFloat(sVel.value); vVel.textContent = f(v, 2);
          var rho = parseFloat(sRho.value); vRho.textContent = f(rho, 0);
          var mu = parseFloat(sMu.value); vMu.textContent = f(mu, 4);

          var Re = (rho * v * D) / mu;
          var regime = 'Laminar (Re < 2,100)';
          var fFactor = 64 / Math.max(1, Re);
          if (Re >= 2100 && Re <= 4000) {
            regime = 'Transition Flow';
            fFactor = 0.035;
          } else if (Re > 4000) {
            regime = 'Turbulent (Re > 4,000)';
            fFactor = 0.3164 / Math.pow(Re, 0.25); // Blasius smooth pipe
          }
          var dP_L = (fFactor * rho * v * v) / (2 * D);

          rRe.textContent = f(Re, 0);
          rRegime.textContent = regime;
          rF.textContent = f(fFactor, 4);
          rDpl.textContent = f(dP_L, 1) + ' Pa/m';

          var isTurb = Re > 4000;
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="50" y="40" width="500" height="120" fill="#f1f5f9" stroke="#334155" stroke-width="3" rx="4"/>' +
                          '<line x1="50" y1="100" x2="550" y2="100" stroke="#94a3b8" stroke-dasharray="6 4"/>' +
                          '<path d="M 80 45 Q ' + (isTurb ? 140 : 250) + ' 100 80 155" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<path d="M 230 45 Q ' + (isTurb ? 290 : 400) + ' 100 230 155" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<path d="M 380 45 Q ' + (isTurb ? 440 : 550) + ' 100 380 155" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Velocity Profile: ' + (isTurb ? 'Turbulent (Flattened Core)' : 'Laminar (Parabolic Poiseuille)') + '</text>' +
                          '<text x="300" y="180" text-anchor="middle" font-size="11" fill="#475569">Pipe D = ' + f(D*1000, 0) + ' mm | Mean v = ' + f(v, 2) + ' m/s</text>';
          diag.textContent = 'Dimensionless Reynolds Number: Re = ' + f(Re, 0) + '. Hydraulic head loss gradient: ' + f(dP_L, 1) + ' Pa per meter of pipe.';
        }
        [sD, sVel, sRho, sMu].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Degrees of Freedom & Stream Balance Solver</h3><p class="lead">Audit process flowsheet solvability: verify whether system is correctly specified (Ndf = 0), overspecified, or underspecified.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Unknown Stream Variables (Nv) <span><output id="v-nv">6</output></span></label><input type="range" id="s-nv" min="3" max="15" step="1" value="6"></div>' +
              '<div class="control-group"><label>Independent Material Balances (Nm) <span><output id="v-nm">3</output></span></label><input type="range" id="s-nm" min="1" max="8" step="1" value="3"></div>' +
              '<div class="control-group"><label>Specified Compositions/Flows (Ns) <span><output id="v-ns">2</output></span></label><input type="range" id="s-ns" min="0" max="8" step="1" value="2"></div>' +
              '<div class="control-group"><label>Auxiliary Physical Relations (Nr) <span><output id="v-nr">1</output></span></label><input type="range" id="s-nr" min="0" max="4" step="1" value="1"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Independent Equations (Ne)</div><div class="readout-value" id="r-ne">6</div></div>' +
              '<div class="readout-card"><div class="readout-label">Degrees of Freedom (Ndf)</div><div class="readout-value" id="r-ndf">0</div></div>' +
              '<div class="readout-card"><div class="readout-label">Solvability Status</div><div class="readout-value" id="r-status">Exactly Specified</div></div>' +
              '<div class="readout-card"><div class="readout-label">Action Required</div><div class="readout-value" id="r-action">Solve Linear System</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-cef3" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-cef3"></p>',
      init: function(el) {
        var sNv = el.querySelector('#s-nv'), vNv = el.querySelector('#v-nv');
        var sNm = el.querySelector('#s-nm'), vNm = el.querySelector('#v-nm');
        var sNs = el.querySelector('#s-ns'), vNs = el.querySelector('#v-ns');
        var sNr = el.querySelector('#s-nr'), vNr = el.querySelector('#v-nr');
        var rNe = el.querySelector('#r-ne'), rNdf = el.querySelector('#r-ndf');
        var rStatus = el.querySelector('#r-status'), rAction = el.querySelector('#r-action');
        var svg = el.querySelector('#svg-cef3'), diag = el.querySelector('#diag-cef3');

        function update() {
          var nv = parseInt(sNv.value, 10); vNv.textContent = nv;
          var nm = parseInt(sNm.value, 10); vNm.textContent = nm;
          var ns = parseInt(sNs.value, 10); vNs.textContent = ns;
          var nr = parseInt(sNr.value, 10); vNr.textContent = nr;

          var ne = nm + ns + nr;
          var ndf = nv - ne;

          rNe.textContent = ne;
          rNdf.textContent = ndf;

          var statusColor = '#16a34a';
          if (ndf === 0) {
            rStatus.textContent = 'Unique Solution (Ndf = 0)';
            rAction.textContent = 'System solvable without extra data';
          } else if (ndf > 0) {
            statusColor = '#ea580c';
            rStatus.textContent = 'Under-specified (Ndf = +' + ndf + ')';
            rAction.textContent = 'Specify ' + ndf + ' additional stream variables';
          } else {
            statusColor = '#dc2626';
            rStatus.textContent = 'Over-specified (Ndf = ' + ndf + ')';
            rAction.textContent = 'Remove ' + Math.abs(ndf) + ' redundant constraints';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="50" width="180" height="100" fill="#e0f2fe" stroke="#0284c7" stroke-width="2" rx="6"/>' +
                          '<text x="170" y="85" text-anchor="middle" font-size="13" font-weight="700" fill="#0369a1">Unknowns Nv</text>' +
                          '<text x="170" y="115" text-anchor="middle" font-size="24" font-weight="800" fill="#0284c7">' + nv + '</text>' +
                          '<rect x="340" y="50" width="180" height="100" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="6"/>' +
                          '<text x="430" y="85" text-anchor="middle" font-size="13" font-weight="700" fill="#92400e">Equations Ne</text>' +
                          '<text x="430" y="115" text-anchor="middle" font-size="24" font-weight="800" fill="#b45309">' + ne + '</text>' +
                          '<circle cx="300" cy="100" r="28" fill="' + statusColor + '"/>' +
                          '<text x="300" y="106" text-anchor="middle" font-size="14" font-weight="800" fill="#ffffff">' + (ndf >= 0 ? '+' + ndf : ndf) + '</text>' +
                          '<text x="300" y="180" text-anchor="middle" font-size="12" font-weight="700" fill="' + statusColor + '">' + rStatus.textContent + '</text>';
          diag.textContent = 'Degrees of Freedom analysis: Ndf = Nv - (Nm + Ns + Nr) = ' + nv + ' - ' + ne + ' = ' + ndf + '.';
        }
        [sNv, sNm, sNs, sNr].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Recycle and Purge Stream Conservation Simulator</h3><p class="lead">Simulate material flow accumulation, recycle ratio, single-pass vs. overall plant conversion, and purge fraction.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Fresh Feed F0 <span><output id="v-f0">100</output> mol/h</span></label><input type="range" id="s-f0" min="20" max="500" step="10" value="100"></div>' +
              '<div class="control-group"><label>Single-Pass Conversion Xsp <span><output id="v-xsp">30.0</output> %</span></label><input type="range" id="s-xsp" min="10.0" max="80.0" step="1.0" value="30.0"></div>' +
              '<div class="control-group"><label>Purge Fraction fp <span><output id="v-fp">10.0</output> %</span></label><input type="range" id="s-fp" min="2.0" max="40.0" step="1.0" value="10.0"></div>' +
              '<div class="control-group"><label>Overall Required Conversion <span><output id="v-xov">92.0</output> %</span></label><input type="range" id="s-xov" min="70.0" max="99.0" step="1.0" value="92.0"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Recycle Flow (R)</div><div class="readout-value" id="r-rf">206.67 mol/h</div></div>' +
              '<div class="readout-card"><div class="readout-label">Purge Stream (P)</div><div class="readout-value" id="r-pur">22.96 mol/h</div></div>' +
              '<div class="readout-card"><div class="readout-label">Reactor Feed (F1)</div><div class="readout-value" id="r-rf1">306.67 mol/h</div></div>' +
              '<div class="readout-card"><div class="readout-label">Recycle Ratio (R/F0)</div><div class="readout-value" id="r-rr">2.07</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-cef4" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-cef4"></p>',
      init: function(el) {
        var sF0 = el.querySelector('#s-f0'), vF0 = el.querySelector('#v-f0');
        var sXsp = el.querySelector('#s-xsp'), vXsp = el.querySelector('#v-xsp');
        var sFp = el.querySelector('#s-fp'), vFp = el.querySelector('#v-fp');
        var sXov = el.querySelector('#s-xov'), vXov = el.querySelector('#v-xov');
        var rRf = el.querySelector('#r-rf'), rPur = el.querySelector('#r-pur');
        var rRf1 = el.querySelector('#r-rf1'), rRr = el.querySelector('#r-rr');
        var svg = el.querySelector('#svg-cef4'), diag = el.querySelector('#diag-cef4');

        function update() {
          var F0 = parseFloat(sF0.value); vF0.textContent = f(F0, 0);
          var Xsp = parseFloat(sXsp.value) / 100; vXsp.textContent = f(Xsp * 100, 1);
          var fp = parseFloat(sFp.value) / 100; vFp.textContent = f(fp * 100, 1);
          var Xov = parseFloat(sXov.value) / 100; vXov.textContent = f(Xov * 100, 1);

          // In recycle system with purge: F1 = F0 / (1 - (1 - Xsp)*(1 - fp))
          var denom = 1 - (1 - Xsp) * (1 - fp);
          var F1 = F0 / Math.max(0.01, denom);
          var unreacted = F1 * (1 - Xsp);
          var P = unreacted * fp;
          var R = unreacted * (1 - fp);
          var recRatio = F0 > 0 ? (R / F0) : 0;

          rRf.textContent = f(R, 2) + ' mol/h';
          rPur.textContent = f(P, 2) + ' mol/h';
          rRf1.textContent = f(F1, 2) + ' mol/h';
          rRr.textContent = f(recRatio, 2);

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="230" y="70" width="120" height="70" fill="#dbeafe" stroke="#2563eb" stroke-width="2" rx="4"/>' +
                          '<text x="290" y="105" text-anchor="middle" font-size="12" font-weight="700" fill="#1e40af">Reactor (Xsp=' + f(Xsp*100,0) + '%)</text>' +
                          '<text x="290" y="125" text-anchor="middle" font-size="11" fill="#3b82f6">Feed: ' + f(F1,1) + '</text>' +
                          '<line x1="50" y1="105" x2="230" y2="105" stroke="#0f172a" stroke-width="3"/>' +
                          '<text x="110" y="95" font-size="11" fill="#334155" font-weight="700">F0: ' + f(F0,0) + '</text>' +
                          '<line x1="350" y1="105" x2="440" y2="105" stroke="#0f172a" stroke-width="3"/>' +
                          '<rect x="440" y="70" width="80" height="70" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="4"/>' +
                          '<text x="480" y="110" text-anchor="middle" font-size="11" font-weight="700" fill="#92400e">Separator</text>' +
                          '<line x1="480" y1="70" x2="480" y2="35" stroke="#dc2626" stroke-width="3"/>' +
                          '<text x="490" y="45" font-size="10" fill="#dc2626" font-weight="700">Purge: ' + f(P,1) + '</text>' +
                          '<path d="M 480 35 L 170 35 L 170 105" fill="none" stroke="#16a34a" stroke-width="3"/>' +
                          '<text x="310" y="28" text-anchor="middle" font-size="11" fill="#15803d" font-weight="700">Recycle R: ' + f(R,1) + ' mol/h</text>';
          diag.textContent = 'Steady-state recycle loop: Reactor feed F1 = ' + f(F1, 2) + ' mol/h (' + f(recRatio, 2) + 'x fresh feed). Purge stream P removes inerts.';
        }
        [sF0, sXsp, sFp, sXov].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Continuous Reactor Enthalpy and Heat Duty Simulator</h3><p class="lead">Simulate sensible temperature changes, heat of reaction, and net cooling/heating utility duties in continuous reactors.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Molar Flow Rate <span><output id="v-flow">50.0</output> mol/s</span></label><input type="range" id="s-flow" min="10" max="200" step="5" value="50"></div>' +
              '<div class="control-group"><label>Inlet Temp Tin <span><output id="v-tin">25.0</output> °C</span></label><input type="range" id="s-tin" min="10" max="150" step="5" value="25"></div>' +
              '<div class="control-group"><label>Outlet Temp Tout <span><output id="v-tout">180.0</output> °C</span></label><input type="range" id="s-tout" min="50" max="400" step="10" value="180"></div>' +
              '<div class="control-group"><label>Reaction Heat ΔHrxn <span><output id="v-dhrxn">-65.0</output> kJ/mol</span></label><input type="range" id="s-dhrxn" min="-150" max="50" step="5" value="-65"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Sensible Enthalpy ΔHsens</div><div class="readout-value" id="r-sens">310.0 kW</div></div>' +
              '<div class="readout-card"><div class="readout-label">Reaction Heat Release</div><div class="readout-value" id="r-rxn">-3,250.0 kW</div></div>' +
              '<div class="readout-card"><div class="readout-label">Net Required Duty Q̇</div><div class="readout-value" id="r-qdot">-2,940.0 kW</div></div>' +
              '<div class="readout-card"><div class="readout-label">Utility Mode</div><div class="readout-value" id="r-mode">Jacket Cooling Required</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-cef5" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-cef5"></p>',
      init: function(el) {
        var sFlow = el.querySelector('#s-flow'), vFlow = el.querySelector('#v-flow');
        var sTin = el.querySelector('#s-tin'), vTin = el.querySelector('#v-tin');
        var sTout = el.querySelector('#s-tout'), vTout = el.querySelector('#v-tout');
        var sDhrxn = el.querySelector('#s-dhrxn'), vDhrxn = el.querySelector('#v-dhrxn');
        var rSens = el.querySelector('#r-sens'), rRxn = el.querySelector('#r-rxn');
        var rQdot = el.querySelector('#r-qdot'), rMode = el.querySelector('#r-mode');
        var svg = el.querySelector('#svg-cef5'), diag = el.querySelector('#diag-cef5');

        var Cp = 0.040; // kJ/(mol·K) average mean heat capacity

        function update() {
          var nDot = parseFloat(sFlow.value); vFlow.textContent = f(nDot, 1);
          var Tin = parseFloat(sTin.value); vTin.textContent = f(Tin, 1);
          var Tout = parseFloat(sTout.value); vTout.textContent = f(Tout, 1);
          var dHrxn = parseFloat(sDhrxn.value); vDhrxn.textContent = f(dHrxn, 1);

          var deltaT = Tout - Tin;
          var Qsens = nDot * Cp * deltaT; // kW
          var Qrxn = nDot * dHrxn; // kW
          var Qnet = Qsens + Qrxn; // kW

          rSens.textContent = f(Qsens, 1) + ' kW';
          rRxn.textContent = f(Qrxn, 1) + ' kW';
          rQdot.textContent = f(Qnet, 1) + ' kW';

          var isCooling = Qnet < 0;
          rMode.textContent = isCooling ? 'Jacket Cooling Required' : 'Process Heating Required';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="220" y="40" width="160" height="120" fill="' + (isCooling ? '#fee2e2' : '#ffedd5') + '" stroke="' + (isCooling ? '#ef4444' : '#f97316') + '" stroke-width="3" rx="8"/>' +
                          '<text x="300" y="80" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">CSTR Vessel</text>' +
                          '<text x="300" y="105" text-anchor="middle" font-size="12" fill="#475569">Tout = ' + f(Tout, 0) + ' °C</text>' +
                          '<text x="300" y="130" text-anchor="middle" font-size="12" font-weight="700" fill="' + (isCooling ? '#b91c1c' : '#c2410c') + '">Q̇ = ' + f(Qnet, 1) + ' kW</text>' +
                          '<line x1="60" y1="100" x2="220" y2="100" stroke="#0284c7" stroke-width="4"/>' +
                          '<text x="140" y="85" text-anchor="middle" font-size="11" font-weight="700" fill="#0369a1">In: ' + f(Tin, 0) + ' °C (' + f(nDot, 0) + ' mol/s)</text>' +
                          '<line x1="380" y1="100" x2="540" y2="100" stroke="#059669" stroke-width="4"/>' +
                          '<text x="460" y="85" text-anchor="middle" font-size="11" font-weight="700" fill="#047857">Out: ' + f(Tout, 0) + ' °C</text>';
          diag.textContent = 'Energy balance: Q̇ = ΔHsens + ΔHrxn = ' + f(Qsens, 1) + ' + (' + f(Qrxn, 1) + ') = ' + f(Qnet, 1) + ' kW.';
        }
        [sFlow, sTin, sTout, sDhrxn].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Van der Waals PVT Equation of State Simulator</h3><p class="lead">Compare ideal gas law vs. Van der Waals real fluid PV isotherms, critical point compressibility, and non-ideality.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Temperature T <span><output id="v-temp">350</output> K</span></label><input type="range" id="s-temp" min="200" max="600" step="10" value="350"></div>' +
              '<div class="control-group"><label>Molar Volume Vm <span><output id="v-vm">0.80</output> L/mol</span></label><input type="range" id="s-vm" min="0.10" max="4.00" step="0.05" value="0.80"></div>' +
              '<div class="control-group"><label>vdW Parameter a <span><output id="v-va">3.64</output> bar·L²/mol²</span></label><input type="range" id="s-va" min="0.5" max="10.0" step="0.1" value="3.64"></div>' +
              '<div class="control-group"><label>vdW Parameter b <span><output id="v-vb">0.0427</output> L/mol</span></label><input type="range" id="s-vb" min="0.010" max="0.100" step="0.005" value="0.0427"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Ideal Gas Pressure</div><div class="readout-value" id="r-pid">36.38 bar</div></div>' +
              '<div class="readout-card"><div class="readout-label">vdW Real Gas Pressure</div><div class="readout-value" id="r-pvdw">32.65 bar</div></div>' +
              '<div class="readout-card"><div class="readout-label">Compressibility Factor Z</div><div class="readout-value" id="r-z">0.897</div></div>' +
              '<div class="readout-card"><div class="readout-label">Non-Ideality Deviation</div><div class="readout-value" id="r-dev">-10.3 %</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-cef6" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-cef6"></p>',
      init: function(el) {
        var sTemp = el.querySelector('#s-temp'), vTemp = el.querySelector('#v-temp');
        var sVm = el.querySelector('#s-vm'), vVm = el.querySelector('#v-vm');
        var sVa = el.querySelector('#s-va'), vVa = el.querySelector('#v-va');
        var sVb = el.querySelector('#s-vb'), vVb = el.querySelector('#v-vb');
        var rPid = el.querySelector('#r-pid'), rPvdw = el.querySelector('#r-pvdw');
        var rZ = el.querySelector('#r-z'), rDev = el.querySelector('#r-dev');
        var svg = el.querySelector('#svg-cef6'), diag = el.querySelector('#diag-cef6');

        var R = 0.08314; // bar·L/(mol·K)

        function update() {
          var T = parseFloat(sTemp.value); vTemp.textContent = f(T, 0);
          var Vm = parseFloat(sVm.value); vVm.textContent = f(Vm, 2);
          var a = parseFloat(sVa.value); vVa.textContent = f(a, 2);
          var b = parseFloat(sVb.value); vVb.textContent = f(b, 4);

          var Pideal = (R * T) / Vm;
          var denom = Math.max(0.001, Vm - b);
          var PvdW = (R * T) / denom - a / (Vm * Vm);
          PvdW = Math.max(0.01, PvdW);

          var Z = (PvdW * Vm) / (R * T);
          var deviation = ((PvdW - Pideal) / Pideal) * 100;

          rPid.textContent = f(Pideal, 2) + ' bar';
          rPvdw.textContent = f(PvdW, 2) + ' bar';
          rZ.textContent = f(Z, 3);
          rDev.textContent = (deviation >= 0 ? '+' : '') + f(deviation, 1) + ' %';

          // Render PV curve points
          var ptsIdeal = [], ptsVdw = [];
          for (var vStep = 0.1; vStep <= 4.0; vStep += 0.1) {
            var x = 80 + (vStep / 4.0) * 480;
            var pi = (R * T) / vStep;
            var pv = (R * T) / Math.max(0.001, vStep - b) - a / (vStep * vStep);
            pv = Math.max(0, Math.min(100, pv));
            pi = Math.max(0, Math.min(100, pi));
            var yi = 180 - (pi / 100) * 150;
            var yv = 180 - (pv / 100) * 150;
            ptsIdeal.push(f(x,1) + ',' + f(yi,1));
            ptsVdw.push(f(x,1) + ',' + f(yv,1));
          }

          var curX = 80 + (Vm / 4.0) * 480;
          var curY = 180 - (Math.min(100, PvdW) / 100) * 150;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<polyline points="' + ptsIdeal.join(' ') + '" fill="none" stroke="#94a3b8" stroke-dasharray="4 4" stroke-width="2"/>' +
                          '<polyline points="' + ptsVdw.join(' ') + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<circle cx="' + curX + '" cy="' + curY + '" r="6" fill="#dc2626"/>' +
                          '<text x="80" y="25" font-size="11" font-weight="700" fill="#2563eb">vdW Isotherm (T=' + f(T,0) + 'K)</text>' +
                          '<text x="250" y="25" font-size="11" fill="#64748b">-- Ideal Gas</text>' +
                          '<text x="' + (curX + 10) + '" y="' + curY + '" font-size="11" font-weight="700" fill="#dc2626">Vm=' + f(Vm,2) + 'L, P=' + f(PvdW,1) + 'bar</text>';
          diag.textContent = 'Equation of state comparison at T = ' + f(T, 0) + ' K: Z = ' + f(Z, 3) + '. Attraction parameter a reduces pressure by ' + f(a / (Vm * Vm), 2) + ' bar.';
        }
        [sTemp, sVm, sVa, sVb].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Heat Exchanger LMTD and Sizing Simulator</h3><p class="lead">Size process shell-and-tube exchangers: calculate countercurrent log mean temperature difference and required heat exchange area.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Heat Duty Q <span><output id="v-qduty">250</output> kW</span></label><input type="range" id="s-qduty" min="50" max="1000" step="25" value="250"></div>' +
              '<div class="control-group"><label>Overall Coeff U <span><output id="v-ucoeff">450</output> W/(m²·K)</span></label><input type="range" id="s-ucoeff" min="100" max="1500" step="50" value="450"></div>' +
              '<div class="control-group"><label>Hot Stream ΔT (In-Out) <span><output id="v-dthot">60.0</output> °C</span></label><input type="range" id="s-dthot" min="20.0" max="120.0" step="5.0" value="60.0"></div>' +
              '<div class="control-group"><label>Cold Stream ΔT (Out-In) <span><output id="v-dtcold">40.0</output> °C</span></label><input type="range" id="s-dtcold" min="15.0" max="90.0" step="5.0" value="40.0"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">LMTD (ΔTlm)</div><div class="readout-value" id="r-lmtd">49.33 °C</div></div>' +
              '<div class="readout-card"><div class="readout-label">Required Area A</div><div class="readout-value" id="r-area">11.26 m²</div></div>' +
              '<div class="readout-card"><div class="readout-label">Tubes Needed (16mm OD)</div><div class="readout-value" id="r-tubes">75 tubes</div></div>' +
              '<div class="readout-card"><div class="readout-label">Thermal Effectiveness</div><div class="readout-value" id="r-eff">66.7 %</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-cef7" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-cef7"></p>',
      init: function(el) {
        var sQduty = el.querySelector('#s-qduty'), vQduty = el.querySelector('#v-qduty');
        var sUcoeff = el.querySelector('#s-ucoeff'), vUcoeff = el.querySelector('#v-ucoeff');
        var sDthot = el.querySelector('#s-dthot'), vDthot = el.querySelector('#v-dthot');
        var sDtcold = el.querySelector('#s-dtcold'), vDtcold = el.querySelector('#v-dtcold');
        var rLmtd = el.querySelector('#r-lmtd'), rArea = el.querySelector('#r-area');
        var rTubes = el.querySelector('#r-tubes'), rEff = el.querySelector('#r-eff');
        var svg = el.querySelector('#svg-cef7'), diag = el.querySelector('#diag-cef7');

        function update() {
          var Q = parseFloat(sQduty.value); vQduty.textContent = f(Q, 0);
          var U = parseFloat(sUcoeff.value); vUcoeff.textContent = f(U, 0);
          var dt1 = parseFloat(sDthot.value); vDthot.textContent = f(dt1, 1);
          var dt2 = parseFloat(sDtcold.value); vDtcold.textContent = f(dt2, 1);

          var lmtd = (dt1 === dt2) ? dt1 : (dt1 - dt2) / Math.log(dt1 / dt2);
          var A = (Q * 1000) / (U * Math.max(0.1, lmtd));
          var tubeArea = Math.PI * 0.016 * 3.0; // 16mm OD, 3m length
          var tubes = Math.ceil(A / tubeArea);
          var eff = (dt2 / Math.max(dt1, dt2)) * 100;

          rLmtd.textContent = f(lmtd, 2) + ' °C';
          rArea.textContent = f(A, 2) + ' m²';
          rTubes.textContent = tubes + ' tubes';
          rEff.textContent = f(eff, 1) + ' %';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="50" width="440" height="100" fill="#e2e8f0" stroke="#475569" stroke-width="2" rx="8"/>' +
                          '<line x1="80" y1="80" x2="520" y2="80" stroke="#ef4444" stroke-width="4"/>' +
                          '<text x="60" y="85" text-anchor="end" font-size="11" font-weight="700" fill="#dc2626">Hot In</text>' +
                          '<text x="540" y="85" text-anchor="start" font-size="11" font-weight="700" fill="#dc2626">Hot Out</text>' +
                          '<line x1="520" y1="120" x2="80" y2="120" stroke="#3b82f6" stroke-width="4"/>' +
                          '<text x="540" y="125" text-anchor="start" font-size="11" font-weight="700" fill="#2563eb">Cold In</text>' +
                          '<text x="60" y="125" text-anchor="end" font-size="11" font-weight="700" fill="#2563eb">Cold Out</text>' +
                          '<text x="300" y="40" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Countercurrent Exchanger: Area = ' + f(A,2) + ' m²</text>' +
                          '<text x="300" y="180" text-anchor="middle" font-size="11" fill="#475569">U = ' + f(U,0) + ' W/(m²·K) | LMTD = ' + f(lmtd,1) + ' °C | ' + tubes + ' tubes (3m x 16mm)</text>';
          diag.textContent = 'Exchanger heat balance: Q = U·A·ΔTlm = ' + f(Q, 0) + ' kW. Required heat transfer area A = ' + f(A, 2) + ' m².';
        }
        [sQduty, sUcoeff, sDthot, sDtcold].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Process Safety & Economic Capital Payback Simulator</h3><p class="lead">Assess Dow Fire & Explosion Index hazard severity alongside capital expenditure and payback economics.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Material Hazard Factor (MF) <span><output id="v-mf">16</output></span></label><input type="range" id="s-mf" min="1" max="40" step="1" value="16"></div>' +
              '<div class="control-group"><label>Process Hazard Factor (F3) <span><output id="v-f3">2.40</output></span></label><input type="range" id="s-f3" min="1.0" max="5.0" step="0.1" value="2.4"></div>' +
              '<div class="control-group"><label>Capital Investment (CapEx) <span><output id="v-capex">5.0</output> $M</span></label><input type="range" id="s-capex" min="0.5" max="25.0" step="0.5" value="5.0"></div>' +
              '<div class="control-group"><label>Annual Net Cash Flow <span><output id="v-cash">1.40</output> $M/yr</span></label><input type="range" id="s-cash" min="0.1" max="8.0" step="0.1" value="1.4"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Fire & Explosion Index</div><div class="readout-value" id="r-fei">38.4</div></div>' +
              '<div class="readout-card"><div class="readout-label">Hazard Classification</div><div class="readout-value" id="r-hazard">Moderate Hazard</div></div>' +
              '<div class="readout-card"><div class="readout-label">Simple Payback Period</div><div class="readout-value" id="r-payback">3.57 years</div></div>' +
              '<div class="readout-card"><div class="readout-label">Return on Investment (ROI)</div><div class="readout-value" id="r-roi">28.0 %</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-cef8" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-cef8"></p>',
      init: function(el) {
        var sMf = el.querySelector('#s-mf'), vMf = el.querySelector('#v-mf');
        var sF3 = el.querySelector('#s-f3'), vF3 = el.querySelector('#v-f3');
        var sCapex = el.querySelector('#s-capex'), vCapex = el.querySelector('#v-capex');
        var sCash = el.querySelector('#s-cash'), vCash = el.querySelector('#v-cash');
        var rFei = el.querySelector('#r-fei'), rHazard = el.querySelector('#r-hazard');
        var rPayback = el.querySelector('#r-payback'), rRoi = el.querySelector('#r-roi');
        var svg = el.querySelector('#svg-cef8'), diag = el.querySelector('#diag-cef8');

        function update() {
          var mf = parseFloat(sMf.value); vMf.textContent = f(mf, 0);
          var f3 = parseFloat(sF3.value); vF3.textContent = f(f3, 2);
          var capex = parseFloat(sCapex.value); vCapex.textContent = f(capex, 1);
          var cash = parseFloat(sCash.value); vCash.textContent = f(cash, 2);

          var fei = mf * f3;
          var hazard = 'Light (1-60)';
          var hazardColor = '#16a34a';
          if (fei > 60 && fei <= 96) { hazard = 'Moderate (61-96)'; hazardColor = '#ca8a04'; }
          else if (fei > 96 && fei <= 127) { hazard = 'Intermediate (97-127)'; hazardColor = '#ea580c'; }
          else if (fei > 127 && fei <= 158) { hazard = 'Heavy (128-158)'; hazardColor = '#dc2626'; }
          else if (fei > 158) { hazard = 'Severe (> 158)'; hazardColor = '#7f1d1d'; }

          var payback = cash > 0 ? (capex / cash) : 999;
          var roi = capex > 0 ? ((cash / capex) * 100) : 0;

          rFei.textContent = f(fei, 1);
          rHazard.textContent = hazard;
          rPayback.textContent = f(payback, 2) + ' yrs';
          rRoi.textContent = f(roi, 1) + ' %';

          var gaugeX = Math.min(500, Math.max(50, (fei / 200) * 500));

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="50" y="60" width="500" height="30" fill="#e2e8f0" rx="4"/>' +
                          '<rect x="50" y="60" width="' + gaugeX + '" height="30" fill="' + hazardColor + '" rx="4"/>' +
                          '<text x="50" y="50" font-size="11" fill="#16a34a">Light</text>' +
                          '<text x="200" y="50" font-size="11" fill="#ca8a04">Moderate</text>' +
                          '<text x="320" y="50" font-size="11" fill="#ea580c">Intermediate</text>' +
                          '<text x="440" y="50" font-size="11" fill="#dc2626">Heavy/Severe</text>' +
                          '<line x1="' + (50 + gaugeX) + '" y1="55" x2="' + (50 + gaugeX) + '" y2="95" stroke="#0f172a" stroke-width="3"/>' +
                          '<text x="300" y="130" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">Dow F&EI: ' + f(fei,1) + ' (' + hazard + ')</text>' +
                          '<text x="300" y="160" text-anchor="middle" font-size="12" fill="#475569">Economic Payback: ' + f(payback,2) + ' years | ROI: ' + f(roi,1) + '%</text>';
          diag.textContent = 'Risk & Economics: Fire & Explosion Index F&EI = ' + f(fei, 1) + ' (' + hazard + '). Simple payback period = ' + f(payback, 2) + ' years.';
        }
        [sMf, sF3, sCapex, sCash].forEach(function(el) { el.addEventListener('input', update); });
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
