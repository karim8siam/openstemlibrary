/* theory-of-machines-and-mechanisms Interactive Simulation Suite */
(function(window) {
  'use strict';

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 01 OF 16 \u00b7 OFFLINE</span><h3>Angular velocity from rpm</h3><p>Move the controls to examine one explicitly simplified physical relationship.</p><div class=\"links\"></div></section><p class=\"notice\">Constant-speed shaft: scaling rpm and multiplier; not a load capacity model. Synthetic parameter ranges only; not approved for machine sizing or safety decisions.</p><section class=\"sim\"><label for=\"slider-x\">Speed (rpm): <span id=\"value-x\"></span></label><input type=\"range\" id=\"slider-x\" min=\"60\" max=\"3600\" value=\"900\" step=\"any\"><label for=\"slider-y\">Multiplier (\u00d7): <span id=\"value-y\"></span></label><input type=\"range\" id=\"slider-y\" min=\"0.5\" max=\"2\" value=\"1\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 720 282\" role=\"img\" aria-label=\"Model output versus first input\"></svg><p id=\"note\">The plot rescales vertically for each second-slider setting. Compare numbers rather than curve heights between different settings.</p><h2>Analysis questions</h2><p>Find a nonlinear region, if present. Determine whether the output is signed or always nonnegative. Check a physically relevant limiting value using the model equation, then propose an independent observation that would reveal model failure. If a quantity has large sensitivity, identify a manufacturing or instrumentation uncertainty that could make it unreliable.</p></section>",
    init: function(card) {
      try {
const sx=card.querySelector("#" + 'slider-x'.replace(/^#/, "")),sy=card.querySelector("#" + 'slider-y'.replace(/^#/, ""));
const vx=card.querySelector("#" + 'value-x'.replace(/^#/, "")),vy=card.querySelector("#" + 'value-y'.replace(/^#/, "")),out=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const lo=Number(sx.min),hi=Number(sx.max);
function model(x,y){return (2*Math.PI*x/60)*y;}
function render(){
 const x=Number(sx.value),y=Number(sy.value),v=model(x,y);
 vx.textContent=x.toPrecision(4);vy.textContent=y.toPrecision(4);out.textContent=(Number.isFinite(v)?v.toPrecision(6):'Outside domain')+' rad/s';
 const pts=Array.from({length:91},(_,i)=>{let a=lo+(hi-lo)*i/90;return [a,model(a,y)];}).filter(k=>Number.isFinite(k[1]));
 if(pts.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...pts.map(p=>p[1])),vmax=Math.max(...pts.map(p=>p[1]));
 if(vmin===vmax){vmin-=1;vmax+=1;}
 const Y=q=>235-185*(q-vmin)/(vmax-vmin),X=q=>45+630*(q-lo)/(hi-lo);
 const line=pts.map((p,i)=>(i?'L':'M')+X(p[0]).toFixed(2)+','+Y(p[1]).toFixed(2)).join(' ');
 plot.innerHTML='<path d="M45 24 V235 H684" stroke="#8b9aaf" stroke-width="1" fill="none"/><path d="'+line+'" fill="none" stroke="#128397" stroke-width="3"/><circle cx="'+X(x).toFixed(2)+'" cy="'+Y(v).toFixed(2)+'" r="6" fill="#e29b36"/><text x="48" y="270" fill="currentColor" font-size="15">First slider increases →</text>';
}
sx.addEventListener('input',render);sy.addEventListener('input',render);render();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 1,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 02 OF 16 \u00b7 OFFLINE</span><h3>Rigid-link tangential speed</h3><p>Move the controls to examine one explicitly simplified physical relationship.</p><div class=\"links\"></div></section><p class=\"notice\">Pivot stationary; no slip and no flexible-body deformation. Synthetic parameter ranges only; not approved for machine sizing or safety decisions.</p><section class=\"sim\"><label for=\"slider-x\">Radius (m): <span id=\"value-x\"></span></label><input type=\"range\" id=\"slider-x\" min=\"0.05\" max=\"0.5\" value=\"0.2\" step=\"any\"><label for=\"slider-y\">Angular speed (rad/s): <span id=\"value-y\"></span></label><input type=\"range\" id=\"slider-y\" min=\"1\" max=\"45\" value=\"12\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 720 282\" role=\"img\" aria-label=\"Model output versus first input\"></svg><p id=\"note\">The plot rescales vertically for each second-slider setting. Compare numbers rather than curve heights between different settings.</p><h2>Analysis questions</h2><p>Find a nonlinear region, if present. Determine whether the output is signed or always nonnegative. Check a physically relevant limiting value using the model equation, then propose an independent observation that would reveal model failure. If a quantity has large sensitivity, identify a manufacturing or instrumentation uncertainty that could make it unreliable.</p></section>",
    init: function(card) {
      try {
const sx=card.querySelector("#" + 'slider-x'.replace(/^#/, "")),sy=card.querySelector("#" + 'slider-y'.replace(/^#/, ""));
const vx=card.querySelector("#" + 'value-x'.replace(/^#/, "")),vy=card.querySelector("#" + 'value-y'.replace(/^#/, "")),out=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const lo=Number(sx.min),hi=Number(sx.max);
function model(x,y){return x*y;}
function render(){
 const x=Number(sx.value),y=Number(sy.value),v=model(x,y);
 vx.textContent=x.toPrecision(4);vy.textContent=y.toPrecision(4);out.textContent=(Number.isFinite(v)?v.toPrecision(6):'Outside domain')+' m/s';
 const pts=Array.from({length:91},(_,i)=>{let a=lo+(hi-lo)*i/90;return [a,model(a,y)];}).filter(k=>Number.isFinite(k[1]));
 if(pts.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...pts.map(p=>p[1])),vmax=Math.max(...pts.map(p=>p[1]));
 if(vmin===vmax){vmin-=1;vmax+=1;}
 const Y=q=>235-185*(q-vmin)/(vmax-vmin),X=q=>45+630*(q-lo)/(hi-lo);
 const line=pts.map((p,i)=>(i?'L':'M')+X(p[0]).toFixed(2)+','+Y(p[1]).toFixed(2)).join(' ');
 plot.innerHTML='<path d="M45 24 V235 H684" stroke="#8b9aaf" stroke-width="1" fill="none"/><path d="'+line+'" fill="none" stroke="#128397" stroke-width="3"/><circle cx="'+X(x).toFixed(2)+'" cy="'+Y(v).toFixed(2)+'" r="6" fill="#e29b36"/><text x="48" y="270" fill="currentColor" font-size="15">First slider increases →</text>';
}
sx.addEventListener('input',render);sy.addEventListener('input',render);render();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 2,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 03 OF 16 \u00b7 OFFLINE</span><h3>Normal acceleration</h3><p>Move the controls to examine one explicitly simplified physical relationship.</p><div class=\"links\"></div></section><p class=\"notice\">Pure rigid rotation about a fixed reference point. Synthetic parameter ranges only; not approved for machine sizing or safety decisions.</p><section class=\"sim\"><label for=\"slider-x\">Radius (m): <span id=\"value-x\"></span></label><input type=\"range\" id=\"slider-x\" min=\"0.02\" max=\"0.4\" value=\"0.16\" step=\"any\"><label for=\"slider-y\">Angular speed (rad/s): <span id=\"value-y\"></span></label><input type=\"range\" id=\"slider-y\" min=\"2\" max=\"80\" value=\"25\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 720 282\" role=\"img\" aria-label=\"Model output versus first input\"></svg><p id=\"note\">The plot rescales vertically for each second-slider setting. Compare numbers rather than curve heights between different settings.</p><h2>Analysis questions</h2><p>Find a nonlinear region, if present. Determine whether the output is signed or always nonnegative. Check a physically relevant limiting value using the model equation, then propose an independent observation that would reveal model failure. If a quantity has large sensitivity, identify a manufacturing or instrumentation uncertainty that could make it unreliable.</p></section>",
    init: function(card) {
      try {
const sx=card.querySelector("#" + 'slider-x'.replace(/^#/, "")),sy=card.querySelector("#" + 'slider-y'.replace(/^#/, ""));
const vx=card.querySelector("#" + 'value-x'.replace(/^#/, "")),vy=card.querySelector("#" + 'value-y'.replace(/^#/, "")),out=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const lo=Number(sx.min),hi=Number(sx.max);
function model(x,y){return x*y*y;}
function render(){
 const x=Number(sx.value),y=Number(sy.value),v=model(x,y);
 vx.textContent=x.toPrecision(4);vy.textContent=y.toPrecision(4);out.textContent=(Number.isFinite(v)?v.toPrecision(6):'Outside domain')+' m/s²';
 const pts=Array.from({length:91},(_,i)=>{let a=lo+(hi-lo)*i/90;return [a,model(a,y)];}).filter(k=>Number.isFinite(k[1]));
 if(pts.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...pts.map(p=>p[1])),vmax=Math.max(...pts.map(p=>p[1]));
 if(vmin===vmax){vmin-=1;vmax+=1;}
 const Y=q=>235-185*(q-vmin)/(vmax-vmin),X=q=>45+630*(q-lo)/(hi-lo);
 const line=pts.map((p,i)=>(i?'L':'M')+X(p[0]).toFixed(2)+','+Y(p[1]).toFixed(2)).join(' ');
 plot.innerHTML='<path d="M45 24 V235 H684" stroke="#8b9aaf" stroke-width="1" fill="none"/><path d="'+line+'" fill="none" stroke="#128397" stroke-width="3"/><circle cx="'+X(x).toFixed(2)+'" cy="'+Y(v).toFixed(2)+'" r="6" fill="#e29b36"/><text x="48" y="270" fill="currentColor" font-size="15">First slider increases →</text>';
}
sx.addEventListener('input',render);sy.addEventListener('input',render);render();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 2,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 04 OF 16 \u00b7 OFFLINE</span><h3>Slider crank exact position</h3><p>Move the controls to examine one explicitly simplified physical relationship.</p><div class=\"links\"></div></section><p class=\"notice\">r=0.05 m, in-line slider, same positive square-root assembly branch. Synthetic parameter ranges only; not approved for machine sizing or safety decisions.</p><section class=\"sim\"><label for=\"slider-x\">Crank angle (deg): <span id=\"value-x\"></span></label><input type=\"range\" id=\"slider-x\" min=\"0\" max=\"360\" value=\"75\" step=\"any\"><label for=\"slider-y\">Rod length ratio (l/r): <span id=\"value-y\"></span></label><input type=\"range\" id=\"slider-y\" min=\"1.5\" max=\"6\" value=\"3\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 720 282\" role=\"img\" aria-label=\"Model output versus first input\"></svg><p id=\"note\">The plot rescales vertically for each second-slider setting. Compare numbers rather than curve heights between different settings.</p><h2>Analysis questions</h2><p>Find a nonlinear region, if present. Determine whether the output is signed or always nonnegative. Check a physically relevant limiting value using the model equation, then propose an independent observation that would reveal model failure. If a quantity has large sensitivity, identify a manufacturing or instrumentation uncertainty that could make it unreliable.</p></section>",
    init: function(card) {
      try {
const sx=card.querySelector("#" + 'slider-x'.replace(/^#/, "")),sy=card.querySelector("#" + 'slider-y'.replace(/^#/, ""));
const vx=card.querySelector("#" + 'value-x'.replace(/^#/, "")),vy=card.querySelector("#" + 'value-y'.replace(/^#/, "")),out=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const lo=Number(sx.min),hi=Number(sx.max);
function model(x,y){return 0.05*Math.cos(x*Math.PI/180)+Math.sqrt((0.05*y)**2-(0.05*Math.sin(x*Math.PI/180))**2);}
function render(){
 const x=Number(sx.value),y=Number(sy.value),v=model(x,y);
 vx.textContent=x.toPrecision(4);vy.textContent=y.toPrecision(4);out.textContent=(Number.isFinite(v)?v.toPrecision(6):'Outside domain')+' m';
 const pts=Array.from({length:91},(_,i)=>{let a=lo+(hi-lo)*i/90;return [a,model(a,y)];}).filter(k=>Number.isFinite(k[1]));
 if(pts.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...pts.map(p=>p[1])),vmax=Math.max(...pts.map(p=>p[1]));
 if(vmin===vmax){vmin-=1;vmax+=1;}
 const Y=q=>235-185*(q-vmin)/(vmax-vmin),X=q=>45+630*(q-lo)/(hi-lo);
 const line=pts.map((p,i)=>(i?'L':'M')+X(p[0]).toFixed(2)+','+Y(p[1]).toFixed(2)).join(' ');
 plot.innerHTML='<path d="M45 24 V235 H684" stroke="#8b9aaf" stroke-width="1" fill="none"/><path d="'+line+'" fill="none" stroke="#128397" stroke-width="3"/><circle cx="'+X(x).toFixed(2)+'" cy="'+Y(v).toFixed(2)+'" r="6" fill="#e29b36"/><text x="48" y="270" fill="currentColor" font-size="15">First slider increases →</text>';
}
sx.addEventListener('input',render);sy.addEventListener('input',render);render();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 3,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 05 OF 16 \u00b7 OFFLINE</span><h3>Slider-crank long-rod deviation</h3><p>Move the controls to examine one explicitly simplified physical relationship.</p><div class=\"links\"></div></section><p class=\"notice\">Difference between finite-rod exact position and long-rod x\u2248l+r cos\u03b8 (can be negative). Synthetic parameter ranges only; not approved for machine sizing or safety decisions.</p><section class=\"sim\"><label for=\"slider-x\">Crank angle (deg): <span id=\"value-x\"></span></label><input type=\"range\" id=\"slider-x\" min=\"0\" max=\"360\" value=\"90\" step=\"any\"><label for=\"slider-y\">Rod ratio (l/r): <span id=\"value-y\"></span></label><input type=\"range\" id=\"slider-y\" min=\"1.4\" max=\"6\" value=\"2.5\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 720 282\" role=\"img\" aria-label=\"Model output versus first input\"></svg><p id=\"note\">The plot rescales vertically for each second-slider setting. Compare numbers rather than curve heights between different settings.</p><h2>Analysis questions</h2><p>Find a nonlinear region, if present. Determine whether the output is signed or always nonnegative. Check a physically relevant limiting value using the model equation, then propose an independent observation that would reveal model failure. If a quantity has large sensitivity, identify a manufacturing or instrumentation uncertainty that could make it unreliable.</p></section>",
    init: function(card) {
      try {
const sx=card.querySelector("#" + 'slider-x'.replace(/^#/, "")),sy=card.querySelector("#" + 'slider-y'.replace(/^#/, ""));
const vx=card.querySelector("#" + 'value-x'.replace(/^#/, "")),vy=card.querySelector("#" + 'value-y'.replace(/^#/, "")),out=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const lo=Number(sx.min),hi=Number(sx.max);
function model(x,y){return 1000*(Math.sqrt((0.05*y)**2-(0.05*Math.sin(x*Math.PI/180))**2)-0.05*y);}
function render(){
 const x=Number(sx.value),y=Number(sy.value),v=model(x,y);
 vx.textContent=x.toPrecision(4);vy.textContent=y.toPrecision(4);out.textContent=(Number.isFinite(v)?v.toPrecision(6):'Outside domain')+' mm';
 const pts=Array.from({length:91},(_,i)=>{let a=lo+(hi-lo)*i/90;return [a,model(a,y)];}).filter(k=>Number.isFinite(k[1]));
 if(pts.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...pts.map(p=>p[1])),vmax=Math.max(...pts.map(p=>p[1]));
 if(vmin===vmax){vmin-=1;vmax+=1;}
 const Y=q=>235-185*(q-vmin)/(vmax-vmin),X=q=>45+630*(q-lo)/(hi-lo);
 const line=pts.map((p,i)=>(i?'L':'M')+X(p[0]).toFixed(2)+','+Y(p[1]).toFixed(2)).join(' ');
 plot.innerHTML='<path d="M45 24 V235 H684" stroke="#8b9aaf" stroke-width="1" fill="none"/><path d="'+line+'" fill="none" stroke="#128397" stroke-width="3"/><circle cx="'+X(x).toFixed(2)+'" cy="'+Y(v).toFixed(2)+'" r="6" fill="#e29b36"/><text x="48" y="270" fill="currentColor" font-size="15">First slider increases →</text>';
}
sx.addEventListener('input',render);sy.addEventListener('input',render);render();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 3,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 06 OF 16 \u00b7 OFFLINE</span><h3>External gear ratio</h3><p>Move the controls to examine one explicitly simplified physical relationship.</p><div class=\"links\"></div></section><p class=\"notice\">Signed output/input speed, external mesh; ratio only, no efficiency information. Synthetic parameter ranges only; not approved for machine sizing or safety decisions.</p><section class=\"sim\"><label for=\"slider-x\">Driver teeth (teeth): <span id=\"value-x\"></span></label><input type=\"range\" id=\"slider-x\" min=\"12\" max=\"80\" value=\"24\" step=\"any\"><label for=\"slider-y\">Driven teeth (teeth): <span id=\"value-y\"></span></label><input type=\"range\" id=\"slider-y\" min=\"12\" max=\"120\" value=\"72\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 720 282\" role=\"img\" aria-label=\"Model output versus first input\"></svg><p id=\"note\">The plot rescales vertically for each second-slider setting. Compare numbers rather than curve heights between different settings.</p><h2>Analysis questions</h2><p>Find a nonlinear region, if present. Determine whether the output is signed or always nonnegative. Check a physically relevant limiting value using the model equation, then propose an independent observation that would reveal model failure. If a quantity has large sensitivity, identify a manufacturing or instrumentation uncertainty that could make it unreliable.</p></section>",
    init: function(card) {
      try {
const sx=card.querySelector("#" + 'slider-x'.replace(/^#/, "")),sy=card.querySelector("#" + 'slider-y'.replace(/^#/, ""));
const vx=card.querySelector("#" + 'value-x'.replace(/^#/, "")),vy=card.querySelector("#" + 'value-y'.replace(/^#/, "")),out=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const lo=Number(sx.min),hi=Number(sx.max);
function model(x,y){return -x/y;}
function render(){
 const x=Number(sx.value),y=Number(sy.value),v=model(x,y);
 vx.textContent=x.toPrecision(4);vy.textContent=y.toPrecision(4);out.textContent=(Number.isFinite(v)?v.toPrecision(6):'Outside domain')+' ratio';
 const pts=Array.from({length:91},(_,i)=>{let a=lo+(hi-lo)*i/90;return [a,model(a,y)];}).filter(k=>Number.isFinite(k[1]));
 if(pts.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...pts.map(p=>p[1])),vmax=Math.max(...pts.map(p=>p[1]));
 if(vmin===vmax){vmin-=1;vmax+=1;}
 const Y=q=>235-185*(q-vmin)/(vmax-vmin),X=q=>45+630*(q-lo)/(hi-lo);
 const line=pts.map((p,i)=>(i?'L':'M')+X(p[0]).toFixed(2)+','+Y(p[1]).toFixed(2)).join(' ');
 plot.innerHTML='<path d="M45 24 V235 H684" stroke="#8b9aaf" stroke-width="1" fill="none"/><path d="'+line+'" fill="none" stroke="#128397" stroke-width="3"/><circle cx="'+X(x).toFixed(2)+'" cy="'+Y(v).toFixed(2)+'" r="6" fill="#e29b36"/><text x="48" y="270" fill="currentColor" font-size="15">First slider increases →</text>';
}
sx.addEventListener('input',render);sy.addEventListener('input',render);render();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 4,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 07 OF 16 \u00b7 OFFLINE</span><h3>Ideal gear output speed</h3><p>Move the controls to examine one explicitly simplified physical relationship.</p><div class=\"links\"></div></section><p class=\"notice\">Magnitudes only, ideal gear train without slip or loss. Synthetic parameter ranges only; not approved for machine sizing or safety decisions.</p><section class=\"sim\"><label for=\"slider-x\">Input speed (rpm): <span id=\"value-x\"></span></label><input type=\"range\" id=\"slider-x\" min=\"100\" max=\"3000\" value=\"1200\" step=\"any\"><label for=\"slider-y\">Gear reduction (ratio): <span id=\"value-y\"></span></label><input type=\"range\" id=\"slider-y\" min=\"1\" max=\"12\" value=\"4\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 720 282\" role=\"img\" aria-label=\"Model output versus first input\"></svg><p id=\"note\">The plot rescales vertically for each second-slider setting. Compare numbers rather than curve heights between different settings.</p><h2>Analysis questions</h2><p>Find a nonlinear region, if present. Determine whether the output is signed or always nonnegative. Check a physically relevant limiting value using the model equation, then propose an independent observation that would reveal model failure. If a quantity has large sensitivity, identify a manufacturing or instrumentation uncertainty that could make it unreliable.</p></section>",
    init: function(card) {
      try {
const sx=card.querySelector("#" + 'slider-x'.replace(/^#/, "")),sy=card.querySelector("#" + 'slider-y'.replace(/^#/, ""));
const vx=card.querySelector("#" + 'value-x'.replace(/^#/, "")),vy=card.querySelector("#" + 'value-y'.replace(/^#/, "")),out=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const lo=Number(sx.min),hi=Number(sx.max);
function model(x,y){return x/y;}
function render(){
 const x=Number(sx.value),y=Number(sy.value),v=model(x,y);
 vx.textContent=x.toPrecision(4);vy.textContent=y.toPrecision(4);out.textContent=(Number.isFinite(v)?v.toPrecision(6):'Outside domain')+' rpm';
 const pts=Array.from({length:91},(_,i)=>{let a=lo+(hi-lo)*i/90;return [a,model(a,y)];}).filter(k=>Number.isFinite(k[1]));
 if(pts.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...pts.map(p=>p[1])),vmax=Math.max(...pts.map(p=>p[1]));
 if(vmin===vmax){vmin-=1;vmax+=1;}
 const Y=q=>235-185*(q-vmin)/(vmax-vmin),X=q=>45+630*(q-lo)/(hi-lo);
 const line=pts.map((p,i)=>(i?'L':'M')+X(p[0]).toFixed(2)+','+Y(p[1]).toFixed(2)).join(' ');
 plot.innerHTML='<path d="M45 24 V235 H684" stroke="#8b9aaf" stroke-width="1" fill="none"/><path d="'+line+'" fill="none" stroke="#128397" stroke-width="3"/><circle cx="'+X(x).toFixed(2)+'" cy="'+Y(v).toFixed(2)+'" r="6" fill="#e29b36"/><text x="48" y="270" fill="currentColor" font-size="15">First slider increases →</text>';
}
sx.addEventListener('input',render);sy.addEventListener('input',render);render();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 4,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 08 OF 16 \u00b7 OFFLINE</span><h3>Ideal belt driven speed</h3><p>Move the controls to examine one explicitly simplified physical relationship.</p><div class=\"links\"></div></section><p class=\"notice\">Driver fixed at 1500 rpm; pitch diameters, no slip or creep. Synthetic parameter ranges only; not approved for machine sizing or safety decisions.</p><section class=\"sim\"><label for=\"slider-x\">Driver diameter (mm): <span id=\"value-x\"></span></label><input type=\"range\" id=\"slider-x\" min=\"30\" max=\"200\" value=\"80\" step=\"any\"><label for=\"slider-y\">Driven diameter (mm): <span id=\"value-y\"></span></label><input type=\"range\" id=\"slider-y\" min=\"30\" max=\"300\" value=\"160\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 720 282\" role=\"img\" aria-label=\"Model output versus first input\"></svg><p id=\"note\">The plot rescales vertically for each second-slider setting. Compare numbers rather than curve heights between different settings.</p><h2>Analysis questions</h2><p>Find a nonlinear region, if present. Determine whether the output is signed or always nonnegative. Check a physically relevant limiting value using the model equation, then propose an independent observation that would reveal model failure. If a quantity has large sensitivity, identify a manufacturing or instrumentation uncertainty that could make it unreliable.</p></section>",
    init: function(card) {
      try {
const sx=card.querySelector("#" + 'slider-x'.replace(/^#/, "")),sy=card.querySelector("#" + 'slider-y'.replace(/^#/, ""));
const vx=card.querySelector("#" + 'value-x'.replace(/^#/, "")),vy=card.querySelector("#" + 'value-y'.replace(/^#/, "")),out=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const lo=Number(sx.min),hi=Number(sx.max);
function model(x,y){return 1500*x/y;}
function render(){
 const x=Number(sx.value),y=Number(sy.value),v=model(x,y);
 vx.textContent=x.toPrecision(4);vy.textContent=y.toPrecision(4);out.textContent=(Number.isFinite(v)?v.toPrecision(6):'Outside domain')+' rpm';
 const pts=Array.from({length:91},(_,i)=>{let a=lo+(hi-lo)*i/90;return [a,model(a,y)];}).filter(k=>Number.isFinite(k[1]));
 if(pts.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...pts.map(p=>p[1])),vmax=Math.max(...pts.map(p=>p[1]));
 if(vmin===vmax){vmin-=1;vmax+=1;}
 const Y=q=>235-185*(q-vmin)/(vmax-vmin),X=q=>45+630*(q-lo)/(hi-lo);
 const line=pts.map((p,i)=>(i?'L':'M')+X(p[0]).toFixed(2)+','+Y(p[1]).toFixed(2)).join(' ');
 plot.innerHTML='<path d="M45 24 V235 H684" stroke="#8b9aaf" stroke-width="1" fill="none"/><path d="'+line+'" fill="none" stroke="#128397" stroke-width="3"/><circle cx="'+X(x).toFixed(2)+'" cy="'+Y(v).toFixed(2)+'" r="6" fill="#e29b36"/><text x="48" y="270" fill="currentColor" font-size="15">First slider increases →</text>';
}
sx.addEventListener('input',render);sy.addEventListener('input',render);render();
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  MODELS.push({
    idx: 9,
    unit: 5,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 09 OF 16 \u00b7 OFFLINE</span><h3>Cam simple-harmonic rise</h3><p>Move the controls to examine one explicitly simplified physical relationship.</p><div class=\"links\"></div></section><p class=\"notice\">Only the rise segment; no cam contact or acceleration load prediction. Synthetic parameter ranges only; not approved for machine sizing or safety decisions.</p><section class=\"sim\"><label for=\"slider-x\">Rise progress (fraction): <span id=\"value-x\"></span></label><input type=\"range\" id=\"slider-x\" min=\"0\" max=\"1\" value=\"0.5\" step=\"any\"><label for=\"slider-y\">Lift (mm): <span id=\"value-y\"></span></label><input type=\"range\" id=\"slider-y\" min=\"3\" max=\"40\" value=\"12\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 720 282\" role=\"img\" aria-label=\"Model output versus first input\"></svg><p id=\"note\">The plot rescales vertically for each second-slider setting. Compare numbers rather than curve heights between different settings.</p><h2>Analysis questions</h2><p>Find a nonlinear region, if present. Determine whether the output is signed or always nonnegative. Check a physically relevant limiting value using the model equation, then propose an independent observation that would reveal model failure. If a quantity has large sensitivity, identify a manufacturing or instrumentation uncertainty that could make it unreliable.</p></section>",
    init: function(card) {
      try {
const sx=card.querySelector("#" + 'slider-x'.replace(/^#/, "")),sy=card.querySelector("#" + 'slider-y'.replace(/^#/, ""));
const vx=card.querySelector("#" + 'value-x'.replace(/^#/, "")),vy=card.querySelector("#" + 'value-y'.replace(/^#/, "")),out=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const lo=Number(sx.min),hi=Number(sx.max);
function model(x,y){return y/2*(1-Math.cos(Math.PI*x));}
function render(){
 const x=Number(sx.value),y=Number(sy.value),v=model(x,y);
 vx.textContent=x.toPrecision(4);vy.textContent=y.toPrecision(4);out.textContent=(Number.isFinite(v)?v.toPrecision(6):'Outside domain')+' mm';
 const pts=Array.from({length:91},(_,i)=>{let a=lo+(hi-lo)*i/90;return [a,model(a,y)];}).filter(k=>Number.isFinite(k[1]));
 if(pts.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...pts.map(p=>p[1])),vmax=Math.max(...pts.map(p=>p[1]));
 if(vmin===vmax){vmin-=1;vmax+=1;}
 const Y=q=>235-185*(q-vmin)/(vmax-vmin),X=q=>45+630*(q-lo)/(hi-lo);
 const line=pts.map((p,i)=>(i?'L':'M')+X(p[0]).toFixed(2)+','+Y(p[1]).toFixed(2)).join(' ');
 plot.innerHTML='<path d="M45 24 V235 H684" stroke="#8b9aaf" stroke-width="1" fill="none"/><path d="'+line+'" fill="none" stroke="#128397" stroke-width="3"/><circle cx="'+X(x).toFixed(2)+'" cy="'+Y(v).toFixed(2)+'" r="6" fill="#e29b36"/><text x="48" y="270" fill="currentColor" font-size="15">First slider increases →</text>';
}
sx.addEventListener('input',render);sy.addEventListener('input',render);render();
      } catch (err) {
        console.warn('Sim init error in model 9:', err);
      }
    }
  });

  MODELS.push({
    idx: 10,
    unit: 5,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 10 OF 16 \u00b7 OFFLINE</span><h3>Cycloidal rise displacement</h3><p>Move the controls to examine one explicitly simplified physical relationship.</p><div class=\"links\"></div></section><p class=\"notice\">Ideal cycloidal lift law; dwell and return omitted. Synthetic parameter ranges only; not approved for machine sizing or safety decisions.</p><section class=\"sim\"><label for=\"slider-x\">Rise progress (fraction): <span id=\"value-x\"></span></label><input type=\"range\" id=\"slider-x\" min=\"0\" max=\"1\" value=\"0.3\" step=\"any\"><label for=\"slider-y\">Lift (mm): <span id=\"value-y\"></span></label><input type=\"range\" id=\"slider-y\" min=\"3\" max=\"40\" value=\"12\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 720 282\" role=\"img\" aria-label=\"Model output versus first input\"></svg><p id=\"note\">The plot rescales vertically for each second-slider setting. Compare numbers rather than curve heights between different settings.</p><h2>Analysis questions</h2><p>Find a nonlinear region, if present. Determine whether the output is signed or always nonnegative. Check a physically relevant limiting value using the model equation, then propose an independent observation that would reveal model failure. If a quantity has large sensitivity, identify a manufacturing or instrumentation uncertainty that could make it unreliable.</p></section>",
    init: function(card) {
      try {
const sx=card.querySelector("#" + 'slider-x'.replace(/^#/, "")),sy=card.querySelector("#" + 'slider-y'.replace(/^#/, ""));
const vx=card.querySelector("#" + 'value-x'.replace(/^#/, "")),vy=card.querySelector("#" + 'value-y'.replace(/^#/, "")),out=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const lo=Number(sx.min),hi=Number(sx.max);
function model(x,y){return y*(x-Math.sin(2*Math.PI*x)/(2*Math.PI));}
function render(){
 const x=Number(sx.value),y=Number(sy.value),v=model(x,y);
 vx.textContent=x.toPrecision(4);vy.textContent=y.toPrecision(4);out.textContent=(Number.isFinite(v)?v.toPrecision(6):'Outside domain')+' mm';
 const pts=Array.from({length:91},(_,i)=>{let a=lo+(hi-lo)*i/90;return [a,model(a,y)];}).filter(k=>Number.isFinite(k[1]));
 if(pts.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...pts.map(p=>p[1])),vmax=Math.max(...pts.map(p=>p[1]));
 if(vmin===vmax){vmin-=1;vmax+=1;}
 const Y=q=>235-185*(q-vmin)/(vmax-vmin),X=q=>45+630*(q-lo)/(hi-lo);
 const line=pts.map((p,i)=>(i?'L':'M')+X(p[0]).toFixed(2)+','+Y(p[1]).toFixed(2)).join(' ');
 plot.innerHTML='<path d="M45 24 V235 H684" stroke="#8b9aaf" stroke-width="1" fill="none"/><path d="'+line+'" fill="none" stroke="#128397" stroke-width="3"/><circle cx="'+X(x).toFixed(2)+'" cy="'+Y(v).toFixed(2)+'" r="6" fill="#e29b36"/><text x="48" y="270" fill="currentColor" font-size="15">First slider increases →</text>';
}
sx.addEventListener('input',render);sy.addEventListener('input',render);render();
      } catch (err) {
        console.warn('Sim init error in model 10:', err);
      }
    }
  });

  MODELS.push({
    idx: 11,
    unit: 6,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 11 OF 16 \u00b7 OFFLINE</span><h3>Rotor inertial torque</h3><p>Move the controls to examine one explicitly simplified physical relationship.</p><div class=\"links\"></div></section><p class=\"notice\">Net inertial torque, ignoring friction and working load. Synthetic parameter ranges only; not approved for machine sizing or safety decisions.</p><section class=\"sim\"><label for=\"slider-x\">Inertia (kg m\u00b2): <span id=\"value-x\"></span></label><input type=\"range\" id=\"slider-x\" min=\"0.01\" max=\"1\" value=\"0.12\" step=\"any\"><label for=\"slider-y\">Angular acceleration (rad/s\u00b2): <span id=\"value-y\"></span></label><input type=\"range\" id=\"slider-y\" min=\"0\" max=\"80\" value=\"20\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 720 282\" role=\"img\" aria-label=\"Model output versus first input\"></svg><p id=\"note\">The plot rescales vertically for each second-slider setting. Compare numbers rather than curve heights between different settings.</p><h2>Analysis questions</h2><p>Find a nonlinear region, if present. Determine whether the output is signed or always nonnegative. Check a physically relevant limiting value using the model equation, then propose an independent observation that would reveal model failure. If a quantity has large sensitivity, identify a manufacturing or instrumentation uncertainty that could make it unreliable.</p></section>",
    init: function(card) {
      try {
const sx=card.querySelector("#" + 'slider-x'.replace(/^#/, "")),sy=card.querySelector("#" + 'slider-y'.replace(/^#/, ""));
const vx=card.querySelector("#" + 'value-x'.replace(/^#/, "")),vy=card.querySelector("#" + 'value-y'.replace(/^#/, "")),out=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const lo=Number(sx.min),hi=Number(sx.max);
function model(x,y){return x*y;}
function render(){
 const x=Number(sx.value),y=Number(sy.value),v=model(x,y);
 vx.textContent=x.toPrecision(4);vy.textContent=y.toPrecision(4);out.textContent=(Number.isFinite(v)?v.toPrecision(6):'Outside domain')+' N·m';
 const pts=Array.from({length:91},(_,i)=>{let a=lo+(hi-lo)*i/90;return [a,model(a,y)];}).filter(k=>Number.isFinite(k[1]));
 if(pts.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...pts.map(p=>p[1])),vmax=Math.max(...pts.map(p=>p[1]));
 if(vmin===vmax){vmin-=1;vmax+=1;}
 const Y=q=>235-185*(q-vmin)/(vmax-vmin),X=q=>45+630*(q-lo)/(hi-lo);
 const line=pts.map((p,i)=>(i?'L':'M')+X(p[0]).toFixed(2)+','+Y(p[1]).toFixed(2)).join(' ');
 plot.innerHTML='<path d="M45 24 V235 H684" stroke="#8b9aaf" stroke-width="1" fill="none"/><path d="'+line+'" fill="none" stroke="#128397" stroke-width="3"/><circle cx="'+X(x).toFixed(2)+'" cy="'+Y(v).toFixed(2)+'" r="6" fill="#e29b36"/><text x="48" y="270" fill="currentColor" font-size="15">First slider increases →</text>';
}
sx.addEventListener('input',render);sy.addEventListener('input',render);render();
      } catch (err) {
        console.warn('Sim init error in model 11:', err);
      }
    }
  });

  MODELS.push({
    idx: 12,
    unit: 6,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 12 OF 16 \u00b7 OFFLINE</span><h3>Flywheel kinetic energy</h3><p>Move the controls to examine one explicitly simplified physical relationship.</p><div class=\"links\"></div></section><p class=\"notice\">Total stored kinetic energy, not energy available over allowed speed drop. Synthetic parameter ranges only; not approved for machine sizing or safety decisions.</p><section class=\"sim\"><label for=\"slider-x\">Inertia (kg m\u00b2): <span id=\"value-x\"></span></label><input type=\"range\" id=\"slider-x\" min=\"0.01\" max=\"1\" value=\"0.4\" step=\"any\"><label for=\"slider-y\">Angular speed (rad/s): <span id=\"value-y\"></span></label><input type=\"range\" id=\"slider-y\" min=\"0\" max=\"100\" value=\"24\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 720 282\" role=\"img\" aria-label=\"Model output versus first input\"></svg><p id=\"note\">The plot rescales vertically for each second-slider setting. Compare numbers rather than curve heights between different settings.</p><h2>Analysis questions</h2><p>Find a nonlinear region, if present. Determine whether the output is signed or always nonnegative. Check a physically relevant limiting value using the model equation, then propose an independent observation that would reveal model failure. If a quantity has large sensitivity, identify a manufacturing or instrumentation uncertainty that could make it unreliable.</p></section>",
    init: function(card) {
      try {
const sx=card.querySelector("#" + 'slider-x'.replace(/^#/, "")),sy=card.querySelector("#" + 'slider-y'.replace(/^#/, ""));
const vx=card.querySelector("#" + 'value-x'.replace(/^#/, "")),vy=card.querySelector("#" + 'value-y'.replace(/^#/, "")),out=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const lo=Number(sx.min),hi=Number(sx.max);
function model(x,y){return 0.5*x*y*y;}
function render(){
 const x=Number(sx.value),y=Number(sy.value),v=model(x,y);
 vx.textContent=x.toPrecision(4);vy.textContent=y.toPrecision(4);out.textContent=(Number.isFinite(v)?v.toPrecision(6):'Outside domain')+' J';
 const pts=Array.from({length:91},(_,i)=>{let a=lo+(hi-lo)*i/90;return [a,model(a,y)];}).filter(k=>Number.isFinite(k[1]));
 if(pts.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...pts.map(p=>p[1])),vmax=Math.max(...pts.map(p=>p[1]));
 if(vmin===vmax){vmin-=1;vmax+=1;}
 const Y=q=>235-185*(q-vmin)/(vmax-vmin),X=q=>45+630*(q-lo)/(hi-lo);
 const line=pts.map((p,i)=>(i?'L':'M')+X(p[0]).toFixed(2)+','+Y(p[1]).toFixed(2)).join(' ');
 plot.innerHTML='<path d="M45 24 V235 H684" stroke="#8b9aaf" stroke-width="1" fill="none"/><path d="'+line+'" fill="none" stroke="#128397" stroke-width="3"/><circle cx="'+X(x).toFixed(2)+'" cy="'+Y(v).toFixed(2)+'" r="6" fill="#e29b36"/><text x="48" y="270" fill="currentColor" font-size="15">First slider increases →</text>';
}
sx.addEventListener('input',render);sy.addEventListener('input',render);render();
      } catch (err) {
        console.warn('Sim init error in model 12:', err);
      }
    }
  });

  MODELS.push({
    idx: 13,
    unit: 7,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 13 OF 16 \u00b7 OFFLINE</span><h3>Unbalance force</h3><p>Move the controls to examine one explicitly simplified physical relationship.</p><div class=\"links\"></div></section><p class=\"notice\">Equivalent eccentricity fixed at 8 mm; one-plane model. Synthetic parameter ranges only; not approved for machine sizing or safety decisions.</p><section class=\"sim\"><label for=\"slider-x\">Unbalance mass (kg): <span id=\"value-x\"></span></label><input type=\"range\" id=\"slider-x\" min=\"0.001\" max=\"0.1\" value=\"0.02\" step=\"any\"><label for=\"slider-y\">Angular speed (rad/s): <span id=\"value-y\"></span></label><input type=\"range\" id=\"slider-y\" min=\"10\" max=\"150\" value=\"100\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 720 282\" role=\"img\" aria-label=\"Model output versus first input\"></svg><p id=\"note\">The plot rescales vertically for each second-slider setting. Compare numbers rather than curve heights between different settings.</p><h2>Analysis questions</h2><p>Find a nonlinear region, if present. Determine whether the output is signed or always nonnegative. Check a physically relevant limiting value using the model equation, then propose an independent observation that would reveal model failure. If a quantity has large sensitivity, identify a manufacturing or instrumentation uncertainty that could make it unreliable.</p></section>",
    init: function(card) {
      try {
const sx=card.querySelector("#" + 'slider-x'.replace(/^#/, "")),sy=card.querySelector("#" + 'slider-y'.replace(/^#/, ""));
const vx=card.querySelector("#" + 'value-x'.replace(/^#/, "")),vy=card.querySelector("#" + 'value-y'.replace(/^#/, "")),out=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const lo=Number(sx.min),hi=Number(sx.max);
function model(x,y){return x*0.008*y*y;}
function render(){
 const x=Number(sx.value),y=Number(sy.value),v=model(x,y);
 vx.textContent=x.toPrecision(4);vy.textContent=y.toPrecision(4);out.textContent=(Number.isFinite(v)?v.toPrecision(6):'Outside domain')+' N';
 const pts=Array.from({length:91},(_,i)=>{let a=lo+(hi-lo)*i/90;return [a,model(a,y)];}).filter(k=>Number.isFinite(k[1]));
 if(pts.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...pts.map(p=>p[1])),vmax=Math.max(...pts.map(p=>p[1]));
 if(vmin===vmax){vmin-=1;vmax+=1;}
 const Y=q=>235-185*(q-vmin)/(vmax-vmin),X=q=>45+630*(q-lo)/(hi-lo);
 const line=pts.map((p,i)=>(i?'L':'M')+X(p[0]).toFixed(2)+','+Y(p[1]).toFixed(2)).join(' ');
 plot.innerHTML='<path d="M45 24 V235 H684" stroke="#8b9aaf" stroke-width="1" fill="none"/><path d="'+line+'" fill="none" stroke="#128397" stroke-width="3"/><circle cx="'+X(x).toFixed(2)+'" cy="'+Y(v).toFixed(2)+'" r="6" fill="#e29b36"/><text x="48" y="270" fill="currentColor" font-size="15">First slider increases →</text>';
}
sx.addEventListener('input',render);sy.addEventListener('input',render);render();
      } catch (err) {
        console.warn('Sim init error in model 13:', err);
      }
    }
  });

  MODELS.push({
    idx: 14,
    unit: 7,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 14 OF 16 \u00b7 OFFLINE</span><h3>SDOF natural frequency</h3><p>Move the controls to examine one explicitly simplified physical relationship.</p><div class=\"links\"></div></section><p class=\"notice\">Small-amplitude undamped linear mode; distributed machine modes omitted. Synthetic parameter ranges only; not approved for machine sizing or safety decisions.</p><section class=\"sim\"><label for=\"slider-x\">Equivalent mass (kg): <span id=\"value-x\"></span></label><input type=\"range\" id=\"slider-x\" min=\"1\" max=\"80\" value=\"20\" step=\"any\"><label for=\"slider-y\">Stiffness (kN/m): <span id=\"value-y\"></span></label><input type=\"range\" id=\"slider-y\" min=\"5\" max=\"200\" value=\"80\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 720 282\" role=\"img\" aria-label=\"Model output versus first input\"></svg><p id=\"note\">The plot rescales vertically for each second-slider setting. Compare numbers rather than curve heights between different settings.</p><h2>Analysis questions</h2><p>Find a nonlinear region, if present. Determine whether the output is signed or always nonnegative. Check a physically relevant limiting value using the model equation, then propose an independent observation that would reveal model failure. If a quantity has large sensitivity, identify a manufacturing or instrumentation uncertainty that could make it unreliable.</p></section>",
    init: function(card) {
      try {
const sx=card.querySelector("#" + 'slider-x'.replace(/^#/, "")),sy=card.querySelector("#" + 'slider-y'.replace(/^#/, ""));
const vx=card.querySelector("#" + 'value-x'.replace(/^#/, "")),vy=card.querySelector("#" + 'value-y'.replace(/^#/, "")),out=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const lo=Number(sx.min),hi=Number(sx.max);
function model(x,y){return Math.sqrt(y*1000/x)/(2*Math.PI);}
function render(){
 const x=Number(sx.value),y=Number(sy.value),v=model(x,y);
 vx.textContent=x.toPrecision(4);vy.textContent=y.toPrecision(4);out.textContent=(Number.isFinite(v)?v.toPrecision(6):'Outside domain')+' Hz';
 const pts=Array.from({length:91},(_,i)=>{let a=lo+(hi-lo)*i/90;return [a,model(a,y)];}).filter(k=>Number.isFinite(k[1]));
 if(pts.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...pts.map(p=>p[1])),vmax=Math.max(...pts.map(p=>p[1]));
 if(vmin===vmax){vmin-=1;vmax+=1;}
 const Y=q=>235-185*(q-vmin)/(vmax-vmin),X=q=>45+630*(q-lo)/(hi-lo);
 const line=pts.map((p,i)=>(i?'L':'M')+X(p[0]).toFixed(2)+','+Y(p[1]).toFixed(2)).join(' ');
 plot.innerHTML='<path d="M45 24 V235 H684" stroke="#8b9aaf" stroke-width="1" fill="none"/><path d="'+line+'" fill="none" stroke="#128397" stroke-width="3"/><circle cx="'+X(x).toFixed(2)+'" cy="'+Y(v).toFixed(2)+'" r="6" fill="#e29b36"/><text x="48" y="270" fill="currentColor" font-size="15">First slider increases →</text>';
}
sx.addEventListener('input',render);sy.addEventListener('input',render);render();
      } catch (err) {
        console.warn('Sim init error in model 14:', err);
      }
    }
  });

  MODELS.push({
    idx: 15,
    unit: 8,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 15 OF 16 \u00b7 OFFLINE</span><h3>Viscous damping ratio</h3><p>Move the controls to examine one explicitly simplified physical relationship.</p><div class=\"links\"></div></section><p class=\"notice\">Mass fixed at 20 kg; ideal viscous linear model. Synthetic parameter ranges only; not approved for machine sizing or safety decisions.</p><section class=\"sim\"><label for=\"slider-x\">Damping (N s/m): <span id=\"value-x\"></span></label><input type=\"range\" id=\"slider-x\" min=\"10\" max=\"800\" value=\"400\" step=\"any\"><label for=\"slider-y\">Stiffness (kN/m): <span id=\"value-y\"></span></label><input type=\"range\" id=\"slider-y\" min=\"10\" max=\"150\" value=\"80\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 720 282\" role=\"img\" aria-label=\"Model output versus first input\"></svg><p id=\"note\">The plot rescales vertically for each second-slider setting. Compare numbers rather than curve heights between different settings.</p><h2>Analysis questions</h2><p>Find a nonlinear region, if present. Determine whether the output is signed or always nonnegative. Check a physically relevant limiting value using the model equation, then propose an independent observation that would reveal model failure. If a quantity has large sensitivity, identify a manufacturing or instrumentation uncertainty that could make it unreliable.</p></section>",
    init: function(card) {
      try {
const sx=card.querySelector("#" + 'slider-x'.replace(/^#/, "")),sy=card.querySelector("#" + 'slider-y'.replace(/^#/, ""));
const vx=card.querySelector("#" + 'value-x'.replace(/^#/, "")),vy=card.querySelector("#" + 'value-y'.replace(/^#/, "")),out=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const lo=Number(sx.min),hi=Number(sx.max);
function model(x,y){return x/(2*Math.sqrt(y*1000*20));}
function render(){
 const x=Number(sx.value),y=Number(sy.value),v=model(x,y);
 vx.textContent=x.toPrecision(4);vy.textContent=y.toPrecision(4);out.textContent=(Number.isFinite(v)?v.toPrecision(6):'Outside domain')+' ratio';
 const pts=Array.from({length:91},(_,i)=>{let a=lo+(hi-lo)*i/90;return [a,model(a,y)];}).filter(k=>Number.isFinite(k[1]));
 if(pts.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...pts.map(p=>p[1])),vmax=Math.max(...pts.map(p=>p[1]));
 if(vmin===vmax){vmin-=1;vmax+=1;}
 const Y=q=>235-185*(q-vmin)/(vmax-vmin),X=q=>45+630*(q-lo)/(hi-lo);
 const line=pts.map((p,i)=>(i?'L':'M')+X(p[0]).toFixed(2)+','+Y(p[1]).toFixed(2)).join(' ');
 plot.innerHTML='<path d="M45 24 V235 H684" stroke="#8b9aaf" stroke-width="1" fill="none"/><path d="'+line+'" fill="none" stroke="#128397" stroke-width="3"/><circle cx="'+X(x).toFixed(2)+'" cy="'+Y(v).toFixed(2)+'" r="6" fill="#e29b36"/><text x="48" y="270" fill="currentColor" font-size="15">First slider increases →</text>';
}
sx.addEventListener('input',render);sy.addEventListener('input',render);render();
      } catch (err) {
        console.warn('Sim init error in model 15:', err);
      }
    }
  });

  MODELS.push({
    idx: 16,
    unit: 8,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 16 OF 16 \u00b7 OFFLINE</span><h3>Linear tolerance sensitivity</h3><p>Move the controls to examine one explicitly simplified physical relationship.</p><div class=\"links\"></div></section><p class=\"notice\">First-order local output uncertainty estimate; not valid across singularities. Synthetic parameter ranges only; not approved for machine sizing or safety decisions.</p><section class=\"sim\"><label for=\"slider-x\">Input error (mm): <span id=\"value-x\"></span></label><input type=\"range\" id=\"slider-x\" min=\"0\" max=\"1\" value=\"0.25\" step=\"any\"><label for=\"slider-y\">Sensitivity (\u00d7): <span id=\"value-y\"></span></label><input type=\"range\" id=\"slider-y\" min=\"0.1\" max=\"12\" value=\"4\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 720 282\" role=\"img\" aria-label=\"Model output versus first input\"></svg><p id=\"note\">The plot rescales vertically for each second-slider setting. Compare numbers rather than curve heights between different settings.</p><h2>Analysis questions</h2><p>Find a nonlinear region, if present. Determine whether the output is signed or always nonnegative. Check a physically relevant limiting value using the model equation, then propose an independent observation that would reveal model failure. If a quantity has large sensitivity, identify a manufacturing or instrumentation uncertainty that could make it unreliable.</p></section>",
    init: function(card) {
      try {
const sx=card.querySelector("#" + 'slider-x'.replace(/^#/, "")),sy=card.querySelector("#" + 'slider-y'.replace(/^#/, ""));
const vx=card.querySelector("#" + 'value-x'.replace(/^#/, "")),vy=card.querySelector("#" + 'value-y'.replace(/^#/, "")),out=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const lo=Number(sx.min),hi=Number(sx.max);
function model(x,y){return x*y;}
function render(){
 const x=Number(sx.value),y=Number(sy.value),v=model(x,y);
 vx.textContent=x.toPrecision(4);vy.textContent=y.toPrecision(4);out.textContent=(Number.isFinite(v)?v.toPrecision(6):'Outside domain')+' mm';
 const pts=Array.from({length:91},(_,i)=>{let a=lo+(hi-lo)*i/90;return [a,model(a,y)];}).filter(k=>Number.isFinite(k[1]));
 if(pts.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...pts.map(p=>p[1])),vmax=Math.max(...pts.map(p=>p[1]));
 if(vmin===vmax){vmin-=1;vmax+=1;}
 const Y=q=>235-185*(q-vmin)/(vmax-vmin),X=q=>45+630*(q-lo)/(hi-lo);
 const line=pts.map((p,i)=>(i?'L':'M')+X(p[0]).toFixed(2)+','+Y(p[1]).toFixed(2)).join(' ');
 plot.innerHTML='<path d="M45 24 V235 H684" stroke="#8b9aaf" stroke-width="1" fill="none"/><path d="'+line+'" fill="none" stroke="#128397" stroke-width="3"/><circle cx="'+X(x).toFixed(2)+'" cy="'+Y(v).toFixed(2)+'" r="6" fill="#e29b36"/><text x="48" y="270" fill="currentColor" font-size="15">First slider increases →</text>';
}
sx.addEventListener('input',render);sy.addEventListener('input',render);render();
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

    var modelsForUnit = MODELS.filter(function(m) { return m.unit === unitNum; });
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.slice(0, 2);

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
