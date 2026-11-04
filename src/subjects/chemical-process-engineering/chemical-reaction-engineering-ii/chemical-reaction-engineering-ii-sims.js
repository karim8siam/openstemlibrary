/* Chemical Reaction Engineering II Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Langmuir-Hinshelwood Heterogeneous Surface Catalysis</h3><p class="lead">Model catalytic surface adsorption, site saturation, and apparent reaction order transitions.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Reactant Pressure PA <span><output id="v-pa">1.50</output> bar</span></label><input type="range" id="s-pa" min="0.05" max="10.0" step="0.05" value="1.50"></div>' +
              '<div class="control-group"><label>Adsorption Constant KA <span><output id="v-ka">1.20</output> bar⁻¹</span></label><input type="range" id="s-ka" min="0.10" max="5.00" step="0.10" value="1.20"></div>' +
              '<div class="control-group"><label>Surface Rate Constant kr <span><output id="v-kr">4.50</output> mol/g·h</span></label><input type="range" id="s-kr" min="0.50" max="10.0" step="0.25" value="4.50"></div>' +
              '<div class="control-group"><label>Inhibitor Pressure PB <span><output id="v-pb">0.20</output> bar</span></label><input type="range" id="s-pb" min="0.00" max="3.00" step="0.10" value="0.20"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Surface Coverage θA</span><span class="value" id="r-theta">0.00</span><span class="subtext">fraction of active sites</span></div>' +
              '<div class="readout-card"><span class="label">Reaction Rate rA</span><span class="value" id="r-rate">0.00</span><span class="subtext">mol / (g-cat · h)</span></div>' +
              '<div class="readout-card"><span class="label">Apparent Order</span><span class="value" id="r-order">0.00</span><span class="subtext">d ln(r) / d ln(PA)</span></div>' +
              '<div class="readout-card"><span class="label">Site Saturation</span><span class="value" id="r-sat">0.0%</span><span class="subtext">monolayer fullness</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-cre2-u1" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-cre2-u1"></div>',
      init: function(card) {
        var sPA = card.querySelector('#s-pa'), vPA = card.querySelector('#v-pa');
        var sKA = card.querySelector('#s-ka'), vKA = card.querySelector('#v-ka');
        var sKr = card.querySelector('#s-kr'), vKr = card.querySelector('#v-kr');
        var sPB = card.querySelector('#s-pb'), vPB = card.querySelector('#v-pb');
        var rTheta = card.querySelector('#r-theta'), rRate = card.querySelector('#r-rate');
        var rOrder = card.querySelector('#r-order'), rSat = card.querySelector('#r-sat');
        var svg = card.querySelector('#plot-cre2-u1'), diag = card.querySelector('#diag-cre2-u1');

        function update() {
          var PA = parseFloat(sPA.value); vPA.textContent = f(PA, 2);
          var KA = parseFloat(sKA.value); vKA.textContent = f(KA, 2);
          var kr = parseFloat(sKr.value); vKr.textContent = f(kr, 2);
          var PB = parseFloat(sPB.value); vPB.textContent = f(PB, 2);
          var KB = 0.8; // competitive adsorption constant

          var denom = 1 + KA * PA + KB * PB;
          var thetaA = (KA * PA) / denom;
          var rA = kr * thetaA;
          var appOrder = 1 / denom; // apparent order transitions from 1 at low PA to 0 at high PA
          var totalCov = (KA * PA + KB * PB) / denom;

          rTheta.textContent = f(thetaA, 3);
          rRate.textContent = f(rA, 2) + ' mol/g·h';
          rOrder.textContent = f(appOrder, 2);
          rSat.textContent = f(totalCov * 100, 1) + ' %';

          // SVG curve of rA vs P
          var dPath = 'M 40 170 ';
          for (var p = 0.05; p <= 10.0; p += 0.2) {
            var den_i = 1 + KA * p + KB * PB;
            var r_i = kr * (KA * p) / den_i;
            var x_px = 40 + (p / 10.0) * 520;
            var y_px = 170 - (r_i / (kr + 0.01)) * 140;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          var cur_x = 40 + (PA / 10.0) * 520;
          var cur_y = 170 - (rA / (kr + 0.01)) * 140;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<circle cx="' + cur_x.toFixed(1) + '" cy="' + cur_y.toFixed(1) + '" r="6" fill="#ef4444" stroke="#fff" stroke-width="2"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Partial Pressure PA (bar)</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Reaction Rate rA</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Langmuir-Hinshelwood Isotherm: Apparent Order ' + f(appOrder, 2) + '</text>';
          diag.textContent = 'At PA = ' + f(PA, 2) + ' bar, active surface site coverage is ' + f(thetaA * 100, 1) + '%. Apparent reaction order is ' + f(appOrder, 2) + ' (' + (appOrder > 0.7 ? 'first-order limited by adsorption' : (appOrder < 0.3 ? 'zero-order site saturation' : 'intermediate mixed regime')) + ').';
        }
        [sPA, sKA, sKr, sPB].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Catalyst Deactivation & Coking Dynamics</h3><p class="lead">Simulate catalyst activity decay, sintering, and residual operating life.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Operating Days t <span><output id="v-day">60</output> d</span></label><input type="range" id="s-day" min="0" max="300" step="5" value="60"></div>' +
              '<div class="control-group"><label>Deactivation Const kd <span><output id="v-kd">0.012</output> d⁻¹</span></label><input type="range" id="s-kd" min="0.002" max="0.050" step="0.002" value="0.012"></div>' +
              '<div class="control-group"><label>Deactivation Order <span><output id="v-dord">1st Order</output></span></label><input type="range" id="s-dord" min="1" max="2" step="1" value="1"></div>' +
              '<div class="control-group"><label>Fresh Activity a0 <span><output id="v-a0">1.00</output></span></label><input type="range" id="s-a0" min="0.80" max="1.00" step="0.05" value="1.00"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Current Activity a(t)</span><span class="value" id="r-act">1.00</span><span class="subtext">fraction of pristine state</span></div>' +
              '<div class="readout-card"><span class="label">Residual Rate rA</span><span class="value" id="r-rrate">100%</span><span class="subtext">relative to fresh catalyst</span></div>' +
              '<div class="readout-card"><span class="label">Catalyst Half-Life</span><span class="value" id="r-halflife">0 d</span><span class="subtext">time to 50% activity</span></div>' +
              '<div class="readout-card"><span class="label">Lost Productivity</span><span class="value" id="r-prodloss">0%</span><span class="subtext">cumulative yield deficit</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-cre2-u2" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-cre2-u2"></div>',
      init: function(card) {
        var sDay = card.querySelector('#s-day'), vDay = card.querySelector('#v-day');
        var sKd = card.querySelector('#s-kd'), vKd = card.querySelector('#v-kd');
        var sDord = card.querySelector('#s-dord'), vDord = card.querySelector('#v-dord');
        var sA0 = card.querySelector('#s-a0'), vA0 = card.querySelector('#v-a0');
        var rAct = card.querySelector('#r-act'), rRrate = card.querySelector('#r-rrate');
        var rHalf = card.querySelector('#r-halflife'), rProd = card.querySelector('#r-prodloss');
        var svg = card.querySelector('#plot-cre2-u2'), diag = card.querySelector('#diag-cre2-u2');

        function update() {
          var t = parseFloat(sDay.value); vDay.textContent = f(t, 0);
          var kd = parseFloat(sKd.value); vKd.textContent = f(kd, 3);
          var dord = parseInt(sDord.value, 10); vDord.textContent = dord === 1 ? '1st Order' : '2nd Order';
          var a0 = parseFloat(sA0.value); vA0.textContent = f(a0, 2);

          var act = dord === 1 ? a0 * Math.exp(-kd * t) : a0 / (1 + kd * t * a0);
          var halfLife = dord === 1 ? Math.log(2) / kd : 1 / (kd * a0);
          var loss = (1 - act / a0) * 100;

          rAct.textContent = f(act, 3);
          rRrate.textContent = f(act * 100, 1) + ' %';
          rHalf.textContent = f(halfLife, 0) + ' d';
          rProd.textContent = f(loss, 1) + ' %';

          var dPath = 'M 40 ' + (170 - a0 * 130).toFixed(1) + ' ';
          for (var d = 0; d <= 300; d += 10) {
            var a_i = dord === 1 ? a0 * Math.exp(-kd * d) : a0 / (1 + kd * d * a0);
            var x_px = 40 + (d / 300.0) * 520;
            var y_px = 170 - (a_i / 1.0) * 130;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          var cur_x = 40 + (t / 300.0) * 520;
          var cur_y = 170 - (act / 1.0) * 130;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="' + (170 - 0.5 * 130) + '" x2="560" y2="' + (170 - 0.5 * 130) + '" stroke="#cbd5e1" stroke-dasharray="4"/>' +
                          '<text x="560" y="' + (165 - 0.5 * 130) + '" text-anchor="end" font-size="10" fill="#94a3b8">50% Half-Life Threshold</text>' +
                          '<path d="' + dPath + '" fill="none" stroke="#d97706" stroke-width="3"/>' +
                          '<circle cx="' + cur_x.toFixed(1) + '" cy="' + cur_y.toFixed(1) + '" r="6" fill="#b45309" stroke="#fff" stroke-width="2"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">On-Stream Time (Days)</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Activity a(t)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Catalyst Deactivation Curve (Half-Life: ' + f(halfLife, 0) + ' days)</text>';
          diag.textContent = 'At ' + f(t, 0) + ' days of operation, catalyst activity is ' + f(act * 100, 1) + '%. Estimated half-life is ' + f(halfLife, 0) + ' days before regeneration or replacement is required.';
        }
        [sDay, sKd, sDord, sA0].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Intraparticle Diffusion & Thiele Modulus</h3><p class="lead">Simulate internal pore diffusion resistance and catalyst effectiveness factor η.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Pellet Radius Rp <span><output id="v-rp">2.0</output> mm</span></label><input type="range" id="s-rp" min="0.5" max="6.0" step="0.5" value="2.0"></div>' +
              '<div class="control-group"><label>Effective Diffusivity De <span><output id="v-de">4.0</output> × 10⁻⁷ m²/s</span></label><input type="range" id="s-de" min="1.0" max="10.0" step="0.5" value="4.0"></div>' +
              '<div class="control-group"><label>Intrinsic Rate Const kv <span><output id="v-kv">2.50</output> s⁻¹</span></label><input type="range" id="s-kv" min="0.20" max="8.00" step="0.20" value="2.50"></div>' +
              '<div class="control-group"><label>Pellet Shape <span><output id="v-shape">Sphere</output></span></label><input type="range" id="s-shape" min="1" max="2" step="1" value="1"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Thiele Modulus Φ</span><span class="value" id="r-thiele">0.00</span><span class="subtext">reaction / diffusion ratio</span></div>' +
              '<div class="readout-card"><span class="label">Effectiveness Factor η</span><span class="value" id="r-eta">0.00</span><span class="subtext">actual rate / surface rate</span></div>' +
              '<div class="readout-card"><span class="label">Controlling Regime</span><span class="value" id="r-regime">-</span><span class="subtext">kinetic limitation</span></div>' +
              '<div class="readout-card"><span class="label">Weisz-Prater Criterion</span><span class="value" id="r-weisz">0.00</span><span class="subtext">η · Φ² observable</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-cre2-u3" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-cre2-u3"></div>',
      init: function(card) {
        var sRp = card.querySelector('#s-rp'), vRp = card.querySelector('#v-rp');
        var sDe = card.querySelector('#s-de'), vDe = card.querySelector('#v-de');
        var sKv = card.querySelector('#s-kv'), vKv = card.querySelector('#v-kv');
        var sShape = card.querySelector('#s-shape'), vShape = card.querySelector('#v-shape');
        var rThiele = card.querySelector('#r-thiele'), rEta = card.querySelector('#r-eta');
        var rRegime = card.querySelector('#r-regime'), rWeisz = card.querySelector('#r-weisz');
        var svg = card.querySelector('#plot-cre2-u3'), diag = card.querySelector('#diag-cre2-u3');

        function update() {
          var Rp = parseFloat(sRp.value) * 1e-3; vRp.textContent = f(Rp * 1e3, 1);
          var De = parseFloat(sDe.value) * 1e-7; vDe.textContent = f(De * 1e7, 1);
          var kv = parseFloat(sKv.value); vKv.textContent = f(kv, 2);
          var isSphere = parseInt(sShape.value, 10) === 1; vShape.textContent = isSphere ? 'Sphere' : 'Flat Slab';

          var phi = Rp * Math.sqrt(kv / De);
          var eta;
          if (isSphere) {
            eta = phi > 0.01 ? (3 / phi) * (1 / Math.tanh(phi) - 1 / phi) : 1.0;
          } else {
            eta = phi > 0.01 ? Math.tanh(phi) / phi : 1.0;
          }
          eta = Math.min(1.0, Math.max(0.01, eta));
          var weisz = eta * phi * phi;
          var regime = phi < 0.5 ? 'Reaction Limited (η ≈ 1)' : (phi > 3.0 ? 'Strong Pore Diffusion' : 'Transition Zone');

          rThiele.textContent = f(phi, 2);
          rEta.textContent = f(eta, 3);
          rRegime.textContent = regime;
          rWeisz.textContent = f(weisz, 2);

          // SVG radial concentration profile C(r)/Cs
          var dPath = 'M 40 ';
          var cCenter = isSphere ? (phi > 0.05 ? phi / Math.sinh(phi) : 1.0) : (phi > 0.05 ? 1 / Math.cosh(phi) : 1.0);
          dPath += (170 - cCenter * 130).toFixed(1) + ' ';
          for (var r_rel = 0.02; r_rel <= 1.0; r_rel += 0.04) {
            var c_r;
            if (isSphere) {
              c_r = phi > 0.05 ? Math.sinh(phi * r_rel) / (r_rel * Math.sinh(phi)) : 1.0;
            } else {
              c_r = phi > 0.05 ? Math.cosh(phi * r_rel) / Math.cosh(phi) : 1.0;
            }
            c_r = Math.min(1.0, Math.max(0, c_r));
            var x_px = 40 + r_rel * 520;
            var y_px = 170 - c_r * 130;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#059669" stroke-width="3"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Normalized Radial Position (r / Rp)</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Concentration C(r) / Cs</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Intraparticle Concentration Profile (η = ' + f(eta, 2) + ', Φ = ' + f(phi, 2) + ')</text>';
          diag.textContent = 'Thiele modulus is ' + f(phi, 2) + ' with internal effectiveness factor η = ' + f(eta, 3) + '. ' + (phi > 3 ? 'Pellet interior is starved of reactant; reducing pellet radius will substantially improve utilization.' : 'Pellet is nearly fully utilized throughout its internal volume.');
        }
        [sRp, sDe, sKv, sShape].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Packed-Bed Catalytic Reactor (Ergun Pressure Drop)</h3><p class="lead">Simulate pressure loss and fluid flow resistance through packed catalyst beds.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Superficial Velocity u <span><output id="v-u">1.20</output> m/s</span></label><input type="range" id="s-u" min="0.20" max="3.50" step="0.10" value="1.20"></div>' +
              '<div class="control-group"><label>Pellet Diameter dp <span><output id="v-dp">3.0</output> mm</span></label><input type="range" id="s-dp" min="1.0" max="8.0" step="0.5" value="3.0"></div>' +
              '<div class="control-group"><label>Bed Voidage ε <span><output id="v-eps">0.40</output></span></label><input type="range" id="s-eps" min="0.32" max="0.48" step="0.01" value="0.40"></div>' +
              '<div class="control-group"><label>Bed Length L <span><output id="v-L">4.0</output> m</span></label><input type="range" id="s-L" min="1.0" max="10.0" step="0.5" value="4.0"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Total ΔP</span><span class="value" id="r-deltap">0 kPa</span><span class="subtext">Ergun pressure loss</span></div>' +
              '<div class="readout-card"><span class="label">Gradient (ΔP / L)</span><span class="value" id="r-grad">0 kPa/m</span><span class="subtext">head loss per meter</span></div>' +
              '<div class="readout-card"><span class="label">Viscous Fraction</span><span class="value" id="r-visc">0%</span><span class="subtext">laminar term (150)</span></div>' +
              '<div class="readout-card"><span class="label">Inertial Fraction</span><span class="value" id="r-inert">0%</span><span class="subtext">turbulent term (1.75)</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-cre2-u4" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-cre2-u4"></div>',
      init: function(card) {
        var sU = card.querySelector('#s-u'), vU = card.querySelector('#v-u');
        var sDp = card.querySelector('#s-dp'), vDp = card.querySelector('#v-dp');
        var sEps = card.querySelector('#s-eps'), vEps = card.querySelector('#v-eps');
        var sL = card.querySelector('#s-L'), vL = card.querySelector('#v-L');
        var rDelta = card.querySelector('#r-deltap'), rGrad = card.querySelector('#r-grad');
        var rVisc = card.querySelector('#r-visc'), rInert = card.querySelector('#r-inert');
        var svg = card.querySelector('#plot-cre2-u4'), diag = card.querySelector('#diag-cre2-u4');

        function update() {
          var u = parseFloat(sU.value); vU.textContent = f(u, 2);
          var dp = parseFloat(sDp.value) * 1e-3; vDp.textContent = f(dp * 1e3, 1);
          var eps = parseFloat(sEps.value); vEps.textContent = f(eps, 2);
          var L = parseFloat(sL.value); vL.textContent = f(L, 1);

          var mu = 2.0e-5; // Pa s (gas viscosity)
          var rho = 1.2;    // kg/m3 (gas density)

          var term1 = 150 * (Math.pow(1 - eps, 2) / Math.pow(eps, 3)) * (mu * u / (dp * dp));
          var term2 = 1.75 * ((1 - eps) / Math.pow(eps, 3)) * (rho * u * u / dp);
          var dP_dL = term1 + term2; // Pa/m
          var total_dP = (dP_dL * L) / 1000; // kPa

          var viscPct = (term1 / dP_dL) * 100;
          var inertPct = (term2 / dP_dL) * 100;

          rDelta.textContent = f(total_dP, 1) + ' kPa';
          rGrad.textContent = f(dP_dL / 1000, 2) + ' kPa/m';
          rVisc.textContent = f(viscPct, 1) + ' %';
          rInert.textContent = f(inertPct, 1) + ' %';

          // SVG packed bed column showing pressure drop along length
          var pIn = 500; // kPa
          var pOut = Math.max(0, pIn - total_dP);

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="50" width="440" height="70" fill="#e2e8f0" stroke="#475569" stroke-width="2" rx="4"/>' +
                          '<text x="60" y="90" text-anchor="end" font-size="12" font-weight="700" fill="#1e293b">Inlet: 500 kPa</text>' +
                          '<text x="540" y="90" text-anchor="start" font-size="12" font-weight="700" fill="#dc2626">Exit: ' + f(pOut, 0) + ' kPa</text>' +
                          '<rect x="80" y="140" width="' + (viscPct * 4.4).toFixed(1) + '" height="20" fill="#3b82f6" rx="2"/>' +
                          '<rect x="' + (80 + viscPct * 4.4).toFixed(1) + '" y="140" width="' + (inertPct * 4.4).toFixed(1) + '" height="20" fill="#f59e0b" rx="2"/>' +
                          '<text x="80" y="175" font-size="11" fill="#1e40af">Viscous (Laminar): ' + f(viscPct, 0) + '%</text>' +
                          '<text x="520" y="175" text-anchor="end" font-size="11" fill="#b45309">Inertial (Turbulent): ' + f(inertPct, 0) + '%</text>' +
                          '<text x="300" y="30" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Ergun Pressure Loss: ΔP = ' + f(total_dP, 1) + ' kPa (L = ' + f(L, 1) + ' m)</text>';
          diag.textContent = 'At superficial velocity ' + f(u, 2) + ' m/s and pellet diameter ' + f(dp * 1e3, 1) + ' mm, total bed pressure loss is ' + f(total_dP, 1) + ' kPa (' + f(dP_dL / 1000, 2) + ' kPa/m). Inertial turbulent dissipation accounts for ' + f(inertPct, 1) + '% of the loss.';
        }
        [sU, sDp, sEps, sL].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Thermal Stability & Multiple Steady States in Catalytic CSTR</h3><p class="lead">Simulate heat generation Qg(T) vs heat removal Qr(T) and identify van Heerden ignition points.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Feed Temp T0 <span><output id="v-t0">320</output> K</span></label><input type="range" id="s-t0" min="290" max="380" step="5" value="320"></div>' +
              '<div class="control-group"><label>Cooling Temp Tc <span><output id="v-tc">300</output> K</span></label><input type="range" id="s-tc" min="280" max="340" step="5" value="300"></div>' +
              '<div class="control-group"><label>Heat Exchanger UA <span><output id="v-ua">8.0</output> kW/K</span></label><input type="range" id="s-ua" min="2.0" max="20.0" step="1.0" value="8.0"></div>' +
              '<div class="control-group"><label>Heat of Reaction -ΔHr <span><output id="v-dhr">80.0</output> kJ/mol</span></label><input type="range" id="s-dhr" min="40.0" max="140.0" step="5.0" value="80.0"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Steady States</span><span class="value" id="r-sscount">1 Point</span><span class="subtext">stable / unstable intersections</span></div>' +
              '<div class="readout-card"><span class="label">Operating T</span><span class="value" id="r-opT">345 K</span><span class="subtext">reactor core temperature</span></div>' +
              '<div class="readout-card"><span class="label">Thermal Regime</span><span class="value" id="r-threg">Sub-Ignition</span><span class="subtext">safety margin</span></div>' +
              '<div class="readout-card"><span class="label">Heat Released Qg</span><span class="value" id="r-qg">0 kW</span><span class="subtext">reaction exotherm</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-cre2-u5" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-cre2-u5"></div>',
      init: function(card) {
        var sT0 = card.querySelector('#s-t0'), vT0 = card.querySelector('#v-t0');
        var sTc = card.querySelector('#s-tc'), vTc = card.querySelector('#v-tc');
        var sUA = card.querySelector('#s-ua'), vUA = card.querySelector('#v-ua');
        var sDhr = card.querySelector('#s-dhr'), vDhr = card.querySelector('#v-dhr');
        var rCount = card.querySelector('#r-sscount'), rOpT = card.querySelector('#r-opT');
        var rReg = card.querySelector('#r-threg'), rQg = card.querySelector('#r-qg');
        var svg = card.querySelector('#plot-cre2-u5'), diag = card.querySelector('#diag-cre2-u5');

        function update() {
          var T0 = parseFloat(sT0.value); vT0.textContent = f(T0, 0);
          var Tc = parseFloat(sTc.value); vTc.textContent = f(Tc, 0);
          var UA = parseFloat(sUA.value); vUA.textContent = f(UA, 1);
          var dHr = parseFloat(sDhr.value); vDhr.textContent = f(dHr, 1);

          var mCp = 15.0; // kW/K (sensible heat capacity flow)
          var tau = 10.0; // s
          var A = 1.0e8; var Ea = 65000; var R = 8.314;

          // Qg(T) and Qr(T)
          var pathQg = 'M 40 ';
          var pathQr = 'M 40 ';
          var intersections = [];

          for (var t_k = 280; t_k <= 500; t_k += 5) {
            var k_i = A * Math.exp(-Ea / (R * t_k));
            var X_i = (k_i * tau) / (1 + k_i * tau);
            var qg_i = dHr * 2.0 * X_i * 2.5; // kW
            var qr_i = mCp * (t_k - T0) + UA * (t_k - Tc);

            var x_px = 40 + ((t_k - 280) / 220) * 520;
            var y_g = 170 - (qg_i / 600.0) * 140;
            var y_r = 170 - (Math.max(0, qr_i) / 600.0) * 140;
            y_g = Math.min(170, Math.max(20, y_g));
            y_r = Math.min(170, Math.max(20, y_r));

            if (t_k === 280) {
              pathQg += y_g.toFixed(1) + ' ';
              pathQr += y_r.toFixed(1) + ' ';
            } else {
              pathQg += 'L ' + x_px.toFixed(1) + ' ' + y_g.toFixed(1) + ' ';
              pathQr += 'L ' + x_px.toFixed(1) + ' ' + y_r.toFixed(1) + ' ';
            }
            if (Math.abs(qg_i - qr_i) < 15 && t_k > 290) {
              intersections.push({ T: t_k, Q: qg_i });
            }
          }

          var numSS = intersections.length >= 3 ? 3 : (intersections.length > 0 ? 1 : 1);
          var activeT = intersections.length > 0 ? intersections[intersections.length - 1].T : T0 + 20;
          var activeQ = intersections.length > 0 ? intersections[intersections.length - 1].Q : 50;

          rCount.textContent = numSS === 3 ? '3 (Hysteresis)' : '1 Steady State';
          rOpT.textContent = f(activeT, 0) + ' K';
          rReg.textContent = activeT > 420 ? 'Ignited (High T)' : (numSS === 3 ? 'Multiple SS Risk' : 'Extinguished / Cool');
          rQg.textContent = f(activeQ, 0) + ' kW';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + pathQg + '" fill="none" stroke="#dc2626" stroke-width="3"/>' +
                          '<path d="' + pathQr + '" fill="none" stroke="#2563eb" stroke-width="2"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Temperature T (K)</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Heat Rate (kW)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">van Heerden Stability Diagram (Red: Qg, Blue: Qr)</text>';
          diag.textContent = 'Thermal analysis: ' + (numSS === 3 ? 'System exhibits 3 steady states (lower stable, middle unstable, upper ignited). Thermal runaway is possible if feed temperature surges.' : 'Single steady state operating at T = ' + f(activeT, 0) + ' K without hysteresis risk.');
        }
        [sT0, sTc, sUA, sDhr].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Fluidized-Bed Bubbling Reactor (Two-Phase Model)</h3><p class="lead">Simulate gas-solid bubbling fluidization, bubble rise velocity, and interphase exchange.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Gas Velocity u0 <span><output id="v-u0">0.35</output> m/s</span></label><input type="range" id="s-u0" min="0.05" max="1.00" step="0.05" value="0.35"></div>' +
              '<div class="control-group"><label>Min Fluidization umf <span><output id="v-umf">0.03</output> m/s</span></label><input type="range" id="s-umf" min="0.01" max="0.08" step="0.01" value="0.03"></div>' +
              '<div class="control-group"><label>Bubble Diameter db <span><output id="v-db">5.0</output> cm</span></label><input type="range" id="s-db" min="1.0" max="12.0" step="0.5" value="5.0"></div>' +
              '<div class="control-group"><label>Settled Height H0 <span><output id="v-h0">1.50</output> m</span></label><input type="range" id="s-h0" min="0.50" max="3.00" step="0.10" value="1.50"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Bubble Velocity ub</span><span class="value" id="r-ub">0.00 m/s</span><span class="subtext">absolute rise velocity</span></div>' +
              '<div class="readout-card"><span class="label">Bed Void Fraction δ</span><span class="value" id="r-delta">0.0%</span><span class="subtext">bubble gas holdup</span></div>' +
              '<div class="readout-card"><span class="label">Expanded Height Hf</span><span class="value" id="r-hf">0.00 m</span><span class="subtext">fluidized bed level</span></div>' +
              '<div class="readout-card"><span class="label">Interphase Kbe</span><span class="value" id="r-kbe">0.00 s⁻¹</span><span class="subtext">mass transfer rate</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-cre2-u6" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-cre2-u6"></div>',
      init: function(card) {
        var sU0 = card.querySelector('#s-u0'), vU0 = card.querySelector('#v-u0');
        var sUmf = card.querySelector('#s-umf'), vUmf = card.querySelector('#v-umf');
        var sDb = card.querySelector('#s-db'), vDb = card.querySelector('#v-db');
        var sH0 = card.querySelector('#s-h0'), vH0 = card.querySelector('#v-h0');
        var rUb = card.querySelector('#r-ub'), rDelta = card.querySelector('#r-delta');
        var rHf = card.querySelector('#r-hf'), rKbe = card.querySelector('#r-kbe');
        var svg = card.querySelector('#plot-cre2-u6'), diag = card.querySelector('#diag-cre2-u6');

        function update() {
          var u0 = parseFloat(sU0.value); vU0.textContent = f(u0, 2);
          var umf = parseFloat(sUmf.value); vUmf.textContent = f(umf, 2);
          var db = parseFloat(sDb.value) * 1e-2; vDb.textContent = f(db * 1e2, 1);
          var H0 = parseFloat(sH0.value); vH0.textContent = f(H0, 2);

          var g = 9.81;
          var u_br = 0.711 * Math.sqrt(g * db);
          var ub = (u0 - umf) + u_br;
          var delta = Math.max(0, Math.min(0.65, (u0 - umf) / ub));
          var Hf = H0 / (1 - delta);
          var Kbe = (4.5 * (umf / db) + 5.85 * Math.pow(1.0e-5, 0.5) * Math.pow(g, 0.25) / Math.pow(db, 1.25));

          rUb.textContent = f(ub, 2) + ' m/s';
          rDelta.textContent = f(delta * 100, 1) + ' %';
          rHf.textContent = f(Hf, 2) + ' m';
          rKbe.textContent = f(Kbe, 2) + ' s⁻¹';

          var expPx = Math.min(100, delta * 150);

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="220" y="40" width="160" height="130" fill="#f1f5f9" stroke="#334155" stroke-width="2" rx="4"/>' +
                          '<rect x="220" y="' + (170 - 70 - expPx).toFixed(1) + '" width="160" height="' + (70 + expPx).toFixed(1) + '" fill="#fed7aa" opacity="0.8"/>' +
                          '<circle cx="260" cy="110" r="12" fill="#fff" stroke="#f97316" stroke-width="2"/>' +
                          '<circle cx="330" cy="90" r="16" fill="#fff" stroke="#f97316" stroke-width="2"/>' +
                          '<circle cx="285" cy="65" r="14" fill="#fff" stroke="#f97316" stroke-width="2"/>' +
                          '<text x="210" y="' + (170 - 70 - expPx).toFixed(1) + '" text-anchor="end" font-size="11" font-weight="700" fill="#ea580c">Hf = ' + f(Hf, 2) + ' m</text>' +
                          '<text x="210" y="100" text-anchor="end" font-size="10" fill="#64748b">H0 = ' + f(H0, 2) + ' m</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Kunii-Levenspiel Bubbling Bed Model (δ = ' + f(delta*100, 1) + '%)</text>';
          diag.textContent = 'Operating at ' + f(u0 / umf, 1) + '× minimum fluidization velocity. Bubble volume fraction is ' + f(delta * 100, 1) + '%, expanding bed height from ' + f(H0, 2) + ' m to ' + f(Hf, 2) + ' m. Interphase exchange coefficient Kbe is ' + f(Kbe, 2) + ' s⁻¹.';
        }
        [sU0, sUmf, sDb, sH0].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Fluid-Solid Reactions (Shrinking Core Model)</h3><p class="lead">Simulate non-catalytic particle consumption, ash diffusion, and reaction control.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Particle Radius R0 <span><output id="v-r0">0.80</output> mm</span></label><input type="range" id="s-r0" min="0.10" max="2.00" step="0.10" value="0.80"></div>' +
              '<div class="control-group"><label>Fluid Velocity u <span><output id="v-vel">0.50</output> m/s</span></label><input type="range" id="s-vel" min="0.10" max="2.00" step="0.10" value="0.50"></div>' +
              '<div class="control-group"><label>Ash Diffusivity De <span><output id="v-ashde">2.0</output> × 10⁻⁸ m²/s</span></label><input type="range" id="s-ashde" min="0.5" max="8.0" step="0.5" value="2.0"></div>' +
              '<div class="control-group"><label>Surface Rate Const ks <span><output id="v-ks">0.05</output> m/s</span></label><input type="range" id="s-ks" min="0.01" max="0.20" step="0.01" value="0.05"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Total Burn Time τ</span><span class="value" id="r-tau">0 min</span><span class="subtext">complete conversion</span></div>' +
              '<div class="readout-card"><span class="label">Film Resistance</span><span class="value" id="r-rfilm">0%</span><span class="subtext">gas boundary layer</span></div>' +
              '<div class="readout-card"><span class="label">Ash Diffusion Res</span><span class="value" id="r-rash">0%</span><span class="subtext">porous shell layer</span></div>' +
              '<div class="readout-card"><span class="label">Chemical Rxn Res</span><span class="value" id="r-rrxn">0%</span><span class="subtext">surface kinetics</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-cre2-u7" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-cre2-u7"></div>',
      init: function(card) {
        var sR0 = card.querySelector('#s-r0'), vR0 = card.querySelector('#v-r0');
        var sVel = card.querySelector('#s-vel'), vVel = card.querySelector('#v-vel');
        var sDe = card.querySelector('#s-ashde'), vDe = card.querySelector('#v-ashde');
        var sKs = card.querySelector('#s-ks'), vKs = card.querySelector('#v-ks');
        var rTau = card.querySelector('#r-tau'), rRfilm = card.querySelector('#r-rfilm');
        var rRash = card.querySelector('#r-rash'), rRrxn = card.querySelector('#r-rrxn');
        var svg = card.querySelector('#plot-cre2-u7'), diag = card.querySelector('#diag-cre2-u7');

        function update() {
          var R0 = parseFloat(sR0.value) * 1e-3; vR0.textContent = f(R0 * 1e3, 2);
          var vel = parseFloat(sVel.value); vVel.textContent = f(vel, 2);
          var De = parseFloat(sDe.value) * 1e-8; vDe.textContent = f(De * 1e8, 1);
          var ks = parseFloat(sKs.value); vKs.textContent = f(ks, 2);

          var rhoB = 20000; // mol/m3
          var CAg = 2.0;    // mol/m3
          var kg = 0.02 * Math.sqrt(vel / (R0 * 2)); // mass transfer coefficient

          var t_film = (rhoB * R0) / (3 * kg * CAg);
          var t_ash = (rhoB * R0 * R0) / (6 * De * CAg);
          var t_rxn = (rhoB * R0) / (ks * CAg);
          var t_tot = t_film + t_ash + t_rxn; // s

          var pFilm = (t_film / t_tot) * 100;
          var pAsh = (t_ash / t_tot) * 100;
          var pRxn = (t_rxn / t_tot) * 100;

          rTau.textContent = f(t_tot / 60, 1) + ' min';
          rRfilm.textContent = f(pFilm, 1) + ' %';
          rRash.textContent = f(pAsh, 1) + ' %';
          rRrxn.textContent = f(pRxn, 1) + ' %';

          // SVG showing shrinking core particle
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<circle cx="200" cy="100" r="60" fill="#e2e8f0" stroke="#64748b" stroke-width="2"/>' +
                          '<circle cx="200" cy="100" r="35" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>' +
                          '<text x="200" y="105" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">Unreacted Core</text>' +
                          '<text x="200" y="175" text-anchor="middle" font-size="11" fill="#475569">R0 = ' + f(R0*1e3, 1) + ' mm (Ash layer outer shell)</text>' +
                          '<rect x="340" y="55" width="220" height="24" fill="#94a3b8" rx="3"/>' +
                          '<rect x="340" y="95" width="220" height="24" fill="#f59e0b" rx="3"/>' +
                          '<rect x="340" y="135" width="220" height="24" fill="#3b82f6" rx="3"/>' +
                          '<text x="350" y="72" font-size="11" font-weight="700" fill="#fff">Film Mass Transfer: ' + f(pFilm, 0) + '%</text>' +
                          '<text x="350" y="112" font-size="11" font-weight="700" fill="#fff">Ash Diffusion: ' + f(pAsh, 0) + '%</text>' +
                          '<text x="350" y="152" font-size="11" font-weight="700" fill="#fff">Surface Reaction: ' + f(pRxn, 0) + '%</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Shrinking Core Resistance Breakdown (τ = ' + f(t_tot/60, 1) + ' min)</text>';
          diag.textContent = 'Complete reaction requires ' + f(t_tot / 60, 1) + ' minutes. ' + (pAsh > 50 ? 'Ash layer diffusion is the dominant rate-controlling step (' + f(pAsh, 1) + '% of total resistance).' : (pRxn > 50 ? 'Chemical surface kinetics control the overall rate.' : 'Mixed film and chemical control regime.'));
        }
        [sR0, sVel, sDe, sKs].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>RTD & Tanks-in-Series Model Scale-Up</h3><p class="lead">Simulate residence time distribution E(θ), vessel dispersion, and non-ideal mixing.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Number of Tanks N <span><output id="v-tanks">4</output></span></label><input type="range" id="s-tanks" min="1" max="25" step="1" value="4"></div>' +
              '<div class="control-group"><label>Mean Res Time τ <span><output id="v-rtau">20</output> min</span></label><input type="range" id="s-rtau" min="5" max="60" step="5" value="20"></div>' +
              '<div class="control-group"><label>Tracer Mass M <span><output id="v-mass">50</output> g</span></label><input type="range" id="s-mass" min="10" max="100" step="10" value="50"></div>' +
              '<div class="control-group"><label>Comparison Mode <span><output id="v-mode">Tanks-in-Series</output></span></label><input type="range" id="s-mode" min="1" max="2" step="1" value="1"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Dimensionless Var σ²</span><span class="value" id="r-var">0.25</span><span class="subtext">variance = 1 / N</span></div>' +
              '<div class="readout-card"><span class="label">Dispersion No. (D/uL)</span><span class="value" id="r-disp">0.125</span><span class="subtext">equivalent axial mixing</span></div>' +
              '<div class="readout-card"><span class="label">Peak Height Emax</span><span class="value" id="r-emax">1.00</span><span class="subtext">normalized concentration</span></div>' +
              '<div class="readout-card"><span class="label">Flow Character</span><span class="value" id="r-flowchar">Moderate Mixing</span><span class="subtext">plug flow approach</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-cre2-u8" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-cre2-u8"></div>',
      init: function(card) {
        var sTanks = card.querySelector('#s-tanks'), vTanks = card.querySelector('#v-tanks');
        var sRtau = card.querySelector('#s-rtau'), vRtau = card.querySelector('#v-rtau');
        var sMass = card.querySelector('#s-mass'), vMass = card.querySelector('#v-mass');
        var sMode = card.querySelector('#s-mode'), vMode = card.querySelector('#v-mode');
        var rVar = card.querySelector('#r-var'), rDisp = card.querySelector('#r-disp');
        var rEmax = card.querySelector('#r-emax'), rFlow = card.querySelector('#r-flowchar');
        var svg = card.querySelector('#plot-cre2-u8'), diag = card.querySelector('#diag-cre2-u8');

        function factorial(n) {
          var res = 1; for (var i = 2; i <= n; i++) res *= i; return res;
        }

        function update() {
          var N = parseInt(sTanks.value, 10); vTanks.textContent = N;
          var tau = parseFloat(sRtau.value); vRtau.textContent = f(tau, 0);
          var M = parseFloat(sMass.value); vMass.textContent = f(M, 0);
          var isSeries = parseInt(sMode.value, 10) === 1; vMode.textContent = isSeries ? 'Tanks-in-Series' : 'Dispersion Equiv';

          var variance = 1 / N;
          var D_uL = 1 / (2 * N);
          var charFlow = N === 1 ? 'Perfect Mixed Flow (CSTR)' : (N > 15 ? 'Near Ideal Plug Flow (PFR)' : 'Dispersed Flow');

          rVar.textContent = f(variance, 3);
          rDisp.textContent = f(D_uL, 3);
          rFlow.textContent = charFlow;

          // RTD curve E(theta)
          var dPath = 'M 40 170 ';
          var maxE = 0;
          for (var th = 0.05; th <= 3.0; th += 0.05) {
            // E(theta) = (N^N / (N-1)!) * theta^(N-1) * exp(-N * theta)
            var logE = N * Math.log(N) - (N > 1 ? (N - 1) * Math.log(th) : 0);
            var E_val = (Math.pow(N, N) / (factorial(Math.min(12, N - 1)))) * Math.pow(th, N - 1) * Math.exp(-N * th);
            if (E_val > maxE) maxE = E_val;
            var x_px = 40 + (th / 3.0) * 520;
            var y_px = 170 - (Math.min(3.0, E_val) / 3.0) * 140;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          rEmax.textContent = f(maxE, 2);

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#7c3aed" stroke-width="3"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Dimensionless Time θ = t / τ</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">RTD E(θ)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">RTD Curve for N = ' + N + ' CSTRs in Series (σ² = ' + f(variance, 3) + ')</text>';
          diag.textContent = 'For N = ' + N + ' equal tanks in series, RTD variance σθ² is ' + f(variance, 3) + ', corresponding to an equivalent dispersion number D/(uL) of ' + f(D_uL, 3) + '. ' + (N > 10 ? 'Approaches plug flow behavior with sharp pulse transit.' : 'Substantial backmixing and spread across the reactor train.');
        }
        [sTanks, sRtau, sMass, sMode].forEach(function(el) { el.addEventListener('input', update); });
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
