/* Signals and Systems Interactive Simulation Suite */
(function(window) {
  'use strict';
"use strict";
const TAU=2*Math.PI;
const configs=[{"title": "Continuous sampling and aliasing", "description": "Sweep a tone between 0 and 1.5 times the sample rate. Samples alone cannot identify which analog band generated the observed alias.", "parameterLabel": "Frequency multiple of sampling rate", "min": 0.05, "max": 1.5, "step": 0.01, "default": 0.72}, {"title": "Linearity and superposition", "description": "Compare output from combined inputs against the sum of separate outputs for a linear gain model.", "parameterLabel": "Scale of second input", "min": 0.1, "max": 3, "step": 0.05, "default": 1}, {"title": "Time-shift and scaling", "description": "A Gaussian pulse is delayed and compressed; its onset and width move with time-coordinate transformations.", "parameterLabel": "Pulse delay (s)", "min": -2, "max": 2, "step": 0.05, "default": 0.4}, {"title": "Rectangular-pulse convolution", "description": "Convolution overlap creates a triangular or trapezoidal output depending on pulse widths.", "parameterLabel": "Second-pulse width (s)", "min": 0.2, "max": 3, "step": 0.05, "default": 1.5}, {"title": "First-order impulse and step response", "description": "Compare a normalized one-pole impulse response with its integrated step response.", "parameterLabel": "Time constant (s)", "min": 0.1, "max": 2, "step": 0.05, "default": 0.6}, {"title": "Moving-average response", "description": "The mean of the last M samples attenuates rapid variations and delays narrow peaks.", "parameterLabel": "Window length (samples)", "min": 2, "max": 20, "step": 1, "default": 6}, {"title": "Harmonic Fourier synthesis", "description": "Odd harmonics approximate a bipolar square wave; finite sums exhibit edge overshoot.", "parameterLabel": "Number of odd harmonics", "min": 1, "max": 31, "step": 1, "default": 7}, {"title": "Spectral leakage and DFT window", "description": "A finite record with a noncoherent frequency leaks across bins; the displayed graph shows DFT magnitudes.", "parameterLabel": "Tone frequency (cycles / record)", "min": 2, "max": 13, "step": 0.1, "default": 5.4}, {"title": "Sampling frequency folding", "description": "A high-frequency sine sampled at a lower clock rate produces a folded discrete sequence.", "parameterLabel": "Tone frequency (Hz)", "min": 50, "max": 1400, "step": 10, "default": 720}, {"title": "Laplace pole and exponential mode", "description": "A single stable real pole produces exponentially decaying impulse response.", "parameterLabel": "Pole magnitude (s⁻¹)", "min": 0.2, "max": 8, "step": 0.1, "default": 3}, {"title": "One-pole continuous Bode magnitude", "description": "The magnitude of a first-order low-pass approaches unity at DC and rolls off beyond cutoff.", "parameterLabel": "Cutoff frequency (Hz)", "min": 10, "max": 400, "step": 10, "default": 100}, {"title": "Discrete one-pole IIR step", "description": "Vary feedback pole a; the unit-DC-gain one-pole filter becomes slower as a approaches one.", "parameterLabel": "Feedback pole a", "min": 0.05, "max": 0.98, "step": 0.01, "default": 0.75}, {"title": "FIR two-tap frequency response", "description": "Two-tap smoothing suppresses high normalized frequencies with a cosine-shaped response.", "parameterLabel": "Tap weight a", "min": 0, "max": 1, "step": 0.02, "default": 0.5}, {"title": "Amplitude-modulation sidebands", "description": "Multiplying a message and a carrier creates symmetric upper and lower sidebands.", "parameterLabel": "Message frequency (Hz)", "min": 20, "max": 300, "step": 10, "default": 100}, {"title": "Cross-correlation lag", "description": "A delayed pulse gives a cross-correlation maximum at the appropriate lag with a stated sign convention.", "parameterLabel": "Integer lag (samples)", "min": -16, "max": 16, "step": 1, "default": 4}, {"title": "Uniform quantization error", "description": "Rounding to a fixed number of levels produces granular error and clipping when input exceeds range.", "parameterLabel": "Quantization bits", "min": 2, "max": 12, "step": 1, "default": 5}];
function clamp(x,a,b){return Math.max(a,Math.min(b,x));}
function fftMag(arr){const N=arr.length;let out=[];for(let k=0;k<N/2;k++){let re=0,im=0;for(let n=0;n<N;n++){const th=-TAU*k*n/N;re+=arr[n]*Math.cos(th);im+=arr[n]*Math.sin(th);}out.push(Math.hypot(re,im)*2/N);}return out;}
function evaluate(id,p){let x=[],y=[],secondary=[],summary=''; const N=240;
 for(let i=0;i<N;i++)x.push(i/(N-1));
 switch(id){
 case 1: {const alias=Math.abs(((p+.5)%1+1)%1-.5);y=x.map(t=>Math.sin(TAU*p*t*18));secondary=x.map(t=>Math.sin(TAU*alias*t*18));summary=`Analog f/fs=${p.toFixed(2)}; folded f/fs=${alias.toFixed(3)}. Lines compare ideal analog (navy) and alias-frequency curve (teal).`;break;}
 case 2: {const a=.7,b=p;y=x.map(t=>a*Math.sin(TAU*3*t)+b*Math.cos(TAU*5*t));secondary=x.map(t=>a*Math.sin(TAU*3*t)+b*Math.cos(TAU*5*t));summary=`For the linear identity system S[x1+${b.toFixed(2)}x2]=S[x1]+${b.toFixed(2)}S[x2]; curves coincide.`;break;}
 case 3: {const d=p;y=x.map(t=>Math.exp(-Math.pow((8*t-4-d)*2,2)));secondary=x.map(t=>Math.exp(-Math.pow(8*t-4,2)));summary=`Pulse center shift ${d.toFixed(2)} s in displayed coordinates; secondary is the unshifted reference.`;break;}
 case 4: {const w=p;y=x.map(t=>Math.max(0,Math.min(1,3*t)-Math.max(0,3*t-w)));summary=`Unit-height pulses of widths 1 and ${w.toFixed(2)} s: convolution equals overlap length.`;break;}
 case 5: {const tau=p;y=x.map(t=>1-Math.exp(-3*t/tau));secondary=x.map(t=>Math.exp(-3*t/tau)/tau);summary=`Normalized step 1−exp(−t/τ), impulse exp(−t/τ)/τ; plotted over t=0…3 s.`;break;}
 case 6: {let m=Math.round(p);let inp=x.map(t=>Math.sin(TAU*8*t)+.5*Math.sin(TAU*36*t));y=inp.map((_,i)=>{let sum=0;for(let k=0;k<m;k++)sum+=i-k>=0?inp[i-k]:0;return sum/m;});secondary=inp;summary=`M=${m} samples. Blue is moving-average output; teal is original two-tone input.`;break;}
 case 7: {let h=Math.round(p);y=x.map(t=>{let v=0;for(let k=1;k<=h;k++)v+=4/(Math.PI*(2*k-1))*Math.sin(TAU*(2*k-1)*t);return v;});secondary=x.map(t=>Math.sin(TAU*t)>=0?1:-1);summary=`${h} odd harmonics of a bipolar square wave, fundamental one cycle/window.`;break;}
 case 8: {const M=64;let inp=Array.from({length:M},(_,i)=>Math.cos(TAU*p*i/M));let H=fftMag(inp);x=H.map((_,i)=>i);y=H;summary=`N=64 rectangular-window DFT magnitude; tone lies at ${p.toFixed(2)} cycles/record. Bin spacing is 1 cycle/record.`;break;}
 case 9: {const fs=1000,f=p,fold=Math.abs(((f+fs/2)%fs+fs)%fs-fs/2);x=Array.from({length:80},(_,i)=>i);y=x.map(i=>Math.sin(TAU*f*i/fs));secondary=x.map(i=>Math.sin(TAU*fold*i/fs));summary=`Input ${f.toFixed(0)} Hz at 1000 samples/s folds to ${fold.toFixed(0)} Hz; sign/phase can differ.`;break;}
 case 10: {x=x.map(t=>3*t);y=x.map(t=>Math.exp(-p*t));summary=`h(t)=e^(−${p.toFixed(2)}t)u(t); causal stable pole s=−${p.toFixed(2)} s⁻¹.`;break;}
 case 11: {x=x.map(t=>1+3*t);y=x.map(logf=>1/Math.sqrt(1+(Math.pow(10,logf)/p)**2));summary=`|H(j2πf)|=1/√(1+(f/fc)²), fc=${p.toFixed(0)} Hz; horizontal axis is log10(f/Hz), 10–10,000 Hz.`;break;}
 case 12: {x=x.map((t,i)=>i);y=x.map(n=>1-Math.pow(p,n+1));summary=`y[n]=${p.toFixed(2)}y[n−1]+${(1-p).toFixed(2)}x[n] for a unit step; y[−1]=0.`;break;}
 case 13: {x=x.map(t=>Math.PI*t);y=x.map(w=>Math.hypot(p+(1-p)*Math.cos(w),(1-p)*Math.sin(w)));summary=`H(e^jω)=a+(1−a)e^(−jω), a=${p.toFixed(2)}; x-axis 0…π rad/sample.`;break;}
 case 14: {x=x.map(t=>.02*t);y=x.map(t=>Math.cos(TAU*p*t)*Math.cos(TAU*1000*t));secondary=x.map(t=>Math.cos(TAU*p*t));summary=`DSB-SC tone: carrier 1000 Hz, message ${p.toFixed(0)} Hz, sidebands ${1000-p} and ${1000+p} Hz.`;break;}
 case 15: {const lag=Math.round(p),base=Array.from({length:100},(_,i)=>Math.exp(-Math.pow((i-45)/9,2))); x=Array.from({length:61},(_,i)=>i-30);y=x.map(k=>{let c=0;for(let i=0;i<100;i++){const j=i+k-lag;if(j>=0&&j<100)c+=base[i]*base[j];}return c;});summary=`For y[n]=x[n−${lag}], Rxy[k]=Σ x[n]y[n+k] is maximal near k=${lag}.`;break;}
 case 16: {const bits=Math.round(p),q=2/(2**bits);x=x.map(t=>TAU*3*t);secondary=x.map(t=>.8*Math.sin(t));y=secondary.map(v=>clamp(Math.round((v+1)/q)*q-1,-1,1));const rmse=Math.sqrt(y.reduce((s,v,i)=>s+(v-secondary[i])**2,0)/y.length);summary=`${bits}-bit signed span [−1,+1], step ${q.toPrecision(3)}, observed RMS error ${rmse.toPrecision(4)}.`;break;}
 default:throw new Error('unknown model');
 }
 return {x,y,secondary,summary};
}
function draw(canvas,data){const ctx=canvas.getContext('2d');const w=canvas.width=880,h=canvas.height=330;ctx.clearRect(0,0,w,h);ctx.fillStyle='#fff';ctx.fillRect(0,0,w,h);
 const pad={l:65,r:25,t:25,b:48};let ys=data.y.concat(data.secondary);let lo=Math.min(...ys,0),hi=Math.max(...ys,0); if(hi===lo){hi=lo+1;}let wig=(hi-lo)*.08;lo-=wig;hi+=wig;
 let xmin=Math.min(...data.x),xmax=Math.max(...data.x);if(xmax===xmin)xmax=xmin+1;
 let X=x=>pad.l+(x-xmin)/(xmax-xmin)*(w-pad.l-pad.r), Y=v=>h-pad.b-(v-lo)/(hi-lo)*(h-pad.t-pad.b);
 ctx.strokeStyle='#e0ebea';ctx.lineWidth=1;ctx.font='12px system-ui';ctx.fillStyle='#57707a';
 for(let n=0;n<=4;n++){let yy=pad.t+n*(h-pad.t-pad.b)/4;ctx.beginPath();ctx.moveTo(pad.l,yy);ctx.lineTo(w-pad.r,yy);ctx.stroke();ctx.fillText((hi-n*(hi-lo)/4).toPrecision(3),6,yy+4);}
 for(let n=0;n<=5;n++){let xx=pad.l+n*(w-pad.l-pad.r)/5;ctx.beginPath();ctx.moveTo(xx,pad.t);ctx.lineTo(xx,h-pad.b);ctx.stroke();ctx.fillText((xmin+n*(xmax-xmin)/5).toPrecision(3),xx-12,h-20);}
 const line=(a,color)=>{if(!a.length)return;ctx.beginPath();ctx.lineWidth=2.2;ctx.strokeStyle=color;for(let i=0;i<a.length;i++) i?ctx.lineTo(X(data.x[i]),Y(a[i])):ctx.moveTo(X(data.x[i]),Y(a[i]));ctx.stroke();};
 line(data.secondary,'#079697');line(data.y,'#174d75');
 ctx.fillStyle='#174d75';ctx.fillRect(w-195,12,14,3);ctx.fillText('Result',w-173,18);if(data.secondary.length){ctx.fillStyle='#079697';ctx.fillRect(w-102,12,14,3);ctx.fillText('Reference',w-80,18);}
}
function init(){const host=document.getElementById('model');if(!host)return;const id=Number(host.dataset.id),c=configs[id-1];const slider=document.getElementById('param'),value=document.getElementById('current'),output=document.getElementById('status'),canvas=document.getElementById('plot');
 slider.min=c.min;slider.max=c.max;slider.step=c.step;slider.value=c.default;
 const update=()=>{const p=Number(slider.value);value.textContent=String(p);try{const result=evaluate(id,p);draw(canvas,result);output.textContent=result.summary;}catch(err){output.textContent='Model error: '+err.message;}};
 slider.addEventListener('input',update);update();}



  var MODELS = [];
  for (var i = 1; i <= 16; i++) {
    (function(idx) {
      var cfg = configs[idx - 1];
      var unit = Math.floor((idx - 1) / 2) + 1;
      var html = '<div class="sim-header"><span class="badge">Model ' + (idx < 10 ? '0' : '') + idx + '</span><h3>' + cfg.title + '</h3><p>' + cfg.description + '</p></div>' +
        '<div class="sim-controls"><label for="param-' + idx + '">' + cfg.parameterLabel + ': <output id="current-' + idx + '"></output></label>' +
        '<input id="param-' + idx + '" type="range" min="' + cfg.min + '" max="' + cfg.max + '" step="' + cfg.step + '" value="' + cfg.default + '"/></div>' +
        '<div class="plot"><canvas id="plot-' + idx + '" width="680" height="260" role="img" aria-label="Signal response plot"></canvas></div>' +
        '<div class="stat-box" id="status-' + idx + '" aria-live="polite"></div>';
      
      MODELS.push({
        idx: idx,
        unit: unit,
        html: html,
        init: function(card) {
          try {
            var slider = card.querySelector('#param-' + idx);
            var value = card.querySelector('#current-' + idx);
            var output = card.querySelector('#status-' + idx);
            var canvas = card.querySelector('#plot-' + idx);
            function update() {
              var p = Number(slider.value);
              if (value) value.textContent = String(p);
              try {
                var result = evaluate(idx, p);
                draw(canvas, result);
                if (output) output.textContent = result.summary;
              } catch (err) {
                if (output) output.textContent = 'Model error: ' + err.message;
              }
            }
            slider.addEventListener('input', update);
            update();
          } catch (err) {
            console.warn('Signals and Systems sim error in model ' + idx + ':', err);
          }
        }
      });
    })(i);
  }

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
