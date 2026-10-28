/* control-systems-engineering Interactive Simulation Suite */
(function(window) {
  'use strict';

  var OPENSTEM_SIM_MODELS = [];
  // Core model definitions
// Offline educational model library. These are simplified equations, not equipment simulations.
(function(root){
'use strict';
const specs=[{"id":1,"title":"First-order step response","formula":"y(t)=K(1−e^(−t/τ))","type":"first","a":{"label":"Gain K","min":0.2,"max":5,"step":0.1,"value":2},"b":{"label":"Time constant τ (s)","min":0.2,"max":8,"step":0.1,"value":2},"ylabel":"Output","xlabel":"Time (s)","assumption":"Single-pole linear plant; zero initial condition."},{"id":2,"title":"Proportional closed-loop tracking","formula":"T(s)=Kp/(τs+1+Kp)","type":"pstep","a":{"label":"Proportional gain Kp","min":0.1,"max":15,"step":0.1,"value":3},"b":{"label":"Plant τ (s)","min":0.2,"max":8,"step":0.1,"value":2},"ylabel":"Output","xlabel":"Time (s)","assumption":"Unity negative feedback around a plant 1/(τs+1)."},{"id":3,"title":"Second-order damping and overshoot","formula":"ωn²/(s²+2ζωns+ωn²)","type":"second","a":{"label":"Damping ratio ζ","min":0.05,"max":0.95,"step":0.01,"value":0.45},"b":{"label":"Natural frequency ωn (rad/s)","min":1,"max":18,"step":0.5,"value":6},"ylabel":"Output","xlabel":"Time (s)","assumption":"Ideal underdamped, unit-gain second-order step."},{"id":4,"title":"Decay of a complex pole mode","formula":"e^(−σt)cos(ωdt)","type":"complex","a":{"label":"Decay σ (1/s)","min":0.1,"max":5,"step":0.1,"value":1},"b":{"label":"Oscillation ωd (rad/s)","min":0.5,"max":15,"step":0.1,"value":6},"ylabel":"Mode amplitude","xlabel":"Time (s)","assumption":"Single ideal damped oscillatory mode, initial amplitude 1."},{"id":5,"title":"Cubic Routh stability margin","formula":"a₂a₁−a₀ >0","type":"routh","a":{"label":"a₂ coefficient","min":0.2,"max":8,"step":0.1,"value":4},"b":{"label":"a₀ coefficient","min":0.1,"max":30,"step":0.1,"value":12},"ylabel":"Stability margin","xlabel":"a₀ coefficient","assumption":"For s³+a₂s²+5s+a₀; positive coefficients and margin required."},{"id":6,"title":"Proportional step-tracking error","formula":"e(t)=1−y(t)","type":"error","a":{"label":"Gain Kp","min":0.1,"max":12,"step":0.1,"value":3},"b":{"label":"Plant τ (s)","min":0.2,"max":8,"step":0.1,"value":2},"ylabel":"Error","xlabel":"Time (s)","assumption":"Reference is a unit step; plant 1/(τs+1)."},{"id":7,"title":"First-order Bode magnitude","formula":"20log10[K/√(1+(ωτ)²)]","type":"bode","a":{"label":"Gain K","min":0.1,"max":10,"step":0.1,"value":2},"b":{"label":"Time constant τ (s)","min":0.05,"max":5,"step":0.05,"value":0.5},"ylabel":"Magnitude (dB)","xlabel":"ω (rad/s), log scale","assumption":"Frequency response of K/(1+τs)."},{"id":8,"title":"Lag from a pole and transport delay","formula":"Phase=−atan(ωτ)−ωL","type":"phase","a":{"label":"Delay L (s)","min":0,"max":1,"step":0.01,"value":0.12},"b":{"label":"Time constant τ (s)","min":0.05,"max":2,"step":0.05,"value":0.5},"ylabel":"Phase (deg)","xlabel":"ω (rad/s)","assumption":"Unwrapped continuous phase of e^(−Ls)/(1+τs)."},{"id":9,"title":"PI loop step response","formula":"u=Kp e+Ki∫e dt","type":"pi","a":{"label":"Gain Kp","min":0.1,"max":5,"step":0.1,"value":1.5},"b":{"label":"Integral gain Ki (1/s)","min":0.05,"max":3,"step":0.05,"value":0.5},"ylabel":"Output","xlabel":"Time (s)","assumption":"Ideal unit-gain first-order plant τ=2 s; numerical integration with no saturation."},{"id":10,"title":"Lead-network phase contribution","formula":"atan(ωT)−atan(αωT)","type":"lead","a":{"label":"Lead ratio α","min":0.05,"max":0.95,"step":0.05,"value":0.25},"b":{"label":"Zero constant T (s)","min":0.1,"max":5,"step":0.1,"value":1},"ylabel":"Added phase (deg)","xlabel":"ω (rad/s), log scale","assumption":"Lead C(s)=(1+sT)/(1+sαT), 0<α<1."},{"id":11,"title":"Double-integrator state-feedback decay","formula":"ẍ+k₂ẋ+k₁x=0","type":"state","a":{"label":"Position gain k1 (1/s²)","min":0.5,"max":25,"step":0.5,"value":6},"b":{"label":"Velocity gain k2 (1/s)","min":0.5,"max":12,"step":0.5,"value":5},"ylabel":"Position (m)","xlabel":"Time (s)","assumption":"Initial x=1 m and velocity zero; ideal force-to-acceleration plant."},{"id":12,"title":"State observer estimation error","formula":"e(t)=e₀exp[−(2+L)t]","type":"observer","a":{"label":"Observer gain L (1/s)","min":0,"max":20,"step":0.5,"value":4},"b":{"label":"Initial estimation error e0","min":0.1,"max":5,"step":0.1,"value":1},"ylabel":"State error","xlabel":"Time (s)","assumption":"Scalar plant ẋ=−2x+u, sensor y=x; no bias or model mismatch."},{"id":13,"title":"Exact sampled first-order system","formula":"x[k+1]=ax[k]+(1−a)u[k]","type":"zoh","a":{"label":"Sample interval h (s)","min":0.05,"max":3,"step":0.05,"value":0.5},"b":{"label":"Time constant τ (s)","min":0.4,"max":5,"step":0.1,"value":2},"ylabel":"Output","xlabel":"Time (s)","assumption":"Unit-step command; exact zero-order-hold discretization."},{"id":14,"title":"Aliasing in sampled measurements","formula":"falias=|f−round(f/fs)fs|","type":"alias","a":{"label":"Signal frequency f (Hz)","min":0.5,"max":40,"step":0.5,"value":12},"b":{"label":"Sample frequency fs (Hz)","min":5,"max":50,"step":1,"value":20},"ylabel":"Sampled amplitude","xlabel":"Sample index","assumption":"Samples of unit-amplitude sinusoid, no anti-alias filter."},{"id":15,"title":"PI saturation and anti-windup comparison","formula":"u=sat(Kp e+I)","type":"sat","a":{"label":"Proportional gain Kp","min":0.2,"max":5,"step":0.1,"value":2},"b":{"label":"Integral gain Ki (1/s)","min":0.05,"max":3,"step":0.05,"value":0.5},"ylabel":"Output","xlabel":"Time (s)","assumption":"Reference 1.5 before 10 s, then 0.4; max actuator 1. Two traces: ordinary and conditional-integrator PI."},{"id":16,"title":"Lumped thermal step response","formula":"ΔT=P/(hA)(1−e^(−hAt/Cth))","type":"thermal","a":{"label":"Heater power P (W)","min":20,"max":500,"step":10,"value":200},"b":{"label":"Heat-loss coefficient hA (W/K)","min":2,"max":30,"step":1,"value":10},"ylabel":"Temperature rise (K)","xlabel":"Time (s)","assumption":"Constant heater input, Cth=1000 J/K, linearized losses."}];
function calc(id,a,b){
 const p=specs[id-1];if(!p||!Number.isFinite(a)||!Number.isFinite(b)) throw Error('invalid inputs');
 let xs=[],ys=[],alt=null,metric='',unit='';
 const range=(start,stop,n,fn)=>{for(let i=0;i<n;i++){let x=start+(stop-start)*i/(n-1);xs.push(x);ys.push(fn(x));}};
 const run=(dt,end,fn)=>{let n=Math.round(end/dt);for(let i=0;i<=n;i++){let x=i*dt;xs.push(x);ys.push(fn(x,i));}};
 switch(p.type){
  case 'first':range(0,20,241,t=>a*(1-Math.exp(-t/b))); metric=(a*(1-Math.exp(-10/b))).toFixed(4)+' at t=10 s';break;
  case 'pstep':range(0,20,241,t=>a/(1+a)*(1-Math.exp(-(1+a)*t/b)));metric='DC gain '+(a/(1+a)).toFixed(4);break;
  case 'second':{const wd=b*Math.sqrt(1-a*a);range(0,5,301,t=>1-Math.exp(-a*b*t)*(Math.cos(wd*t)+(a/Math.sqrt(1-a*a))*Math.sin(wd*t)));metric='overshoot '+(100*Math.exp(-Math.PI*a/Math.sqrt(1-a*a))).toFixed(2)+'%';break;}
  case 'complex':range(0,8,241,t=>Math.exp(-a*t)*Math.cos(b*t));metric='time constant '+(1/a).toFixed(3)+' s';break;
  case 'routh':range(0,30,301,c=>5*a-c);metric=(5*a-b>0?'stable cubic ':'not strictly stable ')+', margin '+(5*a-b).toFixed(2);break;
  case 'error':range(0,20,241,t=>1-a/(1+a)*(1-Math.exp(-(1+a)*t/b)));metric='steady error '+(1/(1+a)).toFixed(4);break;
  case 'bode':range(-2,2.5,301,log=>20*Math.log10(a/Math.sqrt(1+Math.pow(Math.pow(10,log)*b,2))));metric='gain at 1 rad/s '+(20*Math.log10(a/Math.sqrt(1+b*b))).toFixed(2)+' dB';break;
  case 'phase':range(0.1,20,301,w=>-(Math.atan(w*b)+w*a)*180/Math.PI);metric='phase at 1 rad/s '+(-(Math.atan(b)+a)*180/Math.PI).toFixed(2)+'°';break;
  case 'pi':{let y=0,I=0,dt=0.01; for(let i=0;i<=2000;i++){let t=i*dt; if(i%10===0){xs.push(t);ys.push(y);}let e=1-y;let u=a*e+I; I+=b*dt*e;y+=dt*(u-y)/2;}metric='last output '+y.toFixed(4);break;}
  case 'lead':range(-2,2.5,301,log=>(Math.atan(Math.pow(10,log)*b)-Math.atan(a*Math.pow(10,log)*b))*180/Math.PI);metric='max ideal lead '+(Math.asin((1-a)/(1+a))*180/Math.PI).toFixed(2)+'°';break;
  case 'state':{let x=1,v=0,dt=0.005;for(let i=0;i<=1600;i++){let t=i*dt;if(i%8===0){xs.push(t);ys.push(x);}const acceleration=(x,v)=>-a*x-b*v;let k1x=v,k1v=acceleration(x,v),k2x=v+0.5*dt*k1v,k2v=acceleration(x+0.5*dt*k1x,v+0.5*dt*k1v),k3x=v+0.5*dt*k2v,k3v=acceleration(x+0.5*dt*k2x,v+0.5*dt*k2v),k4x=v+dt*k3v,k4v=acceleration(x+dt*k3x,v+dt*k3v);x+=dt*(k1x+2*k2x+2*k3x+k4x)/6;v+=dt*(k1v+2*k2v+2*k3v+k4v)/6;}metric='final x '+x.toFixed(4)+' m';break;}
  case 'observer':range(0,5,251,t=>b*Math.exp(-(2+a)*t));metric='error time constant '+(1/(2+a)).toFixed(3)+' s';break;
  case 'zoh':{let z=0,t=0,k=0;while(t<=12+1e-8){xs.push(t);ys.push(z); z=Math.exp(-a/b)*z+(1-Math.exp(-a/b));k++;t=k*a;}metric='sample factor '+Math.exp(-a/b).toFixed(5);break;}
  case 'alias':for(let k=0;k<=40;k++){xs.push(k);ys.push(Math.sin(2*Math.PI*a*k/b));}metric='apparent alias '+Math.abs(a-Math.round(a/b)*b).toFixed(3)+' Hz';break;
  case 'sat':{let dt=0.01,ys1=[],ys2=[],y1=0,y2=0,I1=0,I2=0;for(let i=0;i<=2500;i++){let t=i*dt,r=t<10?1.5:0.4;if(i%10===0){xs.push(t);ys1.push(y1);ys2.push(y2);}let e1=r-y1,e2=r-y2,v1=a*e1+I1,v2=a*e2+I2,u1=Math.max(0,Math.min(1,v1)),u2=Math.max(0,Math.min(1,v2));I1+=b*dt*e1;if(!(v2>=1&&e2>0)&&!(v2<=0&&e2<0))I2+=b*dt*e2; y1+=dt*(u1-y1)/5;y2+=dt*(u2-y2)/5;}ys=ys1;alt=ys2;metric='two traces: no anti-windup / conditional integration';break;}
  case 'thermal':range(0,400,301,t=>a/b*(1-Math.exp(-b*t/1000)));metric='final ΔT '+(a/b).toFixed(3)+' K';break;
  default: throw Error('unknown model');
 }
 if(!xs.length||!ys.length||xs.some(v=>!Number.isFinite(v))||ys.some(v=>!Number.isFinite(v)))throw Error('invalid numeric result');
 return {xs,ys,alt,metric,xlabel:p.xlabel,ylabel:p.ylabel};
}
root.OpenSTEMModels={specs,calc};
if(typeof module!=='undefined'&&module.exports)module.exports=root.OpenSTEMModels;
})(typeof window==='undefined'?globalThis:window);



  OPENSTEM_SIM_MODELS.push({
    idx: 1,
    unit: 1,
    html: "<div class=\"panel\"><span class=\"label\">Offline interactive demonstration 01/16</span><h3>First-order step response</h3><p><strong>Equation:</strong> y(t)=K(1\u2212e^(\u2212t/\u03c4))</p><p>Single-pole linear plant; zero initial condition.</p><div class=\"formgrid\"><div><label for=\"a\">Gain K: <output id=\"aout\"></output></label><input type=\"range\" id=\"a\" min=\"0.2\" max=\"5\" step=\"0.1\" value=\"2\"></div><div><label for=\"b\">Time constant \u03c4 (s): <output id=\"bout\"></output></label><input type=\"range\" id=\"b\" min=\"0.2\" max=\"8\" step=\"0.1\" value=\"2\"></div></div><div class=\"reading\">Calculated result: <span id=\"metric\" aria-live=\"polite\"></span></div><svg id=\"graph\" class=\"graph\" viewBox=\"0 0 810 300\" role=\"img\" aria-label=\"Interactive model output plotted against the horizontal axis\"></svg><p><button type=\"button\" id=\"reset\">Reset values</button> <span id=\"status\" class=\"muted\" role=\"status\"></span></p><div class=\"warn\"><b>Educational model, not equipment validation.</b> Simplifying assumptions exclude many real sensor, actuator, friction, failure and safety effects. Check parameters and physical limits before using any equation in engineering work.</div></div>",
    init: function(card) {
      try {
        card.dataset.model = String(1);
        document.body.dataset.model = String(1);
const i=Number(document.body.dataset.model)-1,s=OpenSTEMModels.specs[i],a=card.querySelector('#a'),b=card.querySelector('#b'),aout=card.querySelector('#aout'),bout=card.querySelector('#bout'),metric=card.querySelector('#metric'),svg=card.querySelector('#graph'),status=card.querySelector('#status');
function f(v){return Number(v).toLocaleString('en-US',{maximumFractionDigits:4});}
function draw(){const aa=Number(a.value),bb=Number(b.value);aout.textContent=f(aa);bout.textContent=f(bb); const o=OpenSTEMModels.calc(i+1,aa,bb);metric.textContent=o.metric;let mn=Math.min(...o.ys,...(o.alt||[])),mx=Math.max(...o.ys,...(o.alt||[]));if(mx===mn){mn-=1;mx+=1;}else{let m=(mx-mn)*.13;mn-=m;mx+=m;}
let x0=o.xs[0],x1=o.xs[o.xs.length-1],w=810,h=300,l=65,t=20,r=20,bt=54;let X=x=>l+(x-x0)/(x1-x0)*(w-l-r),Y=y=>t+(mx-y)/(mx-mn)*(h-t-bt),pts=y=>y.map((v,j)=>X(o.xs[j]).toFixed(2)+','+Y(v).toFixed(2)).join(' ');
svg.innerHTML='<rect x="'+l+'" y="'+t+'" width="'+(w-l-r)+'" height="'+(h-t-bt)+'" fill="#fafcff" stroke="#b5c9d9"/>';
let mk=(tag,attr,txt)=>{const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attr).forEach(([k,v])=>el.setAttribute(k,v));if(txt!==undefined)el.textContent=txt;svg.append(el);};
for(let k=0;k<=4;k++){let yy=t+k*(h-t-bt)/4;mk('line',{x1:l,y1:yy,x2:w-r,y2:yy,stroke:'#e0e9ef'});mk('text',{x:3,y:yy+5},f(mx-(mx-mn)*k/4));}
for(let k=0;k<=4;k++){let xx=l+k*(w-l-r)/4;mk('text',{x:xx-15,y:h-24},f(x0+(x1-x0)*k/4));}
mk('polyline',{points:pts(o.ys),class:'trace'});if(o.alt)mk('polyline',{points:pts(o.alt),class:'alt'});
mk('text',{x:w/2-80,y:h-2},o.xlabel);mk('text',{x:l+5,y:14},o.ylabel);
status.textContent='Recomputed for current parameters. Solid blue: model output'+(o.alt?'; dashed orange: conditional-integrator result':'')+'.';
}
a.addEventListener('input',draw);b.addEventListener('input',draw);card.querySelector('#reset').addEventListener('click',()=>{a.value=s.a.value;b.value=s.b.value;draw();});draw();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 2,
    unit: 1,
    html: "<div class=\"panel\"><span class=\"label\">Offline interactive demonstration 02/16</span><h3>Proportional closed-loop tracking</h3><p><strong>Equation:</strong> T(s)=Kp/(\u03c4s+1+Kp)</p><p>Unity negative feedback around a plant 1/(\u03c4s+1).</p><div class=\"formgrid\"><div><label for=\"a\">Proportional gain Kp: <output id=\"aout\"></output></label><input type=\"range\" id=\"a\" min=\"0.1\" max=\"15\" step=\"0.1\" value=\"3\"></div><div><label for=\"b\">Plant \u03c4 (s): <output id=\"bout\"></output></label><input type=\"range\" id=\"b\" min=\"0.2\" max=\"8\" step=\"0.1\" value=\"2\"></div></div><div class=\"reading\">Calculated result: <span id=\"metric\" aria-live=\"polite\"></span></div><svg id=\"graph\" class=\"graph\" viewBox=\"0 0 810 300\" role=\"img\" aria-label=\"Interactive model output plotted against the horizontal axis\"></svg><p><button type=\"button\" id=\"reset\">Reset values</button> <span id=\"status\" class=\"muted\" role=\"status\"></span></p><div class=\"warn\"><b>Educational model, not equipment validation.</b> Simplifying assumptions exclude many real sensor, actuator, friction, failure and safety effects. Check parameters and physical limits before using any equation in engineering work.</div></div>",
    init: function(card) {
      try {
        card.dataset.model = String(2);
        document.body.dataset.model = String(2);
const i=Number(document.body.dataset.model)-1,s=OpenSTEMModels.specs[i],a=card.querySelector('#a'),b=card.querySelector('#b'),aout=card.querySelector('#aout'),bout=card.querySelector('#bout'),metric=card.querySelector('#metric'),svg=card.querySelector('#graph'),status=card.querySelector('#status');
function f(v){return Number(v).toLocaleString('en-US',{maximumFractionDigits:4});}
function draw(){const aa=Number(a.value),bb=Number(b.value);aout.textContent=f(aa);bout.textContent=f(bb); const o=OpenSTEMModels.calc(i+1,aa,bb);metric.textContent=o.metric;let mn=Math.min(...o.ys,...(o.alt||[])),mx=Math.max(...o.ys,...(o.alt||[]));if(mx===mn){mn-=1;mx+=1;}else{let m=(mx-mn)*.13;mn-=m;mx+=m;}
let x0=o.xs[0],x1=o.xs[o.xs.length-1],w=810,h=300,l=65,t=20,r=20,bt=54;let X=x=>l+(x-x0)/(x1-x0)*(w-l-r),Y=y=>t+(mx-y)/(mx-mn)*(h-t-bt),pts=y=>y.map((v,j)=>X(o.xs[j]).toFixed(2)+','+Y(v).toFixed(2)).join(' ');
svg.innerHTML='<rect x="'+l+'" y="'+t+'" width="'+(w-l-r)+'" height="'+(h-t-bt)+'" fill="#fafcff" stroke="#b5c9d9"/>';
let mk=(tag,attr,txt)=>{const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attr).forEach(([k,v])=>el.setAttribute(k,v));if(txt!==undefined)el.textContent=txt;svg.append(el);};
for(let k=0;k<=4;k++){let yy=t+k*(h-t-bt)/4;mk('line',{x1:l,y1:yy,x2:w-r,y2:yy,stroke:'#e0e9ef'});mk('text',{x:3,y:yy+5},f(mx-(mx-mn)*k/4));}
for(let k=0;k<=4;k++){let xx=l+k*(w-l-r)/4;mk('text',{x:xx-15,y:h-24},f(x0+(x1-x0)*k/4));}
mk('polyline',{points:pts(o.ys),class:'trace'});if(o.alt)mk('polyline',{points:pts(o.alt),class:'alt'});
mk('text',{x:w/2-80,y:h-2},o.xlabel);mk('text',{x:l+5,y:14},o.ylabel);
status.textContent='Recomputed for current parameters. Solid blue: model output'+(o.alt?'; dashed orange: conditional-integrator result':'')+'.';
}
a.addEventListener('input',draw);b.addEventListener('input',draw);card.querySelector('#reset').addEventListener('click',()=>{a.value=s.a.value;b.value=s.b.value;draw();});draw();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 3,
    unit: 2,
    html: "<div class=\"panel\"><span class=\"label\">Offline interactive demonstration 03/16</span><h3>Second-order damping and overshoot</h3><p><strong>Equation:</strong> \u03c9n\u00b2/(s\u00b2+2\u03b6\u03c9ns+\u03c9n\u00b2)</p><p>Ideal underdamped, unit-gain second-order step.</p><div class=\"formgrid\"><div><label for=\"a\">Damping ratio \u03b6: <output id=\"aout\"></output></label><input type=\"range\" id=\"a\" min=\"0.05\" max=\"0.95\" step=\"0.01\" value=\"0.45\"></div><div><label for=\"b\">Natural frequency \u03c9n (rad/s): <output id=\"bout\"></output></label><input type=\"range\" id=\"b\" min=\"1\" max=\"18\" step=\"0.5\" value=\"6\"></div></div><div class=\"reading\">Calculated result: <span id=\"metric\" aria-live=\"polite\"></span></div><svg id=\"graph\" class=\"graph\" viewBox=\"0 0 810 300\" role=\"img\" aria-label=\"Interactive model output plotted against the horizontal axis\"></svg><p><button type=\"button\" id=\"reset\">Reset values</button> <span id=\"status\" class=\"muted\" role=\"status\"></span></p><div class=\"warn\"><b>Educational model, not equipment validation.</b> Simplifying assumptions exclude many real sensor, actuator, friction, failure and safety effects. Check parameters and physical limits before using any equation in engineering work.</div></div>",
    init: function(card) {
      try {
        card.dataset.model = String(3);
        document.body.dataset.model = String(3);
const i=Number(document.body.dataset.model)-1,s=OpenSTEMModels.specs[i],a=card.querySelector('#a'),b=card.querySelector('#b'),aout=card.querySelector('#aout'),bout=card.querySelector('#bout'),metric=card.querySelector('#metric'),svg=card.querySelector('#graph'),status=card.querySelector('#status');
function f(v){return Number(v).toLocaleString('en-US',{maximumFractionDigits:4});}
function draw(){const aa=Number(a.value),bb=Number(b.value);aout.textContent=f(aa);bout.textContent=f(bb); const o=OpenSTEMModels.calc(i+1,aa,bb);metric.textContent=o.metric;let mn=Math.min(...o.ys,...(o.alt||[])),mx=Math.max(...o.ys,...(o.alt||[]));if(mx===mn){mn-=1;mx+=1;}else{let m=(mx-mn)*.13;mn-=m;mx+=m;}
let x0=o.xs[0],x1=o.xs[o.xs.length-1],w=810,h=300,l=65,t=20,r=20,bt=54;let X=x=>l+(x-x0)/(x1-x0)*(w-l-r),Y=y=>t+(mx-y)/(mx-mn)*(h-t-bt),pts=y=>y.map((v,j)=>X(o.xs[j]).toFixed(2)+','+Y(v).toFixed(2)).join(' ');
svg.innerHTML='<rect x="'+l+'" y="'+t+'" width="'+(w-l-r)+'" height="'+(h-t-bt)+'" fill="#fafcff" stroke="#b5c9d9"/>';
let mk=(tag,attr,txt)=>{const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attr).forEach(([k,v])=>el.setAttribute(k,v));if(txt!==undefined)el.textContent=txt;svg.append(el);};
for(let k=0;k<=4;k++){let yy=t+k*(h-t-bt)/4;mk('line',{x1:l,y1:yy,x2:w-r,y2:yy,stroke:'#e0e9ef'});mk('text',{x:3,y:yy+5},f(mx-(mx-mn)*k/4));}
for(let k=0;k<=4;k++){let xx=l+k*(w-l-r)/4;mk('text',{x:xx-15,y:h-24},f(x0+(x1-x0)*k/4));}
mk('polyline',{points:pts(o.ys),class:'trace'});if(o.alt)mk('polyline',{points:pts(o.alt),class:'alt'});
mk('text',{x:w/2-80,y:h-2},o.xlabel);mk('text',{x:l+5,y:14},o.ylabel);
status.textContent='Recomputed for current parameters. Solid blue: model output'+(o.alt?'; dashed orange: conditional-integrator result':'')+'.';
}
a.addEventListener('input',draw);b.addEventListener('input',draw);card.querySelector('#reset').addEventListener('click',()=>{a.value=s.a.value;b.value=s.b.value;draw();});draw();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 4,
    unit: 2,
    html: "<div class=\"panel\"><span class=\"label\">Offline interactive demonstration 04/16</span><h3>Decay of a complex pole mode</h3><p><strong>Equation:</strong> e^(\u2212\u03c3t)cos(\u03c9dt)</p><p>Single ideal damped oscillatory mode, initial amplitude 1.</p><div class=\"formgrid\"><div><label for=\"a\">Decay \u03c3 (1/s): <output id=\"aout\"></output></label><input type=\"range\" id=\"a\" min=\"0.1\" max=\"5\" step=\"0.1\" value=\"1\"></div><div><label for=\"b\">Oscillation \u03c9d (rad/s): <output id=\"bout\"></output></label><input type=\"range\" id=\"b\" min=\"0.5\" max=\"15\" step=\"0.1\" value=\"6\"></div></div><div class=\"reading\">Calculated result: <span id=\"metric\" aria-live=\"polite\"></span></div><svg id=\"graph\" class=\"graph\" viewBox=\"0 0 810 300\" role=\"img\" aria-label=\"Interactive model output plotted against the horizontal axis\"></svg><p><button type=\"button\" id=\"reset\">Reset values</button> <span id=\"status\" class=\"muted\" role=\"status\"></span></p><div class=\"warn\"><b>Educational model, not equipment validation.</b> Simplifying assumptions exclude many real sensor, actuator, friction, failure and safety effects. Check parameters and physical limits before using any equation in engineering work.</div></div>",
    init: function(card) {
      try {
        card.dataset.model = String(4);
        document.body.dataset.model = String(4);
const i=Number(document.body.dataset.model)-1,s=OpenSTEMModels.specs[i],a=card.querySelector('#a'),b=card.querySelector('#b'),aout=card.querySelector('#aout'),bout=card.querySelector('#bout'),metric=card.querySelector('#metric'),svg=card.querySelector('#graph'),status=card.querySelector('#status');
function f(v){return Number(v).toLocaleString('en-US',{maximumFractionDigits:4});}
function draw(){const aa=Number(a.value),bb=Number(b.value);aout.textContent=f(aa);bout.textContent=f(bb); const o=OpenSTEMModels.calc(i+1,aa,bb);metric.textContent=o.metric;let mn=Math.min(...o.ys,...(o.alt||[])),mx=Math.max(...o.ys,...(o.alt||[]));if(mx===mn){mn-=1;mx+=1;}else{let m=(mx-mn)*.13;mn-=m;mx+=m;}
let x0=o.xs[0],x1=o.xs[o.xs.length-1],w=810,h=300,l=65,t=20,r=20,bt=54;let X=x=>l+(x-x0)/(x1-x0)*(w-l-r),Y=y=>t+(mx-y)/(mx-mn)*(h-t-bt),pts=y=>y.map((v,j)=>X(o.xs[j]).toFixed(2)+','+Y(v).toFixed(2)).join(' ');
svg.innerHTML='<rect x="'+l+'" y="'+t+'" width="'+(w-l-r)+'" height="'+(h-t-bt)+'" fill="#fafcff" stroke="#b5c9d9"/>';
let mk=(tag,attr,txt)=>{const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attr).forEach(([k,v])=>el.setAttribute(k,v));if(txt!==undefined)el.textContent=txt;svg.append(el);};
for(let k=0;k<=4;k++){let yy=t+k*(h-t-bt)/4;mk('line',{x1:l,y1:yy,x2:w-r,y2:yy,stroke:'#e0e9ef'});mk('text',{x:3,y:yy+5},f(mx-(mx-mn)*k/4));}
for(let k=0;k<=4;k++){let xx=l+k*(w-l-r)/4;mk('text',{x:xx-15,y:h-24},f(x0+(x1-x0)*k/4));}
mk('polyline',{points:pts(o.ys),class:'trace'});if(o.alt)mk('polyline',{points:pts(o.alt),class:'alt'});
mk('text',{x:w/2-80,y:h-2},o.xlabel);mk('text',{x:l+5,y:14},o.ylabel);
status.textContent='Recomputed for current parameters. Solid blue: model output'+(o.alt?'; dashed orange: conditional-integrator result':'')+'.';
}
a.addEventListener('input',draw);b.addEventListener('input',draw);card.querySelector('#reset').addEventListener('click',()=>{a.value=s.a.value;b.value=s.b.value;draw();});draw();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 5,
    unit: 3,
    html: "<div class=\"panel\"><span class=\"label\">Offline interactive demonstration 05/16</span><h3>Cubic Routh stability margin</h3><p><strong>Equation:</strong> a\u2082a\u2081\u2212a\u2080 &gt;0</p><p>For s\u00b3+a\u2082s\u00b2+5s+a\u2080; positive coefficients and margin required.</p><div class=\"formgrid\"><div><label for=\"a\">a\u2082 coefficient: <output id=\"aout\"></output></label><input type=\"range\" id=\"a\" min=\"0.2\" max=\"8\" step=\"0.1\" value=\"4\"></div><div><label for=\"b\">a\u2080 coefficient: <output id=\"bout\"></output></label><input type=\"range\" id=\"b\" min=\"0.1\" max=\"30\" step=\"0.1\" value=\"12\"></div></div><div class=\"reading\">Calculated result: <span id=\"metric\" aria-live=\"polite\"></span></div><svg id=\"graph\" class=\"graph\" viewBox=\"0 0 810 300\" role=\"img\" aria-label=\"Interactive model output plotted against the horizontal axis\"></svg><p><button type=\"button\" id=\"reset\">Reset values</button> <span id=\"status\" class=\"muted\" role=\"status\"></span></p><div class=\"warn\"><b>Educational model, not equipment validation.</b> Simplifying assumptions exclude many real sensor, actuator, friction, failure and safety effects. Check parameters and physical limits before using any equation in engineering work.</div></div>",
    init: function(card) {
      try {
        card.dataset.model = String(5);
        document.body.dataset.model = String(5);
const i=Number(document.body.dataset.model)-1,s=OpenSTEMModels.specs[i],a=card.querySelector('#a'),b=card.querySelector('#b'),aout=card.querySelector('#aout'),bout=card.querySelector('#bout'),metric=card.querySelector('#metric'),svg=card.querySelector('#graph'),status=card.querySelector('#status');
function f(v){return Number(v).toLocaleString('en-US',{maximumFractionDigits:4});}
function draw(){const aa=Number(a.value),bb=Number(b.value);aout.textContent=f(aa);bout.textContent=f(bb); const o=OpenSTEMModels.calc(i+1,aa,bb);metric.textContent=o.metric;let mn=Math.min(...o.ys,...(o.alt||[])),mx=Math.max(...o.ys,...(o.alt||[]));if(mx===mn){mn-=1;mx+=1;}else{let m=(mx-mn)*.13;mn-=m;mx+=m;}
let x0=o.xs[0],x1=o.xs[o.xs.length-1],w=810,h=300,l=65,t=20,r=20,bt=54;let X=x=>l+(x-x0)/(x1-x0)*(w-l-r),Y=y=>t+(mx-y)/(mx-mn)*(h-t-bt),pts=y=>y.map((v,j)=>X(o.xs[j]).toFixed(2)+','+Y(v).toFixed(2)).join(' ');
svg.innerHTML='<rect x="'+l+'" y="'+t+'" width="'+(w-l-r)+'" height="'+(h-t-bt)+'" fill="#fafcff" stroke="#b5c9d9"/>';
let mk=(tag,attr,txt)=>{const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attr).forEach(([k,v])=>el.setAttribute(k,v));if(txt!==undefined)el.textContent=txt;svg.append(el);};
for(let k=0;k<=4;k++){let yy=t+k*(h-t-bt)/4;mk('line',{x1:l,y1:yy,x2:w-r,y2:yy,stroke:'#e0e9ef'});mk('text',{x:3,y:yy+5},f(mx-(mx-mn)*k/4));}
for(let k=0;k<=4;k++){let xx=l+k*(w-l-r)/4;mk('text',{x:xx-15,y:h-24},f(x0+(x1-x0)*k/4));}
mk('polyline',{points:pts(o.ys),class:'trace'});if(o.alt)mk('polyline',{points:pts(o.alt),class:'alt'});
mk('text',{x:w/2-80,y:h-2},o.xlabel);mk('text',{x:l+5,y:14},o.ylabel);
status.textContent='Recomputed for current parameters. Solid blue: model output'+(o.alt?'; dashed orange: conditional-integrator result':'')+'.';
}
a.addEventListener('input',draw);b.addEventListener('input',draw);card.querySelector('#reset').addEventListener('click',()=>{a.value=s.a.value;b.value=s.b.value;draw();});draw();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 6,
    unit: 3,
    html: "<div class=\"panel\"><span class=\"label\">Offline interactive demonstration 06/16</span><h3>Proportional step-tracking error</h3><p><strong>Equation:</strong> e(t)=1\u2212y(t)</p><p>Reference is a unit step; plant 1/(\u03c4s+1).</p><div class=\"formgrid\"><div><label for=\"a\">Gain Kp: <output id=\"aout\"></output></label><input type=\"range\" id=\"a\" min=\"0.1\" max=\"12\" step=\"0.1\" value=\"3\"></div><div><label for=\"b\">Plant \u03c4 (s): <output id=\"bout\"></output></label><input type=\"range\" id=\"b\" min=\"0.2\" max=\"8\" step=\"0.1\" value=\"2\"></div></div><div class=\"reading\">Calculated result: <span id=\"metric\" aria-live=\"polite\"></span></div><svg id=\"graph\" class=\"graph\" viewBox=\"0 0 810 300\" role=\"img\" aria-label=\"Interactive model output plotted against the horizontal axis\"></svg><p><button type=\"button\" id=\"reset\">Reset values</button> <span id=\"status\" class=\"muted\" role=\"status\"></span></p><div class=\"warn\"><b>Educational model, not equipment validation.</b> Simplifying assumptions exclude many real sensor, actuator, friction, failure and safety effects. Check parameters and physical limits before using any equation in engineering work.</div></div>",
    init: function(card) {
      try {
        card.dataset.model = String(6);
        document.body.dataset.model = String(6);
const i=Number(document.body.dataset.model)-1,s=OpenSTEMModels.specs[i],a=card.querySelector('#a'),b=card.querySelector('#b'),aout=card.querySelector('#aout'),bout=card.querySelector('#bout'),metric=card.querySelector('#metric'),svg=card.querySelector('#graph'),status=card.querySelector('#status');
function f(v){return Number(v).toLocaleString('en-US',{maximumFractionDigits:4});}
function draw(){const aa=Number(a.value),bb=Number(b.value);aout.textContent=f(aa);bout.textContent=f(bb); const o=OpenSTEMModels.calc(i+1,aa,bb);metric.textContent=o.metric;let mn=Math.min(...o.ys,...(o.alt||[])),mx=Math.max(...o.ys,...(o.alt||[]));if(mx===mn){mn-=1;mx+=1;}else{let m=(mx-mn)*.13;mn-=m;mx+=m;}
let x0=o.xs[0],x1=o.xs[o.xs.length-1],w=810,h=300,l=65,t=20,r=20,bt=54;let X=x=>l+(x-x0)/(x1-x0)*(w-l-r),Y=y=>t+(mx-y)/(mx-mn)*(h-t-bt),pts=y=>y.map((v,j)=>X(o.xs[j]).toFixed(2)+','+Y(v).toFixed(2)).join(' ');
svg.innerHTML='<rect x="'+l+'" y="'+t+'" width="'+(w-l-r)+'" height="'+(h-t-bt)+'" fill="#fafcff" stroke="#b5c9d9"/>';
let mk=(tag,attr,txt)=>{const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attr).forEach(([k,v])=>el.setAttribute(k,v));if(txt!==undefined)el.textContent=txt;svg.append(el);};
for(let k=0;k<=4;k++){let yy=t+k*(h-t-bt)/4;mk('line',{x1:l,y1:yy,x2:w-r,y2:yy,stroke:'#e0e9ef'});mk('text',{x:3,y:yy+5},f(mx-(mx-mn)*k/4));}
for(let k=0;k<=4;k++){let xx=l+k*(w-l-r)/4;mk('text',{x:xx-15,y:h-24},f(x0+(x1-x0)*k/4));}
mk('polyline',{points:pts(o.ys),class:'trace'});if(o.alt)mk('polyline',{points:pts(o.alt),class:'alt'});
mk('text',{x:w/2-80,y:h-2},o.xlabel);mk('text',{x:l+5,y:14},o.ylabel);
status.textContent='Recomputed for current parameters. Solid blue: model output'+(o.alt?'; dashed orange: conditional-integrator result':'')+'.';
}
a.addEventListener('input',draw);b.addEventListener('input',draw);card.querySelector('#reset').addEventListener('click',()=>{a.value=s.a.value;b.value=s.b.value;draw();});draw();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 7,
    unit: 4,
    html: "<div class=\"panel\"><span class=\"label\">Offline interactive demonstration 07/16</span><h3>First-order Bode magnitude</h3><p><strong>Equation:</strong> 20log10[K/\u221a(1+(\u03c9\u03c4)\u00b2)]</p><p>Frequency response of K/(1+\u03c4s).</p><div class=\"formgrid\"><div><label for=\"a\">Gain K: <output id=\"aout\"></output></label><input type=\"range\" id=\"a\" min=\"0.1\" max=\"10\" step=\"0.1\" value=\"2\"></div><div><label for=\"b\">Time constant \u03c4 (s): <output id=\"bout\"></output></label><input type=\"range\" id=\"b\" min=\"0.05\" max=\"5\" step=\"0.05\" value=\"0.5\"></div></div><div class=\"reading\">Calculated result: <span id=\"metric\" aria-live=\"polite\"></span></div><svg id=\"graph\" class=\"graph\" viewBox=\"0 0 810 300\" role=\"img\" aria-label=\"Interactive model output plotted against the horizontal axis\"></svg><p><button type=\"button\" id=\"reset\">Reset values</button> <span id=\"status\" class=\"muted\" role=\"status\"></span></p><div class=\"warn\"><b>Educational model, not equipment validation.</b> Simplifying assumptions exclude many real sensor, actuator, friction, failure and safety effects. Check parameters and physical limits before using any equation in engineering work.</div></div>",
    init: function(card) {
      try {
        card.dataset.model = String(7);
        document.body.dataset.model = String(7);
const i=Number(document.body.dataset.model)-1,s=OpenSTEMModels.specs[i],a=card.querySelector('#a'),b=card.querySelector('#b'),aout=card.querySelector('#aout'),bout=card.querySelector('#bout'),metric=card.querySelector('#metric'),svg=card.querySelector('#graph'),status=card.querySelector('#status');
function f(v){return Number(v).toLocaleString('en-US',{maximumFractionDigits:4});}
function draw(){const aa=Number(a.value),bb=Number(b.value);aout.textContent=f(aa);bout.textContent=f(bb); const o=OpenSTEMModels.calc(i+1,aa,bb);metric.textContent=o.metric;let mn=Math.min(...o.ys,...(o.alt||[])),mx=Math.max(...o.ys,...(o.alt||[]));if(mx===mn){mn-=1;mx+=1;}else{let m=(mx-mn)*.13;mn-=m;mx+=m;}
let x0=o.xs[0],x1=o.xs[o.xs.length-1],w=810,h=300,l=65,t=20,r=20,bt=54;let X=x=>l+(x-x0)/(x1-x0)*(w-l-r),Y=y=>t+(mx-y)/(mx-mn)*(h-t-bt),pts=y=>y.map((v,j)=>X(o.xs[j]).toFixed(2)+','+Y(v).toFixed(2)).join(' ');
svg.innerHTML='<rect x="'+l+'" y="'+t+'" width="'+(w-l-r)+'" height="'+(h-t-bt)+'" fill="#fafcff" stroke="#b5c9d9"/>';
let mk=(tag,attr,txt)=>{const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attr).forEach(([k,v])=>el.setAttribute(k,v));if(txt!==undefined)el.textContent=txt;svg.append(el);};
for(let k=0;k<=4;k++){let yy=t+k*(h-t-bt)/4;mk('line',{x1:l,y1:yy,x2:w-r,y2:yy,stroke:'#e0e9ef'});mk('text',{x:3,y:yy+5},f(mx-(mx-mn)*k/4));}
for(let k=0;k<=4;k++){let xx=l+k*(w-l-r)/4;mk('text',{x:xx-15,y:h-24},f(x0+(x1-x0)*k/4));}
mk('polyline',{points:pts(o.ys),class:'trace'});if(o.alt)mk('polyline',{points:pts(o.alt),class:'alt'});
mk('text',{x:w/2-80,y:h-2},o.xlabel);mk('text',{x:l+5,y:14},o.ylabel);
status.textContent='Recomputed for current parameters. Solid blue: model output'+(o.alt?'; dashed orange: conditional-integrator result':'')+'.';
}
a.addEventListener('input',draw);b.addEventListener('input',draw);card.querySelector('#reset').addEventListener('click',()=>{a.value=s.a.value;b.value=s.b.value;draw();});draw();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 8,
    unit: 4,
    html: "<div class=\"panel\"><span class=\"label\">Offline interactive demonstration 08/16</span><h3>Lag from a pole and transport delay</h3><p><strong>Equation:</strong> Phase=\u2212atan(\u03c9\u03c4)\u2212\u03c9L</p><p>Unwrapped continuous phase of e^(\u2212Ls)/(1+\u03c4s).</p><div class=\"formgrid\"><div><label for=\"a\">Delay L (s): <output id=\"aout\"></output></label><input type=\"range\" id=\"a\" min=\"0\" max=\"1\" step=\"0.01\" value=\"0.12\"></div><div><label for=\"b\">Time constant \u03c4 (s): <output id=\"bout\"></output></label><input type=\"range\" id=\"b\" min=\"0.05\" max=\"2\" step=\"0.05\" value=\"0.5\"></div></div><div class=\"reading\">Calculated result: <span id=\"metric\" aria-live=\"polite\"></span></div><svg id=\"graph\" class=\"graph\" viewBox=\"0 0 810 300\" role=\"img\" aria-label=\"Interactive model output plotted against the horizontal axis\"></svg><p><button type=\"button\" id=\"reset\">Reset values</button> <span id=\"status\" class=\"muted\" role=\"status\"></span></p><div class=\"warn\"><b>Educational model, not equipment validation.</b> Simplifying assumptions exclude many real sensor, actuator, friction, failure and safety effects. Check parameters and physical limits before using any equation in engineering work.</div></div>",
    init: function(card) {
      try {
        card.dataset.model = String(8);
        document.body.dataset.model = String(8);
const i=Number(document.body.dataset.model)-1,s=OpenSTEMModels.specs[i],a=card.querySelector('#a'),b=card.querySelector('#b'),aout=card.querySelector('#aout'),bout=card.querySelector('#bout'),metric=card.querySelector('#metric'),svg=card.querySelector('#graph'),status=card.querySelector('#status');
function f(v){return Number(v).toLocaleString('en-US',{maximumFractionDigits:4});}
function draw(){const aa=Number(a.value),bb=Number(b.value);aout.textContent=f(aa);bout.textContent=f(bb); const o=OpenSTEMModels.calc(i+1,aa,bb);metric.textContent=o.metric;let mn=Math.min(...o.ys,...(o.alt||[])),mx=Math.max(...o.ys,...(o.alt||[]));if(mx===mn){mn-=1;mx+=1;}else{let m=(mx-mn)*.13;mn-=m;mx+=m;}
let x0=o.xs[0],x1=o.xs[o.xs.length-1],w=810,h=300,l=65,t=20,r=20,bt=54;let X=x=>l+(x-x0)/(x1-x0)*(w-l-r),Y=y=>t+(mx-y)/(mx-mn)*(h-t-bt),pts=y=>y.map((v,j)=>X(o.xs[j]).toFixed(2)+','+Y(v).toFixed(2)).join(' ');
svg.innerHTML='<rect x="'+l+'" y="'+t+'" width="'+(w-l-r)+'" height="'+(h-t-bt)+'" fill="#fafcff" stroke="#b5c9d9"/>';
let mk=(tag,attr,txt)=>{const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attr).forEach(([k,v])=>el.setAttribute(k,v));if(txt!==undefined)el.textContent=txt;svg.append(el);};
for(let k=0;k<=4;k++){let yy=t+k*(h-t-bt)/4;mk('line',{x1:l,y1:yy,x2:w-r,y2:yy,stroke:'#e0e9ef'});mk('text',{x:3,y:yy+5},f(mx-(mx-mn)*k/4));}
for(let k=0;k<=4;k++){let xx=l+k*(w-l-r)/4;mk('text',{x:xx-15,y:h-24},f(x0+(x1-x0)*k/4));}
mk('polyline',{points:pts(o.ys),class:'trace'});if(o.alt)mk('polyline',{points:pts(o.alt),class:'alt'});
mk('text',{x:w/2-80,y:h-2},o.xlabel);mk('text',{x:l+5,y:14},o.ylabel);
status.textContent='Recomputed for current parameters. Solid blue: model output'+(o.alt?'; dashed orange: conditional-integrator result':'')+'.';
}
a.addEventListener('input',draw);b.addEventListener('input',draw);card.querySelector('#reset').addEventListener('click',()=>{a.value=s.a.value;b.value=s.b.value;draw();});draw();
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 9,
    unit: 5,
    html: "<div class=\"panel\"><span class=\"label\">Offline interactive demonstration 09/16</span><h3>PI loop step response</h3><p><strong>Equation:</strong> u=Kp e+Ki\u222be dt</p><p>Ideal unit-gain first-order plant \u03c4=2 s; numerical integration with no saturation.</p><div class=\"formgrid\"><div><label for=\"a\">Gain Kp: <output id=\"aout\"></output></label><input type=\"range\" id=\"a\" min=\"0.1\" max=\"5\" step=\"0.1\" value=\"1.5\"></div><div><label for=\"b\">Integral gain Ki (1/s): <output id=\"bout\"></output></label><input type=\"range\" id=\"b\" min=\"0.05\" max=\"3\" step=\"0.05\" value=\"0.5\"></div></div><div class=\"reading\">Calculated result: <span id=\"metric\" aria-live=\"polite\"></span></div><svg id=\"graph\" class=\"graph\" viewBox=\"0 0 810 300\" role=\"img\" aria-label=\"Interactive model output plotted against the horizontal axis\"></svg><p><button type=\"button\" id=\"reset\">Reset values</button> <span id=\"status\" class=\"muted\" role=\"status\"></span></p><div class=\"warn\"><b>Educational model, not equipment validation.</b> Simplifying assumptions exclude many real sensor, actuator, friction, failure and safety effects. Check parameters and physical limits before using any equation in engineering work.</div></div>",
    init: function(card) {
      try {
        card.dataset.model = String(9);
        document.body.dataset.model = String(9);
const i=Number(document.body.dataset.model)-1,s=OpenSTEMModels.specs[i],a=card.querySelector('#a'),b=card.querySelector('#b'),aout=card.querySelector('#aout'),bout=card.querySelector('#bout'),metric=card.querySelector('#metric'),svg=card.querySelector('#graph'),status=card.querySelector('#status');
function f(v){return Number(v).toLocaleString('en-US',{maximumFractionDigits:4});}
function draw(){const aa=Number(a.value),bb=Number(b.value);aout.textContent=f(aa);bout.textContent=f(bb); const o=OpenSTEMModels.calc(i+1,aa,bb);metric.textContent=o.metric;let mn=Math.min(...o.ys,...(o.alt||[])),mx=Math.max(...o.ys,...(o.alt||[]));if(mx===mn){mn-=1;mx+=1;}else{let m=(mx-mn)*.13;mn-=m;mx+=m;}
let x0=o.xs[0],x1=o.xs[o.xs.length-1],w=810,h=300,l=65,t=20,r=20,bt=54;let X=x=>l+(x-x0)/(x1-x0)*(w-l-r),Y=y=>t+(mx-y)/(mx-mn)*(h-t-bt),pts=y=>y.map((v,j)=>X(o.xs[j]).toFixed(2)+','+Y(v).toFixed(2)).join(' ');
svg.innerHTML='<rect x="'+l+'" y="'+t+'" width="'+(w-l-r)+'" height="'+(h-t-bt)+'" fill="#fafcff" stroke="#b5c9d9"/>';
let mk=(tag,attr,txt)=>{const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attr).forEach(([k,v])=>el.setAttribute(k,v));if(txt!==undefined)el.textContent=txt;svg.append(el);};
for(let k=0;k<=4;k++){let yy=t+k*(h-t-bt)/4;mk('line',{x1:l,y1:yy,x2:w-r,y2:yy,stroke:'#e0e9ef'});mk('text',{x:3,y:yy+5},f(mx-(mx-mn)*k/4));}
for(let k=0;k<=4;k++){let xx=l+k*(w-l-r)/4;mk('text',{x:xx-15,y:h-24},f(x0+(x1-x0)*k/4));}
mk('polyline',{points:pts(o.ys),class:'trace'});if(o.alt)mk('polyline',{points:pts(o.alt),class:'alt'});
mk('text',{x:w/2-80,y:h-2},o.xlabel);mk('text',{x:l+5,y:14},o.ylabel);
status.textContent='Recomputed for current parameters. Solid blue: model output'+(o.alt?'; dashed orange: conditional-integrator result':'')+'.';
}
a.addEventListener('input',draw);b.addEventListener('input',draw);card.querySelector('#reset').addEventListener('click',()=>{a.value=s.a.value;b.value=s.b.value;draw();});draw();
      } catch (err) {
        console.warn('Sim init error in model 9:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 10,
    unit: 5,
    html: "<div class=\"panel\"><span class=\"label\">Offline interactive demonstration 10/16</span><h3>Lead-network phase contribution</h3><p><strong>Equation:</strong> atan(\u03c9T)\u2212atan(\u03b1\u03c9T)</p><p>Lead C(s)=(1+sT)/(1+s\u03b1T), 0&lt;\u03b1&lt;1.</p><div class=\"formgrid\"><div><label for=\"a\">Lead ratio \u03b1: <output id=\"aout\"></output></label><input type=\"range\" id=\"a\" min=\"0.05\" max=\"0.95\" step=\"0.05\" value=\"0.25\"></div><div><label for=\"b\">Zero constant T (s): <output id=\"bout\"></output></label><input type=\"range\" id=\"b\" min=\"0.1\" max=\"5\" step=\"0.1\" value=\"1\"></div></div><div class=\"reading\">Calculated result: <span id=\"metric\" aria-live=\"polite\"></span></div><svg id=\"graph\" class=\"graph\" viewBox=\"0 0 810 300\" role=\"img\" aria-label=\"Interactive model output plotted against the horizontal axis\"></svg><p><button type=\"button\" id=\"reset\">Reset values</button> <span id=\"status\" class=\"muted\" role=\"status\"></span></p><div class=\"warn\"><b>Educational model, not equipment validation.</b> Simplifying assumptions exclude many real sensor, actuator, friction, failure and safety effects. Check parameters and physical limits before using any equation in engineering work.</div></div>",
    init: function(card) {
      try {
        card.dataset.model = String(10);
        document.body.dataset.model = String(10);
const i=Number(document.body.dataset.model)-1,s=OpenSTEMModels.specs[i],a=card.querySelector('#a'),b=card.querySelector('#b'),aout=card.querySelector('#aout'),bout=card.querySelector('#bout'),metric=card.querySelector('#metric'),svg=card.querySelector('#graph'),status=card.querySelector('#status');
function f(v){return Number(v).toLocaleString('en-US',{maximumFractionDigits:4});}
function draw(){const aa=Number(a.value),bb=Number(b.value);aout.textContent=f(aa);bout.textContent=f(bb); const o=OpenSTEMModels.calc(i+1,aa,bb);metric.textContent=o.metric;let mn=Math.min(...o.ys,...(o.alt||[])),mx=Math.max(...o.ys,...(o.alt||[]));if(mx===mn){mn-=1;mx+=1;}else{let m=(mx-mn)*.13;mn-=m;mx+=m;}
let x0=o.xs[0],x1=o.xs[o.xs.length-1],w=810,h=300,l=65,t=20,r=20,bt=54;let X=x=>l+(x-x0)/(x1-x0)*(w-l-r),Y=y=>t+(mx-y)/(mx-mn)*(h-t-bt),pts=y=>y.map((v,j)=>X(o.xs[j]).toFixed(2)+','+Y(v).toFixed(2)).join(' ');
svg.innerHTML='<rect x="'+l+'" y="'+t+'" width="'+(w-l-r)+'" height="'+(h-t-bt)+'" fill="#fafcff" stroke="#b5c9d9"/>';
let mk=(tag,attr,txt)=>{const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attr).forEach(([k,v])=>el.setAttribute(k,v));if(txt!==undefined)el.textContent=txt;svg.append(el);};
for(let k=0;k<=4;k++){let yy=t+k*(h-t-bt)/4;mk('line',{x1:l,y1:yy,x2:w-r,y2:yy,stroke:'#e0e9ef'});mk('text',{x:3,y:yy+5},f(mx-(mx-mn)*k/4));}
for(let k=0;k<=4;k++){let xx=l+k*(w-l-r)/4;mk('text',{x:xx-15,y:h-24},f(x0+(x1-x0)*k/4));}
mk('polyline',{points:pts(o.ys),class:'trace'});if(o.alt)mk('polyline',{points:pts(o.alt),class:'alt'});
mk('text',{x:w/2-80,y:h-2},o.xlabel);mk('text',{x:l+5,y:14},o.ylabel);
status.textContent='Recomputed for current parameters. Solid blue: model output'+(o.alt?'; dashed orange: conditional-integrator result':'')+'.';
}
a.addEventListener('input',draw);b.addEventListener('input',draw);card.querySelector('#reset').addEventListener('click',()=>{a.value=s.a.value;b.value=s.b.value;draw();});draw();
      } catch (err) {
        console.warn('Sim init error in model 10:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 11,
    unit: 6,
    html: "<div class=\"panel\"><span class=\"label\">Offline interactive demonstration 11/16</span><h3>Double-integrator state-feedback decay</h3><p><strong>Equation:</strong> x\u0308+k\u2082x\u0307+k\u2081x=0</p><p>Initial x=1 m and velocity zero; ideal force-to-acceleration plant.</p><div class=\"formgrid\"><div><label for=\"a\">Position gain k1 (1/s\u00b2): <output id=\"aout\"></output></label><input type=\"range\" id=\"a\" min=\"0.5\" max=\"25\" step=\"0.5\" value=\"6\"></div><div><label for=\"b\">Velocity gain k2 (1/s): <output id=\"bout\"></output></label><input type=\"range\" id=\"b\" min=\"0.5\" max=\"12\" step=\"0.5\" value=\"5\"></div></div><div class=\"reading\">Calculated result: <span id=\"metric\" aria-live=\"polite\"></span></div><svg id=\"graph\" class=\"graph\" viewBox=\"0 0 810 300\" role=\"img\" aria-label=\"Interactive model output plotted against the horizontal axis\"></svg><p><button type=\"button\" id=\"reset\">Reset values</button> <span id=\"status\" class=\"muted\" role=\"status\"></span></p><div class=\"warn\"><b>Educational model, not equipment validation.</b> Simplifying assumptions exclude many real sensor, actuator, friction, failure and safety effects. Check parameters and physical limits before using any equation in engineering work.</div></div>",
    init: function(card) {
      try {
        card.dataset.model = String(11);
        document.body.dataset.model = String(11);
const i=Number(document.body.dataset.model)-1,s=OpenSTEMModels.specs[i],a=card.querySelector('#a'),b=card.querySelector('#b'),aout=card.querySelector('#aout'),bout=card.querySelector('#bout'),metric=card.querySelector('#metric'),svg=card.querySelector('#graph'),status=card.querySelector('#status');
function f(v){return Number(v).toLocaleString('en-US',{maximumFractionDigits:4});}
function draw(){const aa=Number(a.value),bb=Number(b.value);aout.textContent=f(aa);bout.textContent=f(bb); const o=OpenSTEMModels.calc(i+1,aa,bb);metric.textContent=o.metric;let mn=Math.min(...o.ys,...(o.alt||[])),mx=Math.max(...o.ys,...(o.alt||[]));if(mx===mn){mn-=1;mx+=1;}else{let m=(mx-mn)*.13;mn-=m;mx+=m;}
let x0=o.xs[0],x1=o.xs[o.xs.length-1],w=810,h=300,l=65,t=20,r=20,bt=54;let X=x=>l+(x-x0)/(x1-x0)*(w-l-r),Y=y=>t+(mx-y)/(mx-mn)*(h-t-bt),pts=y=>y.map((v,j)=>X(o.xs[j]).toFixed(2)+','+Y(v).toFixed(2)).join(' ');
svg.innerHTML='<rect x="'+l+'" y="'+t+'" width="'+(w-l-r)+'" height="'+(h-t-bt)+'" fill="#fafcff" stroke="#b5c9d9"/>';
let mk=(tag,attr,txt)=>{const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attr).forEach(([k,v])=>el.setAttribute(k,v));if(txt!==undefined)el.textContent=txt;svg.append(el);};
for(let k=0;k<=4;k++){let yy=t+k*(h-t-bt)/4;mk('line',{x1:l,y1:yy,x2:w-r,y2:yy,stroke:'#e0e9ef'});mk('text',{x:3,y:yy+5},f(mx-(mx-mn)*k/4));}
for(let k=0;k<=4;k++){let xx=l+k*(w-l-r)/4;mk('text',{x:xx-15,y:h-24},f(x0+(x1-x0)*k/4));}
mk('polyline',{points:pts(o.ys),class:'trace'});if(o.alt)mk('polyline',{points:pts(o.alt),class:'alt'});
mk('text',{x:w/2-80,y:h-2},o.xlabel);mk('text',{x:l+5,y:14},o.ylabel);
status.textContent='Recomputed for current parameters. Solid blue: model output'+(o.alt?'; dashed orange: conditional-integrator result':'')+'.';
}
a.addEventListener('input',draw);b.addEventListener('input',draw);card.querySelector('#reset').addEventListener('click',()=>{a.value=s.a.value;b.value=s.b.value;draw();});draw();
      } catch (err) {
        console.warn('Sim init error in model 11:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 12,
    unit: 6,
    html: "<div class=\"panel\"><span class=\"label\">Offline interactive demonstration 12/16</span><h3>State observer estimation error</h3><p><strong>Equation:</strong> e(t)=e\u2080exp[\u2212(2+L)t]</p><p>Scalar plant x\u0307=\u22122x+u, sensor y=x; no bias or model mismatch.</p><div class=\"formgrid\"><div><label for=\"a\">Observer gain L (1/s): <output id=\"aout\"></output></label><input type=\"range\" id=\"a\" min=\"0\" max=\"20\" step=\"0.5\" value=\"4\"></div><div><label for=\"b\">Initial estimation error e0: <output id=\"bout\"></output></label><input type=\"range\" id=\"b\" min=\"0.1\" max=\"5\" step=\"0.1\" value=\"1\"></div></div><div class=\"reading\">Calculated result: <span id=\"metric\" aria-live=\"polite\"></span></div><svg id=\"graph\" class=\"graph\" viewBox=\"0 0 810 300\" role=\"img\" aria-label=\"Interactive model output plotted against the horizontal axis\"></svg><p><button type=\"button\" id=\"reset\">Reset values</button> <span id=\"status\" class=\"muted\" role=\"status\"></span></p><div class=\"warn\"><b>Educational model, not equipment validation.</b> Simplifying assumptions exclude many real sensor, actuator, friction, failure and safety effects. Check parameters and physical limits before using any equation in engineering work.</div></div>",
    init: function(card) {
      try {
        card.dataset.model = String(12);
        document.body.dataset.model = String(12);
const i=Number(document.body.dataset.model)-1,s=OpenSTEMModels.specs[i],a=card.querySelector('#a'),b=card.querySelector('#b'),aout=card.querySelector('#aout'),bout=card.querySelector('#bout'),metric=card.querySelector('#metric'),svg=card.querySelector('#graph'),status=card.querySelector('#status');
function f(v){return Number(v).toLocaleString('en-US',{maximumFractionDigits:4});}
function draw(){const aa=Number(a.value),bb=Number(b.value);aout.textContent=f(aa);bout.textContent=f(bb); const o=OpenSTEMModels.calc(i+1,aa,bb);metric.textContent=o.metric;let mn=Math.min(...o.ys,...(o.alt||[])),mx=Math.max(...o.ys,...(o.alt||[]));if(mx===mn){mn-=1;mx+=1;}else{let m=(mx-mn)*.13;mn-=m;mx+=m;}
let x0=o.xs[0],x1=o.xs[o.xs.length-1],w=810,h=300,l=65,t=20,r=20,bt=54;let X=x=>l+(x-x0)/(x1-x0)*(w-l-r),Y=y=>t+(mx-y)/(mx-mn)*(h-t-bt),pts=y=>y.map((v,j)=>X(o.xs[j]).toFixed(2)+','+Y(v).toFixed(2)).join(' ');
svg.innerHTML='<rect x="'+l+'" y="'+t+'" width="'+(w-l-r)+'" height="'+(h-t-bt)+'" fill="#fafcff" stroke="#b5c9d9"/>';
let mk=(tag,attr,txt)=>{const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attr).forEach(([k,v])=>el.setAttribute(k,v));if(txt!==undefined)el.textContent=txt;svg.append(el);};
for(let k=0;k<=4;k++){let yy=t+k*(h-t-bt)/4;mk('line',{x1:l,y1:yy,x2:w-r,y2:yy,stroke:'#e0e9ef'});mk('text',{x:3,y:yy+5},f(mx-(mx-mn)*k/4));}
for(let k=0;k<=4;k++){let xx=l+k*(w-l-r)/4;mk('text',{x:xx-15,y:h-24},f(x0+(x1-x0)*k/4));}
mk('polyline',{points:pts(o.ys),class:'trace'});if(o.alt)mk('polyline',{points:pts(o.alt),class:'alt'});
mk('text',{x:w/2-80,y:h-2},o.xlabel);mk('text',{x:l+5,y:14},o.ylabel);
status.textContent='Recomputed for current parameters. Solid blue: model output'+(o.alt?'; dashed orange: conditional-integrator result':'')+'.';
}
a.addEventListener('input',draw);b.addEventListener('input',draw);card.querySelector('#reset').addEventListener('click',()=>{a.value=s.a.value;b.value=s.b.value;draw();});draw();
      } catch (err) {
        console.warn('Sim init error in model 12:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 13,
    unit: 7,
    html: "<div class=\"panel\"><span class=\"label\">Offline interactive demonstration 13/16</span><h3>Exact sampled first-order system</h3><p><strong>Equation:</strong> x[k+1]=ax[k]+(1\u2212a)u[k]</p><p>Unit-step command; exact zero-order-hold discretization.</p><div class=\"formgrid\"><div><label for=\"a\">Sample interval h (s): <output id=\"aout\"></output></label><input type=\"range\" id=\"a\" min=\"0.05\" max=\"3\" step=\"0.05\" value=\"0.5\"></div><div><label for=\"b\">Time constant \u03c4 (s): <output id=\"bout\"></output></label><input type=\"range\" id=\"b\" min=\"0.4\" max=\"5\" step=\"0.1\" value=\"2\"></div></div><div class=\"reading\">Calculated result: <span id=\"metric\" aria-live=\"polite\"></span></div><svg id=\"graph\" class=\"graph\" viewBox=\"0 0 810 300\" role=\"img\" aria-label=\"Interactive model output plotted against the horizontal axis\"></svg><p><button type=\"button\" id=\"reset\">Reset values</button> <span id=\"status\" class=\"muted\" role=\"status\"></span></p><div class=\"warn\"><b>Educational model, not equipment validation.</b> Simplifying assumptions exclude many real sensor, actuator, friction, failure and safety effects. Check parameters and physical limits before using any equation in engineering work.</div></div>",
    init: function(card) {
      try {
        card.dataset.model = String(13);
        document.body.dataset.model = String(13);
const i=Number(document.body.dataset.model)-1,s=OpenSTEMModels.specs[i],a=card.querySelector('#a'),b=card.querySelector('#b'),aout=card.querySelector('#aout'),bout=card.querySelector('#bout'),metric=card.querySelector('#metric'),svg=card.querySelector('#graph'),status=card.querySelector('#status');
function f(v){return Number(v).toLocaleString('en-US',{maximumFractionDigits:4});}
function draw(){const aa=Number(a.value),bb=Number(b.value);aout.textContent=f(aa);bout.textContent=f(bb); const o=OpenSTEMModels.calc(i+1,aa,bb);metric.textContent=o.metric;let mn=Math.min(...o.ys,...(o.alt||[])),mx=Math.max(...o.ys,...(o.alt||[]));if(mx===mn){mn-=1;mx+=1;}else{let m=(mx-mn)*.13;mn-=m;mx+=m;}
let x0=o.xs[0],x1=o.xs[o.xs.length-1],w=810,h=300,l=65,t=20,r=20,bt=54;let X=x=>l+(x-x0)/(x1-x0)*(w-l-r),Y=y=>t+(mx-y)/(mx-mn)*(h-t-bt),pts=y=>y.map((v,j)=>X(o.xs[j]).toFixed(2)+','+Y(v).toFixed(2)).join(' ');
svg.innerHTML='<rect x="'+l+'" y="'+t+'" width="'+(w-l-r)+'" height="'+(h-t-bt)+'" fill="#fafcff" stroke="#b5c9d9"/>';
let mk=(tag,attr,txt)=>{const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attr).forEach(([k,v])=>el.setAttribute(k,v));if(txt!==undefined)el.textContent=txt;svg.append(el);};
for(let k=0;k<=4;k++){let yy=t+k*(h-t-bt)/4;mk('line',{x1:l,y1:yy,x2:w-r,y2:yy,stroke:'#e0e9ef'});mk('text',{x:3,y:yy+5},f(mx-(mx-mn)*k/4));}
for(let k=0;k<=4;k++){let xx=l+k*(w-l-r)/4;mk('text',{x:xx-15,y:h-24},f(x0+(x1-x0)*k/4));}
mk('polyline',{points:pts(o.ys),class:'trace'});if(o.alt)mk('polyline',{points:pts(o.alt),class:'alt'});
mk('text',{x:w/2-80,y:h-2},o.xlabel);mk('text',{x:l+5,y:14},o.ylabel);
status.textContent='Recomputed for current parameters. Solid blue: model output'+(o.alt?'; dashed orange: conditional-integrator result':'')+'.';
}
a.addEventListener('input',draw);b.addEventListener('input',draw);card.querySelector('#reset').addEventListener('click',()=>{a.value=s.a.value;b.value=s.b.value;draw();});draw();
      } catch (err) {
        console.warn('Sim init error in model 13:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 14,
    unit: 7,
    html: "<div class=\"panel\"><span class=\"label\">Offline interactive demonstration 14/16</span><h3>Aliasing in sampled measurements</h3><p><strong>Equation:</strong> falias=|f\u2212round(f/fs)fs|</p><p>Samples of unit-amplitude sinusoid, no anti-alias filter.</p><div class=\"formgrid\"><div><label for=\"a\">Signal frequency f (Hz): <output id=\"aout\"></output></label><input type=\"range\" id=\"a\" min=\"0.5\" max=\"40\" step=\"0.5\" value=\"12\"></div><div><label for=\"b\">Sample frequency fs (Hz): <output id=\"bout\"></output></label><input type=\"range\" id=\"b\" min=\"5\" max=\"50\" step=\"1\" value=\"20\"></div></div><div class=\"reading\">Calculated result: <span id=\"metric\" aria-live=\"polite\"></span></div><svg id=\"graph\" class=\"graph\" viewBox=\"0 0 810 300\" role=\"img\" aria-label=\"Interactive model output plotted against the horizontal axis\"></svg><p><button type=\"button\" id=\"reset\">Reset values</button> <span id=\"status\" class=\"muted\" role=\"status\"></span></p><div class=\"warn\"><b>Educational model, not equipment validation.</b> Simplifying assumptions exclude many real sensor, actuator, friction, failure and safety effects. Check parameters and physical limits before using any equation in engineering work.</div></div>",
    init: function(card) {
      try {
        card.dataset.model = String(14);
        document.body.dataset.model = String(14);
const i=Number(document.body.dataset.model)-1,s=OpenSTEMModels.specs[i],a=card.querySelector('#a'),b=card.querySelector('#b'),aout=card.querySelector('#aout'),bout=card.querySelector('#bout'),metric=card.querySelector('#metric'),svg=card.querySelector('#graph'),status=card.querySelector('#status');
function f(v){return Number(v).toLocaleString('en-US',{maximumFractionDigits:4});}
function draw(){const aa=Number(a.value),bb=Number(b.value);aout.textContent=f(aa);bout.textContent=f(bb); const o=OpenSTEMModels.calc(i+1,aa,bb);metric.textContent=o.metric;let mn=Math.min(...o.ys,...(o.alt||[])),mx=Math.max(...o.ys,...(o.alt||[]));if(mx===mn){mn-=1;mx+=1;}else{let m=(mx-mn)*.13;mn-=m;mx+=m;}
let x0=o.xs[0],x1=o.xs[o.xs.length-1],w=810,h=300,l=65,t=20,r=20,bt=54;let X=x=>l+(x-x0)/(x1-x0)*(w-l-r),Y=y=>t+(mx-y)/(mx-mn)*(h-t-bt),pts=y=>y.map((v,j)=>X(o.xs[j]).toFixed(2)+','+Y(v).toFixed(2)).join(' ');
svg.innerHTML='<rect x="'+l+'" y="'+t+'" width="'+(w-l-r)+'" height="'+(h-t-bt)+'" fill="#fafcff" stroke="#b5c9d9"/>';
let mk=(tag,attr,txt)=>{const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attr).forEach(([k,v])=>el.setAttribute(k,v));if(txt!==undefined)el.textContent=txt;svg.append(el);};
for(let k=0;k<=4;k++){let yy=t+k*(h-t-bt)/4;mk('line',{x1:l,y1:yy,x2:w-r,y2:yy,stroke:'#e0e9ef'});mk('text',{x:3,y:yy+5},f(mx-(mx-mn)*k/4));}
for(let k=0;k<=4;k++){let xx=l+k*(w-l-r)/4;mk('text',{x:xx-15,y:h-24},f(x0+(x1-x0)*k/4));}
mk('polyline',{points:pts(o.ys),class:'trace'});if(o.alt)mk('polyline',{points:pts(o.alt),class:'alt'});
mk('text',{x:w/2-80,y:h-2},o.xlabel);mk('text',{x:l+5,y:14},o.ylabel);
status.textContent='Recomputed for current parameters. Solid blue: model output'+(o.alt?'; dashed orange: conditional-integrator result':'')+'.';
}
a.addEventListener('input',draw);b.addEventListener('input',draw);card.querySelector('#reset').addEventListener('click',()=>{a.value=s.a.value;b.value=s.b.value;draw();});draw();
      } catch (err) {
        console.warn('Sim init error in model 14:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 15,
    unit: 8,
    html: "<div class=\"panel\"><span class=\"label\">Offline interactive demonstration 15/16</span><h3>PI saturation and anti-windup comparison</h3><p><strong>Equation:</strong> u=sat(Kp e+I)</p><p>Reference 1.5 before 10 s, then 0.4; max actuator 1. Two traces: ordinary and conditional-integrator PI.</p><div class=\"formgrid\"><div><label for=\"a\">Proportional gain Kp: <output id=\"aout\"></output></label><input type=\"range\" id=\"a\" min=\"0.2\" max=\"5\" step=\"0.1\" value=\"2\"></div><div><label for=\"b\">Integral gain Ki (1/s): <output id=\"bout\"></output></label><input type=\"range\" id=\"b\" min=\"0.05\" max=\"3\" step=\"0.05\" value=\"0.5\"></div></div><div class=\"reading\">Calculated result: <span id=\"metric\" aria-live=\"polite\"></span></div><svg id=\"graph\" class=\"graph\" viewBox=\"0 0 810 300\" role=\"img\" aria-label=\"Interactive model output plotted against the horizontal axis\"></svg><p><button type=\"button\" id=\"reset\">Reset values</button> <span id=\"status\" class=\"muted\" role=\"status\"></span></p><div class=\"warn\"><b>Educational model, not equipment validation.</b> Simplifying assumptions exclude many real sensor, actuator, friction, failure and safety effects. Check parameters and physical limits before using any equation in engineering work.</div></div>",
    init: function(card) {
      try {
        card.dataset.model = String(15);
        document.body.dataset.model = String(15);
const i=Number(document.body.dataset.model)-1,s=OpenSTEMModels.specs[i],a=card.querySelector('#a'),b=card.querySelector('#b'),aout=card.querySelector('#aout'),bout=card.querySelector('#bout'),metric=card.querySelector('#metric'),svg=card.querySelector('#graph'),status=card.querySelector('#status');
function f(v){return Number(v).toLocaleString('en-US',{maximumFractionDigits:4});}
function draw(){const aa=Number(a.value),bb=Number(b.value);aout.textContent=f(aa);bout.textContent=f(bb); const o=OpenSTEMModels.calc(i+1,aa,bb);metric.textContent=o.metric;let mn=Math.min(...o.ys,...(o.alt||[])),mx=Math.max(...o.ys,...(o.alt||[]));if(mx===mn){mn-=1;mx+=1;}else{let m=(mx-mn)*.13;mn-=m;mx+=m;}
let x0=o.xs[0],x1=o.xs[o.xs.length-1],w=810,h=300,l=65,t=20,r=20,bt=54;let X=x=>l+(x-x0)/(x1-x0)*(w-l-r),Y=y=>t+(mx-y)/(mx-mn)*(h-t-bt),pts=y=>y.map((v,j)=>X(o.xs[j]).toFixed(2)+','+Y(v).toFixed(2)).join(' ');
svg.innerHTML='<rect x="'+l+'" y="'+t+'" width="'+(w-l-r)+'" height="'+(h-t-bt)+'" fill="#fafcff" stroke="#b5c9d9"/>';
let mk=(tag,attr,txt)=>{const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attr).forEach(([k,v])=>el.setAttribute(k,v));if(txt!==undefined)el.textContent=txt;svg.append(el);};
for(let k=0;k<=4;k++){let yy=t+k*(h-t-bt)/4;mk('line',{x1:l,y1:yy,x2:w-r,y2:yy,stroke:'#e0e9ef'});mk('text',{x:3,y:yy+5},f(mx-(mx-mn)*k/4));}
for(let k=0;k<=4;k++){let xx=l+k*(w-l-r)/4;mk('text',{x:xx-15,y:h-24},f(x0+(x1-x0)*k/4));}
mk('polyline',{points:pts(o.ys),class:'trace'});if(o.alt)mk('polyline',{points:pts(o.alt),class:'alt'});
mk('text',{x:w/2-80,y:h-2},o.xlabel);mk('text',{x:l+5,y:14},o.ylabel);
status.textContent='Recomputed for current parameters. Solid blue: model output'+(o.alt?'; dashed orange: conditional-integrator result':'')+'.';
}
a.addEventListener('input',draw);b.addEventListener('input',draw);card.querySelector('#reset').addEventListener('click',()=>{a.value=s.a.value;b.value=s.b.value;draw();});draw();
      } catch (err) {
        console.warn('Sim init error in model 15:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 16,
    unit: 8,
    html: "<div class=\"panel\"><span class=\"label\">Offline interactive demonstration 16/16</span><h3>Lumped thermal step response</h3><p><strong>Equation:</strong> \u0394T=P/(hA)(1\u2212e^(\u2212hAt/Cth))</p><p>Constant heater input, Cth=1000 J/K, linearized losses.</p><div class=\"formgrid\"><div><label for=\"a\">Heater power P (W): <output id=\"aout\"></output></label><input type=\"range\" id=\"a\" min=\"20\" max=\"500\" step=\"10\" value=\"200\"></div><div><label for=\"b\">Heat-loss coefficient hA (W/K): <output id=\"bout\"></output></label><input type=\"range\" id=\"b\" min=\"2\" max=\"30\" step=\"1\" value=\"10\"></div></div><div class=\"reading\">Calculated result: <span id=\"metric\" aria-live=\"polite\"></span></div><svg id=\"graph\" class=\"graph\" viewBox=\"0 0 810 300\" role=\"img\" aria-label=\"Interactive model output plotted against the horizontal axis\"></svg><p><button type=\"button\" id=\"reset\">Reset values</button> <span id=\"status\" class=\"muted\" role=\"status\"></span></p><div class=\"warn\"><b>Educational model, not equipment validation.</b> Simplifying assumptions exclude many real sensor, actuator, friction, failure and safety effects. Check parameters and physical limits before using any equation in engineering work.</div></div>",
    init: function(card) {
      try {
        card.dataset.model = String(16);
        document.body.dataset.model = String(16);
const i=Number(document.body.dataset.model)-1,s=OpenSTEMModels.specs[i],a=card.querySelector('#a'),b=card.querySelector('#b'),aout=card.querySelector('#aout'),bout=card.querySelector('#bout'),metric=card.querySelector('#metric'),svg=card.querySelector('#graph'),status=card.querySelector('#status');
function f(v){return Number(v).toLocaleString('en-US',{maximumFractionDigits:4});}
function draw(){const aa=Number(a.value),bb=Number(b.value);aout.textContent=f(aa);bout.textContent=f(bb); const o=OpenSTEMModels.calc(i+1,aa,bb);metric.textContent=o.metric;let mn=Math.min(...o.ys,...(o.alt||[])),mx=Math.max(...o.ys,...(o.alt||[]));if(mx===mn){mn-=1;mx+=1;}else{let m=(mx-mn)*.13;mn-=m;mx+=m;}
let x0=o.xs[0],x1=o.xs[o.xs.length-1],w=810,h=300,l=65,t=20,r=20,bt=54;let X=x=>l+(x-x0)/(x1-x0)*(w-l-r),Y=y=>t+(mx-y)/(mx-mn)*(h-t-bt),pts=y=>y.map((v,j)=>X(o.xs[j]).toFixed(2)+','+Y(v).toFixed(2)).join(' ');
svg.innerHTML='<rect x="'+l+'" y="'+t+'" width="'+(w-l-r)+'" height="'+(h-t-bt)+'" fill="#fafcff" stroke="#b5c9d9"/>';
let mk=(tag,attr,txt)=>{const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attr).forEach(([k,v])=>el.setAttribute(k,v));if(txt!==undefined)el.textContent=txt;svg.append(el);};
for(let k=0;k<=4;k++){let yy=t+k*(h-t-bt)/4;mk('line',{x1:l,y1:yy,x2:w-r,y2:yy,stroke:'#e0e9ef'});mk('text',{x:3,y:yy+5},f(mx-(mx-mn)*k/4));}
for(let k=0;k<=4;k++){let xx=l+k*(w-l-r)/4;mk('text',{x:xx-15,y:h-24},f(x0+(x1-x0)*k/4));}
mk('polyline',{points:pts(o.ys),class:'trace'});if(o.alt)mk('polyline',{points:pts(o.alt),class:'alt'});
mk('text',{x:w/2-80,y:h-2},o.xlabel);mk('text',{x:l+5,y:14},o.ylabel);
status.textContent='Recomputed for current parameters. Solid blue: model output'+(o.alt?'; dashed orange: conditional-integrator result':'')+'.';
}
a.addEventListener('input',draw);b.addEventListener('input',draw);card.querySelector('#reset').addEventListener('click',()=>{a.value=s.a.value;b.value=s.b.value;draw();});draw();
      } catch (err) {
        console.warn('Sim init error in model 16:', err);
      }
    }
  });

  if (!window.SimulationEngine) {
    window.SimulationEngine = {};
  }

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
      if (bMatch !== undefined && bMatch !== null && bMatch !== '') {
        unitNum = parseInt(bMatch, 10) + 1;
      } else {
        var pMatch = window.location.pathname.match(/chapter-(\d+)/);
        if (pMatch) {
          unitNum = parseInt(pMatch[1], 10);
        }
      }
    }

    if (isNaN(unitNum) || unitNum < 1 || unitNum > 8) unitNum = 1;

    var modelsForUnit = OPENSTEM_SIM_MODELS.filter(function(m) { return m.unit === unitNum; });
    if (modelsForUnit.length === 0) modelsForUnit = OPENSTEM_SIM_MODELS.slice(0, 2);

    modelsForUnit.forEach(function(m) {
      var card = document.createElement('section');
      card.className = 'me-sim-card';
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
        if (document.getElementById('sim-container')) {
          window.SimulationEngine.initSimulation('sim-container');
        }
      });
    } else {
      if (document.getElementById('sim-container')) {
        window.SimulationEngine.initSimulation('sim-container');
      }
    }
  }
})(typeof window === 'undefined' ? globalThis : window);
