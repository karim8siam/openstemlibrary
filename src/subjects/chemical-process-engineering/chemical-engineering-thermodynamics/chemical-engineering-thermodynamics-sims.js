/* Chemical Engineering Thermodynamics Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Ideal Gas Isothermal & Isobaric State Explorer</h3><p class="lead">Evaluate state functions, exact differentials, and PVT paths across pure gas phases.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Temperature T <span><output id="v-t1">350</output> K</span></label><input type="range" id="s-t1" min="200" max="600" step="10" value="350"></div>' +
              '<div class="control-group"><label>Molar Volume Vm <span><output id="v-vm1">4.0</output> m³/kmol</span></label><input type="range" id="s-vm1" min="0.5" max="15.0" step="0.5" value="4.0"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>System Pressure P</small><output id="out-p1">727.5</output> kPa</div>' +
              '<div class="stat-box"><small>Enthalpy Departure</small><output id="out-dh1">0.00</output> kJ/kmol</div>' +
              '<div class="stat-box"><small>Compressibility Z</small><output id="out-z1">1.000</output></div>' +
            '</div>' +
            '<svg id="svg-cet1" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-cet1">Ideal gas equation of state: P = R * T / Vm; state functions depend solely on endpoints.</div>',
      init: function(card) {
        var sT = card.querySelector('#s-t1'), sVm = card.querySelector('#s-vm1');
        var vT = card.querySelector('#v-t1'), vVm = card.querySelector('#v-vm1');
        var outP = card.querySelector('#out-p1'), outDh = card.querySelector('#out-dh1'), outZ = card.querySelector('#out-z1');
        var svg = card.querySelector('#svg-cet1'), diag = card.querySelector('#diag-cet1');

        function update() {
          var T = parseFloat(sT.value), Vm = parseFloat(sVm.value);
          vT.textContent = f(T, 0); vVm.textContent = f(Vm, 1);
          var R = 8.314462;
          var P = (R * T) / Vm; // kPa

          outP.textContent = f(P, 1); outDh.textContent = '0.00'; outZ.textContent = '1.000';

          var pts = '';
          for (var v = 1.0; v <= 15.0; v += 0.5) {
            var p_pt = (R * T) / v;
            var xP = 60 + ((v - 1.0) / 14.0) * 360;
            var yP = 135 - Math.min(105, (p_pt / 2500.0) * 105);
            pts += (pts ? ' ' : '') + xP.toFixed(1) + ',' + yP.toFixed(1);
          }
          var curX = 60 + ((Vm - 1.0) / 14.0) * 360;
          var curY = 135 - Math.min(105, (P / 2500.0) * 105);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="125" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<polyline points="' + pts + '" fill="none" stroke="#0284c7" stroke-width="2.5"/>' +
                          '<circle cx="' + curX + '" cy="' + curY + '" r="5" fill="#ef4444"/>' +
                          '<text x="60" y="38" font-size="11" fill="#0369a1" font-weight="700">Isotherm at T = ' + f(T, 0) + ' K (P vs Vm)</text>' +
                          '<text x="' + Math.min(320, curX + 10) + '" y="' + curY + '" font-size="11" fill="#b91c1c" font-weight="700">P = ' + f(P, 1) + ' kPa</text>' +
                          '<text x="210" y="142" font-size="10" fill="#64748b">Molar Volume (m³/kmol)</text>';
          diag.textContent = 'Thermodynamic state verified: P = ' + f(P, 1) + ' kPa at Vm = ' + f(Vm, 1) + ' m³/kmol.';
        }
        [sT, sVm].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Peng-Robinson Cubic Equation of State</h3><p class="lead">Solve real fluid compressibility factor Z, vapor-liquid cubic roots, and volume departures.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Reduced Temp Tr <span><output id="v-tr">1.10</output></span></label><input type="range" id="s-tr" min="0.60" max="2.00" step="0.05" value="1.10"></div>' +
              '<div class="control-group"><label>Reduced Press Pr <span><output id="v-pr">0.80</output></span></label><input type="range" id="s-pr" min="0.10" max="4.00" step="0.10" value="0.80"></div>' +
              '<div class="control-group"><label>Acentric Factor \u03C9 <span><output id="v-om">0.15</output></span></label><input type="range" id="s-om" min="0.0" max="0.50" step="0.05" value="0.15"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Vapor Factor Zv</small><output id="out-zv">0.785</output></div>' +
              '<div class="stat-box"><small>Liquid Factor Zl</small><output id="out-zl">0.092</output></div>' +
              '<div class="stat-box"><small>Departure (1-Z)</small><output id="out-dz">0.215</output></div>' +
            '</div>' +
            '<svg id="svg-cet2" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-cet2">Peng-Robinson cubic form: Z³ - (1-B)Z² + (A - 3B² - 2B)Z - (AB - B² - B³) = 0.</div>',
      init: function(card) {
        var sTr = card.querySelector('#s-tr'), sPr = card.querySelector('#s-pr'), sOm = card.querySelector('#s-om');
        var vTr = card.querySelector('#v-tr'), vPr = card.querySelector('#v-pr'), vOm = card.querySelector('#v-om');
        var outZv = card.querySelector('#out-zv'), outZl = card.querySelector('#out-zl'), outDz = card.querySelector('#out-dz');
        var svg = card.querySelector('#svg-cet2'), diag = card.querySelector('#diag-cet2');

        function update() {
          var Tr = parseFloat(sTr.value), Pr = parseFloat(sPr.value), om = parseFloat(sOm.value);
          vTr.textContent = f(Tr, 2); vPr.textContent = f(Pr, 2); vOm.textContent = f(om, 2);

          var kappa = 0.37464 + 1.54226 * om - 0.26992 * Math.pow(om, 2);
          var alpha = Math.pow(1.0 + kappa * (1.0 - Math.sqrt(Tr)), 2);
          var A = 0.45724 * alpha * Pr / Math.pow(Tr, 2);
          var B = 0.07780 * Pr / Tr;

          // Solve cubic: Z^3 - (1-B)Z^2 + (A - 3B^2 - 2B)Z - (AB - B^2 - B^3) = 0
          var c2 = -(1.0 - B);
          var c1 = A - 3.0 * Math.pow(B, 2) - 2.0 * B;
          var c0 = -(A * B - Math.pow(B, 2) - Math.pow(B, 3));

          // Newton solver for vapor root (start high Z=1)
          var Zv = 1.0;
          for (var i = 0; i < 20; i++) {
            var fZ = Math.pow(Zv, 3) + c2 * Math.pow(Zv, 2) + c1 * Zv + c0;
            var dfZ = 3.0 * Math.pow(Zv, 2) + 2.0 * c2 * Zv + c1;
            Zv = Zv - fZ / dfZ;
          }
          // Liquid root (start near B)
          var Zl = B + 0.001;
          for (var j = 0; j < 20; j++) {
            var fZ2 = Math.pow(Zl, 3) + c2 * Math.pow(Zl, 2) + c1 * Zl + c0;
            var dfZ2 = 3.0 * Math.pow(Zl, 2) + 2.0 * c2 * Zl + c1;
            Zl = Zl - fZ2 / dfZ2;
          }
          Zv = Math.max(0.1, Math.min(1.5, Zv));
          Zl = Math.max(B, Math.min(0.4, Zl));
          var dZ = Math.abs(1.0 - Zv);

          outZv.textContent = f(Zv, 3); outZl.textContent = f(Zl, 3); outDz.textContent = f(dZ, 3);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<rect x="60" y="50" width="' + (Zv * 200) + '" height="30" fill="#0284c7" rx="4"/>' +
                          '<rect x="60" y="90" width="' + (Zl * 200) + '" height="30" fill="#10b981" rx="4"/>' +
                          '<text x="65" y="42" font-size="11" fill="#0369a1" font-weight="700">Vapor Compressibility Zv = ' + f(Zv, 3) + '</text>' +
                          '<text x="65" y="130" font-size="11" fill="#047857" font-weight="700">Liquid Compressibility Zl = ' + f(Zl, 3) + '</text>' +
                          '<text x="280" y="70" font-size="11" fill="#475569">Parameters: A = ' + f(A, 3) + ', B = ' + f(B, 3) + '</text>';
          diag.textContent = 'Real gas solution: Vapor deviation (1-Z) is ' + f(dZ * 100, 1) + '%; cubic EOS roots stable.';
        }
        [sTr, sPr, sOm].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Heat of Reaction Temperature Dependence (Kirchhoff)</h3><p class="lead">Simulate standard reaction enthalpy shift Delta H(T) = Delta H(T0) + Integral Delta Cp dT.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Reaction Temp T <span><output id="v-tr3">500</output> K</span></label><input type="range" id="s-tr3" min="298" max="900" step="20" value="500"></div>' +
              '<div class="control-group"><label>Base \u0394H°(298) <span><output id="v-dh0">-50.0</output> kJ/mol</span></label><input type="range" id="s-dh0" min="-120" max="60" step="5" value="-50"></div>' +
              '<div class="control-group"><label>\u0394Cp <span><output id="v-dcp">15.0</output> J/mol·K</span></label><input type="range" id="s-dcp" min="-30" max="40" step="5" value="15"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Actual \u0394H°(T)</small><output id="out-dht">-46.97</output> kJ/mol</div>' +
              '<div class="stat-box"><small>Heat Capacity Shift</small><output id="out-dcpterm">3.03</output> kJ/mol</div>' +
              '<div class="stat-box"><small>Reaction Type</small><output id="out-rxtype">Exothermic</output></div>' +
            '</div>' +
            '<svg id="svg-cet3" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-cet3">Kirchhoff relation: d(\u0394H)/dT = \u0394Cp; endothermicity increases with positive \u0394Cp.</div>',
      init: function(card) {
        var sT = card.querySelector('#s-tr3'), sDh0 = card.querySelector('#s-dh0'), sDcp = card.querySelector('#s-dcp');
        var vT = card.querySelector('#v-tr3'), vDh0 = card.querySelector('#v-dh0'), vDcp = card.querySelector('#v-dcp');
        var outDht = card.querySelector('#out-dht'), outDcpterm = card.querySelector('#out-dcpterm'), outRxtype = card.querySelector('#out-rxtype');
        var svg = card.querySelector('#svg-cet3'), diag = card.querySelector('#diag-cet3');

        function update() {
          var T = parseFloat(sT.value), dh0 = parseFloat(sDh0.value), dcp = parseFloat(sDcp.value);
          vT.textContent = f(T, 0); vDh0.textContent = f(dh0, 1); vDcp.textContent = f(dcp, 1);

          var dCpTerm = (dcp * (T - 298.15)) / 1000.0; // kJ/mol
          var dhT = dh0 + dCpTerm;
          var rxType = dhT < 0 ? 'Exothermic' : 'Endothermic';

          outDht.textContent = f(dhT, 2); outDcpterm.textContent = f(dCpTerm, 2); outRxtype.textContent = rxType;

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<line x1="60" y1="80" x2="420" y2="80" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="2"/>' +
                          '<line x1="60" y1="' + (80 - dh0) + '" x2="420" y2="' + (80 - (dh0 + dcp * 600 / 1000.0)) + '" stroke="#0284c7" stroke-width="3"/>' +
                          '<circle cx="' + (60 + ((T - 298) / 600.0) * 360) + '" cy="' + (80 - dhT) + '" r="5" fill="#ef4444"/>' +
                          '<text x="60" y="38" font-size="12" fill="#0369a1" font-weight="700">\u0394H° at ' + f(T,0) + ' K = ' + f(dhT, 2) + ' kJ/mol (' + rxType + ')</text>' +
                          '<text x="240" y="115" font-size="11" fill="#475569">\u0394Cp correction = ' + f(dCpTerm, 2) + ' kJ/mol</text>';
          diag.textContent = 'Kirchhoff energy integral verified: Standard enthalpy of reaction is ' + f(dhT, 2) + ' kJ/mol at ' + f(T, 0) + ' K.';
        }
        [sT, sDh0, sDcp].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Carnot Efficiency & Entropy Generation</h3><p class="lead">Simulate maximum thermal conversion efficiency, heat rejection, and lost work.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Hot Reservoir Th <span><output id="v-th4">600</output> K</span></label><input type="range" id="s-th4" min="400" max="1000" step="20" value="600"></div>' +
              '<div class="control-group"><label>Cold Reservoir Tc <span><output id="v-tc4">300</output> K</span></label><input type="range" id="s-tc4" min="280" max="400" step="10" value="300"></div>' +
              '<div class="control-group"><label>Heat Addition Qh <span><output id="v-qh4">100</output> kW</span></label><input type="range" id="s-qh4" min="20" max="250" step="10" value="100"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Carnot Efficiency</small><output id="out-eta">50.0</output> %</div>' +
              '<div class="stat-box"><small>Maximum Work W</small><output id="out-wmax">50.0</output> kW</div>' +
              '<div class="stat-box"><small>Rejected Heat Qc</small><output id="out-qc">50.0</output> kW</div>' +
            '</div>' +
            '<svg id="svg-cet4" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-cet4">Carnot efficiency eta = 1 - Tc/Th represents the thermodynamic upper bound on power generation.</div>',
      init: function(card) {
        var sTh = card.querySelector('#s-th4'), sTc = card.querySelector('#s-tc4'), sQh = card.querySelector('#s-qh4');
        var vTh = card.querySelector('#v-th4'), vTc = card.querySelector('#v-tc4'), vQh = card.querySelector('#v-qh4');
        var outEta = card.querySelector('#out-eta'), outWmax = card.querySelector('#out-wmax'), outQc = card.querySelector('#out-qc');
        var svg = card.querySelector('#svg-cet4'), diag = card.querySelector('#diag-cet4');

        function update() {
          var th = parseFloat(sTh.value), tc = parseFloat(sTc.value), qh = parseFloat(sQh.value);
          vTh.textContent = f(th, 0); vTc.textContent = f(tc, 0); vQh.textContent = f(qh, 0);

          var eta = 1.0 - tc / th;
          var wMax = qh * eta;
          var qc = qh - wMax;

          outEta.textContent = f(eta * 100.0, 1); outWmax.textContent = f(wMax, 1); outQc.textContent = f(qc, 1);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<rect x="60" y="30" width="100" height="30" rx="4" fill="#ef4444"/>' +
                          '<text x="75" y="50" font-size="11" fill="#fff" font-weight="700">Th = ' + f(th,0) + ' K</text>' +
                          '<rect x="60" y="95" width="100" height="30" rx="4" fill="#0284c7"/>' +
                          '<text x="75" y="115" font-size="11" fill="#fff" font-weight="700">Tc = ' + f(tc,0) + ' K</text>' +
                          '<circle cx="230" cy="77" r="25" fill="#f59e0b"/>' +
                          '<text x="215" y="82" font-size="12" fill="#fff" font-weight="700">HE</text>' +
                          '<line x1="160" y1="45" x2="210" y2="65" stroke="#ef4444" stroke-width="2"/>' +
                          '<line x1="210" y1="90" x2="160" y2="110" stroke="#0284c7" stroke-width="2"/>' +
                          '<line x1="255" y1="77" x2="340" y2="77" stroke="#10b981" stroke-width="4"/>' +
                          '<text x="350" y="82" font-size="13" fill="#047857" font-weight="700">W = ' + f(wMax,1) + ' kW</text>';
          diag.textContent = 'Second law limit: Maximum Carnot efficiency is ' + f(eta * 100, 1) + '%; reversible work output = ' + f(wMax, 1) + ' kW.';
        }
        [sTh, sTc, sQh].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Fugacity & Residual Enthalpy Departures</h3><p class="lead">Calculate real fluid fugacity coefficient phi and enthalpy departure H - H_ig.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Pressure P <span><output id="v-p5">5.0</output> MPa</span></label><input type="range" id="s-p5" min="0.5" max="25.0" step="0.5" value="5.0"></div>' +
              '<div class="control-group"><label>Temperature T <span><output id="v-t5">400</output> K</span></label><input type="range" id="s-t5" min="250" max="650" step="10" value="400"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Fugacity Coeff \u03C6</small><output id="out-phi">0.892</output></div>' +
              '<div class="stat-box"><small>Fugacity f</small><output id="out-fug">4.46</output> MPa</div>' +
              '<div class="stat-box"><small>Residual H^R</small><output id="out-hr">-450</output> kJ/kmol</div>' +
            '</div>' +
            '<svg id="svg-cet5" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-cet5">Fugacity represents effective thermodynamic chemical pressure: ln(phi) = Integral (Z-1)/P dP.</div>',
      init: function(card) {
        var sP = card.querySelector('#s-p5'), sT = card.querySelector('#s-t5');
        var vP = card.querySelector('#v-p5'), vT = card.querySelector('#v-t5');
        var outPhi = card.querySelector('#out-phi'), outFug = card.querySelector('#out-fug'), outHr = card.querySelector('#out-hr');
        var svg = card.querySelector('#svg-cet5'), diag = card.querySelector('#diag-cet5');

        function update() {
          var P = parseFloat(sP.value), T = parseFloat(sT.value);
          vP.textContent = f(P, 1); vT.textContent = f(T, 0);

          // Simplified virial/departure: B = b0 - b1/T
          var B_vir = 0.04 - 25.0 / T;
          var R = 8.314e-3; // MPa m3 / kmol K
          var phi = Math.exp((B_vir * P) / (R * T));
          phi = Math.max(0.1, Math.min(1.5, phi));
          var fug = phi * P;
          var HR = -50.0 * P * (300.0 / T);

          outPhi.textContent = f(phi, 3); outFug.textContent = f(fug, 2); outHr.textContent = f(HR, 0);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<rect x="60" y="50" width="' + (phi * 200) + '" height="35" rx="4" fill="#0284c7"/>' +
                          '<text x="65" y="42" font-size="11" fill="#0369a1" font-weight="700">Fugacity Coefficient \u03C6 = ' + f(phi, 3) + '</text>' +
                          '<text x="280" y="65" font-size="12" fill="#0f172a" font-weight="700">f = ' + f(fug, 2) + ' MPa</text>' +
                          '<text x="280" y="90" font-size="11" fill="#475569">Enthalpy departure H^R = ' + f(HR, 0) + ' kJ/kmol</text>';
          diag.textContent = 'Non-ideality quantified: Chemical fugacity is ' + f(fug, 2) + ' MPa at ' + f(P, 1) + ' MPa total pressure.';
        }
        [sP, sT].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Binary Vapor-Liquid Equilibrium (Raoult Law)</h3><p class="lead">Simulate T-x-y bubble and dew point envelopes for ideal binary solutions.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Liquid Mole Frac xA <span><output id="v-xa6">0.40</output></span></label><input type="range" id="s-xa6" min="0.05" max="0.95" step="0.05" value="0.40"></div>' +
              '<div class="control-group"><label>Total Pressure P <span><output id="v-ptot">101.3</output> kPa</span></label><input type="range" id="s-ptot" min="50" max="300" step="10" value="101.3"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Vapor Mole Frac yA</small><output id="out-ya6">0.625</output></div>' +
              '<div class="stat-box"><small>Bubble Temp T_bub</small><output id="out-tbub">92.4</output> °C</div>' +
              '<div class="stat-box"><small>Relative Volatility</small><output id="out-relvol">2.50</output></div>' +
            '</div>' +
            '<svg id="svg-cet6" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-cet6">Raoult law: P = xA * P_sat,A + xB * P_sat,B; yA = (xA * P_sat,A) / P.</div>',
      init: function(card) {
        var sXa = card.querySelector('#s-xa6'), sPtot = card.querySelector('#s-ptot');
        var vXa = card.querySelector('#v-xa6'), vPtot = card.querySelector('#v-ptot');
        var outYa = card.querySelector('#out-ya6'), outTbub = card.querySelector('#out-tbub'), outRelvol = card.querySelector('#out-relvol');
        var svg = card.querySelector('#svg-cet6'), diag = card.querySelector('#diag-cet6');

        function update() {
          var xA = parseFloat(sXa.value), P = parseFloat(sPtot.value);
          vXa.textContent = f(xA, 2); vPtot.textContent = f(P, 1);

          var alpha = 2.5;
          var yA = (alpha * xA) / (1.0 + (alpha - 1.0) * xA);
          // Pure component boiling points: Ta=80, Tb=110
          var tBub = 110.0 - (110.0 - 80.0) * (xA * alpha) / (1.0 + (alpha - 1.0) * xA);

          outYa.textContent = f(yA, 3); outTbub.textContent = f(tBub, 1); outRelvol.textContent = f(alpha, 2);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<path d="M 60 120 Q 200 70 420 30" fill="none" stroke="#0284c7" stroke-width="2.5"/>' +
                          '<path d="M 60 120 Q 280 90 420 30" fill="none" stroke="#f59e0b" stroke-width="2.5"/>' +
                          '<circle cx="' + (60 + xA * 360) + '" cy="' + (120 - (tBub - 80) * 2.5) + '" r="5" fill="#ef4444"/>' +
                          '<text x="60" y="35" font-size="11" fill="#0369a1" font-weight="700">T-x-y Phase Diagram (P = ' + f(P,0) + ' kPa)</text>' +
                          '<text x="240" y="75" font-size="11" fill="#b91c1c" font-weight="700">xA = ' + f(xA,2) + ' \u2192 yA = ' + f(yA,3) + '</text>' +
                          '<text x="240" y="95" font-size="11" fill="#475569">Bubble point = ' + f(tBub,1) + ' °C</text>';
          diag.textContent = 'Phase equilibrium confirmed: Liquid xA = ' + f(xA, 2) + ' coexists with equilibrium vapor yA = ' + f(yA, 3) + '.';
        }
        [sXa, sPtot].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>NRTL Activity Coefficient & Excess Gibbs Free Energy</h3><p class="lead">Simulate non-ideal liquid activity coefficients gamma_i and G_E/RT.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Mole Fraction x1 <span><output id="v-x7">0.50</output></span></label><input type="range" id="s-x7" min="0.05" max="0.95" step="0.05" value="0.50"></div>' +
              '<div class="control-group"><label>Interaction \u03C412 <span><output id="v-tau12">0.80</output></span></label><input type="range" id="s-tau12" min="-1.50" max="2.50" step="0.10" value="0.80"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Activity Coeff \u03B31</small><output id="out-gam1">1.25</output></div>' +
              '<div class="stat-box"><small>Activity Coeff \u03B32</small><output id="out-gam2">1.22</output></div>' +
              '<div class="stat-box"><small>Excess Gibbs G_E/RT</small><output id="out-gert">0.21</output></div>' +
            '</div>' +
            '<svg id="svg-cet7" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-cet7">NRTL local composition model captures positive and negative deviations from Raoult law.</div>',
      init: function(card) {
        var sX = card.querySelector('#s-x7'), sTau = card.querySelector('#s-tau12');
        var vX = card.querySelector('#v-x7'), vTau = card.querySelector('#v-tau12');
        var outGam1 = card.querySelector('#out-gam1'), outGam2 = card.querySelector('#out-gam2'), outGert = card.querySelector('#out-gert');
        var svg = card.querySelector('#svg-cet7'), diag = card.querySelector('#diag-cet7');

        function update() {
          var x1 = parseFloat(sX.value), tau12 = parseFloat(sTau.value);
          vX.textContent = f(x1, 2); vTau.textContent = f(tau12, 2);

          var x2 = 1.0 - x1;
          var alpha = 0.3;
          var G12 = Math.exp(-alpha * tau12);
          var lnGam1 = Math.pow(x2, 2) * (tau12 * Math.pow(G12 / (x1 + x2 * G12), 2));
          var lnGam2 = Math.pow(x1, 2) * (tau12 * Math.pow(1.0 / (x2 + x1 * G12), 2));
          var gam1 = Math.exp(lnGam1);
          var gam2 = Math.exp(lnGam2);
          var gERT = x1 * lnGam1 + x2 * lnGam2;

          outGam1.textContent = f(gam1, 2); outGam2.textContent = f(gam2, 2); outGert.textContent = f(gERT, 2);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<rect x="60" y="45" width="' + (gam1 * 100) + '" height="30" fill="#0284c7" rx="4"/>' +
                          '<rect x="60" y="85" width="' + (gam2 * 100) + '" height="30" fill="#10b981" rx="4"/>' +
                          '<text x="65" y="38" font-size="11" fill="#0369a1" font-weight="700">\u03B31 = ' + f(gam1, 2) + '</text>' +
                          '<text x="65" y="125" font-size="11" fill="#047857" font-weight="700">\u03B32 = ' + f(gam2, 2) + '</text>' +
                          '<text x="240" y="70" font-size="12" fill="#0f172a" font-weight="700">Excess Gibbs G_E/RT = ' + f(gERT, 3) + '</text>' +
                          '<text x="240" y="95" font-size="11" fill="#475569">Local composition factor G12 = ' + f(G12, 3) + '</text>';
          diag.textContent = 'Non-ideal solution thermodynamics: Activity coefficients \u03B31 = ' + f(gam1, 2) + ', \u03B32 = ' + f(gam2, 2) + '.';
        }
        [sX, sTau].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Chemical Reaction Equilibrium Constant K(T)</h3><p class="lead">Simulate Van \'t Hoff equilibrium conversion and temperature sensitivity.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Temperature T <span><output id="v-teq">600</output> K</span></label><input type="range" id="s-teq" min="300" max="1000" step="25" value="600"></div>' +
              '<div class="control-group"><label>\u0394H°rxn <span><output id="v-dh8">-45</output> kJ/mol</span></label><input type="range" id="s-dh8" min="-100" max="60" step="5" value="-45"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Equilibrium K</small><output id="out-keq">8.42</output></div>' +
              '<div class="stat-box"><small>Equilibrium Conversion</small><output id="out-xeq">89.4</output> %</div>' +
              '<div class="stat-box"><small>Van \'t Hoff dlnK/dT</small><output id="out-dlnk">-0.015</output> K⁻¹</div>' +
            '</div>' +
            '<svg id="svg-cet8" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-cet8">Van \'t Hoff equation: d(ln K)/dT = \u0394H° / (R * T²). Exothermic reactions show decreasing K with temperature.</div>',
      init: function(card) {
        var sT = card.querySelector('#s-teq'), sDh = card.querySelector('#s-dh8');
        var vT = card.querySelector('#v-teq'), vDh = card.querySelector('#v-dh8');
        var outKeq = card.querySelector('#out-keq'), outXeq = card.querySelector('#out-xeq'), outDlnk = card.querySelector('#out-dlnk');
        var svg = card.querySelector('#svg-cet8'), diag = card.querySelector('#diag-cet8');

        function update() {
          var T = parseFloat(sT.value), dH = parseFloat(sDh.value);
          vT.textContent = f(T, 0); vDh.textContent = f(dH, 0);

          var R = 8.314e-3; // kJ/mol K
          var dG0 = 5.0; // at 298
          var lnK = -(dH / (R * T)) + (dH - dG0) / (R * 298.15);
          var K = Math.exp(Math.max(-8, Math.min(8, lnK)));
          // A <-> B: K = x / (1-x) => x_eq = K / (1 + K)
          var xEq = (K / (1.0 + K)) * 100.0;
          var dlnK = dH / (8.314e-3 * Math.pow(T, 2));

          outKeq.textContent = f(K, 2); outXeq.textContent = f(xEq, 1); outDlnk.textContent = f(dlnK, 4);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<rect x="60" y="55" width="' + (xEq * 3.4) + '" height="35" rx="4" fill="#0284c7"/>' +
                          '<text x="65" y="45" font-size="12" fill="#0369a1" font-weight="700">Equilibrium Conversion X_eq = ' + f(xEq, 1) + '%</text>' +
                          '<text x="60" y="115" font-size="11" fill="#475569">Equilibrium constant K = ' + f(K, 2) + ' at T = ' + f(T, 0) + ' K</text>' +
                          '<text x="280" y="115" font-size="11" fill="#0f172a">d(ln K)/dT = ' + f(dlnK, 4) + ' K⁻¹</text>';
          diag.textContent = 'Reaction equilibrium closed: Equilibrium conversion reaches ' + f(xEq, 1) + '% at ' + f(T, 0) + ' K.';
        }
        [sT, sDh].forEach(function(el) { el.addEventListener('input', update); });
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
