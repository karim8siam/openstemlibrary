/* engineering-mechanics Interactive Simulation Suite */
(function(window) {
  'use strict';

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: "<div class=\"hero\"><p class=\"meta\">Unit 1 \u00b7 Model 1 / 16 \u00b7 Offline interactive</p><h3>Vector Resolution</h3><p>Resolve an inclined force into perpendicular components.</p><p class=\"formula\">Fx = F cos \u03b8; Fy = F sin \u03b8</p></div><div class=\"sim-controls\"><label class=\"control\">F: <output id=\"av\">550</output> N<input id=\"a\" type=\"range\" min=\"100\" max=\"1200\" value=\"550\" step=\"2.20000\" aria-label=\"F\"></label>\n<label class=\"control\">angle: <output id=\"bv\">35</output> deg<input id=\"b\" type=\"range\" min=\"0\" max=\"90\" value=\"35\" step=\"0.18000\" aria-label=\"angle\"></label></div>\n<div class=\"grid\"><div class=\"card\"><small>Fx</small><div><output id=\"r1\">...</output></div></div><div class=\"card\"><small>Fy</small><div><output id=\"r2\">...</output></div></div></div><div class=\"plot\" id=\"plot\"></div><section><h2>How to investigate</h2><p>Record the default output, then move one slider at a time. Before changing the slider, predict the shape of the response. The chart plots the first output against the first input while holding the second input constant. Compare the predicted and computed trends. Finally, state the model limitation that matters most in a real device. All values are idealized; they are not measured field data.</p><div class=\"warn\">Educational model only. Not a product safety calculation, medical device analysis, or engineering certification.</div></section>",
    init: function(card) {
      try {
const model = (a,b) => [a*Math.cos(b*Math.PI/180),a*Math.sin(b*Math.PI/180)];
const aInput=card.querySelector('#a'),bInput=card.querySelector('#b');
const aVal=card.querySelector('#av'),bVal=card.querySelector('#bv'),r1=card.querySelector('#r1'),r2=card.querySelector('#r2');
const plot=card.querySelector('#plot');
const fmt=n=>Number.isFinite(n)?(Math.abs(n)>0&&Math.abs(n)<.0001?n.toExponential(3):n.toLocaleString('en-US',{maximumFractionDigits:5})):'undefined';
function draw(){
 const a=Number(aInput.value),b=Number(bInput.value); const r=model(a,b);
 aVal.textContent=fmt(a);bVal.textContent=fmt(b);r1.textContent=fmt(r[0]);r2.textContent=fmt(r[1]);
 const lo=Number(aInput.min),hi=Number(aInput.max),points=[];
 for(let i=0;i<=60;i++){const x=lo+(hi-lo)*i/60;const y=model(x,b)[0];if(Number.isFinite(y))points.push({x,y});}
 if(!points.length){plot.innerHTML='No valid plotting range';return}
 let ymin=Math.min(...points.map(p=>p.y)), ymax=Math.max(...points.map(p=>p.y));
 if(ymax===ymin){ymin-=1;ymax+=1;}
 const pad=(ymax-ymin)*.08; ymin-=pad;ymax+=pad;
 const px=x=>50+(x-lo)/(hi-lo)*620,py=y=>230-(y-ymin)/(ymax-ymin)*190;
 const line=points.map(p=>`${px(p.x).toFixed(1)},${py(p.y).toFixed(1)}`).join(' ');
 const c=px(a),d=py(r[0]);
 plot.innerHTML=`<svg viewBox="0 0 720 270" role="img" aria-label="Computed response plotted versus the first input" style="width:100%;height:auto">
 <line x1="50" x2="690" y1="230" y2="230" stroke="#7291ae"/><line x1="50" x2="50" y1="40" y2="230" stroke="#7291ae"/>
 <polyline points="${line}" fill="none" stroke="#74ddc1" stroke-width="3"/>
 <circle cx="${c}" cy="${d}" r="5" fill="#ffc47c"/>
 <text x="55" y="30" fill="#cadbec" font-size="14">Response ${fmt(ymin)} to ${fmt(ymax)}</text>
 <text x="455" y="256" fill="#cadbec" font-size="14">First input: ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
aInput.addEventListener('input',draw);bInput.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 1,
    html: "<div class=\"hero\"><p class=\"meta\">Unit 1 \u00b7 Model 2 / 16 \u00b7 Offline interactive</p><h3>Resultant Forces</h3><p>Combine simultaneous components without adding magnitudes. If R = 0, its angle is undefined (0\u00b0 is displayed as a placeholder).</p><p class=\"formula\">R = \u221a(Fx\u00b2 + Fy\u00b2)</p></div><div class=\"sim-controls\"><label class=\"control\">Fx: <output id=\"av\">120</output> N<input id=\"a\" type=\"range\" min=\"-500\" max=\"500\" value=\"120\" step=\"2.00000\" aria-label=\"Fx\"></label>\n<label class=\"control\">Fy: <output id=\"bv\">100</output> N<input id=\"b\" type=\"range\" min=\"-500\" max=\"500\" value=\"100\" step=\"2.00000\" aria-label=\"Fy\"></label></div>\n<div class=\"grid\"><div class=\"card\"><small>Magnitude</small><div><output id=\"r1\">...</output></div></div><div class=\"card\"><small>Angle (deg)</small><div><output id=\"r2\">...</output></div></div></div><div class=\"plot\" id=\"plot\"></div><section><h2>How to investigate</h2><p>Record the default output, then move one slider at a time. Before changing the slider, predict the shape of the response. The chart plots the first output against the first input while holding the second input constant. Compare the predicted and computed trends. Finally, state the model limitation that matters most in a real device. All values are idealized; they are not measured field data.</p><div class=\"warn\">Educational model only. Not a product safety calculation, medical device analysis, or engineering certification.</div></section>",
    init: function(card) {
      try {
const model = (a,b) => [Math.hypot(a,b),Math.hypot(a,b)<1e-12?0:Math.atan2(b,a)*180/Math.PI];
const aInput=card.querySelector('#a'),bInput=card.querySelector('#b');
const aVal=card.querySelector('#av'),bVal=card.querySelector('#bv'),r1=card.querySelector('#r1'),r2=card.querySelector('#r2');
const plot=card.querySelector('#plot');
const fmt=n=>Number.isFinite(n)?(Math.abs(n)>0&&Math.abs(n)<.0001?n.toExponential(3):n.toLocaleString('en-US',{maximumFractionDigits:5})):'undefined';
function draw(){
 const a=Number(aInput.value),b=Number(bInput.value); const r=model(a,b);
 aVal.textContent=fmt(a);bVal.textContent=fmt(b);r1.textContent=fmt(r[0]);r2.textContent=fmt(r[1]);
 const lo=Number(aInput.min),hi=Number(aInput.max),points=[];
 for(let i=0;i<=60;i++){const x=lo+(hi-lo)*i/60;const y=model(x,b)[0];if(Number.isFinite(y))points.push({x,y});}
 if(!points.length){plot.innerHTML='No valid plotting range';return}
 let ymin=Math.min(...points.map(p=>p.y)), ymax=Math.max(...points.map(p=>p.y));
 if(ymax===ymin){ymin-=1;ymax+=1;}
 const pad=(ymax-ymin)*.08; ymin-=pad;ymax+=pad;
 const px=x=>50+(x-lo)/(hi-lo)*620,py=y=>230-(y-ymin)/(ymax-ymin)*190;
 const line=points.map(p=>`${px(p.x).toFixed(1)},${py(p.y).toFixed(1)}`).join(' ');
 const c=px(a),d=py(r[0]);
 plot.innerHTML=`<svg viewBox="0 0 720 270" role="img" aria-label="Computed response plotted versus the first input" style="width:100%;height:auto">
 <line x1="50" x2="690" y1="230" y2="230" stroke="#7291ae"/><line x1="50" x2="50" y1="40" y2="230" stroke="#7291ae"/>
 <polyline points="${line}" fill="none" stroke="#74ddc1" stroke-width="3"/>
 <circle cx="${c}" cy="${d}" r="5" fill="#ffc47c"/>
 <text x="55" y="30" fill="#cadbec" font-size="14">Response ${fmt(ymin)} to ${fmt(ymax)}</text>
 <text x="455" y="256" fill="#cadbec" font-size="14">First input: ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
aInput.addEventListener('input',draw);bInput.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 2,
    html: "<div class=\"hero\"><p class=\"meta\">Unit 2 \u00b7 Model 3 / 16 \u00b7 Offline interactive</p><h3>Beam Point-Load Reactions</h3><p>Move the load and observe how reaction distribution changes.</p><p class=\"formula\">RB = P x / L; RA = P \u2212 RB (L = 5 m)</p></div><div class=\"sim-controls\"><label class=\"control\">P: <output id=\"av\">600</output> N<input id=\"a\" type=\"range\" min=\"100\" max=\"1500\" value=\"600\" step=\"2.80000\" aria-label=\"P\"></label>\n<label class=\"control\">x: <output id=\"bv\">2</output> m<input id=\"b\" type=\"range\" min=\"0.2\" max=\"4.8\" value=\"2\" step=\"0.00920\" aria-label=\"x\"></label></div>\n<div class=\"grid\"><div class=\"card\"><small>RA</small><div><output id=\"r1\">...</output></div></div><div class=\"card\"><small>RB (N)</small><div><output id=\"r2\">...</output></div></div></div><div class=\"plot\" id=\"plot\"></div><section><h2>How to investigate</h2><p>Record the default output, then move one slider at a time. Before changing the slider, predict the shape of the response. The chart plots the first output against the first input while holding the second input constant. Compare the predicted and computed trends. Finally, state the model limitation that matters most in a real device. All values are idealized; they are not measured field data.</p><div class=\"warn\">Educational model only. Not a product safety calculation, medical device analysis, or engineering certification.</div></section>",
    init: function(card) {
      try {
const model = (a,b) => [a*(1-b/5),a*b/5];
const aInput=card.querySelector('#a'),bInput=card.querySelector('#b');
const aVal=card.querySelector('#av'),bVal=card.querySelector('#bv'),r1=card.querySelector('#r1'),r2=card.querySelector('#r2');
const plot=card.querySelector('#plot');
const fmt=n=>Number.isFinite(n)?(Math.abs(n)>0&&Math.abs(n)<.0001?n.toExponential(3):n.toLocaleString('en-US',{maximumFractionDigits:5})):'undefined';
function draw(){
 const a=Number(aInput.value),b=Number(bInput.value); const r=model(a,b);
 aVal.textContent=fmt(a);bVal.textContent=fmt(b);r1.textContent=fmt(r[0]);r2.textContent=fmt(r[1]);
 const lo=Number(aInput.min),hi=Number(aInput.max),points=[];
 for(let i=0;i<=60;i++){const x=lo+(hi-lo)*i/60;const y=model(x,b)[0];if(Number.isFinite(y))points.push({x,y});}
 if(!points.length){plot.innerHTML='No valid plotting range';return}
 let ymin=Math.min(...points.map(p=>p.y)), ymax=Math.max(...points.map(p=>p.y));
 if(ymax===ymin){ymin-=1;ymax+=1;}
 const pad=(ymax-ymin)*.08; ymin-=pad;ymax+=pad;
 const px=x=>50+(x-lo)/(hi-lo)*620,py=y=>230-(y-ymin)/(ymax-ymin)*190;
 const line=points.map(p=>`${px(p.x).toFixed(1)},${py(p.y).toFixed(1)}`).join(' ');
 const c=px(a),d=py(r[0]);
 plot.innerHTML=`<svg viewBox="0 0 720 270" role="img" aria-label="Computed response plotted versus the first input" style="width:100%;height:auto">
 <line x1="50" x2="690" y1="230" y2="230" stroke="#7291ae"/><line x1="50" x2="50" y1="40" y2="230" stroke="#7291ae"/>
 <polyline points="${line}" fill="none" stroke="#74ddc1" stroke-width="3"/>
 <circle cx="${c}" cy="${d}" r="5" fill="#ffc47c"/>
 <text x="55" y="30" fill="#cadbec" font-size="14">Response ${fmt(ymin)} to ${fmt(ymax)}</text>
 <text x="455" y="256" fill="#cadbec" font-size="14">First input: ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
aInput.addEventListener('input',draw);bInput.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 2,
    html: "<div class=\"hero\"><p class=\"meta\">Unit 2 \u00b7 Model 4 / 16 \u00b7 Offline interactive</p><h3>Uniform Beam Load</h3><p>Observe that reactions scale with intensity and span.</p><p class=\"formula\">RA = RB = q L / 2</p></div><div class=\"sim-controls\"><label class=\"control\">q: <output id=\"av\">350</output> N/m<input id=\"a\" type=\"range\" min=\"20\" max=\"650\" value=\"350\" step=\"1.26000\" aria-label=\"q\"></label>\n<label class=\"control\">L: <output id=\"bv\">3</output> m<input id=\"b\" type=\"range\" min=\"1\" max=\"10\" value=\"3\" step=\"0.01800\" aria-label=\"L\"></label></div>\n<div class=\"grid\"><div class=\"card\"><small>Reaction at each end (N)</small><div><output id=\"r1\">...</output></div></div><div class=\"card\"><small>Total load (N)</small><div><output id=\"r2\">...</output></div></div></div><div class=\"plot\" id=\"plot\"></div><section><h2>How to investigate</h2><p>Record the default output, then move one slider at a time. Before changing the slider, predict the shape of the response. The chart plots the first output against the first input while holding the second input constant. Compare the predicted and computed trends. Finally, state the model limitation that matters most in a real device. All values are idealized; they are not measured field data.</p><div class=\"warn\">Educational model only. Not a product safety calculation, medical device analysis, or engineering certification.</div></section>",
    init: function(card) {
      try {
const model = (a,b) => [a*b/2,a*b];
const aInput=card.querySelector('#a'),bInput=card.querySelector('#b');
const aVal=card.querySelector('#av'),bVal=card.querySelector('#bv'),r1=card.querySelector('#r1'),r2=card.querySelector('#r2');
const plot=card.querySelector('#plot');
const fmt=n=>Number.isFinite(n)?(Math.abs(n)>0&&Math.abs(n)<.0001?n.toExponential(3):n.toLocaleString('en-US',{maximumFractionDigits:5})):'undefined';
function draw(){
 const a=Number(aInput.value),b=Number(bInput.value); const r=model(a,b);
 aVal.textContent=fmt(a);bVal.textContent=fmt(b);r1.textContent=fmt(r[0]);r2.textContent=fmt(r[1]);
 const lo=Number(aInput.min),hi=Number(aInput.max),points=[];
 for(let i=0;i<=60;i++){const x=lo+(hi-lo)*i/60;const y=model(x,b)[0];if(Number.isFinite(y))points.push({x,y});}
 if(!points.length){plot.innerHTML='No valid plotting range';return}
 let ymin=Math.min(...points.map(p=>p.y)), ymax=Math.max(...points.map(p=>p.y));
 if(ymax===ymin){ymin-=1;ymax+=1;}
 const pad=(ymax-ymin)*.08; ymin-=pad;ymax+=pad;
 const px=x=>50+(x-lo)/(hi-lo)*620,py=y=>230-(y-ymin)/(ymax-ymin)*190;
 const line=points.map(p=>`${px(p.x).toFixed(1)},${py(p.y).toFixed(1)}`).join(' ');
 const c=px(a),d=py(r[0]);
 plot.innerHTML=`<svg viewBox="0 0 720 270" role="img" aria-label="Computed response plotted versus the first input" style="width:100%;height:auto">
 <line x1="50" x2="690" y1="230" y2="230" stroke="#7291ae"/><line x1="50" x2="50" y1="40" y2="230" stroke="#7291ae"/>
 <polyline points="${line}" fill="none" stroke="#74ddc1" stroke-width="3"/>
 <circle cx="${c}" cy="${d}" r="5" fill="#ffc47c"/>
 <text x="55" y="30" fill="#cadbec" font-size="14">Response ${fmt(ymin)} to ${fmt(ymax)}</text>
 <text x="455" y="256" fill="#cadbec" font-size="14">First input: ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
aInput.addEventListener('input',draw);bInput.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 3,
    html: "<div class=\"hero\"><p class=\"meta\">Unit 3 \u00b7 Model 5 / 16 \u00b7 Offline interactive</p><h3>Symmetric Truss</h3><p>Observe compression/tension force amplification at shallow angles.</p><p class=\"formula\">F = P / (2 sin \u03b8)</p></div><div class=\"sim-controls\"><label class=\"control\">P: <output id=\"av\">600</output> N<input id=\"a\" type=\"range\" min=\"100\" max=\"1500\" value=\"600\" step=\"2.80000\" aria-label=\"P\"></label>\n<label class=\"control\">theta: <output id=\"bv\">60</output> deg<input id=\"b\" type=\"range\" min=\"15\" max=\"80\" value=\"60\" step=\"0.13000\" aria-label=\"theta\"></label></div>\n<div class=\"grid\"><div class=\"card\"><small>Axial force (N)</small><div><output id=\"r1\">...</output></div></div><div class=\"card\"><small>Applied load (N)</small><div><output id=\"r2\">...</output></div></div></div><div class=\"plot\" id=\"plot\"></div><section><h2>How to investigate</h2><p>Record the default output, then move one slider at a time. Before changing the slider, predict the shape of the response. The chart plots the first output against the first input while holding the second input constant. Compare the predicted and computed trends. Finally, state the model limitation that matters most in a real device. All values are idealized; they are not measured field data.</p><div class=\"warn\">Educational model only. Not a product safety calculation, medical device analysis, or engineering certification.</div></section>",
    init: function(card) {
      try {
const model = (a,b) => [a/(2*Math.sin(b*Math.PI/180)),a];
const aInput=card.querySelector('#a'),bInput=card.querySelector('#b');
const aVal=card.querySelector('#av'),bVal=card.querySelector('#bv'),r1=card.querySelector('#r1'),r2=card.querySelector('#r2');
const plot=card.querySelector('#plot');
const fmt=n=>Number.isFinite(n)?(Math.abs(n)>0&&Math.abs(n)<.0001?n.toExponential(3):n.toLocaleString('en-US',{maximumFractionDigits:5})):'undefined';
function draw(){
 const a=Number(aInput.value),b=Number(bInput.value); const r=model(a,b);
 aVal.textContent=fmt(a);bVal.textContent=fmt(b);r1.textContent=fmt(r[0]);r2.textContent=fmt(r[1]);
 const lo=Number(aInput.min),hi=Number(aInput.max),points=[];
 for(let i=0;i<=60;i++){const x=lo+(hi-lo)*i/60;const y=model(x,b)[0];if(Number.isFinite(y))points.push({x,y});}
 if(!points.length){plot.innerHTML='No valid plotting range';return}
 let ymin=Math.min(...points.map(p=>p.y)), ymax=Math.max(...points.map(p=>p.y));
 if(ymax===ymin){ymin-=1;ymax+=1;}
 const pad=(ymax-ymin)*.08; ymin-=pad;ymax+=pad;
 const px=x=>50+(x-lo)/(hi-lo)*620,py=y=>230-(y-ymin)/(ymax-ymin)*190;
 const line=points.map(p=>`${px(p.x).toFixed(1)},${py(p.y).toFixed(1)}`).join(' ');
 const c=px(a),d=py(r[0]);
 plot.innerHTML=`<svg viewBox="0 0 720 270" role="img" aria-label="Computed response plotted versus the first input" style="width:100%;height:auto">
 <line x1="50" x2="690" y1="230" y2="230" stroke="#7291ae"/><line x1="50" x2="50" y1="40" y2="230" stroke="#7291ae"/>
 <polyline points="${line}" fill="none" stroke="#74ddc1" stroke-width="3"/>
 <circle cx="${c}" cy="${d}" r="5" fill="#ffc47c"/>
 <text x="55" y="30" fill="#cadbec" font-size="14">Response ${fmt(ymin)} to ${fmt(ymax)}</text>
 <text x="455" y="256" fill="#cadbec" font-size="14">First input: ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
aInput.addEventListener('input',draw);bInput.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 3,
    html: "<div class=\"hero\"><p class=\"meta\">Unit 3 \u00b7 Model 6 / 16 \u00b7 Offline interactive</p><h3>Cantilever Root Moment</h3><p>A longer offset increases root moment even when force is unchanged.</p><p class=\"formula\">M = P L</p></div><div class=\"sim-controls\"><label class=\"control\">P: <output id=\"av\">250</output> N<input id=\"a\" type=\"range\" min=\"100\" max=\"1000\" value=\"250\" step=\"1.80000\" aria-label=\"P\"></label>\n<label class=\"control\">L: <output id=\"bv\">0.5</output> m<input id=\"b\" type=\"range\" min=\"0.1\" max=\"2\" value=\"0.5\" step=\"0.00380\" aria-label=\"L\"></label></div>\n<div class=\"grid\"><div class=\"card\"><small>Root moment (N\u00b7m)</small><div><output id=\"r1\">...</output></div></div><div class=\"card\"><small>absolute magnitude</small><div><output id=\"r2\">...</output></div></div></div><div class=\"plot\" id=\"plot\"></div><section><h2>How to investigate</h2><p>Record the default output, then move one slider at a time. Before changing the slider, predict the shape of the response. The chart plots the first output against the first input while holding the second input constant. Compare the predicted and computed trends. Finally, state the model limitation that matters most in a real device. All values are idealized; they are not measured field data.</p><div class=\"warn\">Educational model only. Not a product safety calculation, medical device analysis, or engineering certification.</div></section>",
    init: function(card) {
      try {
const model = (a,b) => [a*b,a*b];
const aInput=card.querySelector('#a'),bInput=card.querySelector('#b');
const aVal=card.querySelector('#av'),bVal=card.querySelector('#bv'),r1=card.querySelector('#r1'),r2=card.querySelector('#r2');
const plot=card.querySelector('#plot');
const fmt=n=>Number.isFinite(n)?(Math.abs(n)>0&&Math.abs(n)<.0001?n.toExponential(3):n.toLocaleString('en-US',{maximumFractionDigits:5})):'undefined';
function draw(){
 const a=Number(aInput.value),b=Number(bInput.value); const r=model(a,b);
 aVal.textContent=fmt(a);bVal.textContent=fmt(b);r1.textContent=fmt(r[0]);r2.textContent=fmt(r[1]);
 const lo=Number(aInput.min),hi=Number(aInput.max),points=[];
 for(let i=0;i<=60;i++){const x=lo+(hi-lo)*i/60;const y=model(x,b)[0];if(Number.isFinite(y))points.push({x,y});}
 if(!points.length){plot.innerHTML='No valid plotting range';return}
 let ymin=Math.min(...points.map(p=>p.y)), ymax=Math.max(...points.map(p=>p.y));
 if(ymax===ymin){ymin-=1;ymax+=1;}
 const pad=(ymax-ymin)*.08; ymin-=pad;ymax+=pad;
 const px=x=>50+(x-lo)/(hi-lo)*620,py=y=>230-(y-ymin)/(ymax-ymin)*190;
 const line=points.map(p=>`${px(p.x).toFixed(1)},${py(p.y).toFixed(1)}`).join(' ');
 const c=px(a),d=py(r[0]);
 plot.innerHTML=`<svg viewBox="0 0 720 270" role="img" aria-label="Computed response plotted versus the first input" style="width:100%;height:auto">
 <line x1="50" x2="690" y1="230" y2="230" stroke="#7291ae"/><line x1="50" x2="50" y1="40" y2="230" stroke="#7291ae"/>
 <polyline points="${line}" fill="none" stroke="#74ddc1" stroke-width="3"/>
 <circle cx="${c}" cy="${d}" r="5" fill="#ffc47c"/>
 <text x="55" y="30" fill="#cadbec" font-size="14">Response ${fmt(ymin)} to ${fmt(ymax)}</text>
 <text x="455" y="256" fill="#cadbec" font-size="14">First input: ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
aInput.addEventListener('input',draw);bInput.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 4,
    html: "<div class=\"hero\"><p class=\"meta\">Unit 4 \u00b7 Model 7 / 16 \u00b7 Offline interactive</p><h3>Two-Mass Center</h3><p>Watch a payload move the assembly balance point.</p><p class=\"formula\">xG = (20\u00d70.2 + m2\u00d7x2)/(20 + m2)</p></div><div class=\"sim-controls\"><label class=\"control\">m2: <output id=\"av\">5</output> kg<input id=\"a\" type=\"range\" min=\"1\" max=\"40\" value=\"5\" step=\"0.07800\" aria-label=\"m2\"></label>\n<label class=\"control\">x2: <output id=\"bv\">0.8</output> m<input id=\"b\" type=\"range\" min=\"0.1\" max=\"2\" value=\"0.8\" step=\"0.00380\" aria-label=\"x2\"></label></div>\n<div class=\"grid\"><div class=\"card\"><small>Balance x (m)</small><div><output id=\"r1\">...</output></div></div><div class=\"card\"><small>Total mass (kg)</small><div><output id=\"r2\">...</output></div></div></div><div class=\"plot\" id=\"plot\"></div><section><h2>How to investigate</h2><p>Record the default output, then move one slider at a time. Before changing the slider, predict the shape of the response. The chart plots the first output against the first input while holding the second input constant. Compare the predicted and computed trends. Finally, state the model limitation that matters most in a real device. All values are idealized; they are not measured field data.</p><div class=\"warn\">Educational model only. Not a product safety calculation, medical device analysis, or engineering certification.</div></section>",
    init: function(card) {
      try {
const model = (a,b) => [(20*.2+a*b)/(20+a),20+a];
const aInput=card.querySelector('#a'),bInput=card.querySelector('#b');
const aVal=card.querySelector('#av'),bVal=card.querySelector('#bv'),r1=card.querySelector('#r1'),r2=card.querySelector('#r2');
const plot=card.querySelector('#plot');
const fmt=n=>Number.isFinite(n)?(Math.abs(n)>0&&Math.abs(n)<.0001?n.toExponential(3):n.toLocaleString('en-US',{maximumFractionDigits:5})):'undefined';
function draw(){
 const a=Number(aInput.value),b=Number(bInput.value); const r=model(a,b);
 aVal.textContent=fmt(a);bVal.textContent=fmt(b);r1.textContent=fmt(r[0]);r2.textContent=fmt(r[1]);
 const lo=Number(aInput.min),hi=Number(aInput.max),points=[];
 for(let i=0;i<=60;i++){const x=lo+(hi-lo)*i/60;const y=model(x,b)[0];if(Number.isFinite(y))points.push({x,y});}
 if(!points.length){plot.innerHTML='No valid plotting range';return}
 let ymin=Math.min(...points.map(p=>p.y)), ymax=Math.max(...points.map(p=>p.y));
 if(ymax===ymin){ymin-=1;ymax+=1;}
 const pad=(ymax-ymin)*.08; ymin-=pad;ymax+=pad;
 const px=x=>50+(x-lo)/(hi-lo)*620,py=y=>230-(y-ymin)/(ymax-ymin)*190;
 const line=points.map(p=>`${px(p.x).toFixed(1)},${py(p.y).toFixed(1)}`).join(' ');
 const c=px(a),d=py(r[0]);
 plot.innerHTML=`<svg viewBox="0 0 720 270" role="img" aria-label="Computed response plotted versus the first input" style="width:100%;height:auto">
 <line x1="50" x2="690" y1="230" y2="230" stroke="#7291ae"/><line x1="50" x2="50" y1="40" y2="230" stroke="#7291ae"/>
 <polyline points="${line}" fill="none" stroke="#74ddc1" stroke-width="3"/>
 <circle cx="${c}" cy="${d}" r="5" fill="#ffc47c"/>
 <text x="55" y="30" fill="#cadbec" font-size="14">Response ${fmt(ymin)} to ${fmt(ymax)}</text>
 <text x="455" y="256" fill="#cadbec" font-size="14">First input: ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
aInput.addEventListener('input',draw);bInput.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 4,
    html: "<div class=\"hero\"><p class=\"meta\">Unit 4 \u00b7 Model 8 / 16 \u00b7 Offline interactive</p><h3>Rectangle Second Moment</h3><p>Depth contributes cubically to the second moment of area.</p><p class=\"formula\">Ix = b h\u00b3 / 12</p></div><div class=\"sim-controls\"><label class=\"control\">b: <output id=\"av\">0.02</output> m<input id=\"a\" type=\"range\" min=\"0.01\" max=\"0.2\" value=\"0.02\" step=\"0.00100\" aria-label=\"b\"></label>\n<label class=\"control\">h: <output id=\"bv\">0.06</output> m<input id=\"b\" type=\"range\" min=\"0.01\" max=\"0.2\" value=\"0.06\" step=\"0.00100\" aria-label=\"h\"></label></div>\n<div class=\"grid\"><div class=\"card\"><small>Area moment (m\u2074)</small><div><output id=\"r1\">...</output></div></div><div class=\"card\"><small>Area (m\u00b2)</small><div><output id=\"r2\">...</output></div></div></div><div class=\"plot\" id=\"plot\"></div><section><h2>How to investigate</h2><p>Record the default output, then move one slider at a time. Before changing the slider, predict the shape of the response. The chart plots the first output against the first input while holding the second input constant. Compare the predicted and computed trends. Finally, state the model limitation that matters most in a real device. All values are idealized; they are not measured field data.</p><div class=\"warn\">Educational model only. Not a product safety calculation, medical device analysis, or engineering certification.</div></section>",
    init: function(card) {
      try {
const model = (a,b) => [a*Math.pow(b,3)/12,a*b];
const aInput=card.querySelector('#a'),bInput=card.querySelector('#b');
const aVal=card.querySelector('#av'),bVal=card.querySelector('#bv'),r1=card.querySelector('#r1'),r2=card.querySelector('#r2');
const plot=card.querySelector('#plot');
const fmt=n=>Number.isFinite(n)?(Math.abs(n)>0&&Math.abs(n)<.0001?n.toExponential(3):n.toLocaleString('en-US',{maximumFractionDigits:5})):'undefined';
function draw(){
 const a=Number(aInput.value),b=Number(bInput.value); const r=model(a,b);
 aVal.textContent=fmt(a);bVal.textContent=fmt(b);r1.textContent=fmt(r[0]);r2.textContent=fmt(r[1]);
 const lo=Number(aInput.min),hi=Number(aInput.max),points=[];
 for(let i=0;i<=60;i++){const x=lo+(hi-lo)*i/60;const y=model(x,b)[0];if(Number.isFinite(y))points.push({x,y});}
 if(!points.length){plot.innerHTML='No valid plotting range';return}
 let ymin=Math.min(...points.map(p=>p.y)), ymax=Math.max(...points.map(p=>p.y));
 if(ymax===ymin){ymin-=1;ymax+=1;}
 const pad=(ymax-ymin)*.08; ymin-=pad;ymax+=pad;
 const px=x=>50+(x-lo)/(hi-lo)*620,py=y=>230-(y-ymin)/(ymax-ymin)*190;
 const line=points.map(p=>`${px(p.x).toFixed(1)},${py(p.y).toFixed(1)}`).join(' ');
 const c=px(a),d=py(r[0]);
 plot.innerHTML=`<svg viewBox="0 0 720 270" role="img" aria-label="Computed response plotted versus the first input" style="width:100%;height:auto">
 <line x1="50" x2="690" y1="230" y2="230" stroke="#7291ae"/><line x1="50" x2="50" y1="40" y2="230" stroke="#7291ae"/>
 <polyline points="${line}" fill="none" stroke="#74ddc1" stroke-width="3"/>
 <circle cx="${c}" cy="${d}" r="5" fill="#ffc47c"/>
 <text x="55" y="30" fill="#cadbec" font-size="14">Response ${fmt(ymin)} to ${fmt(ymax)}</text>
 <text x="455" y="256" fill="#cadbec" font-size="14">First input: ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
aInput.addEventListener('input',draw);bInput.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  MODELS.push({
    idx: 9,
    unit: 5,
    html: "<div class=\"hero\"><p class=\"meta\">Unit 5 \u00b7 Model 9 / 16 \u00b7 Offline interactive</p><h3>Static Friction Limit</h3><p>See how normal load and surface coefficient set an ideal threshold.</p><p class=\"formula\">Fmax = \u03bcs m g</p></div><div class=\"sim-controls\"><label class=\"control\">m: <output id=\"av\">30</output> kg<input id=\"a\" type=\"range\" min=\"1\" max=\"100\" value=\"30\" step=\"0.19800\" aria-label=\"m\"></label>\n<label class=\"control\">mu: <output id=\"bv\">0.4</output> <input id=\"b\" type=\"range\" min=\"0.05\" max=\"0.9\" value=\"0.4\" step=\"0.00170\" aria-label=\"mu\"></label></div>\n<div class=\"grid\"><div class=\"card\"><small>Maximum static friction (N)</small><div><output id=\"r1\">...</output></div></div><div class=\"card\"><small>Weight (N)</small><div><output id=\"r2\">...</output></div></div></div><div class=\"plot\" id=\"plot\"></div><section><h2>How to investigate</h2><p>Record the default output, then move one slider at a time. Before changing the slider, predict the shape of the response. The chart plots the first output against the first input while holding the second input constant. Compare the predicted and computed trends. Finally, state the model limitation that matters most in a real device. All values are idealized; they are not measured field data.</p><div class=\"warn\">Educational model only. Not a product safety calculation, medical device analysis, or engineering certification.</div></section>",
    init: function(card) {
      try {
const model = (a,b) => [a*b*9.81,a*9.81];
const aInput=card.querySelector('#a'),bInput=card.querySelector('#b');
const aVal=card.querySelector('#av'),bVal=card.querySelector('#bv'),r1=card.querySelector('#r1'),r2=card.querySelector('#r2');
const plot=card.querySelector('#plot');
const fmt=n=>Number.isFinite(n)?(Math.abs(n)>0&&Math.abs(n)<.0001?n.toExponential(3):n.toLocaleString('en-US',{maximumFractionDigits:5})):'undefined';
function draw(){
 const a=Number(aInput.value),b=Number(bInput.value); const r=model(a,b);
 aVal.textContent=fmt(a);bVal.textContent=fmt(b);r1.textContent=fmt(r[0]);r2.textContent=fmt(r[1]);
 const lo=Number(aInput.min),hi=Number(aInput.max),points=[];
 for(let i=0;i<=60;i++){const x=lo+(hi-lo)*i/60;const y=model(x,b)[0];if(Number.isFinite(y))points.push({x,y});}
 if(!points.length){plot.innerHTML='No valid plotting range';return}
 let ymin=Math.min(...points.map(p=>p.y)), ymax=Math.max(...points.map(p=>p.y));
 if(ymax===ymin){ymin-=1;ymax+=1;}
 const pad=(ymax-ymin)*.08; ymin-=pad;ymax+=pad;
 const px=x=>50+(x-lo)/(hi-lo)*620,py=y=>230-(y-ymin)/(ymax-ymin)*190;
 const line=points.map(p=>`${px(p.x).toFixed(1)},${py(p.y).toFixed(1)}`).join(' ');
 const c=px(a),d=py(r[0]);
 plot.innerHTML=`<svg viewBox="0 0 720 270" role="img" aria-label="Computed response plotted versus the first input" style="width:100%;height:auto">
 <line x1="50" x2="690" y1="230" y2="230" stroke="#7291ae"/><line x1="50" x2="50" y1="40" y2="230" stroke="#7291ae"/>
 <polyline points="${line}" fill="none" stroke="#74ddc1" stroke-width="3"/>
 <circle cx="${c}" cy="${d}" r="5" fill="#ffc47c"/>
 <text x="55" y="30" fill="#cadbec" font-size="14">Response ${fmt(ymin)} to ${fmt(ymax)}</text>
 <text x="455" y="256" fill="#cadbec" font-size="14">First input: ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
aInput.addEventListener('input',draw);bInput.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 9:', err);
      }
    }
  });

  MODELS.push({
    idx: 10,
    unit: 5,
    html: "<div class=\"hero\"><p class=\"meta\">Unit 5 \u00b7 Model 10 / 16 \u00b7 Offline interactive</p><h3>Capstan Tension Ratio</h3><p>Watch the exponential influence of wrap angle in radians.</p><p class=\"formula\">Ttight/Tslack = exp(\u03bc \u03b8)</p></div><div class=\"sim-controls\"><label class=\"control\">mu: <output id=\"av\">0.25</output> <input id=\"a\" type=\"range\" min=\"0.02\" max=\"0.7\" value=\"0.25\" step=\"0.00136\" aria-label=\"mu\"></label>\n<label class=\"control\">theta: <output id=\"bv\">3.14</output> rad<input id=\"b\" type=\"range\" min=\"0.1\" max=\"6.28\" value=\"3.14\" step=\"0.01236\" aria-label=\"theta\"></label></div>\n<div class=\"grid\"><div class=\"card\"><small>Tension ratio</small><div><output id=\"r1\">...</output></div></div><div class=\"card\"><small>Tight-side tension for 100 N slack (N)</small><div><output id=\"r2\">...</output></div></div></div><div class=\"plot\" id=\"plot\"></div><section><h2>How to investigate</h2><p>Record the default output, then move one slider at a time. Before changing the slider, predict the shape of the response. The chart plots the first output against the first input while holding the second input constant. Compare the predicted and computed trends. Finally, state the model limitation that matters most in a real device. All values are idealized; they are not measured field data.</p><div class=\"warn\">Educational model only. Not a product safety calculation, medical device analysis, or engineering certification.</div></section>",
    init: function(card) {
      try {
const model = (a,b) => [Math.exp(a*b),100*Math.exp(a*b)];
const aInput=card.querySelector('#a'),bInput=card.querySelector('#b');
const aVal=card.querySelector('#av'),bVal=card.querySelector('#bv'),r1=card.querySelector('#r1'),r2=card.querySelector('#r2');
const plot=card.querySelector('#plot');
const fmt=n=>Number.isFinite(n)?(Math.abs(n)>0&&Math.abs(n)<.0001?n.toExponential(3):n.toLocaleString('en-US',{maximumFractionDigits:5})):'undefined';
function draw(){
 const a=Number(aInput.value),b=Number(bInput.value); const r=model(a,b);
 aVal.textContent=fmt(a);bVal.textContent=fmt(b);r1.textContent=fmt(r[0]);r2.textContent=fmt(r[1]);
 const lo=Number(aInput.min),hi=Number(aInput.max),points=[];
 for(let i=0;i<=60;i++){const x=lo+(hi-lo)*i/60;const y=model(x,b)[0];if(Number.isFinite(y))points.push({x,y});}
 if(!points.length){plot.innerHTML='No valid plotting range';return}
 let ymin=Math.min(...points.map(p=>p.y)), ymax=Math.max(...points.map(p=>p.y));
 if(ymax===ymin){ymin-=1;ymax+=1;}
 const pad=(ymax-ymin)*.08; ymin-=pad;ymax+=pad;
 const px=x=>50+(x-lo)/(hi-lo)*620,py=y=>230-(y-ymin)/(ymax-ymin)*190;
 const line=points.map(p=>`${px(p.x).toFixed(1)},${py(p.y).toFixed(1)}`).join(' ');
 const c=px(a),d=py(r[0]);
 plot.innerHTML=`<svg viewBox="0 0 720 270" role="img" aria-label="Computed response plotted versus the first input" style="width:100%;height:auto">
 <line x1="50" x2="690" y1="230" y2="230" stroke="#7291ae"/><line x1="50" x2="50" y1="40" y2="230" stroke="#7291ae"/>
 <polyline points="${line}" fill="none" stroke="#74ddc1" stroke-width="3"/>
 <circle cx="${c}" cy="${d}" r="5" fill="#ffc47c"/>
 <text x="55" y="30" fill="#cadbec" font-size="14">Response ${fmt(ymin)} to ${fmt(ymax)}</text>
 <text x="455" y="256" fill="#cadbec" font-size="14">First input: ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
aInput.addEventListener('input',draw);bInput.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 10:', err);
      }
    }
  });

  MODELS.push({
    idx: 11,
    unit: 6,
    html: "<div class=\"hero\"><p class=\"meta\">Unit 6 \u00b7 Model 11 / 16 \u00b7 Offline interactive</p><h3>Constant-Acceleration Travel</h3><p>Compare speed and elapsed time effects on travel.</p><p class=\"formula\">x = v0 t + (1/2) a t\u00b2</p></div><div class=\"sim-controls\"><label class=\"control\">v0: <output id=\"av\">3</output> m/s<input id=\"a\" type=\"range\" min=\"0\" max=\"25\" value=\"3\" step=\"0.05000\" aria-label=\"v0\"></label>\n<label class=\"control\">t: <output id=\"bv\">4</output> s<input id=\"b\" type=\"range\" min=\"0\" max=\"12\" value=\"4\" step=\"0.02400\" aria-label=\"t\"></label></div>\n<div class=\"grid\"><div class=\"card\"><small>Displacement (m)</small><div><output id=\"r1\">...</output></div></div><div class=\"card\"><small>Final velocity (m/s)</small><div><output id=\"r2\">...</output></div></div></div><div class=\"plot\" id=\"plot\"></div><section><h2>How to investigate</h2><p>Record the default output, then move one slider at a time. Before changing the slider, predict the shape of the response. The chart plots the first output against the first input while holding the second input constant. Compare the predicted and computed trends. Finally, state the model limitation that matters most in a real device. All values are idealized; they are not measured field data.</p><div class=\"warn\">Educational model only. Not a product safety calculation, medical device analysis, or engineering certification.</div></section>",
    init: function(card) {
      try {
const model = (a,b) => [a*b+b*b,a+2*b];
const aInput=card.querySelector('#a'),bInput=card.querySelector('#b');
const aVal=card.querySelector('#av'),bVal=card.querySelector('#bv'),r1=card.querySelector('#r1'),r2=card.querySelector('#r2');
const plot=card.querySelector('#plot');
const fmt=n=>Number.isFinite(n)?(Math.abs(n)>0&&Math.abs(n)<.0001?n.toExponential(3):n.toLocaleString('en-US',{maximumFractionDigits:5})):'undefined';
function draw(){
 const a=Number(aInput.value),b=Number(bInput.value); const r=model(a,b);
 aVal.textContent=fmt(a);bVal.textContent=fmt(b);r1.textContent=fmt(r[0]);r2.textContent=fmt(r[1]);
 const lo=Number(aInput.min),hi=Number(aInput.max),points=[];
 for(let i=0;i<=60;i++){const x=lo+(hi-lo)*i/60;const y=model(x,b)[0];if(Number.isFinite(y))points.push({x,y});}
 if(!points.length){plot.innerHTML='No valid plotting range';return}
 let ymin=Math.min(...points.map(p=>p.y)), ymax=Math.max(...points.map(p=>p.y));
 if(ymax===ymin){ymin-=1;ymax+=1;}
 const pad=(ymax-ymin)*.08; ymin-=pad;ymax+=pad;
 const px=x=>50+(x-lo)/(hi-lo)*620,py=y=>230-(y-ymin)/(ymax-ymin)*190;
 const line=points.map(p=>`${px(p.x).toFixed(1)},${py(p.y).toFixed(1)}`).join(' ');
 const c=px(a),d=py(r[0]);
 plot.innerHTML=`<svg viewBox="0 0 720 270" role="img" aria-label="Computed response plotted versus the first input" style="width:100%;height:auto">
 <line x1="50" x2="690" y1="230" y2="230" stroke="#7291ae"/><line x1="50" x2="50" y1="40" y2="230" stroke="#7291ae"/>
 <polyline points="${line}" fill="none" stroke="#74ddc1" stroke-width="3"/>
 <circle cx="${c}" cy="${d}" r="5" fill="#ffc47c"/>
 <text x="55" y="30" fill="#cadbec" font-size="14">Response ${fmt(ymin)} to ${fmt(ymax)}</text>
 <text x="455" y="256" fill="#cadbec" font-size="14">First input: ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
aInput.addEventListener('input',draw);bInput.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 11:', err);
      }
    }
  });

  MODELS.push({
    idx: 12,
    unit: 6,
    html: "<div class=\"hero\"><p class=\"meta\">Unit 6 \u00b7 Model 12 / 16 \u00b7 Offline interactive</p><h3>Work to Speed</h3><p>Energy per unit mass controls the final ideal speed.</p><p class=\"formula\">v = sqrt(2W/m)</p></div><div class=\"sim-controls\"><label class=\"control\">W: <output id=\"av\">400</output> J<input id=\"a\" type=\"range\" min=\"5\" max=\"2000\" value=\"400\" step=\"3.99000\" aria-label=\"W\"></label>\n<label class=\"control\">m: <output id=\"bv\">20</output> kg<input id=\"b\" type=\"range\" min=\"1\" max=\"100\" value=\"20\" step=\"0.19800\" aria-label=\"m\"></label></div>\n<div class=\"grid\"><div class=\"card\"><small>Speed (m/s)</small><div><output id=\"r1\">...</output></div></div><div class=\"card\"><small>Specific work (J/kg)</small><div><output id=\"r2\">...</output></div></div></div><div class=\"plot\" id=\"plot\"></div><section><h2>How to investigate</h2><p>Record the default output, then move one slider at a time. Before changing the slider, predict the shape of the response. The chart plots the first output against the first input while holding the second input constant. Compare the predicted and computed trends. Finally, state the model limitation that matters most in a real device. All values are idealized; they are not measured field data.</p><div class=\"warn\">Educational model only. Not a product safety calculation, medical device analysis, or engineering certification.</div></section>",
    init: function(card) {
      try {
const model = (a,b) => [Math.sqrt(2*a/b),a/b];
const aInput=card.querySelector('#a'),bInput=card.querySelector('#b');
const aVal=card.querySelector('#av'),bVal=card.querySelector('#bv'),r1=card.querySelector('#r1'),r2=card.querySelector('#r2');
const plot=card.querySelector('#plot');
const fmt=n=>Number.isFinite(n)?(Math.abs(n)>0&&Math.abs(n)<.0001?n.toExponential(3):n.toLocaleString('en-US',{maximumFractionDigits:5})):'undefined';
function draw(){
 const a=Number(aInput.value),b=Number(bInput.value); const r=model(a,b);
 aVal.textContent=fmt(a);bVal.textContent=fmt(b);r1.textContent=fmt(r[0]);r2.textContent=fmt(r[1]);
 const lo=Number(aInput.min),hi=Number(aInput.max),points=[];
 for(let i=0;i<=60;i++){const x=lo+(hi-lo)*i/60;const y=model(x,b)[0];if(Number.isFinite(y))points.push({x,y});}
 if(!points.length){plot.innerHTML='No valid plotting range';return}
 let ymin=Math.min(...points.map(p=>p.y)), ymax=Math.max(...points.map(p=>p.y));
 if(ymax===ymin){ymin-=1;ymax+=1;}
 const pad=(ymax-ymin)*.08; ymin-=pad;ymax+=pad;
 const px=x=>50+(x-lo)/(hi-lo)*620,py=y=>230-(y-ymin)/(ymax-ymin)*190;
 const line=points.map(p=>`${px(p.x).toFixed(1)},${py(p.y).toFixed(1)}`).join(' ');
 const c=px(a),d=py(r[0]);
 plot.innerHTML=`<svg viewBox="0 0 720 270" role="img" aria-label="Computed response plotted versus the first input" style="width:100%;height:auto">
 <line x1="50" x2="690" y1="230" y2="230" stroke="#7291ae"/><line x1="50" x2="50" y1="40" y2="230" stroke="#7291ae"/>
 <polyline points="${line}" fill="none" stroke="#74ddc1" stroke-width="3"/>
 <circle cx="${c}" cy="${d}" r="5" fill="#ffc47c"/>
 <text x="55" y="30" fill="#cadbec" font-size="14">Response ${fmt(ymin)} to ${fmt(ymax)}</text>
 <text x="455" y="256" fill="#cadbec" font-size="14">First input: ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
aInput.addEventListener('input',draw);bInput.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 12:', err);
      }
    }
  });

  MODELS.push({
    idx: 13,
    unit: 7,
    html: "<div class=\"hero\"><p class=\"meta\">Unit 7 \u00b7 Model 13 / 16 \u00b7 Offline interactive</p><h3>Solid-Disk Inertia</h3><p>Moving mass farther from axis dramatically increases inertia.</p><p class=\"formula\">I = (1/2) m r\u00b2</p></div><div class=\"sim-controls\"><label class=\"control\">m: <output id=\"av\">10</output> kg<input id=\"a\" type=\"range\" min=\"0.5\" max=\"40\" value=\"10\" step=\"0.07900\" aria-label=\"m\"></label>\n<label class=\"control\">r: <output id=\"bv\">0.25</output> m<input id=\"b\" type=\"range\" min=\"0.05\" max=\"0.5\" value=\"0.25\" step=\"0.00100\" aria-label=\"r\"></label></div>\n<div class=\"grid\"><div class=\"card\"><small>Inertia (kg\u00b7m\u00b2)</small><div><output id=\"r1\">...</output></div></div><div class=\"card\"><small>Mass (kg)</small><div><output id=\"r2\">...</output></div></div></div><div class=\"plot\" id=\"plot\"></div><section><h2>How to investigate</h2><p>Record the default output, then move one slider at a time. Before changing the slider, predict the shape of the response. The chart plots the first output against the first input while holding the second input constant. Compare the predicted and computed trends. Finally, state the model limitation that matters most in a real device. All values are idealized; they are not measured field data.</p><div class=\"warn\">Educational model only. Not a product safety calculation, medical device analysis, or engineering certification.</div></section>",
    init: function(card) {
      try {
const model = (a,b) => [.5*a*b*b,a];
const aInput=card.querySelector('#a'),bInput=card.querySelector('#b');
const aVal=card.querySelector('#av'),bVal=card.querySelector('#bv'),r1=card.querySelector('#r1'),r2=card.querySelector('#r2');
const plot=card.querySelector('#plot');
const fmt=n=>Number.isFinite(n)?(Math.abs(n)>0&&Math.abs(n)<.0001?n.toExponential(3):n.toLocaleString('en-US',{maximumFractionDigits:5})):'undefined';
function draw(){
 const a=Number(aInput.value),b=Number(bInput.value); const r=model(a,b);
 aVal.textContent=fmt(a);bVal.textContent=fmt(b);r1.textContent=fmt(r[0]);r2.textContent=fmt(r[1]);
 const lo=Number(aInput.min),hi=Number(aInput.max),points=[];
 for(let i=0;i<=60;i++){const x=lo+(hi-lo)*i/60;const y=model(x,b)[0];if(Number.isFinite(y))points.push({x,y});}
 if(!points.length){plot.innerHTML='No valid plotting range';return}
 let ymin=Math.min(...points.map(p=>p.y)), ymax=Math.max(...points.map(p=>p.y));
 if(ymax===ymin){ymin-=1;ymax+=1;}
 const pad=(ymax-ymin)*.08; ymin-=pad;ymax+=pad;
 const px=x=>50+(x-lo)/(hi-lo)*620,py=y=>230-(y-ymin)/(ymax-ymin)*190;
 const line=points.map(p=>`${px(p.x).toFixed(1)},${py(p.y).toFixed(1)}`).join(' ');
 const c=px(a),d=py(r[0]);
 plot.innerHTML=`<svg viewBox="0 0 720 270" role="img" aria-label="Computed response plotted versus the first input" style="width:100%;height:auto">
 <line x1="50" x2="690" y1="230" y2="230" stroke="#7291ae"/><line x1="50" x2="50" y1="40" y2="230" stroke="#7291ae"/>
 <polyline points="${line}" fill="none" stroke="#74ddc1" stroke-width="3"/>
 <circle cx="${c}" cy="${d}" r="5" fill="#ffc47c"/>
 <text x="55" y="30" fill="#cadbec" font-size="14">Response ${fmt(ymin)} to ${fmt(ymax)}</text>
 <text x="455" y="256" fill="#cadbec" font-size="14">First input: ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
aInput.addEventListener('input',draw);bInput.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 13:', err);
      }
    }
  });

  MODELS.push({
    idx: 14,
    unit: 7,
    html: "<div class=\"hero\"><p class=\"meta\">Unit 7 \u00b7 Model 14 / 16 \u00b7 Offline interactive</p><h3>Pure Rolling</h3><p>No-slip condition relates ground speed to wheel radius.</p><p class=\"formula\">\u03c9 = v/r</p></div><div class=\"sim-controls\"><label class=\"control\">v: <output id=\"av\">3</output> m/s<input id=\"a\" type=\"range\" min=\"0.1\" max=\"25\" value=\"3\" step=\"0.04980\" aria-label=\"v\"></label>\n<label class=\"control\">r: <output id=\"bv\">0.3</output> m<input id=\"b\" type=\"range\" min=\"0.05\" max=\"1\" value=\"0.3\" step=\"0.00190\" aria-label=\"r\"></label></div>\n<div class=\"grid\"><div class=\"card\"><small>Angular speed (rad/s)</small><div><output id=\"r1\">...</output></div></div><div class=\"card\"><small>rpm</small><div><output id=\"r2\">...</output></div></div></div><div class=\"plot\" id=\"plot\"></div><section><h2>How to investigate</h2><p>Record the default output, then move one slider at a time. Before changing the slider, predict the shape of the response. The chart plots the first output against the first input while holding the second input constant. Compare the predicted and computed trends. Finally, state the model limitation that matters most in a real device. All values are idealized; they are not measured field data.</p><div class=\"warn\">Educational model only. Not a product safety calculation, medical device analysis, or engineering certification.</div></section>",
    init: function(card) {
      try {
const model = (a,b) => [a/b,60*a/(2*Math.PI*b)];
const aInput=card.querySelector('#a'),bInput=card.querySelector('#b');
const aVal=card.querySelector('#av'),bVal=card.querySelector('#bv'),r1=card.querySelector('#r1'),r2=card.querySelector('#r2');
const plot=card.querySelector('#plot');
const fmt=n=>Number.isFinite(n)?(Math.abs(n)>0&&Math.abs(n)<.0001?n.toExponential(3):n.toLocaleString('en-US',{maximumFractionDigits:5})):'undefined';
function draw(){
 const a=Number(aInput.value),b=Number(bInput.value); const r=model(a,b);
 aVal.textContent=fmt(a);bVal.textContent=fmt(b);r1.textContent=fmt(r[0]);r2.textContent=fmt(r[1]);
 const lo=Number(aInput.min),hi=Number(aInput.max),points=[];
 for(let i=0;i<=60;i++){const x=lo+(hi-lo)*i/60;const y=model(x,b)[0];if(Number.isFinite(y))points.push({x,y});}
 if(!points.length){plot.innerHTML='No valid plotting range';return}
 let ymin=Math.min(...points.map(p=>p.y)), ymax=Math.max(...points.map(p=>p.y));
 if(ymax===ymin){ymin-=1;ymax+=1;}
 const pad=(ymax-ymin)*.08; ymin-=pad;ymax+=pad;
 const px=x=>50+(x-lo)/(hi-lo)*620,py=y=>230-(y-ymin)/(ymax-ymin)*190;
 const line=points.map(p=>`${px(p.x).toFixed(1)},${py(p.y).toFixed(1)}`).join(' ');
 const c=px(a),d=py(r[0]);
 plot.innerHTML=`<svg viewBox="0 0 720 270" role="img" aria-label="Computed response plotted versus the first input" style="width:100%;height:auto">
 <line x1="50" x2="690" y1="230" y2="230" stroke="#7291ae"/><line x1="50" x2="50" y1="40" y2="230" stroke="#7291ae"/>
 <polyline points="${line}" fill="none" stroke="#74ddc1" stroke-width="3"/>
 <circle cx="${c}" cy="${d}" r="5" fill="#ffc47c"/>
 <text x="55" y="30" fill="#cadbec" font-size="14">Response ${fmt(ymin)} to ${fmt(ymax)}</text>
 <text x="455" y="256" fill="#cadbec" font-size="14">First input: ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
aInput.addEventListener('input',draw);bInput.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 14:', err);
      }
    }
  });

  MODELS.push({
    idx: 15,
    unit: 8,
    html: "<div class=\"hero\"><p class=\"meta\">Unit 8 \u00b7 Model 15 / 16 \u00b7 Offline interactive</p><h3>Ideal Lever</h3><p>Observe force gain traded against output travel.</p><p class=\"formula\">Fout = Fin \u00d7 (input arm / output arm)</p></div><div class=\"sim-controls\"><label class=\"control\">Fin: <output id=\"av\">100</output> N<input id=\"a\" type=\"range\" min=\"20\" max=\"400\" value=\"100\" step=\"0.76000\" aria-label=\"Fin\"></label>\n<label class=\"control\">ratio: <output id=\"bv\">7.5</output> <input id=\"b\" type=\"range\" min=\"1\" max=\"20\" value=\"7.5\" step=\"0.03800\" aria-label=\"ratio\"></label></div>\n<div class=\"grid\"><div class=\"card\"><small>Ideal output force (N)</small><div><output id=\"r1\">...</output></div></div><div class=\"card\"><small>Advantage</small><div><output id=\"r2\">...</output></div></div></div><div class=\"plot\" id=\"plot\"></div><section><h2>How to investigate</h2><p>Record the default output, then move one slider at a time. Before changing the slider, predict the shape of the response. The chart plots the first output against the first input while holding the second input constant. Compare the predicted and computed trends. Finally, state the model limitation that matters most in a real device. All values are idealized; they are not measured field data.</p><div class=\"warn\">Educational model only. Not a product safety calculation, medical device analysis, or engineering certification.</div></section>",
    init: function(card) {
      try {
const model = (a,b) => [a*b,b];
const aInput=card.querySelector('#a'),bInput=card.querySelector('#b');
const aVal=card.querySelector('#av'),bVal=card.querySelector('#bv'),r1=card.querySelector('#r1'),r2=card.querySelector('#r2');
const plot=card.querySelector('#plot');
const fmt=n=>Number.isFinite(n)?(Math.abs(n)>0&&Math.abs(n)<.0001?n.toExponential(3):n.toLocaleString('en-US',{maximumFractionDigits:5})):'undefined';
function draw(){
 const a=Number(aInput.value),b=Number(bInput.value); const r=model(a,b);
 aVal.textContent=fmt(a);bVal.textContent=fmt(b);r1.textContent=fmt(r[0]);r2.textContent=fmt(r[1]);
 const lo=Number(aInput.min),hi=Number(aInput.max),points=[];
 for(let i=0;i<=60;i++){const x=lo+(hi-lo)*i/60;const y=model(x,b)[0];if(Number.isFinite(y))points.push({x,y});}
 if(!points.length){plot.innerHTML='No valid plotting range';return}
 let ymin=Math.min(...points.map(p=>p.y)), ymax=Math.max(...points.map(p=>p.y));
 if(ymax===ymin){ymin-=1;ymax+=1;}
 const pad=(ymax-ymin)*.08; ymin-=pad;ymax+=pad;
 const px=x=>50+(x-lo)/(hi-lo)*620,py=y=>230-(y-ymin)/(ymax-ymin)*190;
 const line=points.map(p=>`${px(p.x).toFixed(1)},${py(p.y).toFixed(1)}`).join(' ');
 const c=px(a),d=py(r[0]);
 plot.innerHTML=`<svg viewBox="0 0 720 270" role="img" aria-label="Computed response plotted versus the first input" style="width:100%;height:auto">
 <line x1="50" x2="690" y1="230" y2="230" stroke="#7291ae"/><line x1="50" x2="50" y1="40" y2="230" stroke="#7291ae"/>
 <polyline points="${line}" fill="none" stroke="#74ddc1" stroke-width="3"/>
 <circle cx="${c}" cy="${d}" r="5" fill="#ffc47c"/>
 <text x="55" y="30" fill="#cadbec" font-size="14">Response ${fmt(ymin)} to ${fmt(ymax)}</text>
 <text x="455" y="256" fill="#cadbec" font-size="14">First input: ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
aInput.addEventListener('input',draw);bInput.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 15:', err);
      }
    }
  });

  MODELS.push({
    idx: 16,
    unit: 8,
    html: "<div class=\"hero\"><p class=\"meta\">Unit 8 \u00b7 Model 16 / 16 \u00b7 Offline interactive</p><h3>Hoist Drum Torque</h3><p>A larger drum radius raises holding torque at the same load.</p><p class=\"formula\">M = m g r</p></div><div class=\"sim-controls\"><label class=\"control\">m: <output id=\"av\">120</output> kg<input id=\"a\" type=\"range\" min=\"5\" max=\"500\" value=\"120\" step=\"0.99000\" aria-label=\"m\"></label>\n<label class=\"control\">r: <output id=\"bv\">0.12</output> m<input id=\"b\" type=\"range\" min=\"0.03\" max=\"0.6\" value=\"0.12\" step=\"0.00114\" aria-label=\"r\"></label></div>\n<div class=\"grid\"><div class=\"card\"><small>Torque (N\u00b7m)</small><div><output id=\"r1\">...</output></div></div><div class=\"card\"><small>Cable weight (N)</small><div><output id=\"r2\">...</output></div></div></div><div class=\"plot\" id=\"plot\"></div><section><h2>How to investigate</h2><p>Record the default output, then move one slider at a time. Before changing the slider, predict the shape of the response. The chart plots the first output against the first input while holding the second input constant. Compare the predicted and computed trends. Finally, state the model limitation that matters most in a real device. All values are idealized; they are not measured field data.</p><div class=\"warn\">Educational model only. Not a product safety calculation, medical device analysis, or engineering certification.</div></section>",
    init: function(card) {
      try {
const model = (a,b) => [a*9.81*b,a*9.81];
const aInput=card.querySelector('#a'),bInput=card.querySelector('#b');
const aVal=card.querySelector('#av'),bVal=card.querySelector('#bv'),r1=card.querySelector('#r1'),r2=card.querySelector('#r2');
const plot=card.querySelector('#plot');
const fmt=n=>Number.isFinite(n)?(Math.abs(n)>0&&Math.abs(n)<.0001?n.toExponential(3):n.toLocaleString('en-US',{maximumFractionDigits:5})):'undefined';
function draw(){
 const a=Number(aInput.value),b=Number(bInput.value); const r=model(a,b);
 aVal.textContent=fmt(a);bVal.textContent=fmt(b);r1.textContent=fmt(r[0]);r2.textContent=fmt(r[1]);
 const lo=Number(aInput.min),hi=Number(aInput.max),points=[];
 for(let i=0;i<=60;i++){const x=lo+(hi-lo)*i/60;const y=model(x,b)[0];if(Number.isFinite(y))points.push({x,y});}
 if(!points.length){plot.innerHTML='No valid plotting range';return}
 let ymin=Math.min(...points.map(p=>p.y)), ymax=Math.max(...points.map(p=>p.y));
 if(ymax===ymin){ymin-=1;ymax+=1;}
 const pad=(ymax-ymin)*.08; ymin-=pad;ymax+=pad;
 const px=x=>50+(x-lo)/(hi-lo)*620,py=y=>230-(y-ymin)/(ymax-ymin)*190;
 const line=points.map(p=>`${px(p.x).toFixed(1)},${py(p.y).toFixed(1)}`).join(' ');
 const c=px(a),d=py(r[0]);
 plot.innerHTML=`<svg viewBox="0 0 720 270" role="img" aria-label="Computed response plotted versus the first input" style="width:100%;height:auto">
 <line x1="50" x2="690" y1="230" y2="230" stroke="#7291ae"/><line x1="50" x2="50" y1="40" y2="230" stroke="#7291ae"/>
 <polyline points="${line}" fill="none" stroke="#74ddc1" stroke-width="3"/>
 <circle cx="${c}" cy="${d}" r="5" fill="#ffc47c"/>
 <text x="55" y="30" fill="#cadbec" font-size="14">Response ${fmt(ymin)} to ${fmt(ymax)}</text>
 <text x="455" y="256" fill="#cadbec" font-size="14">First input: ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
aInput.addEventListener('input',draw);bInput.addEventListener('input',draw);draw();
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

  // Auto-init when DOM is ready if #sim-container is present
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
