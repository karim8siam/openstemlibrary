/* Biochemical Engineering Interactive Simulation Suite */
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
