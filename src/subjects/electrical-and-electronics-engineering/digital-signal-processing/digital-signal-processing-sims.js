/* Digital Signal Processing Interactive Simulation Suite */
(function(window) {
  'use strict';

  "use strict";
const TAU=2*Math.PI;
const configs=[{"title": "Aliasing frequency fold", "description": "The apparent discrete frequency is the distance to the nearest integer multiple of fs.", "parameterLabel": "Analog frequency (Hz)", "min": 0, "max": 9500, "step": 50, "default": 6100}, {"title": "ADC quantization and step size", "description": "Quantize an ideal sine to finite signed full-scale levels; compare with the unquantized trace.", "parameterLabel": "ADC bits", "min": 2, "max": 12, "step": 1, "default": 5}, {"title": "FIR impulse and step response", "description": "A normalized moving average of M samples rises in M steps and has a finite impulse response.", "parameterLabel": "Averaging taps", "min": 2, "max": 24, "step": 1, "default": 8}, {"title": "DFT coherent versus noncoherent tones", "description": "The rectangular-window finite DFT spreads energy across bins for a tone off its coherent grid.", "parameterLabel": "Cycles per 64 samples", "min": 2, "max": 18, "step": 0.1, "default": 5.35}, {"title": "Hann-window leakage comparison", "description": "A Hann taper reduces distant sidelobes at the expense of a wider main lobe.", "parameterLabel": "Cycles per record", "min": 2, "max": 14, "step": 0.1, "default": 6.3}, {"title": "FFT arithmetic growth", "description": "Compare the scaling indicators N² and N log2 N; these are not implementation timings.", "parameterLabel": "FFT exponent log2(N)", "min": 5, "max": 13, "step": 1, "default": 10}, {"title": "Moving-average magnitude response", "description": "A boxcar filter has periodic frequency-response nulls depending on M.", "parameterLabel": "Averaging length M", "min": 2, "max": 30, "step": 1, "default": 10}, {"title": "Windowed-sinc FIR low-pass", "description": "Vary cutoff of a 41-tap symmetric Hann-windowed low-pass; response is numerically evaluated.", "parameterLabel": "Normalized cutoff fc/fs", "min": 0.03, "max": 0.42, "step": 0.01, "default": 0.16}, {"title": "Symmetric FIR linear-phase delay", "description": "The ideal symmetric impulse response has group delay (M−1)/2 samples.", "parameterLabel": "Odd number of taps", "min": 3, "max": 41, "step": 2, "default": 15}, {"title": "One-pole IIR step transient", "description": "y[n]=a y[n−1]+(1−a)u[n] with zero initial state.", "parameterLabel": "Pole a", "min": 0.05, "max": 0.98, "step": 0.01, "default": 0.8}, {"title": "Second-order resonance radius", "description": "A damped discrete sinusoid r^n cos(ω0n) decays faster for smaller pole radius.", "parameterLabel": "Pole radius", "min": 0.5, "max": 0.995, "step": 0.005, "default": 0.92}, {"title": "Fixed-point coefficient error", "description": "Quantize a one-pole feedback coefficient; plot the difference from its ideal step output.", "parameterLabel": "Fractional precision (bits)", "min": 3, "max": 15, "step": 1, "default": 7}, {"title": "Statistical noise reduction", "description": "A causal moving average smooths deterministic seeded white-noise observations at a cost in delay.", "parameterLabel": "Moving average M", "min": 1, "max": 30, "step": 1, "default": 8}, {"title": "LMS one-tap convergence", "description": "Adapt w to a noiseless desired gain of 0.7 using a single constant excitation x=1.", "parameterLabel": "LMS step size μ", "min": 0.01, "max": 1.9, "step": 0.01, "default": 0.25}, {"title": "Decimation alias illustration", "description": "Show folding of a high-rate sinusoid after keeping every Mth sample without an anti-alias filter.", "parameterLabel": "Decimation factor", "min": 2, "max": 10, "step": 1, "default": 4}, {"title": "Welch spectral averaging", "description": "Average deterministic seeded periodograms with varying segment count; the plotted estimator becomes smoother.", "parameterLabel": "Average segments", "min": 1, "max": 12, "step": 1, "default": 4}];
function clamp(x,a,b){return Math.max(a,Math.min(b,x));}
function fftMag(arr){const N=arr.length;let out=[];for(let k=0;k<N/2;k++){let re=0,im=0;for(let n=0;n<N;n++){const th=-TAU*k*n/N;re+=arr[n]*Math.cos(th);im+=arr[n]*Math.sin(th);}out.push(Math.hypot(re,im)*2/N);}return out;}
function evaluate(id,p){let x=[],y=[],secondary=[],summary='';const N=240;
const dft=(a)=>{const n=a.length,out=[];for(let k=0;k<n/2;k++){let re=0,im=0;for(let j=0;j<n;j++){const q=TAU*k*j/n;re+=a[j]*Math.cos(q);im-=a[j]*Math.sin(q);}out.push(Math.hypot(re,im)*2/n);}return out;};
const sine=(n,k,sz)=>Math.sin(TAU*k*n/sz);
const noise=(i)=>Math.sin(12.9898*i+78.233)*.35+Math.sin(4.135*i)*.17;
const response=(taps,omega)=>{let re=0,im=0;for(let k=0;k<taps.length;k++){re+=taps[k]*Math.cos(omega*k);im-=taps[k]*Math.sin(omega*k);}return Math.hypot(re,im);};
switch(id){
case 1:{const fs=8000, folded=Math.abs(p-Math.round(p/fs)*fs);x=Array.from({length:120},(_,i)=>i);y=x.map(n=>Math.sin(TAU*p*n/fs));secondary=x.map(n=>Math.sin(TAU*folded*n/fs));summary=`At fs=8000 samples/s, ${p} Hz aliases to |f−round(f/fs)fs|=${folded.toFixed(0)} Hz (a sign-reversed phase may occur).`;break;}
case 2:{const b=Math.round(p),delta=2/(2**b),quant=(v)=>Math.min(1-delta,Math.max(-1,Math.round((v+1)/delta)*delta-1));x=Array.from({length:N},(_,i)=>i);secondary=x.map(n=>.83*Math.sin(TAU*7*n/N));y=secondary.map(quant);const mse=y.reduce((s,a,i)=>s+(a-secondary[i])**2,0)/N;summary=`${b} bits over [−1,+1): Δ=${delta.toPrecision(4)}, observed RMSE=${Math.sqrt(mse).toPrecision(4)} (illustrative quantizer).`;break;}
case 3:{const M=Math.round(p);x=Array.from({length:85},(_,i)=>i);y=x.map(n=>Math.max(0,Math.min(1,(n+1)/M)));secondary=x.map(n=>1);summary=`Length M=${M}, h[k]=1/M for k=0…M−1; step settles by n=${M-1}, nominal delay ${(M-1)/2} samples.`;break;}
case 4:{const sz=64,v=Array.from({length:sz},(_,n)=>sine(n,p,sz));x=Array.from({length:sz/2},(_,i)=>i);y=dft(v);summary=`Rectangular window, 64 samples, frequency ${p.toFixed(2)} cycles per record. Noninteger frequency spreads energy among bins.`;break;}
case 5:{const sz=64,signal=Array.from({length:sz},(_,n)=>sine(n,p,sz)),hann=signal.map((a,n)=>a*(.5-.5*Math.cos(TAU*n/(sz-1))));x=Array.from({length:sz/2},(_,k)=>k);y=dft(signal);secondary=dft(hann).map(a=>a*2);summary=`Rectangular (result) and Hann (reference, approx coherent-gain compensated) DFT at ${p.toFixed(1)} cycles/record.`;break;}
case 6:{x=Array.from({length:9},(_,i)=>2**(i+5));y=x.map(n=>n*n);secondary=x.map(n=>n*Math.log2(n));summary=`For N=${2**Math.round(p)}: direct N²=${(2**Math.round(p))**2}; radix-two scaling N log2(N)=${(2**Math.round(p))*Math.round(p)} (not FLOP or timing measurements).`;break;}
case 7:{const M=Math.round(p),h=Array(M).fill(1/M);x=Array.from({length:200},(_,i)=>Math.PI*i/199);y=x.map(w=>response(h,w));summary=`${M}-point boxcar |H(e^jω)| from 0 to π rad/sample; DC gain=${response(h,0).toFixed(2)}.`;break;}
case 8:{const M=41,c=(M-1)/2,h=Array.from({length:M},(_,k)=>{const t=k-c,window=.5-.5*Math.cos(TAU*k/(M-1));return window*(t===0?2*p:Math.sin(2*Math.PI*p*t)/(Math.PI*t));});const sm=h.reduce((a,b)=>a+b,0);h.forEach((v,i)=>h[i]=v/sm);x=Array.from({length:200},(_,i)=>Math.PI*i/199);y=x.map(w=>response(h,w));summary=`41-tap Hann-windowed sinc with fc/fs=${p.toFixed(2)}; DC normalized to 1. Finite transition, not brick-wall.`;break;}
case 9:{const M=Math.round(p),delay=(M-1)/2;x=Array.from({length:100},(_,i)=>i);secondary=x.map(n=>Math.exp(-(((n-25)/6)**2)));y=x.map(n=>Math.exp(-(((n-25-delay)/6)**2)));summary=`Illustrative low-frequency pulse under an ideal pure delay of ${(M-1)/2} samples from a symmetric ${M}-tap FIR. Magnitude shaping is not modeled.`;break;}
case 10:{const a=p;x=Array.from({length:120},(_,i)=>i);y=x.map(n=>1-a**(n+1));secondary=x.map(()=>1);summary=`y[n]=a y[n−1]+(1−a)u[n], a=${a.toFixed(3)}, y[0]=${(1-a).toFixed(3)}, stable for |a|<1.`;break;}
case 11:{const r=p,w=.32*Math.PI;x=Array.from({length:120},(_,i)=>i);y=x.map(n=>r**n*Math.cos(w*n));secondary=x.map(n=>r**n);summary=`Damped mode r^n cos(0.32πn) for r=${r.toFixed(3)}, envelope at n=20 ${(r**20).toFixed(4)}.`;break;}
case 12:{const bits=Math.round(p),a=.87,step=2**(-bits),aq=Math.round(a/step)*step;const resp=(coef,n)=>1-coef**(n+1);x=Array.from({length:100},(_,i)=>i);secondary=x.map(n=>resp(a,n));y=x.map(n=>resp(aq,n));summary=`Ideal a=${a.toFixed(3)} versus rounded a=${aq.toFixed(6)} at ${bits} fractional bits (stable if |a|<1).`;break;}
case 13:{const M=Math.round(p);x=Array.from({length:160},(_,i)=>i);secondary=x.map(i=>Math.sin(TAU*3*i/160));const raw=x.map(i=>secondary[i]+noise(i));y=x.map(i=>{let s=0,c=0;for(let k=0;k<M;k++){if(i-k>=0){s+=raw[i-k];c++;}}return s/c;});summary=`Causal moving average M=${M} of a seeded deterministic noisy sinusoid. Increased M increases lag and may remove the desired waveform.`;break;}
case 14:{const mu=p;x=Array.from({length:45},(_,i)=>i);let w=0;y=x.map(n=>{let old=w;const e=.7-w;w+=mu*e;return old;});secondary=x.map(()=>.7);summary=`One-tap LMS with x=1, d=0.7; μ=${mu.toFixed(2)} and w[n+1]=w[n]+μ(0.7−w[n]). 0<μ<2 converges in this special model.`;break;}
case 15:{const M=Math.round(p),fs=2400,f=710;x=Array.from({length:100},(_,i)=>i);y=x.map(i=>Math.sin(TAU*f*(M*i)/fs));secondary=x.map(i=>Math.sin(TAU*(Math.abs(f-Math.round(f/(fs/M))*(fs/M)))*i/(fs/M)));summary=`${f} Hz input, fs=${fs} → fs_new=${(fs/M).toFixed(1)} Hz with M=${M}; no anti-alias filter. Folded frequency=${Math.abs(f-Math.round(f/(fs/M))*(fs/M)).toFixed(1)} Hz.`;break;}
case 16:{const K=Math.round(p),sz=64;x=Array.from({length:sz/2},(_,i)=>i);let sum=Array(sz/2).fill(0);for(let j=0;j<K;j++){const a=Array.from({length:sz},(_,n)=>Math.sin(TAU*9*n/sz)+noise(n+127*j));const sp=dft(a);sp.forEach((v,k)=>sum[k]+=v*v/K);}y=sum;summary=`Average K=${K} seeded segment periodograms (relative power; not PSD in physical units). Tones retain bins; random ripples tend to lessen.`;break;}
default:throw new Error('unknown DSP model');}
return {x,y,secondary,summary};}
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


  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: '<div class="sim-header"><span class="badge">Model 01</span><h3>' + "Aliasing frequency fold" + '</h3><p>' + "The apparent discrete frequency is the distance to the nearest integer multiple of fs." + '</p></div>' +
          '<div class="sim-controls"><div class="control"><label>' + "Analog frequency (Hz)" + ': <strong id="val-1">6100</strong></label>' +
          '<input id="slider-1" type="range" min="0" max="9500" step="50" value="6100" aria-label="' + "Analog frequency (Hz)" + '"></div></div>' +
          '<div class="readouts"><div class="stat-box"><small>Analysis</small><output id="stat-1">-</output></div></div>' +
          '<canvas id="canvas-1" width="800" height="300" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></canvas>',
    init: function(card) {
      try {
        var slider = card.querySelector('#slider-1');
        var valSpan = card.querySelector('#val-1');
        var statOut = card.querySelector('#stat-1');
        var canvas = card.querySelector('#canvas-1');

        function update() {
          var p = Number(slider.value);
          valSpan.textContent = String(p);
          try {
            var res = evaluate(1, p);
            draw(canvas, res);
            statOut.textContent = res.summary;
          } catch (err) {
            statOut.textContent = 'Model error: ' + err.message;
          }
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('DSP init error in model 1:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 1,
    html: '<div class="sim-header"><span class="badge">Model 02</span><h3>' + "ADC quantization and step size" + '</h3><p>' + "Quantize an ideal sine to finite signed full-scale levels; compare with the unquantized trace." + '</p></div>' +
          '<div class="sim-controls"><div class="control"><label>' + "ADC bits" + ': <strong id="val-2">5</strong></label>' +
          '<input id="slider-2" type="range" min="2" max="12" step="1" value="5" aria-label="' + "ADC bits" + '"></div></div>' +
          '<div class="readouts"><div class="stat-box"><small>Analysis</small><output id="stat-2">-</output></div></div>' +
          '<canvas id="canvas-2" width="800" height="300" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></canvas>',
    init: function(card) {
      try {
        var slider = card.querySelector('#slider-2');
        var valSpan = card.querySelector('#val-2');
        var statOut = card.querySelector('#stat-2');
        var canvas = card.querySelector('#canvas-2');

        function update() {
          var p = Number(slider.value);
          valSpan.textContent = String(p);
          try {
            var res = evaluate(2, p);
            draw(canvas, res);
            statOut.textContent = res.summary;
          } catch (err) {
            statOut.textContent = 'Model error: ' + err.message;
          }
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('DSP init error in model 2:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 2,
    html: '<div class="sim-header"><span class="badge">Model 03</span><h3>' + "FIR impulse and step response" + '</h3><p>' + "A normalized moving average of M samples rises in M steps and has a finite impulse response." + '</p></div>' +
          '<div class="sim-controls"><div class="control"><label>' + "Averaging taps" + ': <strong id="val-3">8</strong></label>' +
          '<input id="slider-3" type="range" min="2" max="24" step="1" value="8" aria-label="' + "Averaging taps" + '"></div></div>' +
          '<div class="readouts"><div class="stat-box"><small>Analysis</small><output id="stat-3">-</output></div></div>' +
          '<canvas id="canvas-3" width="800" height="300" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></canvas>',
    init: function(card) {
      try {
        var slider = card.querySelector('#slider-3');
        var valSpan = card.querySelector('#val-3');
        var statOut = card.querySelector('#stat-3');
        var canvas = card.querySelector('#canvas-3');

        function update() {
          var p = Number(slider.value);
          valSpan.textContent = String(p);
          try {
            var res = evaluate(3, p);
            draw(canvas, res);
            statOut.textContent = res.summary;
          } catch (err) {
            statOut.textContent = 'Model error: ' + err.message;
          }
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('DSP init error in model 3:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 2,
    html: '<div class="sim-header"><span class="badge">Model 04</span><h3>' + "DFT coherent versus noncoherent tones" + '</h3><p>' + "The rectangular-window finite DFT spreads energy across bins for a tone off its coherent grid." + '</p></div>' +
          '<div class="sim-controls"><div class="control"><label>' + "Cycles per 64 samples" + ': <strong id="val-4">5.35</strong></label>' +
          '<input id="slider-4" type="range" min="2" max="18" step="0.1" value="5.35" aria-label="' + "Cycles per 64 samples" + '"></div></div>' +
          '<div class="readouts"><div class="stat-box"><small>Analysis</small><output id="stat-4">-</output></div></div>' +
          '<canvas id="canvas-4" width="800" height="300" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></canvas>',
    init: function(card) {
      try {
        var slider = card.querySelector('#slider-4');
        var valSpan = card.querySelector('#val-4');
        var statOut = card.querySelector('#stat-4');
        var canvas = card.querySelector('#canvas-4');

        function update() {
          var p = Number(slider.value);
          valSpan.textContent = String(p);
          try {
            var res = evaluate(4, p);
            draw(canvas, res);
            statOut.textContent = res.summary;
          } catch (err) {
            statOut.textContent = 'Model error: ' + err.message;
          }
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('DSP init error in model 4:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 3,
    html: '<div class="sim-header"><span class="badge">Model 05</span><h3>' + "Hann-window leakage comparison" + '</h3><p>' + "A Hann taper reduces distant sidelobes at the expense of a wider main lobe." + '</p></div>' +
          '<div class="sim-controls"><div class="control"><label>' + "Cycles per record" + ': <strong id="val-5">6.3</strong></label>' +
          '<input id="slider-5" type="range" min="2" max="14" step="0.1" value="6.3" aria-label="' + "Cycles per record" + '"></div></div>' +
          '<div class="readouts"><div class="stat-box"><small>Analysis</small><output id="stat-5">-</output></div></div>' +
          '<canvas id="canvas-5" width="800" height="300" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></canvas>',
    init: function(card) {
      try {
        var slider = card.querySelector('#slider-5');
        var valSpan = card.querySelector('#val-5');
        var statOut = card.querySelector('#stat-5');
        var canvas = card.querySelector('#canvas-5');

        function update() {
          var p = Number(slider.value);
          valSpan.textContent = String(p);
          try {
            var res = evaluate(5, p);
            draw(canvas, res);
            statOut.textContent = res.summary;
          } catch (err) {
            statOut.textContent = 'Model error: ' + err.message;
          }
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('DSP init error in model 5:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 3,
    html: '<div class="sim-header"><span class="badge">Model 06</span><h3>' + "FFT arithmetic growth" + '</h3><p>' + "Compare the scaling indicators N\u00b2 and N log2 N; these are not implementation timings." + '</p></div>' +
          '<div class="sim-controls"><div class="control"><label>' + "FFT exponent log2(N)" + ': <strong id="val-6">10</strong></label>' +
          '<input id="slider-6" type="range" min="5" max="13" step="1" value="10" aria-label="' + "FFT exponent log2(N)" + '"></div></div>' +
          '<div class="readouts"><div class="stat-box"><small>Analysis</small><output id="stat-6">-</output></div></div>' +
          '<canvas id="canvas-6" width="800" height="300" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></canvas>',
    init: function(card) {
      try {
        var slider = card.querySelector('#slider-6');
        var valSpan = card.querySelector('#val-6');
        var statOut = card.querySelector('#stat-6');
        var canvas = card.querySelector('#canvas-6');

        function update() {
          var p = Number(slider.value);
          valSpan.textContent = String(p);
          try {
            var res = evaluate(6, p);
            draw(canvas, res);
            statOut.textContent = res.summary;
          } catch (err) {
            statOut.textContent = 'Model error: ' + err.message;
          }
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('DSP init error in model 6:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 4,
    html: '<div class="sim-header"><span class="badge">Model 07</span><h3>' + "Moving-average magnitude response" + '</h3><p>' + "A boxcar filter has periodic frequency-response nulls depending on M." + '</p></div>' +
          '<div class="sim-controls"><div class="control"><label>' + "Averaging length M" + ': <strong id="val-7">10</strong></label>' +
          '<input id="slider-7" type="range" min="2" max="30" step="1" value="10" aria-label="' + "Averaging length M" + '"></div></div>' +
          '<div class="readouts"><div class="stat-box"><small>Analysis</small><output id="stat-7">-</output></div></div>' +
          '<canvas id="canvas-7" width="800" height="300" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></canvas>',
    init: function(card) {
      try {
        var slider = card.querySelector('#slider-7');
        var valSpan = card.querySelector('#val-7');
        var statOut = card.querySelector('#stat-7');
        var canvas = card.querySelector('#canvas-7');

        function update() {
          var p = Number(slider.value);
          valSpan.textContent = String(p);
          try {
            var res = evaluate(7, p);
            draw(canvas, res);
            statOut.textContent = res.summary;
          } catch (err) {
            statOut.textContent = 'Model error: ' + err.message;
          }
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('DSP init error in model 7:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 4,
    html: '<div class="sim-header"><span class="badge">Model 08</span><h3>' + "Windowed-sinc FIR low-pass" + '</h3><p>' + "Vary cutoff of a 41-tap symmetric Hann-windowed low-pass; response is numerically evaluated." + '</p></div>' +
          '<div class="sim-controls"><div class="control"><label>' + "Normalized cutoff fc/fs" + ': <strong id="val-8">0.16</strong></label>' +
          '<input id="slider-8" type="range" min="0.03" max="0.42" step="0.01" value="0.16" aria-label="' + "Normalized cutoff fc/fs" + '"></div></div>' +
          '<div class="readouts"><div class="stat-box"><small>Analysis</small><output id="stat-8">-</output></div></div>' +
          '<canvas id="canvas-8" width="800" height="300" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></canvas>',
    init: function(card) {
      try {
        var slider = card.querySelector('#slider-8');
        var valSpan = card.querySelector('#val-8');
        var statOut = card.querySelector('#stat-8');
        var canvas = card.querySelector('#canvas-8');

        function update() {
          var p = Number(slider.value);
          valSpan.textContent = String(p);
          try {
            var res = evaluate(8, p);
            draw(canvas, res);
            statOut.textContent = res.summary;
          } catch (err) {
            statOut.textContent = 'Model error: ' + err.message;
          }
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('DSP init error in model 8:', err);
      }
    }
  });

  MODELS.push({
    idx: 9,
    unit: 5,
    html: '<div class="sim-header"><span class="badge">Model 09</span><h3>' + "Symmetric FIR linear-phase delay" + '</h3><p>' + "The ideal symmetric impulse response has group delay (M\u22121)/2 samples." + '</p></div>' +
          '<div class="sim-controls"><div class="control"><label>' + "Odd number of taps" + ': <strong id="val-9">15</strong></label>' +
          '<input id="slider-9" type="range" min="3" max="41" step="2" value="15" aria-label="' + "Odd number of taps" + '"></div></div>' +
          '<div class="readouts"><div class="stat-box"><small>Analysis</small><output id="stat-9">-</output></div></div>' +
          '<canvas id="canvas-9" width="800" height="300" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></canvas>',
    init: function(card) {
      try {
        var slider = card.querySelector('#slider-9');
        var valSpan = card.querySelector('#val-9');
        var statOut = card.querySelector('#stat-9');
        var canvas = card.querySelector('#canvas-9');

        function update() {
          var p = Number(slider.value);
          valSpan.textContent = String(p);
          try {
            var res = evaluate(9, p);
            draw(canvas, res);
            statOut.textContent = res.summary;
          } catch (err) {
            statOut.textContent = 'Model error: ' + err.message;
          }
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('DSP init error in model 9:', err);
      }
    }
  });

  MODELS.push({
    idx: 10,
    unit: 5,
    html: '<div class="sim-header"><span class="badge">Model 10</span><h3>' + "One-pole IIR step transient" + '</h3><p>' + "y[n]=a y[n\u22121]+(1\u2212a)u[n] with zero initial state." + '</p></div>' +
          '<div class="sim-controls"><div class="control"><label>' + "Pole a" + ': <strong id="val-10">0.8</strong></label>' +
          '<input id="slider-10" type="range" min="0.05" max="0.98" step="0.01" value="0.8" aria-label="' + "Pole a" + '"></div></div>' +
          '<div class="readouts"><div class="stat-box"><small>Analysis</small><output id="stat-10">-</output></div></div>' +
          '<canvas id="canvas-10" width="800" height="300" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></canvas>',
    init: function(card) {
      try {
        var slider = card.querySelector('#slider-10');
        var valSpan = card.querySelector('#val-10');
        var statOut = card.querySelector('#stat-10');
        var canvas = card.querySelector('#canvas-10');

        function update() {
          var p = Number(slider.value);
          valSpan.textContent = String(p);
          try {
            var res = evaluate(10, p);
            draw(canvas, res);
            statOut.textContent = res.summary;
          } catch (err) {
            statOut.textContent = 'Model error: ' + err.message;
          }
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('DSP init error in model 10:', err);
      }
    }
  });

  MODELS.push({
    idx: 11,
    unit: 6,
    html: '<div class="sim-header"><span class="badge">Model 11</span><h3>' + "Second-order resonance radius" + '</h3><p>' + "A damped discrete sinusoid r^n cos(\u03c90n) decays faster for smaller pole radius." + '</p></div>' +
          '<div class="sim-controls"><div class="control"><label>' + "Pole radius" + ': <strong id="val-11">0.92</strong></label>' +
          '<input id="slider-11" type="range" min="0.5" max="0.995" step="0.005" value="0.92" aria-label="' + "Pole radius" + '"></div></div>' +
          '<div class="readouts"><div class="stat-box"><small>Analysis</small><output id="stat-11">-</output></div></div>' +
          '<canvas id="canvas-11" width="800" height="300" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></canvas>',
    init: function(card) {
      try {
        var slider = card.querySelector('#slider-11');
        var valSpan = card.querySelector('#val-11');
        var statOut = card.querySelector('#stat-11');
        var canvas = card.querySelector('#canvas-11');

        function update() {
          var p = Number(slider.value);
          valSpan.textContent = String(p);
          try {
            var res = evaluate(11, p);
            draw(canvas, res);
            statOut.textContent = res.summary;
          } catch (err) {
            statOut.textContent = 'Model error: ' + err.message;
          }
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('DSP init error in model 11:', err);
      }
    }
  });

  MODELS.push({
    idx: 12,
    unit: 6,
    html: '<div class="sim-header"><span class="badge">Model 12</span><h3>' + "Fixed-point coefficient error" + '</h3><p>' + "Quantize a one-pole feedback coefficient; plot the difference from its ideal step output." + '</p></div>' +
          '<div class="sim-controls"><div class="control"><label>' + "Fractional precision (bits)" + ': <strong id="val-12">7</strong></label>' +
          '<input id="slider-12" type="range" min="3" max="15" step="1" value="7" aria-label="' + "Fractional precision (bits)" + '"></div></div>' +
          '<div class="readouts"><div class="stat-box"><small>Analysis</small><output id="stat-12">-</output></div></div>' +
          '<canvas id="canvas-12" width="800" height="300" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></canvas>',
    init: function(card) {
      try {
        var slider = card.querySelector('#slider-12');
        var valSpan = card.querySelector('#val-12');
        var statOut = card.querySelector('#stat-12');
        var canvas = card.querySelector('#canvas-12');

        function update() {
          var p = Number(slider.value);
          valSpan.textContent = String(p);
          try {
            var res = evaluate(12, p);
            draw(canvas, res);
            statOut.textContent = res.summary;
          } catch (err) {
            statOut.textContent = 'Model error: ' + err.message;
          }
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('DSP init error in model 12:', err);
      }
    }
  });

  MODELS.push({
    idx: 13,
    unit: 7,
    html: '<div class="sim-header"><span class="badge">Model 13</span><h3>' + "Statistical noise reduction" + '</h3><p>' + "A causal moving average smooths deterministic seeded white-noise observations at a cost in delay." + '</p></div>' +
          '<div class="sim-controls"><div class="control"><label>' + "Moving average M" + ': <strong id="val-13">8</strong></label>' +
          '<input id="slider-13" type="range" min="1" max="30" step="1" value="8" aria-label="' + "Moving average M" + '"></div></div>' +
          '<div class="readouts"><div class="stat-box"><small>Analysis</small><output id="stat-13">-</output></div></div>' +
          '<canvas id="canvas-13" width="800" height="300" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></canvas>',
    init: function(card) {
      try {
        var slider = card.querySelector('#slider-13');
        var valSpan = card.querySelector('#val-13');
        var statOut = card.querySelector('#stat-13');
        var canvas = card.querySelector('#canvas-13');

        function update() {
          var p = Number(slider.value);
          valSpan.textContent = String(p);
          try {
            var res = evaluate(13, p);
            draw(canvas, res);
            statOut.textContent = res.summary;
          } catch (err) {
            statOut.textContent = 'Model error: ' + err.message;
          }
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('DSP init error in model 13:', err);
      }
    }
  });

  MODELS.push({
    idx: 14,
    unit: 7,
    html: '<div class="sim-header"><span class="badge">Model 14</span><h3>' + "LMS one-tap convergence" + '</h3><p>' + "Adapt w to a noiseless desired gain of 0.7 using a single constant excitation x=1." + '</p></div>' +
          '<div class="sim-controls"><div class="control"><label>' + "LMS step size \u03bc" + ': <strong id="val-14">0.25</strong></label>' +
          '<input id="slider-14" type="range" min="0.01" max="1.9" step="0.01" value="0.25" aria-label="' + "LMS step size \u03bc" + '"></div></div>' +
          '<div class="readouts"><div class="stat-box"><small>Analysis</small><output id="stat-14">-</output></div></div>' +
          '<canvas id="canvas-14" width="800" height="300" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></canvas>',
    init: function(card) {
      try {
        var slider = card.querySelector('#slider-14');
        var valSpan = card.querySelector('#val-14');
        var statOut = card.querySelector('#stat-14');
        var canvas = card.querySelector('#canvas-14');

        function update() {
          var p = Number(slider.value);
          valSpan.textContent = String(p);
          try {
            var res = evaluate(14, p);
            draw(canvas, res);
            statOut.textContent = res.summary;
          } catch (err) {
            statOut.textContent = 'Model error: ' + err.message;
          }
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('DSP init error in model 14:', err);
      }
    }
  });

  MODELS.push({
    idx: 15,
    unit: 8,
    html: '<div class="sim-header"><span class="badge">Model 15</span><h3>' + "Decimation alias illustration" + '</h3><p>' + "Show folding of a high-rate sinusoid after keeping every Mth sample without an anti-alias filter." + '</p></div>' +
          '<div class="sim-controls"><div class="control"><label>' + "Decimation factor" + ': <strong id="val-15">4</strong></label>' +
          '<input id="slider-15" type="range" min="2" max="10" step="1" value="4" aria-label="' + "Decimation factor" + '"></div></div>' +
          '<div class="readouts"><div class="stat-box"><small>Analysis</small><output id="stat-15">-</output></div></div>' +
          '<canvas id="canvas-15" width="800" height="300" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></canvas>',
    init: function(card) {
      try {
        var slider = card.querySelector('#slider-15');
        var valSpan = card.querySelector('#val-15');
        var statOut = card.querySelector('#stat-15');
        var canvas = card.querySelector('#canvas-15');

        function update() {
          var p = Number(slider.value);
          valSpan.textContent = String(p);
          try {
            var res = evaluate(15, p);
            draw(canvas, res);
            statOut.textContent = res.summary;
          } catch (err) {
            statOut.textContent = 'Model error: ' + err.message;
          }
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('DSP init error in model 15:', err);
      }
    }
  });

  MODELS.push({
    idx: 16,
    unit: 8,
    html: '<div class="sim-header"><span class="badge">Model 16</span><h3>' + "Welch spectral averaging" + '</h3><p>' + "Average deterministic seeded periodograms with varying segment count; the plotted estimator becomes smoother." + '</p></div>' +
          '<div class="sim-controls"><div class="control"><label>' + "Average segments" + ': <strong id="val-16">4</strong></label>' +
          '<input id="slider-16" type="range" min="1" max="12" step="1" value="4" aria-label="' + "Average segments" + '"></div></div>' +
          '<div class="readouts"><div class="stat-box"><small>Analysis</small><output id="stat-16">-</output></div></div>' +
          '<canvas id="canvas-16" width="800" height="300" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></canvas>',
    init: function(card) {
      try {
        var slider = card.querySelector('#slider-16');
        var valSpan = card.querySelector('#val-16');
        var statOut = card.querySelector('#stat-16');
        var canvas = card.querySelector('#canvas-16');

        function update() {
          var p = Number(slider.value);
          valSpan.textContent = String(p);
          try {
            var res = evaluate(16, p);
            draw(canvas, res);
            statOut.textContent = res.summary;
          } catch (err) {
            statOut.textContent = 'Model error: ' + err.message;
          }
        }
        slider.addEventListener('input', update);
        update();
      } catch (err) {
        console.warn('DSP init error in model 16:', err);
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
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', function() {
        if (document.getElementById('sim-container')) window.SimulationEngine.initSimulation('sim-container');
      });
    } else {
      if (document.getElementById('sim-container')) window.SimulationEngine.initSimulation('sim-container');
    }
  }
})(typeof window === 'undefined' ? globalThis : window);
