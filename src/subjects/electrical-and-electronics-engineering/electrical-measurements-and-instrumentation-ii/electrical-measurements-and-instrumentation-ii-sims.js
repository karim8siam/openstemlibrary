/* Electrical Measurements & Instrumentation II Interactive Simulation Suite */
(function(window) {
  'use strict';

  const numeric=(x)=>Number.isFinite(x)?x:0;
function gaussianTail(z){const t=1/(1+0.2316419*Math.abs(z));const d=0.3989422804014327*Math.exp(-z*z/2);const q=d*t*(0.31938153+t*(-0.356563782+t*(1.781477937+t*(-1.821255978+t*1.330274429))));return z>=0?q:1-q;}
const models={
1:p=>{const [T,a,b,c]=p;const v=t=>a+b*t+c*t*t;return{value:v(T),message:`Voltage ${v(T).toFixed(5)} V; local sensitivity ${(b+2*c*T).toFixed(5)} V/°C; +2 mV local error ≈ ${(0.002/(b+2*c*T)).toFixed(4)} °C`,points:Array.from({length:101},(_,i)=>({x:i,y:v(i)}))};},
2:p=>{const [ppm,h,offset,ref]=p;const drift=t=>offset+(ppm-ref)*1e-6*t*3600*1000;return{value:drift(h),message:`Net rate error ${(ppm-ref).toFixed(3)} ppm; accumulated time error ${drift(h).toFixed(4)} ms`,points:Array.from({length:85},(_,i)=>{let x=i*h/84;return{x,y:drift(x)};})};},
3:p=>{const [f,scan,filter,cable]=p;const delay=scan+filter+cable;const phase=x=>360*x*delay*1e-6;return{value:phase(f),message:`Total skew ${delay} µs; phase = ${phase(f).toFixed(3)}° (unwrapped); modulo 360° = ${((phase(f)%360)+360)%360}°`,points:Array.from({length:90},(_,i)=>({x:10+i*2990/89,y:phase(10+i*2990/89)}))};},
4:p=>{const [R,C,f,fixture]=p;const z=x=>Math.hypot(R+fixture,1/(2*Math.PI*x*C*1e-6));const angle=-Math.atan2(1/(2*Math.PI*f*C*1e-6),R+fixture)*180/Math.PI;return{value:z(f),message:`|Z|=${z(f).toFixed(3)} Ω; phase=${angle.toFixed(2)}° at ${f} Hz`,points:Array.from({length:110},(_,i)=>{let x=50+i*9950/109;return{x,y:z(x)};})};},
5:p=>{const [a,phase,xbg,ybg]=p;const rad=phase*Math.PI/180;const X=a*Math.cos(rad)+xbg,Y=a*Math.sin(rad)+ybg;return{value:Math.hypot(X,Y),message:`X=${X.toFixed(3)} µV; Y=${Y.toFixed(3)} µV; vector magnitude=${Math.hypot(X,Y).toFixed(3)} µV`,points:Array.from({length:97},(_,i)=>{let t=i*2*Math.PI/96;return{x:t*180/Math.PI,y:a*Math.cos(t)+xbg};})};},
6:p=>{const [bin,hann,a,noise]=p;const N=128;const data=Array.from({length:N},(_,n)=>a*Math.cos(2*Math.PI*bin*n/N)+noise*Math.cos(2*Math.PI*37*n/N));const win=Array.from({length:N},(_,n)=>hann>0.5?(0.5-0.5*Math.cos(2*Math.PI*n/(N-1))):1);const coherent=win.reduce((x,y)=>x+y,0)/N;const bins=Array.from({length:64},(_,k)=>{let re=0,im=0;for(let n=0;n<N;n++){const theta=2*Math.PI*k*n/N;re+=data[n]*win[n]*Math.cos(theta);im-=data[n]*win[n]*Math.sin(theta);}return{x:k,y:2*Math.hypot(re,im)/N/coherent};});const peak=bins.reduce((m,q)=>q.y>m.y?q:m,bins[0]);return{value:peak.y,message:`Strongest observed bin ${peak.x}; estimated bin amplitude ${peak.y.toFixed(4)}; window=${hann>.5?'Hann':'rectangular'}. Non-bin-centered tones leak.`,points:bins};},
7:p=>{const [conv,overhead,batch,gap]=p;const rate=n=>1000*n/(n*conv+overhead+gap);return{value:rate(batch),message:`Ideal sustained throughput ≈${rate(batch).toFixed(1)} samples/s; batch duration ${(batch*conv+overhead+gap).toFixed(2)} ms`,points:Array.from({length:100},(_,i)=>{let x=1+i*499/99;return{x,y:rate(x)};})};},
8:p=>{const [sigma,N,mu,sd]=p;const pfa=gaussianTail(sigma);return{value:N*pfa,message:`Threshold = ${(mu+sd*sigma).toFixed(3)} physical score; single-test tail probability ≈${pfa.toExponential(3)}; expected exceedances ≈${(N*pfa).toFixed(2)}`,points:Array.from({length:80},(_,i)=>{let x=1+i*4/79;return{x,y:N*gaussianTail(x)};})};}
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

  function renderEMI2Plot(plot, id, res) {
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
      stroke: '#0d9488',
      'stroke-width': 2.5,
      'stroke-linecap': 'round',
      'stroke-linejoin': 'round'
    }));

    var xl = makeSvgEl('text', {x: W / 2, y: H - 8, 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12});
    xl.textContent = 'Parameter span: ' + xmin.toPrecision(3) + ' → ' + xmax.toPrecision(3);
    plot.appendChild(xl);
    var yl = makeSvgEl('text', {x: 16, y: (H - B + T) / 2, transform: 'rotate(-90 16 ' + ((H - B + T) / 2) + ')', 'text-anchor': 'middle', fill: '#1e293b', 'font-size': 12});
    yl.textContent = 'Instrument response';
    plot.appendChild(yl);
  }

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: '<div class="sim-header"><span class="badge">Model 01</span><h3>' + "Nonlinear sensor transfer function and sensitivity" + '</h3><p>' + "Quadratic RTD/thermistor curve fitting, voltage sensitivity, and Taylor series error bounds." + '</p></div>' +
          '<div class="sim-controls" id="controls-emi2-1"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metric</small><output id="out-metric-emi2-1">-</output></div></div>' +
          '<svg id="plot-emi2-1" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-emi2-1');
        var metricEl = card.querySelector('#out-metric-emi2-1');
        var plotEl = card.querySelector('#plot-emi2-1');
        var cfgControls = [["Temperature T (\u00b0C)", 0, 100, 25, 1], ["Offset a (V)", 0.0, 1.0, 0.1, 0.01], ["Gain b (V/\u00b0C)", 0.005, 0.05, 0.02, 0.001], ["Curvature c", -0.0001, 0.0001, 2e-05, 5e-06]];
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
          var mFn = models[1];
          if (mFn) {
            var res = mFn(v);
            if (metricEl) metricEl.textContent = res.message;
            if (plotEl) renderEMI2Plot(plotEl, 1, res);
          }
        }
        update();
      } catch (err) {
        console.warn('EMI2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 2,
    html: '<div class="sim-header"><span class="badge">Model 02</span><h3>' + "Clock drift and counter time error" + '</h3><p>' + "Time-interval measurement drift, ppm crystal oscillator stability, and cumulative timing bias." + '</p></div>' +
          '<div class="sim-controls" id="controls-emi2-2"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metric</small><output id="out-metric-emi2-2">-</output></div></div>' +
          '<svg id="plot-emi2-2" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-emi2-2');
        var metricEl = card.querySelector('#out-metric-emi2-2');
        var plotEl = card.querySelector('#plot-emi2-2');
        var cfgControls = [["Crystal ppm", -50, 50, 15, 1], ["Duration (hours)", 1, 48, 12, 1], ["Initial offset (ms)", -5, 5, 0.5, 0.1], ["Ref ppm", -10, 10, 0, 1]];
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
          var mFn = models[2];
          if (mFn) {
            var res = mFn(v);
            if (metricEl) metricEl.textContent = res.message;
            if (plotEl) renderEMI2Plot(plotEl, 2, res);
          }
        }
        update();
      } catch (err) {
        console.warn('EMI2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 3,
    html: '<div class="sim-header"><span class="badge">Model 03</span><h3>' + "Multichannel DAQ sampling and skew" + '</h3><p>' + "Sequential multiplexer channel-to-channel time skew and phase error at elevated frequencies." + '</p></div>' +
          '<div class="sim-controls" id="controls-emi2-3"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metric</small><output id="out-metric-emi2-3">-</output></div></div>' +
          '<svg id="plot-emi2-3" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-emi2-3');
        var metricEl = card.querySelector('#out-metric-emi2-3');
        var plotEl = card.querySelector('#plot-emi2-3');
        var cfgControls = [["Channel count", 2, 16, 4, 1], ["Sample rate (kSa/s)", 10, 500, 100, 10], ["Signal f (kHz)", 1, 50, 10, 1], ["Amplitude", 0.5, 5, 2, 0.5]];
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
          var mFn = models[3];
          if (mFn) {
            var res = mFn(v);
            if (metricEl) metricEl.textContent = res.message;
            if (plotEl) renderEMI2Plot(plotEl, 3, res);
          }
        }
        update();
      } catch (err) {
        console.warn('EMI2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 4,
    html: '<div class="sim-header"><span class="badge">Model 04</span><h3>' + "Complex impedance spectroscopy" + '</h3><p>' + "Cole-Cole dielectric relaxation plot and RC network equivalent impedance circle." + '</p></div>' +
          '<div class="sim-controls" id="controls-emi2-4"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metric</small><output id="out-metric-emi2-4">-</output></div></div>' +
          '<svg id="plot-emi2-4" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-emi2-4');
        var metricEl = card.querySelector('#out-metric-emi2-4');
        var plotEl = card.querySelector('#plot-emi2-4');
        var cfgControls = [["R series (\u03a9)", 10, 500, 100, 5], ["R parallel (k\u03a9)", 1, 100, 10, 1], ["C (nF)", 1, 100, 10, 1], ["Frequency (kHz)", 0.1, 100, 5, 0.5]];
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
          var mFn = models[4];
          if (mFn) {
            var res = mFn(v);
            if (metricEl) metricEl.textContent = res.message;
            if (plotEl) renderEMI2Plot(plotEl, 4, res);
          }
        }
        update();
      } catch (err) {
        console.warn('EMI2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 5,
    html: '<div class="sim-header"><span class="badge">Model 05</span><h3>' + "Lock-in amplifier phase-sensitive detection" + '</h3><p>' + "Synchronous demodulation and narrow-band noise rejection of microvolt transducer signals." + '</p></div>' +
          '<div class="sim-controls" id="controls-emi2-5"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metric</small><output id="out-metric-emi2-5">-</output></div></div>' +
          '<svg id="plot-emi2-5" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-emi2-5');
        var metricEl = card.querySelector('#out-metric-emi2-5');
        var plotEl = card.querySelector('#plot-emi2-5');
        var cfgControls = [["Signal amp (mV)", 0.1, 10, 1.0, 0.1], ["Noise amp (mV)", 1, 50, 20, 1], ["Ref phase (\u00b0)", 0, 180, 0, 5], ["Filter time const (ms)", 10, 500, 100, 10]];
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
          var mFn = models[5];
          if (mFn) {
            var res = mFn(v);
            if (metricEl) metricEl.textContent = res.message;
            if (plotEl) renderEMI2Plot(plotEl, 5, res);
          }
        }
        update();
      } catch (err) {
        console.warn('EMI2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 6,
    html: '<div class="sim-header"><span class="badge">Model 06</span><h3>' + "ADC quantization and harmonic distortion" + '</h3><p>' + "Successive-approximation ADC quantization noise floor, SNR, and effective number of bits (ENOB)." + '</p></div>' +
          '<div class="sim-controls" id="controls-emi2-6"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metric</small><output id="out-metric-emi2-6">-</output></div></div>' +
          '<svg id="plot-emi2-6" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-emi2-6');
        var metricEl = card.querySelector('#out-metric-emi2-6');
        var plotEl = card.querySelector('#plot-emi2-6');
        var cfgControls = [["ADC resolution (bits)", 4, 16, 8, 1], ["Input amp (V)", 0.1, 5.0, 2.5, 0.1], ["Full scale (V)", 1.0, 10.0, 5.0, 0.5], ["Harmonic factor", 0.0, 0.2, 0.02, 0.005]];
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
          var mFn = models[6];
          if (mFn) {
            var res = mFn(v);
            if (metricEl) metricEl.textContent = res.message;
            if (plotEl) renderEMI2Plot(plotEl, 6, res);
          }
        }
        update();
      } catch (err) {
        console.warn('EMI2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 7,
    html: '<div class="sim-header"><span class="badge">Model 07</span><h3>' + "Strain gauge bridge conditioning and non-linearity" + '</h3><p>' + "Quarter-bridge and full-bridge strain measurement, lead resistance cancellation, and Poisson ratio." + '</p></div>' +
          '<div class="sim-controls" id="controls-emi2-7"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metric</small><output id="out-metric-emi2-7">-</output></div></div>' +
          '<svg id="plot-emi2-7" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-emi2-7');
        var metricEl = card.querySelector('#out-metric-emi2-7');
        var plotEl = card.querySelector('#plot-emi2-7');
        var cfgControls = [["Strain \u03b5 (\u00b5\u03b5)", 10, 2000, 500, 20], ["Gauge factor GF", 1.5, 4.0, 2.1, 0.1], ["Excitation V (V)", 1, 15, 5, 0.5], ["Bridge type (1=q,4=f)", 1, 4, 1, 3]];
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
          var mFn = models[7];
          if (mFn) {
            var res = mFn(v);
            if (metricEl) metricEl.textContent = res.message;
            if (plotEl) renderEMI2Plot(plotEl, 7, res);
          }
        }
        update();
      } catch (err) {
        console.warn('EMI2 init error:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 8,
    html: '<div class="sim-header"><span class="badge">Model 08</span><h3>' + "Virtual instrument automated measurement loop" + '</h3><p>' + "SCPI trigger latency, data buffer throughput, and GPIB/USB communication timing." + '</p></div>' +
          '<div class="sim-controls" id="controls-emi2-8"></div>' +
          '<div class="readouts"><div class="stat-box"><small>System Metric</small><output id="out-metric-emi2-8">-</output></div></div>' +
          '<svg id="plot-emi2-8" viewBox="0 0 800 320" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;"></svg>',
    init: function(card) {
      try {
        var ctrlsDiv = card.querySelector('#controls-emi2-8');
        var metricEl = card.querySelector('#out-metric-emi2-8');
        var plotEl = card.querySelector('#plot-emi2-8');
        var cfgControls = [["Command rate (cmd/s)", 10, 500, 100, 10], ["Buffer size", 64, 2048, 256, 64], ["Transfer mode", 1, 3, 1, 1], ["Payload bytes", 16, 1024, 128, 16]];
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
          var mFn = models[8];
          if (mFn) {
            var res = mFn(v);
            if (metricEl) metricEl.textContent = res.message;
            if (plotEl) renderEMI2Plot(plotEl, 8, res);
          }
        }
        update();
      } catch (err) {
        console.warn('EMI2 init error:', err);
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
