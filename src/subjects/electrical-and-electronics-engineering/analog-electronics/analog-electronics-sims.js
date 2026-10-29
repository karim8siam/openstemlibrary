/* Analog Electronics Interactive Simulation Suite */
(function(window) {
  'use strict';
  const kb = 1.380649e-23;
  const specs = {
    diode: [0, 0.65, 0.005, 0.52, 'V'],
    rectifier: [1, 20, 0.2, 10, 'V'],
    ripple: [10, 400, 5, 100, 'mA'],
    zener: [0, 30, 0.5, 10, 'mA'],
    bjt_sat: [0, 7, 0.05, 2, 'mA'],
    bjt_bias: [50, 250, 5, 100, 'β'],
    ce_gain: [0.1, 5, 0.05, 1, 'mA'],
    degen: [0, 400, 5, 100, 'Ω'],
    mos_square: [0, 4, 0.05, 1, 'V'],
    cs_stage: [0.5, 20, 0.1, 8, 'mS'],
    diff_pair: [-100, 100, 2, 0, 'mV'],
    opamp_inv: [-1, 1, 0.02, 0.5, 'V'],
    sallen_key: [10, 10000, 10, 1000, 'Hz'],
    feedback: [1, 2000, 10, 1000, 'V/V'],
    pushpull: [0.1, 9, 0.1, 8, 'V'],
    thermal: [0.1, 10, 0.1, 2.5, 'W']
  };

  function model(kind, x) {
    let y = 0, units = '', text = '';
    if (kind === 'diode') {
      y = 1e-12 * Math.expm1(x / (1.8 * 0.02585)) * 1e3; units = 'mA'; text = 'Diode current ' + y.toFixed(4) + ' mA';
    } else if (kind === 'rectifier') {
      y = 2 * x / Math.PI; units = 'V'; text = 'Ideal full-wave mean ≈ ' + y.toFixed(3) + ' V';
    } else if (kind === 'ripple') {
      y = (x / 1000) / (100 * 0.001); units = 'V'; text = 'Ripple ≈ ' + y.toFixed(3) + ' V pk-pk';
    } else if (kind === 'zener') {
      let I = (12 - 5.1) / 330 * 1000, iz = I - x; y = Math.max(0, iz); units = 'mA'; text = 'Zener current ≈ ' + iz.toFixed(3) + ' mA';
    } else if (kind === 'bjt_sat') {
      y = 12 - (x / 1000) * 2200; units = 'V'; text = 'V_ce ≈ ' + y.toFixed(3) + ' V';
    } else if (kind === 'bjt_bias') {
      let ib = (2 - 0.7) / (5000 + (x + 1) * 1000); y = x * ib * 1000; units = 'mA'; text = 'I_c ≈ ' + y.toFixed(3) + ' mA';
    } else if (kind === 'ce_gain') {
      let gm = (x / 1000) / 0.02585; y = -gm * 2000; units = 'V/V'; text = 'Small-signal gain ≈ ' + y.toFixed(2) + ' V/V';
    } else if (kind === 'degen') {
      y = -0.04 * 2000 / (1 + 0.04 * x); units = 'V/V'; text = 'Degenerated gain ≈ ' + y.toFixed(2) + ' V/V';
    } else if (kind === 'mos_square') {
      let vov = Math.max(0, x - 1.0), k = 0.002; y = 0.5 * k * vov * vov * 1000; units = 'mA'; text = 'I_d ≈ ' + y.toFixed(3) + ' mA';
    } else if (kind === 'cs_stage') {
      let g = x / 1000; y = -g * 2200; units = 'V/V'; text = 'CS voltage gain ≈ ' + y.toFixed(2) + ' V/V';
    } else if (kind === 'diff_pair') {
      let vdiff = x * 0.001, Itail = 2.0; y = Itail / (1 + Math.exp(-vdiff / 0.02585)); units = 'mA'; text = 'I_c1 ≈ ' + y.toFixed(3) + ' mA';
    } else if (kind === 'opamp_inv') {
      y = Math.max(-12, Math.min(12, -10 * x)); units = 'V'; text = 'V_out ≈ ' + y.toFixed(3) + ' V';
    } else if (kind === 'sallen_key') {
      y = 1 / Math.sqrt(1 + Math.pow(x / 1000, 4)); units = 'mag'; text = '2nd-order gain ≈ ' + y.toFixed(4);
    } else if (kind === 'feedback') {
      y = x / (1 + x * 0.05); units = 'V/V'; text = 'Closed-loop A_f ≈ ' + y.toFixed(3) + ' V/V';
    } else if (kind === 'pushpull') {
      let vout = Math.abs(x) > 0.7 ? (x > 0 ? x - 0.7 : x + 0.7) : 0; y = vout; units = 'V'; text = 'V_out ≈ ' + y.toFixed(3) + ' V';
    } else if (kind === 'thermal') {
      let Rth = 40; y = 25 + x * Rth; units = '°C'; text = 'Junction temp Tj ≈ ' + y.toFixed(1) + ' °C';
    }
    return { val: y, text: text, units: units };
  }
  

  function renderGraph(kind, v, S) {
    const curr = model(kind, v);
    const W = 680, H = 240, left = 55, right = 20, top = 20, bottom = 35;
    const pts = [];
    for (let i = 0; i <= 60; i++) {
      const x = S[0] + (S[1] - S[0]) * (i / 60);
      pts.push([x, model(kind, x).val]);
    }
    const ymin = Math.min(...pts.map(p => p[1]));
    let ymax = Math.max(...pts.map(p => p[1]));
    if (ymax - ymin < 1e-9) ymax = ymin + 1;
    const mapX = x => left + ((x - S[0]) / (S[1] - S[0] || 1)) * (W - left - right);
    const mapY = y => H - bottom - ((y - ymin) / (ymax - ymin || 1)) * (H - top - bottom);
    const pathD = pts.map((p, i) => (i === 0 ? 'M' : 'L') + mapX(p[0]).toFixed(1) + ',' + mapY(p[1]).toFixed(1)).join(' ');
    const activeY = mapY(Math.min(Math.max(curr.val, ymin), ymax));
    return `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Analog transfer curve" style="width:100%;height:auto;display:block">
      <rect x="${left}" y="${top}" width="${W - left - right}" height="${H - top - bottom}" fill="#0f172a" rx="4"/>
      <path d="${pathD}" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      <circle cx="${mapX(v).toFixed(1)}" cy="${activeY.toFixed(1)}" r="5" fill="#f59e0b"/>
      <text x="${left}" y="${H - 10}" fill="#94a3b8" font-size="11">${S[0]} ${S[4]}</text>
      <text x="${W - right}" y="${H - 10}" fill="#94a3b8" text-anchor="end" font-size="11">${S[1]} ${S[4]}</text>
      <text x="${left}" y="${top - 6}" fill="#38bdf8" font-size="11">${curr.units} (max: ${ymax.toFixed(2)})</text>
    </svg>`;
  }

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: '<div class="sim-header"><span class="badge">Model 01</span><h3>Diode Exponential Current</h3><p>Voltage sweep 0–0.65 V, fixed Is=1 pA, n=1.8, T=300 K; ideal isothermal diode only.</p></div>' +
          '<div class="sim-controls"><label for="param-1">Input sweep (' + specs['diode'][4] + '): <output id="val-1"></output></label>' +
          '<input id="param-1" type="range" min="' + specs['diode'][0] + '" max="' + specs['diode'][1] + '" step="' + specs['diode'][2] + '" value="' + specs['diode'][3] + '"/></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Response</small><output id="readout-1">-</output></div></div>' +
          '<div class="plot" id="plot-1"></div>',
    init: function(card) {
      try {
        var slider = card.querySelector('#param-1');
        var valOut = card.querySelector('#val-1');
        var resOut = card.querySelector('#readout-1');
        var plot = card.querySelector('#plot-1');
        var S = specs['diode'];
        function update() {
          var v = Number(slider.value);
          if (valOut) valOut.textContent = v.toFixed(3) + ' ' + S[4];
          var res = model('diode', v);
          if (resOut) resOut.textContent = res.text;
          if (plot) plot.innerHTML = renderGraph('diode', v, S);
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Analog Electronics sim error in model 1:', err);
      }
    }
  });
  MODELS.push({
    idx: 2,
    unit: 1,
    html: '<div class="sim-header"><span class="badge">Model 02</span><h3>Half-Wave Rectifier Peak</h3><p>Peak output across load resistor without filtering capacitor.</p></div>' +
          '<div class="sim-controls"><label for="param-2">Input sweep (' + specs['rectifier'][4] + '): <output id="val-2"></output></label>' +
          '<input id="param-2" type="range" min="' + specs['rectifier'][0] + '" max="' + specs['rectifier'][1] + '" step="' + specs['rectifier'][2] + '" value="' + specs['rectifier'][3] + '"/></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Response</small><output id="readout-2">-</output></div></div>' +
          '<div class="plot" id="plot-2"></div>',
    init: function(card) {
      try {
        var slider = card.querySelector('#param-2');
        var valOut = card.querySelector('#val-2');
        var resOut = card.querySelector('#readout-2');
        var plot = card.querySelector('#plot-2');
        var S = specs['rectifier'];
        function update() {
          var v = Number(slider.value);
          if (valOut) valOut.textContent = v.toFixed(3) + ' ' + S[4];
          var res = model('rectifier', v);
          if (resOut) resOut.textContent = res.text;
          if (plot) plot.innerHTML = renderGraph('rectifier', v, S);
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Analog Electronics sim error in model 2:', err);
      }
    }
  });
  MODELS.push({
    idx: 3,
    unit: 2,
    html: '<div class="sim-header"><span class="badge">Model 03</span><h3>Filter Capacitor Ripple</h3><p>Filter capacitor smoothing ripple voltage under load current.</p></div>' +
          '<div class="sim-controls"><label for="param-3">Input sweep (' + specs['ripple'][4] + '): <output id="val-3"></output></label>' +
          '<input id="param-3" type="range" min="' + specs['ripple'][0] + '" max="' + specs['ripple'][1] + '" step="' + specs['ripple'][2] + '" value="' + specs['ripple'][3] + '"/></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Response</small><output id="readout-3">-</output></div></div>' +
          '<div class="plot" id="plot-3"></div>',
    init: function(card) {
      try {
        var slider = card.querySelector('#param-3');
        var valOut = card.querySelector('#val-3');
        var resOut = card.querySelector('#readout-3');
        var plot = card.querySelector('#plot-3');
        var S = specs['ripple'];
        function update() {
          var v = Number(slider.value);
          if (valOut) valOut.textContent = v.toFixed(3) + ' ' + S[4];
          var res = model('ripple', v);
          if (resOut) resOut.textContent = res.text;
          if (plot) plot.innerHTML = renderGraph('ripple', v, S);
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Analog Electronics sim error in model 3:', err);
      }
    }
  });
  MODELS.push({
    idx: 4,
    unit: 2,
    html: '<div class="sim-header"><span class="badge">Model 04</span><h3>Zener Voltage Regulator</h3><p>Zener diode shunt breakdown regulation and series current limiting.</p></div>' +
          '<div class="sim-controls"><label for="param-4">Input sweep (' + specs['zener'][4] + '): <output id="val-4"></output></label>' +
          '<input id="param-4" type="range" min="' + specs['zener'][0] + '" max="' + specs['zener'][1] + '" step="' + specs['zener'][2] + '" value="' + specs['zener'][3] + '"/></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Response</small><output id="readout-4">-</output></div></div>' +
          '<div class="plot" id="plot-4"></div>',
    init: function(card) {
      try {
        var slider = card.querySelector('#param-4');
        var valOut = card.querySelector('#val-4');
        var resOut = card.querySelector('#readout-4');
        var plot = card.querySelector('#plot-4');
        var S = specs['zener'];
        function update() {
          var v = Number(slider.value);
          if (valOut) valOut.textContent = v.toFixed(3) + ' ' + S[4];
          var res = model('zener', v);
          if (resOut) resOut.textContent = res.text;
          if (plot) plot.innerHTML = renderGraph('zener', v, S);
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Analog Electronics sim error in model 4:', err);
      }
    }
  });
  MODELS.push({
    idx: 5,
    unit: 3,
    html: '<div class="sim-header"><span class="badge">Model 05</span><h3>BJT Saturation & Active Line</h3><p>Base-emitter overdrive and collector-emitter saturation boundary.</p></div>' +
          '<div class="sim-controls"><label for="param-5">Input sweep (' + specs['bjt_sat'][4] + '): <output id="val-5"></output></label>' +
          '<input id="param-5" type="range" min="' + specs['bjt_sat'][0] + '" max="' + specs['bjt_sat'][1] + '" step="' + specs['bjt_sat'][2] + '" value="' + specs['bjt_sat'][3] + '"/></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Response</small><output id="readout-5">-</output></div></div>' +
          '<div class="plot" id="plot-5"></div>',
    init: function(card) {
      try {
        var slider = card.querySelector('#param-5');
        var valOut = card.querySelector('#val-5');
        var resOut = card.querySelector('#readout-5');
        var plot = card.querySelector('#plot-5');
        var S = specs['bjt_sat'];
        function update() {
          var v = Number(slider.value);
          if (valOut) valOut.textContent = v.toFixed(3) + ' ' + S[4];
          var res = model('bjt_sat', v);
          if (resOut) resOut.textContent = res.text;
          if (plot) plot.innerHTML = renderGraph('bjt_sat', v, S);
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Analog Electronics sim error in model 5:', err);
      }
    }
  });
  MODELS.push({
    idx: 6,
    unit: 3,
    html: '<div class="sim-header"><span class="badge">Model 06</span><h3>Four-Resistor Divider Bias</h3><p>Thermal stability of collector current against beta variations.</p></div>' +
          '<div class="sim-controls"><label for="param-6">Input sweep (' + specs['bjt_bias'][4] + '): <output id="val-6"></output></label>' +
          '<input id="param-6" type="range" min="' + specs['bjt_bias'][0] + '" max="' + specs['bjt_bias'][1] + '" step="' + specs['bjt_bias'][2] + '" value="' + specs['bjt_bias'][3] + '"/></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Response</small><output id="readout-6">-</output></div></div>' +
          '<div class="plot" id="plot-6"></div>',
    init: function(card) {
      try {
        var slider = card.querySelector('#param-6');
        var valOut = card.querySelector('#val-6');
        var resOut = card.querySelector('#readout-6');
        var plot = card.querySelector('#plot-6');
        var S = specs['bjt_bias'];
        function update() {
          var v = Number(slider.value);
          if (valOut) valOut.textContent = v.toFixed(3) + ' ' + S[4];
          var res = model('bjt_bias', v);
          if (resOut) resOut.textContent = res.text;
          if (plot) plot.innerHTML = renderGraph('bjt_bias', v, S);
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Analog Electronics sim error in model 6:', err);
      }
    }
  });
  MODELS.push({
    idx: 7,
    unit: 4,
    html: '<div class="sim-header"><span class="badge">Model 07</span><h3>Common Emitter Small-Signal Gain</h3><p>Midband transconductance gain with collector and load resistance.</p></div>' +
          '<div class="sim-controls"><label for="param-7">Input sweep (' + specs['ce_gain'][4] + '): <output id="val-7"></output></label>' +
          '<input id="param-7" type="range" min="' + specs['ce_gain'][0] + '" max="' + specs['ce_gain'][1] + '" step="' + specs['ce_gain'][2] + '" value="' + specs['ce_gain'][3] + '"/></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Response</small><output id="readout-7">-</output></div></div>' +
          '<div class="plot" id="plot-7"></div>',
    init: function(card) {
      try {
        var slider = card.querySelector('#param-7');
        var valOut = card.querySelector('#val-7');
        var resOut = card.querySelector('#readout-7');
        var plot = card.querySelector('#plot-7');
        var S = specs['ce_gain'];
        function update() {
          var v = Number(slider.value);
          if (valOut) valOut.textContent = v.toFixed(3) + ' ' + S[4];
          var res = model('ce_gain', v);
          if (resOut) resOut.textContent = res.text;
          if (plot) plot.innerHTML = renderGraph('ce_gain', v, S);
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Analog Electronics sim error in model 7:', err);
      }
    }
  });
  MODELS.push({
    idx: 8,
    unit: 4,
    html: '<div class="sim-header"><span class="badge">Model 08</span><h3>Emitter Degeneration Trade-Off</h3><p>Gain reduction versus linearity and input impedance stabilization.</p></div>' +
          '<div class="sim-controls"><label for="param-8">Input sweep (' + specs['degen'][4] + '): <output id="val-8"></output></label>' +
          '<input id="param-8" type="range" min="' + specs['degen'][0] + '" max="' + specs['degen'][1] + '" step="' + specs['degen'][2] + '" value="' + specs['degen'][3] + '"/></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Response</small><output id="readout-8">-</output></div></div>' +
          '<div class="plot" id="plot-8"></div>',
    init: function(card) {
      try {
        var slider = card.querySelector('#param-8');
        var valOut = card.querySelector('#val-8');
        var resOut = card.querySelector('#readout-8');
        var plot = card.querySelector('#plot-8');
        var S = specs['degen'];
        function update() {
          var v = Number(slider.value);
          if (valOut) valOut.textContent = v.toFixed(3) + ' ' + S[4];
          var res = model('degen', v);
          if (resOut) resOut.textContent = res.text;
          if (plot) plot.innerHTML = renderGraph('degen', v, S);
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Analog Electronics sim error in model 8:', err);
      }
    }
  });
  MODELS.push({
    idx: 9,
    unit: 5,
    html: '<div class="sim-header"><span class="badge">Model 09</span><h3>MOSFET Square-Law Conduction</h3><p>Overdrive voltage Vgs-Vt and saturation drain current id.</p></div>' +
          '<div class="sim-controls"><label for="param-9">Input sweep (' + specs['mos_square'][4] + '): <output id="val-9"></output></label>' +
          '<input id="param-9" type="range" min="' + specs['mos_square'][0] + '" max="' + specs['mos_square'][1] + '" step="' + specs['mos_square'][2] + '" value="' + specs['mos_square'][3] + '"/></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Response</small><output id="readout-9">-</output></div></div>' +
          '<div class="plot" id="plot-9"></div>',
    init: function(card) {
      try {
        var slider = card.querySelector('#param-9');
        var valOut = card.querySelector('#val-9');
        var resOut = card.querySelector('#readout-9');
        var plot = card.querySelector('#plot-9');
        var S = specs['mos_square'];
        function update() {
          var v = Number(slider.value);
          if (valOut) valOut.textContent = v.toFixed(3) + ' ' + S[4];
          var res = model('mos_square', v);
          if (resOut) resOut.textContent = res.text;
          if (plot) plot.innerHTML = renderGraph('mos_square', v, S);
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Analog Electronics sim error in model 9:', err);
      }
    }
  });
  MODELS.push({
    idx: 10,
    unit: 5,
    html: '<div class="sim-header"><span class="badge">Model 10</span><h3>Common Source Amplifier Gain</h3><p>MOSFET transconductance gm and small-signal stage gain.</p></div>' +
          '<div class="sim-controls"><label for="param-10">Input sweep (' + specs['cs_stage'][4] + '): <output id="val-10"></output></label>' +
          '<input id="param-10" type="range" min="' + specs['cs_stage'][0] + '" max="' + specs['cs_stage'][1] + '" step="' + specs['cs_stage'][2] + '" value="' + specs['cs_stage'][3] + '"/></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Response</small><output id="readout-10">-</output></div></div>' +
          '<div class="plot" id="plot-10"></div>',
    init: function(card) {
      try {
        var slider = card.querySelector('#param-10');
        var valOut = card.querySelector('#val-10');
        var resOut = card.querySelector('#readout-10');
        var plot = card.querySelector('#plot-10');
        var S = specs['cs_stage'];
        function update() {
          var v = Number(slider.value);
          if (valOut) valOut.textContent = v.toFixed(3) + ' ' + S[4];
          var res = model('cs_stage', v);
          if (resOut) resOut.textContent = res.text;
          if (plot) plot.innerHTML = renderGraph('cs_stage', v, S);
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Analog Electronics sim error in model 10:', err);
      }
    }
  });
  MODELS.push({
    idx: 11,
    unit: 6,
    html: '<div class="sim-header"><span class="badge">Model 11</span><h3>Differential Pair Steering</h3><p>Differential input voltage steering current between balanced arms.</p></div>' +
          '<div class="sim-controls"><label for="param-11">Input sweep (' + specs['diff_pair'][4] + '): <output id="val-11"></output></label>' +
          '<input id="param-11" type="range" min="' + specs['diff_pair'][0] + '" max="' + specs['diff_pair'][1] + '" step="' + specs['diff_pair'][2] + '" value="' + specs['diff_pair'][3] + '"/></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Response</small><output id="readout-11">-</output></div></div>' +
          '<div class="plot" id="plot-11"></div>',
    init: function(card) {
      try {
        var slider = card.querySelector('#param-11');
        var valOut = card.querySelector('#val-11');
        var resOut = card.querySelector('#readout-11');
        var plot = card.querySelector('#plot-11');
        var S = specs['diff_pair'];
        function update() {
          var v = Number(slider.value);
          if (valOut) valOut.textContent = v.toFixed(3) + ' ' + S[4];
          var res = model('diff_pair', v);
          if (resOut) resOut.textContent = res.text;
          if (plot) plot.innerHTML = renderGraph('diff_pair', v, S);
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Analog Electronics sim error in model 11:', err);
      }
    }
  });
  MODELS.push({
    idx: 12,
    unit: 6,
    html: '<div class="sim-header"><span class="badge">Model 12</span><h3>Inverting Op-Amp Closed-Loop</h3><p>Virtual ground and closed-loop feedback gain -Rf/Rin.</p></div>' +
          '<div class="sim-controls"><label for="param-12">Input sweep (' + specs['opamp_inv'][4] + '): <output id="val-12"></output></label>' +
          '<input id="param-12" type="range" min="' + specs['opamp_inv'][0] + '" max="' + specs['opamp_inv'][1] + '" step="' + specs['opamp_inv'][2] + '" value="' + specs['opamp_inv'][3] + '"/></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Response</small><output id="readout-12">-</output></div></div>' +
          '<div class="plot" id="plot-12"></div>',
    init: function(card) {
      try {
        var slider = card.querySelector('#param-12');
        var valOut = card.querySelector('#val-12');
        var resOut = card.querySelector('#readout-12');
        var plot = card.querySelector('#plot-12');
        var S = specs['opamp_inv'];
        function update() {
          var v = Number(slider.value);
          if (valOut) valOut.textContent = v.toFixed(3) + ' ' + S[4];
          var res = model('opamp_inv', v);
          if (resOut) resOut.textContent = res.text;
          if (plot) plot.innerHTML = renderGraph('opamp_inv', v, S);
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Analog Electronics sim error in model 12:', err);
      }
    }
  });
  MODELS.push({
    idx: 13,
    unit: 7,
    html: '<div class="sim-header"><span class="badge">Model 13</span><h3>Sallen-Key Active Filter</h3><p>Second-order Butterworth low-pass filter cutoff and Q factor.</p></div>' +
          '<div class="sim-controls"><label for="param-13">Input sweep (' + specs['sallen_key'][4] + '): <output id="val-13"></output></label>' +
          '<input id="param-13" type="range" min="' + specs['sallen_key'][0] + '" max="' + specs['sallen_key'][1] + '" step="' + specs['sallen_key'][2] + '" value="' + specs['sallen_key'][3] + '"/></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Response</small><output id="readout-13">-</output></div></div>' +
          '<div class="plot" id="plot-13"></div>',
    init: function(card) {
      try {
        var slider = card.querySelector('#param-13');
        var valOut = card.querySelector('#val-13');
        var resOut = card.querySelector('#readout-13');
        var plot = card.querySelector('#plot-13');
        var S = specs['sallen_key'];
        function update() {
          var v = Number(slider.value);
          if (valOut) valOut.textContent = v.toFixed(3) + ' ' + S[4];
          var res = model('sallen_key', v);
          if (resOut) resOut.textContent = res.text;
          if (plot) plot.innerHTML = renderGraph('sallen_key', v, S);
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Analog Electronics sim error in model 13:', err);
      }
    }
  });
  MODELS.push({
    idx: 14,
    unit: 7,
    html: '<div class="sim-header"><span class="badge">Model 14</span><h3>Negative Feedback Desensitization</h3><p>Closed-loop gain desensitization vs open-loop gain A and beta.</p></div>' +
          '<div class="sim-controls"><label for="param-14">Input sweep (' + specs['feedback'][4] + '): <output id="val-14"></output></label>' +
          '<input id="param-14" type="range" min="' + specs['feedback'][0] + '" max="' + specs['feedback'][1] + '" step="' + specs['feedback'][2] + '" value="' + specs['feedback'][3] + '"/></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Response</small><output id="readout-14">-</output></div></div>' +
          '<div class="plot" id="plot-14"></div>',
    init: function(card) {
      try {
        var slider = card.querySelector('#param-14');
        var valOut = card.querySelector('#val-14');
        var resOut = card.querySelector('#readout-14');
        var plot = card.querySelector('#plot-14');
        var S = specs['feedback'];
        function update() {
          var v = Number(slider.value);
          if (valOut) valOut.textContent = v.toFixed(3) + ' ' + S[4];
          var res = model('feedback', v);
          if (resOut) resOut.textContent = res.text;
          if (plot) plot.innerHTML = renderGraph('feedback', v, S);
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Analog Electronics sim error in model 14:', err);
      }
    }
  });
  MODELS.push({
    idx: 15,
    unit: 8,
    html: '<div class="sim-header"><span class="badge">Model 15</span><h3>Class-B Push-Pull Crossover</h3><p>Deadband crossover distortion near zero-crossing without diode bias.</p></div>' +
          '<div class="sim-controls"><label for="param-15">Input sweep (' + specs['pushpull'][4] + '): <output id="val-15"></output></label>' +
          '<input id="param-15" type="range" min="' + specs['pushpull'][0] + '" max="' + specs['pushpull'][1] + '" step="' + specs['pushpull'][2] + '" value="' + specs['pushpull'][3] + '"/></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Response</small><output id="readout-15">-</output></div></div>' +
          '<div class="plot" id="plot-15"></div>',
    init: function(card) {
      try {
        var slider = card.querySelector('#param-15');
        var valOut = card.querySelector('#val-15');
        var resOut = card.querySelector('#readout-15');
        var plot = card.querySelector('#plot-15');
        var S = specs['pushpull'];
        function update() {
          var v = Number(slider.value);
          if (valOut) valOut.textContent = v.toFixed(3) + ' ' + S[4];
          var res = model('pushpull', v);
          if (resOut) resOut.textContent = res.text;
          if (plot) plot.innerHTML = renderGraph('pushpull', v, S);
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Analog Electronics sim error in model 15:', err);
      }
    }
  });
  MODELS.push({
    idx: 16,
    unit: 8,
    html: '<div class="sim-header"><span class="badge">Model 16</span><h3>Transistor Junction Thermal Limits</h3><p>Power dissipation, junction-to-ambient thermal resistance and Tj.</p></div>' +
          '<div class="sim-controls"><label for="param-16">Input sweep (' + specs['thermal'][4] + '): <output id="val-16"></output></label>' +
          '<input id="param-16" type="range" min="' + specs['thermal'][0] + '" max="' + specs['thermal'][1] + '" step="' + specs['thermal'][2] + '" value="' + specs['thermal'][3] + '"/></div>' +
          '<div class="readouts"><div class="stat-box"><small>Calculated Response</small><output id="readout-16">-</output></div></div>' +
          '<div class="plot" id="plot-16"></div>',
    init: function(card) {
      try {
        var slider = card.querySelector('#param-16');
        var valOut = card.querySelector('#val-16');
        var resOut = card.querySelector('#readout-16');
        var plot = card.querySelector('#plot-16');
        var S = specs['thermal'];
        function update() {
          var v = Number(slider.value);
          if (valOut) valOut.textContent = v.toFixed(3) + ' ' + S[4];
          var res = model('thermal', v);
          if (resOut) resOut.textContent = res.text;
          if (plot) plot.innerHTML = renderGraph('thermal', v, S);
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('Analog Electronics sim error in model 16:', err);
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
