/* mechanics-of-solids Interactive Simulation Suite */
(function(window) {
  'use strict';

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: "<section class=\"hero\"><span class=\"tag\">MECHANICAL ENGINEERING \u00b7 UNIT 01 \u00b7 MODEL 01</span><h3>Nominal tensile stress</h3><p>Change either parameter to explore a numerical prediction. The chart shows the first output against the first slider while the second slider is held constant. The default values are illustrative; they are not field measurements.</p></section><section class=\"sim-controls\"><label class=\"control\">Axial force: <output id=\"av\">24</output> kN<input type=\"range\" id=\"a\" min=\"1\" max=\"200\" value=\"24\" step=\"0.01\" aria-label=\"Axial force\"></label><label class=\"control\">Net area: <output id=\"bv\">120</output> mm\u00b2<input type=\"range\" id=\"b\" min=\"50\" max=\"1500\" value=\"120\" step=\"0.01\" aria-label=\"Net area\"></label></section><section class=\"grid\"><article class=\"card\"><small>Nominal stress in MPa</small><div><output id=\"r1\">...</output></div></article><article class=\"card\"><small> illustrative strain at E = 200 GPa</small><div><output id=\"r2\">...</output></div></article></section><div id=\"plot\" class=\"plot\"></div><section><h2>Interpret and check</h2><p>Write a prediction before moving a slider. For one altered setting, calculate an independent value manually and explain the units. Then identify which physical assumption prevents extrapolating the curve indefinitely.</p><div class=\"warn\">Use only where uniform axial stress and known effective area are defensible. Educational formula only \u2014 not certification, design authorization or calibrated experimental data.</div></section>",
    init: function(card) {
      try {
const model=(a,b)=>{const y=[1000*a/b,1000*a/b/200000];return y};
const ia=card.querySelector("#" + 'a'.replace(/^#/, "")),ib=card.querySelector("#" + 'b'.replace(/^#/, "")),res1=card.querySelector("#" + 'r1'.replace(/^#/, "")),res2=card.querySelector("#" + 'r2'.replace(/^#/, "")),av=card.querySelector("#" + 'av'.replace(/^#/, "")),bv=card.querySelector("#" + 'bv'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const fmt=n=>!Number.isFinite(n)?'Not defined':(Math.abs(n)>0&&Math.abs(n)<0.0001?n.toExponential(4):n.toLocaleString('en-US',{maximumFractionDigits:5}));
function paint(){
 let a=Number(ia.value),b=Number(ib.value),v=model(a,b);av.textContent=fmt(a);bv.textContent=fmt(b);res1.textContent=fmt(v[0]);res2.textContent=fmt(v[1]);
 const lo=Number(ia.min),hi=Number(ia.max),pts=[];
 for(let k=0;k<=60;k++){let x=lo+(hi-lo)*k/60,y=model(x,b)[0];if(Number.isFinite(y))pts.push({x,y})}
 if(!pts.length){plot.textContent='No numeric response at these inputs';return}
 let mn=Math.min(...pts.map(x=>x.y)),mx=Math.max(...pts.map(x=>x.y));if(mx-mn<1e-12){mn-=1;mx+=1}let s=(mx-mn)*0.08;mn-=s;mx+=s;
 let tx=x=>52+620*(x-lo)/(hi-lo),ty=y=>235-185*(y-mn)/(mx-mn);
 const path=pts.map((q,i)=>(i?'L':'M')+tx(q.x).toFixed(2)+' '+ty(q.y).toFixed(2)).join(' ');
 plot.innerHTML=`<svg viewBox="0 0 720 270" style="width:100%;height:auto" role="img" aria-label="Output versus first slider with second held constant"><line x1="52" y1="235" x2="690" y2="235" stroke="#9caec4"/><line x1="52" y1="38" x2="52" y2="235" stroke="#9caec4"/><path d="${path}" fill="none" stroke="#74ddc1" stroke-width="3"/><circle cx="${tx(a)}" cy="${ty(v[0])}" r="5" fill="#ffcf81"/><text x="55" y="28" fill="#e4edf3" font-size="13">Output range: ${fmt(mn)} to ${fmt(mx)}</text><text x="405" y="258" fill="#e4edf3" font-size="13">First input ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
ia.addEventListener('input',paint);ib.addEventListener('input',paint);paint();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 1,
    html: "<section class=\"hero\"><span class=\"tag\">MECHANICAL ENGINEERING \u00b7 UNIT 01 \u00b7 MODEL 02</span><h3>Poisson lateral strain</h3><p>Change either parameter to explore a numerical prediction. The chart shows the first output against the first slider while the second slider is held constant. The default values are illustrative; they are not field measurements.</p></section><section class=\"sim-controls\"><label class=\"control\">Axial strain: <output id=\"av\">1200</output> microstrain<input type=\"range\" id=\"a\" min=\"100\" max=\"3000\" value=\"1200\" step=\"0.01\" aria-label=\"Axial strain\"></label><label class=\"control\">Poisson ratio: <output id=\"bv\">0.29</output><input type=\"range\" id=\"b\" min=\"0.1\" max=\"0.48\" value=\"0.29\" step=\"0.01\" aria-label=\"Poisson ratio\"></label></section><section class=\"grid\"><article class=\"card\"><small>Lateral microstrain</small><div><output id=\"r1\">...</output></div></article><article class=\"card\"><small> lateral millistrain</small><div><output id=\"r2\">...</output></div></article></section><div id=\"plot\" class=\"plot\"></div><section><h2>Interpret and check</h2><p>Write a prediction before moving a slider. For one altered setting, calculate an independent value manually and explain the units. Then identify which physical assumption prevents extrapolating the curve indefinitely.</p><div class=\"warn\">Uniaxial linear isotropic loading, small strain only. Educational formula only \u2014 not certification, design authorization or calibrated experimental data.</div></section>",
    init: function(card) {
      try {
const model=(a,b)=>{const y=[-a*b,-a*b/1000];return y};
const ia=card.querySelector("#" + 'a'.replace(/^#/, "")),ib=card.querySelector("#" + 'b'.replace(/^#/, "")),res1=card.querySelector("#" + 'r1'.replace(/^#/, "")),res2=card.querySelector("#" + 'r2'.replace(/^#/, "")),av=card.querySelector("#" + 'av'.replace(/^#/, "")),bv=card.querySelector("#" + 'bv'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const fmt=n=>!Number.isFinite(n)?'Not defined':(Math.abs(n)>0&&Math.abs(n)<0.0001?n.toExponential(4):n.toLocaleString('en-US',{maximumFractionDigits:5}));
function paint(){
 let a=Number(ia.value),b=Number(ib.value),v=model(a,b);av.textContent=fmt(a);bv.textContent=fmt(b);res1.textContent=fmt(v[0]);res2.textContent=fmt(v[1]);
 const lo=Number(ia.min),hi=Number(ia.max),pts=[];
 for(let k=0;k<=60;k++){let x=lo+(hi-lo)*k/60,y=model(x,b)[0];if(Number.isFinite(y))pts.push({x,y})}
 if(!pts.length){plot.textContent='No numeric response at these inputs';return}
 let mn=Math.min(...pts.map(x=>x.y)),mx=Math.max(...pts.map(x=>x.y));if(mx-mn<1e-12){mn-=1;mx+=1}let s=(mx-mn)*0.08;mn-=s;mx+=s;
 let tx=x=>52+620*(x-lo)/(hi-lo),ty=y=>235-185*(y-mn)/(mx-mn);
 const path=pts.map((q,i)=>(i?'L':'M')+tx(q.x).toFixed(2)+' '+ty(q.y).toFixed(2)).join(' ');
 plot.innerHTML=`<svg viewBox="0 0 720 270" style="width:100%;height:auto" role="img" aria-label="Output versus first slider with second held constant"><line x1="52" y1="235" x2="690" y2="235" stroke="#9caec4"/><line x1="52" y1="38" x2="52" y2="235" stroke="#9caec4"/><path d="${path}" fill="none" stroke="#74ddc1" stroke-width="3"/><circle cx="${tx(a)}" cy="${ty(v[0])}" r="5" fill="#ffcf81"/><text x="55" y="28" fill="#e4edf3" font-size="13">Output range: ${fmt(mn)} to ${fmt(mx)}</text><text x="405" y="258" fill="#e4edf3" font-size="13">First input ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
ia.addEventListener('input',paint);ib.addEventListener('input',paint);paint();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 2,
    html: "<section class=\"hero\"><span class=\"tag\">MECHANICAL ENGINEERING \u00b7 UNIT 02 \u00b7 MODEL 03</span><h3>Axial bar extension</h3><p>Change either parameter to explore a numerical prediction. The chart shows the first output against the first slider while the second slider is held constant. The default values are illustrative; they are not field measurements.</p></section><section class=\"sim-controls\"><label class=\"control\">Axial force: <output id=\"av\">20</output> kN<input type=\"range\" id=\"a\" min=\"1\" max=\"120\" value=\"20\" step=\"0.01\" aria-label=\"Axial force\"></label><label class=\"control\">Member length: <output id=\"bv\">2</output> m<input type=\"range\" id=\"b\" min=\"0.2\" max=\"6\" value=\"2\" step=\"0.01\" aria-label=\"Member length\"></label></section><section class=\"grid\"><article class=\"card\"><small>Elongation mm</small><div><output id=\"r1\">...</output></div></article><article class=\"card\"><small> normal stress MPa</small><div><output id=\"r2\">...</output></div></article></section><div id=\"plot\" class=\"plot\"></div><section><h2>Interpret and check</h2><p>Write a prediction before moving a slider. For one altered setting, calculate an independent value manually and explain the units. Then identify which physical assumption prevents extrapolating the curve indefinitely.</p><div class=\"warn\">A = 400 mm\u00b2 and E = 200 GPa fixed; small elastic extension. Educational formula only \u2014 not certification, design authorization or calibrated experimental data.</div></section>",
    init: function(card) {
      try {
const model=(a,b)=>{const y=[a*b*1e6/(400*200000),1000*a/400];return y};
const ia=card.querySelector("#" + 'a'.replace(/^#/, "")),ib=card.querySelector("#" + 'b'.replace(/^#/, "")),res1=card.querySelector("#" + 'r1'.replace(/^#/, "")),res2=card.querySelector("#" + 'r2'.replace(/^#/, "")),av=card.querySelector("#" + 'av'.replace(/^#/, "")),bv=card.querySelector("#" + 'bv'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const fmt=n=>!Number.isFinite(n)?'Not defined':(Math.abs(n)>0&&Math.abs(n)<0.0001?n.toExponential(4):n.toLocaleString('en-US',{maximumFractionDigits:5}));
function paint(){
 let a=Number(ia.value),b=Number(ib.value),v=model(a,b);av.textContent=fmt(a);bv.textContent=fmt(b);res1.textContent=fmt(v[0]);res2.textContent=fmt(v[1]);
 const lo=Number(ia.min),hi=Number(ia.max),pts=[];
 for(let k=0;k<=60;k++){let x=lo+(hi-lo)*k/60,y=model(x,b)[0];if(Number.isFinite(y))pts.push({x,y})}
 if(!pts.length){plot.textContent='No numeric response at these inputs';return}
 let mn=Math.min(...pts.map(x=>x.y)),mx=Math.max(...pts.map(x=>x.y));if(mx-mn<1e-12){mn-=1;mx+=1}let s=(mx-mn)*0.08;mn-=s;mx+=s;
 let tx=x=>52+620*(x-lo)/(hi-lo),ty=y=>235-185*(y-mn)/(mx-mn);
 const path=pts.map((q,i)=>(i?'L':'M')+tx(q.x).toFixed(2)+' '+ty(q.y).toFixed(2)).join(' ');
 plot.innerHTML=`<svg viewBox="0 0 720 270" style="width:100%;height:auto" role="img" aria-label="Output versus first slider with second held constant"><line x1="52" y1="235" x2="690" y2="235" stroke="#9caec4"/><line x1="52" y1="38" x2="52" y2="235" stroke="#9caec4"/><path d="${path}" fill="none" stroke="#74ddc1" stroke-width="3"/><circle cx="${tx(a)}" cy="${ty(v[0])}" r="5" fill="#ffcf81"/><text x="55" y="28" fill="#e4edf3" font-size="13">Output range: ${fmt(mn)} to ${fmt(mx)}</text><text x="405" y="258" fill="#e4edf3" font-size="13">First input ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
ia.addEventListener('input',paint);ib.addEventListener('input',paint);paint();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 2,
    html: "<section class=\"hero\"><span class=\"tag\">MECHANICAL ENGINEERING \u00b7 UNIT 02 \u00b7 MODEL 04</span><h3>Fully constrained thermal stress</h3><p>Change either parameter to explore a numerical prediction. The chart shows the first output against the first slider while the second slider is held constant. The default values are illustrative; they are not field measurements.</p></section><section class=\"sim-controls\"><label class=\"control\">Temperature rise: <output id=\"av\">40</output> K<input type=\"range\" id=\"a\" min=\"1\" max=\"150\" value=\"40\" step=\"0.01\" aria-label=\"Temperature rise\"></label><label class=\"control\">Expansion coefficient: <output id=\"bv\">12</output> microstrain/K<input type=\"range\" id=\"b\" min=\"5\" max=\"30\" value=\"12\" step=\"0.01\" aria-label=\"Expansion coefficient\"></label></section><section class=\"grid\"><article class=\"card\"><small>Thermal stress MPa</small><div><output id=\"r1\">...</output></div></article><article class=\"card\"><small> free strain microstrain</small><div><output id=\"r2\">...</output></div></article></section><div id=\"plot\" class=\"plot\"></div><section><h2>Interpret and check</h2><p>Write a prediction before moving a slider. For one altered setting, calculate an independent value manually and explain the units. Then identify which physical assumption prevents extrapolating the curve indefinitely.</p><div class=\"warn\">Ideal fully fixed axial bar with E = 200 GPa. Educational formula only \u2014 not certification, design authorization or calibrated experimental data.</div></section>",
    init: function(card) {
      try {
const model=(a,b)=>{const y=[-200*a*b/1000,a*b];return y};
const ia=card.querySelector("#" + 'a'.replace(/^#/, "")),ib=card.querySelector("#" + 'b'.replace(/^#/, "")),res1=card.querySelector("#" + 'r1'.replace(/^#/, "")),res2=card.querySelector("#" + 'r2'.replace(/^#/, "")),av=card.querySelector("#" + 'av'.replace(/^#/, "")),bv=card.querySelector("#" + 'bv'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const fmt=n=>!Number.isFinite(n)?'Not defined':(Math.abs(n)>0&&Math.abs(n)<0.0001?n.toExponential(4):n.toLocaleString('en-US',{maximumFractionDigits:5}));
function paint(){
 let a=Number(ia.value),b=Number(ib.value),v=model(a,b);av.textContent=fmt(a);bv.textContent=fmt(b);res1.textContent=fmt(v[0]);res2.textContent=fmt(v[1]);
 const lo=Number(ia.min),hi=Number(ia.max),pts=[];
 for(let k=0;k<=60;k++){let x=lo+(hi-lo)*k/60,y=model(x,b)[0];if(Number.isFinite(y))pts.push({x,y})}
 if(!pts.length){plot.textContent='No numeric response at these inputs';return}
 let mn=Math.min(...pts.map(x=>x.y)),mx=Math.max(...pts.map(x=>x.y));if(mx-mn<1e-12){mn-=1;mx+=1}let s=(mx-mn)*0.08;mn-=s;mx+=s;
 let tx=x=>52+620*(x-lo)/(hi-lo),ty=y=>235-185*(y-mn)/(mx-mn);
 const path=pts.map((q,i)=>(i?'L':'M')+tx(q.x).toFixed(2)+' '+ty(q.y).toFixed(2)).join(' ');
 plot.innerHTML=`<svg viewBox="0 0 720 270" style="width:100%;height:auto" role="img" aria-label="Output versus first slider with second held constant"><line x1="52" y1="235" x2="690" y2="235" stroke="#9caec4"/><line x1="52" y1="38" x2="52" y2="235" stroke="#9caec4"/><path d="${path}" fill="none" stroke="#74ddc1" stroke-width="3"/><circle cx="${tx(a)}" cy="${ty(v[0])}" r="5" fill="#ffcf81"/><text x="55" y="28" fill="#e4edf3" font-size="13">Output range: ${fmt(mn)} to ${fmt(mx)}</text><text x="405" y="258" fill="#e4edf3" font-size="13">First input ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
ia.addEventListener('input',paint);ib.addEventListener('input',paint);paint();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 3,
    html: "<section class=\"hero\"><span class=\"tag\">MECHANICAL ENGINEERING \u00b7 UNIT 03 \u00b7 MODEL 05</span><h3>Circular shaft shear</h3><p>Change either parameter to explore a numerical prediction. The chart shows the first output against the first slider while the second slider is held constant. The default values are illustrative; they are not field measurements.</p></section><section class=\"sim-controls\"><label class=\"control\">Torque: <output id=\"av\">400</output> N\u00b7m<input type=\"range\" id=\"a\" min=\"10\" max=\"2000\" value=\"400\" step=\"0.01\" aria-label=\"Torque\"></label><label class=\"control\">Diameter: <output id=\"bv\">30</output> mm<input type=\"range\" id=\"b\" min=\"10\" max=\"70\" value=\"30\" step=\"0.01\" aria-label=\"Diameter\"></label></section><section class=\"grid\"><article class=\"card\"><small>Surface shear MPa</small><div><output id=\"r1\">...</output></div></article><article class=\"card\"><small> torsional factor 32T/(\u03c0d\u2074)</small><div><output id=\"r2\">...</output></div></article></section><div id=\"plot\" class=\"plot\"></div><section><h2>Interpret and check</h2><p>Write a prediction before moving a slider. For one altered setting, calculate an independent value manually and explain the units. Then identify which physical assumption prevents extrapolating the curve indefinitely.</p><div class=\"warn\">Ideal solid round Saint-Venant torsion, no keyway. Educational formula only \u2014 not certification, design authorization or calibrated experimental data.</div></section>",
    init: function(card) {
      try {
const model=(a,b)=>{const y=[16*a*1000/(Math.PI*b**3),32*a*1000/(Math.PI*b**4)];return y};
const ia=card.querySelector("#" + 'a'.replace(/^#/, "")),ib=card.querySelector("#" + 'b'.replace(/^#/, "")),res1=card.querySelector("#" + 'r1'.replace(/^#/, "")),res2=card.querySelector("#" + 'r2'.replace(/^#/, "")),av=card.querySelector("#" + 'av'.replace(/^#/, "")),bv=card.querySelector("#" + 'bv'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const fmt=n=>!Number.isFinite(n)?'Not defined':(Math.abs(n)>0&&Math.abs(n)<0.0001?n.toExponential(4):n.toLocaleString('en-US',{maximumFractionDigits:5}));
function paint(){
 let a=Number(ia.value),b=Number(ib.value),v=model(a,b);av.textContent=fmt(a);bv.textContent=fmt(b);res1.textContent=fmt(v[0]);res2.textContent=fmt(v[1]);
 const lo=Number(ia.min),hi=Number(ia.max),pts=[];
 for(let k=0;k<=60;k++){let x=lo+(hi-lo)*k/60,y=model(x,b)[0];if(Number.isFinite(y))pts.push({x,y})}
 if(!pts.length){plot.textContent='No numeric response at these inputs';return}
 let mn=Math.min(...pts.map(x=>x.y)),mx=Math.max(...pts.map(x=>x.y));if(mx-mn<1e-12){mn-=1;mx+=1}let s=(mx-mn)*0.08;mn-=s;mx+=s;
 let tx=x=>52+620*(x-lo)/(hi-lo),ty=y=>235-185*(y-mn)/(mx-mn);
 const path=pts.map((q,i)=>(i?'L':'M')+tx(q.x).toFixed(2)+' '+ty(q.y).toFixed(2)).join(' ');
 plot.innerHTML=`<svg viewBox="0 0 720 270" style="width:100%;height:auto" role="img" aria-label="Output versus first slider with second held constant"><line x1="52" y1="235" x2="690" y2="235" stroke="#9caec4"/><line x1="52" y1="38" x2="52" y2="235" stroke="#9caec4"/><path d="${path}" fill="none" stroke="#74ddc1" stroke-width="3"/><circle cx="${tx(a)}" cy="${ty(v[0])}" r="5" fill="#ffcf81"/><text x="55" y="28" fill="#e4edf3" font-size="13">Output range: ${fmt(mn)} to ${fmt(mx)}</text><text x="405" y="258" fill="#e4edf3" font-size="13">First input ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
ia.addEventListener('input',paint);ib.addEventListener('input',paint);paint();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 3,
    html: "<section class=\"hero\"><span class=\"tag\">MECHANICAL ENGINEERING \u00b7 UNIT 03 \u00b7 MODEL 06</span><h3>Circular shaft twist</h3><p>Change either parameter to explore a numerical prediction. The chart shows the first output against the first slider while the second slider is held constant. The default values are illustrative; they are not field measurements.</p></section><section class=\"sim-controls\"><label class=\"control\">Torque: <output id=\"av\">100</output> N\u00b7m<input type=\"range\" id=\"a\" min=\"10\" max=\"1200\" value=\"100\" step=\"0.01\" aria-label=\"Torque\"></label><label class=\"control\">Shaft length: <output id=\"bv\">1</output> m<input type=\"range\" id=\"b\" min=\"0.2\" max=\"4\" value=\"1\" step=\"0.01\" aria-label=\"Shaft length\"></label></section><section class=\"grid\"><article class=\"card\"><small>Twist radians</small><div><output id=\"r1\">...</output></div></article><article class=\"card\"><small> twist degrees</small><div><output id=\"r2\">...</output></div></article></section><div id=\"plot\" class=\"plot\"></div><section><h2>Interpret and check</h2><p>Write a prediction before moving a slider. For one altered setting, calculate an independent value manually and explain the units. Then identify which physical assumption prevents extrapolating the curve indefinitely.</p><div class=\"warn\">Diameter fixed at 25 mm; G = 80 GPa. Educational formula only \u2014 not certification, design authorization or calibrated experimental data.</div></section>",
    init: function(card) {
      try {
const model=(a,b)=>{const y=[32*a*1000*b*1000/(Math.PI*80000*25**4),32*a*1000*b*1000/(Math.PI*80000*25**4)*180/Math.PI];return y};
const ia=card.querySelector("#" + 'a'.replace(/^#/, "")),ib=card.querySelector("#" + 'b'.replace(/^#/, "")),res1=card.querySelector("#" + 'r1'.replace(/^#/, "")),res2=card.querySelector("#" + 'r2'.replace(/^#/, "")),av=card.querySelector("#" + 'av'.replace(/^#/, "")),bv=card.querySelector("#" + 'bv'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const fmt=n=>!Number.isFinite(n)?'Not defined':(Math.abs(n)>0&&Math.abs(n)<0.0001?n.toExponential(4):n.toLocaleString('en-US',{maximumFractionDigits:5}));
function paint(){
 let a=Number(ia.value),b=Number(ib.value),v=model(a,b);av.textContent=fmt(a);bv.textContent=fmt(b);res1.textContent=fmt(v[0]);res2.textContent=fmt(v[1]);
 const lo=Number(ia.min),hi=Number(ia.max),pts=[];
 for(let k=0;k<=60;k++){let x=lo+(hi-lo)*k/60,y=model(x,b)[0];if(Number.isFinite(y))pts.push({x,y})}
 if(!pts.length){plot.textContent='No numeric response at these inputs';return}
 let mn=Math.min(...pts.map(x=>x.y)),mx=Math.max(...pts.map(x=>x.y));if(mx-mn<1e-12){mn-=1;mx+=1}let s=(mx-mn)*0.08;mn-=s;mx+=s;
 let tx=x=>52+620*(x-lo)/(hi-lo),ty=y=>235-185*(y-mn)/(mx-mn);
 const path=pts.map((q,i)=>(i?'L':'M')+tx(q.x).toFixed(2)+' '+ty(q.y).toFixed(2)).join(' ');
 plot.innerHTML=`<svg viewBox="0 0 720 270" style="width:100%;height:auto" role="img" aria-label="Output versus first slider with second held constant"><line x1="52" y1="235" x2="690" y2="235" stroke="#9caec4"/><line x1="52" y1="38" x2="52" y2="235" stroke="#9caec4"/><path d="${path}" fill="none" stroke="#74ddc1" stroke-width="3"/><circle cx="${tx(a)}" cy="${ty(v[0])}" r="5" fill="#ffcf81"/><text x="55" y="28" fill="#e4edf3" font-size="13">Output range: ${fmt(mn)} to ${fmt(mx)}</text><text x="405" y="258" fill="#e4edf3" font-size="13">First input ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
ia.addEventListener('input',paint);ib.addEventListener('input',paint);paint();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 4,
    html: "<section class=\"hero\"><span class=\"tag\">MECHANICAL ENGINEERING \u00b7 UNIT 04 \u00b7 MODEL 07</span><h3>Rectangular beam bending stress</h3><p>Change either parameter to explore a numerical prediction. The chart shows the first output against the first slider while the second slider is held constant. The default values are illustrative; they are not field measurements.</p></section><section class=\"sim-controls\"><label class=\"control\">Bending moment: <output id=\"av\">2</output> kN\u00b7m<input type=\"range\" id=\"a\" min=\"0.1\" max=\"10\" value=\"2\" step=\"0.01\" aria-label=\"Bending moment\"></label><label class=\"control\">Beam depth: <output id=\"bv\">80</output> mm<input type=\"range\" id=\"b\" min=\"30\" max=\"180\" value=\"80\" step=\"0.01\" aria-label=\"Beam depth\"></label></section><section class=\"grid\"><article class=\"card\"><small>Peak bending MPa</small><div><output id=\"r1\">...</output></div></article><article class=\"card\"><small> moment / I (N/mm\u00b3)</small><div><output id=\"r2\">...</output></div></article></section><div id=\"plot\" class=\"plot\"></div><section><h2>Interpret and check</h2><p>Write a prediction before moving a slider. For one altered setting, calculate an independent value manually and explain the units. Then identify which physical assumption prevents extrapolating the curve indefinitely.</p><div class=\"warn\">Width = 40 mm; simple symmetric linear bending. Educational formula only \u2014 not certification, design authorization or calibrated experimental data.</div></section>",
    init: function(card) {
      try {
const model=(a,b)=>{const y=[6*a*1e6/(40*b*b),a*1e6/(40*b**3/12)];return y};
const ia=card.querySelector("#" + 'a'.replace(/^#/, "")),ib=card.querySelector("#" + 'b'.replace(/^#/, "")),res1=card.querySelector("#" + 'r1'.replace(/^#/, "")),res2=card.querySelector("#" + 'r2'.replace(/^#/, "")),av=card.querySelector("#" + 'av'.replace(/^#/, "")),bv=card.querySelector("#" + 'bv'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const fmt=n=>!Number.isFinite(n)?'Not defined':(Math.abs(n)>0&&Math.abs(n)<0.0001?n.toExponential(4):n.toLocaleString('en-US',{maximumFractionDigits:5}));
function paint(){
 let a=Number(ia.value),b=Number(ib.value),v=model(a,b);av.textContent=fmt(a);bv.textContent=fmt(b);res1.textContent=fmt(v[0]);res2.textContent=fmt(v[1]);
 const lo=Number(ia.min),hi=Number(ia.max),pts=[];
 for(let k=0;k<=60;k++){let x=lo+(hi-lo)*k/60,y=model(x,b)[0];if(Number.isFinite(y))pts.push({x,y})}
 if(!pts.length){plot.textContent='No numeric response at these inputs';return}
 let mn=Math.min(...pts.map(x=>x.y)),mx=Math.max(...pts.map(x=>x.y));if(mx-mn<1e-12){mn-=1;mx+=1}let s=(mx-mn)*0.08;mn-=s;mx+=s;
 let tx=x=>52+620*(x-lo)/(hi-lo),ty=y=>235-185*(y-mn)/(mx-mn);
 const path=pts.map((q,i)=>(i?'L':'M')+tx(q.x).toFixed(2)+' '+ty(q.y).toFixed(2)).join(' ');
 plot.innerHTML=`<svg viewBox="0 0 720 270" style="width:100%;height:auto" role="img" aria-label="Output versus first slider with second held constant"><line x1="52" y1="235" x2="690" y2="235" stroke="#9caec4"/><line x1="52" y1="38" x2="52" y2="235" stroke="#9caec4"/><path d="${path}" fill="none" stroke="#74ddc1" stroke-width="3"/><circle cx="${tx(a)}" cy="${ty(v[0])}" r="5" fill="#ffcf81"/><text x="55" y="28" fill="#e4edf3" font-size="13">Output range: ${fmt(mn)} to ${fmt(mx)}</text><text x="405" y="258" fill="#e4edf3" font-size="13">First input ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
ia.addEventListener('input',paint);ib.addEventListener('input',paint);paint();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 4,
    html: "<section class=\"hero\"><span class=\"tag\">MECHANICAL ENGINEERING \u00b7 UNIT 04 \u00b7 MODEL 08</span><h3>Beam rectangular area moment</h3><p>Change either parameter to explore a numerical prediction. The chart shows the first output against the first slider while the second slider is held constant. The default values are illustrative; they are not field measurements.</p></section><section class=\"sim-controls\"><label class=\"control\">Beam depth: <output id=\"av\">100</output> mm<input type=\"range\" id=\"a\" min=\"20\" max=\"200\" value=\"100\" step=\"0.01\" aria-label=\"Beam depth\"></label><label class=\"control\">Beam width: <output id=\"bv\">50</output> mm<input type=\"range\" id=\"b\" min=\"10\" max=\"120\" value=\"50\" step=\"0.01\" aria-label=\"Beam width\"></label></section><section class=\"grid\"><article class=\"card\"><small>Area moment I (mm\u2074)</small><div><output id=\"r1\">...</output></div></article><article class=\"card\"><small> area (mm\u00b2)</small><div><output id=\"r2\">...</output></div></article></section><div id=\"plot\" class=\"plot\"></div><section><h2>Interpret and check</h2><p>Write a prediction before moving a slider. For one altered setting, calculate an independent value manually and explain the units. Then identify which physical assumption prevents extrapolating the curve indefinitely.</p><div class=\"warn\">About the centroidal horizontal axis. Educational formula only \u2014 not certification, design authorization or calibrated experimental data.</div></section>",
    init: function(card) {
      try {
const model=(a,b)=>{const y=[b*a**3/12,b*a];return y};
const ia=card.querySelector("#" + 'a'.replace(/^#/, "")),ib=card.querySelector("#" + 'b'.replace(/^#/, "")),res1=card.querySelector("#" + 'r1'.replace(/^#/, "")),res2=card.querySelector("#" + 'r2'.replace(/^#/, "")),av=card.querySelector("#" + 'av'.replace(/^#/, "")),bv=card.querySelector("#" + 'bv'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const fmt=n=>!Number.isFinite(n)?'Not defined':(Math.abs(n)>0&&Math.abs(n)<0.0001?n.toExponential(4):n.toLocaleString('en-US',{maximumFractionDigits:5}));
function paint(){
 let a=Number(ia.value),b=Number(ib.value),v=model(a,b);av.textContent=fmt(a);bv.textContent=fmt(b);res1.textContent=fmt(v[0]);res2.textContent=fmt(v[1]);
 const lo=Number(ia.min),hi=Number(ia.max),pts=[];
 for(let k=0;k<=60;k++){let x=lo+(hi-lo)*k/60,y=model(x,b)[0];if(Number.isFinite(y))pts.push({x,y})}
 if(!pts.length){plot.textContent='No numeric response at these inputs';return}
 let mn=Math.min(...pts.map(x=>x.y)),mx=Math.max(...pts.map(x=>x.y));if(mx-mn<1e-12){mn-=1;mx+=1}let s=(mx-mn)*0.08;mn-=s;mx+=s;
 let tx=x=>52+620*(x-lo)/(hi-lo),ty=y=>235-185*(y-mn)/(mx-mn);
 const path=pts.map((q,i)=>(i?'L':'M')+tx(q.x).toFixed(2)+' '+ty(q.y).toFixed(2)).join(' ');
 plot.innerHTML=`<svg viewBox="0 0 720 270" style="width:100%;height:auto" role="img" aria-label="Output versus first slider with second held constant"><line x1="52" y1="235" x2="690" y2="235" stroke="#9caec4"/><line x1="52" y1="38" x2="52" y2="235" stroke="#9caec4"/><path d="${path}" fill="none" stroke="#74ddc1" stroke-width="3"/><circle cx="${tx(a)}" cy="${ty(v[0])}" r="5" fill="#ffcf81"/><text x="55" y="28" fill="#e4edf3" font-size="13">Output range: ${fmt(mn)} to ${fmt(mx)}</text><text x="405" y="258" fill="#e4edf3" font-size="13">First input ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
ia.addEventListener('input',paint);ib.addEventListener('input',paint);paint();
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  MODELS.push({
    idx: 9,
    unit: 5,
    html: "<section class=\"hero\"><span class=\"tag\">MECHANICAL ENGINEERING \u00b7 UNIT 05 \u00b7 MODEL 09</span><h3>Midspan point-load deflection</h3><p>Change either parameter to explore a numerical prediction. The chart shows the first output against the first slider while the second slider is held constant. The default values are illustrative; they are not field measurements.</p></section><section class=\"sim-controls\"><label class=\"control\">Point load: <output id=\"av\">8</output> kN<input type=\"range\" id=\"a\" min=\"0.2\" max=\"50\" value=\"8\" step=\"0.01\" aria-label=\"Point load\"></label><label class=\"control\">Span: <output id=\"bv\">3</output> m<input type=\"range\" id=\"b\" min=\"0.5\" max=\"7\" value=\"3\" step=\"0.01\" aria-label=\"Span\"></label></section><section class=\"grid\"><article class=\"card\"><small>Midspan deflection mm</small><div><output id=\"r1\">...</output></div></article><article class=\"card\"><small> maximum moment kN\u00b7m</small><div><output id=\"r2\">...</output></div></article></section><div id=\"plot\" class=\"plot\"></div><section><h2>Interpret and check</h2><p>Write a prediction before moving a slider. For one altered setting, calculate an independent value manually and explain the units. Then identify which physical assumption prevents extrapolating the curve indefinitely.</p><div class=\"warn\">Simply supported; E = 200 GPa; I = 800 cm\u2074. Educational formula only \u2014 not certification, design authorization or calibrated experimental data.</div></section>",
    init: function(card) {
      try {
const model=(a,b)=>{const y=[a*b**3*1e5/(48*200*800),a*b/(4)];return y};
const ia=card.querySelector("#" + 'a'.replace(/^#/, "")),ib=card.querySelector("#" + 'b'.replace(/^#/, "")),res1=card.querySelector("#" + 'r1'.replace(/^#/, "")),res2=card.querySelector("#" + 'r2'.replace(/^#/, "")),av=card.querySelector("#" + 'av'.replace(/^#/, "")),bv=card.querySelector("#" + 'bv'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const fmt=n=>!Number.isFinite(n)?'Not defined':(Math.abs(n)>0&&Math.abs(n)<0.0001?n.toExponential(4):n.toLocaleString('en-US',{maximumFractionDigits:5}));
function paint(){
 let a=Number(ia.value),b=Number(ib.value),v=model(a,b);av.textContent=fmt(a);bv.textContent=fmt(b);res1.textContent=fmt(v[0]);res2.textContent=fmt(v[1]);
 const lo=Number(ia.min),hi=Number(ia.max),pts=[];
 for(let k=0;k<=60;k++){let x=lo+(hi-lo)*k/60,y=model(x,b)[0];if(Number.isFinite(y))pts.push({x,y})}
 if(!pts.length){plot.textContent='No numeric response at these inputs';return}
 let mn=Math.min(...pts.map(x=>x.y)),mx=Math.max(...pts.map(x=>x.y));if(mx-mn<1e-12){mn-=1;mx+=1}let s=(mx-mn)*0.08;mn-=s;mx+=s;
 let tx=x=>52+620*(x-lo)/(hi-lo),ty=y=>235-185*(y-mn)/(mx-mn);
 const path=pts.map((q,i)=>(i?'L':'M')+tx(q.x).toFixed(2)+' '+ty(q.y).toFixed(2)).join(' ');
 plot.innerHTML=`<svg viewBox="0 0 720 270" style="width:100%;height:auto" role="img" aria-label="Output versus first slider with second held constant"><line x1="52" y1="235" x2="690" y2="235" stroke="#9caec4"/><line x1="52" y1="38" x2="52" y2="235" stroke="#9caec4"/><path d="${path}" fill="none" stroke="#74ddc1" stroke-width="3"/><circle cx="${tx(a)}" cy="${ty(v[0])}" r="5" fill="#ffcf81"/><text x="55" y="28" fill="#e4edf3" font-size="13">Output range: ${fmt(mn)} to ${fmt(mx)}</text><text x="405" y="258" fill="#e4edf3" font-size="13">First input ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
ia.addEventListener('input',paint);ib.addEventListener('input',paint);paint();
      } catch (err) {
        console.warn('Sim init error in model 9:', err);
      }
    }
  });

  MODELS.push({
    idx: 10,
    unit: 5,
    html: "<section class=\"hero\"><span class=\"tag\">MECHANICAL ENGINEERING \u00b7 UNIT 05 \u00b7 MODEL 10</span><h3>Cantilever point-load deflection</h3><p>Change either parameter to explore a numerical prediction. The chart shows the first output against the first slider while the second slider is held constant. The default values are illustrative; they are not field measurements.</p></section><section class=\"sim-controls\"><label class=\"control\">Tip load: <output id=\"av\">500</output> N<input type=\"range\" id=\"a\" min=\"20\" max=\"2500\" value=\"500\" step=\"0.01\" aria-label=\"Tip load\"></label><label class=\"control\">Cantilever length: <output id=\"bv\">1</output> m<input type=\"range\" id=\"b\" min=\"0.2\" max=\"3\" value=\"1\" step=\"0.01\" aria-label=\"Cantilever length\"></label></section><section class=\"grid\"><article class=\"card\"><small>Tip deflection mm</small><div><output id=\"r1\">...</output></div></article><article class=\"card\"><small> tip rotation radians</small><div><output id=\"r2\">...</output></div></article></section><div id=\"plot\" class=\"plot\"></div><section><h2>Interpret and check</h2><p>Write a prediction before moving a slider. For one altered setting, calculate an independent value manually and explain the units. Then identify which physical assumption prevents extrapolating the curve indefinitely.</p><div class=\"warn\">E = 200 GPa; I = 400 cm\u2074; small-deflection cantilever. Educational formula only \u2014 not certification, design authorization or calibrated experimental data.</div></section>",
    init: function(card) {
      try {
const model=(a,b)=>{const y=[a*b**3*1e3/(3*200e9*(400e-8)),a*b*b/(2*200e9*(400e-8))];return y};
const ia=card.querySelector("#" + 'a'.replace(/^#/, "")),ib=card.querySelector("#" + 'b'.replace(/^#/, "")),res1=card.querySelector("#" + 'r1'.replace(/^#/, "")),res2=card.querySelector("#" + 'r2'.replace(/^#/, "")),av=card.querySelector("#" + 'av'.replace(/^#/, "")),bv=card.querySelector("#" + 'bv'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const fmt=n=>!Number.isFinite(n)?'Not defined':(Math.abs(n)>0&&Math.abs(n)<0.0001?n.toExponential(4):n.toLocaleString('en-US',{maximumFractionDigits:5}));
function paint(){
 let a=Number(ia.value),b=Number(ib.value),v=model(a,b);av.textContent=fmt(a);bv.textContent=fmt(b);res1.textContent=fmt(v[0]);res2.textContent=fmt(v[1]);
 const lo=Number(ia.min),hi=Number(ia.max),pts=[];
 for(let k=0;k<=60;k++){let x=lo+(hi-lo)*k/60,y=model(x,b)[0];if(Number.isFinite(y))pts.push({x,y})}
 if(!pts.length){plot.textContent='No numeric response at these inputs';return}
 let mn=Math.min(...pts.map(x=>x.y)),mx=Math.max(...pts.map(x=>x.y));if(mx-mn<1e-12){mn-=1;mx+=1}let s=(mx-mn)*0.08;mn-=s;mx+=s;
 let tx=x=>52+620*(x-lo)/(hi-lo),ty=y=>235-185*(y-mn)/(mx-mn);
 const path=pts.map((q,i)=>(i?'L':'M')+tx(q.x).toFixed(2)+' '+ty(q.y).toFixed(2)).join(' ');
 plot.innerHTML=`<svg viewBox="0 0 720 270" style="width:100%;height:auto" role="img" aria-label="Output versus first slider with second held constant"><line x1="52" y1="235" x2="690" y2="235" stroke="#9caec4"/><line x1="52" y1="38" x2="52" y2="235" stroke="#9caec4"/><path d="${path}" fill="none" stroke="#74ddc1" stroke-width="3"/><circle cx="${tx(a)}" cy="${ty(v[0])}" r="5" fill="#ffcf81"/><text x="55" y="28" fill="#e4edf3" font-size="13">Output range: ${fmt(mn)} to ${fmt(mx)}</text><text x="405" y="258" fill="#e4edf3" font-size="13">First input ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
ia.addEventListener('input',paint);ib.addEventListener('input',paint);paint();
      } catch (err) {
        console.warn('Sim init error in model 10:', err);
      }
    }
  });

  MODELS.push({
    idx: 11,
    unit: 6,
    html: "<section class=\"hero\"><span class=\"tag\">MECHANICAL ENGINEERING \u00b7 UNIT 06 \u00b7 MODEL 11</span><h3>Plane stress principal values</h3><p>Change either parameter to explore a numerical prediction. The chart shows the first output against the first slider while the second slider is held constant. The default values are illustrative; they are not field measurements.</p></section><section class=\"sim-controls\"><label class=\"control\">Normal sigma_x: <output id=\"av\">100</output> MPa<input type=\"range\" id=\"a\" min=\"-150\" max=\"200\" value=\"100\" step=\"0.01\" aria-label=\"Normal sigma_x\"></label><label class=\"control\">Shear tau_xy: <output id=\"bv\">30</output> MPa<input type=\"range\" id=\"b\" min=\"-100\" max=\"100\" value=\"30\" step=\"0.01\" aria-label=\"Shear tau_xy\"></label></section><section class=\"grid\"><article class=\"card\"><small>Larger in-plane principal MPa</small><div><output id=\"r1\">...</output></div></article><article class=\"card\"><small> smaller principal MPa</small><div><output id=\"r2\">...</output></div></article></section><div id=\"plot\" class=\"plot\"></div><section><h2>Interpret and check</h2><p>Write a prediction before moving a slider. For one altered setting, calculate an independent value manually and explain the units. Then identify which physical assumption prevents extrapolating the curve indefinitely.</p><div class=\"warn\">Plane stress with fixed sigma_y = 20 MPa. Educational formula only \u2014 not certification, design authorization or calibrated experimental data.</div></section>",
    init: function(card) {
      try {
const model=(a,b)=>{const y=[(a+20)/2+Math.hypot((a-20)/2,b),(a+20)/2-Math.hypot((a-20)/2,b)];return y};
const ia=card.querySelector("#" + 'a'.replace(/^#/, "")),ib=card.querySelector("#" + 'b'.replace(/^#/, "")),res1=card.querySelector("#" + 'r1'.replace(/^#/, "")),res2=card.querySelector("#" + 'r2'.replace(/^#/, "")),av=card.querySelector("#" + 'av'.replace(/^#/, "")),bv=card.querySelector("#" + 'bv'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const fmt=n=>!Number.isFinite(n)?'Not defined':(Math.abs(n)>0&&Math.abs(n)<0.0001?n.toExponential(4):n.toLocaleString('en-US',{maximumFractionDigits:5}));
function paint(){
 let a=Number(ia.value),b=Number(ib.value),v=model(a,b);av.textContent=fmt(a);bv.textContent=fmt(b);res1.textContent=fmt(v[0]);res2.textContent=fmt(v[1]);
 const lo=Number(ia.min),hi=Number(ia.max),pts=[];
 for(let k=0;k<=60;k++){let x=lo+(hi-lo)*k/60,y=model(x,b)[0];if(Number.isFinite(y))pts.push({x,y})}
 if(!pts.length){plot.textContent='No numeric response at these inputs';return}
 let mn=Math.min(...pts.map(x=>x.y)),mx=Math.max(...pts.map(x=>x.y));if(mx-mn<1e-12){mn-=1;mx+=1}let s=(mx-mn)*0.08;mn-=s;mx+=s;
 let tx=x=>52+620*(x-lo)/(hi-lo),ty=y=>235-185*(y-mn)/(mx-mn);
 const path=pts.map((q,i)=>(i?'L':'M')+tx(q.x).toFixed(2)+' '+ty(q.y).toFixed(2)).join(' ');
 plot.innerHTML=`<svg viewBox="0 0 720 270" style="width:100%;height:auto" role="img" aria-label="Output versus first slider with second held constant"><line x1="52" y1="235" x2="690" y2="235" stroke="#9caec4"/><line x1="52" y1="38" x2="52" y2="235" stroke="#9caec4"/><path d="${path}" fill="none" stroke="#74ddc1" stroke-width="3"/><circle cx="${tx(a)}" cy="${ty(v[0])}" r="5" fill="#ffcf81"/><text x="55" y="28" fill="#e4edf3" font-size="13">Output range: ${fmt(mn)} to ${fmt(mx)}</text><text x="405" y="258" fill="#e4edf3" font-size="13">First input ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
ia.addEventListener('input',paint);ib.addEventListener('input',paint);paint();
      } catch (err) {
        console.warn('Sim init error in model 11:', err);
      }
    }
  });

  MODELS.push({
    idx: 12,
    unit: 6,
    html: "<section class=\"hero\"><span class=\"tag\">MECHANICAL ENGINEERING \u00b7 UNIT 06 \u00b7 MODEL 12</span><h3>Von Mises plane stress</h3><p>Change either parameter to explore a numerical prediction. The chart shows the first output against the first slider while the second slider is held constant. The default values are illustrative; they are not field measurements.</p></section><section class=\"sim-controls\"><label class=\"control\">Normal sigma_x: <output id=\"av\">100</output> MPa<input type=\"range\" id=\"a\" min=\"0\" max=\"300\" value=\"100\" step=\"0.01\" aria-label=\"Normal sigma_x\"></label><label class=\"control\">Shear tau_xy: <output id=\"bv\">50</output> MPa<input type=\"range\" id=\"b\" min=\"0\" max=\"140\" value=\"50\" step=\"0.01\" aria-label=\"Shear tau_xy\"></label></section><section class=\"grid\"><article class=\"card\"><small>Von Mises equivalent MPa</small><div><output id=\"r1\">...</output></div></article><article class=\"card\"><small> in-plane Mohr radius MPa</small><div><output id=\"r2\">...</output></div></article></section><div id=\"plot\" class=\"plot\"></div><section><h2>Interpret and check</h2><p>Write a prediction before moving a slider. For one altered setting, calculate an independent value manually and explain the units. Then identify which physical assumption prevents extrapolating the curve indefinitely.</p><div class=\"warn\">Plane stress sigma_y = 0; isotropic ductile yield screening. Educational formula only \u2014 not certification, design authorization or calibrated experimental data.</div></section>",
    init: function(card) {
      try {
const model=(a,b)=>{const y=[Math.sqrt(a*a+3*b*b),Math.sqrt((a/2)**2+b*b)];return y};
const ia=card.querySelector("#" + 'a'.replace(/^#/, "")),ib=card.querySelector("#" + 'b'.replace(/^#/, "")),res1=card.querySelector("#" + 'r1'.replace(/^#/, "")),res2=card.querySelector("#" + 'r2'.replace(/^#/, "")),av=card.querySelector("#" + 'av'.replace(/^#/, "")),bv=card.querySelector("#" + 'bv'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const fmt=n=>!Number.isFinite(n)?'Not defined':(Math.abs(n)>0&&Math.abs(n)<0.0001?n.toExponential(4):n.toLocaleString('en-US',{maximumFractionDigits:5}));
function paint(){
 let a=Number(ia.value),b=Number(ib.value),v=model(a,b);av.textContent=fmt(a);bv.textContent=fmt(b);res1.textContent=fmt(v[0]);res2.textContent=fmt(v[1]);
 const lo=Number(ia.min),hi=Number(ia.max),pts=[];
 for(let k=0;k<=60;k++){let x=lo+(hi-lo)*k/60,y=model(x,b)[0];if(Number.isFinite(y))pts.push({x,y})}
 if(!pts.length){plot.textContent='No numeric response at these inputs';return}
 let mn=Math.min(...pts.map(x=>x.y)),mx=Math.max(...pts.map(x=>x.y));if(mx-mn<1e-12){mn-=1;mx+=1}let s=(mx-mn)*0.08;mn-=s;mx+=s;
 let tx=x=>52+620*(x-lo)/(hi-lo),ty=y=>235-185*(y-mn)/(mx-mn);
 const path=pts.map((q,i)=>(i?'L':'M')+tx(q.x).toFixed(2)+' '+ty(q.y).toFixed(2)).join(' ');
 plot.innerHTML=`<svg viewBox="0 0 720 270" style="width:100%;height:auto" role="img" aria-label="Output versus first slider with second held constant"><line x1="52" y1="235" x2="690" y2="235" stroke="#9caec4"/><line x1="52" y1="38" x2="52" y2="235" stroke="#9caec4"/><path d="${path}" fill="none" stroke="#74ddc1" stroke-width="3"/><circle cx="${tx(a)}" cy="${ty(v[0])}" r="5" fill="#ffcf81"/><text x="55" y="28" fill="#e4edf3" font-size="13">Output range: ${fmt(mn)} to ${fmt(mx)}</text><text x="405" y="258" fill="#e4edf3" font-size="13">First input ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
ia.addEventListener('input',paint);ib.addEventListener('input',paint);paint();
      } catch (err) {
        console.warn('Sim init error in model 12:', err);
      }
    }
  });

  MODELS.push({
    idx: 13,
    unit: 7,
    html: "<section class=\"hero\"><span class=\"tag\">MECHANICAL ENGINEERING \u00b7 UNIT 07 \u00b7 MODEL 13</span><h3>Euler pinned-column buckling</h3><p>Change either parameter to explore a numerical prediction. The chart shows the first output against the first slider while the second slider is held constant. The default values are illustrative; they are not field measurements.</p></section><section class=\"sim-controls\"><label class=\"control\">Elastic modulus: <output id=\"av\">200</output> GPa<input type=\"range\" id=\"a\" min=\"50\" max=\"230\" value=\"200\" step=\"0.01\" aria-label=\"Elastic modulus\"></label><label class=\"control\">Column length: <output id=\"bv\">3</output> m<input type=\"range\" id=\"b\" min=\"0.8\" max=\"7\" value=\"3\" step=\"0.01\" aria-label=\"Column length\"></label></section><section class=\"grid\"><article class=\"card\"><small>Ideal critical load kN</small><div><output id=\"r1\">...</output></div></article><article class=\"card\"><small> illustrative 1/4 load kN</small><div><output id=\"r2\">...</output></div></article></section><div id=\"plot\" class=\"plot\"></div><section><h2>Interpret and check</h2><p>Write a prediction before moving a slider. For one altered setting, calculate an independent value manually and explain the units. Then identify which physical assumption prevents extrapolating the curve indefinitely.</p><div class=\"warn\">Pinned\u2013pinned, I=400 cm\u2074, ideal slender elastic column. Educational formula only \u2014 not certification, design authorization or calibrated experimental data.</div></section>",
    init: function(card) {
      try {
const model=(a,b)=>{const y=[Math.PI**2*0.01*a*400/(b*b),Math.PI**2*0.01*a*400/(b*b)/4];return y};
const ia=card.querySelector("#" + 'a'.replace(/^#/, "")),ib=card.querySelector("#" + 'b'.replace(/^#/, "")),res1=card.querySelector("#" + 'r1'.replace(/^#/, "")),res2=card.querySelector("#" + 'r2'.replace(/^#/, "")),av=card.querySelector("#" + 'av'.replace(/^#/, "")),bv=card.querySelector("#" + 'bv'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const fmt=n=>!Number.isFinite(n)?'Not defined':(Math.abs(n)>0&&Math.abs(n)<0.0001?n.toExponential(4):n.toLocaleString('en-US',{maximumFractionDigits:5}));
function paint(){
 let a=Number(ia.value),b=Number(ib.value),v=model(a,b);av.textContent=fmt(a);bv.textContent=fmt(b);res1.textContent=fmt(v[0]);res2.textContent=fmt(v[1]);
 const lo=Number(ia.min),hi=Number(ia.max),pts=[];
 for(let k=0;k<=60;k++){let x=lo+(hi-lo)*k/60,y=model(x,b)[0];if(Number.isFinite(y))pts.push({x,y})}
 if(!pts.length){plot.textContent='No numeric response at these inputs';return}
 let mn=Math.min(...pts.map(x=>x.y)),mx=Math.max(...pts.map(x=>x.y));if(mx-mn<1e-12){mn-=1;mx+=1}let s=(mx-mn)*0.08;mn-=s;mx+=s;
 let tx=x=>52+620*(x-lo)/(hi-lo),ty=y=>235-185*(y-mn)/(mx-mn);
 const path=pts.map((q,i)=>(i?'L':'M')+tx(q.x).toFixed(2)+' '+ty(q.y).toFixed(2)).join(' ');
 plot.innerHTML=`<svg viewBox="0 0 720 270" style="width:100%;height:auto" role="img" aria-label="Output versus first slider with second held constant"><line x1="52" y1="235" x2="690" y2="235" stroke="#9caec4"/><line x1="52" y1="38" x2="52" y2="235" stroke="#9caec4"/><path d="${path}" fill="none" stroke="#74ddc1" stroke-width="3"/><circle cx="${tx(a)}" cy="${ty(v[0])}" r="5" fill="#ffcf81"/><text x="55" y="28" fill="#e4edf3" font-size="13">Output range: ${fmt(mn)} to ${fmt(mx)}</text><text x="405" y="258" fill="#e4edf3" font-size="13">First input ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
ia.addEventListener('input',paint);ib.addEventListener('input',paint);paint();
      } catch (err) {
        console.warn('Sim init error in model 13:', err);
      }
    }
  });

  MODELS.push({
    idx: 14,
    unit: 7,
    html: "<section class=\"hero\"><span class=\"tag\">MECHANICAL ENGINEERING \u00b7 UNIT 07 \u00b7 MODEL 14</span><h3>Crack-tip mode I intensity</h3><p>Change either parameter to explore a numerical prediction. The chart shows the first output against the first slider while the second slider is held constant. The default values are illustrative; they are not field measurements.</p></section><section class=\"sim-controls\"><label class=\"control\">Nominal stress: <output id=\"av\">100</output> MPa<input type=\"range\" id=\"a\" min=\"10\" max=\"350\" value=\"100\" step=\"0.01\" aria-label=\"Nominal stress\"></label><label class=\"control\">Crack size: <output id=\"bv\">1</output> mm<input type=\"range\" id=\"b\" min=\"0.1\" max=\"10\" value=\"1\" step=\"0.01\" aria-label=\"Crack size\"></label></section><section class=\"grid\"><article class=\"card\"><small>K_I MPa\u221am</small><div><output id=\"r1\">...</output></div></article><article class=\"card\"><small> K_I/40 MPa\u221am ratio</small><div><output id=\"r2\">...</output></div></article></section><div id=\"plot\" class=\"plot\"></div><section><h2>Interpret and check</h2><p>Write a prediction before moving a slider. For one altered setting, calculate an independent value manually and explain the units. Then identify which physical assumption prevents extrapolating the curve indefinitely.</p><div class=\"warn\">Illustrative Y = 1; ratio uses hypothetical toughness 40 MPa\u221am. Educational formula only \u2014 not certification, design authorization or calibrated experimental data.</div></section>",
    init: function(card) {
      try {
const model=(a,b)=>{const y=[a*Math.sqrt(Math.PI*b/1000),a*Math.sqrt(Math.PI*b/1000)/40];return y};
const ia=card.querySelector("#" + 'a'.replace(/^#/, "")),ib=card.querySelector("#" + 'b'.replace(/^#/, "")),res1=card.querySelector("#" + 'r1'.replace(/^#/, "")),res2=card.querySelector("#" + 'r2'.replace(/^#/, "")),av=card.querySelector("#" + 'av'.replace(/^#/, "")),bv=card.querySelector("#" + 'bv'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const fmt=n=>!Number.isFinite(n)?'Not defined':(Math.abs(n)>0&&Math.abs(n)<0.0001?n.toExponential(4):n.toLocaleString('en-US',{maximumFractionDigits:5}));
function paint(){
 let a=Number(ia.value),b=Number(ib.value),v=model(a,b);av.textContent=fmt(a);bv.textContent=fmt(b);res1.textContent=fmt(v[0]);res2.textContent=fmt(v[1]);
 const lo=Number(ia.min),hi=Number(ia.max),pts=[];
 for(let k=0;k<=60;k++){let x=lo+(hi-lo)*k/60,y=model(x,b)[0];if(Number.isFinite(y))pts.push({x,y})}
 if(!pts.length){plot.textContent='No numeric response at these inputs';return}
 let mn=Math.min(...pts.map(x=>x.y)),mx=Math.max(...pts.map(x=>x.y));if(mx-mn<1e-12){mn-=1;mx+=1}let s=(mx-mn)*0.08;mn-=s;mx+=s;
 let tx=x=>52+620*(x-lo)/(hi-lo),ty=y=>235-185*(y-mn)/(mx-mn);
 const path=pts.map((q,i)=>(i?'L':'M')+tx(q.x).toFixed(2)+' '+ty(q.y).toFixed(2)).join(' ');
 plot.innerHTML=`<svg viewBox="0 0 720 270" style="width:100%;height:auto" role="img" aria-label="Output versus first slider with second held constant"><line x1="52" y1="235" x2="690" y2="235" stroke="#9caec4"/><line x1="52" y1="38" x2="52" y2="235" stroke="#9caec4"/><path d="${path}" fill="none" stroke="#74ddc1" stroke-width="3"/><circle cx="${tx(a)}" cy="${ty(v[0])}" r="5" fill="#ffcf81"/><text x="55" y="28" fill="#e4edf3" font-size="13">Output range: ${fmt(mn)} to ${fmt(mx)}</text><text x="405" y="258" fill="#e4edf3" font-size="13">First input ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
ia.addEventListener('input',paint);ib.addEventListener('input',paint);paint();
      } catch (err) {
        console.warn('Sim init error in model 14:', err);
      }
    }
  });

  MODELS.push({
    idx: 15,
    unit: 8,
    html: "<section class=\"hero\"><span class=\"tag\">MECHANICAL ENGINEERING \u00b7 UNIT 08 \u00b7 MODEL 15</span><h3>Strain gauge response</h3><p>Change either parameter to explore a numerical prediction. The chart shows the first output against the first slider while the second slider is held constant. The default values are illustrative; they are not field measurements.</p></section><section class=\"sim-controls\"><label class=\"control\">Axial strain: <output id=\"av\">600</output> microstrain<input type=\"range\" id=\"a\" min=\"50\" max=\"2500\" value=\"600\" step=\"0.01\" aria-label=\"Axial strain\"></label><label class=\"control\">Gauge factor: <output id=\"bv\">2.1</output><input type=\"range\" id=\"b\" min=\"1.5\" max=\"3\" value=\"2.1\" step=\"0.01\" aria-label=\"Gauge factor\"></label></section><section class=\"grid\"><article class=\"card\"><small>\u0394R/R (dimensionless)</small><div><output id=\"r1\">...</output></div></article><article class=\"card\"><small> \u0394R/R as percent</small><div><output id=\"r2\">...</output></div></article></section><div id=\"plot\" class=\"plot\"></div><section><h2>Interpret and check</h2><p>Write a prediction before moving a slider. For one altered setting, calculate an independent value manually and explain the units. Then identify which physical assumption prevents extrapolating the curve indefinitely.</p><div class=\"warn\">Constant gauge factor; neglects temperature, transverse sensitivity. Educational formula only \u2014 not certification, design authorization or calibrated experimental data.</div></section>",
    init: function(card) {
      try {
const model=(a,b)=>{const y=[a*1e-6*b,a*b*0.0001];return y};
const ia=card.querySelector("#" + 'a'.replace(/^#/, "")),ib=card.querySelector("#" + 'b'.replace(/^#/, "")),res1=card.querySelector("#" + 'r1'.replace(/^#/, "")),res2=card.querySelector("#" + 'r2'.replace(/^#/, "")),av=card.querySelector("#" + 'av'.replace(/^#/, "")),bv=card.querySelector("#" + 'bv'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const fmt=n=>!Number.isFinite(n)?'Not defined':(Math.abs(n)>0&&Math.abs(n)<0.0001?n.toExponential(4):n.toLocaleString('en-US',{maximumFractionDigits:5}));
function paint(){
 let a=Number(ia.value),b=Number(ib.value),v=model(a,b);av.textContent=fmt(a);bv.textContent=fmt(b);res1.textContent=fmt(v[0]);res2.textContent=fmt(v[1]);
 const lo=Number(ia.min),hi=Number(ia.max),pts=[];
 for(let k=0;k<=60;k++){let x=lo+(hi-lo)*k/60,y=model(x,b)[0];if(Number.isFinite(y))pts.push({x,y})}
 if(!pts.length){plot.textContent='No numeric response at these inputs';return}
 let mn=Math.min(...pts.map(x=>x.y)),mx=Math.max(...pts.map(x=>x.y));if(mx-mn<1e-12){mn-=1;mx+=1}let s=(mx-mn)*0.08;mn-=s;mx+=s;
 let tx=x=>52+620*(x-lo)/(hi-lo),ty=y=>235-185*(y-mn)/(mx-mn);
 const path=pts.map((q,i)=>(i?'L':'M')+tx(q.x).toFixed(2)+' '+ty(q.y).toFixed(2)).join(' ');
 plot.innerHTML=`<svg viewBox="0 0 720 270" style="width:100%;height:auto" role="img" aria-label="Output versus first slider with second held constant"><line x1="52" y1="235" x2="690" y2="235" stroke="#9caec4"/><line x1="52" y1="38" x2="52" y2="235" stroke="#9caec4"/><path d="${path}" fill="none" stroke="#74ddc1" stroke-width="3"/><circle cx="${tx(a)}" cy="${ty(v[0])}" r="5" fill="#ffcf81"/><text x="55" y="28" fill="#e4edf3" font-size="13">Output range: ${fmt(mn)} to ${fmt(mx)}</text><text x="405" y="258" fill="#e4edf3" font-size="13">First input ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
ia.addEventListener('input',paint);ib.addEventListener('input',paint);paint();
      } catch (err) {
        console.warn('Sim init error in model 15:', err);
      }
    }
  });

  MODELS.push({
    idx: 16,
    unit: 8,
    html: "<section class=\"hero\"><span class=\"tag\">MECHANICAL ENGINEERING \u00b7 UNIT 08 \u00b7 MODEL 16</span><h3>Beam section sensitivity</h3><p>Change either parameter to explore a numerical prediction. The chart shows the first output against the first slider while the second slider is held constant. The default values are illustrative; they are not field measurements.</p></section><section class=\"sim-controls\"><label class=\"control\">Height change: <output id=\"av\">2</output> percent<input type=\"range\" id=\"a\" min=\"-15\" max=\"15\" value=\"2\" step=\"0.01\" aria-label=\"Height change\"></label><label class=\"control\">Original height: <output id=\"bv\">100</output> mm<input type=\"range\" id=\"b\" min=\"30\" max=\"180\" value=\"100\" step=\"0.01\" aria-label=\"Original height\"></label></section><section class=\"grid\"><article class=\"card\"><small>Relative bending I</small><div><output id=\"r1\">...</output></div></article><article class=\"card\"><small> new height mm</small><div><output id=\"r2\">...</output></div></article></section><div id=\"plot\" class=\"plot\"></div><section><h2>Interpret and check</h2><p>Write a prediction before moving a slider. For one altered setting, calculate an independent value manually and explain the units. Then identify which physical assumption prevents extrapolating the curve indefinitely.</p><div class=\"warn\">Constant width; centroidal rectangular section. Educational formula only \u2014 not certification, design authorization or calibrated experimental data.</div></section>",
    init: function(card) {
      try {
const model=(a,b)=>{const y=[(1+a/100)**3, b*(1+a/100)];return y};
const ia=card.querySelector("#" + 'a'.replace(/^#/, "")),ib=card.querySelector("#" + 'b'.replace(/^#/, "")),res1=card.querySelector("#" + 'r1'.replace(/^#/, "")),res2=card.querySelector("#" + 'r2'.replace(/^#/, "")),av=card.querySelector("#" + 'av'.replace(/^#/, "")),bv=card.querySelector("#" + 'bv'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
const fmt=n=>!Number.isFinite(n)?'Not defined':(Math.abs(n)>0&&Math.abs(n)<0.0001?n.toExponential(4):n.toLocaleString('en-US',{maximumFractionDigits:5}));
function paint(){
 let a=Number(ia.value),b=Number(ib.value),v=model(a,b);av.textContent=fmt(a);bv.textContent=fmt(b);res1.textContent=fmt(v[0]);res2.textContent=fmt(v[1]);
 const lo=Number(ia.min),hi=Number(ia.max),pts=[];
 for(let k=0;k<=60;k++){let x=lo+(hi-lo)*k/60,y=model(x,b)[0];if(Number.isFinite(y))pts.push({x,y})}
 if(!pts.length){plot.textContent='No numeric response at these inputs';return}
 let mn=Math.min(...pts.map(x=>x.y)),mx=Math.max(...pts.map(x=>x.y));if(mx-mn<1e-12){mn-=1;mx+=1}let s=(mx-mn)*0.08;mn-=s;mx+=s;
 let tx=x=>52+620*(x-lo)/(hi-lo),ty=y=>235-185*(y-mn)/(mx-mn);
 const path=pts.map((q,i)=>(i?'L':'M')+tx(q.x).toFixed(2)+' '+ty(q.y).toFixed(2)).join(' ');
 plot.innerHTML=`<svg viewBox="0 0 720 270" style="width:100%;height:auto" role="img" aria-label="Output versus first slider with second held constant"><line x1="52" y1="235" x2="690" y2="235" stroke="#9caec4"/><line x1="52" y1="38" x2="52" y2="235" stroke="#9caec4"/><path d="${path}" fill="none" stroke="#74ddc1" stroke-width="3"/><circle cx="${tx(a)}" cy="${ty(v[0])}" r="5" fill="#ffcf81"/><text x="55" y="28" fill="#e4edf3" font-size="13">Output range: ${fmt(mn)} to ${fmt(mx)}</text><text x="405" y="258" fill="#e4edf3" font-size="13">First input ${fmt(lo)} to ${fmt(hi)}</text></svg>`;
}
ia.addEventListener('input',paint);ib.addEventListener('input',paint);paint();
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
