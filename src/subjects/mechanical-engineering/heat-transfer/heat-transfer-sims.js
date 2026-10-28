/* heat-transfer Interactive Simulation Suite */
(function(window) {
  'use strict';

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: "<div class=\"hero\"><span class=\"pill\">OFFLINE MODEL 01 / 16</span><h3>Slab conduction</h3><p>Explore one explicit mathematical approximation using two independent sliders. The plot and result respond instantly.</p><div class=\"links\"></div></div><div class=\"notice\">Conduction rate for area 2 m\u00b2 and \u0394T=30 K; constant k and no thermal bridges. These are teaching inputs, not calibrated equipment or certified safety limits.</div><section class=\"model\"><label for=\"a\">Thickness L (m): <span id=\"a-value\"></span></label><input id=\"a\" type=\"range\" min=\"0.01\" max=\"0.3\" value=\"0.08\" step=\"any\"><label for=\"b\">Conductivity k (W/(m K)): <span id=\"b-value\"></span></label><input id=\"b\" type=\"range\" min=\"0.04\" max=\"200\" value=\"0.8\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 735 280\" role=\"img\" aria-label=\"Calculated output versus the first slider\"></svg><p id=\"readout\" class=\"mini\"></p><h2>Interpretation exercise</h2><p>Change one parameter while holding the other fixed. Explain the direction of response, check the governing equation and identify a limit in which this approximation becomes invalid. Return both sliders to their starting values and explain why the curve is not empirical evidence of real equipment performance.</p></section>",
    init: function(card) {
      try {
const rangeA=card.querySelector("#" + 'a'.replace(/^#/, "")),rangeB=card.querySelector("#" + 'b'.replace(/^#/, ""));
const valueA=card.querySelector("#" + 'a-value'.replace(/^#/, "")),valueB=card.querySelector("#" + 'b-value'.replace(/^#/, "")),result=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, "")),readout=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const lo=0.01,hi=0.3;
function evaluateModel(L,k){return (k*2*30/L);}
function draw(){
 const L=Number(rangeA.value),k=Number(rangeB.value);
 const y=evaluateModel(L,k);valueA.textContent=L.toPrecision(4);valueB.textContent=k.toPrecision(4);
 result.textContent=Number.isFinite(y)?y.toPrecision(5)+' W':'Outside modeled range';
 const pts=[];const vals=[];
 for(let i=0;i<=70;i++){const x=lo+(hi-lo)*i/70, v=evaluateModel(x,k);if(Number.isFinite(v)){vals.push(v);pts.push([x,v]);}}
 if(vals.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...vals),vmax=Math.max(...vals);if(vmax===vmin){vmin-=1;vmax+=1;}
 let path=pts.map(([x,v],j)=>`${j?'L':'M'}${(45+(x-lo)/(hi-lo)*650).toFixed(1)},${(240-(v-vmin)/(vmax-vmin)*195).toFixed(1)}`).join(' ');
 let dotx=45+(L-lo)/(hi-lo)*650,doty=240-(y-vmin)/(vmax-vmin)*195;
 plot.innerHTML=`<path class="axis" fill="none" d="M45 25 V240 H708"/><path class="bar" fill="none" d="${path}"/><circle cx="${dotx.toFixed(1)}" cy="${doty.toFixed(1)}" r="6" fill="#e89a29"/><text x="52" y="22" font-size="14" fill="currentColor">Output at fixed second input</text><text x="52" y="263" font-size="13" fill="currentColor">Thickness L increases →</text>`;
 readout.textContent='Range along horizontal axis: '+lo+' to '+hi+' m. Output plot rescales vertically to demonstrate trend; it is not a fixed comparison across different second-input settings.';
}
rangeA.addEventListener('input',draw);rangeB.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 1,
    html: "<div class=\"hero\"><span class=\"pill\">OFFLINE MODEL 02 / 16</span><h3>Two-layer wall</h3><p>Explore one explicit mathematical approximation using two independent sliders. The plot and result respond instantly.</p><div class=\"links\"></div></div><div class=\"notice\">Two layers in series; area 2 m\u00b2; base layer 0.02 m with k=0.8; \u0394T=25 K. These are teaching inputs, not calibrated equipment or certified safety limits.</div><section class=\"model\"><label for=\"a\">Insulation thickness (m): <span id=\"a-value\"></span></label><input id=\"a\" type=\"range\" min=\"0.01\" max=\"0.3\" value=\"0.1\" step=\"any\"><label for=\"b\">Insulation k (W/(m K)): <span id=\"b-value\"></span></label><input id=\"b\" type=\"range\" min=\"0.025\" max=\"0.2\" value=\"0.04\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 735 280\" role=\"img\" aria-label=\"Calculated output versus the first slider\"></svg><p id=\"readout\" class=\"mini\"></p><h2>Interpretation exercise</h2><p>Change one parameter while holding the other fixed. Explain the direction of response, check the governing equation and identify a limit in which this approximation becomes invalid. Return both sliders to their starting values and explain why the curve is not empirical evidence of real equipment performance.</p></section>",
    init: function(card) {
      try {
const rangeA=card.querySelector("#" + 'a'.replace(/^#/, "")),rangeB=card.querySelector("#" + 'b'.replace(/^#/, ""));
const valueA=card.querySelector("#" + 'a-value'.replace(/^#/, "")),valueB=card.querySelector("#" + 'b-value'.replace(/^#/, "")),result=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, "")),readout=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const lo=0.01,hi=0.3;
function evaluateModel(L,k){return (2*25/(0.02/.8 + L/k));}
function draw(){
 const L=Number(rangeA.value),k=Number(rangeB.value);
 const y=evaluateModel(L,k);valueA.textContent=L.toPrecision(4);valueB.textContent=k.toPrecision(4);
 result.textContent=Number.isFinite(y)?y.toPrecision(5)+' W':'Outside modeled range';
 const pts=[];const vals=[];
 for(let i=0;i<=70;i++){const x=lo+(hi-lo)*i/70, v=evaluateModel(x,k);if(Number.isFinite(v)){vals.push(v);pts.push([x,v]);}}
 if(vals.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...vals),vmax=Math.max(...vals);if(vmax===vmin){vmin-=1;vmax+=1;}
 let path=pts.map(([x,v],j)=>`${j?'L':'M'}${(45+(x-lo)/(hi-lo)*650).toFixed(1)},${(240-(v-vmin)/(vmax-vmin)*195).toFixed(1)}`).join(' ');
 let dotx=45+(L-lo)/(hi-lo)*650,doty=240-(y-vmin)/(vmax-vmin)*195;
 plot.innerHTML=`<path class="axis" fill="none" d="M45 25 V240 H708"/><path class="bar" fill="none" d="${path}"/><circle cx="${dotx.toFixed(1)}" cy="${doty.toFixed(1)}" r="6" fill="#e89a29"/><text x="52" y="22" font-size="14" fill="currentColor">Output at fixed second input</text><text x="52" y="263" font-size="13" fill="currentColor">Insulation thickness increases →</text>`;
 readout.textContent='Range along horizontal axis: '+lo+' to '+hi+' m. Output plot rescales vertically to demonstrate trend; it is not a fixed comparison across different second-input settings.';
}
rangeA.addEventListener('input',draw);rangeB.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 2,
    html: "<div class=\"hero\"><span class=\"pill\">OFFLINE MODEL 03 / 16</span><h3>Cylindrical insulation</h3><p>Explore one explicit mathematical approximation using two independent sliders. The plot and result respond instantly.</p><div class=\"links\"></div></div><div class=\"notice\">Pipe inner insulation radius 0.02 m, insulated length 1 m and \u0394T=45 K; no external convection. These are teaching inputs, not calibrated equipment or certified safety limits.</div><section class=\"model\"><label for=\"a\">Outer radius (m): <span id=\"a-value\"></span></label><input id=\"a\" type=\"range\" min=\"0.03\" max=\"0.14\" value=\"0.065\" step=\"any\"><label for=\"b\">Thermal conductivity (W/(m K)): <span id=\"b-value\"></span></label><input id=\"b\" type=\"range\" min=\"0.025\" max=\"0.3\" value=\"0.05\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 735 280\" role=\"img\" aria-label=\"Calculated output versus the first slider\"></svg><p id=\"readout\" class=\"mini\"></p><h2>Interpretation exercise</h2><p>Change one parameter while holding the other fixed. Explain the direction of response, check the governing equation and identify a limit in which this approximation becomes invalid. Return both sliders to their starting values and explain why the curve is not empirical evidence of real equipment performance.</p></section>",
    init: function(card) {
      try {
const rangeA=card.querySelector("#" + 'a'.replace(/^#/, "")),rangeB=card.querySelector("#" + 'b'.replace(/^#/, ""));
const valueA=card.querySelector("#" + 'a-value'.replace(/^#/, "")),valueB=card.querySelector("#" + 'b-value'.replace(/^#/, "")),result=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, "")),readout=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const lo=0.03,hi=0.14;
function evaluateModel(L,k){return (2*Math.PI*k*1*45/Math.log(L/.02));}
function draw(){
 const L=Number(rangeA.value),k=Number(rangeB.value);
 const y=evaluateModel(L,k);valueA.textContent=L.toPrecision(4);valueB.textContent=k.toPrecision(4);
 result.textContent=Number.isFinite(y)?y.toPrecision(5)+' W':'Outside modeled range';
 const pts=[];const vals=[];
 for(let i=0;i<=70;i++){const x=lo+(hi-lo)*i/70, v=evaluateModel(x,k);if(Number.isFinite(v)){vals.push(v);pts.push([x,v]);}}
 if(vals.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...vals),vmax=Math.max(...vals);if(vmax===vmin){vmin-=1;vmax+=1;}
 let path=pts.map(([x,v],j)=>`${j?'L':'M'}${(45+(x-lo)/(hi-lo)*650).toFixed(1)},${(240-(v-vmin)/(vmax-vmin)*195).toFixed(1)}`).join(' ');
 let dotx=45+(L-lo)/(hi-lo)*650,doty=240-(y-vmin)/(vmax-vmin)*195;
 plot.innerHTML=`<path class="axis" fill="none" d="M45 25 V240 H708"/><path class="bar" fill="none" d="${path}"/><circle cx="${dotx.toFixed(1)}" cy="${doty.toFixed(1)}" r="6" fill="#e89a29"/><text x="52" y="22" font-size="14" fill="currentColor">Output at fixed second input</text><text x="52" y="263" font-size="13" fill="currentColor">Outer radius increases →</text>`;
 readout.textContent='Range along horizontal axis: '+lo+' to '+hi+' m. Output plot rescales vertically to demonstrate trend; it is not a fixed comparison across different second-input settings.';
}
rangeA.addEventListener('input',draw);rangeB.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 2,
    html: "<div class=\"hero\"><span class=\"pill\">OFFLINE MODEL 04 / 16</span><h3>Straight fin efficiency</h3><p>Explore one explicit mathematical approximation using two independent sliders. The plot and result respond instantly.</p><div class=\"links\"></div></div><div class=\"notice\">Constant cross-section fin, k fin=180 W/(m K), perimeter 0.04 m, area 0.0001 m\u00b2; adiabatic-tip approximation. These are teaching inputs, not calibrated equipment or certified safety limits.</div><section class=\"model\"><label for=\"a\">Fin length (m): <span id=\"a-value\"></span></label><input id=\"a\" type=\"range\" min=\"0.01\" max=\"0.18\" value=\"0.08\" step=\"any\"><label for=\"b\">Convection coefficient (W/(m\u00b2 K)): <span id=\"b-value\"></span></label><input id=\"b\" type=\"range\" min=\"5\" max=\"100\" value=\"18\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 735 280\" role=\"img\" aria-label=\"Calculated output versus the first slider\"></svg><p id=\"readout\" class=\"mini\"></p><h2>Interpretation exercise</h2><p>Change one parameter while holding the other fixed. Explain the direction of response, check the governing equation and identify a limit in which this approximation becomes invalid. Return both sliders to their starting values and explain why the curve is not empirical evidence of real equipment performance.</p></section>",
    init: function(card) {
      try {
const rangeA=card.querySelector("#" + 'a'.replace(/^#/, "")),rangeB=card.querySelector("#" + 'b'.replace(/^#/, ""));
const valueA=card.querySelector("#" + 'a-value'.replace(/^#/, "")),valueB=card.querySelector("#" + 'b-value'.replace(/^#/, "")),result=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, "")),readout=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const lo=0.01,hi=0.18;
function evaluateModel(L,k){return (function(){let m=Math.sqrt(k*.04/(180*.0001));let x=m*L;return Math.tanh(x)/x})();}
function draw(){
 const L=Number(rangeA.value),k=Number(rangeB.value);
 const y=evaluateModel(L,k);valueA.textContent=L.toPrecision(4);valueB.textContent=k.toPrecision(4);
 result.textContent=Number.isFinite(y)?y.toPrecision(5)+' fraction':'Outside modeled range';
 const pts=[];const vals=[];
 for(let i=0;i<=70;i++){const x=lo+(hi-lo)*i/70, v=evaluateModel(x,k);if(Number.isFinite(v)){vals.push(v);pts.push([x,v]);}}
 if(vals.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...vals),vmax=Math.max(...vals);if(vmax===vmin){vmin-=1;vmax+=1;}
 let path=pts.map(([x,v],j)=>`${j?'L':'M'}${(45+(x-lo)/(hi-lo)*650).toFixed(1)},${(240-(v-vmin)/(vmax-vmin)*195).toFixed(1)}`).join(' ');
 let dotx=45+(L-lo)/(hi-lo)*650,doty=240-(y-vmin)/(vmax-vmin)*195;
 plot.innerHTML=`<path class="axis" fill="none" d="M45 25 V240 H708"/><path class="bar" fill="none" d="${path}"/><circle cx="${dotx.toFixed(1)}" cy="${doty.toFixed(1)}" r="6" fill="#e89a29"/><text x="52" y="22" font-size="14" fill="currentColor">Output at fixed second input</text><text x="52" y="263" font-size="13" fill="currentColor">Fin length increases →</text>`;
 readout.textContent='Range along horizontal axis: '+lo+' to '+hi+' m. Output plot rescales vertically to demonstrate trend; it is not a fixed comparison across different second-input settings.';
}
rangeA.addEventListener('input',draw);rangeB.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 3,
    html: "<div class=\"hero\"><span class=\"pill\">OFFLINE MODEL 05 / 16</span><h3>Lumped cooling</h3><p>Explore one explicit mathematical approximation using two independent sliders. The plot and result respond instantly.</p><div class=\"links\"></div></div><div class=\"notice\">Initial body 370 K, environment 300 K, mass 0.1 kg, c=500 J/(kg K); requires small Biot number. These are teaching inputs, not calibrated equipment or certified safety limits.</div><section class=\"model\"><label for=\"a\">Elapsed time (s): <span id=\"a-value\"></span></label><input id=\"a\" type=\"range\" min=\"0\" max=\"600\" value=\"120\" step=\"any\"><label for=\"b\">hA conductance (W/K): <span id=\"b-value\"></span></label><input id=\"b\" type=\"range\" min=\"0.2\" max=\"5\" value=\"1\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 735 280\" role=\"img\" aria-label=\"Calculated output versus the first slider\"></svg><p id=\"readout\" class=\"mini\"></p><h2>Interpretation exercise</h2><p>Change one parameter while holding the other fixed. Explain the direction of response, check the governing equation and identify a limit in which this approximation becomes invalid. Return both sliders to their starting values and explain why the curve is not empirical evidence of real equipment performance.</p></section>",
    init: function(card) {
      try {
const rangeA=card.querySelector("#" + 'a'.replace(/^#/, "")),rangeB=card.querySelector("#" + 'b'.replace(/^#/, ""));
const valueA=card.querySelector("#" + 'a-value'.replace(/^#/, "")),valueB=card.querySelector("#" + 'b-value'.replace(/^#/, "")),result=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, "")),readout=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const lo=0,hi=600;
function evaluateModel(L,k){return (300 + 70*Math.exp(-k*L/(.1*500)));}
function draw(){
 const L=Number(rangeA.value),k=Number(rangeB.value);
 const y=evaluateModel(L,k);valueA.textContent=L.toPrecision(4);valueB.textContent=k.toPrecision(4);
 result.textContent=Number.isFinite(y)?y.toPrecision(5)+' K':'Outside modeled range';
 const pts=[];const vals=[];
 for(let i=0;i<=70;i++){const x=lo+(hi-lo)*i/70, v=evaluateModel(x,k);if(Number.isFinite(v)){vals.push(v);pts.push([x,v]);}}
 if(vals.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...vals),vmax=Math.max(...vals);if(vmax===vmin){vmin-=1;vmax+=1;}
 let path=pts.map(([x,v],j)=>`${j?'L':'M'}${(45+(x-lo)/(hi-lo)*650).toFixed(1)},${(240-(v-vmin)/(vmax-vmin)*195).toFixed(1)}`).join(' ');
 let dotx=45+(L-lo)/(hi-lo)*650,doty=240-(y-vmin)/(vmax-vmin)*195;
 plot.innerHTML=`<path class="axis" fill="none" d="M45 25 V240 H708"/><path class="bar" fill="none" d="${path}"/><circle cx="${dotx.toFixed(1)}" cy="${doty.toFixed(1)}" r="6" fill="#e89a29"/><text x="52" y="22" font-size="14" fill="currentColor">Output at fixed second input</text><text x="52" y="263" font-size="13" fill="currentColor">Elapsed time increases →</text>`;
 readout.textContent='Range along horizontal axis: '+lo+' to '+hi+' s. Output plot rescales vertically to demonstrate trend; it is not a fixed comparison across different second-input settings.';
}
rangeA.addEventListener('input',draw);rangeB.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 3,
    html: "<div class=\"hero\"><span class=\"pill\">OFFLINE MODEL 06 / 16</span><h3>Biot number</h3><p>Explore one explicit mathematical approximation using two independent sliders. The plot and result respond instantly.</p><div class=\"links\"></div></div><div class=\"notice\">Bi=hLc/k with constant solid conductivity k=16 W/(m K), Lc approximated by half thickness. These are teaching inputs, not calibrated equipment or certified safety limits.</div><section class=\"model\"><label for=\"a\">Half thickness (m): <span id=\"a-value\"></span></label><input id=\"a\" type=\"range\" min=\"0.001\" max=\"0.06\" value=\"0.012\" step=\"any\"><label for=\"b\">Convection h (W/(m\u00b2 K)): <span id=\"b-value\"></span></label><input id=\"b\" type=\"range\" min=\"2\" max=\"120\" value=\"20\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 735 280\" role=\"img\" aria-label=\"Calculated output versus the first slider\"></svg><p id=\"readout\" class=\"mini\"></p><h2>Interpretation exercise</h2><p>Change one parameter while holding the other fixed. Explain the direction of response, check the governing equation and identify a limit in which this approximation becomes invalid. Return both sliders to their starting values and explain why the curve is not empirical evidence of real equipment performance.</p></section>",
    init: function(card) {
      try {
const rangeA=card.querySelector("#" + 'a'.replace(/^#/, "")),rangeB=card.querySelector("#" + 'b'.replace(/^#/, ""));
const valueA=card.querySelector("#" + 'a-value'.replace(/^#/, "")),valueB=card.querySelector("#" + 'b-value'.replace(/^#/, "")),result=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, "")),readout=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const lo=0.001,hi=0.06;
function evaluateModel(L,k){return (k*L/16);}
function draw(){
 const L=Number(rangeA.value),k=Number(rangeB.value);
 const y=evaluateModel(L,k);valueA.textContent=L.toPrecision(4);valueB.textContent=k.toPrecision(4);
 result.textContent=Number.isFinite(y)?y.toPrecision(5)+' dimensionless':'Outside modeled range';
 const pts=[];const vals=[];
 for(let i=0;i<=70;i++){const x=lo+(hi-lo)*i/70, v=evaluateModel(x,k);if(Number.isFinite(v)){vals.push(v);pts.push([x,v]);}}
 if(vals.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...vals),vmax=Math.max(...vals);if(vmax===vmin){vmin-=1;vmax+=1;}
 let path=pts.map(([x,v],j)=>`${j?'L':'M'}${(45+(x-lo)/(hi-lo)*650).toFixed(1)},${(240-(v-vmin)/(vmax-vmin)*195).toFixed(1)}`).join(' ');
 let dotx=45+(L-lo)/(hi-lo)*650,doty=240-(y-vmin)/(vmax-vmin)*195;
 plot.innerHTML=`<path class="axis" fill="none" d="M45 25 V240 H708"/><path class="bar" fill="none" d="${path}"/><circle cx="${dotx.toFixed(1)}" cy="${doty.toFixed(1)}" r="6" fill="#e89a29"/><text x="52" y="22" font-size="14" fill="currentColor">Output at fixed second input</text><text x="52" y="263" font-size="13" fill="currentColor">Half thickness increases →</text>`;
 readout.textContent='Range along horizontal axis: '+lo+' to '+hi+' m. Output plot rescales vertically to demonstrate trend; it is not a fixed comparison across different second-input settings.';
}
rangeA.addEventListener('input',draw);rangeB.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 4,
    html: "<div class=\"hero\"><span class=\"pill\">OFFLINE MODEL 07 / 16</span><h3>Fourier number</h3><p>Explore one explicit mathematical approximation using two independent sliders. The plot and result respond instantly.</p><div class=\"links\"></div></div><div class=\"notice\">Fo=\u03b1t/Lc\u00b2 with characteristic length 0.02 m; a dimensionless diffusion time, not a temperature. These are teaching inputs, not calibrated equipment or certified safety limits.</div><section class=\"model\"><label for=\"a\">Elapsed time (s): <span id=\"a-value\"></span></label><input id=\"a\" type=\"range\" min=\"0\" max=\"2000\" value=\"320\" step=\"any\"><label for=\"b\">Thermal diffusivity (m\u00b2/s): <span id=\"b-value\"></span></label><input id=\"b\" type=\"range\" min=\"1e-06\" max=\"3e-05\" value=\"1e-05\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 735 280\" role=\"img\" aria-label=\"Calculated output versus the first slider\"></svg><p id=\"readout\" class=\"mini\"></p><h2>Interpretation exercise</h2><p>Change one parameter while holding the other fixed. Explain the direction of response, check the governing equation and identify a limit in which this approximation becomes invalid. Return both sliders to their starting values and explain why the curve is not empirical evidence of real equipment performance.</p></section>",
    init: function(card) {
      try {
const rangeA=card.querySelector("#" + 'a'.replace(/^#/, "")),rangeB=card.querySelector("#" + 'b'.replace(/^#/, ""));
const valueA=card.querySelector("#" + 'a-value'.replace(/^#/, "")),valueB=card.querySelector("#" + 'b-value'.replace(/^#/, "")),result=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, "")),readout=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const lo=0,hi=2000;
function evaluateModel(L,k){return (k*L/(.02*.02));}
function draw(){
 const L=Number(rangeA.value),k=Number(rangeB.value);
 const y=evaluateModel(L,k);valueA.textContent=L.toPrecision(4);valueB.textContent=k.toPrecision(4);
 result.textContent=Number.isFinite(y)?y.toPrecision(5)+' dimensionless':'Outside modeled range';
 const pts=[];const vals=[];
 for(let i=0;i<=70;i++){const x=lo+(hi-lo)*i/70, v=evaluateModel(x,k);if(Number.isFinite(v)){vals.push(v);pts.push([x,v]);}}
 if(vals.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...vals),vmax=Math.max(...vals);if(vmax===vmin){vmin-=1;vmax+=1;}
 let path=pts.map(([x,v],j)=>`${j?'L':'M'}${(45+(x-lo)/(hi-lo)*650).toFixed(1)},${(240-(v-vmin)/(vmax-vmin)*195).toFixed(1)}`).join(' ');
 let dotx=45+(L-lo)/(hi-lo)*650,doty=240-(y-vmin)/(vmax-vmin)*195;
 plot.innerHTML=`<path class="axis" fill="none" d="M45 25 V240 H708"/><path class="bar" fill="none" d="${path}"/><circle cx="${dotx.toFixed(1)}" cy="${doty.toFixed(1)}" r="6" fill="#e89a29"/><text x="52" y="22" font-size="14" fill="currentColor">Output at fixed second input</text><text x="52" y="263" font-size="13" fill="currentColor">Elapsed time increases →</text>`;
 readout.textContent='Range along horizontal axis: '+lo+' to '+hi+' s. Output plot rescales vertically to demonstrate trend; it is not a fixed comparison across different second-input settings.';
}
rangeA.addEventListener('input',draw);rangeB.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 4,
    html: "<div class=\"hero\"><span class=\"pill\">OFFLINE MODEL 08 / 16</span><h3>Forced convection over a plate</h3><p>Explore one explicit mathematical approximation using two independent sliders. The plot and result respond instantly.</p><div class=\"links\"></div></div><div class=\"notice\">Mean h from laminar average Nu correlation, air \u03c1=1.2 kg/m\u00b3, \u03bc=1.8e\u22125 Pa\u00b7s, Pr=0.71 and kf=0.026 W/(m K). These are teaching inputs, not calibrated equipment or certified safety limits.</div><section class=\"model\"><label for=\"a\">Air speed (m/s): <span id=\"a-value\"></span></label><input id=\"a\" type=\"range\" min=\"0.2\" max=\"12\" value=\"3\" step=\"any\"><label for=\"b\">Plate length (m): <span id=\"b-value\"></span></label><input id=\"b\" type=\"range\" min=\"0.05\" max=\"0.8\" value=\"0.3\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 735 280\" role=\"img\" aria-label=\"Calculated output versus the first slider\"></svg><p id=\"readout\" class=\"mini\"></p><h2>Interpretation exercise</h2><p>Change one parameter while holding the other fixed. Explain the direction of response, check the governing equation and identify a limit in which this approximation becomes invalid. Return both sliders to their starting values and explain why the curve is not empirical evidence of real equipment performance.</p></section>",
    init: function(card) {
      try {
const rangeA=card.querySelector("#" + 'a'.replace(/^#/, "")),rangeB=card.querySelector("#" + 'b'.replace(/^#/, ""));
const valueA=card.querySelector("#" + 'a-value'.replace(/^#/, "")),valueB=card.querySelector("#" + 'b-value'.replace(/^#/, "")),result=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, "")),readout=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const lo=0.2,hi=12;
function evaluateModel(L,k){return (function(){let Re=1.2*L*k/1.8e-5; let Nu=.664*Math.sqrt(Re)*Math.pow(.71,1/3);return Nu*.026/k})();}
function draw(){
 const L=Number(rangeA.value),k=Number(rangeB.value);
 const y=evaluateModel(L,k);valueA.textContent=L.toPrecision(4);valueB.textContent=k.toPrecision(4);
 result.textContent=Number.isFinite(y)?y.toPrecision(5)+' W/(m² K)':'Outside modeled range';
 const pts=[];const vals=[];
 for(let i=0;i<=70;i++){const x=lo+(hi-lo)*i/70, v=evaluateModel(x,k);if(Number.isFinite(v)){vals.push(v);pts.push([x,v]);}}
 if(vals.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...vals),vmax=Math.max(...vals);if(vmax===vmin){vmin-=1;vmax+=1;}
 let path=pts.map(([x,v],j)=>`${j?'L':'M'}${(45+(x-lo)/(hi-lo)*650).toFixed(1)},${(240-(v-vmin)/(vmax-vmin)*195).toFixed(1)}`).join(' ');
 let dotx=45+(L-lo)/(hi-lo)*650,doty=240-(y-vmin)/(vmax-vmin)*195;
 plot.innerHTML=`<path class="axis" fill="none" d="M45 25 V240 H708"/><path class="bar" fill="none" d="${path}"/><circle cx="${dotx.toFixed(1)}" cy="${doty.toFixed(1)}" r="6" fill="#e89a29"/><text x="52" y="22" font-size="14" fill="currentColor">Output at fixed second input</text><text x="52" y="263" font-size="13" fill="currentColor">Air speed increases →</text>`;
 readout.textContent='Range along horizontal axis: '+lo+' to '+hi+' m/s. Output plot rescales vertically to demonstrate trend; it is not a fixed comparison across different second-input settings.';
}
rangeA.addEventListener('input',draw);rangeB.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  MODELS.push({
    idx: 9,
    unit: 5,
    html: "<div class=\"hero\"><span class=\"pill\">OFFLINE MODEL 09 / 16</span><h3>Laminar tube convection</h3><p>Explore one explicit mathematical approximation using two independent sliders. The plot and result respond instantly.</p><div class=\"links\"></div></div><div class=\"notice\">Ideal thermally fully-developed laminar circular-tube convection at constant wall temperature; no entrance effects. These are teaching inputs, not calibrated equipment or certified safety limits.</div><section class=\"model\"><label for=\"a\">Tube diameter (m): <span id=\"a-value\"></span></label><input id=\"a\" type=\"range\" min=\"0.003\" max=\"0.08\" value=\"0.02\" step=\"any\"><label for=\"b\">Fluid conductivity (W/(m K)): <span id=\"b-value\"></span></label><input id=\"b\" type=\"range\" min=\"0.02\" max=\"0.65\" value=\"0.6\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 735 280\" role=\"img\" aria-label=\"Calculated output versus the first slider\"></svg><p id=\"readout\" class=\"mini\"></p><h2>Interpretation exercise</h2><p>Change one parameter while holding the other fixed. Explain the direction of response, check the governing equation and identify a limit in which this approximation becomes invalid. Return both sliders to their starting values and explain why the curve is not empirical evidence of real equipment performance.</p></section>",
    init: function(card) {
      try {
const rangeA=card.querySelector("#" + 'a'.replace(/^#/, "")),rangeB=card.querySelector("#" + 'b'.replace(/^#/, ""));
const valueA=card.querySelector("#" + 'a-value'.replace(/^#/, "")),valueB=card.querySelector("#" + 'b-value'.replace(/^#/, "")),result=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, "")),readout=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const lo=0.003,hi=0.08;
function evaluateModel(L,k){return (3.66*k/L);}
function draw(){
 const L=Number(rangeA.value),k=Number(rangeB.value);
 const y=evaluateModel(L,k);valueA.textContent=L.toPrecision(4);valueB.textContent=k.toPrecision(4);
 result.textContent=Number.isFinite(y)?y.toPrecision(5)+' W/(m² K)':'Outside modeled range';
 const pts=[];const vals=[];
 for(let i=0;i<=70;i++){const x=lo+(hi-lo)*i/70, v=evaluateModel(x,k);if(Number.isFinite(v)){vals.push(v);pts.push([x,v]);}}
 if(vals.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...vals),vmax=Math.max(...vals);if(vmax===vmin){vmin-=1;vmax+=1;}
 let path=pts.map(([x,v],j)=>`${j?'L':'M'}${(45+(x-lo)/(hi-lo)*650).toFixed(1)},${(240-(v-vmin)/(vmax-vmin)*195).toFixed(1)}`).join(' ');
 let dotx=45+(L-lo)/(hi-lo)*650,doty=240-(y-vmin)/(vmax-vmin)*195;
 plot.innerHTML=`<path class="axis" fill="none" d="M45 25 V240 H708"/><path class="bar" fill="none" d="${path}"/><circle cx="${dotx.toFixed(1)}" cy="${doty.toFixed(1)}" r="6" fill="#e89a29"/><text x="52" y="22" font-size="14" fill="currentColor">Output at fixed second input</text><text x="52" y="263" font-size="13" fill="currentColor">Tube diameter increases →</text>`;
 readout.textContent='Range along horizontal axis: '+lo+' to '+hi+' m. Output plot rescales vertically to demonstrate trend; it is not a fixed comparison across different second-input settings.';
}
rangeA.addEventListener('input',draw);rangeB.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 9:', err);
      }
    }
  });

  MODELS.push({
    idx: 10,
    unit: 5,
    html: "<div class=\"hero\"><span class=\"pill\">OFFLINE MODEL 10 / 16</span><h3>Turbulent tube convection</h3><p>Explore one explicit mathematical approximation using two independent sliders. The plot and result respond instantly.</p><div class=\"links\"></div></div><div class=\"notice\">Dittus\u2013Boelter approximation for smooth-tube heating, D=0.02 m and kf=0.6 W/(m K); restricted range. These are teaching inputs, not calibrated equipment or certified safety limits.</div><section class=\"model\"><label for=\"a\">Reynolds number (dimensionless): <span id=\"a-value\"></span></label><input id=\"a\" type=\"range\" min=\"10000\" max=\"120000\" value=\"35000\" step=\"any\"><label for=\"b\">Prandtl number (dimensionless): <span id=\"b-value\"></span></label><input id=\"b\" type=\"range\" min=\"0.7\" max=\"8\" value=\"3\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 735 280\" role=\"img\" aria-label=\"Calculated output versus the first slider\"></svg><p id=\"readout\" class=\"mini\"></p><h2>Interpretation exercise</h2><p>Change one parameter while holding the other fixed. Explain the direction of response, check the governing equation and identify a limit in which this approximation becomes invalid. Return both sliders to their starting values and explain why the curve is not empirical evidence of real equipment performance.</p></section>",
    init: function(card) {
      try {
const rangeA=card.querySelector("#" + 'a'.replace(/^#/, "")),rangeB=card.querySelector("#" + 'b'.replace(/^#/, ""));
const valueA=card.querySelector("#" + 'a-value'.replace(/^#/, "")),valueB=card.querySelector("#" + 'b-value'.replace(/^#/, "")),result=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, "")),readout=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const lo=10000,hi=120000;
function evaluateModel(L,k){return (function(){let Nu=.023*Math.pow(L,.8)*Math.pow(k,.4);return Nu*.6/.02})();}
function draw(){
 const L=Number(rangeA.value),k=Number(rangeB.value);
 const y=evaluateModel(L,k);valueA.textContent=L.toPrecision(4);valueB.textContent=k.toPrecision(4);
 result.textContent=Number.isFinite(y)?y.toPrecision(5)+' W/(m² K)':'Outside modeled range';
 const pts=[];const vals=[];
 for(let i=0;i<=70;i++){const x=lo+(hi-lo)*i/70, v=evaluateModel(x,k);if(Number.isFinite(v)){vals.push(v);pts.push([x,v]);}}
 if(vals.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...vals),vmax=Math.max(...vals);if(vmax===vmin){vmin-=1;vmax+=1;}
 let path=pts.map(([x,v],j)=>`${j?'L':'M'}${(45+(x-lo)/(hi-lo)*650).toFixed(1)},${(240-(v-vmin)/(vmax-vmin)*195).toFixed(1)}`).join(' ');
 let dotx=45+(L-lo)/(hi-lo)*650,doty=240-(y-vmin)/(vmax-vmin)*195;
 plot.innerHTML=`<path class="axis" fill="none" d="M45 25 V240 H708"/><path class="bar" fill="none" d="${path}"/><circle cx="${dotx.toFixed(1)}" cy="${doty.toFixed(1)}" r="6" fill="#e89a29"/><text x="52" y="22" font-size="14" fill="currentColor">Output at fixed second input</text><text x="52" y="263" font-size="13" fill="currentColor">Reynolds number increases →</text>`;
 readout.textContent='Range along horizontal axis: '+lo+' to '+hi+' dimensionless. Output plot rescales vertically to demonstrate trend; it is not a fixed comparison across different second-input settings.';
}
rangeA.addEventListener('input',draw);rangeB.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 10:', err);
      }
    }
  });

  MODELS.push({
    idx: 11,
    unit: 6,
    html: "<div class=\"hero\"><span class=\"pill\">OFFLINE MODEL 11 / 16</span><h3>Idealized freezing front</h3><p>Explore one explicit mathematical approximation using two independent sliders. The plot and result respond instantly.</p><div class=\"links\"></div></div><div class=\"notice\">One-phase quasi-steady planar Stefan approximation; ice \u03c1=920 kg/m\u00b3, k=2.2 W/(m K), latent heat 334 kJ/kg. These are teaching inputs, not calibrated equipment or certified safety limits.</div><section class=\"model\"><label for=\"a\">Elapsed time (s): <span id=\"a-value\"></span></label><input id=\"a\" type=\"range\" min=\"0\" max=\"3600\" value=\"300\" step=\"any\"><label for=\"b\">Temperature difference (K): <span id=\"b-value\"></span></label><input id=\"b\" type=\"range\" min=\"1\" max=\"30\" value=\"12\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 735 280\" role=\"img\" aria-label=\"Calculated output versus the first slider\"></svg><p id=\"readout\" class=\"mini\"></p><h2>Interpretation exercise</h2><p>Change one parameter while holding the other fixed. Explain the direction of response, check the governing equation and identify a limit in which this approximation becomes invalid. Return both sliders to their starting values and explain why the curve is not empirical evidence of real equipment performance.</p></section>",
    init: function(card) {
      try {
const rangeA=card.querySelector("#" + 'a'.replace(/^#/, "")),rangeB=card.querySelector("#" + 'b'.replace(/^#/, ""));
const valueA=card.querySelector("#" + 'a-value'.replace(/^#/, "")),valueB=card.querySelector("#" + 'b-value'.replace(/^#/, "")),result=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, "")),readout=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const lo=0,hi=3600;
function evaluateModel(L,k){return (1000*Math.sqrt(2*2.2*k*L/(920*334000)));}
function draw(){
 const L=Number(rangeA.value),k=Number(rangeB.value);
 const y=evaluateModel(L,k);valueA.textContent=L.toPrecision(4);valueB.textContent=k.toPrecision(4);
 result.textContent=Number.isFinite(y)?y.toPrecision(5)+' mm':'Outside modeled range';
 const pts=[];const vals=[];
 for(let i=0;i<=70;i++){const x=lo+(hi-lo)*i/70, v=evaluateModel(x,k);if(Number.isFinite(v)){vals.push(v);pts.push([x,v]);}}
 if(vals.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...vals),vmax=Math.max(...vals);if(vmax===vmin){vmin-=1;vmax+=1;}
 let path=pts.map(([x,v],j)=>`${j?'L':'M'}${(45+(x-lo)/(hi-lo)*650).toFixed(1)},${(240-(v-vmin)/(vmax-vmin)*195).toFixed(1)}`).join(' ');
 let dotx=45+(L-lo)/(hi-lo)*650,doty=240-(y-vmin)/(vmax-vmin)*195;
 plot.innerHTML=`<path class="axis" fill="none" d="M45 25 V240 H708"/><path class="bar" fill="none" d="${path}"/><circle cx="${dotx.toFixed(1)}" cy="${doty.toFixed(1)}" r="6" fill="#e89a29"/><text x="52" y="22" font-size="14" fill="currentColor">Output at fixed second input</text><text x="52" y="263" font-size="13" fill="currentColor">Elapsed time increases →</text>`;
 readout.textContent='Range along horizontal axis: '+lo+' to '+hi+' s. Output plot rescales vertically to demonstrate trend; it is not a fixed comparison across different second-input settings.';
}
rangeA.addEventListener('input',draw);rangeB.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 11:', err);
      }
    }
  });

  MODELS.push({
    idx: 12,
    unit: 6,
    html: "<div class=\"hero\"><span class=\"pill\">OFFLINE MODEL 12 / 16</span><h3>Radiative exchange</h3><p>Explore one explicit mathematical approximation using two independent sliders. The plot and result respond instantly.</p><div class=\"links\"></div></div><div class=\"notice\">Single diffuse-gray surface with large surroundings at 300 K; constant emissivity. These are teaching inputs, not calibrated equipment or certified safety limits.</div><section class=\"model\"><label for=\"a\">Surface temperature (K): <span id=\"a-value\"></span></label><input id=\"a\" type=\"range\" min=\"300\" max=\"1000\" value=\"450\" step=\"any\"><label for=\"b\">Surface emissivity (fraction): <span id=\"b-value\"></span></label><input id=\"b\" type=\"range\" min=\"0.1\" max=\"1\" value=\"0.8\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 735 280\" role=\"img\" aria-label=\"Calculated output versus the first slider\"></svg><p id=\"readout\" class=\"mini\"></p><h2>Interpretation exercise</h2><p>Change one parameter while holding the other fixed. Explain the direction of response, check the governing equation and identify a limit in which this approximation becomes invalid. Return both sliders to their starting values and explain why the curve is not empirical evidence of real equipment performance.</p></section>",
    init: function(card) {
      try {
const rangeA=card.querySelector("#" + 'a'.replace(/^#/, "")),rangeB=card.querySelector("#" + 'b'.replace(/^#/, ""));
const valueA=card.querySelector("#" + 'a-value'.replace(/^#/, "")),valueB=card.querySelector("#" + 'b-value'.replace(/^#/, "")),result=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, "")),readout=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const lo=300,hi=1000;
function evaluateModel(L,k){return (k*5.670374419e-8*(Math.pow(L,4)-Math.pow(300,4)));}
function draw(){
 const L=Number(rangeA.value),k=Number(rangeB.value);
 const y=evaluateModel(L,k);valueA.textContent=L.toPrecision(4);valueB.textContent=k.toPrecision(4);
 result.textContent=Number.isFinite(y)?y.toPrecision(5)+' W/m²':'Outside modeled range';
 const pts=[];const vals=[];
 for(let i=0;i<=70;i++){const x=lo+(hi-lo)*i/70, v=evaluateModel(x,k);if(Number.isFinite(v)){vals.push(v);pts.push([x,v]);}}
 if(vals.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...vals),vmax=Math.max(...vals);if(vmax===vmin){vmin-=1;vmax+=1;}
 let path=pts.map(([x,v],j)=>`${j?'L':'M'}${(45+(x-lo)/(hi-lo)*650).toFixed(1)},${(240-(v-vmin)/(vmax-vmin)*195).toFixed(1)}`).join(' ');
 let dotx=45+(L-lo)/(hi-lo)*650,doty=240-(y-vmin)/(vmax-vmin)*195;
 plot.innerHTML=`<path class="axis" fill="none" d="M45 25 V240 H708"/><path class="bar" fill="none" d="${path}"/><circle cx="${dotx.toFixed(1)}" cy="${doty.toFixed(1)}" r="6" fill="#e89a29"/><text x="52" y="22" font-size="14" fill="currentColor">Output at fixed second input</text><text x="52" y="263" font-size="13" fill="currentColor">Surface temperature increases →</text>`;
 readout.textContent='Range along horizontal axis: '+lo+' to '+hi+' K. Output plot rescales vertically to demonstrate trend; it is not a fixed comparison across different second-input settings.';
}
rangeA.addEventListener('input',draw);rangeB.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 12:', err);
      }
    }
  });

  MODELS.push({
    idx: 13,
    unit: 7,
    html: "<div class=\"hero\"><span class=\"pill\">OFFLINE MODEL 13 / 16</span><h3>Two-surface radiation</h3><p>Explore one explicit mathematical approximation using two independent sliders. The plot and result respond instantly.</p><div class=\"links\"></div></div><div class=\"notice\">Large facing diffuse-gray plates; cold surface 300 K, emissivity 0.8; zero intermediary shields. These are teaching inputs, not calibrated equipment or certified safety limits.</div><section class=\"model\"><label for=\"a\">Hot surface (K): <span id=\"a-value\"></span></label><input id=\"a\" type=\"range\" min=\"350\" max=\"900\" value=\"520\" step=\"any\"><label for=\"b\">Hot emissivity (fraction): <span id=\"b-value\"></span></label><input id=\"b\" type=\"range\" min=\"0.1\" max=\"1\" value=\"0.7\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 735 280\" role=\"img\" aria-label=\"Calculated output versus the first slider\"></svg><p id=\"readout\" class=\"mini\"></p><h2>Interpretation exercise</h2><p>Change one parameter while holding the other fixed. Explain the direction of response, check the governing equation and identify a limit in which this approximation becomes invalid. Return both sliders to their starting values and explain why the curve is not empirical evidence of real equipment performance.</p></section>",
    init: function(card) {
      try {
const rangeA=card.querySelector("#" + 'a'.replace(/^#/, "")),rangeB=card.querySelector("#" + 'b'.replace(/^#/, ""));
const valueA=card.querySelector("#" + 'a-value'.replace(/^#/, "")),valueB=card.querySelector("#" + 'b-value'.replace(/^#/, "")),result=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, "")),readout=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const lo=350,hi=900;
function evaluateModel(L,k){return (5.670374419e-8*(Math.pow(L,4)-Math.pow(300,4))/(1/k+1/.8-1));}
function draw(){
 const L=Number(rangeA.value),k=Number(rangeB.value);
 const y=evaluateModel(L,k);valueA.textContent=L.toPrecision(4);valueB.textContent=k.toPrecision(4);
 result.textContent=Number.isFinite(y)?y.toPrecision(5)+' W/m²':'Outside modeled range';
 const pts=[];const vals=[];
 for(let i=0;i<=70;i++){const x=lo+(hi-lo)*i/70, v=evaluateModel(x,k);if(Number.isFinite(v)){vals.push(v);pts.push([x,v]);}}
 if(vals.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...vals),vmax=Math.max(...vals);if(vmax===vmin){vmin-=1;vmax+=1;}
 let path=pts.map(([x,v],j)=>`${j?'L':'M'}${(45+(x-lo)/(hi-lo)*650).toFixed(1)},${(240-(v-vmin)/(vmax-vmin)*195).toFixed(1)}`).join(' ');
 let dotx=45+(L-lo)/(hi-lo)*650,doty=240-(y-vmin)/(vmax-vmin)*195;
 plot.innerHTML=`<path class="axis" fill="none" d="M45 25 V240 H708"/><path class="bar" fill="none" d="${path}"/><circle cx="${dotx.toFixed(1)}" cy="${doty.toFixed(1)}" r="6" fill="#e89a29"/><text x="52" y="22" font-size="14" fill="currentColor">Output at fixed second input</text><text x="52" y="263" font-size="13" fill="currentColor">Hot surface increases →</text>`;
 readout.textContent='Range along horizontal axis: '+lo+' to '+hi+' K. Output plot rescales vertically to demonstrate trend; it is not a fixed comparison across different second-input settings.';
}
rangeA.addEventListener('input',draw);rangeB.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 13:', err);
      }
    }
  });

  MODELS.push({
    idx: 14,
    unit: 7,
    html: "<div class=\"hero\"><span class=\"pill\">OFFLINE MODEL 14 / 16</span><h3>Log-mean temperature difference</h3><p>Explore one explicit mathematical approximation using two independent sliders. The plot and result respond instantly.</p><div class=\"links\"></div></div><div class=\"notice\">LMTD for positive terminal differences in the chosen exchanger flow arrangement; no temperature crossing. These are teaching inputs, not calibrated equipment or certified safety limits.</div><section class=\"model\"><label for=\"a\">Hot-end difference (K): <span id=\"a-value\"></span></label><input id=\"a\" type=\"range\" min=\"2\" max=\"75\" value=\"40\" step=\"any\"><label for=\"b\">Cold-end difference (K): <span id=\"b-value\"></span></label><input id=\"b\" type=\"range\" min=\"2\" max=\"75\" value=\"18\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 735 280\" role=\"img\" aria-label=\"Calculated output versus the first slider\"></svg><p id=\"readout\" class=\"mini\"></p><h2>Interpretation exercise</h2><p>Change one parameter while holding the other fixed. Explain the direction of response, check the governing equation and identify a limit in which this approximation becomes invalid. Return both sliders to their starting values and explain why the curve is not empirical evidence of real equipment performance.</p></section>",
    init: function(card) {
      try {
const rangeA=card.querySelector("#" + 'a'.replace(/^#/, "")),rangeB=card.querySelector("#" + 'b'.replace(/^#/, ""));
const valueA=card.querySelector("#" + 'a-value'.replace(/^#/, "")),valueB=card.querySelector("#" + 'b-value'.replace(/^#/, "")),result=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, "")),readout=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const lo=2,hi=75;
function evaluateModel(L,k){return (Math.abs(L-k)<1e-9?L:(L-k)/Math.log(L/k));}
function draw(){
 const L=Number(rangeA.value),k=Number(rangeB.value);
 const y=evaluateModel(L,k);valueA.textContent=L.toPrecision(4);valueB.textContent=k.toPrecision(4);
 result.textContent=Number.isFinite(y)?y.toPrecision(5)+' K':'Outside modeled range';
 const pts=[];const vals=[];
 for(let i=0;i<=70;i++){const x=lo+(hi-lo)*i/70, v=evaluateModel(x,k);if(Number.isFinite(v)){vals.push(v);pts.push([x,v]);}}
 if(vals.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...vals),vmax=Math.max(...vals);if(vmax===vmin){vmin-=1;vmax+=1;}
 let path=pts.map(([x,v],j)=>`${j?'L':'M'}${(45+(x-lo)/(hi-lo)*650).toFixed(1)},${(240-(v-vmin)/(vmax-vmin)*195).toFixed(1)}`).join(' ');
 let dotx=45+(L-lo)/(hi-lo)*650,doty=240-(y-vmin)/(vmax-vmin)*195;
 plot.innerHTML=`<path class="axis" fill="none" d="M45 25 V240 H708"/><path class="bar" fill="none" d="${path}"/><circle cx="${dotx.toFixed(1)}" cy="${doty.toFixed(1)}" r="6" fill="#e89a29"/><text x="52" y="22" font-size="14" fill="currentColor">Output at fixed second input</text><text x="52" y="263" font-size="13" fill="currentColor">Hot-end difference increases →</text>`;
 readout.textContent='Range along horizontal axis: '+lo+' to '+hi+' K. Output plot rescales vertically to demonstrate trend; it is not a fixed comparison across different second-input settings.';
}
rangeA.addEventListener('input',draw);rangeB.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 14:', err);
      }
    }
  });

  MODELS.push({
    idx: 15,
    unit: 8,
    html: "<div class=\"hero\"><span class=\"pill\">OFFLINE MODEL 15 / 16</span><h3>Counterflow effectiveness\u2013NTU</h3><p>Explore one explicit mathematical approximation using two independent sliders. The plot and result respond instantly.</p><div class=\"links\"></div></div><div class=\"notice\">Counterflow, single-pass two-stream \u03b5\u2013NTU relation with Cmin/Cmax &lt;1 and constant heat capacity rates. These are teaching inputs, not calibrated equipment or certified safety limits.</div><section class=\"model\"><label for=\"a\">Number of transfer units (dimensionless): <span id=\"a-value\"></span></label><input id=\"a\" type=\"range\" min=\"0.05\" max=\"5\" value=\"1.5\" step=\"any\"><label for=\"b\">Heat capacity ratio (fraction): <span id=\"b-value\"></span></label><input id=\"b\" type=\"range\" min=\"0.05\" max=\"0.95\" value=\"0.5\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 735 280\" role=\"img\" aria-label=\"Calculated output versus the first slider\"></svg><p id=\"readout\" class=\"mini\"></p><h2>Interpretation exercise</h2><p>Change one parameter while holding the other fixed. Explain the direction of response, check the governing equation and identify a limit in which this approximation becomes invalid. Return both sliders to their starting values and explain why the curve is not empirical evidence of real equipment performance.</p></section>",
    init: function(card) {
      try {
const rangeA=card.querySelector("#" + 'a'.replace(/^#/, "")),rangeB=card.querySelector("#" + 'b'.replace(/^#/, ""));
const valueA=card.querySelector("#" + 'a-value'.replace(/^#/, "")),valueB=card.querySelector("#" + 'b-value'.replace(/^#/, "")),result=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, "")),readout=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const lo=0.05,hi=5;
function evaluateModel(L,k){return ((1-Math.exp(-L*(1-k)))/(1-k*Math.exp(-L*(1-k))));}
function draw(){
 const L=Number(rangeA.value),k=Number(rangeB.value);
 const y=evaluateModel(L,k);valueA.textContent=L.toPrecision(4);valueB.textContent=k.toPrecision(4);
 result.textContent=Number.isFinite(y)?y.toPrecision(5)+' fraction':'Outside modeled range';
 const pts=[];const vals=[];
 for(let i=0;i<=70;i++){const x=lo+(hi-lo)*i/70, v=evaluateModel(x,k);if(Number.isFinite(v)){vals.push(v);pts.push([x,v]);}}
 if(vals.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...vals),vmax=Math.max(...vals);if(vmax===vmin){vmin-=1;vmax+=1;}
 let path=pts.map(([x,v],j)=>`${j?'L':'M'}${(45+(x-lo)/(hi-lo)*650).toFixed(1)},${(240-(v-vmin)/(vmax-vmin)*195).toFixed(1)}`).join(' ');
 let dotx=45+(L-lo)/(hi-lo)*650,doty=240-(y-vmin)/(vmax-vmin)*195;
 plot.innerHTML=`<path class="axis" fill="none" d="M45 25 V240 H708"/><path class="bar" fill="none" d="${path}"/><circle cx="${dotx.toFixed(1)}" cy="${doty.toFixed(1)}" r="6" fill="#e89a29"/><text x="52" y="22" font-size="14" fill="currentColor">Output at fixed second input</text><text x="52" y="263" font-size="13" fill="currentColor">Number of transfer units increases →</text>`;
 readout.textContent='Range along horizontal axis: '+lo+' to '+hi+' dimensionless. Output plot rescales vertically to demonstrate trend; it is not a fixed comparison across different second-input settings.';
}
rangeA.addEventListener('input',draw);rangeB.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 15:', err);
      }
    }
  });

  MODELS.push({
    idx: 16,
    unit: 8,
    html: "<div class=\"hero\"><span class=\"pill\">OFFLINE MODEL 16 / 16</span><h3>Electronic heat-sink rise</h3><p>Explore one explicit mathematical approximation using two independent sliders. The plot and result respond instantly.</p><div class=\"links\"></div></div><div class=\"notice\">\u0394T=Q\u00b7R\u03b8 for overall component-to-ambient resistance, valid only for approximately linearized steady operation. These are teaching inputs, not calibrated equipment or certified safety limits.</div><section class=\"model\"><label for=\"a\">Heat load (W): <span id=\"a-value\"></span></label><input id=\"a\" type=\"range\" min=\"1\" max=\"150\" value=\"45\" step=\"any\"><label for=\"b\">Thermal resistance (K/W): <span id=\"b-value\"></span></label><input id=\"b\" type=\"range\" min=\"0.05\" max=\"2\" value=\"0.6\" step=\"any\"><output id=\"result\" aria-live=\"polite\"></output><svg id=\"plot\" viewBox=\"0 0 735 280\" role=\"img\" aria-label=\"Calculated output versus the first slider\"></svg><p id=\"readout\" class=\"mini\"></p><h2>Interpretation exercise</h2><p>Change one parameter while holding the other fixed. Explain the direction of response, check the governing equation and identify a limit in which this approximation becomes invalid. Return both sliders to their starting values and explain why the curve is not empirical evidence of real equipment performance.</p></section>",
    init: function(card) {
      try {
const rangeA=card.querySelector("#" + 'a'.replace(/^#/, "")),rangeB=card.querySelector("#" + 'b'.replace(/^#/, ""));
const valueA=card.querySelector("#" + 'a-value'.replace(/^#/, "")),valueB=card.querySelector("#" + 'b-value'.replace(/^#/, "")),result=card.querySelector("#" + 'result'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, "")),readout=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const lo=1,hi=150;
function evaluateModel(L,k){return (L*k);}
function draw(){
 const L=Number(rangeA.value),k=Number(rangeB.value);
 const y=evaluateModel(L,k);valueA.textContent=L.toPrecision(4);valueB.textContent=k.toPrecision(4);
 result.textContent=Number.isFinite(y)?y.toPrecision(5)+' K':'Outside modeled range';
 const pts=[];const vals=[];
 for(let i=0;i<=70;i++){const x=lo+(hi-lo)*i/70, v=evaluateModel(x,k);if(Number.isFinite(v)){vals.push(v);pts.push([x,v]);}}
 if(vals.length<2){plot.innerHTML='';return;}
 let vmin=Math.min(...vals),vmax=Math.max(...vals);if(vmax===vmin){vmin-=1;vmax+=1;}
 let path=pts.map(([x,v],j)=>`${j?'L':'M'}${(45+(x-lo)/(hi-lo)*650).toFixed(1)},${(240-(v-vmin)/(vmax-vmin)*195).toFixed(1)}`).join(' ');
 let dotx=45+(L-lo)/(hi-lo)*650,doty=240-(y-vmin)/(vmax-vmin)*195;
 plot.innerHTML=`<path class="axis" fill="none" d="M45 25 V240 H708"/><path class="bar" fill="none" d="${path}"/><circle cx="${dotx.toFixed(1)}" cy="${doty.toFixed(1)}" r="6" fill="#e89a29"/><text x="52" y="22" font-size="14" fill="currentColor">Output at fixed second input</text><text x="52" y="263" font-size="13" fill="currentColor">Heat load increases →</text>`;
 readout.textContent='Range along horizontal axis: '+lo+' to '+hi+' W. Output plot rescales vertically to demonstrate trend; it is not a fixed comparison across different second-input settings.';
}
rangeA.addEventListener('input',draw);rangeB.addEventListener('input',draw);draw();
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
