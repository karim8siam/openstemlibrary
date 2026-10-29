/* Electrical Measurements & Instrumentation I Interactive Simulation Suite */
(function(window) {
  'use strict';

  const defs={
1:{labels:['Type A u (V)','Type B u (V)','Other u (V)','Coverage k'],calc:p=>{let u=Math.hypot(p[0],p[1],p[2]);return {value:u*p[3],text:`Combined u = ${u.toFixed(5)} V; expanded U = ${(u*p[3]).toFixed(5)} V (k=${p[3]})`,points:Array.from({length:80},(_,i)=>({x:1+i*2/79,y:u*(1+i*2/79)}))};}},
2:{labels:['Thevenin V (V)','Source R (kΩ)','Meter input R (kΩ)','Source voltage factor'],calc:p=>{let y=p[0]*p[3]*p[2]/(p[1]+p[2]);return {value:y,text:`Meter reads ${y.toFixed(5)} V; loading error ${((y/(p[0]*p[3])-1)*100).toFixed(3)}%`,points:Array.from({length:80},(_,i)=>{let r=50+(i*15000/79);return{x:r,y:p[0]*p[3]*r/(p[1]+r)};})};}},
3:{labels:['Excitation V','R1 (Ω)','R2 (Ω)','R3 (Ω)','Unknown Rx (Ω)'],calc:p=>{let r=p[3]*p[2]/p[1];let y=p[0]*(p[2]/(p[1]+p[2])-p[4]/(p[3]+p[4]));return {value:y,text:`Ideal balance Rx=${r.toFixed(3)} Ω; detector V=${y.toFixed(6)} V for selected Rx=${p[4]} Ω`,points:Array.from({length:80},(_,i)=>{let rx=r*(.65+i*.7/79);return{x:rx,y:p[0]*(p[2]/(p[1]+p[2])-rx/(p[3]+rx))};})};}},
4:{labels:['Primary I (A)','CT ratio N = Ip/Is','Burden R (Ω)','Cable resistance (Ω)'],calc:p=>{let isec=p[0]/p[1];let x=isec*isec*(p[2]+p[3]);return{value:x,text:`Ideal Is=${isec.toFixed(3)} A; total burden = ${x.toFixed(3)} VA (including cable resistance)`,points:Array.from({length:80},(_,i)=>{let ip=p[0]*i/79;return{x:ip,y:(ip/p[1])**2*(p[2]+p[3])};})};}},
5:{labels:['Signal frequency (Hz)','Sample rate (Hz)','Phase (°)','Amplitude'],calc:p=>{let alias=Math.abs(p[0]-Math.round(p[0]/p[1])*p[1]);return{value:alias,text:`Aliased displayed frequency: ${alias.toFixed(2)} Hz; Nyquist limit ${(p[1]/2).toFixed(2)} Hz; phase ${p[2]}°; amplitude ${p[3]}`,points:Array.from({length:80},(_,i)=>({x:i/p[1],y:p[3]*Math.sin(2*Math.PI*p[0]*i/p[1]+p[2]*Math.PI/180)}))};}},
6:{labels:['Bits','Reference voltage V','Input V','Offset V'],calc:p=>{let bits=Math.round(p[0]),n=2**bits,step=p[1]/n,vin=Math.min(p[1]-step,Math.max(0,p[2]+p[3])),code=Math.min(n-1,Math.max(0,Math.round(vin/step))),q=code*step,err=(q-vin)*1000;return{value:err,text:`LSB ${(step*1000).toFixed(5)} mV; code ${code}; quantization error ${err.toFixed(5)} mV; selected input ${p[2]} V; offset ${p[3]} V`,points:Array.from({length:80},(_,i)=>{let x=i/79*p[1];let c=Math.min(n-1,Math.round(x/step));return{x,y:(c*step-x)*1000};})};}},
7:{labels:['Calibration gain','Offset','Holdout x','Observed holdout y'],calc:p=>{let pred=p[0]*p[2]+p[1],err=p[3]-pred;return{value:err,text:`Predicted y=${pred.toFixed(4)}; holdout residual=${err.toFixed(4)}`,points:Array.from({length:80},(_,i)=>{let x=i*10/79;return{x,y:p[0]*x+p[1]};})};}},
8:{labels:['Signal A (mV)','Relative phase (°)','Noise density (mV / √Hz)','Integration time (s)'],calc:p=>{let x=p[0]*Math.cos(p[1]*Math.PI/180),y=p[0]*Math.sin(p[1]*Math.PI/180),noise=p[2]/(2*Math.sqrt(p[3]));return{value:Math.hypot(x,y),text:`In phase ${x.toFixed(4)} mV; quadrature ${y.toFixed(4)} mV; recovered magnitude ${Math.hypot(x,y).toFixed(4)} mV; illustrative noise RMS ${noise.toFixed(4)} mV`,points:Array.from({length:80},(_,i)=>({x:i/79*360,y:p[0]*Math.cos((i/79*360)*Math.PI/180)+p[2]/(2*Math.sqrt(p[3]))*Math.sin(i*17)}))};}}
};

  function makeSvgEl(tag, attrs) {
    var el = document.createElementNS('http://www.w3.org/2000/svg', tag);
    for (var k in attrs) {
      if (Object.prototype.hasOwnProperty.call(attrs, k)) {
        el.setAttribute(k, String(attrs[k]));
      }
    }
    return el;
  }

  function renderEMI1Plot(plot, id, res) {
    while (plot.firstChild) plot.removeChild(plot.firstChild);
    var W = 800, H = 320, L = 72, R = 20, T = 20, B = 48;
    var pts = res.points ? res.points.filter(function(p) { return Number.isFinite(p.x) && Number.isFinite(p.y); }) : [];
    if (pts.length === 0) return;
    var xs = pts.map(function(p) { return p.x; }), ys = pts.map(function(p) { return p.y; });
    var xmin = Math.min.apply(null, xs), xmax = Math.max.apply(null, xs);
    var ymin = Math.min.apply(null, ys), ymax = Math.max.apply(null, ys);
    if (ymax === ymin) { ymax += 1; ymin -= 1; }
    else { var pad = (ymax - ymin) * 0.1; ymin -= pad; ymax += pad; }
    if (xmax === xmin) xmax = xmin + 1;

    var px = function(x) { return L + (W - L - R) * (x - xmin) / (xmax - xmin); };
    var py = function(y) { return T + (H - T - B) * (ymax - y) / (ymax - ymin); };

    for (var i = 0; i <= 4; i++) {
      var gy = T + i * (H - T - B) / 4;
      var yv = ymax - i * (ymax - ymin) / 4;
      plot.appendChild(makeSvgEl('line', {x1: L, y1: gy, x2: W - R, y2: gy, stroke: '#e2e8f0'}));
      var yt = makeSvgEl('text', {x: L - 8, y: gy + 4, fill: '#64748b', 'text-anchor': 'end', 'font-size': 11});
      yt.textContent = yv.toPrecision(3);
      plot.appendChild(yt);
    }
    for (var j = 0; j <= 5; j++) {
      var gx = L + j * (W - L - R) / 5;
      var xv = xmin + j * (xmax - xmin) / 5;
      plot.appendChild(makeSvgEl('line', {x1: gx, y1: T, x2: gx, y2: H - B, stroke: '#f1f5f9'}));
      var xt = makeSvgEl('text', {x: gx, y: H - B + 18, 'text-anchor': 'middle', fill: '#64748b', 'font-size': 11});
      xt.textContent = xv.toPrecision(3);
      plot.appendChild(xt);
    }

    var ptsStr = pts.map(function(p) { return px(p.x).toFixed(1) + ',' + py(p.y).toFixed(1); }).join(' ');
    plot.appendChild(makeSvgEl('polyline', {
      points: ptsStr,
      fill: 'none',
      stroke: '#0369a1',
      'stroke-width': 2.5,
      'stroke-linecap': 'round',
      'stroke-linejoin': 'round'
    }));

    var xl = makeSvgEl('text', {x: W / 2, y: H - 8, 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12});
    xl.textContent = 'Sweep parameter: ' + xmin.toPrecision(3) + ' → ' + xmax.toPrecision(3);
    plot.appendChild(xl);
    var yl = makeSvgEl('text', {x: 16, y: (H - B + T) / 2, transform: 'rotate(-90 16 ' + ((H - B + T) / 2) + ')', 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12});
    yl.textContent = 'Meter response';
    plot.appendChild(yl);
  }

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: '<div class="sim-header"><span class="badge">Model 01</span><h3>' + "Measurement uncertainty propagation" + '</h3><p>' + "Evaluate Type A and Type B combined standard uncertainty and expanded uncertainty bounds." + '</p></div>' +
          '<div class="sim-controls" id="controls-emi1-1"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Measurement Output</small><output id="out-metric-emi1-1">-</output></div></div>' +
          '<svg id="plot-emi1-1" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-emi1-1');
        var metricEl = card.querySelector('#out-metric-emi1-1');
        var plotEl = card.querySelector('#plot-emi1-1');
        var cfgControls = [["Type A u (V)", 0.01, 1.0, 0.25, 0.01], ["Type B u (V)", 0.01, 1.0, 0.4, 0.01], ["Other u (V)", 0.0, 0.5, 0.1, 0.01], ["Coverage k", 1.0, 3.0, 2.0, 0.5]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = c[1];
          inp.max = c[2];
          inp.step = c[4];
          inp.value = c[3];
          inp.setAttribute('aria-label', c[0]);
          div.appendChild(lab);
          div.appendChild(inp);
          ctrlsDiv.appendChild(div);
          inputs.push(inp);
          inp.addEventListener('input', function() {
            valSpan.textContent = inp.value;
            update();
          });
        });

        function update() {
          var v = inputs.map(function(el) { return Number(el.value); });
          var def = defs[1];
          if (def && def.calc) {
            var res = def.calc(v);
            if (metricEl) metricEl.textContent = res.text;
            if (plotEl) renderEMI1Plot(plotEl, 1, res);
          }
        }
        update();
      } catch (err) {
        console.warn('EMI1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 2,
    html: '<div class="sim-header"><span class="badge">Model 02</span><h3>' + "Voltmeter loading and input resistance" + '</h3><p>' + "Observe meter loading error as voltmeter internal resistance compares with source Thevenin impedance." + '</p></div>' +
          '<div class="sim-controls" id="controls-emi1-2"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Measurement Output</small><output id="out-metric-emi1-2">-</output></div></div>' +
          '<svg id="plot-emi1-2" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-emi1-2');
        var metricEl = card.querySelector('#out-metric-emi1-2');
        var plotEl = card.querySelector('#plot-emi1-2');
        var cfgControls = [["Thevenin V (V)", 1, 100, 10, 1], ["Source R (k\u03a9)", 1, 100, 20, 1], ["Meter R (k\u03a9)", 10, 1000, 200, 10], ["Scale factor", 0.5, 1.5, 1.0, 0.1]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = c[1];
          inp.max = c[2];
          inp.step = c[4];
          inp.value = c[3];
          inp.setAttribute('aria-label', c[0]);
          div.appendChild(lab);
          div.appendChild(inp);
          ctrlsDiv.appendChild(div);
          inputs.push(inp);
          inp.addEventListener('input', function() {
            valSpan.textContent = inp.value;
            update();
          });
        });

        function update() {
          var v = inputs.map(function(el) { return Number(el.value); });
          var def = defs[2];
          if (def && def.calc) {
            var res = def.calc(v);
            if (metricEl) metricEl.textContent = res.text;
            if (plotEl) renderEMI1Plot(plotEl, 2, res);
          }
        }
        update();
      } catch (err) {
        console.warn('EMI1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 3,
    html: '<div class="sim-header"><span class="badge">Model 03</span><h3>' + "Wheatstone DC bridge balance sensitivity" + '</h3><p>' + "Balance condition Rx = R2\u00b7R3/R1 and galvanometer deflection off null balance." + '</p></div>' +
          '<div class="sim-controls" id="controls-emi1-3"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Measurement Output</small><output id="out-metric-emi1-3">-</output></div></div>' +
          '<svg id="plot-emi1-3" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-emi1-3');
        var metricEl = card.querySelector('#out-metric-emi1-3');
        var plotEl = card.querySelector('#plot-emi1-3');
        var cfgControls = [["Excitation V", 1, 24, 10, 1], ["R1 (\u03a9)", 10, 500, 100, 5], ["R2 (\u03a9)", 10, 500, 100, 5], ["R3 (\u03a9)", 10, 500, 100, 5], ["Rx (\u03a9)", 50, 150, 100, 1]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = c[1];
          inp.max = c[2];
          inp.step = c[4];
          inp.value = c[3];
          inp.setAttribute('aria-label', c[0]);
          div.appendChild(lab);
          div.appendChild(inp);
          ctrlsDiv.appendChild(div);
          inputs.push(inp);
          inp.addEventListener('input', function() {
            valSpan.textContent = inp.value;
            update();
          });
        });

        function update() {
          var v = inputs.map(function(el) { return Number(el.value); });
          var def = defs[3];
          if (def && def.calc) {
            var res = def.calc(v);
            if (metricEl) metricEl.textContent = res.text;
            if (plotEl) renderEMI1Plot(plotEl, 3, res);
          }
        }
        update();
      } catch (err) {
        console.warn('EMI1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 4,
    html: '<div class="sim-header"><span class="badge">Model 04</span><h3>' + "Current transformer (CT) secondary burden" + '</h3><p>' + "Secondary winding current and VA burden under primary load variations." + '</p></div>' +
          '<div class="sim-controls" id="controls-emi1-4"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Measurement Output</small><output id="out-metric-emi1-4">-</output></div></div>' +
          '<svg id="plot-emi1-4" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-emi1-4');
        var metricEl = card.querySelector('#out-metric-emi1-4');
        var plotEl = card.querySelector('#plot-emi1-4');
        var cfgControls = [["Primary I (A)", 10, 500, 100, 5], ["CT ratio N", 10, 100, 20, 5], ["Burden R (\u03a9)", 0.1, 5.0, 1.0, 0.1], ["Cable R (\u03a9)", 0.05, 1.0, 0.2, 0.05]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = c[1];
          inp.max = c[2];
          inp.step = c[4];
          inp.value = c[3];
          inp.setAttribute('aria-label', c[0]);
          div.appendChild(lab);
          div.appendChild(inp);
          ctrlsDiv.appendChild(div);
          inputs.push(inp);
          inp.addEventListener('input', function() {
            valSpan.textContent = inp.value;
            update();
          });
        });

        function update() {
          var v = inputs.map(function(el) { return Number(el.value); });
          var def = defs[4];
          if (def && def.calc) {
            var res = def.calc(v);
            if (metricEl) metricEl.textContent = res.text;
            if (plotEl) renderEMI1Plot(plotEl, 4, res);
          }
        }
        update();
      } catch (err) {
        console.warn('EMI1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 5,
    html: '<div class="sim-header"><span class="badge">Model 05</span><h3>' + "Electrodynamic wattmeter phase angle" + '</h3><p>' + "Power measurement accuracy and power factor sensitivity under reactive phase shift." + '</p></div>' +
          '<div class="sim-controls" id="controls-emi1-5"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Measurement Output</small><output id="out-metric-emi1-5">-</output></div></div>' +
          '<svg id="plot-emi1-5" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-emi1-5');
        var metricEl = card.querySelector('#out-metric-emi1-5');
        var plotEl = card.querySelector('#plot-emi1-5');
        var cfgControls = [["Frequency (Hz)", 10, 100, 50, 5], ["Sample rate (Hz)", 100, 2000, 500, 50], ["Phase (\u00b0)", 0, 90, 30, 5], ["Amplitude", 1, 10, 5, 0.5]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = c[1];
          inp.max = c[2];
          inp.step = c[4];
          inp.value = c[3];
          inp.setAttribute('aria-label', c[0]);
          div.appendChild(lab);
          div.appendChild(inp);
          ctrlsDiv.appendChild(div);
          inputs.push(inp);
          inp.addEventListener('input', function() {
            valSpan.textContent = inp.value;
            update();
          });
        });

        function update() {
          var v = inputs.map(function(el) { return Number(el.value); });
          var def = defs[5];
          if (def && def.calc) {
            var res = def.calc(v);
            if (metricEl) metricEl.textContent = res.text;
            if (plotEl) renderEMI1Plot(plotEl, 5, res);
          }
        }
        update();
      } catch (err) {
        console.warn('EMI1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 6,
    html: '<div class="sim-header"><span class="badge">Model 06</span><h3>' + "Maxwell-Wien AC bridge balance" + '</h3><p>' + "Measure unknown inductance and series resistance via standard capacitance arm." + '</p></div>' +
          '<div class="sim-controls" id="controls-emi1-6"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Measurement Output</small><output id="out-metric-emi1-6">-</output></div></div>' +
          '<svg id="plot-emi1-6" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-emi1-6');
        var metricEl = card.querySelector('#out-metric-emi1-6');
        var plotEl = card.querySelector('#plot-emi1-6');
        var cfgControls = [["R1 (\u03a9)", 100, 5000, 1000, 50], ["R2 (\u03a9)", 100, 5000, 1000, 50], ["R3 (\u03a9)", 100, 5000, 1000, 50], ["C3 (\u00b5F)", 0.01, 2.0, 0.1, 0.01]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = c[1];
          inp.max = c[2];
          inp.step = c[4];
          inp.value = c[3];
          inp.setAttribute('aria-label', c[0]);
          div.appendChild(lab);
          div.appendChild(inp);
          ctrlsDiv.appendChild(div);
          inputs.push(inp);
          inp.addEventListener('input', function() {
            valSpan.textContent = inp.value;
            update();
          });
        });

        function update() {
          var v = inputs.map(function(el) { return Number(el.value); });
          var def = defs[6];
          if (def && def.calc) {
            var res = def.calc(v);
            if (metricEl) metricEl.textContent = res.text;
            if (plotEl) renderEMI1Plot(plotEl, 6, res);
          }
        }
        update();
      } catch (err) {
        console.warn('EMI1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 7,
    html: '<div class="sim-header"><span class="badge">Model 07</span><h3>' + "Schering capacitance and dielectric loss" + '</h3><p>' + "Dissipation factor tan \u03b4 determination and high-voltage capacitance bridge balance." + '</p></div>' +
          '<div class="sim-controls" id="controls-emi1-7"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Measurement Output</small><output id="out-metric-emi1-7">-</output></div></div>' +
          '<svg id="plot-emi1-7" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-emi1-7');
        var metricEl = card.querySelector('#out-metric-emi1-7');
        var plotEl = card.querySelector('#plot-emi1-7');
        var cfgControls = [["Frequency (Hz)", 50, 1000, 50, 10], ["C1 (nF)", 1, 100, 10, 1], ["R1 (k\u03a9)", 1, 100, 10, 1], ["Loss factor", 0.001, 0.1, 0.02, 0.001]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = c[1];
          inp.max = c[2];
          inp.step = c[4];
          inp.value = c[3];
          inp.setAttribute('aria-label', c[0]);
          div.appendChild(lab);
          div.appendChild(inp);
          ctrlsDiv.appendChild(div);
          inputs.push(inp);
          inp.addEventListener('input', function() {
            valSpan.textContent = inp.value;
            update();
          });
        });

        function update() {
          var v = inputs.map(function(el) { return Number(el.value); });
          var def = defs[7];
          if (def && def.calc) {
            var res = def.calc(v);
            if (metricEl) metricEl.textContent = res.text;
            if (plotEl) renderEMI1Plot(plotEl, 7, res);
          }
        }
        update();
      } catch (err) {
        console.warn('EMI1 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 8,
    html: '<div class="sim-header"><span class="badge">Model 08</span><h3>' + "Search-coil magnetic fluxmeter deflection" + '</h3><p>' + "Flux linkage integration and induced voltage ballistic galvanometer trajectory." + '</p></div>' +
          '<div class="sim-controls" id="controls-emi1-8"></div>' +
          '<div class="readouts"><div class="stat-box"><small>Measurement Output</small><output id="out-metric-emi1-8">-</output></div></div>' +
          '<svg id="plot-emi1-8" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-emi1-8');
        var metricEl = card.querySelector('#out-metric-emi1-8');
        var plotEl = card.querySelector('#plot-emi1-8');
        var cfgControls = [["Coil turns N", 10, 500, 100, 10], ["Area A (cm\u00b2)", 1, 50, 10, 1], ["Flux change \u0394B (T)", 0.05, 2.0, 0.8, 0.05], ["Resistance R (\u03a9)", 10, 200, 50, 5]];
        var inputs = [];

        ctrlsDiv.innerHTML = '';
        cfgControls.forEach(function(c, ci) {
          var div = document.createElement('div');
          div.className = 'control';
          var lab = document.createElement('label');
          lab.textContent = c[0] + ': ';
          var valSpan = document.createElement('strong');
          valSpan.textContent = c[3];
          lab.appendChild(valSpan);
          var inp = document.createElement('input');
          inp.type = 'range';
          inp.min = c[1];
          inp.max = c[2];
          inp.step = c[4];
          inp.value = c[3];
          inp.setAttribute('aria-label', c[0]);
          div.appendChild(lab);
          div.appendChild(inp);
          ctrlsDiv.appendChild(div);
          inputs.push(inp);
          inp.addEventListener('input', function() {
            valSpan.textContent = inp.value;
            update();
          });
        });

        function update() {
          var v = inputs.map(function(el) { return Number(el.value); });
          var def = defs[8];
          if (def && def.calc) {
            var res = def.calc(v);
            if (metricEl) metricEl.textContent = res.text;
            if (plotEl) renderEMI1Plot(plotEl, 8, res);
          }
        }
        update();
      } catch (err) {
        console.warn('EMI1 init error:', err);
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
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.slice(0, 1);
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
