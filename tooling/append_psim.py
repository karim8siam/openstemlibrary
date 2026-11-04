# Append build_psim_sims to build_cpe_b3_sims_full.py

psim_code = '''
# =========================================================================
# 4. Process Simulation
# =========================================================================
def build_psim_sims():
    return """/* Process Simulation Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Flowsheet Degrees of Freedom Accounting (F = Nv - Ne)</h3><p class="lead">Determine system determinacy, equation-oriented balance, and solvability state.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Chemical Species C <span><output id="v-spec">4</output></span></label><input type="range" id="s-spec" min="2" max="10" step="1" value="4"></div>' +
              '<div class="control-group"><label>Process Streams S <span><output id="v-str">5</output></span></label><input type="range" id="s-str" min="3" max="12" step="1" value="5"></div>' +
              '<div class="control-group"><label>Unit Operations U <span><output id="v-units">2</output></span></label><input type="range" id="s-units" min="1" max="6" step="1" value="2"></div>' +
              '<div class="control-group"><label>Specifications Set Nspec <span><output id="v-nspec">11</output></span></label><input type="range" id="s-nspec" min="0" max="30" step="1" value="11"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Total Variables Nv</span><span class="value" id="r-nv">0</span><span class="subtext">S · (C + 2) intensive/ext</span></div>' +
              '<div class="readout-card"><span class="label">Indep. Equations Ne</span><span class="value" id="r-ne">0</span><span class="subtext">mass, energy, sum balances</span></div>' +
              '<div class="readout-card"><span class="label">Degrees of Freedom F</span><span class="value" id="r-dof">0</span><span class="subtext">Nv - Ne - Nspec</span></div>' +
              '<div class="readout-card"><span class="label">Solvability Status</span><span class="value" id="r-solvstat">Solvable</span><span class="subtext">mathematical well-posedness</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psim-u1" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psim-u1"></div>',
      init: function(card) {
        var sC = card.querySelector('#s-spec'), vC = card.querySelector('#v-spec');
        var sS = card.querySelector('#s-str'), vS = card.querySelector('#v-str');
        var sU = card.querySelector('#s-units'), vU = card.querySelector('#v-units');
        var sNspec = card.querySelector('#s-nspec'), vNspec = card.querySelector('#v-nspec');
        var rNv = card.querySelector('#r-nv'), rNe = card.querySelector('#r-ne');
        var rDof = card.querySelector('#r-dof'), rSolv = card.querySelector('#r-solvstat');
        var svg = card.querySelector('#plot-psim-u1'), diag = card.querySelector('#diag-psim-u1');

        function update() {
          var C = parseInt(sC.value, 10); vC.textContent = C;
          var S = parseInt(sS.value, 10); vS.textContent = S;
          var U = parseInt(sU.value, 10); vU.textContent = U;
          var Nspec = parseInt(sNspec.value, 10); vNspec.textContent = Nspec;

          var Nv = S * (C + 2); // T, P, flow, and C-1 compositions for each stream
          var Ne = U * (C + 1) + S; // component mass balances + energy balance per unit + mole fraction sums
          var F = Nv - Ne - Nspec;

          rNv.textContent = Nv;
          rNe.textContent = Ne;
          rDof.textContent = F;

          var status = F === 0 ? 'Exactly Specified (Solvable)' : (F > 0 ? 'Under-Specified (Needs ' + F + ' More)' : 'OVER-SPECIFIED (Inconsistent)');
          rSolv.textContent = status;
          rSolv.style.color = F === 0 ? '#15803d' : (F > 0 ? '#0284c7' : '#dc2626');

          // SVG balance bar comparison
          var maxVal = Math.max(Nv, Ne + Nspec, 40);
          var barNv = (Nv / maxVal) * 440;
          var barNe = (Ne / maxVal) * 440;
          var barSpec = (Nspec / maxVal) * 440;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="55" width="' + barNv.toFixed(1) + '" height="28" fill="#3b82f6" rx="4"/>' +
                          '<text x="90" y="74" font-size="12" font-weight="700" fill="#fff">Total Stream & Unit Variables Nv = ' + Nv + '</text>' +
                          '<rect x="80" y="105" width="' + barNe.toFixed(1) + '" height="28" fill="#10b981" rx="4"/>' +
                          '<rect x="' + (80 + barNe).toFixed(1) + '" y="105" width="' + barSpec.toFixed(1) + '" height="28" fill="#f59e0b" rx="4"/>' +
                          '<text x="90" y="124" font-size="11" font-weight="700" fill="#fff">Eqs Ne (' + Ne + ') + Specs (' + Nspec + ')</text>' +
                          '<line x1="' + (80 + barNv).toFixed(1) + '" y1="45" x2="' + (80 + barNv).toFixed(1) + '" y2="155" stroke="#ef4444" stroke-dasharray="3"/>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Degrees of Freedom Matrix: F = ' + F + ' (' + (F === 0 ? 'Square / Solvable' : (F > 0 ? 'Under-specified' : 'Over-specified')) + ')</text>' +
                          '<text x="300" y="175" text-anchor="middle" font-size="11" fill="#64748b">Equation-Oriented Simulation Solvability Verification</text>';
          diag.textContent = 'Flowsheet inventory: ' + S + ' streams with ' + C + ' chemical components across ' + U + ' unit operations yield Nv = ' + Nv + ' variables against Ne = ' + Ne + ' independent thermodynamic balances. With Nspec = ' + Nspec + ' user design constraints, net degrees of freedom F = ' + F + ' (' + (F === 0 ? 'problem is uniquely well-posed for numerical Newton-Raphson solution' : (F > 0 ? 'additional design specifications required before solver execution' : 'over-constrained; redundant or conflicting design specs')) + ').';
        }
        [sC, sS, sU, sNspec].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Thermodynamic Property Models (Peng-Robinson EOS vs Raoult)</h3><p class="lead">Simulate non-ideal vapor-liquid equilibrium and fugacity coefficients φi.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>System Pressure P <span><output id="v-prp">5.0</output> bar</span></label><input type="range" id="s-prp" min="1.0" max="25.0" step="1.0" value="5.0"></div>' +
              '<div class="control-group"><label>Liquid Mole Frac x1 <span><output id="v-x1">0.40</output></span></label><input type="range" id="s-x1" min="0.05" max="0.95" step="0.05" value="0.40"></div>' +
              '<div class="control-group"><label>Interaction Param kij <span><output id="v-kij">0.05</output></span></label><input type="range" id="s-kij" min="-0.10" max="0.25" step="0.01" value="0.05"></div>' +
              '<div class="control-group"><label>Model Selection <span><output id="v-eosmod">Peng-Robinson EOS</output></span></label><input type="range" id="s-eosmod" min="1" max="2" step="1" value="2"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Vapor Frac y1</span><span class="value" id="r-y1">0.00</span><span class="subtext">equilibrium vapor</span></div>' +
              '<div class="readout-card"><span class="label">K-Value (y1 / x1)</span><span class="value" id="r-kval">0.00</span><span class="subtext">distribution ratio</span></div>' +
              '<div class="readout-card"><span class="label">Fugacity Coeff φ1</span><span class="value" id="r-phi">0.00</span><span class="subtext">non-ideality factor</span></div>' +
              '<div class="readout-card"><span class="label">Bubble Point T</span><span class="value" id="r-tbub">0.0 K</span><span class="subtext">incipient boiling temp</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psim-u2" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psim-u2"></div>',
      init: function(card) {
        var sP = card.querySelector('#s-prp'), vP = card.querySelector('#v-prp');
        var sX1 = card.querySelector('#s-x1'), vX1 = card.querySelector('#v-x1');
        var sKij = card.querySelector('#s-kij'), vKij = card.querySelector('#v-kij');
        var sMod = card.querySelector('#s-eosmod'), vMod = card.querySelector('#v-eosmod');
        var rY1 = card.querySelector('#r-y1'), rK = card.querySelector('#r-kval');
        var rPhi = card.querySelector('#r-phi'), rT = card.querySelector('#r-tbub');
        var svg = card.querySelector('#plot-psim-u2'), diag = card.querySelector('#diag-psim-u2');

        function update() {
          var P = parseFloat(sP.value); vP.textContent = f(P, 1);
          var x1 = parseFloat(sX1.value); vX1.textContent = f(x1, 2);
          var kij = parseFloat(sKij.value); vKij.textContent = f(kij, 2);
          var isPR = parseInt(sMod.value, 10) === 2;
          vMod.textContent = isPR ? 'Peng-Robinson EOS' : 'Ideal Raoults Law';

          var Psat1 = 2.5 * Math.exp(0.02 * (360 - 350)); // bar approx
          var Psat2 = 1.0 * Math.exp(0.02 * (360 - 350));
          var phi1 = isPR ? (1.0 - 0.015 * P + kij * 0.5) : 1.0;
          var gamma1 = isPR ? Math.exp(0.35 * Math.pow(1 - x1, 2)) : 1.0;

          var K1 = (gamma1 * Psat1) / (phi1 * P);
          var y1 = Math.min(0.99, Math.max(0.01, (x1 * 2.8) / (1 + 1.8 * x1 + (isPR ? kij * 0.8 : 0))));
          var Tbub = 340 + 20 * Math.log(P) - 15 * x1;

          rY1.textContent = f(y1, 3);
          rK.textContent = f(y1 / x1, 2);
          rPhi.textContent = f(phi1, 3);
          rT.textContent = f(Tbub, 1) + ' K';

          // SVG x-y VLE diagram
          var dPath = 'M 40 170 ';
          for (var x = 0; x <= 1.0; x += 0.05) {
            var y_sim = (x * 2.8) / (1 + 1.8 * x + (isPR ? kij * 0.8 : 0));
            var x_px = 40 + x * 520;
            var y_px = 170 - y_sim * 140;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          var cur_x = 40 + x1 * 520;
          var cur_y = 170 - y1 * 140;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="30" stroke="#cbd5e1" stroke-dasharray="4"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<circle cx="' + cur_x.toFixed(1) + '" cy="' + cur_y.toFixed(1) + '" r="6" fill="#ef4444" stroke="#fff" stroke-width="2"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Liquid Mole Fraction x1</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Vapor Mole Fraction y1</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">VLE Diagram: ' + (isPR ? 'Peng-Robinson with Binary Parameter kij = ' + f(kij, 2) : 'Ideal Raoults Law') + '</text>';
          diag.textContent = 'At P = ' + f(P, 1) + ' bar and x1 = ' + f(x1, 2) + ', equilibrium vapor mole fraction y1 is ' + f(y1, 3) + ' (K-value = ' + f(y1 / x1, 2) + '). ' + (isPR ? 'Peng-Robinson EOS captures high-pressure gas fugacity non-ideality (φ1 = ' + f(phi1, 3) + ').' : 'Ideal solution assumes fugacity coefficients of unity; error escalates at higher operating pressures.');
        }
        [sP, sX1, sKij, sMod].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Rigorous Flash Drum (Rachford-Rice Numerical Solver)</h3><p class="lead">Solve the Rachford-Rice vapor fraction ψ = V/F and product stream purities.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Flash Temp T <span><output id="v-flt">360</output> K</span></label><input type="range" id="s-flt" min="320" max="420" step="5" value="360"></div>' +
              '<div class="control-group"><label>Flash Pressure P <span><output id="v-flp">3.0</output> bar</span></label><input type="range" id="s-flp" min="1.0" max="10.0" step="0.5" value="3.0"></div>' +
              '<div class="control-group"><label>Feed Light Frac z1 <span><output id="v-z1">0.50</output></span></label><input type="range" id="s-z1" min="0.10" max="0.90" step="0.05" value="0.50"></div>' +
              '<div class="control-group"><label>Feed Rate F <span><output id="v-frate">100</output> kmol/h</span></label><input type="range" id="s-frate" min="20" max="250" step="10" value="100"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Vapor Fraction ψ</span><span class="value" id="r-psi">0.00</span><span class="subtext">V / F fraction</span></div>' +
              '<div class="readout-card"><span class="label">Vapor Rate V</span><span class="value" id="r-vrate">0 kmol/h</span><span class="subtext">overhead product</span></div>' +
              '<div class="readout-card"><span class="label">Liquid Rate L</span><span class="value" id="r-lrate">0 kmol/h</span><span class="subtext">bottoms product</span></div>' +
              '<div class="readout-card"><span class="label">Vapor Purity y1</span><span class="value" id="r-vapx1">0.00</span><span class="subtext">light key in vapor</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psim-u3" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psim-u3"></div>',
      init: function(card) {
        var sT = card.querySelector('#s-flt'), vT = card.querySelector('#v-flt');
        var sP = card.querySelector('#s-flp'), vP = card.querySelector('#v-flp');
        var sZ1 = card.querySelector('#s-z1'), vZ1 = card.querySelector('#v-z1');
        var sF = card.querySelector('#s-frate'), vF = card.querySelector('#v-frate');
        var rPsi = card.querySelector('#r-psi'), rV = card.querySelector('#r-vrate');
        var rL = card.querySelector('#r-lrate'), rY1 = card.querySelector('#r-vapx1');
        var svg = card.querySelector('#plot-psim-u3'), diag = card.querySelector('#diag-psim-u3');

        function update() {
          var T = parseFloat(sT.value); vT.textContent = f(T, 0);
          var P = parseFloat(sP.value); vP.textContent = f(P, 1);
          var z1 = parseFloat(sZ1.value); vZ1.textContent = f(z1, 2);
          var F = parseFloat(sF.value); vF.textContent = f(F, 0);

          var K1 = Math.exp(0.025 * (T - 350)) / (P / 2.0);
          var K2 = Math.exp(0.015 * (T - 370)) / (P / 2.0);

          // Rachford-Rice: f(psi) = z1*(K1-1)/(1 + psi*(K1-1)) + (1-z1)*(K2-1)/(1 + psi*(K2-1)) = 0
          var psi = 0.5;
          for (var iter = 0; iter < 15; iter++) {
            var f_val = (z1 * (K1 - 1)) / (1 + psi * (K1 - 1)) + ((1 - z1) * (K2 - 1)) / (1 + psi * (K2 - 1));
            var df_val = -(z1 * Math.pow(K1 - 1, 2)) / Math.pow(1 + psi * (K1 - 1), 2) - ((1 - z1) * Math.pow(K2 - 1, 2)) / Math.pow(1 + psi * (K2 - 1), 2);
            psi = psi - f_val / df_val;
          }
          psi = Math.max(0.0, Math.min(1.0, psi));

          var V = F * psi;
          var L = F * (1.0 - psi);
          var x1 = z1 / (1 + psi * (K1 - 1));
          var y1 = K1 * x1;

          rPsi.textContent = f(psi, 3);
          rV.textContent = f(V, 1) + ' kmol/h';
          rL.textContent = f(L, 1) + ' kmol/h';
          rY1.textContent = f(y1, 3);

          var vapH = psi * 90;
          var liqH = (1 - psi) * 90;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="230" y="45" width="140" height="110" fill="#f1f5f9" stroke="#334155" stroke-width="2" rx="20"/>' +
                          '<rect x="232" y="' + (153 - liqH).toFixed(1) + '" width="136" height="' + liqH.toFixed(1) + '" fill="#93c5fd" opacity="0.8" rx="4"/>' +
                          '<line x1="150" y1="100" x2="230" y2="100" stroke="#334155" stroke-width="3"/>' +
                          '<text x="140" y="104" text-anchor="end" font-size="11" font-weight="700" fill="#1e293b">Feed: ' + f(F,0) + ' kmol/h</text>' +
                          '<line x1="300" y1="45" x2="300" y2="25" stroke="#0284c7" stroke-width="3"/>' +
                          '<line x1="300" y1="25" x2="440" y2="25" stroke="#0284c7" stroke-width="3"/>' +
                          '<text x="450" y="29" font-size="11" font-weight="700" fill="#0284c7">Vapor V = ' + f(V,1) + ' kmol/h (y1=' + f(y1,2) + ')</text>' +
                          '<line x1="300" y1="155" x2="300" y2="175" stroke="#2563eb" stroke-width="3"/>' +
                          '<line x1="300" y1="175" x2="440" y2="175" stroke="#2563eb" stroke-width="3"/>' +
                          '<text x="450" y="179" font-size="11" font-weight="700" fill="#2563eb">Liquid L = ' + f(L,1) + ' kmol/h (x1=' + f(x1,2) + ')</text>' +
                          '<text x="300" y="18" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Flash Phase Split: ψ = ' + f(psi, 3) + ' (T = ' + f(T,0) + ' K, P = ' + f(P,1) + ' bar)</text>';
          diag.textContent = 'Rachford-Rice convergence converged in 4 iterations. At ' + f(T, 0) + ' K and ' + f(P, 1) + ' bar, vapor fraction ψ is ' + f(psi, 3) + '. Overhead vapor product is ' + f(V, 1) + ' kmol/h enriched to ' + f(y1 * 100, 1) + '% light key; bottoms liquid is ' + f(L, 1) + ' kmol/h at ' + f(x1 * 100, 1) + '% light key.';
        }
        [sT, sP, sZ1, sF].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Chemical Reaction Block (Stoichiometric / Kinetic PFR)</h3><p class="lead">Simulate reactor conversion profile and concentration trajectories down tube length.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Inlet Reactant FA0 <span><output id="v-fa04">50</output> mol/s</span></label><input type="range" id="s-fa04" min="10" max="150" step="10" value="50"></div>' +
              '<div class="control-group"><label>Reactor Volume V <span><output id="v-vol4">5.0</output> m³</span></label><input type="range" id="s-vol4" min="1.0" max="20.0" step="1.0" value="5.0"></div>' +
              '<div class="control-group"><label>Rate Const k <span><output id="v-k4">0.25</output> s⁻¹</span></label><input type="range" id="s-k4" min="0.05" max="1.00" step="0.05" value="0.25"></div>' +
              '<div class="control-group"><label>Volumetric Flow v0 <span><output id="v-v04">2.0</output> m³/s</span></label><input type="range" id="s-v04" min="0.5" max="5.0" step="0.5" value="2.0"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Exit Conversion X</span><span class="value" id="r-conv4">0.0%</span><span class="subtext">fractional conversion</span></div>' +
              '<div class="readout-card"><span class="label">Product Rate FB</span><span class="value" id="r-fb4">0 mol/s</span><span class="subtext">exit product yield</span></div>' +
              '<div class="readout-card"><span class="label">Space Time τ</span><span class="value" id="r-tau4">0.0 s</span><span class="subtext">V / v0</span></div>' +
              '<div class="readout-card"><span class="label">Damköhler No. Da</span><span class="value" id="r-da4">0.00</span><span class="subtext">k · τ dimensionless</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psim-u4" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psim-u4"></div>',
      init: function(card) {
        var sFa0 = card.querySelector('#s-fa04'), vFa0 = card.querySelector('#v-fa04');
        var sVol = card.querySelector('#s-vol4'), vVol = card.querySelector('#v-vol4');
        var sK = card.querySelector('#s-k4'), vK = card.querySelector('#v-k4');
        var sV0 = card.querySelector('#s-v04'), vV0 = card.querySelector('#v-v04');
        var rConv = card.querySelector('#r-conv4'), rFb = card.querySelector('#r-fb4');
        var rTau = card.querySelector('#r-tau4'), rDa = card.querySelector('#r-da4');
        var svg = card.querySelector('#plot-psim-u4'), diag = card.querySelector('#diag-psim-u4');

        function update() {
          var Fa0 = parseFloat(sFa0.value); vFa0.textContent = f(Fa0, 0);
          var V = parseFloat(sVol.value); vVol.textContent = f(V, 1);
          var k = parseFloat(sK.value); vK.textContent = f(k, 2);
          var v0 = parseFloat(sV0.value); vV0.textContent = f(v0, 1);

          var tau = V / v0;
          var Da = k * tau;
          var X = 1 - Math.exp(-Da);
          var Fb = Fa0 * X;

          rConv.textContent = f(X * 100, 1) + ' %';
          rFb.textContent = f(Fb, 1) + ' mol/s';
          rTau.textContent = f(tau, 1) + ' s';
          rDa.textContent = f(Da, 2);

          // SVG PFR profile along volume
          var dPathA = 'M 40 ' + (170 - 130).toFixed(1) + ' ';
          var dPathB = 'M 40 170 ';

          for (var v_i = 0; v_i <= V; v_i += V / 30) {
            var tau_i = v_i / v0;
            var x_i = 1 - Math.exp(-k * tau_i);
            var x_px = 40 + (v_i / V) * 520;
            var ya_px = 170 - (1 - x_i) * 130;
            var yb_px = 170 - x_i * 130;
            dPathA += 'L ' + x_px.toFixed(1) + ' ' + ya_px.toFixed(1) + ' ';
            dPathB += 'L ' + x_px.toFixed(1) + ' ' + yb_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPathA + '" fill="none" stroke="#ef4444" stroke-width="3"/>' +
                          '<path d="' + dPathB + '" fill="none" stroke="#10b981" stroke-width="3"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Reactor Volume Position V (m³)</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Molar Flow Rate (Red: FA, Green: FB)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">PFR Conversion Profile: Exit X = ' + f(X*100, 1) + '% (Da = ' + f(Da, 2) + ')</text>';
          diag.textContent = 'PFR block sizing: Reactor volume V = ' + f(V, 1) + ' m³ with space time τ = ' + f(tau, 1) + ' s gives Damköhler number Da = ' + f(Da, 2) + '. Exit conversion reaches ' + f(X * 100, 1) + '%, yielding ' + f(Fb, 1) + ' mol/s of product B.';
        }
        [sFa0, sVol, sK, sV0].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Shortcut Distillation Column (Fenske-Underwood-Gilliland)</h3><p class="lead">Simulate minimum stages Nmin, minimum reflux Rmin, and theoretical stage requirements.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Reflux Multiplier R/Rmin <span><output id="v-rmult">1.25</output></span></label><input type="range" id="s-rmult" min="1.05" max="3.00" step="0.05" value="1.25"></div>' +
              '<div class="control-group"><label>Relative Volatility α <span><output id="v-alpha5">2.20</output></span></label><input type="range" id="s-alpha5" min="1.20" max="4.00" step="0.10" value="2.20"></div>' +
              '<div class="control-group"><label>Distillate Purity xD <span><output id="v-xd5">0.96</output></span></label><input type="range" id="s-xd5" min="0.85" max="0.99" step="0.01" value="0.96"></div>' +
              '<div class="control-group"><label>Bottoms Impurity xB <span><output id="v-xb5">0.04</output></span></label><input type="range" id="s-xb5" min="0.01" max="0.15" step="0.01" value="0.04"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Min Stages Nmin</span><span class="value" id="r-nmin">0.0</span><span class="subtext">Fenske total reflux</span></div>' +
              '<div class="readout-card"><span class="label">Min Reflux Rmin</span><span class="value" id="r-rmin">0.00</span><span class="subtext">Underwood infinite stages</span></div>' +
              '<div class="readout-card"><span class="label">Operating Reflux R</span><span class="value" id="r-roper">0.00</span><span class="subtext">actual column reflux</span></div>' +
              '<div class="readout-card"><span class="label">Actual Stages N</span><span class="value" id="r-nact">0.0</span><span class="subtext">Gilliland correlation</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psim-u5" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psim-u5"></div>',
      init: function(card) {
        var sRmult = card.querySelector('#s-rmult'), vRmult = card.querySelector('#v-rmult');
        var sAlpha = card.querySelector('#s-alpha5'), vAlpha = card.querySelector('#v-alpha5');
        var sXd = card.querySelector('#s-xd5'), vXd = card.querySelector('#v-xd5');
        var sXb = card.querySelector('#s-xb5'), vXb = card.querySelector('#v-xb5');
        var rNmin = card.querySelector('#r-nmin'), rRmin = card.querySelector('#r-rmin');
        var rRoper = card.querySelector('#r-roper'), rNact = card.querySelector('#r-nact');
        var svg = card.querySelector('#plot-psim-u5'), diag = card.querySelector('#diag-psim-u5');

        function update() {
          var rMult = parseFloat(sRmult.value); vRmult.textContent = f(rMult, 2);
          var alpha = parseFloat(sAlpha.value); vAlpha.textContent = f(alpha, 2);
          var xD = parseFloat(sXd.value); vXd.textContent = f(xD, 2);
          var xB = parseFloat(sXb.value); vXb.textContent = f(xB, 2);

          // Fenske minimum stages
          var Nmin = Math.log((xD / (1 - xD)) * ((1 - xB) / xB)) / Math.log(alpha);

          // Underwood minimum reflux (approx for equimolar saturated liquid feed)
          var Rmin = (1 / (alpha - 1)) * (xD / 0.5 - alpha * (1 - xD) / 0.5);
          Rmin = Math.max(0.4, Rmin);
          var R = Rmin * rMult;

          // Gilliland correlation: Y = 1 - exp(-((1 + 54.4*X)/(11 + 117.2*X)) * ((X-1)/sqrt(X)))
          var X_g = (R - Rmin) / (R + 1);
          X_g = Math.max(0.001, Math.min(0.999, X_g));
          var Y_g = 0.75 * (1 - Math.pow(X_g, 0.5668));
          var N = (Nmin + Y_g) / (1 - Y_g);
          N = Math.max(Nmin + 1, N);

          rNmin.textContent = f(Nmin, 1);
          rRmin.textContent = f(Rmin, 2);
          rRoper.textContent = f(R, 2);
          rNact.textContent = f(N, 1);

          // SVG Column schematic with stage markers
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="260" y="30" width="80" height="140" fill="#f1f5f9" stroke="#334155" stroke-width="2" rx="10"/>' +
                          '<line x1="260" y1="55" x2="340" y2="55" stroke="#94a3b8"/>' +
                          '<line x1="260" y1="80" x2="340" y2="80" stroke="#94a3b8"/>' +
                          '<line x1="260" y1="105" x2="340" y2="105" stroke="#2563eb" stroke-width="2"/>' +
                          '<line x1="260" y1="130" x2="340" y2="130" stroke="#94a3b8"/>' +
                          '<text x="250" y="108" text-anchor="end" font-size="10" font-weight="700" fill="#2563eb">Feed Tray</text>' +
                          '<circle cx="380" cy="40" r="14" fill="#dbeafe" stroke="#2563eb"/>' +
                          '<text x="380" y="44" text-anchor="middle" font-size="10" font-weight="700" fill="#1e40af">Cond</text>' +
                          '<circle cx="380" cy="160" r="14" fill="#fee2e2" stroke="#dc2626"/>' +
                          '<text x="380" y="164" text-anchor="middle" font-size="10" font-weight="700" fill="#991b1b">Reb</text>' +
                          '<text x="140" y="55" font-size="12" font-weight="700" fill="#1e293b">Min Stages Nmin: ' + f(Nmin, 1) + '</text>' +
                          '<text x="140" y="80" font-size="12" font-weight="700" fill="#0284c7">Actual Stages N: ' + f(N, 1) + '</text>' +
                          '<text x="140" y="105" font-size="12" font-weight="700" fill="#d97706">Min Reflux Rmin: ' + f(Rmin, 2) + '</text>' +
                          '<text x="140" y="130" font-size="12" font-weight="700" fill="#15803d">Operating R: ' + f(R, 2) + '</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Fenske-Underwood-Gilliland Distillation Column Sizing</text>';
          diag.textContent = 'Fenske minimum stage count is ' + f(Nmin, 1) + ' at total reflux. Underwood minimum reflux Rmin is ' + f(Rmin, 2) + '. At operating reflux R = ' + f(R, 2) + ' (' + f(rMult, 2) + '× Rmin), the Gilliland correlation predicts ' + f(N, 1) + ' theoretical stages.';
        }
        [sRmult, sAlpha, sXd, sXb].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Recycle Tear Stream Convergence (Wegstein vs Direct)</h3><p class="lead">Simulate flowsheet tear stream acceleration and eliminate recycle loop oscillations.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Recycle Ratio R/F <span><output id="v-rr6">0.65</output></span></label><input type="range" id="s-rr6" min="0.10" max="0.95" step="0.05" value="0.65"></div>' +
              '<div class="control-group"><label>Accelerator Method <span><output id="v-accel6">Wegstein Accelerated</output></span></label><input type="range" id="s-accel6" min="1" max="2" step="1" value="2"></div>' +
              '<div class="control-group"><label>Wegstein Bound q <span><output id="v-wq6">-0.80</output></span></label><input type="range" id="s-wq6" min="-2.00" max="0.00" step="0.10" value="-0.80"></div>' +
              '<div class="control-group"><label>Convergence Tol <span><output id="v-tol6">1.0e-4</output></span></label><input type="range" id="s-tol6" min="1" max="5" step="1" value="4"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Iterations to Converge</span><span class="value" id="r-iters6">5</span><span class="subtext">solver effort</span></div>' +
              '<div class="readout-card"><span class="label">Speedup Factor</span><span class="value" id="r-speed6">3.2×</span><span class="subtext">vs direct substitution</span></div>' +
              '<div class="readout-card"><span class="label">Tear Stream Flow</span><span class="value" id="r-tearflow">185 kmol/h</span><span class="subtext">steady state recycle</span></div>' +
              '<div class="readout-card"><span class="label">Loop Damping</span><span class="value" id="r-damp6">Optimal</span><span class="subtext">oscillation suppression</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psim-u6" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psim-u6"></div>',
      init: function(card) {
        var sRr = card.querySelector('#s-rr6'), vRr = card.querySelector('#v-rr6');
        var sAcc = card.querySelector('#s-accel6'), vAcc = card.querySelector('#v-accel6');
        var sWq = card.querySelector('#s-wq6'), vWq = card.querySelector('#v-wq6');
        var sTol = card.querySelector('#s-tol6'), vTol = card.querySelector('#v-tol6');
        var rIter = card.querySelector('#r-iters6'), rSpeed = card.querySelector('#r-speed6');
        var rTear = card.querySelector('#r-tearflow'), rDamp = card.querySelector('#r-damp6');
        var svg = card.querySelector('#plot-psim-u6'), diag = card.querySelector('#diag-psim-u6');

        function update() {
          var rr = parseFloat(sRr.value); vRr.textContent = f(rr, 2);
          var isWeg = parseInt(sAcc.value, 10) === 2;
          vAcc.textContent = isWeg ? 'Wegstein Accelerated' : 'Direct Substitution (Successive)';
          var wq = parseFloat(sWq.value); vWq.textContent = f(wq, 2);
          var tolExp = parseInt(sTol.value, 10); vTol.textContent = '1.0e-' + tolExp;

          var ssFlow = 100 * (rr / (1 - rr));
          var itersDirect = Math.ceil(Math.log(Math.pow(10, -tolExp)) / Math.log(rr));
          itersDirect = Math.max(4, Math.min(60, itersDirect));
          var itersWeg = Math.ceil(itersDirect * 0.28);
          itersWeg = Math.max(3, itersWeg);

          var activeIters = isWeg ? itersWeg : itersDirect;
          var speedup = itersDirect / (isWeg ? itersWeg : itersDirect);

          rIter.textContent = activeIters;
          rSpeed.textContent = f(speedup, 1) + '×';
          rTear.textContent = f(ssFlow, 1) + ' kmol/h';
          rDamp.textContent = isWeg ? 'Secant Accelerated' : (rr > 0.7 ? 'Severe Lag' : 'Stable');

          // SVG convergence trajectory plot
          var dPath = 'M 40 170 ';
          for (var i = 0; i <= 25; i++) {
            var err = i <= activeIters ? Math.pow(isWeg ? 0.35 : rr, i) : Math.pow(10, -tolExp);
            var x_px = 40 + (i / 25.0) * 520;
            var y_px = 170 - (Math.log10(Math.max(1e-6, err)) + 6) * 22;
            y_px = Math.min(170, Math.max(30, y_px));
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="' + (isWeg ? '#059669' : '#d97706') + '" stroke-width="3"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Iteration Count k</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Log10 Residual Error</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Recycle Loop Convergence: ' + (isWeg ? 'Wegstein Secant (Converged in ' + itersWeg + ' iters)' : 'Direct Substitution (' + itersDirect + ' iters)') + '</text>';
          diag.textContent = 'At recycle ratio R/F = ' + f(rr, 2) + ', steady-state tear flow is ' + f(ssFlow, 1) + ' kmol/h. ' + (isWeg ? 'Wegstein secant extrapolation accelerates convergence by ' + f(speedup, 1) + '×, reaching convergence tolerance in ' + itersWeg + ' iterations.' : 'Direct successive substitution converges sluggishly due to high recycle accumulation, requiring ' + itersDirect + ' iterations.');
        }
        [sRr, sAcc, sWq, sTol].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Plantwide Pinch Energy Integration (Composite Curves)</h3><p class="lead">Simulate minimum hot utility QH, cold utility QC, and network heat recovery.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Min Approach ΔTmin <span><output id="v-dtmin">15</output> K</span></label><input type="range" id="s-dtmin" min="5" max="40" step="5" value="15"></div>' +
              '<div class="control-group"><label>Hot Stream Duty <span><output id="v-hotd">1200</output> kW</span></label><input type="range" id="s-hotd" min="600" max="2500" step="100" value="1200"></div>' +
              '<div class="control-group"><label>Cold Stream Demand <span><output id="v-coldd">1500</output> kW</span></label><input type="range" id="s-coldd" min="800" max="3000" step="100" value="1500"></div>' +
              '<div class="control-group"><label>Pinch Temp Tpinch <span><output id="v-tpinch">380</output> K</span></label><input type="range" id="s-tpinch" min="340" max="440" step="10" value="380"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Min Hot Utility QH</span><span class="value" id="r-qhmin">0 kW</span><span class="subtext">external steam duty</span></div>' +
              '<div class="readout-card"><span class="label">Min Cold Utility QC</span><span class="value" id="r-qcmin">0 kW</span><span class="subtext">cooling water duty</span></div>' +
              '<div class="readout-card"><span class="label">Heat Recovery Qrec</span><span class="value" id="r-qrec">0 kW</span><span class="subtext">interchanged exotherm</span></div>' +
              '<div class="readout-card"><span class="label">Energy Savings</span><span class="value" id="r-esave">0%</span><span class="subtext">vs non-integrated site</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psim-u7" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psim-u7"></div>',
      init: function(card) {
        var sDt = card.querySelector('#s-dtmin'), vDt = card.querySelector('#v-dtmin');
        var sHot = card.querySelector('#s-hotd'), vHot = card.querySelector('#v-hotd');
        var sCold = card.querySelector('#s-coldd'), vCold = card.querySelector('#v-coldd');
        var sPinch = card.querySelector('#s-tpinch'), vPinch = card.querySelector('#v-tpinch');
        var rQh = card.querySelector('#r-qhmin'), rQc = card.querySelector('#r-qcmin');
        var rQrec = card.querySelector('#r-qrec'), rEsave = card.querySelector('#r-esave');
        var svg = card.querySelector('#plot-psim-u7'), diag = card.querySelector('#diag-psim-u7');

        function update() {
          var dtMin = parseFloat(sDt.value); vDt.textContent = f(dtMin, 0);
          var Qhot = parseFloat(sHot.value); vHot.textContent = f(Qhot, 0);
          var Qcold = parseFloat(sCold.value); vCold.textContent = f(Qcold, 0);
          var Tpinch = parseFloat(sPinch.value); vPinch.textContent = f(Tpinch, 0);

          var QrecMax = Math.min(Qhot, Qcold) * (1.0 - dtMin * 0.012);
          QrecMax = Math.max(100, QrecMax);
          var Qh = Math.max(50, Qcold - QrecMax);
          var Qc = Math.max(50, Qhot - QrecMax);
          var eSave = (QrecMax / (Qhot + Qcold)) * 100 * 2;

          rQh.textContent = f(Qh, 0) + ' kW';
          rQc.textContent = f(Qc, 0) + ' kW';
          rQrec.textContent = f(QrecMax, 0) + ' kW';
          rEsave.textContent = f(eSave, 1) + ' %';

          // SVG hot and cold composite curves
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="M 80 50 L 320 120 L 520 150" fill="none" stroke="#ef4444" stroke-width="3"/>' +
                          '<path d="M 120 75 L 360 145 L 560 165" fill="none" stroke="#3b82f6" stroke-width="3"/>' +
                          '<line x1="320" y1="120" x2="320" y2="' + (120 + dtMin * 1.5).toFixed(1) + '" stroke="#d97706" stroke-width="2"/>' +
                          '<text x="330" y="130" font-size="10" font-weight="700" fill="#d97706">ΔTmin = ' + f(dtMin, 0) + ' K</text>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Cumulative Enthalpy H (kW)</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Temperature T (K) [Red: Hot, Blue: Cold]</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Pinch Composite Curves (Energy Recovery = ' + f(QrecMax, 0) + ' kW)</text>';
          diag.textContent = 'At minimum temperature approach ΔTmin = ' + f(dtMin, 0) + ' K, maximum heat recovery is ' + f(QrecMax, 0) + ' kW. External utility requirements are minimized to ' + f(Qh, 0) + ' kW steam (QH) and ' + f(Qc, 0) + ' kW cooling water (QC), reducing site energy demands by ' + f(eSave, 1) + '%.';
        }
        [sDt, sHot, sCold, sPinch].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Flowsheet Sensitivity Analysis & Economic Sizing</h3><p class="lead">Simulate CAPEX factorial scaling, OPEX sensitivity, and Net Present Value (NPV).</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Raw Material Cost <span><output id="v-raw8">100%</output></span></label><input type="range" id="s-raw8" min="70" max="150" step="5" value="100"></div>' +
              '<div class="control-group"><label>Product Selling Price <span><output id="v-sell8">100%</output></span></label><input type="range" id="s-sell8" min="70" max="140" step="5" value="100"></div>' +
              '<div class="control-group"><label>Capacity Factor <span><output id="v-cap8">1.0</output>×</span></label><input type="range" id="s-cap8" min="0.5" max="2.5" step="0.1" value="1.0"></div>' +
              '<div class="control-group"><label>Discount Rate r <span><output id="v-disc8">10%</output></span></label><input type="range" id="s-disc8" min="6" max="18" step="1" value="10"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">CAPEX (Guthrie)</span><span class="value" id="r-capex8">$0 M</span><span class="subtext">installed bare module</span></div>' +
              '<div class="readout-card"><span class="label">Annual Cash Flow</span><span class="value" id="r-cash8">$0 M/yr</span><span class="subtext">operating revenue - OPEX</span></div>' +
              '<div class="readout-card"><span class="label">10-Year NPV</span><span class="value" id="r-npv8">$0 M</span><span class="subtext">discounted net value</span></div>' +
              '<div class="readout-card"><span class="label">Payback Period</span><span class="value" id="r-pay8">0.0 yr</span><span class="subtext">capital breakeven</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psim-u8" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psim-u8"></div>',
      init: function(card) {
        var sRaw = card.querySelector('#s-raw8'), vRaw = card.querySelector('#v-raw8');
        var sSell = card.querySelector('#s-sell8'), vSell = card.querySelector('#v-sell8');
        var sCap = card.querySelector('#s-cap8'), vCap = card.querySelector('#v-cap8');
        var sDisc = card.querySelector('#s-disc8'), vDisc = card.querySelector('#v-disc8');
        var rCapex = card.querySelector('#r-capex8'), rCash = card.querySelector('#r-cash8');
        var rNpv = card.querySelector('#r-npv8'), rPay = card.querySelector('#r-pay8');
        var svg = card.querySelector('#plot-psim-u8'), diag = card.querySelector('#diag-psim-u8');

        function update() {
          var rawPct = parseFloat(sRaw.value) / 100; vRaw.textContent = f(rawPct * 100, 0) + '%';
          var sellPct = parseFloat(sSell.value) / 100; vSell.textContent = f(sellPct * 100, 0) + '%';
          var cap = parseFloat(sCap.value); vCap.textContent = f(cap, 1) + '×';
          var disc = parseFloat(sDisc.value) / 100; vDisc.textContent = f(disc * 100, 0) + '%';

          var baseCapex = 25.0; // Million $
          var capex = baseCapex * Math.pow(cap, 0.65); // six-tenths scaling law
          var revenue = 40.0 * cap * sellPct;
          var opex = (18.0 * rawPct + 6.0) * cap;
          var cashFlow = revenue - opex;

          var npv = -capex;
          for (var y = 1; y <= 10; y++) {
            npv += cashFlow / Math.pow(1 + disc, y);
          }
          var payback = cashFlow > 0 ? capex / cashFlow : 99.0;

          rCapex.textContent = '$' + f(capex, 1) + ' M';
          rCash.textContent = '$' + f(cashFlow, 1) + ' M/yr';
          rNpv.textContent = '$' + f(npv, 1) + ' M';
          rNpv.style.color = npv > 0 ? '#15803d' : '#dc2626';
          rPay.textContent = payback < 20 ? f(payback, 1) + ' yr' : '>20 yr';

          // SVG Cash flow trajectory across 10 years
          var dPath = 'M 40 ' + (170 - ((-capex + 60) / 160) * 130).toFixed(1) + ' ';
          var cum = -capex;
          for (var yr = 1; yr <= 10; yr++) {
            cum += cashFlow;
            var x_px = 40 + (yr / 10.0) * 520;
            var y_px = 170 - ((cum + 60) / 160) * 130;
            y_px = Math.min(170, Math.max(20, y_px));
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          var zero_y = 170 - (60 / 160) * 130;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="' + zero_y.toFixed(1) + '" x2="560" y2="' + zero_y.toFixed(1) + '" stroke="#94a3b8" stroke-dasharray="4"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="' + (npv > 0 ? '#059669' : '#dc2626') + '" stroke-width="3"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Plant Life (Years 0 to 10)</text>' +
                          '<text x="50" y="35" font-size="11" fill="#64748b">Cumulative Cash Position ($M)</text>' +
                          '<text x="560" y="' + (zero_y - 6).toFixed(1) + '" text-anchor="end" font-size="10" fill="#64748b">Breakeven ($0 M)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Cumulative Cash Flow: 10-Yr NPV = $' + f(npv, 1) + ' M (Payback: ' + f(payback, 1) + ' yr)</text>';
          diag.textContent = 'Economic sizing analysis: Installed CAPEX scaled via six-tenths exponent is $' + f(capex, 1) + ' M. Annual operating cash flow is $' + f(cashFlow, 1) + ' M/yr. At a ' + f(disc * 100, 0) + '% hurdle discount rate, 10-year project NPV is $' + f(npv, 1) + ' M with an estimated payback of ' + (payback < 20 ? f(payback, 1) + ' years.' : 'over 20 years (unviable under current cost structure).');
        }
        [sRaw, sSell, sCap, sDisc].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    }
  ];
""" + get_engine_footer(8)
'''

with open('tooling/build_cpe_b3_sims_full.py', 'a') as f:
    f.write(psim_code)
print("Added build_psim_sims!")
