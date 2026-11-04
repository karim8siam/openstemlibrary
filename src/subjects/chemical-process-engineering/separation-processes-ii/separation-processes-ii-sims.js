/* Separation Processes II Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Reverse Osmosis (RO) Flux & Concentration Polarization</h3><p class="lead">Simulate membrane desalination: evaluate water flux Jw, osmotic pressure Δπ, and concentration polarization modulus CP.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Feed Pressure ΔP <span><output id="v-delp">55.0</output> bar</span></label><input type="range" id="s-delp" min="15.0" max="80.0" step="2.5" value="55.0"></div>' +
              '<div class="control-group"><label>Feed Salinity Cb <span><output id="v-salin">32.0</output> g/L</span></label><input type="range" id="s-salin" min="2.0" max="65.0" step="1.0" value="32.0"></div>' +
              '<div class="control-group"><label>Water Permeability A <span><output id="v-perma">1.80</output> LMH/bar</span></label><input type="range" id="s-perma" min="0.50" max="4.00" step="0.10" value="1.80"></div>' +
              '<div class="control-group"><label>Crossflow Mass Coeff kcp <span><output id="v-kcp">20.0</output> μm/s</span></label><input type="range" id="s-kcp" min="5.0" max="60.0" step="2.5" value="20.0"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Bulk Osmotic Press πb</div><div class="readout-value" id="r-pib">25.6 bar</div></div>' +
              '<div class="readout-card"><div class="readout-label">Polarization Modulus CP</div><div class="readout-value" id="r-cpmod">1.28</div></div>' +
              '<div class="readout-card"><div class="readout-label">Net Driving NDP</div><div class="readout-value" id="r-ndp">22.2 bar</div></div>' +
              '<div class="readout-card"><div class="readout-label">Water Flux Jw</div><div class="readout-value" id="r-jw">40.0 LMH</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp21" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp21"></p>',
      init: function(el) {
        var sDelp = el.querySelector('#s-delp'), vDelp = el.querySelector('#v-delp');
        var sSalin = el.querySelector('#s-salin'), vSalin = el.querySelector('#v-salin');
        var sPerma = el.querySelector('#s-perma'), vPerma = el.querySelector('#v-perma');
        var sKcp = el.querySelector('#s-kcp'), vKcp = el.querySelector('#v-kcp');
        var rPib = el.querySelector('#r-pib'), rCpmod = el.querySelector('#r-cpmod');
        var rNdp = el.querySelector('#r-ndp'), rJw = el.querySelector('#r-jw');
        var svg = el.querySelector('#svg-sp21'), diag = el.querySelector('#diag-sp21');

        function update() {
          var dP = parseFloat(sDelp.value); vDelp.textContent = f(dP, 1);
          var Cb = parseFloat(sSalin.value); vSalin.textContent = f(Cb, 1);
          var A = parseFloat(sPerma.value); vPerma.textContent = f(A, 2);
          var kcp_um = parseFloat(sKcp.value); vKcp.textContent = f(kcp_um, 1);

          var pi_b = 0.80 * Cb; // approx 0.80 bar per g/L NaCl
          var kcp = kcp_um * 1e-6; // m/s
          var kcp_LMH = kcp * 3.6e6; // L/(m2 h)

          // Coupled solution for Jw and CP:
          var Jw = Math.max(1.0, A * (dP - pi_b));
          var CP = Math.exp(Jw / Math.max(10, kcp_LMH));
          CP = Math.min(2.5, Math.max(1.05, CP));
          var pi_m = pi_b * CP;
          var NDP = Math.max(0.5, dP - pi_m);
          Jw = A * NDP;

          rPib.textContent = f(pi_b, 1) + ' bar';
          rCpmod.textContent = f(CP, 2);
          rNdp.textContent = f(NDP, 1) + ' bar';
          rJw.textContent = f(Jw, 1) + ' LMH';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="280" y="30" width="20" height="140" fill="#0284c7" rx="3"/>' +
                          '<text x="290" y="105" text-anchor="middle" font-size="10" font-weight="700" fill="#ffffff" transform="rotate(-90 290 105)">RO Membrane</text>' +
                          '<rect x="80" y="40" width="200" height="120" fill="#dbeafe" fill-opacity="0.3"/>' +
                          '<text x="180" y="65" text-anchor="middle" font-size="12" font-weight="700" fill="#1e40af">Feed/Retentate Channel</text>' +
                          '<path d="M 120 120 Q 240 120 280 60" fill="none" stroke="#dc2626" stroke-width="3"/>' +
                          '<text x="270" y="55" text-anchor="end" font-size="10" font-weight="700" fill="#dc2626">Cm = ' + f(Cb*CP,1) + ' g/L</text>' +
                          '<line x1="300" y1="100" x2="480" y2="100" stroke="#16a34a" stroke-width="4"/>' +
                          '<text x="400" y="90" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">Permeate Jw = ' + f(Jw,1) + ' LMH</text>' +
                          '<text x="300" y="24" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">RO Transport: NDP = ' + f(NDP,1) + ' bar (CP = ' + f(CP,2) + ')</text>';
          diag.textContent = 'Reverse osmosis: Bulk osmotic pressure = ' + f(pi_b, 1) + ' bar. Concentration polarization increases membrane surface salt by ' + f((CP - 1) * 100, 1) + '%. Net flux = ' + f(Jw, 1) + ' LMH.';
        }
        [sDelp, sSalin, sPerma, sKcp].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Hollow-Fiber Gas Permeation Module & Stage-Cut Selectivity</h3><p class="lead">Simulate industrial gas separation in hollow-fiber bundles: evaluate permeate stage cut θ and membrane area requirements.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Stage Cut θ <span><output id="v-theta">0.25</output></span></label><input type="range" id="s-theta" min="0.05" max="0.50" step="0.05" value="0.25"></div>' +
              '<div class="control-group"><label>Membrane Selectivity α <span><output id="v-alpha22">30.0</output></span></label><input type="range" id="s-alpha22" min="5.0" max="60.0" step="2.5" value="30.0"></div>' +
              '<div class="control-group"><label>Feed Fast Gas zF <span><output id="v-zf22">0.20</output></span></label><input type="range" id="s-zf22" min="0.05" max="0.60" step="0.05" value="0.20"></div>' +
              '<div class="control-group"><label>Fiber Count <span><output id="v-fibers">5000</output></span></label><input type="range" id="s-fibers" min="1000" max="20000" step="1000" value="5000"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Permeate Purity yp</div><div class="readout-value" id="r-yp2">82.5 mol%</div></div>' +
              '<div class="readout-card"><div class="readout-label">Retentate Loss xr</div><div class="readout-value" id="r-xr2">0.058</div></div>' +
              '<div class="readout-card"><div class="readout-label">Recovery of Fast Gas</div><div class="readout-value" id="r-rec22">78.3 %</div></div>' +
              '<div class="readout-card"><div class="readout-label">Total Membrane Area</div><div class="readout-value" id="r-aream">15.7 m²</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp22" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp22"></p>',
      init: function(el) {
        var sTheta = el.querySelector('#s-theta'), vTheta = el.querySelector('#v-theta');
        var sAlpha = el.querySelector('#s-alpha22'), vAlpha = el.querySelector('#v-alpha22');
        var sZf = el.querySelector('#s-zf22'), vZf = el.querySelector('#v-zf22');
        var sFibers = el.querySelector('#s-fibers'), vFibers = el.querySelector('#v-fibers');
        var rYp = el.querySelector('#r-yp2'), rXr = el.querySelector('#r-xr2');
        var rRec = el.querySelector('#r-rec22'), rArea = el.querySelector('#r-aream');
        var svg = el.querySelector('#svg-sp22'), diag = el.querySelector('#diag-sp22');

        function update() {
          var theta = parseFloat(sTheta.value); vTheta.textContent = f(theta, 2);
          var alpha = parseFloat(sAlpha.value); vAlpha.textContent = f(alpha, 1);
          var zF = parseFloat(sZf.value); vZf.textContent = f(zF, 2);
          var fibers = parseInt(sFibers.value, 10); vFibers.textContent = fibers;

          var yp = (alpha * zF) / (1 + (alpha - 1) * zF);
          // Attenuation by stage-cut:
          yp = Math.max(zF * 1.1, yp * (1 - 0.45 * theta));
          var xr = (zF - theta * yp) / Math.max(0.01, (1 - theta));
          xr = Math.max(0.005, xr);
          var recovery = (theta * yp / zF) * 100;
          var area = fibers * Math.PI * 0.0005 * 2.0; // 0.5mm OD, 2m length

          rYp.textContent = f(yp * 100, 1) + ' mol%';
          rXr.textContent = f(xr, 3);
          rRec.textContent = f(recovery, 1) + ' %';
          rArea.textContent = f(area, 1) + ' m²';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="160" y="55" width="280" height="90" fill="#f1f5f9" stroke="#334155" stroke-width="2" rx="10"/>' +
                          '<line x1="170" y1="80" x2="430" y2="80" stroke="#0284c7" stroke-width="2" stroke-dasharray="3 3"/>' +
                          '<line x1="170" y1="100" x2="430" y2="100" stroke="#0284c7" stroke-width="2" stroke-dasharray="3 3"/>' +
                          '<line x1="170" y1="120" x2="430" y2="120" stroke="#0284c7" stroke-width="2" stroke-dasharray="3 3"/>' +
                          '<text x="300" y="45" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Hollow-Fiber Bundle (' + fibers + ' fibers)</text>' +
                          '<line x1="60" y1="100" x2="160" y2="100" stroke="#334155" stroke-width="4"/>' +
                          '<text x="110" y="90" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a">Feed zF=' + f(zF,2) + '</text>' +
                          '<line x1="440" y1="100" x2="540" y2="100" stroke="#64748b" stroke-width="3"/>' +
                          '<text x="490" y="90" text-anchor="middle" font-size="10" fill="#475569">Retentate xr=' + f(xr,3) + '</text>' +
                          '<line x1="300" y1="145" x2="300" y2="180" stroke="#16a34a" stroke-width="4"/>' +
                          '<text x="300" y="195" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">Permeate yp = ' + f(yp*100,1) + ' mol% (θ=' + f(theta,2) + ')</text>';
          diag.textContent = 'Gas permeation module: Stage cut θ = ' + f(theta, 2) + '. Permeate fast gas purity = ' + f(yp * 100, 1) + ' mol% with ' + f(recovery, 1) + '% component recovery.';
        }
        [sTheta, sAlpha, sZf, sFibers].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Fixed-Bed Adsorption Dynamics & Breakthrough Front Simulator</h3><p class="lead">Simulate breakthrough front propagation in activated carbon / zeolite beds: calculate breakthrough time tb and bed utilization.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Bed Length L <span><output id="v-blen">1.20</output> m</span></label><input type="range" id="s-blen" min="0.40" max="3.00" step="0.10" value="1.20"></div>' +
              '<div class="control-group"><label>Interstitial Velocity v <span><output id="v-intv">4.0</output> cm/s</span></label><input type="range" id="s-intv" min="1.0" max="15.0" step="0.5" value="4.0"></div>' +
              '<div class="control-group"><label>Adsorption Capacity qm <span><output id="v-qm">120</output> mg/g</span></label><input type="range" id="s-qm" min="30" max="300" step="10" value="120"></div>' +
              '<div class="control-group"><label>Inlet Concentration C0 <span><output id="v-cin3">1.50</output> g/m³</span></label><input type="range" id="s-cin3" min="0.20" max="5.00" step="0.10" value="1.50"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Breakthrough Time tb</div><div class="readout-value" id="r-tb">38.4 h</div></div>' +
              '<div class="readout-card"><div class="readout-label">Stoichiometric Time ts</div><div class="readout-value" id="r-ts">48.0 h</div></div>' +
              '<div class="readout-card"><div class="readout-label">Bed Utilization %</div><div class="readout-value" id="r-util">80.0 %</div></div>' +
              '<div class="readout-card"><div class="readout-label">MTZ Length</div><div class="readout-value" id="r-mtz">0.24 m</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp23" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp23"></p>',
      init: function(el) {
        var sBlen = el.querySelector('#s-blen'), vBlen = el.querySelector('#v-blen');
        var sIntv = el.querySelector('#s-intv'), vIntv = el.querySelector('#v-intv');
        var sQm = el.querySelector('#s-qm'), vQm = el.querySelector('#v-qm');
        var sCin = el.querySelector('#s-cin3'), vCin = el.querySelector('#v-cin3');
        var rTb = el.querySelector('#r-tb'), rTs = el.querySelector('#r-ts');
        var rUtil = el.querySelector('#r-util'), rMtz = el.querySelector('#r-mtz');
        var svg = el.querySelector('#svg-sp23'), diag = el.querySelector('#diag-sp23');

        var rhoBed = 600; // kg/m3

        function update() {
          var L = parseFloat(sBlen.value); vBlen.textContent = f(L, 2);
          var v_cms = parseFloat(sIntv.value); vIntv.textContent = f(v_cms, 1);
          var qm = parseFloat(sQm.value); vQm.textContent = f(qm, 0);
          var C0 = parseFloat(sCin.value); vCin.textContent = f(C0, 2);

          var v = v_cms * 0.01; // m/s
          var q0_kg = (qm * 1e-3) * rhoBed; // kg adsorbate per m3 bed
          var C0_kg = C0 * 1e-3; // kg/m3

          var uWave = (v * C0_kg) / (q0_kg + C0_kg); // wave velocity m/s
          var t_stoich = (L / Math.max(1e-8, uWave)) / 3600; // hours
          var t_break = t_stoich * 0.80;
          var L_mtz = L * 0.20;
          var util = (t_break / t_stoich) * 100;

          rTb.textContent = f(t_break, 1) + ' h';
          rTs.textContent = f(t_stoich, 1) + ' h';
          rUtil.textContent = f(util, 1) + ' %';
          rMtz.textContent = f(L_mtz, 2) + ' m';

          // S-curve points
          var pts = [];
          for (var tS = 0; tS <= t_stoich * 1.5; tS += t_stoich * 0.05) {
            var px = 100 + (tS / (t_stoich * 1.5)) * 400;
            var c_ratio = 1 / (1 + Math.exp(-8 * (tS - t_stoich) / t_stoich));
            var py = 160 - c_ratio * 110;
            pts.push(f(px,1) + ',' + f(py,1));
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="100" y="40" width="400" height="120" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>' +
                          '<polyline points="' + pts.join(' ') + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<line x1="' + (100 + (t_break/(t_stoich*1.5))*400) + '" y1="40" x2="' + (100 + (t_break/(t_stoich*1.5))*400) + '" y2="160" stroke="#dc2626" stroke-dasharray="3 3"/>' +
                          '<text x="' + (100 + (t_break/(t_stoich*1.5))*400) + '" y="32" text-anchor="middle" font-size="10" font-weight="700" fill="#dc2626">tb = ' + f(t_break,1) + 'h</text>' +
                          '<text x="300" y="22" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Breakthrough Curve C/C0 (L = ' + f(L,2) + 'm)</text>' +
                          '<text x="510" y="55" font-size="10" fill="#64748b">C/C0 = 1.0</text>' +
                          '<text x="510" y="160" font-size="10" fill="#64748b">C/C0 = 0.0</text>' +
                          '<text x="300" y="185" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">Bed Utilization: ' + f(util,1) + '% | MTZ = ' + f(L_mtz,2) + ' m</text>';
          diag.textContent = 'Fixed-bed breakthrough: Breakthrough time tb = ' + f(t_break, 1) + ' h. Bed saturation utilization = ' + f(util, 1) + '% (Mass transfer zone length = ' + f(L_mtz, 2) + ' m).';
        }
        [sBlen, sIntv, sQm, sCin].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Preparative Chromatography Van Deemter Plate Height & Resolution</h3><p class="lead">Simulate chromatographic column dispersion: optimize mobile phase linear velocity u and compute resolution Rs between peak pairs.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Mobile Phase Velocity u <span><output id="v-uvel">2.50</output> mm/s</span></label><input type="range" id="s-uvel" min="0.50" max="10.00" step="0.25" value="2.50"></div>' +
              '<div class="control-group"><label>Packing Particle dp <span><output id="v-dp4">25</output> μm</span></label><input type="range" id="s-dp4" min="5" max="80" step="5" value="25"></div>' +
              '<div class="control-group"><label>Column Length L <span><output id="v-clen">25.0</output> cm</span></label><input type="range" id="s-clen" min="10.0" max="100.0" step="5.0" value="25.0"></div>' +
              '<div class="control-group"><label>Selectivity α <span><output id="v-alphac">1.18</output></span></label><input type="range" id="s-alphac" min="1.05" max="1.60" step="0.02" value="1.18"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Plate Height HETP</div><div class="readout-value" id="r-hetp">54.2 μm</div></div>' +
              '<div class="readout-card"><div class="readout-label">Plate Count N</div><div class="readout-value" id="r-pcount">4,612 plates</div></div>' +
              '<div class="readout-card"><div class="readout-label">Optimum Velocity uopt</div><div class="readout-value" id="r-uopt">2.12 mm/s</div></div>' +
              '<div class="readout-card"><div class="readout-label">Peak Resolution Rs</div><div class="readout-value" id="r-resol">1.82 (Baseline)</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp24" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp24"></p>',
      init: function(el) {
        var sU = el.querySelector('#s-uvel'), vU = el.querySelector('#v-uvel');
        var sDp = el.querySelector('#s-dp4'), vDp = el.querySelector('#v-dp4');
        var sClen = el.querySelector('#s-clen'), vClen = el.querySelector('#v-clen');
        var sAl = el.querySelector('#s-alphac'), vAl = el.querySelector('#v-alphac');
        var rHetp = el.querySelector('#r-hetp'), rPcount = el.querySelector('#r-pcount');
        var rUopt = el.querySelector('#r-uopt'), rResol = el.querySelector('#r-resol');
        var svg = el.querySelector('#svg-sp24'), diag = el.querySelector('#diag-sp24');

        function update() {
          var u = parseFloat(sU.value); vU.textContent = f(u, 2);
          var dp_um = parseFloat(sDp.value); vDp.textContent = f(dp_um, 0);
          var L_cm = parseFloat(sClen.value); vClen.textContent = f(L_cm, 1);
          var alpha = parseFloat(sAl.value); vAl.textContent = f(alpha, 2);

          // Van Deemter: H = A + B/u + C*u
          var A = 1.5 * dp_um; // um
          var B = 35.0; // um * mm/s
          var C = 0.035 * Math.pow(dp_um, 2) / 10; // um / (mm/s)

          var H = A + B / u + C * u; // um
          var u_opt = Math.sqrt(B / Math.max(0.001, C));
          var L_um = L_cm * 10000;
          var N = Math.round(L_um / H);

          var kPrime = 3.0; // average capacity factor
          var Rs = 0.25 * Math.sqrt(N) * ((alpha - 1) / alpha) * (kPrime / (1 + kPrime));

          rHetp.textContent = f(H, 1) + ' μm';
          rPcount.textContent = f(N, 0) + ' plates';
          rUopt.textContent = f(u_opt, 2) + ' mm/s';
          rResol.textContent = f(Rs, 2) + (Rs >= 1.5 ? ' (Baseline)' : ' (Overlap)');

          // Chromatogram twin Gaussian peaks
          var p1_cx = 280, p2_cx = 280 + (alpha - 1) * 200;
          var sigma = Math.max(8, 60 / Math.sqrt(N / 1000));

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="80" y1="160" x2="520" y2="160" stroke="#334155" stroke-width="2"/>' +
                          '<path d="M ' + (p1_cx - 3*sigma) + ' 160 Q ' + p1_cx + ' 50 ' + (p1_cx + 3*sigma) + ' 160" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<path d="M ' + (p2_cx - 3*sigma) + ' 160 Q ' + p2_cx + ' 50 ' + (p2_cx + 3*sigma) + ' 160" fill="none" stroke="#dc2626" stroke-width="3"/>' +
                          '<text x="' + p1_cx + '" y="40" text-anchor="middle" font-size="11" font-weight="700" fill="#2563eb">Peak A</text>' +
                          '<text x="' + p2_cx + '" y="40" text-anchor="middle" font-size="11" font-weight="700" fill="#dc2626">Peak B</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Chromatogram Resolution: Rs = ' + f(Rs,2) + '</text>' +
                          '<text x="300" y="185" text-anchor="middle" font-size="11" fill="#475569">HETP = ' + f(H,1) + ' μm | N = ' + f(N,0) + ' | uopt = ' + f(u_opt,2) + ' mm/s</text>';
          diag.textContent = 'Van Deemter chromatography: Plate height H = ' + f(H, 1) + ' μm (N = ' + f(N, 0) + ' plates). Twin peak resolution Rs = ' + f(Rs, 2) + '.';
        }
        [sU, sDp, sClen, sAl].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>MSMPR Crystallizer Supersaturation & Crystal Size Distribution</h3><p class="lead">Simulate continuous solution crystallization: evaluate primary nucleation rate B0, crystal growth rate G, and dominant size LD.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Supersaturation S <span><output id="v-ssat">1.12</output></span></label><input type="range" id="s-ssat" min="1.02" max="1.30" step="0.01" value="1.12"></div>' +
              '<div class="control-group"><label>Residence Time τ <span><output id="v-tau5">45.0</output> min</span></label><input type="range" id="s-tau5" min="15.0" max="120.0" step="5.0" value="45.0"></div>' +
              '<div class="control-group"><label>Growth Constant kg <span><output id="v-kg5">1.20</output> μm/min</span></label><input type="range" id="s-kg5" min="0.20" max="3.00" step="0.10" value="1.20"></div>' +
              '<div class="control-group"><label>Nucleation Order b <span><output id="v-nord">2.5</output></span></label><input type="range" id="s-nord" min="1.0" max="4.0" step="0.5" value="2.5"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Linear Growth Rate G</div><div class="readout-value" id="r-grate">1.44 μm/min</div></div>' +
              '<div class="readout-card"><div class="readout-label">Dominant Size LD</div><div class="readout-value" id="r-ldom">194.4 μm</div></div>' +
              '<div class="readout-card"><div class="readout-label">Nucleation Rate B0</div><div class="readout-value" id="r-nrate">8.4e6 #/m³·s</div></div>' +
              '<div class="readout-card"><div class="readout-label">Product Quality</div><div class="readout-value" id="r-cqual">Coarse Free-Flowing</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp25" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp25"></p>',
      init: function(el) {
        var sS = el.querySelector('#s-ssat'), vS = el.querySelector('#v-ssat');
        var sTau = el.querySelector('#s-tau5'), vTau = el.querySelector('#v-tau5');
        var sKg = el.querySelector('#s-kg5'), vKg = el.querySelector('#v-kg5');
        var sNord = el.querySelector('#s-nord'), vNord = el.querySelector('#v-nord');
        var rGrate = el.querySelector('#r-grate'), rLdom = el.querySelector('#r-ldom');
        var rNrate = el.querySelector('#r-nrate'), rCqual = el.querySelector('#r-cqual');
        var svg = el.querySelector('#svg-sp25'), diag = el.querySelector('#diag-sp25');

        function update() {
          var S = parseFloat(sS.value); vS.textContent = f(S, 2);
          var tau = parseFloat(sTau.value); vTau.textContent = f(tau, 1);
          var kg = parseFloat(sKg.value); vKg.textContent = f(kg, 2);
          var b = parseFloat(sNord.value); vNord.textContent = f(b, 1);

          var sigma = S - 1.0; // relative supersaturation
          var G = kg * Math.pow(sigma, 1.0); // um/min
          var B0 = 5e7 * Math.pow(sigma, b); // #/m3 s
          var L_D = 3 * G * tau; // um dominant size in MSMPR

          rGrate.textContent = f(G, 2) + ' μm/min';
          rLdom.textContent = f(L_D, 1) + ' μm';
          rNrate.textContent = B0.toExponential(1) + ' #/m³·s';
          rCqual.textContent = L_D > 150 ? 'Coarse Free-Flowing' : (L_D > 60 ? 'Medium Crystals' : 'Fine / Fines Problem');

          // Population density exponential distribution n(L) = n0 * exp(-L / G*tau)
          var pts = [];
          for (var Ls = 0; Ls <= 500; Ls += 10) {
            var px = 80 + (Ls / 500) * 440;
            var frac = Math.exp(-Ls / Math.max(1, G * tau));
            var py = 160 - frac * 120;
            pts.push(f(px,1) + ',' + f(py,1));
          }

          var curX = 80 + (Math.min(500, L_D) / 500) * 440;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="40" width="440" height="120" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>' +
                          '<polyline points="' + pts.join(' ') + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<line x1="' + curX + '" y1="40" x2="' + curX + '" y2="160" stroke="#dc2626" stroke-width="2"/>' +
                          '<text x="' + curX + '" y="32" text-anchor="middle" font-size="11" font-weight="700" fill="#dc2626">LD = ' + f(L_D,0) + ' μm</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Population Balance n(L) in MSMPR (S = ' + f(S,2) + ')</text>' +
                          '<text x="300" y="185" text-anchor="middle" font-size="11" fill="#475569">G = ' + f(G,2) + ' μm/min | B0 = ' + B0.toExponential(1) + ' #/m³·s | ' + rCqual.textContent + '</text>';
          diag.textContent = 'Continuous MSMPR crystallization: Supersaturation ratio S = ' + f(S, 2) + '. Dominant product crystal size LD = 3·G·τ = ' + f(L_D, 1) + ' μm.';
        }
        [sS, sTau, sKg, sNord].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Constant-Pressure Cake Filtration (Ruth Equation)</h3><p class="lead">Simulate solid-liquid slurry filtration: calculate specific cake resistance α, filter medium resistance Rm, and wash cycle.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Filtration Pressure ΔP <span><output id="v-dp6">2.5</output> bar</span></label><input type="range" id="s-dp6" min="0.5" max="6.0" step="0.5" value="2.5"></div>' +
              '<div class="control-group"><label>Slurry Solids Conc c <span><output id="v-cslur">40</output> kg/m³</span></label><input type="range" id="s-cslur" min="10" max="120" step="5" value="40"></div>' +
              '<div class="control-group"><label>Filter Area A <span><output id="v-farea">2.0</output> m²</span></label><input type="range" id="s-farea" min="0.5" max="10.0" step="0.5" value="2.0"></div>' +
              '<div class="control-group"><label>Filtration Time t <span><output id="v-ftime">20.0</output> min</span></label><input type="range" id="s-ftime" min="2.0" max="60.0" step="2.0" value="20.0"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Filtrate Volume V</div><div class="readout-value" id="r-vfilt">3.12 m³</div></div>' +
              '<div class="readout-card"><div class="readout-label">Cake Thickness Lc</div><div class="readout-value" id="r-thick">41.6 mm</div></div>' +
              '<div class="readout-card"><div class="readout-label">Terminal Flow dV/dt</div><div class="readout-value" id="r-termflow">1.30 L/s</div></div>' +
              '<div class="readout-card"><div class="readout-label">Cake Solids Mass</div><div class="readout-value" id="r-smass">124.8 kg</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp26" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp26"></p>',
      init: function(el) {
        var sDp = el.querySelector('#s-dp6'), vDp = el.querySelector('#v-dp6');
        var sCslur = el.querySelector('#s-cslur'), vCslur = el.querySelector('#v-cslur');
        var sFarea = el.querySelector('#s-farea'), vFarea = el.querySelector('#v-farea');
        var sFtime = el.querySelector('#s-ftime'), vFtime = el.querySelector('#v-ftime');
        var rVfilt = el.querySelector('#r-vfilt'), rThick = el.querySelector('#r-thick');
        var rTermflow = el.querySelector('#r-termflow'), rSmass = el.querySelector('#r-smass');
        var svg = el.querySelector('#svg-sp26'), diag = el.querySelector('#diag-sp26');

        var mu = 0.001; // Pa s water
        var alpha = 1.8e11; // m/kg specific cake resistance
        var Rm = 5e10; // 1/m medium resistance

        function update() {
          var dP_bar = parseFloat(sDp.value); vDp.textContent = f(dP_bar, 1);
          var c = parseFloat(sCslur.value); vCslur.textContent = f(c, 0);
          var A = parseFloat(sFarea.value); vFarea.textContent = f(A, 1);
          var t_min = parseFloat(sFtime.value); vFtime.textContent = f(t_min, 1);

          var dP = dP_bar * 1e5; // Pa
          var t_sec = t_min * 60;

          // Ruth parabolic filtration: t / V = (mu * alpha * c) / (2 * A^2 * dP) * V + (mu * Rm) / (A * dP)
          var K_p = (mu * alpha * c) / (2 * A * A * dP);
          var B_p = (mu * Rm) / (A * dP);

          // Solve quadratic: K_p * V^2 + B_p * V - t_sec = 0
          var V = (-B_p + Math.sqrt(B_p * B_p + 4 * K_p * t_sec)) / (2 * K_p);
          var solids = V * c; // kg
          var Lc_mm = (solids / (1500 * A)) * 1000; // 1500 kg/m3 wet cake
          var dV_dt = (A * dP) / (mu * (alpha * c * (V / A) + Rm)) * 1000; // L/s

          rVfilt.textContent = f(V, 2) + ' m³';
          rThick.textContent = f(Lc_mm, 1) + ' mm';
          rTermflow.textContent = f(dV_dt, 2) + ' L/s';
          rSmass.textContent = f(solids, 1) + ' kg';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="180" y="40" width="240" height="120" fill="#f1f5f9" stroke="#334155" stroke-width="2" rx="4"/>' +
                          '<rect x="180" y="110" width="240" height="20" fill="#cbd5e1" stroke="#475569" stroke-width="1"/>' +
                          '<text x="300" y="125" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">Filter Medium Septum</text>' +
                          '<rect x="180" y="' + (110 - Math.min(60, Lc_mm)) + '" width="240" height="' + Math.min(60, Lc_mm) + '" fill="#ca8a04" fill-opacity="0.3" stroke="#ca8a04" stroke-width="1"/>' +
                          '<text x="300" y="' + (100 - Math.min(45, Lc_mm/2)) + '" text-anchor="middle" font-size="11" font-weight="700" fill="#854d0e">Filter Cake Lc=' + f(Lc_mm,1) + 'mm</text>' +
                          '<line x1="300" y1="130" x2="300" y2="180" stroke="#0284c7" stroke-width="3"/>' +
                          '<text x="300" y="195" text-anchor="middle" font-size="11" font-weight="700" fill="#0369a1">Filtrate V = ' + f(V,2) + ' m³ (Rate ' + f(dV_dt,2) + ' L/s)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Constant-Pressure Filtration (ΔP = ' + f(dP_bar,1) + ' bar)</text>';
          diag.textContent = 'Cake filtration: At ΔP = ' + f(dP_bar, 1) + ' bar over ' + f(t_min, 1) + ' min, filtrate volume = ' + f(V, 2) + ' m³ with a ' + f(Lc_mm, 1) + ' mm cake.';
        }
        [sDp, sCslur, sFarea, sFtime].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Rotary Drum Vacuum Filter Continuous Throughput</h3><p class="lead">Simulate industrial continuous filtration on rotating vacuum drums: evaluate cycle submergence and solids throughput.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Drum Speed N <span><output id="v-drumn">0.50</output> RPM</span></label><input type="range" id="s-drumn" min="0.10" max="2.50" step="0.05" value="0.50"></div>' +
              '<div class="control-group"><label>Submergence Fraction f <span><output id="v-subm">35.0</output> %</span></label><input type="range" id="s-subm" min="20.0" max="50.0" step="2.5" value="35.0"></div>' +
              '<div class="control-group"><label>Drum Area A <span><output id="v-darea">15.0</output> m²</span></label><input type="range" id="s-darea" min="5.0" max="50.0" step="2.5" value="15.0"></div>' +
              '<div class="control-group"><label>Vacuum Pressure ΔP <span><output id="v-vac">0.60</output> bar</span></label><input type="range" id="s-vac" min="0.20" max="0.85" step="0.05" value="0.60"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Cake Form Time tf</div><div class="readout-value" id="r-tform">42.0 s</div></div>' +
              '<div class="readout-card"><div class="readout-label">Drum Cycle Time tc</div><div class="readout-value" id="r-tcycl">120.0 s</div></div>' +
              '<div class="readout-card"><div class="readout-label">Solids Production</div><div class="readout-value" id="r-prod7">2.45 ton/h</div></div>' +
              '<div class="readout-card"><div class="readout-label">Discharge Thickness</div><div class="readout-value" id="r-dthick">14.2 mm</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp27" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp27"></p>',
      init: function(el) {
        var sN = el.querySelector('#s-drumn'), vN = el.querySelector('#v-drumn');
        var sSubm = el.querySelector('#s-subm'), vSubm = el.querySelector('#v-subm');
        var sA = el.querySelector('#s-darea'), vA = el.querySelector('#v-darea');
        var sVac = el.querySelector('#s-vac'), vVac = el.querySelector('#v-vac');
        var rTform = el.querySelector('#r-tform'), rTcycl = el.querySelector('#r-tcycl');
        var rProd = el.querySelector('#r-prod7'), rDthick = el.querySelector('#r-dthick');
        var svg = el.querySelector('#svg-sp27'), diag = el.querySelector('#diag-sp27');

        function update() {
          var N_rpm = parseFloat(sN.value); vN.textContent = f(N_rpm, 2);
          var subm = parseFloat(sSubm.value) / 100; vSubm.textContent = f(subm * 100, 1);
          var A = parseFloat(sA.value); vA.textContent = f(A, 1);
          var vac = parseFloat(sVac.value); vVac.textContent = f(vac, 2);

          var tc = 60 / Math.max(0.01, N_rpm); // cycle time seconds
          var tf = tc * subm; // formation time seconds

          // Production rate scales with sqrt(f * N * dP):
          var prod = 1.4 * Math.sqrt(subm * N_rpm * (vac / 0.5)) * (A / 10); // ton/h
          var Lc = (prod * 1000 / (N_rpm * 60 * A * 1.5)); // mm approx

          rTform.textContent = f(tf, 1) + ' s';
          rTcycl.textContent = f(tc, 1) + ' s';
          rProd.textContent = f(prod, 2) + ' ton/h';
          rDthick.textContent = f(Lc, 1) + ' mm';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<circle cx="300" cy="100" r="65" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>' +
                          '<path d="M 235 100 A 65 65 0 0 0 365 100 Z" fill="#ca8a04" fill-opacity="0.25"/>' +
                          '<rect x="210" y="90" width="180" height="50" fill="#bfdbfe" fill-opacity="0.3" stroke="#3b82f6" stroke-width="1"/>' +
                          '<text x="300" y="125" text-anchor="middle" font-size="11" font-weight="700" fill="#1e40af">Slurry Trough (' + f(subm*100,0) + '% subm)</text>' +
                          '<text x="300" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Rotary Drum (N=' + f(N_rpm,2) + ' RPM)</text>' +
                          '<line x1="365" y1="90" x2="420" y2="70" stroke="#ef4444" stroke-width="3"/>' +
                          '<text x="425" y="70" font-size="11" font-weight="700" fill="#dc2626">Knife Discharge (' + f(prod,2) + ' t/h)</text>' +
                          '<text x="300" y="24" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Continuous Vacuum Drum Filtration</text>';
          diag.textContent = 'Rotary drum throughput: Speed = ' + f(N_rpm, 2) + ' RPM (Cycle time = ' + f(tc, 1) + ' s). Solids cake discharge rate = ' + f(prod, 2) + ' ton/h.';
        }
        [sN, sSubm, sA, sVac].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Hybrid Membrane-Distillation Energy & Exergy Optimization</h3><p class="lead">Simulate integrated separation flowsheets: evaluate steam consumption reduction and thermodynamic exergy savings.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Azeotrope Feed Conc <span><output id="v-azfeed">85.0</output> wt%</span></label><input type="range" id="s-azfeed" min="70.0" max="95.0" step="1.0" value="85.0"></div>' +
              '<div class="control-group"><label>Membrane Cut Recovery <span><output id="v-mcut">60.0</output> %</span></label><input type="range" id="s-mcut" min="20.0" max="90.0" step="5.0" value="60.0"></div>' +
              '<div class="control-group"><label>Feed Throughput <span><output id="v-tfthroughput">15.0</output> ton/h</span></label><input type="range" id="s-tfthroughput" min="5.0" max="50.0" step="2.5" value="15.0"></div>' +
              '<div class="control-group"><label>Steam Cost <span><output id="v-scost">22.0</output> $/ton</span></label><input type="range" id="s-scost" min="10.0" max="45.0" step="1.0" value="22.0"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Standalone Column Duty</div><div class="readout-value" id="r-qstand">7.40 MW</div></div>' +
              '<div class="readout-card"><div class="readout-label">Hybrid Flowsheet Duty</div><div class="readout-value" id="r-qhyb">3.85 MW</div></div>' +
              '<div class="readout-card"><div class="readout-label">Thermal Energy Reduction</div><div class="readout-value" id="r-ereduc">48.0 %</div></div>' +
              '<div class="readout-card"><div class="readout-label">Annual Operating Savings</div><div class="readout-value" id="r-opcost">$492,000 /yr</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-sp28" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-sp28"></p>',
      init: function(el) {
        var sAz = el.querySelector('#s-azfeed'), vAz = el.querySelector('#v-azfeed');
        var sCut = el.querySelector('#s-mcut'), vCut = el.querySelector('#v-mcut');
        var sFeed = el.querySelector('#s-tfthroughput'), vFeed = el.querySelector('#v-tfthroughput');
        var sSc = el.querySelector('#s-scost'), vSc = el.querySelector('#v-scost');
        var rQstand = el.querySelector('#r-qstand'), rQhyb = el.querySelector('#r-qhyb');
        var rEreduc = el.querySelector('#r-ereduc'), rOpcost = el.querySelector('#r-opcost');
        var svg = el.querySelector('#svg-sp28'), diag = el.querySelector('#diag-sp28');

        function update() {
          var az = parseFloat(sAz.value); vAz.textContent = f(az, 1);
          var cut = parseFloat(sCut.value) / 100; vCut.textContent = f(cut * 100, 1);
          var feed = parseFloat(sFeed.value); vFeed.textContent = f(feed, 1);
          var sc = parseFloat(sSc.value); vSc.textContent = f(sc, 1);

          var qStand = feed * 0.49; // MW
          var qHyb = qStand * (1 - 0.70 * cut); // Membrane pre-concentrates
          var reduc = ((qStand - qHyb) / qStand) * 100;
          var steamSavedTons = (qStand - qHyb) * 3600 * 8000 / 2200; // tons steam / yr
          var savDollars = steamSavedTons * sc;

          rQstand.textContent = f(qStand, 2) + ' MW';
          rQhyb.textContent = f(qHyb, 2) + ' MW';
          rEreduc.textContent = f(reduc, 1) + ' %';
          rOpcost.textContent = '$' + f(savDollars, 0) + ' /yr';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="55" width="100" height="70" fill="#e0f2fe" stroke="#0284c7" stroke-width="2" rx="4"/>' +
                          '<text x="130" y="90" text-anchor="middle" font-size="11" font-weight="700" fill="#0369a1">Membrane Unit</text>' +
                          '<line x1="180" y1="90" x2="260" y2="90" stroke="#0284c7" stroke-width="3"/>' +
                          '<rect x="260" y="40" width="90" height="100" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="6"/>' +
                          '<text x="305" y="90" text-anchor="middle" font-size="11" font-weight="700" fill="#92400e">Distillation</text>' +
                          '<rect x="420" y="50" width="140" height="80" fill="#dcfce7" stroke="#16a34a" stroke-width="2" rx="6"/>' +
                          '<text x="490" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="#15803d">Energy Savings</text>' +
                          '<text x="490" y="105" text-anchor="middle" font-size="14" font-weight="800" fill="#16a34a">' + f(reduc,1) + '% Saved</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Hybrid Membrane-Distillation System</text>' +
                          '<text x="300" y="180" text-anchor="middle" font-size="11" fill="#475569">Reboiler Steam Reduced from ' + f(qStand,2) + ' MW to ' + f(qHyb,2) + ' MW (Savings: $' + f(savDollars,0) + '/yr)</text>';
          diag.textContent = 'Hybrid separation: Membrane dewatering pre-cut reduces reboiler duty by ' + f(reduc, 1) + '%, saving $' + f(savDollars, 0) + ' annually in utility steam.';
        }
        [sAz, sCut, sFeed, sSc].forEach(function(el) { el.addEventListener('input', update); });
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
