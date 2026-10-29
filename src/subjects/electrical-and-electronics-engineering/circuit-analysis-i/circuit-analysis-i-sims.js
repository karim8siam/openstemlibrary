/* Circuit Analysis I Interactive Simulation Suite */
(function(window) {
  'use strict';

  function compute(id, p) {
    const {V=0, R=1, I=0, S=1, R1=1, R2=1, RL=1, V1=0, V2=0, RS=1, C=1, L=1, T=0, RM=1} = p;
    const f = (x, n=4) => Number(x).toPrecision(n);
    const graph = (fn, start=0, end=1) => Array.from({length: 101}, (_, i) => [start + (end - start) * i / 100, fn(start + (end - start) * i / 100)]);
    switch(id) {
      case 1: return {a: ['Current', f(V / R) + ' A'], b: ['Resistor power', f(V * V / R) + ' W'], points: graph(x => x / R, 0, 24), ylabel: 'I (A)'};
      case 2: return {a: ['Signed power', f(V * I * Math.sign(S || 1)) + ' W'], b: ['Interpretation', V * I * Math.sign(S || 1) >= 0 ? 'absorption' : 'delivery'], points: graph(x => x * I * Math.sign(S || 1), -24, 24), ylabel: 'P (W)'};
      case 3: { let eq = R2 * RL / (R2 + RL); return {a: ['Loaded output', f(V * eq / (R1 + eq)) + ' V'], b: ['Unloaded output', f(V * R2 / (R1 + R2)) + ' V'], points: graph(x => x * eq / (R1 + eq), 0, 24), ylabel: 'Vout (V)'}; }
      case 4: return {a: ['Series equivalent', f(R1 + R2) + ' Ω'], b: ['Parallel equivalent', f(R1 * R2 / (R1 + R2)) + ' Ω'], points: graph(x => R1 * x / (R1 + x), 1, 1000), ylabel: 'parallel R (Ω)'};
      case 5: { let x = V * R2 / (R1 + R2); return {a: ['Node voltage', f(x) + ' V'], b: ['KCL residual', f((x - V) / R1 + x / R2) + ' A'], points: graph(y => y * R2 / (R1 + R2), 0, 24), ylabel: 'Vnode (V)'}; }
      case 6: { let a = R1 + RS, b = R2 + RS, d = a * b - RS * RS, i1 = (V1 * b + RS * V2) / d, i2 = (V2 * a + RS * V1) / d; return {a: ['Mesh 1 current', f(i1) + ' A'], b: ['Mesh 2 current', f(i2) + ' A'], points: graph(x => (x * b + RS * V2) / d, 0, 24), ylabel: 'I1 (A)'}; }
      case 7: { let vl = V * RL / (R + RL); return {a: ['Load voltage', f(vl) + ' V'], b: ['Load power', f(vl * vl / RL) + ' W'], points: graph(x => V * x / (R + x), 1, 100), ylabel: 'Vload (V)'}; }
      case 8: { let pow = V * V * RL / (R + RL)**2; return {a: ['Load power', f(pow) + ' W'], b: ['Delivery efficiency', f(100 * RL / (R + RL)) + ' %'], points: graph(x => V * V * x / (R + x)**2, 1, 100), ylabel: 'Pload (W)'}; }
      case 9: return {a: ['Charge', f(C * 1e-6 * V * 1e3) + ' mC'], b: ['Stored energy', f(0.5 * C * 1e-6 * V * V * 1e3) + ' mJ'], points: graph(x => 0.5 * C * 1e-6 * x * x * 1e3, 0, 30), ylabel: 'E (mJ)'};
      case 10: return {a: ['Stored energy', f(0.5 * L * 1e-3 * I * I * 1e3) + ' mJ'], b: ['Flux linkage', f(L * 1e-3 * I) + ' Wb·turn'], points: graph(x => 0.5 * L * 1e-3 * x * x * 1e3, 0, 10), ylabel: 'E (mJ)'};
      case 11: { let tau = R * 1000 * C * 1e-6; return {a: ['V(t)', f(V * (1 - Math.exp(-T / tau))) + ' V'], b: ['Time constant', f(tau) + ' s'], points: graph(t => V * (1 - Math.exp(-t / tau)), 0, Math.max(0.001, 5 * tau)), ylabel: 'Vc (V)'}; }
      case 12: { let tau = L * 0.001 / R, sec = T * 0.001; return {a: ['I(t)', f((V / R) * (1 - Math.exp(-sec / tau))) + ' A'], b: ['Time constant', f(tau * 1000) + ' ms'], points: graph(t => (V / R) * (1 - Math.exp(-t / tau)), 0, Math.max(0.00001, 5 * tau)), ylabel: 'IL (A)'}; }
      case 13: { let ll = L * 0.001, cc = C * 1e-6, alpha = R / (2 * ll), w = 1 / Math.sqrt(ll * cc), crit = 2 * Math.sqrt(ll / cc), state = alpha < w - 1e-8 ? 'underdamped' : alpha > w + 1e-8 ? 'overdamped' : 'critical'; return {a: ['Damping regime', state], b: ['Critical resistance', f(crit) + ' Ω'], points: graph(x => (x / (2 * ll)) / w, 0, 200), ylabel: 'ζ'}; }
      case 14: { let ll = L * 0.001, cc = C * 1e-6, alpha = R / (2 * ll), w = 1 / Math.sqrt(ll * cc); function calc(t) { if (alpha < w) { let wd = Math.sqrt(w * w - alpha * alpha); return V * Math.exp(-alpha * t) * (Math.cos(wd * t) + (alpha / wd) * Math.sin(wd * t)); } if (Math.abs(alpha - w) < 1e-9) return V * Math.exp(-alpha * t) * (1 + alpha * t); let beta = Math.sqrt(alpha * alpha - w * w); return V * Math.exp(-alpha * t) * (Math.cosh(beta * t) + (alpha / beta) * Math.sinh(beta * t)); } return {a: ['Capacitor voltage', f(calc(T * 0.001)) + ' V'], b: ['Damping ratio', f(alpha / w)], points: graph(t => calc(t), 0, 0.05), ylabel: 'Vc (V)'}; }
      case 15: { let eq = R2 * RM / (R2 + RM); return {a: ['Measured voltage', f(V * eq / (R1 + eq)) + ' V'], b: ['Unloaded voltage', f(V * R2 / (R1 + R2)) + ' V'], points: graph(x => V * (R2 * x / (R2 + x)) / (R1 + R2 * x / (R2 + x)), 100, 100000), ylabel: 'Measured V (V)'}; }
      case 16: { let tol = T / 100, high = V * (R2 * (1 + tol)) / (R1 * (1 - tol) + R2 * (1 + tol)), low = V * (R2 * (1 - tol)) / (R1 * (1 + tol) + R2 * (1 - tol)); return {a: ['Worst-case low', f(low) + ' V'], b: ['Worst-case high', f(high) + ' V'], points: graph(x => V * (R2 * (1 + x / 100)) / (R1 * (1 - x / 100) + R2 * (1 + x / 100)), 0, 20), ylabel: 'Vhigh (V)'}; }
      default: return {a: ['Output', '0'], b: ['Status', 'idle'], points: [], ylabel: 'V'};
    }
  }

  function renderGraph(points, ylabel) {
    const W = 700, H = 240, l = 55, r = 20, t = 20, b = 35;
    let xs = points.map(x => x[0]), ys = points.map(x => x[1]);
    let xmin = Math.min(...xs), xmax = Math.max(...xs), ymin = Math.min(0, ...ys), ymax = Math.max(0, ...ys);
    if (ymax - ymin < 1e-10) ymax = ymin + 1;
    const xx = x => l + (x - xmin) / (xmax - xmin || 1) * (W - l - r);
    const yy = y => t + (ymax - y) / (ymax - ymin) * (H - t - b);
    let d = points.map(([x, y], i) => (i ? 'L' : 'M') + xx(x).toFixed(2) + ',' + yy(y).toFixed(2)).join(' ');
    return `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Response curve" style="width:100%;height:auto;display:block">
      <rect x="${l}" y="${t}" width="${W - l - r}" height="${H - t - b}" fill="#0f172a" rx="4"/>` +
      Array.from({length: 5}, (_, i) => {
        let y = t + (H - t - b) * i / 4, val = ymax - (ymax - ymin) * i / 4;
        return `<line x1="${l}" y1="${y}" x2="${W - r}" y2="${y}" stroke="#1e293b"/>
                <text x="8" y="${y + 4}" font-size="11" fill="#64748b">${val.toPrecision(3)}</text>`;
      }).join('') +
      `<path d="${d}" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-linejoin="round"/>
       <text x="${l}" y="${H - 10}" fill="#94a3b8" font-size="11">input: ${xmin.toPrecision(3)} → ${xmax.toPrecision(3)}</text>
       <text x="${W - r}" y="${H - 10}" fill="#38bdf8" text-anchor="end" font-size="11">${ylabel}</text>
    </svg>`;
  }

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 01</span><h3>Ohm Law and Dissipation</h3><p>Current and heat from an ideal resistor. Change the inputs to test the relationship; the graph and values update immediately. All cases assume ideal lumped components.</p></div><div class=\"sim-controls\"><div class=\"param\"><label for=\"V\">Voltage <span id=\"v-V\">12 V</span></label><input data-param=\"V\" data-unit=\"V\" id=\"V\" type=\"range\" min=\"0\" max=\"24\" value=\"12\" step=\"0.024\"></div>\n<div class=\"param\"><label for=\"R\">Resistance <span id=\"v-R\">220 \u03a9</span></label><input data-param=\"R\" data-unit=\"\u03a9\" id=\"R\" type=\"range\" min=\"1\" max=\"1000\" value=\"220\" step=\"0.999\"></div></div><div class=\"readouts\"><div class=\"stat-box\" id=\"res-a\"><small>-</small><output>-</output></div><div class=\"stat-box\" id=\"res-b\"><small>-</small><output>-</output></div></div><div class=\"plot\" id=\"sim-chart\"></div>",
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        function update() {
          var p = {};
          inputs.forEach(function(el) {
            p[el.dataset.param] = Number(el.value);
            var vEl = card.querySelector('#v-' + el.dataset.param);
            if (vEl) vEl.textContent = el.value + ' ' + (el.dataset.unit || '');
          });
          var r = compute(1, p);
          var ra = card.querySelector('#res-a'), rb = card.querySelector('#res-b');
          if (ra && r.a) { ra.querySelector('small').textContent = r.a[0]; ra.querySelector('output').textContent = r.a[1]; }
          if (rb && r.b) { rb.querySelector('small').textContent = r.b[0]; rb.querySelector('output').textContent = r.b[1]; }
          var chart = card.querySelector('#sim-chart');
          if (chart && r.points) chart.innerHTML = renderGraph(r.points, r.ylabel);
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis I sim error in model 1:', err);
      }
    }
  });
  MODELS.push({
    idx: 2,
    unit: 1,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 02</span><h3>Passive Sign Convention</h3><p>Power positive means absorption only under consistent passive references. Change the inputs to test the relationship; the graph and values update immediately. All cases assume ideal lumped components.</p></div><div class=\"sim-controls\"><div class=\"param\"><label for=\"V\">Voltage <span id=\"v-V\">9 V</span></label><input data-param=\"V\" data-unit=\"V\" id=\"V\" type=\"range\" min=\"-24\" max=\"24\" value=\"9\" step=\"0.048\"></div>\n<div class=\"param\"><label for=\"I\">Current <span id=\"v-I\">0.3 A</span></label><input data-param=\"I\" data-unit=\"A\" id=\"I\" type=\"range\" min=\"-2\" max=\"2\" value=\"0.3\" step=\"0.004\"></div>\n<div class=\"param\"><label for=\"S\">Orientation <span id=\"v-S\">1 sign</span></label><input data-param=\"S\" data-unit=\"sign\" id=\"S\" type=\"range\" min=\"-1\" max=\"1\" value=\"1\" step=\"0.002\"></div></div><div class=\"readouts\"><div class=\"stat-box\" id=\"res-a\"><small>-</small><output>-</output></div><div class=\"stat-box\" id=\"res-b\"><small>-</small><output>-</output></div></div><div class=\"plot\" id=\"sim-chart\"></div>",
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        function update() {
          var p = {};
          inputs.forEach(function(el) {
            p[el.dataset.param] = Number(el.value);
            var vEl = card.querySelector('#v-' + el.dataset.param);
            if (vEl) vEl.textContent = el.value + ' ' + (el.dataset.unit || '');
          });
          var r = compute(2, p);
          var ra = card.querySelector('#res-a'), rb = card.querySelector('#res-b');
          if (ra && r.a) { ra.querySelector('small').textContent = r.a[0]; ra.querySelector('output').textContent = r.a[1]; }
          if (rb && r.b) { rb.querySelector('small').textContent = r.b[0]; rb.querySelector('output').textContent = r.b[1]; }
          var chart = card.querySelector('#sim-chart');
          if (chart && r.points) chart.innerHTML = renderGraph(r.points, r.ylabel);
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis I sim error in model 2:', err);
      }
    }
  });
  MODELS.push({
    idx: 3,
    unit: 2,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 03</span><h3>Loaded Voltage Divider</h3><p>A finite load changes the lower effective resistance. Change the inputs to test the relationship; the graph and values update immediately. All cases assume ideal lumped components.</p></div><div class=\"sim-controls\"><div class=\"param\"><label for=\"V\">Supply <span id=\"v-V\">12 V</span></label><input data-param=\"V\" data-unit=\"V\" id=\"V\" type=\"range\" min=\"1\" max=\"24\" value=\"12\" step=\"0.023\"></div>\n<div class=\"param\"><label for=\"R1\">Upper resistor <span id=\"v-R1\">10000 \u03a9</span></label><input data-param=\"R1\" data-unit=\"\u03a9\" id=\"R1\" type=\"range\" min=\"100\" max=\"20000\" value=\"10000\" step=\"19.9\"></div>\n<div class=\"param\"><label for=\"R2\">Lower resistor <span id=\"v-R2\">10000 \u03a9</span></label><input data-param=\"R2\" data-unit=\"\u03a9\" id=\"R2\" type=\"range\" min=\"100\" max=\"20000\" value=\"10000\" step=\"19.9\"></div>\n<div class=\"param\"><label for=\"RL\">Load <span id=\"v-RL\">20000 \u03a9</span></label><input data-param=\"RL\" data-unit=\"\u03a9\" id=\"RL\" type=\"range\" min=\"100\" max=\"100000\" value=\"20000\" step=\"99.9\"></div></div><div class=\"readouts\"><div class=\"stat-box\" id=\"res-a\"><small>-</small><output>-</output></div><div class=\"stat-box\" id=\"res-b\"><small>-</small><output>-</output></div></div><div class=\"plot\" id=\"sim-chart\"></div>",
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        function update() {
          var p = {};
          inputs.forEach(function(el) {
            p[el.dataset.param] = Number(el.value);
            var vEl = card.querySelector('#v-' + el.dataset.param);
            if (vEl) vEl.textContent = el.value + ' ' + (el.dataset.unit || '');
          });
          var r = compute(3, p);
          var ra = card.querySelector('#res-a'), rb = card.querySelector('#res-b');
          if (ra && r.a) { ra.querySelector('small').textContent = r.a[0]; ra.querySelector('output').textContent = r.a[1]; }
          if (rb && r.b) { rb.querySelector('small').textContent = r.b[0]; rb.querySelector('output').textContent = r.b[1]; }
          var chart = card.querySelector('#sim-chart');
          if (chart && r.points) chart.innerHTML = renderGraph(r.points, r.ylabel);
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis I sim error in model 3:', err);
      }
    }
  });
  MODELS.push({
    idx: 4,
    unit: 2,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 04</span><h3>Series and Parallel Resistors</h3><p>Topological relationship selects which equivalent applies. Change the inputs to test the relationship; the graph and values update immediately. All cases assume ideal lumped components.</p></div><div class=\"sim-controls\"><div class=\"param\"><label for=\"R1\">First resistor <span id=\"v-R1\">100 \u03a9</span></label><input data-param=\"R1\" data-unit=\"\u03a9\" id=\"R1\" type=\"range\" min=\"1\" max=\"1000\" value=\"100\" step=\"0.999\"></div>\n<div class=\"param\"><label for=\"R2\">Second resistor <span id=\"v-R2\">200 \u03a9</span></label><input data-param=\"R2\" data-unit=\"\u03a9\" id=\"R2\" type=\"range\" min=\"1\" max=\"1000\" value=\"200\" step=\"0.999\"></div></div><div class=\"readouts\"><div class=\"stat-box\" id=\"res-a\"><small>-</small><output>-</output></div><div class=\"stat-box\" id=\"res-b\"><small>-</small><output>-</output></div></div><div class=\"plot\" id=\"sim-chart\"></div>",
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        function update() {
          var p = {};
          inputs.forEach(function(el) {
            p[el.dataset.param] = Number(el.value);
            var vEl = card.querySelector('#v-' + el.dataset.param);
            if (vEl) vEl.textContent = el.value + ' ' + (el.dataset.unit || '');
          });
          var r = compute(4, p);
          var ra = card.querySelector('#res-a'), rb = card.querySelector('#res-b');
          if (ra && r.a) { ra.querySelector('small').textContent = r.a[0]; ra.querySelector('output').textContent = r.a[1]; }
          if (rb && r.b) { rb.querySelector('small').textContent = r.b[0]; rb.querySelector('output').textContent = r.b[1]; }
          var chart = card.querySelector('#sim-chart');
          if (chart && r.points) chart.innerHTML = renderGraph(r.points, r.ylabel);
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis I sim error in model 4:', err);
      }
    }
  });
  MODELS.push({
    idx: 5,
    unit: 3,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 05</span><h3>One-Node KCL</h3><p>The node potential satisfies a signed current balance. Change the inputs to test the relationship; the graph and values update immediately. All cases assume ideal lumped components.</p></div><div class=\"sim-controls\"><div class=\"param\"><label for=\"V\">Supply <span id=\"v-V\">10 V</span></label><input data-param=\"V\" data-unit=\"V\" id=\"V\" type=\"range\" min=\"1\" max=\"24\" value=\"10\" step=\"0.023\"></div>\n<div class=\"param\"><label for=\"R1\">Input resistance <span id=\"v-R1\">5 \u03a9</span></label><input data-param=\"R1\" data-unit=\"\u03a9\" id=\"R1\" type=\"range\" min=\"1\" max=\"500\" value=\"5\" step=\"0.499\"></div>\n<div class=\"param\"><label for=\"R2\">Ground resistance <span id=\"v-R2\">10 \u03a9</span></label><input data-param=\"R2\" data-unit=\"\u03a9\" id=\"R2\" type=\"range\" min=\"1\" max=\"500\" value=\"10\" step=\"0.499\"></div></div><div class=\"readouts\"><div class=\"stat-box\" id=\"res-a\"><small>-</small><output>-</output></div><div class=\"stat-box\" id=\"res-b\"><small>-</small><output>-</output></div></div><div class=\"plot\" id=\"sim-chart\"></div>",
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        function update() {
          var p = {};
          inputs.forEach(function(el) {
            p[el.dataset.param] = Number(el.value);
            var vEl = card.querySelector('#v-' + el.dataset.param);
            if (vEl) vEl.textContent = el.value + ' ' + (el.dataset.unit || '');
          });
          var r = compute(5, p);
          var ra = card.querySelector('#res-a'), rb = card.querySelector('#res-b');
          if (ra && r.a) { ra.querySelector('small').textContent = r.a[0]; ra.querySelector('output').textContent = r.a[1]; }
          if (rb && r.b) { rb.querySelector('small').textContent = r.b[0]; rb.querySelector('output').textContent = r.b[1]; }
          var chart = card.querySelector('#sim-chart');
          if (chart && r.points) chart.innerHTML = renderGraph(r.points, r.ylabel);
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis I sim error in model 5:', err);
      }
    }
  });
  MODELS.push({
    idx: 6,
    unit: 3,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 06</span><h3>Coupled Mesh Currents</h3><p>Shared resistance couples two independent clockwise mesh currents. Change the inputs to test the relationship; the graph and values update immediately. All cases assume ideal lumped components.</p></div><div class=\"sim-controls\"><div class=\"param\"><label for=\"V1\">First source <span id=\"v-V1\">12 V</span></label><input data-param=\"V1\" data-unit=\"V\" id=\"V1\" type=\"range\" min=\"0\" max=\"24\" value=\"12\" step=\"0.024\"></div>\n<div class=\"param\"><label for=\"V2\">Second source <span id=\"v-V2\">6 V</span></label><input data-param=\"V2\" data-unit=\"V\" id=\"V2\" type=\"range\" min=\"0\" max=\"24\" value=\"6\" step=\"0.024\"></div>\n<div class=\"param\"><label for=\"R1\">Mesh resistance A <span id=\"v-R1\">8 \u03a9</span></label><input data-param=\"R1\" data-unit=\"\u03a9\" id=\"R1\" type=\"range\" min=\"1\" max=\"100\" value=\"8\" step=\"0.099\"></div>\n<div class=\"param\"><label for=\"R2\">Mesh resistance B <span id=\"v-R2\">12 \u03a9</span></label><input data-param=\"R2\" data-unit=\"\u03a9\" id=\"R2\" type=\"range\" min=\"1\" max=\"100\" value=\"12\" step=\"0.099\"></div>\n<div class=\"param\"><label for=\"RS\">Shared resistor <span id=\"v-RS\">4 \u03a9</span></label><input data-param=\"RS\" data-unit=\"\u03a9\" id=\"RS\" type=\"range\" min=\"1\" max=\"100\" value=\"4\" step=\"0.099\"></div></div><div class=\"readouts\"><div class=\"stat-box\" id=\"res-a\"><small>-</small><output>-</output></div><div class=\"stat-box\" id=\"res-b\"><small>-</small><output>-</output></div></div><div class=\"plot\" id=\"sim-chart\"></div>",
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        function update() {
          var p = {};
          inputs.forEach(function(el) {
            p[el.dataset.param] = Number(el.value);
            var vEl = card.querySelector('#v-' + el.dataset.param);
            if (vEl) vEl.textContent = el.value + ' ' + (el.dataset.unit || '');
          });
          var r = compute(6, p);
          var ra = card.querySelector('#res-a'), rb = card.querySelector('#res-b');
          if (ra && r.a) { ra.querySelector('small').textContent = r.a[0]; ra.querySelector('output').textContent = r.a[1]; }
          if (rb && r.b) { rb.querySelector('small').textContent = r.b[0]; rb.querySelector('output').textContent = r.b[1]; }
          var chart = card.querySelector('#sim-chart');
          if (chart && r.points) chart.innerHTML = renderGraph(r.points, r.ylabel);
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis I sim error in model 6:', err);
      }
    }
  });
  MODELS.push({
    idx: 7,
    unit: 4,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 07</span><h3>Thevenin Loaded Network</h3><p>Equivalent terminal voltage changes with loading. Change the inputs to test the relationship; the graph and values update immediately. All cases assume ideal lumped components.</p></div><div class=\"sim-controls\"><div class=\"param\"><label for=\"V\">Thevenin voltage <span id=\"v-V\">12 V</span></label><input data-param=\"V\" data-unit=\"V\" id=\"V\" type=\"range\" min=\"1\" max=\"30\" value=\"12\" step=\"0.029\"></div>\n<div class=\"param\"><label for=\"R\">Source resistance <span id=\"v-R\">6 \u03a9</span></label><input data-param=\"R\" data-unit=\"\u03a9\" id=\"R\" type=\"range\" min=\"1\" max=\"100\" value=\"6\" step=\"0.099\"></div>\n<div class=\"param\"><label for=\"RL\">Load resistance <span id=\"v-RL\">12 \u03a9</span></label><input data-param=\"RL\" data-unit=\"\u03a9\" id=\"RL\" type=\"range\" min=\"1\" max=\"100\" value=\"12\" step=\"0.099\"></div></div><div class=\"readouts\"><div class=\"stat-box\" id=\"res-a\"><small>-</small><output>-</output></div><div class=\"stat-box\" id=\"res-b\"><small>-</small><output>-</output></div></div><div class=\"plot\" id=\"sim-chart\"></div>",
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        function update() {
          var p = {};
          inputs.forEach(function(el) {
            p[el.dataset.param] = Number(el.value);
            var vEl = card.querySelector('#v-' + el.dataset.param);
            if (vEl) vEl.textContent = el.value + ' ' + (el.dataset.unit || '');
          });
          var r = compute(7, p);
          var ra = card.querySelector('#res-a'), rb = card.querySelector('#res-b');
          if (ra && r.a) { ra.querySelector('small').textContent = r.a[0]; ra.querySelector('output').textContent = r.a[1]; }
          if (rb && r.b) { rb.querySelector('small').textContent = r.b[0]; rb.querySelector('output').textContent = r.b[1]; }
          var chart = card.querySelector('#sim-chart');
          if (chart && r.points) chart.innerHTML = renderGraph(r.points, r.ylabel);
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis I sim error in model 7:', err);
      }
    }
  });
  MODELS.push({
    idx: 8,
    unit: 4,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 08</span><h3>Maximum Power Transfer</h3><p>Maximum output power and maximum efficiency are different goals. Change the inputs to test the relationship; the graph and values update immediately. All cases assume ideal lumped components.</p></div><div class=\"sim-controls\"><div class=\"param\"><label for=\"V\">Thevenin voltage <span id=\"v-V\">12 V</span></label><input data-param=\"V\" data-unit=\"V\" id=\"V\" type=\"range\" min=\"1\" max=\"30\" value=\"12\" step=\"0.029\"></div>\n<div class=\"param\"><label for=\"R\">Source resistance <span id=\"v-R\">6 \u03a9</span></label><input data-param=\"R\" data-unit=\"\u03a9\" id=\"R\" type=\"range\" min=\"1\" max=\"100\" value=\"6\" step=\"0.099\"></div>\n<div class=\"param\"><label for=\"RL\">Load resistance <span id=\"v-RL\">6 \u03a9</span></label><input data-param=\"RL\" data-unit=\"\u03a9\" id=\"RL\" type=\"range\" min=\"1\" max=\"100\" value=\"6\" step=\"0.099\"></div></div><div class=\"readouts\"><div class=\"stat-box\" id=\"res-a\"><small>-</small><output>-</output></div><div class=\"stat-box\" id=\"res-b\"><small>-</small><output>-</output></div></div><div class=\"plot\" id=\"sim-chart\"></div>",
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        function update() {
          var p = {};
          inputs.forEach(function(el) {
            p[el.dataset.param] = Number(el.value);
            var vEl = card.querySelector('#v-' + el.dataset.param);
            if (vEl) vEl.textContent = el.value + ' ' + (el.dataset.unit || '');
          });
          var r = compute(8, p);
          var ra = card.querySelector('#res-a'), rb = card.querySelector('#res-b');
          if (ra && r.a) { ra.querySelector('small').textContent = r.a[0]; ra.querySelector('output').textContent = r.a[1]; }
          if (rb && r.b) { rb.querySelector('small').textContent = r.b[0]; rb.querySelector('output').textContent = r.b[1]; }
          var chart = card.querySelector('#sim-chart');
          if (chart && r.points) chart.innerHTML = renderGraph(r.points, r.ylabel);
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis I sim error in model 8:', err);
      }
    }
  });
  MODELS.push({
    idx: 9,
    unit: 5,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 09</span><h3>Capacitor Charge and Energy</h3><p>Electrostatic energy increases quadratically with voltage. Change the inputs to test the relationship; the graph and values update immediately. All cases assume ideal lumped components.</p></div><div class=\"sim-controls\"><div class=\"param\"><label for=\"C\">Capacitance <span id=\"v-C\">100 \u00b5F</span></label><input data-param=\"C\" data-unit=\"\u00b5F\" id=\"C\" type=\"range\" min=\"1\" max=\"1000\" value=\"100\" step=\"0.999\"></div>\n<div class=\"param\"><label for=\"V\">Voltage <span id=\"v-V\">12 V</span></label><input data-param=\"V\" data-unit=\"V\" id=\"V\" type=\"range\" min=\"0\" max=\"30\" value=\"12\" step=\"0.03\"></div></div><div class=\"readouts\"><div class=\"stat-box\" id=\"res-a\"><small>-</small><output>-</output></div><div class=\"stat-box\" id=\"res-b\"><small>-</small><output>-</output></div></div><div class=\"plot\" id=\"sim-chart\"></div>",
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        function update() {
          var p = {};
          inputs.forEach(function(el) {
            p[el.dataset.param] = Number(el.value);
            var vEl = card.querySelector('#v-' + el.dataset.param);
            if (vEl) vEl.textContent = el.value + ' ' + (el.dataset.unit || '');
          });
          var r = compute(9, p);
          var ra = card.querySelector('#res-a'), rb = card.querySelector('#res-b');
          if (ra && r.a) { ra.querySelector('small').textContent = r.a[0]; ra.querySelector('output').textContent = r.a[1]; }
          if (rb && r.b) { rb.querySelector('small').textContent = r.b[0]; rb.querySelector('output').textContent = r.b[1]; }
          var chart = card.querySelector('#sim-chart');
          if (chart && r.points) chart.innerHTML = renderGraph(r.points, r.ylabel);
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis I sim error in model 9:', err);
      }
    }
  });
  MODELS.push({
    idx: 10,
    unit: 5,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 10</span><h3>Inductor Stored Energy</h3><p>Magnetic energy increases quadratically with current. Change the inputs to test the relationship; the graph and values update immediately. All cases assume ideal lumped components.</p></div><div class=\"sim-controls\"><div class=\"param\"><label for=\"L\">Inductance <span id=\"v-L\">200 mH</span></label><input data-param=\"L\" data-unit=\"mH\" id=\"L\" type=\"range\" min=\"1\" max=\"1000\" value=\"200\" step=\"0.999\"></div>\n<div class=\"param\"><label for=\"I\">Current <span id=\"v-I\">3 A</span></label><input data-param=\"I\" data-unit=\"A\" id=\"I\" type=\"range\" min=\"0\" max=\"10\" value=\"3\" step=\"0.01\"></div></div><div class=\"readouts\"><div class=\"stat-box\" id=\"res-a\"><small>-</small><output>-</output></div><div class=\"stat-box\" id=\"res-b\"><small>-</small><output>-</output></div></div><div class=\"plot\" id=\"sim-chart\"></div>",
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        function update() {
          var p = {};
          inputs.forEach(function(el) {
            p[el.dataset.param] = Number(el.value);
            var vEl = card.querySelector('#v-' + el.dataset.param);
            if (vEl) vEl.textContent = el.value + ' ' + (el.dataset.unit || '');
          });
          var r = compute(10, p);
          var ra = card.querySelector('#res-a'), rb = card.querySelector('#res-b');
          if (ra && r.a) { ra.querySelector('small').textContent = r.a[0]; ra.querySelector('output').textContent = r.a[1]; }
          if (rb && r.b) { rb.querySelector('small').textContent = r.b[0]; rb.querySelector('output').textContent = r.b[1]; }
          var chart = card.querySelector('#sim-chart');
          if (chart && r.points) chart.innerHTML = renderGraph(r.points, r.ylabel);
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis I sim error in model 10:', err);
      }
    }
  });
  MODELS.push({
    idx: 11,
    unit: 6,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 11</span><h3>RC Charging Response</h3><p>Capacitor voltage rises toward the supply with \u03c4=RC. Change the inputs to test the relationship; the graph and values update immediately. All cases assume ideal lumped components.</p></div><div class=\"sim-controls\"><div class=\"param\"><label for=\"V\">Supply <span id=\"v-V\">12 V</span></label><input data-param=\"V\" data-unit=\"V\" id=\"V\" type=\"range\" min=\"1\" max=\"24\" value=\"12\" step=\"0.023\"></div>\n<div class=\"param\"><label for=\"R\">Resistance <span id=\"v-R\">10 k\u03a9</span></label><input data-param=\"R\" data-unit=\"k\u03a9\" id=\"R\" type=\"range\" min=\"1\" max=\"200\" value=\"10\" step=\"0.199\"></div>\n<div class=\"param\"><label for=\"C\">Capacitance <span id=\"v-C\">100 \u00b5F</span></label><input data-param=\"C\" data-unit=\"\u00b5F\" id=\"C\" type=\"range\" min=\"1\" max=\"1000\" value=\"100\" step=\"0.999\"></div>\n<div class=\"param\"><label for=\"T\">Elapsed time <span id=\"v-T\">1 s</span></label><input data-param=\"T\" data-unit=\"s\" id=\"T\" type=\"range\" min=\"0\" max=\"10\" value=\"1\" step=\"0.01\"></div></div><div class=\"readouts\"><div class=\"stat-box\" id=\"res-a\"><small>-</small><output>-</output></div><div class=\"stat-box\" id=\"res-b\"><small>-</small><output>-</output></div></div><div class=\"plot\" id=\"sim-chart\"></div>",
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        function update() {
          var p = {};
          inputs.forEach(function(el) {
            p[el.dataset.param] = Number(el.value);
            var vEl = card.querySelector('#v-' + el.dataset.param);
            if (vEl) vEl.textContent = el.value + ' ' + (el.dataset.unit || '');
          });
          var r = compute(11, p);
          var ra = card.querySelector('#res-a'), rb = card.querySelector('#res-b');
          if (ra && r.a) { ra.querySelector('small').textContent = r.a[0]; ra.querySelector('output').textContent = r.a[1]; }
          if (rb && r.b) { rb.querySelector('small').textContent = r.b[0]; rb.querySelector('output').textContent = r.b[1]; }
          var chart = card.querySelector('#sim-chart');
          if (chart && r.points) chart.innerHTML = renderGraph(r.points, r.ylabel);
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis I sim error in model 11:', err);
      }
    }
  });
  MODELS.push({
    idx: 12,
    unit: 6,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 12</span><h3>RL Current Response</h3><p>Inductor current approaches its final DC value with \u03c4=L/R. Change the inputs to test the relationship; the graph and values update immediately. All cases assume ideal lumped components.</p></div><div class=\"sim-controls\"><div class=\"param\"><label for=\"V\">Supply <span id=\"v-V\">12 V</span></label><input data-param=\"V\" data-unit=\"V\" id=\"V\" type=\"range\" min=\"1\" max=\"24\" value=\"12\" step=\"0.023\"></div>\n<div class=\"param\"><label for=\"R\">Resistance <span id=\"v-R\">6 \u03a9</span></label><input data-param=\"R\" data-unit=\"\u03a9\" id=\"R\" type=\"range\" min=\"1\" max=\"200\" value=\"6\" step=\"0.199\"></div>\n<div class=\"param\"><label for=\"L\">Inductance <span id=\"v-L\">300 mH</span></label><input data-param=\"L\" data-unit=\"mH\" id=\"L\" type=\"range\" min=\"1\" max=\"1000\" value=\"300\" step=\"0.999\"></div>\n<div class=\"param\"><label for=\"T\">Time <span id=\"v-T\">50 ms</span></label><input data-param=\"T\" data-unit=\"ms\" id=\"T\" type=\"range\" min=\"0\" max=\"500\" value=\"50\" step=\"0.5\"></div></div><div class=\"readouts\"><div class=\"stat-box\" id=\"res-a\"><small>-</small><output>-</output></div><div class=\"stat-box\" id=\"res-b\"><small>-</small><output>-</output></div></div><div class=\"plot\" id=\"sim-chart\"></div>",
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        function update() {
          var p = {};
          inputs.forEach(function(el) {
            p[el.dataset.param] = Number(el.value);
            var vEl = card.querySelector('#v-' + el.dataset.param);
            if (vEl) vEl.textContent = el.value + ' ' + (el.dataset.unit || '');
          });
          var r = compute(12, p);
          var ra = card.querySelector('#res-a'), rb = card.querySelector('#res-b');
          if (ra && r.a) { ra.querySelector('small').textContent = r.a[0]; ra.querySelector('output').textContent = r.a[1]; }
          if (rb && r.b) { rb.querySelector('small').textContent = r.b[0]; rb.querySelector('output').textContent = r.b[1]; }
          var chart = card.querySelector('#sim-chart');
          if (chart && r.points) chart.innerHTML = renderGraph(r.points, r.ylabel);
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis I sim error in model 12:', err);
      }
    }
  });
  MODELS.push({
    idx: 13,
    unit: 7,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 13</span><h3>RLC Damping Classifier</h3><p>Damping depends on \u03b1/\u03c9\u2080 rather than resistance alone. Change the inputs to test the relationship; the graph and values update immediately. All cases assume ideal lumped components.</p></div><div class=\"sim-controls\"><div class=\"param\"><label for=\"L\">Inductance <span id=\"v-L\">100 mH</span></label><input data-param=\"L\" data-unit=\"mH\" id=\"L\" type=\"range\" min=\"1\" max=\"1000\" value=\"100\" step=\"0.999\"></div>\n<div class=\"param\"><label for=\"C\">Capacitance <span id=\"v-C\">100 \u00b5F</span></label><input data-param=\"C\" data-unit=\"\u00b5F\" id=\"C\" type=\"range\" min=\"1\" max=\"1000\" value=\"100\" step=\"0.999\"></div>\n<div class=\"param\"><label for=\"R\">Resistance <span id=\"v-R\">20 \u03a9</span></label><input data-param=\"R\" data-unit=\"\u03a9\" id=\"R\" type=\"range\" min=\"0\" max=\"200\" value=\"20\" step=\"0.2\"></div></div><div class=\"readouts\"><div class=\"stat-box\" id=\"res-a\"><small>-</small><output>-</output></div><div class=\"stat-box\" id=\"res-b\"><small>-</small><output>-</output></div></div><div class=\"plot\" id=\"sim-chart\"></div>",
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        function update() {
          var p = {};
          inputs.forEach(function(el) {
            p[el.dataset.param] = Number(el.value);
            var vEl = card.querySelector('#v-' + el.dataset.param);
            if (vEl) vEl.textContent = el.value + ' ' + (el.dataset.unit || '');
          });
          var r = compute(13, p);
          var ra = card.querySelector('#res-a'), rb = card.querySelector('#res-b');
          if (ra && r.a) { ra.querySelector('small').textContent = r.a[0]; ra.querySelector('output').textContent = r.a[1]; }
          if (rb && r.b) { rb.querySelector('small').textContent = r.b[0]; rb.querySelector('output').textContent = r.b[1]; }
          var chart = card.querySelector('#sim-chart');
          if (chart && r.points) chart.innerHTML = renderGraph(r.points, r.ylabel);
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis I sim error in model 13:', err);
      }
    }
  });
  MODELS.push({
    idx: 14,
    unit: 7,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 14</span><h3>Underdamped RLC Response</h3><p>Closed-form capacitor-voltage response for zero initial inductor current. Change the inputs to test the relationship; the graph and values update immediately. All cases assume ideal lumped components.</p></div><div class=\"sim-controls\"><div class=\"param\"><label for=\"V\">Initial capacitor voltage <span id=\"v-V\">10 V</span></label><input data-param=\"V\" data-unit=\"V\" id=\"V\" type=\"range\" min=\"1\" max=\"20\" value=\"10\" step=\"0.019\"></div>\n<div class=\"param\"><label for=\"L\">Inductance <span id=\"v-L\">100 mH</span></label><input data-param=\"L\" data-unit=\"mH\" id=\"L\" type=\"range\" min=\"10\" max=\"1000\" value=\"100\" step=\"0.99\"></div>\n<div class=\"param\"><label for=\"C\">Capacitance <span id=\"v-C\">100 \u00b5F</span></label><input data-param=\"C\" data-unit=\"\u00b5F\" id=\"C\" type=\"range\" min=\"1\" max=\"1000\" value=\"100\" step=\"0.999\"></div>\n<div class=\"param\"><label for=\"R\">Resistance <span id=\"v-R\">10 \u03a9</span></label><input data-param=\"R\" data-unit=\"\u03a9\" id=\"R\" type=\"range\" min=\"0\" max=\"40\" value=\"10\" step=\"0.04\"></div>\n<div class=\"param\"><label for=\"T\">Time <span id=\"v-T\">5 ms</span></label><input data-param=\"T\" data-unit=\"ms\" id=\"T\" type=\"range\" min=\"0\" max=\"50\" value=\"5\" step=\"0.05\"></div></div><div class=\"readouts\"><div class=\"stat-box\" id=\"res-a\"><small>-</small><output>-</output></div><div class=\"stat-box\" id=\"res-b\"><small>-</small><output>-</output></div></div><div class=\"plot\" id=\"sim-chart\"></div>",
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        function update() {
          var p = {};
          inputs.forEach(function(el) {
            p[el.dataset.param] = Number(el.value);
            var vEl = card.querySelector('#v-' + el.dataset.param);
            if (vEl) vEl.textContent = el.value + ' ' + (el.dataset.unit || '');
          });
          var r = compute(14, p);
          var ra = card.querySelector('#res-a'), rb = card.querySelector('#res-b');
          if (ra && r.a) { ra.querySelector('small').textContent = r.a[0]; ra.querySelector('output').textContent = r.a[1]; }
          if (rb && r.b) { rb.querySelector('small').textContent = r.b[0]; rb.querySelector('output').textContent = r.b[1]; }
          var chart = card.querySelector('#sim-chart');
          if (chart && r.points) chart.innerHTML = renderGraph(r.points, r.ylabel);
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis I sim error in model 14:', err);
      }
    }
  });
  MODELS.push({
    idx: 15,
    unit: 8,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 15</span><h3>Voltmeter Loading</h3><p>The meter forms a parallel path with the measured element. Change the inputs to test the relationship; the graph and values update immediately. All cases assume ideal lumped components.</p></div><div class=\"sim-controls\"><div class=\"param\"><label for=\"V\">Supply <span id=\"v-V\">12 V</span></label><input data-param=\"V\" data-unit=\"V\" id=\"V\" type=\"range\" min=\"1\" max=\"24\" value=\"12\" step=\"0.023\"></div>\n<div class=\"param\"><label for=\"R1\">Upper resistance <span id=\"v-R1\">10000 \u03a9</span></label><input data-param=\"R1\" data-unit=\"\u03a9\" id=\"R1\" type=\"range\" min=\"100\" max=\"20000\" value=\"10000\" step=\"19.9\"></div>\n<div class=\"param\"><label for=\"R2\">Lower resistance <span id=\"v-R2\">10000 \u03a9</span></label><input data-param=\"R2\" data-unit=\"\u03a9\" id=\"R2\" type=\"range\" min=\"100\" max=\"20000\" value=\"10000\" step=\"19.9\"></div>\n<div class=\"param\"><label for=\"RM\">Meter input resistance <span id=\"v-RM\">10000 \u03a9</span></label><input data-param=\"RM\" data-unit=\"\u03a9\" id=\"RM\" type=\"range\" min=\"100\" max=\"100000\" value=\"10000\" step=\"99.9\"></div></div><div class=\"readouts\"><div class=\"stat-box\" id=\"res-a\"><small>-</small><output>-</output></div><div class=\"stat-box\" id=\"res-b\"><small>-</small><output>-</output></div></div><div class=\"plot\" id=\"sim-chart\"></div>",
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        function update() {
          var p = {};
          inputs.forEach(function(el) {
            p[el.dataset.param] = Number(el.value);
            var vEl = card.querySelector('#v-' + el.dataset.param);
            if (vEl) vEl.textContent = el.value + ' ' + (el.dataset.unit || '');
          });
          var r = compute(15, p);
          var ra = card.querySelector('#res-a'), rb = card.querySelector('#res-b');
          if (ra && r.a) { ra.querySelector('small').textContent = r.a[0]; ra.querySelector('output').textContent = r.a[1]; }
          if (rb && r.b) { rb.querySelector('small').textContent = r.b[0]; rb.querySelector('output').textContent = r.b[1]; }
          var chart = card.querySelector('#sim-chart');
          if (chart && r.points) chart.innerHTML = renderGraph(r.points, r.ylabel);
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis I sim error in model 15:', err);
      }
    }
  });
  MODELS.push({
    idx: 16,
    unit: 8,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 16</span><h3>Voltage Divider Tolerances</h3><p>Opposite tolerance extremes set the worst-case divider bounds. Change the inputs to test the relationship; the graph and values update immediately. All cases assume ideal lumped components.</p></div><div class=\"sim-controls\"><div class=\"param\"><label for=\"V\">Supply <span id=\"v-V\">5 V</span></label><input data-param=\"V\" data-unit=\"V\" id=\"V\" type=\"range\" min=\"1\" max=\"24\" value=\"5\" step=\"0.023\"></div>\n<div class=\"param\"><label for=\"R1\">Nominal upper resistor <span id=\"v-R1\">10000 \u03a9</span></label><input data-param=\"R1\" data-unit=\"\u03a9\" id=\"R1\" type=\"range\" min=\"100\" max=\"20000\" value=\"10000\" step=\"19.9\"></div>\n<div class=\"param\"><label for=\"R2\">Nominal lower resistor <span id=\"v-R2\">10000 \u03a9</span></label><input data-param=\"R2\" data-unit=\"\u03a9\" id=\"R2\" type=\"range\" min=\"100\" max=\"20000\" value=\"10000\" step=\"19.9\"></div>\n<div class=\"param\"><label for=\"T\">Tolerance <span id=\"v-T\">5 %</span></label><input data-param=\"T\" data-unit=\"%\" id=\"T\" type=\"range\" min=\"0\" max=\"20\" value=\"5\" step=\"0.02\"></div></div><div class=\"readouts\"><div class=\"stat-box\" id=\"res-a\"><small>-</small><output>-</output></div><div class=\"stat-box\" id=\"res-b\"><small>-</small><output>-</output></div></div><div class=\"plot\" id=\"sim-chart\"></div>",
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        function update() {
          var p = {};
          inputs.forEach(function(el) {
            p[el.dataset.param] = Number(el.value);
            var vEl = card.querySelector('#v-' + el.dataset.param);
            if (vEl) vEl.textContent = el.value + ' ' + (el.dataset.unit || '');
          });
          var r = compute(16, p);
          var ra = card.querySelector('#res-a'), rb = card.querySelector('#res-b');
          if (ra && r.a) { ra.querySelector('small').textContent = r.a[0]; ra.querySelector('output').textContent = r.a[1]; }
          if (rb && r.b) { rb.querySelector('small').textContent = r.b[0]; rb.querySelector('output').textContent = r.b[1]; }
          var chart = card.querySelector('#sim-chart');
          if (chart && r.points) chart.innerHTML = renderGraph(r.points, r.ylabel);
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis I sim error in model 16:', err);
      }
    }
  });
  if (!window.SimulationEngine) window.SimulationEngine = {};
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId || 'sim-container');
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
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.slice(0, 2);
    modelsForUnit.forEach(function(m) {
      var card = document.createElement('section');
      card.className = 'eee-sim-card';
      card.setAttribute('aria-label', 'Interactive Simulation ' + m.idx);
      card.id = 'sim-card-' + m.idx;
      card.innerHTML = m.html;
      container.appendChild(card);
      m.init(card);
    });
  };

  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', function() {
        if (document.getElementById('sim-container')) window.SimulationEngine.initSimulation('sim-container');
      });
    } else {
      if (document.getElementById('sim-container')) window.SimulationEngine.initSimulation('sim-container');
    }
  }
})(typeof window === 'undefined' ? globalThis : window);
