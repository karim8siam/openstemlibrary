/* Civil Engineering Statics Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n) { return Number.isFinite(n) ? n.toFixed(3) : 'not defined'; }
  function line(a, b, c, d, color) { color = color || '#21697b'; return '<line x1="' + a + '" y1="' + b + '" x2="' + c + '" y2="' + d + '" stroke="' + color + '" stroke-width="3"/>'; }
  function text(x, y, t) { return '<text x="' + x + '" y="' + y + '" font-size="12" fill="#1e293b">' + t + '</text>'; }

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    kind: 'trapezoid',
    html: "<div class=\\\"sim-header\\\"><span class=\\\"badge\\\">Model 01 \u00b7 Unit 1</span><h3>Distributed Load Resultant</h3><p>Equilibrium reduction of trapezoidal distributed line loads into a single resultant force and its centroidal line of action.</p></div><section class=\\\"sim-controls\\\"><label class=\"control\">Loaded length L (m): <strong id=\"v_L\">8</strong><input id=\"L\" type=\"range\" min=\"2\" max=\"20\" step=\"0.5\" value=\"8\" aria-label=\"Loaded length L (m)\"></label><label class=\"control\">Left intensity q\u2081 (kN/m): <strong id=\"v_q1\">2</strong><input id=\"q1\" type=\"range\" min=\"0\" max=\"12\" step=\"0.5\" value=\"2\" aria-label=\"Left intensity q\u2081 (kN/m)\"></label><label class=\"control\">Right intensity q\u2082 (kN/m): <strong id=\"v_q2\">8</strong><input id=\"q2\" type=\"range\" min=\"0\" max=\"12\" step=\"0.5\" value=\"8\" aria-label=\"Right intensity q\u2082 (kN/m)\"></label></section><div class=\\\"diagram\\\" style=\\\"margin:1rem 0;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:0.5rem;\\\"></div><div class=\\\"readouts\\\"><div class=\\\"stat-box out\\\" style=\\\"width:100%;white-space:pre-line;line-height:1.6;font-family:monospace;font-size:0.875rem;\\\"></div></div>",
    init: function(card) {
      try {
        var ranges = Array.prototype.slice.call(card.querySelectorAll('input[type="range"]'));
        var diagramEl = card.querySelector('.diagram');
        var outEl = card.querySelector('.out');
        function rec() {
          var p = {};
          ranges.forEach(function(r) {
            p[r.id] = Number(r.value);
            var vEl = card.querySelector('#v_' + r.id);
            if (vEl) vEl.textContent = r.value;
          });
          var L = p.L || 0, a = Math.min(p.a || 0, L);
          var svg = '', result = '';
          var kind = 'trapezoid';
          if (kind === 'trapezoid') {
            var W = (p.q1 + p.q2) * L / 2;
            var xx = (p.q1 + p.q2) > 0 ? L * (p.q1 + 2 * p.q2) / (3 * (p.q1 + p.q2)) : 0;
            result = 'Equivalent downward resultant W = ' + f(W) + ' kN\nLocation x̄ = ' + f(xx) + ' m from left\nVerification check: uniform loading yields x̄ = L/2';
            svg = '<svg viewBox="0 0 640 240"><polygon points="80,190 550,190 550,' + (185 - 12 * p.q2) + ' 80,' + (185 - 12 * p.q1) + '" fill="#d5edf2" stroke="#287589" stroke-width="3"/>' +
                  line(80, 190, 550, 190) + text(85, 220, 'Left q1=' + p.q1 + ' kN/m') + text(450, 220, 'Right q2=' + p.q2 + ' kN/m') + text(260, 44, 'W=' + f(W) + ' kN at x=' + f(xx) + ' m') + '</svg>';
          } else if (kind === 'beam') {
            var RA = p.w * L / 2 + p.P * (L - a) / (L || 1);
            var RB = p.w * L / 2 + p.P * a / (L || 1);
            result = 'Left support reaction RA = ' + f(RA) + ' kN\nRight support reaction RB = ' + f(RB) + ' kN\nGlobal equilibrium check: RA + RB = ' + f(RA + RB) + ' kN = wL + P';
            svg = '<svg viewBox="0 0 640 240">' + line(75, 150, 560, 150) + '<polygon points="75,152 60,175 90,175" fill="#2f7184"/><polygon points="560,152 545,175 575,175" fill="#2f7184"/>' +
                  line(75 + 485 * a / (L || 1), 50, 75 + 485 * a / (L || 1), 140, '#b06546') + text(75 + 485 * a / (L || 1), 38, 'P=' + p.P + ' kN') + text(230, 190, 'w=' + p.w + ' kN/m') +
                  text(70, 215, 'RA=' + f(RA)) + text(505, 215, 'RB=' + f(RB)) + '</svg>';
          } else if (kind === 'truss') {
            var th = p.theta * Math.PI / 180;
            var F = p.P / (2 * Math.sin(th));
            result = 'Axial compression magnitude in symmetrical diagonals = ' + f(F) + ' kN\nVertical support reaction per joint = ' + f(p.P / 2) + ' kN\nDeterminacy note: static equilibrium of concurrent joint system.';
            var dx = 190 * Math.cos(th), dy = 190 * Math.sin(th);
            svg = '<svg viewBox="0 0 640 240">' + line(320 - dx, 205, 320, 205 - dy) + line(320, 205 - dy, 320 + dx, 205) + line(320, 30, 320, 196, '#b06546') +
                  text(325, 25, 'P=' + p.P + ' kN') + text(48, 232, 'Diagonal axial force |N| = ' + f(F) + ' kN') + '</svg>';
          } else if (kind === 'cable') {
            var H = p.w * L * L / (8 * (p.f || 0.1));
            var V = p.w * L / 2;
            var T = Math.hypot(H, V);
            result = 'Horizontal cable tension component H = ' + f(H) + ' kN\nVertical reaction at each anchor V = ' + f(V) + ' kN\nMaximum end tension T = ' + f(T) + ' kN\nFormulation: uniform vertical dead load per horizontal metre.';
            var d = 'M 70 65 Q 320 ' + (65 + p.f * 14) + ' 570 65';
            svg = '<svg viewBox="0 0 640 240"><path d="' + d + '" fill="none" stroke="#2a788c" stroke-width="4"/>' + line(70, 65, 70, 220) + line(570, 65, 570, 220) +
                  text(230, 200, 'Sag f=' + p.f + ' m') + text(230, 226, 'H=' + f(H) + ' kN') + '</svg>';
          } else if (kind === 'section') {
            var hw = p.h - p.tf;
            var Af = p.b * p.tf, Aw = p.tw * hw, A = Af + Aw;
            var yf = p.h - p.tf / 2, yw = hw / 2;
            var y = (Af * yf + Aw * yw) / (A || 1);
            var If = p.b * Math.pow(p.tf, 3) / 12 + Af * Math.pow(yf - y, 2);
            var Iw = p.tw * Math.pow(hw, 3) / 12 + Aw * Math.pow(yw - y, 2);
            var I = If + Iw;
            result = 'Total cross-sectional area A = ' + f(A) + ' mm²\nCentroid elevation ȳ = ' + f(y) + ' mm from bottom fiber\nCentroidal second moment of area Ixx = ' + f(I) + ' mm⁴\nFormulation: parallel-axis theorem summation.';
            var fx = 320 - p.b * 0.6, fy = 215 - p.h * 0.6;
            svg = '<svg viewBox="0 0 640 240"><rect x="' + (320 - p.tw * 0.6 / 2) + '" y="' + (fy + p.tf * 0.6) + '" width="' + (p.tw * 0.6) + '" height="' + (hw * 0.6) + '" fill="#9fcdd8"/>' +
                  '<rect x="' + fx + '" y="' + fy + '" width="' + (p.b * 0.6) + '" height="' + (p.tf * 0.6) + '" fill="#367f92"/>' +
                  line(120, 215 - y * 0.6, 520, 215 - y * 0.6, '#b06546') + text(340, 215 - y * 0.6 - 7, 'Centroid ȳ=' + f(y) + ' mm') + '</svg>';
          } else if (kind === 'stability') {
            var F = p.mu * p.W, ms = p.W * p.B / 2, mo = p.H * p.h;
            var rs = F / (p.H || 1), rm = ms / (mo || 1);
            result = 'Available interface friction capacity μW = ' + f(F) + ' kN\nSliding safety ratio μW / H = ' + f(rs) + '\nStabilizing gravity moment W·B/2 = ' + f(ms) + ' kN·m\nOverturning moment H·h = ' + f(mo) + ' kN·m\nOverturning safety ratio = ' + f(rm) + '\nEducational screening: assumes rigid footing contact.';
            svg = '<svg viewBox="0 0 640 240"><rect x="180" y="75" width="250" height="130" fill="#b9dce5" stroke="#34788a"/>' +
                  line(95, 190, 520, 190) + line(400, 99, 510, 99, '#b06546') + text(400, 79, 'H=' + p.H + ' kN') + text(260, 50, 'W=' + p.W + ' kN') + text(100, 231, 'Sliding ratio = ' + f(rs)) + '</svg>';
          } else if (kind === 'lever') {
            var effort = p.Q * p.b / (p.a || 1);
            result = 'Ideal equilibrium effort = Q·b/a = ' + f(effort) + ' kN\nKinematic displacement ratio δx_effort / δx_load = a/b = ' + f(p.a / (p.b || 1)) + '\nPrinciple of virtual work: effort × δx_effort = resistance × δx_load.';
            svg = '<svg viewBox="0 0 640 240">' + line(80, 135, 560, 135) + '<polygon points="310,137 290,177 330,177" fill="#377b8c"/>' +
                  line(100, 35, 100, 125, '#b06546') + line(520, 50, 520, 130, '#21697b') + text(70, 22, 'Effort = ' + f(effort) + ' kN') + text(484, 32, 'Q=' + p.Q + ' kN') + '</svg>';
          } else if (kind === 'stage') {
            var base = p.dead * L / 2, live = p.temp * L / 2;
            var RA = base + live + p.P * (L - a) / (L || 1);
            var RB = base + live + p.P * a / (L || 1);
            result = 'Stage A (permanent dead load): RA = RB = ' + f(base) + ' kN\nStage B (transient erection loads): RA = ' + f(RA) + ' kN, RB = ' + f(RB) + ' kN\nTotal Stage B vertical action = ' + f((p.dead + p.temp) * L + p.P) + ' kN.';
            svg = '<svg viewBox="0 0 640 240">' + line(75, 140, 560, 140) + line(75, 120, 560, 120, '#5c94a4') + line(75 + 485 * a / (L || 1), 38, 75 + 485 * a / (L || 1), 130, '#b06546') +
                  text(85, 50, 'Dead=' + p.dead + ' kN/m') + text(270, 70, 'Temp=' + p.temp + ' kN/m') + text(85, 210, 'RA=' + f(RA)) + text(470, 210, 'RB=' + f(RB)) + '</svg>';
          }
          if (diagramEl) diagramEl.innerHTML = svg;
          if (outEl) outEl.textContent = result;
        }
        ranges.forEach(function(r) { r.addEventListener('input', rec); });
        rec();
      } catch (err) {
        console.warn('Statics sim error in model ' + m.idx + ':', err);
      }
    }
  });
  MODELS.push({
    idx: 2,
    unit: 2,
    kind: 'beam',
    html: "<div class=\\\"sim-header\\\"><span class=\\\"badge\\\">Model 02 \u00b7 Unit 2</span><h3>Simply Supported Beam Equilibrium</h3><p>Calculation of vertical support reactions under combined point actions and uniform distributed loads.</p></div><section class=\\\"sim-controls\\\"><label class=\"control\">Span L (m): <strong id=\"v_L\">8</strong><input id=\"L\" type=\"range\" min=\"2\" max=\"20\" step=\"0.5\" value=\"8\" aria-label=\"Span L (m)\"></label><label class=\"control\">Uniform w (kN/m): <strong id=\"v_w\">2</strong><input id=\"w\" type=\"range\" min=\"0\" max=\"10\" step=\"0.25\" value=\"2\" aria-label=\"Uniform w (kN/m)\"></label><label class=\"control\">Point P (kN): <strong id=\"v_P\">10</strong><input id=\"P\" type=\"range\" min=\"0\" max=\"50\" step=\"1\" value=\"10\" aria-label=\"Point P (kN)\"></label><label class=\"control\">Position a (m): <strong id=\"v_a\">4</strong><input id=\"a\" type=\"range\" min=\"0\" max=\"8\" step=\"0.5\" value=\"4\" aria-label=\"Position a (m)\"></label></section><div class=\\\"diagram\\\" style=\\\"margin:1rem 0;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:0.5rem;\\\"></div><div class=\\\"readouts\\\"><div class=\\\"stat-box out\\\" style=\\\"width:100%;white-space:pre-line;line-height:1.6;font-family:monospace;font-size:0.875rem;\\\"></div></div>",
    init: function(card) {
      try {
        var ranges = Array.prototype.slice.call(card.querySelectorAll('input[type="range"]'));
        var diagramEl = card.querySelector('.diagram');
        var outEl = card.querySelector('.out');
        function rec() {
          var p = {};
          ranges.forEach(function(r) {
            p[r.id] = Number(r.value);
            var vEl = card.querySelector('#v_' + r.id);
            if (vEl) vEl.textContent = r.value;
          });
          var L = p.L || 0, a = Math.min(p.a || 0, L);
          var svg = '', result = '';
          var kind = 'beam';
          if (kind === 'trapezoid') {
            var W = (p.q1 + p.q2) * L / 2;
            var xx = (p.q1 + p.q2) > 0 ? L * (p.q1 + 2 * p.q2) / (3 * (p.q1 + p.q2)) : 0;
            result = 'Equivalent downward resultant W = ' + f(W) + ' kN\nLocation x̄ = ' + f(xx) + ' m from left\nVerification check: uniform loading yields x̄ = L/2';
            svg = '<svg viewBox="0 0 640 240"><polygon points="80,190 550,190 550,' + (185 - 12 * p.q2) + ' 80,' + (185 - 12 * p.q1) + '" fill="#d5edf2" stroke="#287589" stroke-width="3"/>' +
                  line(80, 190, 550, 190) + text(85, 220, 'Left q1=' + p.q1 + ' kN/m') + text(450, 220, 'Right q2=' + p.q2 + ' kN/m') + text(260, 44, 'W=' + f(W) + ' kN at x=' + f(xx) + ' m') + '</svg>';
          } else if (kind === 'beam') {
            var RA = p.w * L / 2 + p.P * (L - a) / (L || 1);
            var RB = p.w * L / 2 + p.P * a / (L || 1);
            result = 'Left support reaction RA = ' + f(RA) + ' kN\nRight support reaction RB = ' + f(RB) + ' kN\nGlobal equilibrium check: RA + RB = ' + f(RA + RB) + ' kN = wL + P';
            svg = '<svg viewBox="0 0 640 240">' + line(75, 150, 560, 150) + '<polygon points="75,152 60,175 90,175" fill="#2f7184"/><polygon points="560,152 545,175 575,175" fill="#2f7184"/>' +
                  line(75 + 485 * a / (L || 1), 50, 75 + 485 * a / (L || 1), 140, '#b06546') + text(75 + 485 * a / (L || 1), 38, 'P=' + p.P + ' kN') + text(230, 190, 'w=' + p.w + ' kN/m') +
                  text(70, 215, 'RA=' + f(RA)) + text(505, 215, 'RB=' + f(RB)) + '</svg>';
          } else if (kind === 'truss') {
            var th = p.theta * Math.PI / 180;
            var F = p.P / (2 * Math.sin(th));
            result = 'Axial compression magnitude in symmetrical diagonals = ' + f(F) + ' kN\nVertical support reaction per joint = ' + f(p.P / 2) + ' kN\nDeterminacy note: static equilibrium of concurrent joint system.';
            var dx = 190 * Math.cos(th), dy = 190 * Math.sin(th);
            svg = '<svg viewBox="0 0 640 240">' + line(320 - dx, 205, 320, 205 - dy) + line(320, 205 - dy, 320 + dx, 205) + line(320, 30, 320, 196, '#b06546') +
                  text(325, 25, 'P=' + p.P + ' kN') + text(48, 232, 'Diagonal axial force |N| = ' + f(F) + ' kN') + '</svg>';
          } else if (kind === 'cable') {
            var H = p.w * L * L / (8 * (p.f || 0.1));
            var V = p.w * L / 2;
            var T = Math.hypot(H, V);
            result = 'Horizontal cable tension component H = ' + f(H) + ' kN\nVertical reaction at each anchor V = ' + f(V) + ' kN\nMaximum end tension T = ' + f(T) + ' kN\nFormulation: uniform vertical dead load per horizontal metre.';
            var d = 'M 70 65 Q 320 ' + (65 + p.f * 14) + ' 570 65';
            svg = '<svg viewBox="0 0 640 240"><path d="' + d + '" fill="none" stroke="#2a788c" stroke-width="4"/>' + line(70, 65, 70, 220) + line(570, 65, 570, 220) +
                  text(230, 200, 'Sag f=' + p.f + ' m') + text(230, 226, 'H=' + f(H) + ' kN') + '</svg>';
          } else if (kind === 'section') {
            var hw = p.h - p.tf;
            var Af = p.b * p.tf, Aw = p.tw * hw, A = Af + Aw;
            var yf = p.h - p.tf / 2, yw = hw / 2;
            var y = (Af * yf + Aw * yw) / (A || 1);
            var If = p.b * Math.pow(p.tf, 3) / 12 + Af * Math.pow(yf - y, 2);
            var Iw = p.tw * Math.pow(hw, 3) / 12 + Aw * Math.pow(yw - y, 2);
            var I = If + Iw;
            result = 'Total cross-sectional area A = ' + f(A) + ' mm²\nCentroid elevation ȳ = ' + f(y) + ' mm from bottom fiber\nCentroidal second moment of area Ixx = ' + f(I) + ' mm⁴\nFormulation: parallel-axis theorem summation.';
            var fx = 320 - p.b * 0.6, fy = 215 - p.h * 0.6;
            svg = '<svg viewBox="0 0 640 240"><rect x="' + (320 - p.tw * 0.6 / 2) + '" y="' + (fy + p.tf * 0.6) + '" width="' + (p.tw * 0.6) + '" height="' + (hw * 0.6) + '" fill="#9fcdd8"/>' +
                  '<rect x="' + fx + '" y="' + fy + '" width="' + (p.b * 0.6) + '" height="' + (p.tf * 0.6) + '" fill="#367f92"/>' +
                  line(120, 215 - y * 0.6, 520, 215 - y * 0.6, '#b06546') + text(340, 215 - y * 0.6 - 7, 'Centroid ȳ=' + f(y) + ' mm') + '</svg>';
          } else if (kind === 'stability') {
            var F = p.mu * p.W, ms = p.W * p.B / 2, mo = p.H * p.h;
            var rs = F / (p.H || 1), rm = ms / (mo || 1);
            result = 'Available interface friction capacity μW = ' + f(F) + ' kN\nSliding safety ratio μW / H = ' + f(rs) + '\nStabilizing gravity moment W·B/2 = ' + f(ms) + ' kN·m\nOverturning moment H·h = ' + f(mo) + ' kN·m\nOverturning safety ratio = ' + f(rm) + '\nEducational screening: assumes rigid footing contact.';
            svg = '<svg viewBox="0 0 640 240"><rect x="180" y="75" width="250" height="130" fill="#b9dce5" stroke="#34788a"/>' +
                  line(95, 190, 520, 190) + line(400, 99, 510, 99, '#b06546') + text(400, 79, 'H=' + p.H + ' kN') + text(260, 50, 'W=' + p.W + ' kN') + text(100, 231, 'Sliding ratio = ' + f(rs)) + '</svg>';
          } else if (kind === 'lever') {
            var effort = p.Q * p.b / (p.a || 1);
            result = 'Ideal equilibrium effort = Q·b/a = ' + f(effort) + ' kN\nKinematic displacement ratio δx_effort / δx_load = a/b = ' + f(p.a / (p.b || 1)) + '\nPrinciple of virtual work: effort × δx_effort = resistance × δx_load.';
            svg = '<svg viewBox="0 0 640 240">' + line(80, 135, 560, 135) + '<polygon points="310,137 290,177 330,177" fill="#377b8c"/>' +
                  line(100, 35, 100, 125, '#b06546') + line(520, 50, 520, 130, '#21697b') + text(70, 22, 'Effort = ' + f(effort) + ' kN') + text(484, 32, 'Q=' + p.Q + ' kN') + '</svg>';
          } else if (kind === 'stage') {
            var base = p.dead * L / 2, live = p.temp * L / 2;
            var RA = base + live + p.P * (L - a) / (L || 1);
            var RB = base + live + p.P * a / (L || 1);
            result = 'Stage A (permanent dead load): RA = RB = ' + f(base) + ' kN\nStage B (transient erection loads): RA = ' + f(RA) + ' kN, RB = ' + f(RB) + ' kN\nTotal Stage B vertical action = ' + f((p.dead + p.temp) * L + p.P) + ' kN.';
            svg = '<svg viewBox="0 0 640 240">' + line(75, 140, 560, 140) + line(75, 120, 560, 120, '#5c94a4') + line(75 + 485 * a / (L || 1), 38, 75 + 485 * a / (L || 1), 130, '#b06546') +
                  text(85, 50, 'Dead=' + p.dead + ' kN/m') + text(270, 70, 'Temp=' + p.temp + ' kN/m') + text(85, 210, 'RA=' + f(RA)) + text(470, 210, 'RB=' + f(RB)) + '</svg>';
          }
          if (diagramEl) diagramEl.innerHTML = svg;
          if (outEl) outEl.textContent = result;
        }
        ranges.forEach(function(r) { r.addEventListener('input', rec); });
        rec();
      } catch (err) {
        console.warn('Statics sim error in model ' + m.idx + ':', err);
      }
    }
  });
  MODELS.push({
    idx: 3,
    unit: 3,
    kind: 'truss',
    html: "<div class=\\\"sim-header\\\"><span class=\\\"badge\\\">Model 03 \u00b7 Unit 3</span><h3>Roof Truss Apex Equilibrium</h3><p>Method of joints resolution at a symmetrical two-bar pin-jointed truss apex carrying a centric downward action.</p></div><section class=\\\"sim-controls\\\"><label class=\"control\">Downward load P (kN): <strong id=\"v_P\">24</strong><input id=\"P\" type=\"range\" min=\"1\" max=\"60\" step=\"1\" value=\"24\" aria-label=\"Downward load P (kN)\"></label><label class=\"control\">Member inclination \u03b8 (degrees): <strong id=\"v_theta\">45</strong><input id=\"theta\" type=\"range\" min=\"15\" max=\"75\" step=\"1\" value=\"45\" aria-label=\"Member inclination \u03b8 (degrees)\"></label></section><div class=\\\"diagram\\\" style=\\\"margin:1rem 0;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:0.5rem;\\\"></div><div class=\\\"readouts\\\"><div class=\\\"stat-box out\\\" style=\\\"width:100%;white-space:pre-line;line-height:1.6;font-family:monospace;font-size:0.875rem;\\\"></div></div>",
    init: function(card) {
      try {
        var ranges = Array.prototype.slice.call(card.querySelectorAll('input[type="range"]'));
        var diagramEl = card.querySelector('.diagram');
        var outEl = card.querySelector('.out');
        function rec() {
          var p = {};
          ranges.forEach(function(r) {
            p[r.id] = Number(r.value);
            var vEl = card.querySelector('#v_' + r.id);
            if (vEl) vEl.textContent = r.value;
          });
          var L = p.L || 0, a = Math.min(p.a || 0, L);
          var svg = '', result = '';
          var kind = 'truss';
          if (kind === 'trapezoid') {
            var W = (p.q1 + p.q2) * L / 2;
            var xx = (p.q1 + p.q2) > 0 ? L * (p.q1 + 2 * p.q2) / (3 * (p.q1 + p.q2)) : 0;
            result = 'Equivalent downward resultant W = ' + f(W) + ' kN\nLocation x̄ = ' + f(xx) + ' m from left\nVerification check: uniform loading yields x̄ = L/2';
            svg = '<svg viewBox="0 0 640 240"><polygon points="80,190 550,190 550,' + (185 - 12 * p.q2) + ' 80,' + (185 - 12 * p.q1) + '" fill="#d5edf2" stroke="#287589" stroke-width="3"/>' +
                  line(80, 190, 550, 190) + text(85, 220, 'Left q1=' + p.q1 + ' kN/m') + text(450, 220, 'Right q2=' + p.q2 + ' kN/m') + text(260, 44, 'W=' + f(W) + ' kN at x=' + f(xx) + ' m') + '</svg>';
          } else if (kind === 'beam') {
            var RA = p.w * L / 2 + p.P * (L - a) / (L || 1);
            var RB = p.w * L / 2 + p.P * a / (L || 1);
            result = 'Left support reaction RA = ' + f(RA) + ' kN\nRight support reaction RB = ' + f(RB) + ' kN\nGlobal equilibrium check: RA + RB = ' + f(RA + RB) + ' kN = wL + P';
            svg = '<svg viewBox="0 0 640 240">' + line(75, 150, 560, 150) + '<polygon points="75,152 60,175 90,175" fill="#2f7184"/><polygon points="560,152 545,175 575,175" fill="#2f7184"/>' +
                  line(75 + 485 * a / (L || 1), 50, 75 + 485 * a / (L || 1), 140, '#b06546') + text(75 + 485 * a / (L || 1), 38, 'P=' + p.P + ' kN') + text(230, 190, 'w=' + p.w + ' kN/m') +
                  text(70, 215, 'RA=' + f(RA)) + text(505, 215, 'RB=' + f(RB)) + '</svg>';
          } else if (kind === 'truss') {
            var th = p.theta * Math.PI / 180;
            var F = p.P / (2 * Math.sin(th));
            result = 'Axial compression magnitude in symmetrical diagonals = ' + f(F) + ' kN\nVertical support reaction per joint = ' + f(p.P / 2) + ' kN\nDeterminacy note: static equilibrium of concurrent joint system.';
            var dx = 190 * Math.cos(th), dy = 190 * Math.sin(th);
            svg = '<svg viewBox="0 0 640 240">' + line(320 - dx, 205, 320, 205 - dy) + line(320, 205 - dy, 320 + dx, 205) + line(320, 30, 320, 196, '#b06546') +
                  text(325, 25, 'P=' + p.P + ' kN') + text(48, 232, 'Diagonal axial force |N| = ' + f(F) + ' kN') + '</svg>';
          } else if (kind === 'cable') {
            var H = p.w * L * L / (8 * (p.f || 0.1));
            var V = p.w * L / 2;
            var T = Math.hypot(H, V);
            result = 'Horizontal cable tension component H = ' + f(H) + ' kN\nVertical reaction at each anchor V = ' + f(V) + ' kN\nMaximum end tension T = ' + f(T) + ' kN\nFormulation: uniform vertical dead load per horizontal metre.';
            var d = 'M 70 65 Q 320 ' + (65 + p.f * 14) + ' 570 65';
            svg = '<svg viewBox="0 0 640 240"><path d="' + d + '" fill="none" stroke="#2a788c" stroke-width="4"/>' + line(70, 65, 70, 220) + line(570, 65, 570, 220) +
                  text(230, 200, 'Sag f=' + p.f + ' m') + text(230, 226, 'H=' + f(H) + ' kN') + '</svg>';
          } else if (kind === 'section') {
            var hw = p.h - p.tf;
            var Af = p.b * p.tf, Aw = p.tw * hw, A = Af + Aw;
            var yf = p.h - p.tf / 2, yw = hw / 2;
            var y = (Af * yf + Aw * yw) / (A || 1);
            var If = p.b * Math.pow(p.tf, 3) / 12 + Af * Math.pow(yf - y, 2);
            var Iw = p.tw * Math.pow(hw, 3) / 12 + Aw * Math.pow(yw - y, 2);
            var I = If + Iw;
            result = 'Total cross-sectional area A = ' + f(A) + ' mm²\nCentroid elevation ȳ = ' + f(y) + ' mm from bottom fiber\nCentroidal second moment of area Ixx = ' + f(I) + ' mm⁴\nFormulation: parallel-axis theorem summation.';
            var fx = 320 - p.b * 0.6, fy = 215 - p.h * 0.6;
            svg = '<svg viewBox="0 0 640 240"><rect x="' + (320 - p.tw * 0.6 / 2) + '" y="' + (fy + p.tf * 0.6) + '" width="' + (p.tw * 0.6) + '" height="' + (hw * 0.6) + '" fill="#9fcdd8"/>' +
                  '<rect x="' + fx + '" y="' + fy + '" width="' + (p.b * 0.6) + '" height="' + (p.tf * 0.6) + '" fill="#367f92"/>' +
                  line(120, 215 - y * 0.6, 520, 215 - y * 0.6, '#b06546') + text(340, 215 - y * 0.6 - 7, 'Centroid ȳ=' + f(y) + ' mm') + '</svg>';
          } else if (kind === 'stability') {
            var F = p.mu * p.W, ms = p.W * p.B / 2, mo = p.H * p.h;
            var rs = F / (p.H || 1), rm = ms / (mo || 1);
            result = 'Available interface friction capacity μW = ' + f(F) + ' kN\nSliding safety ratio μW / H = ' + f(rs) + '\nStabilizing gravity moment W·B/2 = ' + f(ms) + ' kN·m\nOverturning moment H·h = ' + f(mo) + ' kN·m\nOverturning safety ratio = ' + f(rm) + '\nEducational screening: assumes rigid footing contact.';
            svg = '<svg viewBox="0 0 640 240"><rect x="180" y="75" width="250" height="130" fill="#b9dce5" stroke="#34788a"/>' +
                  line(95, 190, 520, 190) + line(400, 99, 510, 99, '#b06546') + text(400, 79, 'H=' + p.H + ' kN') + text(260, 50, 'W=' + p.W + ' kN') + text(100, 231, 'Sliding ratio = ' + f(rs)) + '</svg>';
          } else if (kind === 'lever') {
            var effort = p.Q * p.b / (p.a || 1);
            result = 'Ideal equilibrium effort = Q·b/a = ' + f(effort) + ' kN\nKinematic displacement ratio δx_effort / δx_load = a/b = ' + f(p.a / (p.b || 1)) + '\nPrinciple of virtual work: effort × δx_effort = resistance × δx_load.';
            svg = '<svg viewBox="0 0 640 240">' + line(80, 135, 560, 135) + '<polygon points="310,137 290,177 330,177" fill="#377b8c"/>' +
                  line(100, 35, 100, 125, '#b06546') + line(520, 50, 520, 130, '#21697b') + text(70, 22, 'Effort = ' + f(effort) + ' kN') + text(484, 32, 'Q=' + p.Q + ' kN') + '</svg>';
          } else if (kind === 'stage') {
            var base = p.dead * L / 2, live = p.temp * L / 2;
            var RA = base + live + p.P * (L - a) / (L || 1);
            var RB = base + live + p.P * a / (L || 1);
            result = 'Stage A (permanent dead load): RA = RB = ' + f(base) + ' kN\nStage B (transient erection loads): RA = ' + f(RA) + ' kN, RB = ' + f(RB) + ' kN\nTotal Stage B vertical action = ' + f((p.dead + p.temp) * L + p.P) + ' kN.';
            svg = '<svg viewBox="0 0 640 240">' + line(75, 140, 560, 140) + line(75, 120, 560, 120, '#5c94a4') + line(75 + 485 * a / (L || 1), 38, 75 + 485 * a / (L || 1), 130, '#b06546') +
                  text(85, 50, 'Dead=' + p.dead + ' kN/m') + text(270, 70, 'Temp=' + p.temp + ' kN/m') + text(85, 210, 'RA=' + f(RA)) + text(470, 210, 'RB=' + f(RB)) + '</svg>';
          }
          if (diagramEl) diagramEl.innerHTML = svg;
          if (outEl) outEl.textContent = result;
        }
        ranges.forEach(function(r) { r.addEventListener('input', rec); });
        rec();
      } catch (err) {
        console.warn('Statics sim error in model ' + m.idx + ':', err);
      }
    }
  });
  MODELS.push({
    idx: 4,
    unit: 4,
    kind: 'cable',
    html: "<div class=\\\"sim-header\\\"><span class=\\\"badge\\\">Model 04 \u00b7 Unit 4</span><h3>Parabolic Cable Tension and Sag</h3><p>Horizontal tension, vertical anchor reaction, and maximum tangent tension for a uniformly loaded flexible cable.</p></div><section class=\\\"sim-controls\\\"><label class=\"control\">Span L (m): <strong id=\"v_L\">20</strong><input id=\"L\" type=\"range\" min=\"4\" max=\"40\" step=\"1\" value=\"20\" aria-label=\"Span L (m)\"></label><label class=\"control\">Sag f (m): <strong id=\"v_f\">2</strong><input id=\"f\" type=\"range\" min=\"0.5\" max=\"8\" step=\"0.25\" value=\"2\" aria-label=\"Sag f (m)\"></label><label class=\"control\">Load w (kN/m horizontal): <strong id=\"v_w\">1</strong><input id=\"w\" type=\"range\" min=\"0.5\" max=\"8\" step=\"0.25\" value=\"1\" aria-label=\"Load w (kN/m horizontal)\"></label></section><div class=\\\"diagram\\\" style=\\\"margin:1rem 0;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:0.5rem;\\\"></div><div class=\\\"readouts\\\"><div class=\\\"stat-box out\\\" style=\\\"width:100%;white-space:pre-line;line-height:1.6;font-family:monospace;font-size:0.875rem;\\\"></div></div>",
    init: function(card) {
      try {
        var ranges = Array.prototype.slice.call(card.querySelectorAll('input[type="range"]'));
        var diagramEl = card.querySelector('.diagram');
        var outEl = card.querySelector('.out');
        function rec() {
          var p = {};
          ranges.forEach(function(r) {
            p[r.id] = Number(r.value);
            var vEl = card.querySelector('#v_' + r.id);
            if (vEl) vEl.textContent = r.value;
          });
          var L = p.L || 0, a = Math.min(p.a || 0, L);
          var svg = '', result = '';
          var kind = 'cable';
          if (kind === 'trapezoid') {
            var W = (p.q1 + p.q2) * L / 2;
            var xx = (p.q1 + p.q2) > 0 ? L * (p.q1 + 2 * p.q2) / (3 * (p.q1 + p.q2)) : 0;
            result = 'Equivalent downward resultant W = ' + f(W) + ' kN\nLocation x̄ = ' + f(xx) + ' m from left\nVerification check: uniform loading yields x̄ = L/2';
            svg = '<svg viewBox="0 0 640 240"><polygon points="80,190 550,190 550,' + (185 - 12 * p.q2) + ' 80,' + (185 - 12 * p.q1) + '" fill="#d5edf2" stroke="#287589" stroke-width="3"/>' +
                  line(80, 190, 550, 190) + text(85, 220, 'Left q1=' + p.q1 + ' kN/m') + text(450, 220, 'Right q2=' + p.q2 + ' kN/m') + text(260, 44, 'W=' + f(W) + ' kN at x=' + f(xx) + ' m') + '</svg>';
          } else if (kind === 'beam') {
            var RA = p.w * L / 2 + p.P * (L - a) / (L || 1);
            var RB = p.w * L / 2 + p.P * a / (L || 1);
            result = 'Left support reaction RA = ' + f(RA) + ' kN\nRight support reaction RB = ' + f(RB) + ' kN\nGlobal equilibrium check: RA + RB = ' + f(RA + RB) + ' kN = wL + P';
            svg = '<svg viewBox="0 0 640 240">' + line(75, 150, 560, 150) + '<polygon points="75,152 60,175 90,175" fill="#2f7184"/><polygon points="560,152 545,175 575,175" fill="#2f7184"/>' +
                  line(75 + 485 * a / (L || 1), 50, 75 + 485 * a / (L || 1), 140, '#b06546') + text(75 + 485 * a / (L || 1), 38, 'P=' + p.P + ' kN') + text(230, 190, 'w=' + p.w + ' kN/m') +
                  text(70, 215, 'RA=' + f(RA)) + text(505, 215, 'RB=' + f(RB)) + '</svg>';
          } else if (kind === 'truss') {
            var th = p.theta * Math.PI / 180;
            var F = p.P / (2 * Math.sin(th));
            result = 'Axial compression magnitude in symmetrical diagonals = ' + f(F) + ' kN\nVertical support reaction per joint = ' + f(p.P / 2) + ' kN\nDeterminacy note: static equilibrium of concurrent joint system.';
            var dx = 190 * Math.cos(th), dy = 190 * Math.sin(th);
            svg = '<svg viewBox="0 0 640 240">' + line(320 - dx, 205, 320, 205 - dy) + line(320, 205 - dy, 320 + dx, 205) + line(320, 30, 320, 196, '#b06546') +
                  text(325, 25, 'P=' + p.P + ' kN') + text(48, 232, 'Diagonal axial force |N| = ' + f(F) + ' kN') + '</svg>';
          } else if (kind === 'cable') {
            var H = p.w * L * L / (8 * (p.f || 0.1));
            var V = p.w * L / 2;
            var T = Math.hypot(H, V);
            result = 'Horizontal cable tension component H = ' + f(H) + ' kN\nVertical reaction at each anchor V = ' + f(V) + ' kN\nMaximum end tension T = ' + f(T) + ' kN\nFormulation: uniform vertical dead load per horizontal metre.';
            var d = 'M 70 65 Q 320 ' + (65 + p.f * 14) + ' 570 65';
            svg = '<svg viewBox="0 0 640 240"><path d="' + d + '" fill="none" stroke="#2a788c" stroke-width="4"/>' + line(70, 65, 70, 220) + line(570, 65, 570, 220) +
                  text(230, 200, 'Sag f=' + p.f + ' m') + text(230, 226, 'H=' + f(H) + ' kN') + '</svg>';
          } else if (kind === 'section') {
            var hw = p.h - p.tf;
            var Af = p.b * p.tf, Aw = p.tw * hw, A = Af + Aw;
            var yf = p.h - p.tf / 2, yw = hw / 2;
            var y = (Af * yf + Aw * yw) / (A || 1);
            var If = p.b * Math.pow(p.tf, 3) / 12 + Af * Math.pow(yf - y, 2);
            var Iw = p.tw * Math.pow(hw, 3) / 12 + Aw * Math.pow(yw - y, 2);
            var I = If + Iw;
            result = 'Total cross-sectional area A = ' + f(A) + ' mm²\nCentroid elevation ȳ = ' + f(y) + ' mm from bottom fiber\nCentroidal second moment of area Ixx = ' + f(I) + ' mm⁴\nFormulation: parallel-axis theorem summation.';
            var fx = 320 - p.b * 0.6, fy = 215 - p.h * 0.6;
            svg = '<svg viewBox="0 0 640 240"><rect x="' + (320 - p.tw * 0.6 / 2) + '" y="' + (fy + p.tf * 0.6) + '" width="' + (p.tw * 0.6) + '" height="' + (hw * 0.6) + '" fill="#9fcdd8"/>' +
                  '<rect x="' + fx + '" y="' + fy + '" width="' + (p.b * 0.6) + '" height="' + (p.tf * 0.6) + '" fill="#367f92"/>' +
                  line(120, 215 - y * 0.6, 520, 215 - y * 0.6, '#b06546') + text(340, 215 - y * 0.6 - 7, 'Centroid ȳ=' + f(y) + ' mm') + '</svg>';
          } else if (kind === 'stability') {
            var F = p.mu * p.W, ms = p.W * p.B / 2, mo = p.H * p.h;
            var rs = F / (p.H || 1), rm = ms / (mo || 1);
            result = 'Available interface friction capacity μW = ' + f(F) + ' kN\nSliding safety ratio μW / H = ' + f(rs) + '\nStabilizing gravity moment W·B/2 = ' + f(ms) + ' kN·m\nOverturning moment H·h = ' + f(mo) + ' kN·m\nOverturning safety ratio = ' + f(rm) + '\nEducational screening: assumes rigid footing contact.';
            svg = '<svg viewBox="0 0 640 240"><rect x="180" y="75" width="250" height="130" fill="#b9dce5" stroke="#34788a"/>' +
                  line(95, 190, 520, 190) + line(400, 99, 510, 99, '#b06546') + text(400, 79, 'H=' + p.H + ' kN') + text(260, 50, 'W=' + p.W + ' kN') + text(100, 231, 'Sliding ratio = ' + f(rs)) + '</svg>';
          } else if (kind === 'lever') {
            var effort = p.Q * p.b / (p.a || 1);
            result = 'Ideal equilibrium effort = Q·b/a = ' + f(effort) + ' kN\nKinematic displacement ratio δx_effort / δx_load = a/b = ' + f(p.a / (p.b || 1)) + '\nPrinciple of virtual work: effort × δx_effort = resistance × δx_load.';
            svg = '<svg viewBox="0 0 640 240">' + line(80, 135, 560, 135) + '<polygon points="310,137 290,177 330,177" fill="#377b8c"/>' +
                  line(100, 35, 100, 125, '#b06546') + line(520, 50, 520, 130, '#21697b') + text(70, 22, 'Effort = ' + f(effort) + ' kN') + text(484, 32, 'Q=' + p.Q + ' kN') + '</svg>';
          } else if (kind === 'stage') {
            var base = p.dead * L / 2, live = p.temp * L / 2;
            var RA = base + live + p.P * (L - a) / (L || 1);
            var RB = base + live + p.P * a / (L || 1);
            result = 'Stage A (permanent dead load): RA = RB = ' + f(base) + ' kN\nStage B (transient erection loads): RA = ' + f(RA) + ' kN, RB = ' + f(RB) + ' kN\nTotal Stage B vertical action = ' + f((p.dead + p.temp) * L + p.P) + ' kN.';
            svg = '<svg viewBox="0 0 640 240">' + line(75, 140, 560, 140) + line(75, 120, 560, 120, '#5c94a4') + line(75 + 485 * a / (L || 1), 38, 75 + 485 * a / (L || 1), 130, '#b06546') +
                  text(85, 50, 'Dead=' + p.dead + ' kN/m') + text(270, 70, 'Temp=' + p.temp + ' kN/m') + text(85, 210, 'RA=' + f(RA)) + text(470, 210, 'RB=' + f(RB)) + '</svg>';
          }
          if (diagramEl) diagramEl.innerHTML = svg;
          if (outEl) outEl.textContent = result;
        }
        ranges.forEach(function(r) { r.addEventListener('input', rec); });
        rec();
      } catch (err) {
        console.warn('Statics sim error in model ' + m.idx + ':', err);
      }
    }
  });
  MODELS.push({
    idx: 5,
    unit: 5,
    kind: 'section',
    html: "<div class=\\\"sim-header\\\"><span class=\\\"badge\\\">Model 05 \u00b7 Unit 5</span><h3>Composite Section Centroid and Inertia</h3><p>Parallel-axis theorem calculation of centroid elevation and second moment of area for a structural T-section.</p></div><section class=\\\"sim-controls\\\"><label class=\"control\">Flange width b (mm): <strong id=\"v_b\">240</strong><input id=\"b\" type=\"range\" min=\"100\" max=\"500\" step=\"10\" value=\"240\" aria-label=\"Flange width b (mm)\"></label><label class=\"control\">Flange thickness tf (mm): <strong id=\"v_tf\">20</strong><input id=\"tf\" type=\"range\" min=\"10\" max=\"60\" step=\"5\" value=\"20\" aria-label=\"Flange thickness tf (mm)\"></label><label class=\"control\">Web thickness tw (mm): <strong id=\"v_tw\">30</strong><input id=\"tw\" type=\"range\" min=\"10\" max=\"80\" step=\"5\" value=\"30\" aria-label=\"Web thickness tw (mm)\"></label><label class=\"control\">Total height h (mm): <strong id=\"v_h\">260</strong><input id=\"h\" type=\"range\" min=\"100\" max=\"450\" step=\"10\" value=\"260\" aria-label=\"Total height h (mm)\"></label></section><div class=\\\"diagram\\\" style=\\\"margin:1rem 0;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:0.5rem;\\\"></div><div class=\\\"readouts\\\"><div class=\\\"stat-box out\\\" style=\\\"width:100%;white-space:pre-line;line-height:1.6;font-family:monospace;font-size:0.875rem;\\\"></div></div>",
    init: function(card) {
      try {
        var ranges = Array.prototype.slice.call(card.querySelectorAll('input[type="range"]'));
        var diagramEl = card.querySelector('.diagram');
        var outEl = card.querySelector('.out');
        function rec() {
          var p = {};
          ranges.forEach(function(r) {
            p[r.id] = Number(r.value);
            var vEl = card.querySelector('#v_' + r.id);
            if (vEl) vEl.textContent = r.value;
          });
          var L = p.L || 0, a = Math.min(p.a || 0, L);
          var svg = '', result = '';
          var kind = 'section';
          if (kind === 'trapezoid') {
            var W = (p.q1 + p.q2) * L / 2;
            var xx = (p.q1 + p.q2) > 0 ? L * (p.q1 + 2 * p.q2) / (3 * (p.q1 + p.q2)) : 0;
            result = 'Equivalent downward resultant W = ' + f(W) + ' kN\nLocation x̄ = ' + f(xx) + ' m from left\nVerification check: uniform loading yields x̄ = L/2';
            svg = '<svg viewBox="0 0 640 240"><polygon points="80,190 550,190 550,' + (185 - 12 * p.q2) + ' 80,' + (185 - 12 * p.q1) + '" fill="#d5edf2" stroke="#287589" stroke-width="3"/>' +
                  line(80, 190, 550, 190) + text(85, 220, 'Left q1=' + p.q1 + ' kN/m') + text(450, 220, 'Right q2=' + p.q2 + ' kN/m') + text(260, 44, 'W=' + f(W) + ' kN at x=' + f(xx) + ' m') + '</svg>';
          } else if (kind === 'beam') {
            var RA = p.w * L / 2 + p.P * (L - a) / (L || 1);
            var RB = p.w * L / 2 + p.P * a / (L || 1);
            result = 'Left support reaction RA = ' + f(RA) + ' kN\nRight support reaction RB = ' + f(RB) + ' kN\nGlobal equilibrium check: RA + RB = ' + f(RA + RB) + ' kN = wL + P';
            svg = '<svg viewBox="0 0 640 240">' + line(75, 150, 560, 150) + '<polygon points="75,152 60,175 90,175" fill="#2f7184"/><polygon points="560,152 545,175 575,175" fill="#2f7184"/>' +
                  line(75 + 485 * a / (L || 1), 50, 75 + 485 * a / (L || 1), 140, '#b06546') + text(75 + 485 * a / (L || 1), 38, 'P=' + p.P + ' kN') + text(230, 190, 'w=' + p.w + ' kN/m') +
                  text(70, 215, 'RA=' + f(RA)) + text(505, 215, 'RB=' + f(RB)) + '</svg>';
          } else if (kind === 'truss') {
            var th = p.theta * Math.PI / 180;
            var F = p.P / (2 * Math.sin(th));
            result = 'Axial compression magnitude in symmetrical diagonals = ' + f(F) + ' kN\nVertical support reaction per joint = ' + f(p.P / 2) + ' kN\nDeterminacy note: static equilibrium of concurrent joint system.';
            var dx = 190 * Math.cos(th), dy = 190 * Math.sin(th);
            svg = '<svg viewBox="0 0 640 240">' + line(320 - dx, 205, 320, 205 - dy) + line(320, 205 - dy, 320 + dx, 205) + line(320, 30, 320, 196, '#b06546') +
                  text(325, 25, 'P=' + p.P + ' kN') + text(48, 232, 'Diagonal axial force |N| = ' + f(F) + ' kN') + '</svg>';
          } else if (kind === 'cable') {
            var H = p.w * L * L / (8 * (p.f || 0.1));
            var V = p.w * L / 2;
            var T = Math.hypot(H, V);
            result = 'Horizontal cable tension component H = ' + f(H) + ' kN\nVertical reaction at each anchor V = ' + f(V) + ' kN\nMaximum end tension T = ' + f(T) + ' kN\nFormulation: uniform vertical dead load per horizontal metre.';
            var d = 'M 70 65 Q 320 ' + (65 + p.f * 14) + ' 570 65';
            svg = '<svg viewBox="0 0 640 240"><path d="' + d + '" fill="none" stroke="#2a788c" stroke-width="4"/>' + line(70, 65, 70, 220) + line(570, 65, 570, 220) +
                  text(230, 200, 'Sag f=' + p.f + ' m') + text(230, 226, 'H=' + f(H) + ' kN') + '</svg>';
          } else if (kind === 'section') {
            var hw = p.h - p.tf;
            var Af = p.b * p.tf, Aw = p.tw * hw, A = Af + Aw;
            var yf = p.h - p.tf / 2, yw = hw / 2;
            var y = (Af * yf + Aw * yw) / (A || 1);
            var If = p.b * Math.pow(p.tf, 3) / 12 + Af * Math.pow(yf - y, 2);
            var Iw = p.tw * Math.pow(hw, 3) / 12 + Aw * Math.pow(yw - y, 2);
            var I = If + Iw;
            result = 'Total cross-sectional area A = ' + f(A) + ' mm²\nCentroid elevation ȳ = ' + f(y) + ' mm from bottom fiber\nCentroidal second moment of area Ixx = ' + f(I) + ' mm⁴\nFormulation: parallel-axis theorem summation.';
            var fx = 320 - p.b * 0.6, fy = 215 - p.h * 0.6;
            svg = '<svg viewBox="0 0 640 240"><rect x="' + (320 - p.tw * 0.6 / 2) + '" y="' + (fy + p.tf * 0.6) + '" width="' + (p.tw * 0.6) + '" height="' + (hw * 0.6) + '" fill="#9fcdd8"/>' +
                  '<rect x="' + fx + '" y="' + fy + '" width="' + (p.b * 0.6) + '" height="' + (p.tf * 0.6) + '" fill="#367f92"/>' +
                  line(120, 215 - y * 0.6, 520, 215 - y * 0.6, '#b06546') + text(340, 215 - y * 0.6 - 7, 'Centroid ȳ=' + f(y) + ' mm') + '</svg>';
          } else if (kind === 'stability') {
            var F = p.mu * p.W, ms = p.W * p.B / 2, mo = p.H * p.h;
            var rs = F / (p.H || 1), rm = ms / (mo || 1);
            result = 'Available interface friction capacity μW = ' + f(F) + ' kN\nSliding safety ratio μW / H = ' + f(rs) + '\nStabilizing gravity moment W·B/2 = ' + f(ms) + ' kN·m\nOverturning moment H·h = ' + f(mo) + ' kN·m\nOverturning safety ratio = ' + f(rm) + '\nEducational screening: assumes rigid footing contact.';
            svg = '<svg viewBox="0 0 640 240"><rect x="180" y="75" width="250" height="130" fill="#b9dce5" stroke="#34788a"/>' +
                  line(95, 190, 520, 190) + line(400, 99, 510, 99, '#b06546') + text(400, 79, 'H=' + p.H + ' kN') + text(260, 50, 'W=' + p.W + ' kN') + text(100, 231, 'Sliding ratio = ' + f(rs)) + '</svg>';
          } else if (kind === 'lever') {
            var effort = p.Q * p.b / (p.a || 1);
            result = 'Ideal equilibrium effort = Q·b/a = ' + f(effort) + ' kN\nKinematic displacement ratio δx_effort / δx_load = a/b = ' + f(p.a / (p.b || 1)) + '\nPrinciple of virtual work: effort × δx_effort = resistance × δx_load.';
            svg = '<svg viewBox="0 0 640 240">' + line(80, 135, 560, 135) + '<polygon points="310,137 290,177 330,177" fill="#377b8c"/>' +
                  line(100, 35, 100, 125, '#b06546') + line(520, 50, 520, 130, '#21697b') + text(70, 22, 'Effort = ' + f(effort) + ' kN') + text(484, 32, 'Q=' + p.Q + ' kN') + '</svg>';
          } else if (kind === 'stage') {
            var base = p.dead * L / 2, live = p.temp * L / 2;
            var RA = base + live + p.P * (L - a) / (L || 1);
            var RB = base + live + p.P * a / (L || 1);
            result = 'Stage A (permanent dead load): RA = RB = ' + f(base) + ' kN\nStage B (transient erection loads): RA = ' + f(RA) + ' kN, RB = ' + f(RB) + ' kN\nTotal Stage B vertical action = ' + f((p.dead + p.temp) * L + p.P) + ' kN.';
            svg = '<svg viewBox="0 0 640 240">' + line(75, 140, 560, 140) + line(75, 120, 560, 120, '#5c94a4') + line(75 + 485 * a / (L || 1), 38, 75 + 485 * a / (L || 1), 130, '#b06546') +
                  text(85, 50, 'Dead=' + p.dead + ' kN/m') + text(270, 70, 'Temp=' + p.temp + ' kN/m') + text(85, 210, 'RA=' + f(RA)) + text(470, 210, 'RB=' + f(RB)) + '</svg>';
          }
          if (diagramEl) diagramEl.innerHTML = svg;
          if (outEl) outEl.textContent = result;
        }
        ranges.forEach(function(r) { r.addEventListener('input', rec); });
        rec();
      } catch (err) {
        console.warn('Statics sim error in model ' + m.idx + ':', err);
      }
    }
  });
  MODELS.push({
    idx: 6,
    unit: 6,
    kind: 'stability',
    html: "<div class=\\\"sim-header\\\"><span class=\\\"badge\\\">Model 06 \u00b7 Unit 6</span><h3>Friction, Sliding and Overturning Stability</h3><p>Equilibrium comparison of available Coulomb interface friction and overturning moments on a gravity retaining block.</p></div><section class=\\\"sim-controls\\\"><label class=\"control\">Weight W (kN): <strong id=\"v_W\">100</strong><input id=\"W\" type=\"range\" min=\"30\" max=\"300\" step=\"5\" value=\"100\" aria-label=\"Weight W (kN)\"></label><label class=\"control\">Interface friction coefficient \u03bc: <strong id=\"v_mu\">0.35</strong><input id=\"mu\" type=\"range\" min=\"0.1\" max=\"0.8\" step=\"0.05\" value=\"0.35\" aria-label=\"Interface friction coefficient \u03bc\"></label><label class=\"control\">Horizontal push H (kN): <strong id=\"v_H\">25</strong><input id=\"H\" type=\"range\" min=\"5\" max=\"120\" step=\"5\" value=\"25\" aria-label=\"Horizontal push H (kN)\"></label><label class=\"control\">Push height h (m): <strong id=\"v_h\">2</strong><input id=\"h\" type=\"range\" min=\"0.5\" max=\"5\" step=\"0.25\" value=\"2\" aria-label=\"Push height h (m)\"></label><label class=\"control\">Base width B (m): <strong id=\"v_B\">3</strong><input id=\"B\" type=\"range\" min=\"1\" max=\"6\" step=\"0.25\" value=\"3\" aria-label=\"Base width B (m)\"></label></section><div class=\\\"diagram\\\" style=\\\"margin:1rem 0;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:0.5rem;\\\"></div><div class=\\\"readouts\\\"><div class=\\\"stat-box out\\\" style=\\\"width:100%;white-space:pre-line;line-height:1.6;font-family:monospace;font-size:0.875rem;\\\"></div></div>",
    init: function(card) {
      try {
        var ranges = Array.prototype.slice.call(card.querySelectorAll('input[type="range"]'));
        var diagramEl = card.querySelector('.diagram');
        var outEl = card.querySelector('.out');
        function rec() {
          var p = {};
          ranges.forEach(function(r) {
            p[r.id] = Number(r.value);
            var vEl = card.querySelector('#v_' + r.id);
            if (vEl) vEl.textContent = r.value;
          });
          var L = p.L || 0, a = Math.min(p.a || 0, L);
          var svg = '', result = '';
          var kind = 'stability';
          if (kind === 'trapezoid') {
            var W = (p.q1 + p.q2) * L / 2;
            var xx = (p.q1 + p.q2) > 0 ? L * (p.q1 + 2 * p.q2) / (3 * (p.q1 + p.q2)) : 0;
            result = 'Equivalent downward resultant W = ' + f(W) + ' kN\nLocation x̄ = ' + f(xx) + ' m from left\nVerification check: uniform loading yields x̄ = L/2';
            svg = '<svg viewBox="0 0 640 240"><polygon points="80,190 550,190 550,' + (185 - 12 * p.q2) + ' 80,' + (185 - 12 * p.q1) + '" fill="#d5edf2" stroke="#287589" stroke-width="3"/>' +
                  line(80, 190, 550, 190) + text(85, 220, 'Left q1=' + p.q1 + ' kN/m') + text(450, 220, 'Right q2=' + p.q2 + ' kN/m') + text(260, 44, 'W=' + f(W) + ' kN at x=' + f(xx) + ' m') + '</svg>';
          } else if (kind === 'beam') {
            var RA = p.w * L / 2 + p.P * (L - a) / (L || 1);
            var RB = p.w * L / 2 + p.P * a / (L || 1);
            result = 'Left support reaction RA = ' + f(RA) + ' kN\nRight support reaction RB = ' + f(RB) + ' kN\nGlobal equilibrium check: RA + RB = ' + f(RA + RB) + ' kN = wL + P';
            svg = '<svg viewBox="0 0 640 240">' + line(75, 150, 560, 150) + '<polygon points="75,152 60,175 90,175" fill="#2f7184"/><polygon points="560,152 545,175 575,175" fill="#2f7184"/>' +
                  line(75 + 485 * a / (L || 1), 50, 75 + 485 * a / (L || 1), 140, '#b06546') + text(75 + 485 * a / (L || 1), 38, 'P=' + p.P + ' kN') + text(230, 190, 'w=' + p.w + ' kN/m') +
                  text(70, 215, 'RA=' + f(RA)) + text(505, 215, 'RB=' + f(RB)) + '</svg>';
          } else if (kind === 'truss') {
            var th = p.theta * Math.PI / 180;
            var F = p.P / (2 * Math.sin(th));
            result = 'Axial compression magnitude in symmetrical diagonals = ' + f(F) + ' kN\nVertical support reaction per joint = ' + f(p.P / 2) + ' kN\nDeterminacy note: static equilibrium of concurrent joint system.';
            var dx = 190 * Math.cos(th), dy = 190 * Math.sin(th);
            svg = '<svg viewBox="0 0 640 240">' + line(320 - dx, 205, 320, 205 - dy) + line(320, 205 - dy, 320 + dx, 205) + line(320, 30, 320, 196, '#b06546') +
                  text(325, 25, 'P=' + p.P + ' kN') + text(48, 232, 'Diagonal axial force |N| = ' + f(F) + ' kN') + '</svg>';
          } else if (kind === 'cable') {
            var H = p.w * L * L / (8 * (p.f || 0.1));
            var V = p.w * L / 2;
            var T = Math.hypot(H, V);
            result = 'Horizontal cable tension component H = ' + f(H) + ' kN\nVertical reaction at each anchor V = ' + f(V) + ' kN\nMaximum end tension T = ' + f(T) + ' kN\nFormulation: uniform vertical dead load per horizontal metre.';
            var d = 'M 70 65 Q 320 ' + (65 + p.f * 14) + ' 570 65';
            svg = '<svg viewBox="0 0 640 240"><path d="' + d + '" fill="none" stroke="#2a788c" stroke-width="4"/>' + line(70, 65, 70, 220) + line(570, 65, 570, 220) +
                  text(230, 200, 'Sag f=' + p.f + ' m') + text(230, 226, 'H=' + f(H) + ' kN') + '</svg>';
          } else if (kind === 'section') {
            var hw = p.h - p.tf;
            var Af = p.b * p.tf, Aw = p.tw * hw, A = Af + Aw;
            var yf = p.h - p.tf / 2, yw = hw / 2;
            var y = (Af * yf + Aw * yw) / (A || 1);
            var If = p.b * Math.pow(p.tf, 3) / 12 + Af * Math.pow(yf - y, 2);
            var Iw = p.tw * Math.pow(hw, 3) / 12 + Aw * Math.pow(yw - y, 2);
            var I = If + Iw;
            result = 'Total cross-sectional area A = ' + f(A) + ' mm²\nCentroid elevation ȳ = ' + f(y) + ' mm from bottom fiber\nCentroidal second moment of area Ixx = ' + f(I) + ' mm⁴\nFormulation: parallel-axis theorem summation.';
            var fx = 320 - p.b * 0.6, fy = 215 - p.h * 0.6;
            svg = '<svg viewBox="0 0 640 240"><rect x="' + (320 - p.tw * 0.6 / 2) + '" y="' + (fy + p.tf * 0.6) + '" width="' + (p.tw * 0.6) + '" height="' + (hw * 0.6) + '" fill="#9fcdd8"/>' +
                  '<rect x="' + fx + '" y="' + fy + '" width="' + (p.b * 0.6) + '" height="' + (p.tf * 0.6) + '" fill="#367f92"/>' +
                  line(120, 215 - y * 0.6, 520, 215 - y * 0.6, '#b06546') + text(340, 215 - y * 0.6 - 7, 'Centroid ȳ=' + f(y) + ' mm') + '</svg>';
          } else if (kind === 'stability') {
            var F = p.mu * p.W, ms = p.W * p.B / 2, mo = p.H * p.h;
            var rs = F / (p.H || 1), rm = ms / (mo || 1);
            result = 'Available interface friction capacity μW = ' + f(F) + ' kN\nSliding safety ratio μW / H = ' + f(rs) + '\nStabilizing gravity moment W·B/2 = ' + f(ms) + ' kN·m\nOverturning moment H·h = ' + f(mo) + ' kN·m\nOverturning safety ratio = ' + f(rm) + '\nEducational screening: assumes rigid footing contact.';
            svg = '<svg viewBox="0 0 640 240"><rect x="180" y="75" width="250" height="130" fill="#b9dce5" stroke="#34788a"/>' +
                  line(95, 190, 520, 190) + line(400, 99, 510, 99, '#b06546') + text(400, 79, 'H=' + p.H + ' kN') + text(260, 50, 'W=' + p.W + ' kN') + text(100, 231, 'Sliding ratio = ' + f(rs)) + '</svg>';
          } else if (kind === 'lever') {
            var effort = p.Q * p.b / (p.a || 1);
            result = 'Ideal equilibrium effort = Q·b/a = ' + f(effort) + ' kN\nKinematic displacement ratio δx_effort / δx_load = a/b = ' + f(p.a / (p.b || 1)) + '\nPrinciple of virtual work: effort × δx_effort = resistance × δx_load.';
            svg = '<svg viewBox="0 0 640 240">' + line(80, 135, 560, 135) + '<polygon points="310,137 290,177 330,177" fill="#377b8c"/>' +
                  line(100, 35, 100, 125, '#b06546') + line(520, 50, 520, 130, '#21697b') + text(70, 22, 'Effort = ' + f(effort) + ' kN') + text(484, 32, 'Q=' + p.Q + ' kN') + '</svg>';
          } else if (kind === 'stage') {
            var base = p.dead * L / 2, live = p.temp * L / 2;
            var RA = base + live + p.P * (L - a) / (L || 1);
            var RB = base + live + p.P * a / (L || 1);
            result = 'Stage A (permanent dead load): RA = RB = ' + f(base) + ' kN\nStage B (transient erection loads): RA = ' + f(RA) + ' kN, RB = ' + f(RB) + ' kN\nTotal Stage B vertical action = ' + f((p.dead + p.temp) * L + p.P) + ' kN.';
            svg = '<svg viewBox="0 0 640 240">' + line(75, 140, 560, 140) + line(75, 120, 560, 120, '#5c94a4') + line(75 + 485 * a / (L || 1), 38, 75 + 485 * a / (L || 1), 130, '#b06546') +
                  text(85, 50, 'Dead=' + p.dead + ' kN/m') + text(270, 70, 'Temp=' + p.temp + ' kN/m') + text(85, 210, 'RA=' + f(RA)) + text(470, 210, 'RB=' + f(RB)) + '</svg>';
          }
          if (diagramEl) diagramEl.innerHTML = svg;
          if (outEl) outEl.textContent = result;
        }
        ranges.forEach(function(r) { r.addEventListener('input', rec); });
        rec();
      } catch (err) {
        console.warn('Statics sim error in model ' + m.idx + ':', err);
      }
    }
  });
  MODELS.push({
    idx: 7,
    unit: 7,
    kind: 'lever',
    html: "<div class=\\\"sim-header\\\"><span class=\\\"badge\\\">Model 07 \u00b7 Unit 7</span><h3>Virtual Work Equilibrium of a Lever</h3><p>Principle of virtual work equating virtual work of effort and resistance under kinematically admissible virtual displacements.</p></div><section class=\\\"sim-controls\\\"><label class=\"control\">Resistance Q (kN): <strong id=\"v_Q\">20</strong><input id=\"Q\" type=\"range\" min=\"1\" max=\"50\" step=\"1\" value=\"20\" aria-label=\"Resistance Q (kN)\"></label><label class=\"control\">Effort arm a (m): <strong id=\"v_a\">3</strong><input id=\"a\" type=\"range\" min=\"0.5\" max=\"5\" step=\"0.25\" value=\"3\" aria-label=\"Effort arm a (m)\"></label><label class=\"control\">Resistance arm b (m): <strong id=\"v_b\">1</strong><input id=\"b\" type=\"range\" min=\"0.2\" max=\"3\" step=\"0.1\" value=\"1\" aria-label=\"Resistance arm b (m)\"></label></section><div class=\\\"diagram\\\" style=\\\"margin:1rem 0;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:0.5rem;\\\"></div><div class=\\\"readouts\\\"><div class=\\\"stat-box out\\\" style=\\\"width:100%;white-space:pre-line;line-height:1.6;font-family:monospace;font-size:0.875rem;\\\"></div></div>",
    init: function(card) {
      try {
        var ranges = Array.prototype.slice.call(card.querySelectorAll('input[type="range"]'));
        var diagramEl = card.querySelector('.diagram');
        var outEl = card.querySelector('.out');
        function rec() {
          var p = {};
          ranges.forEach(function(r) {
            p[r.id] = Number(r.value);
            var vEl = card.querySelector('#v_' + r.id);
            if (vEl) vEl.textContent = r.value;
          });
          var L = p.L || 0, a = Math.min(p.a || 0, L);
          var svg = '', result = '';
          var kind = 'lever';
          if (kind === 'trapezoid') {
            var W = (p.q1 + p.q2) * L / 2;
            var xx = (p.q1 + p.q2) > 0 ? L * (p.q1 + 2 * p.q2) / (3 * (p.q1 + p.q2)) : 0;
            result = 'Equivalent downward resultant W = ' + f(W) + ' kN\nLocation x̄ = ' + f(xx) + ' m from left\nVerification check: uniform loading yields x̄ = L/2';
            svg = '<svg viewBox="0 0 640 240"><polygon points="80,190 550,190 550,' + (185 - 12 * p.q2) + ' 80,' + (185 - 12 * p.q1) + '" fill="#d5edf2" stroke="#287589" stroke-width="3"/>' +
                  line(80, 190, 550, 190) + text(85, 220, 'Left q1=' + p.q1 + ' kN/m') + text(450, 220, 'Right q2=' + p.q2 + ' kN/m') + text(260, 44, 'W=' + f(W) + ' kN at x=' + f(xx) + ' m') + '</svg>';
          } else if (kind === 'beam') {
            var RA = p.w * L / 2 + p.P * (L - a) / (L || 1);
            var RB = p.w * L / 2 + p.P * a / (L || 1);
            result = 'Left support reaction RA = ' + f(RA) + ' kN\nRight support reaction RB = ' + f(RB) + ' kN\nGlobal equilibrium check: RA + RB = ' + f(RA + RB) + ' kN = wL + P';
            svg = '<svg viewBox="0 0 640 240">' + line(75, 150, 560, 150) + '<polygon points="75,152 60,175 90,175" fill="#2f7184"/><polygon points="560,152 545,175 575,175" fill="#2f7184"/>' +
                  line(75 + 485 * a / (L || 1), 50, 75 + 485 * a / (L || 1), 140, '#b06546') + text(75 + 485 * a / (L || 1), 38, 'P=' + p.P + ' kN') + text(230, 190, 'w=' + p.w + ' kN/m') +
                  text(70, 215, 'RA=' + f(RA)) + text(505, 215, 'RB=' + f(RB)) + '</svg>';
          } else if (kind === 'truss') {
            var th = p.theta * Math.PI / 180;
            var F = p.P / (2 * Math.sin(th));
            result = 'Axial compression magnitude in symmetrical diagonals = ' + f(F) + ' kN\nVertical support reaction per joint = ' + f(p.P / 2) + ' kN\nDeterminacy note: static equilibrium of concurrent joint system.';
            var dx = 190 * Math.cos(th), dy = 190 * Math.sin(th);
            svg = '<svg viewBox="0 0 640 240">' + line(320 - dx, 205, 320, 205 - dy) + line(320, 205 - dy, 320 + dx, 205) + line(320, 30, 320, 196, '#b06546') +
                  text(325, 25, 'P=' + p.P + ' kN') + text(48, 232, 'Diagonal axial force |N| = ' + f(F) + ' kN') + '</svg>';
          } else if (kind === 'cable') {
            var H = p.w * L * L / (8 * (p.f || 0.1));
            var V = p.w * L / 2;
            var T = Math.hypot(H, V);
            result = 'Horizontal cable tension component H = ' + f(H) + ' kN\nVertical reaction at each anchor V = ' + f(V) + ' kN\nMaximum end tension T = ' + f(T) + ' kN\nFormulation: uniform vertical dead load per horizontal metre.';
            var d = 'M 70 65 Q 320 ' + (65 + p.f * 14) + ' 570 65';
            svg = '<svg viewBox="0 0 640 240"><path d="' + d + '" fill="none" stroke="#2a788c" stroke-width="4"/>' + line(70, 65, 70, 220) + line(570, 65, 570, 220) +
                  text(230, 200, 'Sag f=' + p.f + ' m') + text(230, 226, 'H=' + f(H) + ' kN') + '</svg>';
          } else if (kind === 'section') {
            var hw = p.h - p.tf;
            var Af = p.b * p.tf, Aw = p.tw * hw, A = Af + Aw;
            var yf = p.h - p.tf / 2, yw = hw / 2;
            var y = (Af * yf + Aw * yw) / (A || 1);
            var If = p.b * Math.pow(p.tf, 3) / 12 + Af * Math.pow(yf - y, 2);
            var Iw = p.tw * Math.pow(hw, 3) / 12 + Aw * Math.pow(yw - y, 2);
            var I = If + Iw;
            result = 'Total cross-sectional area A = ' + f(A) + ' mm²\nCentroid elevation ȳ = ' + f(y) + ' mm from bottom fiber\nCentroidal second moment of area Ixx = ' + f(I) + ' mm⁴\nFormulation: parallel-axis theorem summation.';
            var fx = 320 - p.b * 0.6, fy = 215 - p.h * 0.6;
            svg = '<svg viewBox="0 0 640 240"><rect x="' + (320 - p.tw * 0.6 / 2) + '" y="' + (fy + p.tf * 0.6) + '" width="' + (p.tw * 0.6) + '" height="' + (hw * 0.6) + '" fill="#9fcdd8"/>' +
                  '<rect x="' + fx + '" y="' + fy + '" width="' + (p.b * 0.6) + '" height="' + (p.tf * 0.6) + '" fill="#367f92"/>' +
                  line(120, 215 - y * 0.6, 520, 215 - y * 0.6, '#b06546') + text(340, 215 - y * 0.6 - 7, 'Centroid ȳ=' + f(y) + ' mm') + '</svg>';
          } else if (kind === 'stability') {
            var F = p.mu * p.W, ms = p.W * p.B / 2, mo = p.H * p.h;
            var rs = F / (p.H || 1), rm = ms / (mo || 1);
            result = 'Available interface friction capacity μW = ' + f(F) + ' kN\nSliding safety ratio μW / H = ' + f(rs) + '\nStabilizing gravity moment W·B/2 = ' + f(ms) + ' kN·m\nOverturning moment H·h = ' + f(mo) + ' kN·m\nOverturning safety ratio = ' + f(rm) + '\nEducational screening: assumes rigid footing contact.';
            svg = '<svg viewBox="0 0 640 240"><rect x="180" y="75" width="250" height="130" fill="#b9dce5" stroke="#34788a"/>' +
                  line(95, 190, 520, 190) + line(400, 99, 510, 99, '#b06546') + text(400, 79, 'H=' + p.H + ' kN') + text(260, 50, 'W=' + p.W + ' kN') + text(100, 231, 'Sliding ratio = ' + f(rs)) + '</svg>';
          } else if (kind === 'lever') {
            var effort = p.Q * p.b / (p.a || 1);
            result = 'Ideal equilibrium effort = Q·b/a = ' + f(effort) + ' kN\nKinematic displacement ratio δx_effort / δx_load = a/b = ' + f(p.a / (p.b || 1)) + '\nPrinciple of virtual work: effort × δx_effort = resistance × δx_load.';
            svg = '<svg viewBox="0 0 640 240">' + line(80, 135, 560, 135) + '<polygon points="310,137 290,177 330,177" fill="#377b8c"/>' +
                  line(100, 35, 100, 125, '#b06546') + line(520, 50, 520, 130, '#21697b') + text(70, 22, 'Effort = ' + f(effort) + ' kN') + text(484, 32, 'Q=' + p.Q + ' kN') + '</svg>';
          } else if (kind === 'stage') {
            var base = p.dead * L / 2, live = p.temp * L / 2;
            var RA = base + live + p.P * (L - a) / (L || 1);
            var RB = base + live + p.P * a / (L || 1);
            result = 'Stage A (permanent dead load): RA = RB = ' + f(base) + ' kN\nStage B (transient erection loads): RA = ' + f(RA) + ' kN, RB = ' + f(RB) + ' kN\nTotal Stage B vertical action = ' + f((p.dead + p.temp) * L + p.P) + ' kN.';
            svg = '<svg viewBox="0 0 640 240">' + line(75, 140, 560, 140) + line(75, 120, 560, 120, '#5c94a4') + line(75 + 485 * a / (L || 1), 38, 75 + 485 * a / (L || 1), 130, '#b06546') +
                  text(85, 50, 'Dead=' + p.dead + ' kN/m') + text(270, 70, 'Temp=' + p.temp + ' kN/m') + text(85, 210, 'RA=' + f(RA)) + text(470, 210, 'RB=' + f(RB)) + '</svg>';
          }
          if (diagramEl) diagramEl.innerHTML = svg;
          if (outEl) outEl.textContent = result;
        }
        ranges.forEach(function(r) { r.addEventListener('input', rec); });
        rec();
      } catch (err) {
        console.warn('Statics sim error in model ' + m.idx + ':', err);
      }
    }
  });
  MODELS.push({
    idx: 8,
    unit: 8,
    kind: 'stage',
    html: "<div class=\\\"sim-header\\\"><span class=\\\"badge\\\">Model 08 \u00b7 Unit 8</span><h3>Stagewise Construction Load Balance</h3><p>Superposition of permanent dead actions and transient construction loads during sequential erection stages.</p></div><section class=\\\"sim-controls\\\"><label class=\"control\">Span L (m): <strong id=\"v_L\">7</strong><input id=\"L\" type=\"range\" min=\"3\" max=\"15\" step=\"0.5\" value=\"7\" aria-label=\"Span L (m)\"></label><label class=\"control\">Permanent line load (kN/m): <strong id=\"v_dead\">1.5</strong><input id=\"dead\" type=\"range\" min=\"0\" max=\"6\" step=\"0.25\" value=\"1.5\" aria-label=\"Permanent line load (kN/m)\"></label><label class=\"control\">Temporary added line load (kN/m): <strong id=\"v_temp\">4</strong><input id=\"temp\" type=\"range\" min=\"0\" max=\"10\" step=\"0.5\" value=\"4\" aria-label=\"Temporary added line load (kN/m)\"></label><label class=\"control\">Temporary point load P (kN): <strong id=\"v_P\">8</strong><input id=\"P\" type=\"range\" min=\"0\" max=\"30\" step=\"1\" value=\"8\" aria-label=\"Temporary point load P (kN)\"></label><label class=\"control\">Point position a (m): <strong id=\"v_a\">3</strong><input id=\"a\" type=\"range\" min=\"0\" max=\"7\" step=\"0.5\" value=\"3\" aria-label=\"Point position a (m)\"></label></section><div class=\\\"diagram\\\" style=\\\"margin:1rem 0;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:0.5rem;\\\"></div><div class=\\\"readouts\\\"><div class=\\\"stat-box out\\\" style=\\\"width:100%;white-space:pre-line;line-height:1.6;font-family:monospace;font-size:0.875rem;\\\"></div></div>",
    init: function(card) {
      try {
        var ranges = Array.prototype.slice.call(card.querySelectorAll('input[type="range"]'));
        var diagramEl = card.querySelector('.diagram');
        var outEl = card.querySelector('.out');
        function rec() {
          var p = {};
          ranges.forEach(function(r) {
            p[r.id] = Number(r.value);
            var vEl = card.querySelector('#v_' + r.id);
            if (vEl) vEl.textContent = r.value;
          });
          var L = p.L || 0, a = Math.min(p.a || 0, L);
          var svg = '', result = '';
          var kind = 'stage';
          if (kind === 'trapezoid') {
            var W = (p.q1 + p.q2) * L / 2;
            var xx = (p.q1 + p.q2) > 0 ? L * (p.q1 + 2 * p.q2) / (3 * (p.q1 + p.q2)) : 0;
            result = 'Equivalent downward resultant W = ' + f(W) + ' kN\nLocation x̄ = ' + f(xx) + ' m from left\nVerification check: uniform loading yields x̄ = L/2';
            svg = '<svg viewBox="0 0 640 240"><polygon points="80,190 550,190 550,' + (185 - 12 * p.q2) + ' 80,' + (185 - 12 * p.q1) + '" fill="#d5edf2" stroke="#287589" stroke-width="3"/>' +
                  line(80, 190, 550, 190) + text(85, 220, 'Left q1=' + p.q1 + ' kN/m') + text(450, 220, 'Right q2=' + p.q2 + ' kN/m') + text(260, 44, 'W=' + f(W) + ' kN at x=' + f(xx) + ' m') + '</svg>';
          } else if (kind === 'beam') {
            var RA = p.w * L / 2 + p.P * (L - a) / (L || 1);
            var RB = p.w * L / 2 + p.P * a / (L || 1);
            result = 'Left support reaction RA = ' + f(RA) + ' kN\nRight support reaction RB = ' + f(RB) + ' kN\nGlobal equilibrium check: RA + RB = ' + f(RA + RB) + ' kN = wL + P';
            svg = '<svg viewBox="0 0 640 240">' + line(75, 150, 560, 150) + '<polygon points="75,152 60,175 90,175" fill="#2f7184"/><polygon points="560,152 545,175 575,175" fill="#2f7184"/>' +
                  line(75 + 485 * a / (L || 1), 50, 75 + 485 * a / (L || 1), 140, '#b06546') + text(75 + 485 * a / (L || 1), 38, 'P=' + p.P + ' kN') + text(230, 190, 'w=' + p.w + ' kN/m') +
                  text(70, 215, 'RA=' + f(RA)) + text(505, 215, 'RB=' + f(RB)) + '</svg>';
          } else if (kind === 'truss') {
            var th = p.theta * Math.PI / 180;
            var F = p.P / (2 * Math.sin(th));
            result = 'Axial compression magnitude in symmetrical diagonals = ' + f(F) + ' kN\nVertical support reaction per joint = ' + f(p.P / 2) + ' kN\nDeterminacy note: static equilibrium of concurrent joint system.';
            var dx = 190 * Math.cos(th), dy = 190 * Math.sin(th);
            svg = '<svg viewBox="0 0 640 240">' + line(320 - dx, 205, 320, 205 - dy) + line(320, 205 - dy, 320 + dx, 205) + line(320, 30, 320, 196, '#b06546') +
                  text(325, 25, 'P=' + p.P + ' kN') + text(48, 232, 'Diagonal axial force |N| = ' + f(F) + ' kN') + '</svg>';
          } else if (kind === 'cable') {
            var H = p.w * L * L / (8 * (p.f || 0.1));
            var V = p.w * L / 2;
            var T = Math.hypot(H, V);
            result = 'Horizontal cable tension component H = ' + f(H) + ' kN\nVertical reaction at each anchor V = ' + f(V) + ' kN\nMaximum end tension T = ' + f(T) + ' kN\nFormulation: uniform vertical dead load per horizontal metre.';
            var d = 'M 70 65 Q 320 ' + (65 + p.f * 14) + ' 570 65';
            svg = '<svg viewBox="0 0 640 240"><path d="' + d + '" fill="none" stroke="#2a788c" stroke-width="4"/>' + line(70, 65, 70, 220) + line(570, 65, 570, 220) +
                  text(230, 200, 'Sag f=' + p.f + ' m') + text(230, 226, 'H=' + f(H) + ' kN') + '</svg>';
          } else if (kind === 'section') {
            var hw = p.h - p.tf;
            var Af = p.b * p.tf, Aw = p.tw * hw, A = Af + Aw;
            var yf = p.h - p.tf / 2, yw = hw / 2;
            var y = (Af * yf + Aw * yw) / (A || 1);
            var If = p.b * Math.pow(p.tf, 3) / 12 + Af * Math.pow(yf - y, 2);
            var Iw = p.tw * Math.pow(hw, 3) / 12 + Aw * Math.pow(yw - y, 2);
            var I = If + Iw;
            result = 'Total cross-sectional area A = ' + f(A) + ' mm²\nCentroid elevation ȳ = ' + f(y) + ' mm from bottom fiber\nCentroidal second moment of area Ixx = ' + f(I) + ' mm⁴\nFormulation: parallel-axis theorem summation.';
            var fx = 320 - p.b * 0.6, fy = 215 - p.h * 0.6;
            svg = '<svg viewBox="0 0 640 240"><rect x="' + (320 - p.tw * 0.6 / 2) + '" y="' + (fy + p.tf * 0.6) + '" width="' + (p.tw * 0.6) + '" height="' + (hw * 0.6) + '" fill="#9fcdd8"/>' +
                  '<rect x="' + fx + '" y="' + fy + '" width="' + (p.b * 0.6) + '" height="' + (p.tf * 0.6) + '" fill="#367f92"/>' +
                  line(120, 215 - y * 0.6, 520, 215 - y * 0.6, '#b06546') + text(340, 215 - y * 0.6 - 7, 'Centroid ȳ=' + f(y) + ' mm') + '</svg>';
          } else if (kind === 'stability') {
            var F = p.mu * p.W, ms = p.W * p.B / 2, mo = p.H * p.h;
            var rs = F / (p.H || 1), rm = ms / (mo || 1);
            result = 'Available interface friction capacity μW = ' + f(F) + ' kN\nSliding safety ratio μW / H = ' + f(rs) + '\nStabilizing gravity moment W·B/2 = ' + f(ms) + ' kN·m\nOverturning moment H·h = ' + f(mo) + ' kN·m\nOverturning safety ratio = ' + f(rm) + '\nEducational screening: assumes rigid footing contact.';
            svg = '<svg viewBox="0 0 640 240"><rect x="180" y="75" width="250" height="130" fill="#b9dce5" stroke="#34788a"/>' +
                  line(95, 190, 520, 190) + line(400, 99, 510, 99, '#b06546') + text(400, 79, 'H=' + p.H + ' kN') + text(260, 50, 'W=' + p.W + ' kN') + text(100, 231, 'Sliding ratio = ' + f(rs)) + '</svg>';
          } else if (kind === 'lever') {
            var effort = p.Q * p.b / (p.a || 1);
            result = 'Ideal equilibrium effort = Q·b/a = ' + f(effort) + ' kN\nKinematic displacement ratio δx_effort / δx_load = a/b = ' + f(p.a / (p.b || 1)) + '\nPrinciple of virtual work: effort × δx_effort = resistance × δx_load.';
            svg = '<svg viewBox="0 0 640 240">' + line(80, 135, 560, 135) + '<polygon points="310,137 290,177 330,177" fill="#377b8c"/>' +
                  line(100, 35, 100, 125, '#b06546') + line(520, 50, 520, 130, '#21697b') + text(70, 22, 'Effort = ' + f(effort) + ' kN') + text(484, 32, 'Q=' + p.Q + ' kN') + '</svg>';
          } else if (kind === 'stage') {
            var base = p.dead * L / 2, live = p.temp * L / 2;
            var RA = base + live + p.P * (L - a) / (L || 1);
            var RB = base + live + p.P * a / (L || 1);
            result = 'Stage A (permanent dead load): RA = RB = ' + f(base) + ' kN\nStage B (transient erection loads): RA = ' + f(RA) + ' kN, RB = ' + f(RB) + ' kN\nTotal Stage B vertical action = ' + f((p.dead + p.temp) * L + p.P) + ' kN.';
            svg = '<svg viewBox="0 0 640 240">' + line(75, 140, 560, 140) + line(75, 120, 560, 120, '#5c94a4') + line(75 + 485 * a / (L || 1), 38, 75 + 485 * a / (L || 1), 130, '#b06546') +
                  text(85, 50, 'Dead=' + p.dead + ' kN/m') + text(270, 70, 'Temp=' + p.temp + ' kN/m') + text(85, 210, 'RA=' + f(RA)) + text(470, 210, 'RB=' + f(RB)) + '</svg>';
          }
          if (diagramEl) diagramEl.innerHTML = svg;
          if (outEl) outEl.textContent = result;
        }
        ranges.forEach(function(r) { r.addEventListener('input', rec); });
        rec();
      } catch (err) {
        console.warn('Statics sim error in model ' + m.idx + ':', err);
      }
    }
  });
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
      card.className = 'ce-sim-card';
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
