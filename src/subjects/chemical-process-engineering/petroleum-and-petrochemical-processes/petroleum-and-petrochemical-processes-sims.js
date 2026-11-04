/* Petroleum and Petrochemical Processes Interactive Simulation Suite */
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
