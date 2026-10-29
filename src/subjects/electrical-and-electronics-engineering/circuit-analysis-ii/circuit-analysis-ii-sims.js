/* Circuit Analysis II Interactive Simulation Suite */
(function(window) {
  'use strict';
  const pi = Math.PI, sq = Math.sqrt;
  const logspace = (a, b, n=81) => Array.from({length: n}, (_, i) => a * Math.pow(b / a, i / (n - 1)));
  const line = (fn, xs) => xs.map(x => [x, fn(x)]);
  const format = v => typeof v === 'number' ? (Math.abs(v) >= 1000 || (Math.abs(v) < 0.01 && v !== 0) ? v.toExponential(3) : v.toFixed(3)) : v;

function calculate(id,p){
const f=(k)=>Number(p[k]);let a,b,c,d,xs,points,metrics,units,axis;
switch(id){
case 1:{let V=f('Vm'),freq=f('f');points=line(t=>V*Math.cos(2*pi*freq*t),Array.from({length:161},(_,i)=>2*i/(160*freq)));metrics=[['RMS voltage',V/sq(2),'V'],['Period',1000/freq,'ms']];axis='Voltage (V)';break;}
case 2:{let freq=f('f'),ang=f('phi');points=line(t=>Math.cos(2*pi*freq*t-ang*pi/180),Array.from({length:161},(_,i)=>2*i/(160*freq)));metrics=[['Lag time',1000*ang/(360*freq),'ms'],['Phase in radians',ang*pi/180,'rad']];axis='Lagging signal / reference = 1';break;}
case 3:{let R=f('R'),L=f('L')*.001,freq=f('f');xs=logspace(10,5000);points=line(x=>Math.hypot(R,2*pi*x*L),xs);metrics=[['Impedance magnitude',Math.hypot(R,2*pi*freq*L),'Ω'],['Angle',Math.atan2(2*pi*freq*L,R)*180/pi,'deg']];axis='|Z| (Ω)';break;}
case 4:{let R=f('R'),C=f('C')*1e-6,freq=f('f');xs=logspace(10,5000);points=line(x=>Math.hypot(R,1/(2*pi*x*C)),xs);metrics=[['Impedance magnitude',Math.hypot(R,1/(2*pi*freq*C)),'Ω'],['Angle',Math.atan2(-1/(2*pi*freq*C),R)*180/pi,'deg']];axis='|Z| (Ω)';break;}
case 5:{let V=f('V'),I=f('I'),pf=f('pf');xs=Array.from({length:81},(_,i)=>i/80);points=line(x=>V*I*x,xs);metrics=[['Real power',V*I*pf,'W'],['Reactive power',V*I*sq(1-pf*pf),'var'],['Apparent power',V*I,'VA']];axis='Real P (W)';break;}
case 6:{let P=f('P'),pf=f('pf'),tar=f('target');let q=z=>P*sq(1-z*z)/z;points=line(x=>q(pf)-q(x),Array.from({length:81},(_,i)=>Math.max(.1,pf)+(1-Math.max(.1,pf))*i/80));metrics=[['Capacitive var needed',q(pf)-q(tar),'var'],['New apparent power',P/tar,'VA']];axis='Correction Qc (var)';break;}
case 7:{let R=f('R'),L=f('L')*.001,C=f('C')*1e-6;let f0=1/(2*pi*sq(L*C));xs=logspace(Math.max(1,f0/10),f0*10);points=line(h=>10/Math.hypot(R,2*pi*h*L-1/(2*pi*h*C)),xs);metrics=[['Resonant frequency',f0,'Hz'],['Peak current (10 V RMS)',10/R,'A'],['Series Q',2*pi*f0*L/R,'unitless']];axis='Current RMS (A)';break;}
case 8:{let V=f('VL'),I=f('IL'),pf=f('pf');points=line(t=>sq(3)*V*t*pf,Array.from({length:81},(_,i)=>.1+40*i/80));metrics=[['Total real power',sq(3)*V*I*pf,'W'],['Total apparent power',sq(3)*V*I,'VA'],['Phase-neutral voltage',V/sq(3),'V']];axis='Three-phase P (W)';break;}
case 9:{let L1=f('L1'),L2=f('L2'),k=f('k');let M=k*sq(L1*L2);points=line(x=>L1+L2+2*x*sq(L1*L2),Array.from({length:81},(_,i)=>i/80));metrics=[['Mutual inductance',M,'mH'],['Aiding equivalent',L1+L2+2*M,'mH'],['Opposing equivalent',L1+L2-2*M,'mH']];axis='Equivalent L (mH)';break;}
case 10:{let n=f('ratio'),Vp=f('Vp'),RL=f('RL');points=line(x=>Vp/x,Array.from({length:81},(_,i)=>1+19*i/80));metrics=[['Secondary voltage',Vp/n,'V'],['Reflected input load',n*n*RL,'Ω'],['Secondary current',Vp/(n*RL),'A']];axis='Vs (V)';break;}
case 11:{let tau=f('R')*1000*f('C')*1e-6,V=f('V');points=line(t=>V*(1-Math.exp(-t/tau)),Array.from({length:81},(_,i)=>6*tau*i/80));metrics=[['RC time constant',1000*tau,'ms'],['Capacitor after 1τ',V*(1-Math.exp(-1)),'V']];axis='Vc (V)';break;}
case 12:{let R=f('R'),L=f('L')*.001,C=f('C')*1e-6;let w0=1/sq(L*C),z=R/2*sq(C/L);points=line(x=>x/2*sq(C/L),Array.from({length:81},(_,i)=>i*300/80));metrics=[['Natural frequency',w0/(2*pi),'Hz'],['Damping ratio',z,'unitless'],['Damping regime',z<1?'Underdamped':z>1?'Overdamped':'Critical','text']];axis='Damping ratio';break;}
case 13:{let R=f('R')*1e3,C=f('C')*1e-9,freq=f('f'),fc=1/(2*pi*R*C);points=line(x=>1/sq(1+(x/fc)**2),logspace(fc/30,fc*30));metrics=[['Cutoff frequency',fc,'Hz'],['Gain at selected f',1/sq(1+(freq/fc)**2),'V/V'],['Phase',-Math.atan(freq/fc)*180/pi,'deg']];axis='|Hlow| (V/V)';break;}
case 14:{let R=f('R')*1e3,C=f('C')*1e-9,freq=f('f'),fc=1/(2*pi*R*C);points=line(x=>(x/fc)/sq(1+(x/fc)**2),logspace(fc/30,fc*30));metrics=[['Cutoff frequency',fc,'Hz'],['Gain at selected f',(freq/fc)/sq(1+(freq/fc)**2),'V/V'],['Phase',Math.atan(fc/freq)*180/pi,'deg']];axis='|Hhigh| (V/V)';break;}
case 15:{let A=f('A'),n=Math.round(f('n'));points=line(x=>x%2?4*A/(pi*x):0,Array.from({length:21},(_,i)=>i+1));metrics=[['Selected harmonic amplitude',n%2?4*A/(pi*n):0,'V peak'],['Fundamental amplitude',4*A/pi,'V peak']];axis='Harmonic amplitude (V)';break;}
case 16:{let fs=f('fs'),fin=f('fin');let alias=x=>Math.abs(((x+fs/2)%fs+fs)%fs-fs/2);points=line(alias,Array.from({length:121},(_,i)=>3*fs*i/120));metrics=[['Apparent alias frequency',alias(fin),'Hz'],['Nyquist frequency',fs/2,'Hz']];axis='Apparent tone (Hz)';break;}
default:throw Error('Unknown model');}
return {metrics,points,axis,xlabel:['Time (s)','Time (s)','Frequency (Hz)','Frequency (Hz)','Power factor','Target power factor','Frequency (Hz)','Line current (A)','Coupling k','Turns ratio Np/Ns','Time (s)','Resistance (Ω)','Frequency (Hz)','Frequency (Hz)','Harmonic number','Input tone frequency (Hz)'][id-1]};}
function format(n){if(typeof n==='string')return n; if(!Number.isFinite(n))return 'undefined';if(n===0)return '0';return (Math.abs(n)>=1e5||Math.abs(n)<.001)?n.toExponential(3):Number(n.toPrecision(5)).toString();}
function draw(svg,points,axis,xlabel){const good=points.filter(z=>Number.isFinite(z[0])&&Number.isFinite(z[1]));if(!good.length)return;const x0=Math.min(...good.map(z=>z[0])),x1=Math.max(...good.map(z=>z[0])),y0=Math.min(0,...good.map(z=>z[1])),y1=Math.max(1e-12,...good.map(z=>z[1]));let xx=x=>45+590*(x-x0)/(x1-x0||1),yy=y=>270-230*(y-y0)/(y1-y0||1);const vals=good.map(z=>`${xx(z[0]).toFixed(2)},${yy(z[1]).toFixed(2)}`).join(' ');svg.innerHTML='<rect x="0" y="0" width="670" height="320" fill="#fcfefe"/><g stroke="#deeaed" stroke-width="1"><line x1="45" y1="40" x2="45" y2="270"/><line x1="45" y1="270" x2="635" y2="270"/></g><polyline fill="none" stroke="#008978" stroke-width="3" points="'+vals+'"/><g fill="#254452" font-size="13"><text x="45" y="291">'+format(x0)+'</text><text x="565" y="291">'+format(x1)+'</text><text x="50" y="30">'+axis+'</text><text x="290" y="312">'+xlabel+'</text><text x="8" y="45">'+format(y1)+'</text><text x="8" y="266">'+format(y0)+'</text></g>';}

  function draw(svg, points, axis, xlabel) {
    const W = 670, H = 260, pad = 50;
    if (!points || !points.length) return;
    const xs = points.map(d => d[0]), ys = points.map(d => d[1]);
    const minX = Math.min(...xs), maxX = Math.max(...xs);
    let minY = Math.min(...ys), maxY = Math.max(...ys);
    if (minY === maxY) { minY -= 1; maxY += 1; }
    const sx = x => pad + (x - minX) / (maxX - minX || 1) * (W - 2 * pad);
    const sy = y => H - pad - (y - minY) / (maxY - minY || 1) * (H - 2 * pad);
    const pStr = points.map((d, i) => (i ? 'L' : 'M') + sx(d[0]).toFixed(1) + ',' + sy(d[1]).toFixed(1)).join(' ');
    svg.innerHTML = `
      <rect x="${pad}" y="${pad / 2}" width="${W - 2 * pad}" height="${H - 1.5 * pad}" fill="#0f172a" rx="4"/>
      <path d="${pStr}" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      <text x="${pad}" y="${H - 10}" fill="#94a3b8" font-size="11">${xlabel || 'Input'}</text>
      <text x="${W - pad}" y="${H - 10}" fill="#38bdf8" text-anchor="end" font-size="11">${axis || 'Output'}</text>
      <text x="${pad}" y="${pad / 2 - 4}" fill="#64748b" font-size="10">${format(maxY)}</text>
      <text x="${pad}" y="${H - pad + 14}" fill="#64748b" font-size="10">${format(minY)}</text>
    `;
  }

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 01</span><h3>Sinusoid and RMS Explorer</h3><p>Study peak voltage, RMS voltage and cycles per second. The plot shows one generated voltage waveform.</p><p><code>V(t) = Vm cos(2\u03c0 f t); Vrms = Vm/\u221a2.</code></p></div><div class=\"sim-controls\"><div class=\"control\"><label for=\"Vm\">Peak voltage <strong id=\"value-Vm\"></strong></label><input id=\"Vm\" data-param=\"Vm\" data-unit=\"V\" type=\"range\" min=\"1\" max=\"24\" step=\"any\" value=\"12\"></div><div class=\"control\"><label for=\"f\">Frequency <strong id=\"value-f\"></strong></label><input id=\"f\" data-param=\"f\" data-unit=\"Hz\" type=\"range\" min=\"5\" max=\"200\" step=\"any\" value=\"50\"></div></div><div class=\"readouts\" id=\"metrics\"></div><svg id=\"plot\" class=\"plot\" role=\"img\" aria-label=\"Numerical response graph\" viewBox=\"0 0 670 260\"></svg>",
    init: function(card) {
      try {
        var inputs = Array.from(card.querySelectorAll('input[data-param]'));
        var result = card.querySelector('#metrics'), svg = card.querySelector('#plot');
        function update() {
          var p = {};
          for (var i = 0; i < inputs.length; i++) {
            var t = inputs[i];
            p[t.dataset.param] = Number(t.value);
            var o = card.querySelector('#value-' + t.dataset.param);
            if (o) o.textContent = t.value + ' ' + (t.dataset.unit || '');
          }
          var r = calculate(1, p);
          if (result && r.metrics) {
            result.innerHTML = r.metrics.map(function(x) {
              return '<div class="stat-box"><small>' + x[0] + '</small><output>' + format(x[1]) + ' ' + (x[2] === 'text' ? '' : x[2]) + '</output></div>';
            }).join('');
          }
          if (svg && r.points) draw(svg, r.points, r.axis, r.xlabel ? (Array.isArray(r.xlabel) ? r.xlabel[0] : r.xlabel) : 'Sweep');
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis II sim error in model 1:', err);
      }
    }
  });
  MODELS.push({
    idx: 2,
    unit: 1,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 02</span><h3>Phase Lag and Time Shift</h3><p>The same-degree phase change corresponds to a different absolute delay at different frequency.</p><p><code>Delay \u0394t=\u03c6/(360f).</code></p></div><div class=\"sim-controls\"><div class=\"control\"><label for=\"f\">Frequency <strong id=\"value-f\"></strong></label><input id=\"f\" data-param=\"f\" data-unit=\"Hz\" type=\"range\" min=\"5\" max=\"300\" step=\"any\" value=\"50\"></div><div class=\"control\"><label for=\"phi\">Lag angle <strong id=\"value-phi\"></strong></label><input id=\"phi\" data-param=\"phi\" data-unit=\"deg\" type=\"range\" min=\"0\" max=\"180\" step=\"any\" value=\"45\"></div></div><div class=\"readouts\" id=\"metrics\"></div><svg id=\"plot\" class=\"plot\" role=\"img\" aria-label=\"Numerical response graph\" viewBox=\"0 0 670 260\"></svg>",
    init: function(card) {
      try {
        var inputs = Array.from(card.querySelectorAll('input[data-param]'));
        var result = card.querySelector('#metrics'), svg = card.querySelector('#plot');
        function update() {
          var p = {};
          for (var i = 0; i < inputs.length; i++) {
            var t = inputs[i];
            p[t.dataset.param] = Number(t.value);
            var o = card.querySelector('#value-' + t.dataset.param);
            if (o) o.textContent = t.value + ' ' + (t.dataset.unit || '');
          }
          var r = calculate(2, p);
          if (result && r.metrics) {
            result.innerHTML = r.metrics.map(function(x) {
              return '<div class="stat-box"><small>' + x[0] + '</small><output>' + format(x[1]) + ' ' + (x[2] === 'text' ? '' : x[2]) + '</output></div>';
            }).join('');
          }
          if (svg && r.points) draw(svg, r.points, r.axis, r.xlabel ? (Array.isArray(r.xlabel) ? r.xlabel[1] : r.xlabel) : 'Sweep');
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis II sim error in model 2:', err);
      }
    }
  });
  MODELS.push({
    idx: 3,
    unit: 2,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 03</span><h3>Resistor-Inductor Impedance</h3><p>Inspect magnitude and phase of a series RL branch in a steady AC circuit.</p><p><code>Z=R+j2\u03c0fL.</code></p></div><div class=\"sim-controls\"><div class=\"control\"><label for=\"R\">Resistance <strong id=\"value-R\"></strong></label><input id=\"R\" data-param=\"R\" data-unit=\"\u03a9\" type=\"range\" min=\"1\" max=\"500\" step=\"any\" value=\"50\"></div><div class=\"control\"><label for=\"L\">Inductance <strong id=\"value-L\"></strong></label><input id=\"L\" data-param=\"L\" data-unit=\"mH\" type=\"range\" min=\"1\" max=\"500\" step=\"any\" value=\"100\"></div><div class=\"control\"><label for=\"f\">Frequency <strong id=\"value-f\"></strong></label><input id=\"f\" data-param=\"f\" data-unit=\"Hz\" type=\"range\" min=\"10\" max=\"5000\" step=\"any\" value=\"100\"></div></div><div class=\"readouts\" id=\"metrics\"></div><svg id=\"plot\" class=\"plot\" role=\"img\" aria-label=\"Numerical response graph\" viewBox=\"0 0 670 260\"></svg>",
    init: function(card) {
      try {
        var inputs = Array.from(card.querySelectorAll('input[data-param]'));
        var result = card.querySelector('#metrics'), svg = card.querySelector('#plot');
        function update() {
          var p = {};
          for (var i = 0; i < inputs.length; i++) {
            var t = inputs[i];
            p[t.dataset.param] = Number(t.value);
            var o = card.querySelector('#value-' + t.dataset.param);
            if (o) o.textContent = t.value + ' ' + (t.dataset.unit || '');
          }
          var r = calculate(3, p);
          if (result && r.metrics) {
            result.innerHTML = r.metrics.map(function(x) {
              return '<div class="stat-box"><small>' + x[0] + '</small><output>' + format(x[1]) + ' ' + (x[2] === 'text' ? '' : x[2]) + '</output></div>';
            }).join('');
          }
          if (svg && r.points) draw(svg, r.points, r.axis, r.xlabel ? (Array.isArray(r.xlabel) ? r.xlabel[2] : r.xlabel) : 'Sweep');
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis II sim error in model 3:', err);
      }
    }
  });
  MODELS.push({
    idx: 4,
    unit: 2,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 04</span><h3>Resistor-Capacitor Impedance</h3><p>Inspect magnitude and negative phase of series RC impedance across frequency.</p><p><code>Z=R\u2212j/(2\u03c0fC).</code></p></div><div class=\"sim-controls\"><div class=\"control\"><label for=\"R\">Resistance <strong id=\"value-R\"></strong></label><input id=\"R\" data-param=\"R\" data-unit=\"\u03a9\" type=\"range\" min=\"1\" max=\"500\" step=\"any\" value=\"100\"></div><div class=\"control\"><label for=\"C\">Capacitance <strong id=\"value-C\"></strong></label><input id=\"C\" data-param=\"C\" data-unit=\"\u03bcF\" type=\"range\" min=\"0.1\" max=\"200\" step=\"any\" value=\"10\"></div><div class=\"control\"><label for=\"f\">Frequency <strong id=\"value-f\"></strong></label><input id=\"f\" data-param=\"f\" data-unit=\"Hz\" type=\"range\" min=\"10\" max=\"2000\" step=\"any\" value=\"200\"></div></div><div class=\"readouts\" id=\"metrics\"></div><svg id=\"plot\" class=\"plot\" role=\"img\" aria-label=\"Numerical response graph\" viewBox=\"0 0 670 260\"></svg>",
    init: function(card) {
      try {
        var inputs = Array.from(card.querySelectorAll('input[data-param]'));
        var result = card.querySelector('#metrics'), svg = card.querySelector('#plot');
        function update() {
          var p = {};
          for (var i = 0; i < inputs.length; i++) {
            var t = inputs[i];
            p[t.dataset.param] = Number(t.value);
            var o = card.querySelector('#value-' + t.dataset.param);
            if (o) o.textContent = t.value + ' ' + (t.dataset.unit || '');
          }
          var r = calculate(4, p);
          if (result && r.metrics) {
            result.innerHTML = r.metrics.map(function(x) {
              return '<div class="stat-box"><small>' + x[0] + '</small><output>' + format(x[1]) + ' ' + (x[2] === 'text' ? '' : x[2]) + '</output></div>';
            }).join('');
          }
          if (svg && r.points) draw(svg, r.points, r.axis, r.xlabel ? (Array.isArray(r.xlabel) ? r.xlabel[3] : r.xlabel) : 'Sweep');
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis II sim error in model 4:', err);
      }
    }
  });
  MODELS.push({
    idx: 5,
    unit: 3,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 05</span><h3>Complex Power and Power Factor</h3><p>Compare active, reactive and apparent power for a sinusoidal load.</p><p><code>P=VI pf; Q=VI\u221a(1\u2212pf\u00b2).</code></p></div><div class=\"sim-controls\"><div class=\"control\"><label for=\"V\">RMS voltage <strong id=\"value-V\"></strong></label><input id=\"V\" data-param=\"V\" data-unit=\"V\" type=\"range\" min=\"10\" max=\"240\" step=\"any\" value=\"120\"></div><div class=\"control\"><label for=\"I\">RMS current <strong id=\"value-I\"></strong></label><input id=\"I\" data-param=\"I\" data-unit=\"A\" type=\"range\" min=\"0.1\" max=\"15\" step=\"any\" value=\"5\"></div><div class=\"control\"><label for=\"pf\">Lagging PF <strong id=\"value-pf\"></strong></label><input id=\"pf\" data-param=\"pf\" data-unit=\"unitless\" type=\"range\" min=\"0.1\" max=\"1\" step=\"0.01\" value=\"0.8\"></div></div><div class=\"readouts\" id=\"metrics\"></div><svg id=\"plot\" class=\"plot\" role=\"img\" aria-label=\"Numerical response graph\" viewBox=\"0 0 670 260\"></svg>",
    init: function(card) {
      try {
        var inputs = Array.from(card.querySelectorAll('input[data-param]'));
        var result = card.querySelector('#metrics'), svg = card.querySelector('#plot');
        function update() {
          var p = {};
          for (var i = 0; i < inputs.length; i++) {
            var t = inputs[i];
            p[t.dataset.param] = Number(t.value);
            var o = card.querySelector('#value-' + t.dataset.param);
            if (o) o.textContent = t.value + ' ' + (t.dataset.unit || '');
          }
          var r = calculate(5, p);
          if (result && r.metrics) {
            result.innerHTML = r.metrics.map(function(x) {
              return '<div class="stat-box"><small>' + x[0] + '</small><output>' + format(x[1]) + ' ' + (x[2] === 'text' ? '' : x[2]) + '</output></div>';
            }).join('');
          }
          if (svg && r.points) draw(svg, r.points, r.axis, r.xlabel ? (Array.isArray(r.xlabel) ? r.xlabel[4] : r.xlabel) : 'Sweep');
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis II sim error in model 5:', err);
      }
    }
  });
  MODELS.push({
    idx: 6,
    unit: 3,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 06</span><h3>Reactive Power Compensation</h3><p>Idealized correction of an inductive load from one lagging power factor to another.</p><p><code>Qc=P(tan acos pf\u2212tan acos target); target \u2265 original gives capacitive compensation.</code></p></div><div class=\"sim-controls\"><div class=\"control\"><label for=\"P\">Real load power <strong id=\"value-P\"></strong></label><input id=\"P\" data-param=\"P\" data-unit=\"W\" type=\"range\" min=\"100\" max=\"3000\" step=\"any\" value=\"1000\"></div><div class=\"control\"><label for=\"pf\">Original PF <strong id=\"value-pf\"></strong></label><input id=\"pf\" data-param=\"pf\" data-unit=\"unitless\" type=\"range\" min=\"0.3\" max=\"0.95\" step=\"0.01\" value=\"0.75\"></div><div class=\"control\"><label for=\"target\">Target PF <strong id=\"value-target\"></strong></label><input id=\"target\" data-param=\"target\" data-unit=\"unitless\" type=\"range\" min=\"0.75\" max=\"1\" step=\"0.01\" value=\"0.95\"></div></div><div class=\"readouts\" id=\"metrics\"></div><svg id=\"plot\" class=\"plot\" role=\"img\" aria-label=\"Numerical response graph\" viewBox=\"0 0 670 260\"></svg>",
    init: function(card) {
      try {
        var inputs = Array.from(card.querySelectorAll('input[data-param]'));
        var result = card.querySelector('#metrics'), svg = card.querySelector('#plot');
        function update() {
          var p = {};
          for (var i = 0; i < inputs.length; i++) {
            var t = inputs[i];
            p[t.dataset.param] = Number(t.value);
            var o = card.querySelector('#value-' + t.dataset.param);
            if (o) o.textContent = t.value + ' ' + (t.dataset.unit || '');
          }
          var r = calculate(6, p);
          if (result && r.metrics) {
            result.innerHTML = r.metrics.map(function(x) {
              return '<div class="stat-box"><small>' + x[0] + '</small><output>' + format(x[1]) + ' ' + (x[2] === 'text' ? '' : x[2]) + '</output></div>';
            }).join('');
          }
          if (svg && r.points) draw(svg, r.points, r.axis, r.xlabel ? (Array.isArray(r.xlabel) ? r.xlabel[5] : r.xlabel) : 'Sweep');
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis II sim error in model 6:', err);
      }
    }
  });
  MODELS.push({
    idx: 7,
    unit: 4,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 07</span><h3>Series RLC Resonance</h3><p>Explore resonance frequency and current magnitude. Losses are represented only by the ideal series R.</p><p><code>I=10/|R+j(\u03c9L\u22121/(\u03c9C))|; f0=1/(2\u03c0\u221aLC).</code></p></div><div class=\"sim-controls\"><div class=\"control\"><label for=\"R\">Series resistance <strong id=\"value-R\"></strong></label><input id=\"R\" data-param=\"R\" data-unit=\"\u03a9\" type=\"range\" min=\"1\" max=\"100\" step=\"any\" value=\"10\"></div><div class=\"control\"><label for=\"L\">Inductance <strong id=\"value-L\"></strong></label><input id=\"L\" data-param=\"L\" data-unit=\"mH\" type=\"range\" min=\"5\" max=\"150\" step=\"any\" value=\"30\"></div><div class=\"control\"><label for=\"C\">Capacitance <strong id=\"value-C\"></strong></label><input id=\"C\" data-param=\"C\" data-unit=\"\u03bcF\" type=\"range\" min=\"1\" max=\"100\" step=\"any\" value=\"20\"></div></div><div class=\"readouts\" id=\"metrics\"></div><svg id=\"plot\" class=\"plot\" role=\"img\" aria-label=\"Numerical response graph\" viewBox=\"0 0 670 260\"></svg>",
    init: function(card) {
      try {
        var inputs = Array.from(card.querySelectorAll('input[data-param]'));
        var result = card.querySelector('#metrics'), svg = card.querySelector('#plot');
        function update() {
          var p = {};
          for (var i = 0; i < inputs.length; i++) {
            var t = inputs[i];
            p[t.dataset.param] = Number(t.value);
            var o = card.querySelector('#value-' + t.dataset.param);
            if (o) o.textContent = t.value + ' ' + (t.dataset.unit || '');
          }
          var r = calculate(7, p);
          if (result && r.metrics) {
            result.innerHTML = r.metrics.map(function(x) {
              return '<div class="stat-box"><small>' + x[0] + '</small><output>' + format(x[1]) + ' ' + (x[2] === 'text' ? '' : x[2]) + '</output></div>';
            }).join('');
          }
          if (svg && r.points) draw(svg, r.points, r.axis, r.xlabel ? (Array.isArray(r.xlabel) ? r.xlabel[6] : r.xlabel) : 'Sweep');
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis II sim error in model 7:', err);
      }
    }
  });
  MODELS.push({
    idx: 8,
    unit: 4,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 08</span><h3>Balanced Three-Phase Power</h3><p>Power from line RMS quantities under balanced sinusoidal conditions.</p><p><code>P=\u221a3 VL IL pf; S=\u221a3 VL IL.</code></p></div><div class=\"sim-controls\"><div class=\"control\"><label for=\"VL\">Line voltage <strong id=\"value-VL\"></strong></label><input id=\"VL\" data-param=\"VL\" data-unit=\"V\" type=\"range\" min=\"100\" max=\"600\" step=\"any\" value=\"400\"></div><div class=\"control\"><label for=\"IL\">Line current <strong id=\"value-IL\"></strong></label><input id=\"IL\" data-param=\"IL\" data-unit=\"A\" type=\"range\" min=\"0.5\" max=\"40\" step=\"any\" value=\"10\"></div><div class=\"control\"><label for=\"pf\">Lagging PF <strong id=\"value-pf\"></strong></label><input id=\"pf\" data-param=\"pf\" data-unit=\"unitless\" type=\"range\" min=\"0.1\" max=\"1\" step=\"0.01\" value=\"0.9\"></div></div><div class=\"readouts\" id=\"metrics\"></div><svg id=\"plot\" class=\"plot\" role=\"img\" aria-label=\"Numerical response graph\" viewBox=\"0 0 670 260\"></svg>",
    init: function(card) {
      try {
        var inputs = Array.from(card.querySelectorAll('input[data-param]'));
        var result = card.querySelector('#metrics'), svg = card.querySelector('#plot');
        function update() {
          var p = {};
          for (var i = 0; i < inputs.length; i++) {
            var t = inputs[i];
            p[t.dataset.param] = Number(t.value);
            var o = card.querySelector('#value-' + t.dataset.param);
            if (o) o.textContent = t.value + ' ' + (t.dataset.unit || '');
          }
          var r = calculate(8, p);
          if (result && r.metrics) {
            result.innerHTML = r.metrics.map(function(x) {
              return '<div class="stat-box"><small>' + x[0] + '</small><output>' + format(x[1]) + ' ' + (x[2] === 'text' ? '' : x[2]) + '</output></div>';
            }).join('');
          }
          if (svg && r.points) draw(svg, r.points, r.axis, r.xlabel ? (Array.isArray(r.xlabel) ? r.xlabel[7] : r.xlabel) : 'Sweep');
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis II sim error in model 8:', err);
      }
    }
  });
  MODELS.push({
    idx: 9,
    unit: 5,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 09</span><h3>Mutual Inductance and Series Coupling</h3><p>Coupled inductors with positive passive coupling and consistent dots.</p><p><code>M=k\u221a(L1 L2); Laiding=L1+L2+2M.</code></p></div><div class=\"sim-controls\"><div class=\"control\"><label for=\"L1\">Primary inductance <strong id=\"value-L1\"></strong></label><input id=\"L1\" data-param=\"L1\" data-unit=\"mH\" type=\"range\" min=\"1\" max=\"80\" step=\"any\" value=\"20\"></div><div class=\"control\"><label for=\"L2\">Secondary inductance <strong id=\"value-L2\"></strong></label><input id=\"L2\" data-param=\"L2\" data-unit=\"mH\" type=\"range\" min=\"1\" max=\"80\" step=\"any\" value=\"45\"></div><div class=\"control\"><label for=\"k\">Coupling coefficient <strong id=\"value-k\"></strong></label><input id=\"k\" data-param=\"k\" data-unit=\"unitless\" type=\"range\" min=\"0\" max=\"0.99\" step=\"0.01\" value=\"0.65\"></div></div><div class=\"readouts\" id=\"metrics\"></div><svg id=\"plot\" class=\"plot\" role=\"img\" aria-label=\"Numerical response graph\" viewBox=\"0 0 670 260\"></svg>",
    init: function(card) {
      try {
        var inputs = Array.from(card.querySelectorAll('input[data-param]'));
        var result = card.querySelector('#metrics'), svg = card.querySelector('#plot');
        function update() {
          var p = {};
          for (var i = 0; i < inputs.length; i++) {
            var t = inputs[i];
            p[t.dataset.param] = Number(t.value);
            var o = card.querySelector('#value-' + t.dataset.param);
            if (o) o.textContent = t.value + ' ' + (t.dataset.unit || '');
          }
          var r = calculate(9, p);
          if (result && r.metrics) {
            result.innerHTML = r.metrics.map(function(x) {
              return '<div class="stat-box"><small>' + x[0] + '</small><output>' + format(x[1]) + ' ' + (x[2] === 'text' ? '' : x[2]) + '</output></div>';
            }).join('');
          }
          if (svg && r.points) draw(svg, r.points, r.axis, r.xlabel ? (Array.isArray(r.xlabel) ? r.xlabel[8] : r.xlabel) : 'Sweep');
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis II sim error in model 9:', err);
      }
    }
  });
  MODELS.push({
    idx: 10,
    unit: 5,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 10</span><h3>Ideal Transformer Load Reflection</h3><p>An ideal transformer maps voltage and impedance by turns ratio.</p><p><code>Vs=Vp/ratio; Zin=ratio\u00b2RL; no losses.</code></p></div><div class=\"sim-controls\"><div class=\"control\"><label for=\"ratio\">Np/Ns ratio <strong id=\"value-ratio\"></strong></label><input id=\"ratio\" data-param=\"ratio\" data-unit=\"unitless\" type=\"range\" min=\"1\" max=\"20\" step=\"any\" value=\"10\"></div><div class=\"control\"><label for=\"Vp\">Primary RMS <strong id=\"value-Vp\"></strong></label><input id=\"Vp\" data-param=\"Vp\" data-unit=\"V\" type=\"range\" min=\"5\" max=\"240\" step=\"any\" value=\"120\"></div><div class=\"control\"><label for=\"RL\">Secondary load <strong id=\"value-RL\"></strong></label><input id=\"RL\" data-param=\"RL\" data-unit=\"\u03a9\" type=\"range\" min=\"1\" max=\"100\" step=\"any\" value=\"12\"></div></div><div class=\"readouts\" id=\"metrics\"></div><svg id=\"plot\" class=\"plot\" role=\"img\" aria-label=\"Numerical response graph\" viewBox=\"0 0 670 260\"></svg>",
    init: function(card) {
      try {
        var inputs = Array.from(card.querySelectorAll('input[data-param]'));
        var result = card.querySelector('#metrics'), svg = card.querySelector('#plot');
        function update() {
          var p = {};
          for (var i = 0; i < inputs.length; i++) {
            var t = inputs[i];
            p[t.dataset.param] = Number(t.value);
            var o = card.querySelector('#value-' + t.dataset.param);
            if (o) o.textContent = t.value + ' ' + (t.dataset.unit || '');
          }
          var r = calculate(10, p);
          if (result && r.metrics) {
            result.innerHTML = r.metrics.map(function(x) {
              return '<div class="stat-box"><small>' + x[0] + '</small><output>' + format(x[1]) + ' ' + (x[2] === 'text' ? '' : x[2]) + '</output></div>';
            }).join('');
          }
          if (svg && r.points) draw(svg, r.points, r.axis, r.xlabel ? (Array.isArray(r.xlabel) ? r.xlabel[9] : r.xlabel) : 'Sweep');
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis II sim error in model 10:', err);
      }
    }
  });
  MODELS.push({
    idx: 11,
    unit: 6,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 11</span><h3>RC Step-Response Laboratory</h3><p>Initial capacitor voltage 0; an ideal DC step drives an RC series network.</p><p><code>Vc(t)=V[1\u2212exp(\u2212t/(RC))].</code></p></div><div class=\"sim-controls\"><div class=\"control\"><label for=\"R\">Resistance <strong id=\"value-R\"></strong></label><input id=\"R\" data-param=\"R\" data-unit=\"k\u03a9\" type=\"range\" min=\"0.1\" max=\"20\" step=\"any\" value=\"1\"></div><div class=\"control\"><label for=\"C\">Capacitance <strong id=\"value-C\"></strong></label><input id=\"C\" data-param=\"C\" data-unit=\"\u03bcF\" type=\"range\" min=\"0.1\" max=\"200\" step=\"any\" value=\"10\"></div><div class=\"control\"><label for=\"V\">Step level <strong id=\"value-V\"></strong></label><input id=\"V\" data-param=\"V\" data-unit=\"V\" type=\"range\" min=\"1\" max=\"24\" step=\"any\" value=\"5\"></div></div><div class=\"readouts\" id=\"metrics\"></div><svg id=\"plot\" class=\"plot\" role=\"img\" aria-label=\"Numerical response graph\" viewBox=\"0 0 670 260\"></svg>",
    init: function(card) {
      try {
        var inputs = Array.from(card.querySelectorAll('input[data-param]'));
        var result = card.querySelector('#metrics'), svg = card.querySelector('#plot');
        function update() {
          var p = {};
          for (var i = 0; i < inputs.length; i++) {
            var t = inputs[i];
            p[t.dataset.param] = Number(t.value);
            var o = card.querySelector('#value-' + t.dataset.param);
            if (o) o.textContent = t.value + ' ' + (t.dataset.unit || '');
          }
          var r = calculate(11, p);
          if (result && r.metrics) {
            result.innerHTML = r.metrics.map(function(x) {
              return '<div class="stat-box"><small>' + x[0] + '</small><output>' + format(x[1]) + ' ' + (x[2] === 'text' ? '' : x[2]) + '</output></div>';
            }).join('');
          }
          if (svg && r.points) draw(svg, r.points, r.axis, r.xlabel ? (Array.isArray(r.xlabel) ? r.xlabel[10] : r.xlabel) : 'Sweep');
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis II sim error in model 11:', err);
      }
    }
  });
  MODELS.push({
    idx: 12,
    unit: 6,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 12</span><h3>Series RLC Damping</h3><p>Compute natural frequency and damping ratio of a series RLC system.</p><p><code>\u03c90=1/\u221aLC; \u03b6=(R/2)\u221a(C/L).</code></p></div><div class=\"sim-controls\"><div class=\"control\"><label for=\"R\">Resistance <strong id=\"value-R\"></strong></label><input id=\"R\" data-param=\"R\" data-unit=\"\u03a9\" type=\"range\" min=\"0.1\" max=\"300\" step=\"any\" value=\"30\"></div><div class=\"control\"><label for=\"L\">Inductance <strong id=\"value-L\"></strong></label><input id=\"L\" data-param=\"L\" data-unit=\"mH\" type=\"range\" min=\"1\" max=\"200\" step=\"any\" value=\"30\"></div><div class=\"control\"><label for=\"C\">Capacitance <strong id=\"value-C\"></strong></label><input id=\"C\" data-param=\"C\" data-unit=\"\u03bcF\" type=\"range\" min=\"1\" max=\"200\" step=\"any\" value=\"50\"></div></div><div class=\"readouts\" id=\"metrics\"></div><svg id=\"plot\" class=\"plot\" role=\"img\" aria-label=\"Numerical response graph\" viewBox=\"0 0 670 260\"></svg>",
    init: function(card) {
      try {
        var inputs = Array.from(card.querySelectorAll('input[data-param]'));
        var result = card.querySelector('#metrics'), svg = card.querySelector('#plot');
        function update() {
          var p = {};
          for (var i = 0; i < inputs.length; i++) {
            var t = inputs[i];
            p[t.dataset.param] = Number(t.value);
            var o = card.querySelector('#value-' + t.dataset.param);
            if (o) o.textContent = t.value + ' ' + (t.dataset.unit || '');
          }
          var r = calculate(12, p);
          if (result && r.metrics) {
            result.innerHTML = r.metrics.map(function(x) {
              return '<div class="stat-box"><small>' + x[0] + '</small><output>' + format(x[1]) + ' ' + (x[2] === 'text' ? '' : x[2]) + '</output></div>';
            }).join('');
          }
          if (svg && r.points) draw(svg, r.points, r.axis, r.xlabel ? (Array.isArray(r.xlabel) ? r.xlabel[11] : r.xlabel) : 'Sweep');
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis II sim error in model 12:', err);
      }
    }
  });
  MODELS.push({
    idx: 13,
    unit: 7,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 13</span><h3>RC Low-Pass Magnitude</h3><p>Unloaded output across capacitor in an ideal RC network.</p><p><code>|H|=1/\u221a(1+(2\u03c0fRC)\u00b2).</code></p></div><div class=\"sim-controls\"><div class=\"control\"><label for=\"R\">Resistance <strong id=\"value-R\"></strong></label><input id=\"R\" data-param=\"R\" data-unit=\"k\u03a9\" type=\"range\" min=\"0.1\" max=\"20\" step=\"any\" value=\"10\"></div><div class=\"control\"><label for=\"C\">Capacitance <strong id=\"value-C\"></strong></label><input id=\"C\" data-param=\"C\" data-unit=\"nF\" type=\"range\" min=\"1\" max=\"500\" step=\"any\" value=\"10\"></div><div class=\"control\"><label for=\"f\">Frequency <strong id=\"value-f\"></strong></label><input id=\"f\" data-param=\"f\" data-unit=\"Hz\" type=\"range\" min=\"10\" max=\"50000\" step=\"any\" value=\"1600\"></div></div><div class=\"readouts\" id=\"metrics\"></div><svg id=\"plot\" class=\"plot\" role=\"img\" aria-label=\"Numerical response graph\" viewBox=\"0 0 670 260\"></svg>",
    init: function(card) {
      try {
        var inputs = Array.from(card.querySelectorAll('input[data-param]'));
        var result = card.querySelector('#metrics'), svg = card.querySelector('#plot');
        function update() {
          var p = {};
          for (var i = 0; i < inputs.length; i++) {
            var t = inputs[i];
            p[t.dataset.param] = Number(t.value);
            var o = card.querySelector('#value-' + t.dataset.param);
            if (o) o.textContent = t.value + ' ' + (t.dataset.unit || '');
          }
          var r = calculate(13, p);
          if (result && r.metrics) {
            result.innerHTML = r.metrics.map(function(x) {
              return '<div class="stat-box"><small>' + x[0] + '</small><output>' + format(x[1]) + ' ' + (x[2] === 'text' ? '' : x[2]) + '</output></div>';
            }).join('');
          }
          if (svg && r.points) draw(svg, r.points, r.axis, r.xlabel ? (Array.isArray(r.xlabel) ? r.xlabel[12] : r.xlabel) : 'Sweep');
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis II sim error in model 13:', err);
      }
    }
  });
  MODELS.push({
    idx: 14,
    unit: 7,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 14</span><h3>RC High-Pass Magnitude</h3><p>Unloaded output across resistor in an ideal RC high-pass.</p><p><code>|H|=x/\u221a(1+x\u00b2), x=2\u03c0fRC.</code></p></div><div class=\"sim-controls\"><div class=\"control\"><label for=\"R\">Resistance <strong id=\"value-R\"></strong></label><input id=\"R\" data-param=\"R\" data-unit=\"k\u03a9\" type=\"range\" min=\"0.1\" max=\"20\" step=\"any\" value=\"10\"></div><div class=\"control\"><label for=\"C\">Capacitance <strong id=\"value-C\"></strong></label><input id=\"C\" data-param=\"C\" data-unit=\"nF\" type=\"range\" min=\"1\" max=\"500\" step=\"any\" value=\"10\"></div><div class=\"control\"><label for=\"f\">Frequency <strong id=\"value-f\"></strong></label><input id=\"f\" data-param=\"f\" data-unit=\"Hz\" type=\"range\" min=\"10\" max=\"50000\" step=\"any\" value=\"1600\"></div></div><div class=\"readouts\" id=\"metrics\"></div><svg id=\"plot\" class=\"plot\" role=\"img\" aria-label=\"Numerical response graph\" viewBox=\"0 0 670 260\"></svg>",
    init: function(card) {
      try {
        var inputs = Array.from(card.querySelectorAll('input[data-param]'));
        var result = card.querySelector('#metrics'), svg = card.querySelector('#plot');
        function update() {
          var p = {};
          for (var i = 0; i < inputs.length; i++) {
            var t = inputs[i];
            p[t.dataset.param] = Number(t.value);
            var o = card.querySelector('#value-' + t.dataset.param);
            if (o) o.textContent = t.value + ' ' + (t.dataset.unit || '');
          }
          var r = calculate(14, p);
          if (result && r.metrics) {
            result.innerHTML = r.metrics.map(function(x) {
              return '<div class="stat-box"><small>' + x[0] + '</small><output>' + format(x[1]) + ' ' + (x[2] === 'text' ? '' : x[2]) + '</output></div>';
            }).join('');
          }
          if (svg && r.points) draw(svg, r.points, r.axis, r.xlabel ? (Array.isArray(r.xlabel) ? r.xlabel[13] : r.xlabel) : 'Sweep');
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis II sim error in model 14:', err);
      }
    }
  });
  MODELS.push({
    idx: 15,
    unit: 8,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 15</span><h3>Square-Wave Fourier Harmonics</h3><p>First harmonics of an ideal \u00b1A symmetric square wave; sine coefficients for the chosen origin.</p><p><code>An=4A/(\u03c0 n) for odd n; zero for even n.</code></p></div><div class=\"sim-controls\"><div class=\"control\"><label for=\"A\">Square-wave amplitude <strong id=\"value-A\"></strong></label><input id=\"A\" data-param=\"A\" data-unit=\"V\" type=\"range\" min=\"0.5\" max=\"12\" step=\"any\" value=\"4\"></div><div class=\"control\"><label for=\"n\">Harmonic index <strong id=\"value-n\"></strong></label><input id=\"n\" data-param=\"n\" data-unit=\"integer\" type=\"range\" min=\"1\" max=\"21\" step=\"1\" value=\"3\"></div></div><div class=\"readouts\" id=\"metrics\"></div><svg id=\"plot\" class=\"plot\" role=\"img\" aria-label=\"Numerical response graph\" viewBox=\"0 0 670 260\"></svg>",
    init: function(card) {
      try {
        var inputs = Array.from(card.querySelectorAll('input[data-param]'));
        var result = card.querySelector('#metrics'), svg = card.querySelector('#plot');
        function update() {
          var p = {};
          for (var i = 0; i < inputs.length; i++) {
            var t = inputs[i];
            p[t.dataset.param] = Number(t.value);
            var o = card.querySelector('#value-' + t.dataset.param);
            if (o) o.textContent = t.value + ' ' + (t.dataset.unit || '');
          }
          var r = calculate(15, p);
          if (result && r.metrics) {
            result.innerHTML = r.metrics.map(function(x) {
              return '<div class="stat-box"><small>' + x[0] + '</small><output>' + format(x[1]) + ' ' + (x[2] === 'text' ? '' : x[2]) + '</output></div>';
            }).join('');
          }
          if (svg && r.points) draw(svg, r.points, r.axis, r.xlabel ? (Array.isArray(r.xlabel) ? r.xlabel[14] : r.xlabel) : 'Sweep');
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis II sim error in model 15:', err);
      }
    }
  });
  MODELS.push({
    idx: 16,
    unit: 8,
    html: "<div class=\"sim-header\"><span class=\"badge\">Model 16</span><h3>Sampling and Aliasing</h3><p>An ideal tone sampled uniformly without an analog anti-alias filter.</p><p><code>Alias=|((fin+fs/2) mod fs)\u2212fs/2|.</code></p></div><div class=\"sim-controls\"><div class=\"control\"><label for=\"fs\">Sample rate <strong id=\"value-fs\"></strong></label><input id=\"fs\" data-param=\"fs\" data-unit=\"Hz\" type=\"range\" min=\"100\" max=\"6000\" step=\"any\" value=\"1000\"></div><div class=\"control\"><label for=\"fin\">Input tone <strong id=\"value-fin\"></strong></label><input id=\"fin\" data-param=\"fin\" data-unit=\"Hz\" type=\"range\" min=\"1\" max=\"8000\" step=\"any\" value=\"700\"></div></div><div class=\"readouts\" id=\"metrics\"></div><svg id=\"plot\" class=\"plot\" role=\"img\" aria-label=\"Numerical response graph\" viewBox=\"0 0 670 260\"></svg>",
    init: function(card) {
      try {
        var inputs = Array.from(card.querySelectorAll('input[data-param]'));
        var result = card.querySelector('#metrics'), svg = card.querySelector('#plot');
        function update() {
          var p = {};
          for (var i = 0; i < inputs.length; i++) {
            var t = inputs[i];
            p[t.dataset.param] = Number(t.value);
            var o = card.querySelector('#value-' + t.dataset.param);
            if (o) o.textContent = t.value + ' ' + (t.dataset.unit || '');
          }
          var r = calculate(16, p);
          if (result && r.metrics) {
            result.innerHTML = r.metrics.map(function(x) {
              return '<div class="stat-box"><small>' + x[0] + '</small><output>' + format(x[1]) + ' ' + (x[2] === 'text' ? '' : x[2]) + '</output></div>';
            }).join('');
          }
          if (svg && r.points) draw(svg, r.points, r.axis, r.xlabel ? (Array.isArray(r.xlabel) ? r.xlabel[15] : r.xlabel) : 'Sweep');
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Circuit Analysis II sim error in model 16:', err);
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
