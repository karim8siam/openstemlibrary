# Append build_pdc_sims to build_cpe_b3_sims_full.py

pdc_code = '''
# =========================================================================
# 3. Process Dynamics and Control
# =========================================================================
def build_pdc_sims():
    return """/* Process Dynamics and Control Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Gravity-Drained Surge Tank (First-Order Dynamic Response)</h3><p class="lead">Simulate mass conservation, liquid head time constant τ = AR, and step input transitions.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Tank Area A <span><output id="v-area">2.5</output> m²</span></label><input type="range" id="s-area" min="0.5" max="6.0" step="0.5" value="2.5"></div>' +
              '<div class="control-group"><label>Valve Resistance R <span><output id="v-res">12.0</output> min/m²</span></label><input type="range" id="s-res" min="2.0" max="30.0" step="1.0" value="12.0"></div>' +
              '<div class="control-group"><label>Inflow Step ΔFin <span><output id="v-step">0.15</output> m³/min</span></label><input type="range" id="s-step" min="0.02" max="0.50" step="0.02" value="0.15"></div>' +
              '<div class="control-group"><label>Initial Height h0 <span><output id="v-h0">1.80</output> m</span></label><input type="range" id="s-h0" min="0.50" max="4.00" step="0.10" value="1.80"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Time Constant τ</span><span class="value" id="r-tau">0.0 min</span><span class="subtext">A · R parameter</span></div>' +
              '<div class="readout-card"><span class="label">Steady State Δh</span><span class="value" id="r-deltah">0.00 m</span><span class="subtext">ultimate height change</span></div>' +
              '<div class="readout-card"><span class="label">Final Height hss</span><span class="value" id="r-hss">0.00 m</span><span class="subtext">h0 + R · ΔFin</span></div>' +
              '<div class="readout-card"><span class="label">Settling Time</span><span class="value" id="r-settle">0.0 min</span><span class="subtext">4τ (98% response)</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdc-u1" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdc-u1"></div>',
      init: function(card) {
        var sArea = card.querySelector('#s-area'), vArea = card.querySelector('#v-area');
        var sRes = card.querySelector('#s-res'), vRes = card.querySelector('#v-res');
        var sStep = card.querySelector('#s-step'), vStep = card.querySelector('#v-step');
        var sH0 = card.querySelector('#s-h0'), vH0 = card.querySelector('#v-h0');
        var rTau = card.querySelector('#r-tau'), rDeltaH = card.querySelector('#r-deltah');
        var rHss = card.querySelector('#r-hss'), rSettle = card.querySelector('#r-settle');
        var svg = card.querySelector('#plot-pdc-u1'), diag = card.querySelector('#diag-pdc-u1');

        function update() {
          var A = parseFloat(sArea.value); vArea.textContent = f(A, 1);
          var R = parseFloat(sRes.value); vRes.textContent = f(R, 1);
          var dFin = parseFloat(sStep.value); vStep.textContent = f(dFin, 2);
          var h0 = parseFloat(sH0.value); vH0.textContent = f(h0, 2);

          var tau = A * R; // min
          var deltaH = dFin * R;
          var hss = h0 + deltaH;
          var settleTime = 4 * tau;

          rTau.textContent = f(tau, 1) + ' min';
          rDeltaH.textContent = f(deltaH, 2) + ' m';
          rHss.textContent = f(hss, 2) + ' m';
          rSettle.textContent = f(settleTime, 1) + ' min';

          var tMax = Math.max(60, settleTime * 1.3);
          var dPath = 'M 40 ' + (170 - (h0 / (hss * 1.25)) * 130).toFixed(1) + ' ';

          for (var t = 0; t <= tMax; t += tMax / 50) {
            var h_t = h0 + deltaH * (1 - Math.exp(-t / tau));
            var x_px = 40 + (t / tMax) * 520;
            var y_px = 170 - (h_t / (hss * 1.25)) * 130;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          var tau_x = 40 + (tau / tMax) * 520;
          var tau_y = 170 - ((h0 + 0.632 * deltaH) / (hss * 1.25)) * 130;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="' + (170 - (hss / (hss * 1.25)) * 130).toFixed(1) + '" x2="560" y2="' + (170 - (hss / (hss * 1.25)) * 130).toFixed(1) + '" stroke="#cbd5e1" stroke-dasharray="4"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#0284c7" stroke-width="3"/>' +
                          '<circle cx="' + tau_x.toFixed(1) + '" cy="' + tau_y.toFixed(1) + '" r="5" fill="#f59e0b"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Time (min)</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Liquid Height h(t) [m]</text>' +
                          '<text x="' + (tau_x + 8).toFixed(1) + '" y="' + (tau_y - 8).toFixed(1) + '" font-size="10" fill="#d97706" font-weight="700">63.2% at t = τ</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">First-Order Surge Tank Step Response (τ = ' + f(tau, 1) + ' min)</text>';
          diag.textContent = 'Process time constant τ = ' + f(tau, 1) + ' minutes. Liquid level rises from ' + f(h0, 2) + ' m to ' + f(hss, 2) + ' m following a ' + f(dFin, 2) + ' m³/min inflow step. Response reaches 63.2% of steady state at t = ' + f(tau, 1) + ' min and completes settling by t = ' + f(settleTime, 1) + ' min.';
        }
        [sArea, sRes, sStep, sH0].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Second-Order Underdamped / Overdamped Response</h3><p class="lead">Simulate damping ratio ζ, overshoot, decay ratio, and natural oscillation frequency ωn.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Damping Ratio ζ <span><output id="v-zeta">0.35</output></span></label><input type="range" id="s-zeta" min="0.05" max="2.00" step="0.05" value="0.35"></div>' +
              '<div class="control-group"><label>Natural Freq ωn <span><output id="v-wn">1.20</output> rad/s</span></label><input type="range" id="s-wn" min="0.20" max="3.00" step="0.10" value="1.20"></div>' +
              '<div class="control-group"><label>Process Gain K <span><output id="v-gain">1.00</output></span></label><input type="range" id="s-gain" min="0.50" max="2.00" step="0.10" value="1.00"></div>' +
              '<div class="control-group"><label>Step Size Δu <span><output id="v-step2">1.00</output></span></label><input type="range" id="s-step2" min="0.50" max="2.00" step="0.25" value="1.00"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Percent Overshoot</span><span class="value" id="r-os">0.0%</span><span class="subtext">peak above steady state</span></div>' +
              '<div class="readout-card"><span class="label">Decay Ratio</span><span class="value" id="r-decay">0.00</span><span class="subtext">successive peak ratio</span></div>' +
              '<div class="readout-card"><span class="label">Peak Time tp</span><span class="value" id="r-tp">0.0 s</span><span class="subtext">π / ωd</span></div>' +
              '<div class="readout-card"><span class="label">Response Nature</span><span class="value" id="r-nature">Underdamped</span><span class="subtext">ζ regime</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdc-u2" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdc-u2"></div>',
      init: function(card) {
        var sZeta = card.querySelector('#s-zeta'), vZeta = card.querySelector('#v-zeta');
        var sWn = card.querySelector('#s-wn'), vWn = card.querySelector('#v-wn');
        var sGain = card.querySelector('#s-gain'), vGain = card.querySelector('#v-gain');
        var sStep = card.querySelector('#s-step2'), vStep = card.querySelector('#v-step2');
        var rOS = card.querySelector('#r-os'), rDecay = card.querySelector('#r-decay');
        var rTp = card.querySelector('#r-tp'), rNature = card.querySelector('#r-nature');
        var svg = card.querySelector('#plot-pdc-u2'), diag = card.querySelector('#diag-pdc-u2');

        function update() {
          var zeta = parseFloat(sZeta.value); vZeta.textContent = f(zeta, 2);
          var wn = parseFloat(sWn.value); vWn.textContent = f(wn, 2);
          var K = parseFloat(sGain.value); vGain.textContent = f(K, 2);
          var du = parseFloat(sStep.value); vStep.textContent = f(du, 2);

          var y_ss = K * du;
          var os = 0, decay = 0, tp = 0;
          var nature = 'Critically Damped';

          if (zeta < 1.0) {
            nature = 'Underdamped (Oscillatory)';
            var wd = wn * Math.sqrt(1 - zeta * zeta);
            os = 100 * Math.exp(-Math.PI * zeta / Math.sqrt(1 - zeta * zeta));
            decay = Math.exp(-2 * Math.PI * zeta / Math.sqrt(1 - zeta * zeta));
            tp = Math.PI / wd;
          } else if (zeta > 1.0) {
            nature = 'Overdamped (Sluggish)';
            os = 0; decay = 0; tp = 0;
          }

          rOS.textContent = f(os, 1) + ' %';
          rDecay.textContent = f(decay, 3);
          rTp.textContent = tp > 0 ? f(tp, 2) + ' s' : 'N/A';
          rNature.textContent = nature;

          var tMax = Math.max(10, (5 / (zeta * wn)));
          var dPath = 'M 40 170 ';

          for (var t = 0; t <= tMax; t += tMax / 80) {
            var y_t = 0;
            if (zeta < 1.0) {
              var wd_i = wn * Math.sqrt(1 - zeta * zeta);
              var phi = Math.acos(zeta);
              y_t = y_ss * (1 - (Math.exp(-zeta * wn * t) / Math.sqrt(1 - zeta * zeta)) * Math.sin(wd_i * t + phi));
            } else if (Math.abs(zeta - 1.0) < 0.05) {
              y_t = y_ss * (1 - (1 + wn * t) * Math.exp(-wn * t));
            } else {
              var r1 = -zeta * wn + wn * Math.sqrt(zeta * zeta - 1);
              var r2 = -zeta * wn - wn * Math.sqrt(zeta * zeta - 1);
              y_t = y_ss * (1 - (r2 * Math.exp(r1 * t) - r1 * Math.exp(r2 * t)) / (r2 - r1));
            }
            var x_px = 40 + (t / tMax) * 520;
            var y_px = 170 - (y_t / (y_ss * 1.8)) * 140;
            y_px = Math.min(170, Math.max(20, y_px));
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          var ss_y = 170 - (y_ss / (y_ss * 1.8)) * 140;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="' + ss_y.toFixed(1) + '" x2="560" y2="' + ss_y.toFixed(1) + '" stroke="#cbd5e1" stroke-dasharray="4"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Time t (s)</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Response y(t)</text>' +
                          '<text x="560" y="' + (ss_y - 6).toFixed(1) + '" text-anchor="end" font-size="10" fill="#64748b">Steady State (' + f(y_ss, 2) + ')</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Second-Order Step Response (ζ = ' + f(zeta, 2) + ', OS = ' + f(os, 1) + '%)</text>';
          diag.textContent = 'System is ' + nature + '. Damping ratio ζ = ' + f(zeta, 2) + ' yields ' + (zeta < 1 ? f(os, 1) + '% overshoot with decay ratio ' + f(decay, 3) + ' and first peak at tp = ' + f(tp, 2) + ' s.' : 'monotonic non-oscillatory approach to steady state.');
        }
        [sZeta, sWn, sGain, sStep].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Feedback Loop Stability & Closed-Loop Poles</h3><p class="lead">Simulate proportional gain Kc, dead-time θ, and determine Routh-Hurwitz ultimate gain Kcu.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Controller Gain Kc <span><output id="v-kc">2.50</output></span></label><input type="range" id="s-kc" min="0.20" max="15.00" step="0.20" value="2.50"></div>' +
              '<div class="control-group"><label>Process Gain Kp <span><output id="v-kp">1.00</output></span></label><input type="range" id="s-kp" min="0.50" max="3.00" step="0.10" value="1.00"></div>' +
              '<div class="control-group"><label>Dead Time θ <span><output id="v-theta3">1.5</output> min</span></label><input type="range" id="s-theta3" min="0.2" max="5.0" step="0.2" value="1.5"></div>' +
              '<div class="control-group"><label>Time Constant τ <span><output id="v-tau3">4.0</output> min</span></label><input type="range" id="s-tau3" min="1.0" max="10.0" step="0.5" value="4.0"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Loop Stability</span><span class="value" id="r-stab">Stable</span><span class="subtext">closed-loop condition</span></div>' +
              '<div class="readout-card"><span class="label">Ultimate Gain Kcu</span><span class="value" id="r-kcu">0.00</span><span class="subtext">stability limit</span></div>' +
              '<div class="readout-card"><span class="label">Gain Margin</span><span class="value" id="r-gm">0.00</span><span class="subtext">Kcu / Kc</span></div>' +
              '<div class="readout-card"><span class="label">Dead-Time Ratio</span><span class="value" id="r-dtr">0.00</span><span class="subtext">θ / τ controllability</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdc-u3" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdc-u3"></div>',
      init: function(card) {
        var sKc = card.querySelector('#s-kc'), vKc = card.querySelector('#v-kc');
        var sKp = card.querySelector('#s-kp'), vKp = card.querySelector('#v-kp');
        var sTh = card.querySelector('#s-theta3'), vTh = card.querySelector('#v-theta3');
        var sTau = card.querySelector('#s-tau3'), vTau = card.querySelector('#v-tau3');
        var rStab = card.querySelector('#r-stab'), rKcu = card.querySelector('#r-kcu');
        var rGm = card.querySelector('#r-gm'), rDtr = card.querySelector('#r-dtr');
        var svg = card.querySelector('#plot-pdc-u3'), diag = card.querySelector('#diag-pdc-u3');

        function update() {
          var Kc = parseFloat(sKc.value); vKc.textContent = f(Kc, 2);
          var Kp = parseFloat(sKp.value); vKp.textContent = f(Kp, 2);
          var theta = parseFloat(sTh.value); vTh.textContent = f(theta, 1);
          var tau = parseFloat(sTau.value); vTau.textContent = f(tau, 1);

          // Pade 1st order approx: Kcu ≈ (tau / (Kp * theta)) + 0.5 / Kp
          var Kcu = (tau / (Kp * theta)) + (0.5 / Kp);
          var GM = Kcu / Kc;
          var dtRatio = theta / tau;
          var isStable = Kc < Kcu;

          rStab.textContent = isStable ? (GM > 1.7 ? 'Robustly Stable' : 'Marginally Stable') : 'UNSTABLE (Runaway)';
          rStab.style.color = isStable ? (GM > 1.7 ? '#15803d' : '#d97706') : '#dc2626';
          rKcu.textContent = f(Kcu, 2);
          rGm.textContent = f(GM, 2);
          rDtr.textContent = f(dtRatio, 2);

          // Plot transient closed loop response showing stable or growing oscillation
          var dPath = 'M 40 100 ';
          var tMax = 30;
          for (var t = 0; t <= tMax; t += 0.5) {
            var decayRate = (Kcu - Kc) / (2 * tau);
            var freq = Math.PI / (theta + 0.5 * tau);
            var amp = 40 * Math.exp(-decayRate * t);
            amp = Math.min(65, Math.max(-65, amp));
            var y_val = 100 - amp * Math.sin(freq * t);
            var x_px = 40 + (t / tMax) * 520;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_val.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="100" x2="560" y2="100" stroke="#94a3b8" stroke-dasharray="4"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="' + (isStable ? '#059669' : '#dc2626') + '" stroke-width="3"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Time (min)</text>' +
                          '<text x="50" y="35" font-size="11" fill="#64748b">Controlled Variable Deviation e(t)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Feedback Loop Stability (Gain Margin = ' + f(GM, 2) + ')</text>';
          diag.textContent = 'Ultimate gain Kcu is ' + f(Kcu, 2) + '. With current Kc = ' + f(Kc, 2) + ', the loop is ' + (isStable ? 'stable with gain margin ' + f(GM, 2) : 'unstable due to phase lag and excessive proportional gain') + '. Dead-time ratio θ/τ = ' + f(dtRatio, 2) + ' (' + (dtRatio > 0.5 ? 'difficult dead-time dominated process' : 'well-conditioned lag-dominated loop') + ').';
        }
        [sKc, sKp, sTh, sTau].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>PID Controller Sizing & Loop Tuning</h3><p class="lead">Simulate Proportional-Integral-Derivative setpoint tracking and disturbance rejection.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Gain Kc <span><output id="v-pidkc">1.80</output></span></label><input type="range" id="s-pidkc" min="0.20" max="6.00" step="0.20" value="1.80"></div>' +
              '<div class="control-group"><label>Integral Time τI <span><output id="v-taui">4.0</output> min</span></label><input type="range" id="s-taui" min="0.5" max="15.0" step="0.5" value="4.0"></div>' +
              '<div class="control-group"><label>Derivative Time τD <span><output id="v-taud">0.80</output> min</span></label><input type="range" id="s-taud" min="0.00" max="3.00" step="0.10" value="0.80"></div>' +
              '<div class="control-group"><label>Tuning Rule <span><output id="v-tune">Custom</output></span></label><input type="range" id="s-tune" min="1" max="3" step="1" value="1"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Steady State Error</span><span class="value" id="r-sse">0.00%</span><span class="subtext">integral action offset</span></div>' +
              '<div class="readout-card"><span class="label">Settling Time</span><span class="value" id="r-pidset">0.0 min</span><span class="subtext">time inside ±2% band</span></div>' +
              '<div class="readout-card"><span class="label">IAE Performance</span><span class="value" id="r-iae">0.0</span><span class="subtext">integrated absolute error</span></div>' +
              '<div class="readout-card"><span class="label">Control Effort</span><span class="value" id="r-effort">Normal</span><span class="subtext">valve wear index</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdc-u4" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdc-u4"></div>',
      init: function(card) {
        var sKc = card.querySelector('#s-pidkc'), vKc = card.querySelector('#v-pidkc');
        var sTi = card.querySelector('#s-taui'), vTi = card.querySelector('#v-taui');
        var sTd = card.querySelector('#s-taud'), vTd = card.querySelector('#v-taud');
        var sTune = card.querySelector('#s-tune'), vTune = card.querySelector('#v-tune');
        var rSse = card.querySelector('#r-sse'), rSet = card.querySelector('#r-pidset');
        var rIae = card.querySelector('#r-iae'), rEff = card.querySelector('#r-effort');
        var svg = card.querySelector('#plot-pdc-u4'), diag = card.querySelector('#diag-pdc-u4');

        function update() {
          var Kc = parseFloat(sKc.value); vKc.textContent = f(Kc, 2);
          var Ti = parseFloat(sTi.value); vTi.textContent = f(Ti, 1);
          var Td = parseFloat(sTd.value); vTd.textContent = f(Td, 2);
          var tuneRule = parseInt(sTune.value, 10);
          vTune.textContent = tuneRule === 1 ? 'Custom' : (tuneRule === 2 ? 'Ziegler-Nichols' : 'Cohen-Coon');

          var sse = Ti < 50 ? 0.0 : 10.0;
          var damping = (Kc * Ti) / (1 + Td * 2);
          var settle = Math.max(2.0, Ti * 2.2 / (1 + Kc * 0.3));
          var iae = (1 / Kc) * 5 + Ti * 0.8 + (Td > 1.5 ? Td * 4 : 0);

          rSse.textContent = f(sse, 1) + ' %';
          rSet.textContent = f(settle, 1) + ' min';
          rIae.textContent = f(iae, 1);
          rEff.textContent = Td > 1.5 ? 'Excessive (Jitter)' : (Kc > 4 ? 'Aggressive' : 'Smooth');

          var dPath = 'M 40 170 ';
          for (var t = 0; t <= 20; t += 0.4) {
            // PV response to step from 0 to 1
            var y_t = 1.0 - Math.exp(-t / (Ti * 0.4 + 0.5)) * (Math.cos(2 * t / Math.sqrt(Ti + 0.1)) + (0.3 / (Kc + 0.1)) * Math.sin(2 * t));
            var x_px = 40 + (t / 20.0) * 520;
            var y_px = 170 - (Math.min(1.5, Math.max(0, y_t)) / 1.5) * 130;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="' + (170 - (1.0 / 1.5) * 130).toFixed(1) + '" x2="560" y2="' + (170 - (1.0 / 1.5) * 130).toFixed(1) + '" stroke="#cbd5e1" stroke-dasharray="4"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<text x="560" y="' + (165 - (1.0 / 1.5) * 130).toFixed(1) + '" text-anchor="end" font-size="10" fill="#64748b">Setpoint = 1.0</text>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Time (min)</text>' +
                          '<text x="50" y="35" font-size="11" fill="#64748b">Process Variable PV(t)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">PID Response (Kc = ' + f(Kc, 2) + ', τI = ' + f(Ti, 1) + 'm, τD = ' + f(Td, 2) + 'm)</text>';
          diag.textContent = 'PID controller eliminates steady-state offset via reset action (τI = ' + f(Ti, 1) + ' min). Derivative action τD = ' + f(Td, 2) + ' min provides phase lead anticipation. Settling time is ' + f(settle, 1) + ' min.';
        }
        [sKc, sTi, sTd, sTune].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Control Valve Sizing & Installed Flow Characteristic</h3><p class="lead">Simulate valve authority N = ΔPv / ΔPtot and inherent vs installed flow curves.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Valve Authority N <span><output id="v-auth">0.35</output></span></label><input type="range" id="s-auth" min="0.05" max="0.95" step="0.05" value="0.35"></div>' +
              '<div class="control-group"><label>Trim Characteristic <span><output id="v-trim">Equal Percentage</output></span></label><input type="range" id="s-trim" min="1" max="2" step="1" value="2"></div>' +
              '<div class="control-group"><label>Rangeability R <span><output id="v-range">50</output></span></label><input type="range" id="s-range" min="20" max="80" step="10" value="50"></div>' +
              '<div class="control-group"><label>Valve Travel x <span><output id="v-trav">50%</output></span></label><input type="range" id="s-trav" min="0" max="100" step="5" value="50"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Relative Flow q/qmax</span><span class="value" id="r-flow">0.00</span><span class="subtext">installed fraction</span></div>' +
              '<div class="readout-card"><span class="label">Installed Linearity</span><span class="value" id="r-lin">Good</span><span class="subtext">slope stability</span></div>' +
              '<div class="readout-card"><span class="label">Distortion Level</span><span class="value" id="r-dist">Moderate</span><span class="subtext">loss of authority</span></div>' +
              '<div class="readout-card"><span class="label">Recommended Trim</span><span class="value" id="r-rectrim">Equal %</span><span class="subtext">for current N</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdc-u5" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdc-u5"></div>',
      init: function(card) {
        var sAuth = card.querySelector('#s-auth'), vAuth = card.querySelector('#v-auth');
        var sTrim = card.querySelector('#s-trim'), vTrim = card.querySelector('#v-trim');
        var sRange = card.querySelector('#s-range'), vRange = card.querySelector('#v-range');
        var sTrav = card.querySelector('#s-trav'), vTrav = card.querySelector('#v-trav');
        var rFlow = card.querySelector('#r-flow'), rLin = card.querySelector('#r-lin');
        var rDist = card.querySelector('#r-dist'), rRec = card.querySelector('#r-rectrim');
        var svg = card.querySelector('#plot-pdc-u5'), diag = card.querySelector('#diag-pdc-u5');

        function update() {
          var N = parseFloat(sAuth.value); vAuth.textContent = f(N, 2);
          var isEqualPct = parseInt(sTrim.value, 10) === 2;
          vTrim.textContent = isEqualPct ? 'Equal Percentage' : 'Linear Trim';
          var R = parseFloat(sRange.value); vRange.textContent = f(R, 0);
          var travel = parseFloat(sTrav.value) / 100; vTrav.textContent = f(travel * 100, 0) + '%';

          // Inherent characteristic f(x)
          function fx(x) {
            if (isEqualPct) return Math.pow(R, x - 1);
            return x;
          }

          // Installed characteristic: q/qmax = f(x) / sqrt(N + (1 - N) * [f(x)]^2)
          function qInstalled(x) {
            var f_val = fx(x);
            var den = Math.sqrt(N + (1 - N) * f_val * f_val);
            return f_val / den;
          }

          var curFlow = qInstalled(travel);
          rFlow.textContent = f(curFlow, 2);
          rLin.textContent = N > 0.4 ? 'Highly Linear' : (N > 0.2 ? 'Acceptable' : 'Severely Distorted');
          rDist.textContent = N < 0.2 ? 'High (Quick-Opening)' : (N > 0.6 ? 'Minimal' : 'Moderate');
          rRec.textContent = N < 0.5 ? 'Equal % Trim' : 'Linear Trim';

          // SVG plot: Inherent (dashed) vs Installed (solid)
          var pathInherent = 'M 40 170 ';
          var pathInstalled = 'M 40 170 ';

          for (var x = 0; x <= 1.0; x += 0.05) {
            var f_inh = fx(x);
            var f_inst = qInstalled(x);
            var x_px = 40 + x * 520;
            var y_inh = 170 - f_inh * 140;
            var y_inst = 170 - f_inst * 140;
            pathInherent += 'L ' + x_px.toFixed(1) + ' ' + y_inh.toFixed(1) + ' ';
            pathInstalled += 'L ' + x_px.toFixed(1) + ' ' + y_inst.toFixed(1) + ' ';
          }

          var cur_x = 40 + travel * 520;
          var cur_y = 170 - curFlow * 140;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + pathInherent + '" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4"/>' +
                          '<path d="' + pathInstalled + '" fill="none" stroke="#059669" stroke-width="3"/>' +
                          '<circle cx="' + cur_x.toFixed(1) + '" cy="' + cur_y.toFixed(1) + '" r="6" fill="#047857" stroke="#fff" stroke-width="2"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Valve Lift / Travel x (0 to 100%)</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Installed Flow q / qmax</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Valve Flow Characteristics (Authority N = ' + f(N, 2) + ')</text>';
          diag.textContent = 'At valve authority N = ' + f(N, 2) + ', piping line loss absorbs ' + f((1 - N) * 100, 0) + '% of system head. ' + (isEqualPct ? 'The equal-percentage trim compensates for pipeline pressure drop, yielding a nearly linear installed characteristic.' : 'Linear trim is distorted toward quick-opening behavior, degrading low-flow control sensitivity.');
        }
        [sAuth, sTrim, sRange, sTrav].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Feedforward + Feedback Disturbance Rejection</h3><p class="lead">Simulate feedforward lead-lag compensation cancelling upstream disturbances before error forms.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Disturbance Step d <span><output id="v-dist">20%</output></span></label><input type="range" id="s-dist" min="5" max="50" step="5" value="20"></div>' +
              '<div class="control-group"><label>Feedforward Status <span><output id="v-ffstat">FF Active</output></span></label><input type="range" id="s-ffstat" min="0" max="1" step="1" value="1"></div>' +
              '<div class="control-group"><label>FF Lead/Lag Match <span><output id="v-match">Perfect (1.0)</output></span></label><input type="range" id="s-match" min="0.5" max="1.5" step="0.1" value="1.0"></div>' +
              '<div class="control-group"><label>Feedback Gain Kc <span><output id="v-ffkc">1.50</output></span></label><input type="range" id="s-ffkc" min="0.50" max="4.00" step="0.25" value="1.50"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Max Deviation</span><span class="value" id="r-maxdev">0.0%</span><span class="subtext">peak PV excursion</span></div>' +
              '<div class="readout-card"><span class="label">Rejection Time</span><span class="value" id="r-rejtime">0.0 s</span><span class="subtext">recovery to ±1%</span></div>' +
              '<div class="readout-card"><span class="label">IAE Deficit</span><span class="value" id="r-ffiae">0.0</span><span class="subtext">integrated disturbance area</span></div>' +
              '<div class="readout-card"><span class="label">Disturbance Mode</span><span class="value" id="r-ffmode">FF Cancelled</span><span class="subtext">control strategy</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdc-u6" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdc-u6"></div>',
      init: function(card) {
        var sDist = card.querySelector('#s-dist'), vDist = card.querySelector('#v-dist');
        var sFF = card.querySelector('#s-ffstat'), vFF = card.querySelector('#v-ffstat');
        var sMatch = card.querySelector('#s-match'), vMatch = card.querySelector('#v-match');
        var sKc = card.querySelector('#s-ffkc'), vKc = card.querySelector('#v-ffkc');
        var rDev = card.querySelector('#r-maxdev'), rTime = card.querySelector('#r-rejtime');
        var rIae = card.querySelector('#r-ffiae'), rMode = card.querySelector('#r-ffmode');
        var svg = card.querySelector('#plot-pdc-u6'), diag = card.querySelector('#diag-pdc-u6');

        function update() {
          var dist = parseFloat(sDist.value); vDist.textContent = f(dist, 0) + '%';
          var ffOn = parseInt(sFF.value, 10) === 1; vFF.textContent = ffOn ? 'FF Active' : 'Feedback Only';
          var match = parseFloat(sMatch.value); vMatch.textContent = f(match, 1);
          var Kc = parseFloat(sKc.value); vKc.textContent = f(Kc, 2);

          var maxDev = ffOn ? Math.abs(1.0 - match) * dist * 0.45 : dist * 0.85;
          var rejTime = ffOn ? (Math.abs(1.0 - match) < 0.1 ? 0.5 : 3.0) : 12.0 / Kc;
          var iae = ffOn ? maxDev * rejTime * 0.5 : maxDev * 6.0;

          rDev.textContent = f(maxDev, 1) + ' %';
          rTime.textContent = f(rejTime, 1) + ' min';
          rIae.textContent = f(iae, 1);
          rMode.textContent = ffOn ? (Math.abs(1 - match) < 0.1 ? 'Near-Perfect Cancellation' : 'Imperfect FF Match') : 'Feedback Lag Dip';

          var dPath = 'M 40 100 ';
          for (var t = 0; t <= 20; t += 0.4) {
            var y_t = 0;
            if (ffOn) {
              y_t = (1.0 - match) * dist * 0.45 * Math.exp(-t / 2.0) * Math.sin(t * 1.5);
            } else {
              y_t = -dist * 0.85 * Math.exp(-t * Kc * 0.25) * Math.sin(t * 0.8);
            }
            var x_px = 40 + (t / 20.0) * 520;
            var y_px = 100 - (y_t / 30.0) * 70;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="100" x2="560" y2="100" stroke="#94a3b8" stroke-dasharray="4"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="' + (ffOn ? '#059669' : '#dc2626') + '" stroke-width="3"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Time (min)</text>' +
                          '<text x="50" y="35" font-size="11" fill="#64748b">Process Variable Deviation ΔPV</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Disturbance Rejection: ' + (ffOn ? 'Feedforward Active' : 'Feedback Only (Large Deviation)') + '</text>';
          diag.textContent = ffOn ? ('Feedforward action preemptively adjusts the manipulated variable. Peak deviation is constrained to ' + f(maxDev, 1) + '% (vs ' + f(dist * 0.85, 1) + '% under feedback alone).') : 'Feedback only waits for an error to develop in PV before taking corrective action, resulting in a large transient excursion.';
        }
        [sDist, sFF, sMatch, sKc].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Digital Control Sampling & Anti-Aliasing (Nyquist Criterion)</h3><p class="lead">Simulate sampling period Δt, signal reconstruction, and aliasing in discrete digital control.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Sampling Period Δt <span><output id="v-dt">0.10</output> s</span></label><input type="range" id="s-dt" min="0.02" max="0.80" step="0.02" value="0.10"></div>' +
              '<div class="control-group"><label>Signal Freq fsig <span><output id="v-fsig">1.50</output> Hz</span></label><input type="range" id="s-fsig" min="0.50" max="5.00" step="0.25" value="1.50"></div>' +
              '<div class="control-group"><label>Anti-Alias Filter <span><output id="v-filter">Active (Butterworth)</output></span></label><input type="range" id="s-filter" min="0" max="1" step="1" value="1"></div>' +
              '<div class="control-group"><label>Digital Delay θd <span><output id="v-delay">0.05</output> s</span></label><input type="range" id="s-delay" min="0.01" max="0.40" step="0.01" value="0.05"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Sampling Freq fs</span><span class="value" id="r-fs">10.0 Hz</span><span class="subtext">1 / Δt</span></div>' +
              '<div class="readout-card"><span class="label">Nyquist Limit fn</span><span class="value" id="r-fn">5.0 Hz</span><span class="subtext">fs / 2 boundary</span></div>' +
              '<div class="readout-card"><span class="label">Aliasing Status</span><span class="value" id="r-alias">Clean</span><span class="subtext">fsig < fn check</span></div>' +
              '<div class="readout-card"><span class="label">Effective Delay</span><span class="value" id="r-effdel">0.05 s</span><span class="subtext">Δt / 2 phase lag</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdc-u7" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdc-u7"></div>',
      init: function(card) {
        var sDt = card.querySelector('#s-dt'), vDt = card.querySelector('#v-dt');
        var sFsig = card.querySelector('#s-fsig'), vFsig = card.querySelector('#v-fsig');
        var sFilt = card.querySelector('#s-filter'), vFilt = card.querySelector('#v-filter');
        var sDel = card.querySelector('#s-delay'), vDel = card.querySelector('#v-delay');
        var rFs = card.querySelector('#r-fs'), rFn = card.querySelector('#r-fn');
        var rAlias = card.querySelector('#r-alias'), rEff = card.querySelector('#r-effdel');
        var svg = card.querySelector('#plot-pdc-u7'), diag = card.querySelector('#diag-pdc-u7');

        function update() {
          var dt = parseFloat(sDt.value); vDt.textContent = f(dt, 2);
          var fsig = parseFloat(sFsig.value); vFsig.textContent = f(fsig, 2);
          var hasFilter = parseInt(sFilt.value, 10) === 1;
          vFilt.textContent = hasFilter ? 'Active (Butterworth)' : 'No Filter (Bypass)';
          var delay = dt / 2.0; vDel.textContent = f(delay, 2);

          var fs = 1.0 / dt;
          var fn = fs / 2.0;
          var isAliased = fsig > fn && !hasFilter;

          rFs.textContent = f(fs, 1) + ' Hz';
          rFn.textContent = f(fn, 1) + ' Hz';
          rAlias.textContent = isAliased ? 'ALIASED (Ghost Frequency)' : (hasFilter && fsig > fn ? 'Filtered Out' : 'Clean Signal');
          rAlias.style.color = isAliased ? '#dc2626' : '#15803d';
          rEff.textContent = f(delay, 3) + ' s';

          // SVG plot continuous signal vs discrete samples
          var pathCont = 'M 40 ';
          var pointsSample = '';
          for (var t = 0; t <= 2.0; t += 0.01) {
            var val = Math.sin(2 * Math.PI * fsig * t);
            var x_px = 40 + (t / 2.0) * 520;
            var y_px = 100 - val * 65;
            if (t === 0) pathCont += y_px.toFixed(1) + ' ';
            else pathCont += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          for (var ts = 0; ts <= 2.0; ts += dt) {
            var val_s = hasFilter && fsig > fn ? 0 : Math.sin(2 * Math.PI * fsig * ts);
            var xs_px = 40 + (ts / 2.0) * 520;
            var ys_px = 100 - val_s * 65;
            pointsSample += '<circle cx="' + xs_px.toFixed(1) + '" cy="' + ys_px.toFixed(1) + '" r="4" fill="#ef4444"/>';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="100" x2="560" y2="100" stroke="#94a3b8" stroke-dasharray="4"/>' +
                          '<path d="' + pathCont + '" fill="none" stroke="#94a3b8" stroke-width="1.5"/>' +
                          pointsSample +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Time (s)</text>' +
                          '<text x="50" y="35" font-size="11" fill="#64748b">Continuous Wave vs. Discrete Samples</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Nyquist Sampling: fs = ' + f(fs, 1) + ' Hz (Limit: ' + f(fn, 1) + ' Hz)</text>';
          diag.textContent = 'Sampling rate fs = ' + f(fs, 1) + ' Hz defines a Nyquist folding boundary at ' + f(fn, 1) + ' Hz. ' + (isAliased ? 'CRITICAL: Signal frequency exceeds Nyquist limit without filtering; high-frequency content folds back into low frequencies creating false control errors.' : 'Signal satisfies Shannon-Nyquist sampling criterion; zero-order hold introduces Δt/2 = ' + f(delay, 3) + ' s of additional phase delay.');
        }
        [sDt, sFsig, sFilt, sDel].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Cascade Temperature-to-Flow Reactor Control</h3><p class="lead">Simulate master-slave cascade architecture isolating utility pressure fluctuations.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Reactor Temp SP <span><output id="v-tsp">365</output> K</span></label><input type="range" id="s-tsp" min="320" max="420" step="5" value="365"></div>' +
              '<div class="control-group"><label>Utility Pressure Spike <span><output id="v-spike">30%</output></span></label><input type="range" id="s-spike" min="0" max="60" step="5" value="30"></div>' +
              '<div class="control-group"><label>Control Mode <span><output id="v-cmode">Cascade (Master+Slave)</output></span></label><input type="range" id="s-cmode" min="1" max="2" step="1" value="2"></div>' +
              '<div class="control-group"><label>Slave Loop Speed <span><output id="v-sspeed">5× Faster</output></span></label><input type="range" id="s-sspeed" min="2" max="10" step="1" value="5"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Temp Excursion</span><span class="value" id="r-tempex">0.0 K</span><span class="subtext">peak reactor deviation</span></div>' +
              '<div class="readout-card"><span class="label">Cooling Water Flow</span><span class="value" id="r-cwflow">0.0 L/s</span><span class="subtext">manipulated variable</span></div>' +
              '<div class="readout-card"><span class="label">Recovery Time</span><span class="value" id="r-rect">0.0 min</span><span class="subtext">time to stabilize SP</span></div>' +
              '<div class="readout-card"><span class="label">Architecture</span><span class="value" id="r-arch">TIC -> FIC</span><span class="subtext">hierarchical loops</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdc-u8" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdc-u8"></div>',
      init: function(card) {
        var sTsp = card.querySelector('#s-tsp'), vTsp = card.querySelector('#v-tsp');
        var sSpike = card.querySelector('#s-spike'), vSpike = card.querySelector('#v-spike');
        var sMode = card.querySelector('#s-cmode'), vMode = card.querySelector('#v-cmode');
        var sSpeed = card.querySelector('#s-sspeed'), vSpeed = card.querySelector('#v-sspeed');
        var rTemp = card.querySelector('#r-tempex'), rFlow = card.querySelector('#r-cwflow');
        var rRec = card.querySelector('#r-rect'), rArch = card.querySelector('#r-arch');
        var svg = card.querySelector('#plot-pdc-u8'), diag = card.querySelector('#diag-pdc-u8');

        function update() {
          var Tsp = parseFloat(sTsp.value); vTsp.textContent = f(Tsp, 0);
          var spike = parseFloat(sSpike.value); vSpike.textContent = f(spike, 0) + '%';
          var isCascade = parseInt(sMode.value, 10) === 2;
          vMode.textContent = isCascade ? 'Cascade (Master+Slave)' : 'Single Loop Feedback';
          var speed = parseInt(sSpeed.value, 10); vSpeed.textContent = speed + '× Faster';

          var tempExcursion = isCascade ? (spike / 100.0) * (6.0 / speed) : (spike / 100.0) * 14.0;
          var cwFlow = 12.5 + (Tsp - 320) * 0.15;
          var recTime = isCascade ? 1.5 : 8.5;

          rTemp.textContent = f(tempExcursion, 1) + ' K';
          rFlow.textContent = f(cwFlow, 1) + ' L/s';
          rRec.textContent = f(recTime, 1) + ' min';
          rArch.textContent = isCascade ? 'TIC (Master) -> FIC (Slave)' : 'Direct Single TIC -> Valve';

          // SVG plot reactor core temperature
          var dPath = 'M 40 ' + (170 - ((Tsp - 300) / 140) * 130).toFixed(1) + ' ';
          for (var t = 0; t <= 15; t += 0.3) {
            var T_t = Tsp;
            if (t > 2.0) {
              var dt_t = t - 2.0;
              if (isCascade) {
                T_t = Tsp + tempExcursion * Math.exp(-dt_t * 1.8) * Math.sin(dt_t * 2.5);
              } else {
                T_t = Tsp + tempExcursion * Math.exp(-dt_t * 0.45) * Math.sin(dt_t * 1.0);
              }
            }
            var x_px = 40 + (t / 15.0) * 520;
            var y_px = 170 - ((T_t - 300) / 140) * 130;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="' + (170 - ((Tsp - 300) / 140) * 130).toFixed(1) + '" x2="560" y2="' + (170 - ((Tsp - 300) / 140) * 130).toFixed(1) + '" stroke="#cbd5e1" stroke-dasharray="4"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="' + (isCascade ? '#059669' : '#dc2626') + '" stroke-width="3"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Time (min)</text>' +
                          '<text x="50" y="35" font-size="11" fill="#64748b">Reactor Temperature T (K)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Cascade Control: ' + (isCascade ? 'Rapid Slave FIC Rejection' : 'Single Loop Severe Sluggish Drift') + '</text>';
          diag.textContent = isCascade ? ('The fast slave flow controller (FIC) catches supply water pressure fluctuations inside the jacket before they can perturb reactor bulk temperature. Peak deviation is only ' + f(tempExcursion, 1) + ' K.') : ('Under single-loop control, water pressure drops go unmeasured until core reactor temperature drifts upward by ' + f(tempExcursion, 1) + ' K, taking ' + f(recTime, 1) + ' min to recover.');
        }
        [sTsp, sSpike, sMode, sSpeed].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    }
  ];
""" + get_engine_footer(8)
'''

with open('tooling/build_cpe_b3_sims_full.py', 'a') as f:
    f.write(pdc_code)
print("Added build_pdc_sims!")
