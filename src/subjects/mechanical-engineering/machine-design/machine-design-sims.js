/* machine-design Interactive Simulation Suite */
(function(window) {
  'use strict';

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 01 / 16</span><h3>Shaft torsional shear</h3><p>Shaft torque creates nominal surface shear; shoulders and keyways require extra treatment.</p><div class=\"flex\"></div></section><div class=\"notice\">Educational demonstration only. No material, machine or industrial process has been experimentally validated.</div><section class=\"sim\"><h2>Explore one variable</h2><label for=\"variable\">d (mm)</label><input id=\"variable\" type=\"range\" min=\"20\" max=\"65\" step=\"1\" value=\"35\" aria-describedby=\"readout\"><div class=\"flex\"><strong id=\"readout\"></strong></div><output id=\"answer\" for=\"variable\"></output><svg viewBox=\"0 0 545 225\" role=\"img\" aria-label=\"Graph of predicted response over slider range\"><line x1=\"36\" y1=\"15\" x2=\"36\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><line x1=\"36\" y1=\"192\" x2=\"510\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><g id=\"curve\"></g><text x=\"35\" y=\"213\" fill=\"#467181\" font-size=\"12\">20</text><text x=\"460\" y=\"213\" fill=\"#467181\" font-size=\"12\">65</text></svg><p class=\"muted\" id=\"ymax\"></p></section><section class=\"paper\"><h2>Equation and domain</h2><p>This intentionally simplified model demonstrates one physical relationship. Shaft torque creates nominal surface shear; shoulders and keyways require extra treatment. Assumptions: T=160 N\u00b7m; ideal solid, circular shaft. Other loading, geometry, fatigue, thermal effects and manufacturing scatter are not represented. Do not use as an industrial selection or safety approval.</p><p>Move the control toward both limits; compare the direction and curvature of the response. For a real design, obtain independent strength or life data, evaluate load cases and verify physical dimensions and units.</p><h2>Suggested analysis exercise</h2><p>Record three values of d (mm) and their outputs. Calculate a finite-difference sensitivity and explain whether the response changes linearly. State one neglected effect that might make the actual measured response different.</p></section>",
    init: function(card) {
      try {
const calc = (x) => 16*160/(Math.PI*Math.pow(x/1000,3))/1e6;
const lo=20, hi=65;
const inp=card.querySelector("#" + 'variable'.replace(/^#/, ""));
const out=card.querySelector("#" + 'answer'.replace(/^#/, ""));
const chart=card.querySelector("#" + 'curve'.replace(/^#/, ""));
const xread=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const yl=card.querySelector("#" + 'ymax'.replace(/^#/, ""));
function draw(){
 const x=Number(inp.value),y=calc(x),vals=[];
 for(let j=0;j<=65;j++) vals.push(calc(lo+(hi-lo)*j/65));
 const ymin=Math.min(...vals),ymax=Math.max(...vals),span=Math.max(1e-12,ymax-ymin),fx=(xx)=>36+xx*470,fy=(v)=>188-(v-ymin)/span*145;
 const points=vals.map((v,j)=>fx(j/65).toFixed(2)+','+fy(v).toFixed(2)).join(' ');
 const markerX=fx((x-lo)/(hi-lo)),markerY=fy(y);
 chart.innerHTML='<polyline fill="none" stroke="#0b8593" stroke-width="3.4" points="'+points+'"/><circle cx="'+markerX.toFixed(2)+'" cy="'+markerY.toFixed(2)+'" r="7" fill="#d27424" stroke="white" stroke-width="2"/>';
 out.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' MPa';
 xread.textContent=x.toLocaleString('en-US',{maximumFractionDigits:2})+' (d (mm))';
 yl.textContent='Range '+ymin.toLocaleString('en-US',{maximumFractionDigits:3})+' to '+ymax.toLocaleString('en-US',{maximumFractionDigits:3})+' MPa';
}
inp.addEventListener('input',draw); draw();
window.modelCalc=calc;
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 1,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 02 / 16</span><h3>Angle of twist</h3><p>Elastic shaft twist depends on torque, length, shear modulus and diameter to the fourth power.</p><div class=\"flex\"></div></section><div class=\"notice\">Educational demonstration only. No material, machine or industrial process has been experimentally validated.</div><section class=\"sim\"><h2>Explore one variable</h2><label for=\"variable\">d (mm)</label><input id=\"variable\" type=\"range\" min=\"20\" max=\"65\" step=\"1\" value=\"35\" aria-describedby=\"readout\"><div class=\"flex\"><strong id=\"readout\"></strong></div><output id=\"answer\" for=\"variable\"></output><svg viewBox=\"0 0 545 225\" role=\"img\" aria-label=\"Graph of predicted response over slider range\"><line x1=\"36\" y1=\"15\" x2=\"36\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><line x1=\"36\" y1=\"192\" x2=\"510\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><g id=\"curve\"></g><text x=\"35\" y=\"213\" fill=\"#467181\" font-size=\"12\">20</text><text x=\"460\" y=\"213\" fill=\"#467181\" font-size=\"12\">65</text></svg><p class=\"muted\" id=\"ymax\"></p></section><section class=\"paper\"><h2>Equation and domain</h2><p>This intentionally simplified model demonstrates one physical relationship. Elastic shaft twist depends on torque, length, shear modulus and diameter to the fourth power. Assumptions: T=120 N\u00b7m; L=0.70 m; G=79 GPa. Other loading, geometry, fatigue, thermal effects and manufacturing scatter are not represented. Do not use as an industrial selection or safety approval.</p><p>Move the control toward both limits; compare the direction and curvature of the response. For a real design, obtain independent strength or life data, evaluate load cases and verify physical dimensions and units.</p><h2>Suggested analysis exercise</h2><p>Record three values of d (mm) and their outputs. Calculate a finite-difference sensitivity and explain whether the response changes linearly. State one neglected effect that might make the actual measured response different.</p></section>",
    init: function(card) {
      try {
const calc = (x) => 32*120*0.7/(Math.PI*79e9*Math.pow(x/1000,4))*180/Math.PI;
const lo=20, hi=65;
const inp=card.querySelector("#" + 'variable'.replace(/^#/, ""));
const out=card.querySelector("#" + 'answer'.replace(/^#/, ""));
const chart=card.querySelector("#" + 'curve'.replace(/^#/, ""));
const xread=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const yl=card.querySelector("#" + 'ymax'.replace(/^#/, ""));
function draw(){
 const x=Number(inp.value),y=calc(x),vals=[];
 for(let j=0;j<=65;j++) vals.push(calc(lo+(hi-lo)*j/65));
 const ymin=Math.min(...vals),ymax=Math.max(...vals),span=Math.max(1e-12,ymax-ymin),fx=(xx)=>36+xx*470,fy=(v)=>188-(v-ymin)/span*145;
 const points=vals.map((v,j)=>fx(j/65).toFixed(2)+','+fy(v).toFixed(2)).join(' ');
 const markerX=fx((x-lo)/(hi-lo)),markerY=fy(y);
 chart.innerHTML='<polyline fill="none" stroke="#0b8593" stroke-width="3.4" points="'+points+'"/><circle cx="'+markerX.toFixed(2)+'" cy="'+markerY.toFixed(2)+'" r="7" fill="#d27424" stroke="white" stroke-width="2"/>';
 out.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' degrees';
 xread.textContent=x.toLocaleString('en-US',{maximumFractionDigits:2})+' (d (mm))';
 yl.textContent='Range '+ymin.toLocaleString('en-US',{maximumFractionDigits:3})+' to '+ymax.toLocaleString('en-US',{maximumFractionDigits:3})+' degrees';
}
inp.addEventListener('input',draw); draw();
window.modelCalc=calc;
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 2,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 03 / 16</span><h3>Nominal bending stress</h3><p>Simple elastic outer-fiber bending stress for a solid circular section.</p><div class=\"flex\"></div></section><div class=\"notice\">Educational demonstration only. No material, machine or industrial process has been experimentally validated.</div><section class=\"sim\"><h2>Explore one variable</h2><label for=\"variable\">d (mm)</label><input id=\"variable\" type=\"range\" min=\"20\" max=\"65\" step=\"1\" value=\"35\" aria-describedby=\"readout\"><div class=\"flex\"><strong id=\"readout\"></strong></div><output id=\"answer\" for=\"variable\"></output><svg viewBox=\"0 0 545 225\" role=\"img\" aria-label=\"Graph of predicted response over slider range\"><line x1=\"36\" y1=\"15\" x2=\"36\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><line x1=\"36\" y1=\"192\" x2=\"510\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><g id=\"curve\"></g><text x=\"35\" y=\"213\" fill=\"#467181\" font-size=\"12\">20</text><text x=\"460\" y=\"213\" fill=\"#467181\" font-size=\"12\">65</text></svg><p class=\"muted\" id=\"ymax\"></p></section><section class=\"paper\"><h2>Equation and domain</h2><p>This intentionally simplified model demonstrates one physical relationship. Simple elastic outer-fiber bending stress for a solid circular section. Assumptions: Moment=110 N\u00b7m; stress concentrations omitted. Other loading, geometry, fatigue, thermal effects and manufacturing scatter are not represented. Do not use as an industrial selection or safety approval.</p><p>Move the control toward both limits; compare the direction and curvature of the response. For a real design, obtain independent strength or life data, evaluate load cases and verify physical dimensions and units.</p><h2>Suggested analysis exercise</h2><p>Record three values of d (mm) and their outputs. Calculate a finite-difference sensitivity and explain whether the response changes linearly. State one neglected effect that might make the actual measured response different.</p></section>",
    init: function(card) {
      try {
const calc = (x) => 32*110/(Math.PI*Math.pow(x/1000,3))/1e6;
const lo=20, hi=65;
const inp=card.querySelector("#" + 'variable'.replace(/^#/, ""));
const out=card.querySelector("#" + 'answer'.replace(/^#/, ""));
const chart=card.querySelector("#" + 'curve'.replace(/^#/, ""));
const xread=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const yl=card.querySelector("#" + 'ymax'.replace(/^#/, ""));
function draw(){
 const x=Number(inp.value),y=calc(x),vals=[];
 for(let j=0;j<=65;j++) vals.push(calc(lo+(hi-lo)*j/65));
 const ymin=Math.min(...vals),ymax=Math.max(...vals),span=Math.max(1e-12,ymax-ymin),fx=(xx)=>36+xx*470,fy=(v)=>188-(v-ymin)/span*145;
 const points=vals.map((v,j)=>fx(j/65).toFixed(2)+','+fy(v).toFixed(2)).join(' ');
 const markerX=fx((x-lo)/(hi-lo)),markerY=fy(y);
 chart.innerHTML='<polyline fill="none" stroke="#0b8593" stroke-width="3.4" points="'+points+'"/><circle cx="'+markerX.toFixed(2)+'" cy="'+markerY.toFixed(2)+'" r="7" fill="#d27424" stroke="white" stroke-width="2"/>';
 out.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' MPa';
 xread.textContent=x.toLocaleString('en-US',{maximumFractionDigits:2})+' (d (mm))';
 yl.textContent='Range '+ymin.toLocaleString('en-US',{maximumFractionDigits:3})+' to '+ymax.toLocaleString('en-US',{maximumFractionDigits:3})+' MPa';
}
inp.addEventListener('input',draw); draw();
window.modelCalc=calc;
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 2,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 04 / 16</span><h3>Combined shaft von Mises stress</h3><p>Distortion-energy equivalent stress for nominal bending plus torsional shear.</p><div class=\"flex\"></div></section><div class=\"notice\">Educational demonstration only. No material, machine or industrial process has been experimentally validated.</div><section class=\"sim\"><h2>Explore one variable</h2><label for=\"variable\">d (mm)</label><input id=\"variable\" type=\"range\" min=\"20\" max=\"65\" step=\"1\" value=\"35\" aria-describedby=\"readout\"><div class=\"flex\"><strong id=\"readout\"></strong></div><output id=\"answer\" for=\"variable\"></output><svg viewBox=\"0 0 545 225\" role=\"img\" aria-label=\"Graph of predicted response over slider range\"><line x1=\"36\" y1=\"15\" x2=\"36\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><line x1=\"36\" y1=\"192\" x2=\"510\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><g id=\"curve\"></g><text x=\"35\" y=\"213\" fill=\"#467181\" font-size=\"12\">20</text><text x=\"460\" y=\"213\" fill=\"#467181\" font-size=\"12\">65</text></svg><p class=\"muted\" id=\"ymax\"></p></section><section class=\"paper\"><h2>Equation and domain</h2><p>This intentionally simplified model demonstrates one physical relationship. Distortion-energy equivalent stress for nominal bending plus torsional shear. Assumptions: M=110 N\u00b7m; T=80 N\u00b7m; nominal elastic state. Other loading, geometry, fatigue, thermal effects and manufacturing scatter are not represented. Do not use as an industrial selection or safety approval.</p><p>Move the control toward both limits; compare the direction and curvature of the response. For a real design, obtain independent strength or life data, evaluate load cases and verify physical dimensions and units.</p><h2>Suggested analysis exercise</h2><p>Record three values of d (mm) and their outputs. Calculate a finite-difference sensitivity and explain whether the response changes linearly. State one neglected effect that might make the actual measured response different.</p></section>",
    init: function(card) {
      try {
const calc = (x) => Math.sqrt(Math.pow(32*110/(Math.PI*Math.pow(x/1000,3)),2)+3*Math.pow(16*80/(Math.PI*Math.pow(x/1000,3)),2))/1e6;
const lo=20, hi=65;
const inp=card.querySelector("#" + 'variable'.replace(/^#/, ""));
const out=card.querySelector("#" + 'answer'.replace(/^#/, ""));
const chart=card.querySelector("#" + 'curve'.replace(/^#/, ""));
const xread=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const yl=card.querySelector("#" + 'ymax'.replace(/^#/, ""));
function draw(){
 const x=Number(inp.value),y=calc(x),vals=[];
 for(let j=0;j<=65;j++) vals.push(calc(lo+(hi-lo)*j/65));
 const ymin=Math.min(...vals),ymax=Math.max(...vals),span=Math.max(1e-12,ymax-ymin),fx=(xx)=>36+xx*470,fy=(v)=>188-(v-ymin)/span*145;
 const points=vals.map((v,j)=>fx(j/65).toFixed(2)+','+fy(v).toFixed(2)).join(' ');
 const markerX=fx((x-lo)/(hi-lo)),markerY=fy(y);
 chart.innerHTML='<polyline fill="none" stroke="#0b8593" stroke-width="3.4" points="'+points+'"/><circle cx="'+markerX.toFixed(2)+'" cy="'+markerY.toFixed(2)+'" r="7" fill="#d27424" stroke="white" stroke-width="2"/>';
 out.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' MPa';
 xread.textContent=x.toLocaleString('en-US',{maximumFractionDigits:2})+' (d (mm))';
 yl.textContent='Range '+ymin.toLocaleString('en-US',{maximumFractionDigits:3})+' to '+ymax.toLocaleString('en-US',{maximumFractionDigits:3})+' MPa';
}
inp.addEventListener('input',draw); draw();
window.modelCalc=calc;
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 3,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 05 / 16</span><h3>Modified Goodman screening factor</h3><p>Approximate fatigue safety-factor screen, only for positive mean stress and known material allowables.</p><div class=\"flex\"></div></section><div class=\"notice\">Educational demonstration only. No material, machine or industrial process has been experimentally validated.</div><section class=\"sim\"><h2>Explore one variable</h2><label for=\"variable\">sigma_a (MPa)</label><input id=\"variable\" type=\"range\" min=\"20\" max=\"150\" step=\"2\" value=\"75\" aria-describedby=\"readout\"><div class=\"flex\"><strong id=\"readout\"></strong></div><output id=\"answer\" for=\"variable\"></output><svg viewBox=\"0 0 545 225\" role=\"img\" aria-label=\"Graph of predicted response over slider range\"><line x1=\"36\" y1=\"15\" x2=\"36\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><line x1=\"36\" y1=\"192\" x2=\"510\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><g id=\"curve\"></g><text x=\"35\" y=\"213\" fill=\"#467181\" font-size=\"12\">20</text><text x=\"460\" y=\"213\" fill=\"#467181\" font-size=\"12\">150</text></svg><p class=\"muted\" id=\"ymax\"></p></section><section class=\"paper\"><h2>Equation and domain</h2><p>This intentionally simplified model demonstrates one physical relationship. Approximate fatigue safety-factor screen, only for positive mean stress and known material allowables. Assumptions: Se=180 MPa; mean stress=65 MPa; Sut=520 MPa. Other loading, geometry, fatigue, thermal effects and manufacturing scatter are not represented. Do not use as an industrial selection or safety approval.</p><p>Move the control toward both limits; compare the direction and curvature of the response. For a real design, obtain independent strength or life data, evaluate load cases and verify physical dimensions and units.</p><h2>Suggested analysis exercise</h2><p>Record three values of sigma_a (MPa) and their outputs. Calculate a finite-difference sensitivity and explain whether the response changes linearly. State one neglected effect that might make the actual measured response different.</p></section>",
    init: function(card) {
      try {
const calc = (x) => 1/(x/180+65/520);
const lo=20, hi=150;
const inp=card.querySelector("#" + 'variable'.replace(/^#/, ""));
const out=card.querySelector("#" + 'answer'.replace(/^#/, ""));
const chart=card.querySelector("#" + 'curve'.replace(/^#/, ""));
const xread=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const yl=card.querySelector("#" + 'ymax'.replace(/^#/, ""));
function draw(){
 const x=Number(inp.value),y=calc(x),vals=[];
 for(let j=0;j<=65;j++) vals.push(calc(lo+(hi-lo)*j/65));
 const ymin=Math.min(...vals),ymax=Math.max(...vals),span=Math.max(1e-12,ymax-ymin),fx=(xx)=>36+xx*470,fy=(v)=>188-(v-ymin)/span*145;
 const points=vals.map((v,j)=>fx(j/65).toFixed(2)+','+fy(v).toFixed(2)).join(' ');
 const markerX=fx((x-lo)/(hi-lo)),markerY=fy(y);
 chart.innerHTML='<polyline fill="none" stroke="#0b8593" stroke-width="3.4" points="'+points+'"/><circle cx="'+markerX.toFixed(2)+'" cy="'+markerY.toFixed(2)+'" r="7" fill="#d27424" stroke="white" stroke-width="2"/>';
 out.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' factor';
 xread.textContent=x.toLocaleString('en-US',{maximumFractionDigits:2})+' (sigma_a (MPa))';
 yl.textContent='Range '+ymin.toLocaleString('en-US',{maximumFractionDigits:3})+' to '+ymax.toLocaleString('en-US',{maximumFractionDigits:3})+' factor';
}
inp.addEventListener('input',draw); draw();
window.modelCalc=calc;
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 3,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 06 / 16</span><h3>Miner cycle damage index</h3><p>Two-bin linear damage accumulation. A damage index of one is not a guaranteed failure time.</p><div class=\"flex\"></div></section><div class=\"notice\">Educational demonstration only. No material, machine or industrial process has been experimentally validated.</div><section class=\"sim\"><h2>Explore one variable</h2><label for=\"variable\">n1 (thousand cycles)</label><input id=\"variable\" type=\"range\" min=\"0\" max=\"250\" step=\"5\" value=\"40\" aria-describedby=\"readout\"><div class=\"flex\"><strong id=\"readout\"></strong></div><output id=\"answer\" for=\"variable\"></output><svg viewBox=\"0 0 545 225\" role=\"img\" aria-label=\"Graph of predicted response over slider range\"><line x1=\"36\" y1=\"15\" x2=\"36\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><line x1=\"36\" y1=\"192\" x2=\"510\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><g id=\"curve\"></g><text x=\"35\" y=\"213\" fill=\"#467181\" font-size=\"12\">0</text><text x=\"460\" y=\"213\" fill=\"#467181\" font-size=\"12\">250</text></svg><p class=\"muted\" id=\"ymax\"></p></section><section class=\"paper\"><h2>Equation and domain</h2><p>This intentionally simplified model demonstrates one physical relationship. Two-bin linear damage accumulation. A damage index of one is not a guaranteed failure time. Assumptions: N1=300k cycles; n2=50k cycles; N2=500k cycles. Other loading, geometry, fatigue, thermal effects and manufacturing scatter are not represented. Do not use as an industrial selection or safety approval.</p><p>Move the control toward both limits; compare the direction and curvature of the response. For a real design, obtain independent strength or life data, evaluate load cases and verify physical dimensions and units.</p><h2>Suggested analysis exercise</h2><p>Record three values of n1 (thousand cycles) and their outputs. Calculate a finite-difference sensitivity and explain whether the response changes linearly. State one neglected effect that might make the actual measured response different.</p></section>",
    init: function(card) {
      try {
const calc = (x) => (x*1000)/300000+50000/500000;
const lo=0, hi=250;
const inp=card.querySelector("#" + 'variable'.replace(/^#/, ""));
const out=card.querySelector("#" + 'answer'.replace(/^#/, ""));
const chart=card.querySelector("#" + 'curve'.replace(/^#/, ""));
const xread=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const yl=card.querySelector("#" + 'ymax'.replace(/^#/, ""));
function draw(){
 const x=Number(inp.value),y=calc(x),vals=[];
 for(let j=0;j<=65;j++) vals.push(calc(lo+(hi-lo)*j/65));
 const ymin=Math.min(...vals),ymax=Math.max(...vals),span=Math.max(1e-12,ymax-ymin),fx=(xx)=>36+xx*470,fy=(v)=>188-(v-ymin)/span*145;
 const points=vals.map((v,j)=>fx(j/65).toFixed(2)+','+fy(v).toFixed(2)).join(' ');
 const markerX=fx((x-lo)/(hi-lo)),markerY=fy(y);
 chart.innerHTML='<polyline fill="none" stroke="#0b8593" stroke-width="3.4" points="'+points+'"/><circle cx="'+markerX.toFixed(2)+'" cy="'+markerY.toFixed(2)+'" r="7" fill="#d27424" stroke="white" stroke-width="2"/>';
 out.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' damage';
 xread.textContent=x.toLocaleString('en-US',{maximumFractionDigits:2})+' (n1 (thousand cycles))';
 yl.textContent='Range '+ymin.toLocaleString('en-US',{maximumFractionDigits:3})+' to '+ymax.toLocaleString('en-US',{maximumFractionDigits:3})+' damage';
}
inp.addEventListener('input',draw); draw();
window.modelCalc=calc;
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 4,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 07 / 16</span><h3>Approximate bolt preload</h3><p>Simplified torque\u2013tension relation; friction and embedment cause substantial scatter.</p><div class=\"flex\"></div></section><div class=\"notice\">Educational demonstration only. No material, machine or industrial process has been experimentally validated.</div><section class=\"sim\"><h2>Explore one variable</h2><label for=\"variable\">tightening torque (N\u00b7m)</label><input id=\"variable\" type=\"range\" min=\"20\" max=\"120\" step=\"2\" value=\"45\" aria-describedby=\"readout\"><div class=\"flex\"><strong id=\"readout\"></strong></div><output id=\"answer\" for=\"variable\"></output><svg viewBox=\"0 0 545 225\" role=\"img\" aria-label=\"Graph of predicted response over slider range\"><line x1=\"36\" y1=\"15\" x2=\"36\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><line x1=\"36\" y1=\"192\" x2=\"510\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><g id=\"curve\"></g><text x=\"35\" y=\"213\" fill=\"#467181\" font-size=\"12\">20</text><text x=\"460\" y=\"213\" fill=\"#467181\" font-size=\"12\">120</text></svg><p class=\"muted\" id=\"ymax\"></p></section><section class=\"paper\"><h2>Equation and domain</h2><p>This intentionally simplified model demonstrates one physical relationship. Simplified torque\u2013tension relation; friction and embedment cause substantial scatter. Assumptions: nut factor K=0.20; nominal diameter=10 mm. Other loading, geometry, fatigue, thermal effects and manufacturing scatter are not represented. Do not use as an industrial selection or safety approval.</p><p>Move the control toward both limits; compare the direction and curvature of the response. For a real design, obtain independent strength or life data, evaluate load cases and verify physical dimensions and units.</p><h2>Suggested analysis exercise</h2><p>Record three values of tightening torque (N\u00b7m) and their outputs. Calculate a finite-difference sensitivity and explain whether the response changes linearly. State one neglected effect that might make the actual measured response different.</p></section>",
    init: function(card) {
      try {
const calc = (x) => x/(0.20*0.010);
const lo=20, hi=120;
const inp=card.querySelector("#" + 'variable'.replace(/^#/, ""));
const out=card.querySelector("#" + 'answer'.replace(/^#/, ""));
const chart=card.querySelector("#" + 'curve'.replace(/^#/, ""));
const xread=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const yl=card.querySelector("#" + 'ymax'.replace(/^#/, ""));
function draw(){
 const x=Number(inp.value),y=calc(x),vals=[];
 for(let j=0;j<=65;j++) vals.push(calc(lo+(hi-lo)*j/65));
 const ymin=Math.min(...vals),ymax=Math.max(...vals),span=Math.max(1e-12,ymax-ymin),fx=(xx)=>36+xx*470,fy=(v)=>188-(v-ymin)/span*145;
 const points=vals.map((v,j)=>fx(j/65).toFixed(2)+','+fy(v).toFixed(2)).join(' ');
 const markerX=fx((x-lo)/(hi-lo)),markerY=fy(y);
 chart.innerHTML='<polyline fill="none" stroke="#0b8593" stroke-width="3.4" points="'+points+'"/><circle cx="'+markerX.toFixed(2)+'" cy="'+markerY.toFixed(2)+'" r="7" fill="#d27424" stroke="white" stroke-width="2"/>';
 out.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' N';
 xread.textContent=x.toLocaleString('en-US',{maximumFractionDigits:2})+' (tightening torque (N·m))';
 yl.textContent='Range '+ymin.toLocaleString('en-US',{maximumFractionDigits:3})+' to '+ymax.toLocaleString('en-US',{maximumFractionDigits:3})+' N';
}
inp.addEventListener('input',draw); draw();
window.modelCalc=calc;
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 4,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 08 / 16</span><h3>Joint remaining compression</h3><p>A simple linear clamped joint model before separation. Negative means the assumed contact is lost.</p><div class=\"flex\"></div></section><div class=\"notice\">Educational demonstration only. No material, machine or industrial process has been experimentally validated.</div><section class=\"sim\"><h2>Explore one variable</h2><label for=\"variable\">external separation load (N)</label><input id=\"variable\" type=\"range\" min=\"1000\" max=\"15000\" step=\"250\" value=\"4000\" aria-describedby=\"readout\"><div class=\"flex\"><strong id=\"readout\"></strong></div><output id=\"answer\" for=\"variable\"></output><svg viewBox=\"0 0 545 225\" role=\"img\" aria-label=\"Graph of predicted response over slider range\"><line x1=\"36\" y1=\"15\" x2=\"36\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><line x1=\"36\" y1=\"192\" x2=\"510\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><g id=\"curve\"></g><text x=\"35\" y=\"213\" fill=\"#467181\" font-size=\"12\">1000</text><text x=\"460\" y=\"213\" fill=\"#467181\" font-size=\"12\">15000</text></svg><p class=\"muted\" id=\"ymax\"></p></section><section class=\"paper\"><h2>Equation and domain</h2><p>This intentionally simplified model demonstrates one physical relationship. A simple linear clamped joint model before separation. Negative means the assumed contact is lost. Assumptions: Fi=10,000 N; external load fraction C=0.22. Other loading, geometry, fatigue, thermal effects and manufacturing scatter are not represented. Do not use as an industrial selection or safety approval.</p><p>Move the control toward both limits; compare the direction and curvature of the response. For a real design, obtain independent strength or life data, evaluate load cases and verify physical dimensions and units.</p><h2>Suggested analysis exercise</h2><p>Record three values of external separation load (N) and their outputs. Calculate a finite-difference sensitivity and explain whether the response changes linearly. State one neglected effect that might make the actual measured response different.</p></section>",
    init: function(card) {
      try {
const calc = (x) => 10000-(1-0.22)*x;
const lo=1000, hi=15000;
const inp=card.querySelector("#" + 'variable'.replace(/^#/, ""));
const out=card.querySelector("#" + 'answer'.replace(/^#/, ""));
const chart=card.querySelector("#" + 'curve'.replace(/^#/, ""));
const xread=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const yl=card.querySelector("#" + 'ymax'.replace(/^#/, ""));
function draw(){
 const x=Number(inp.value),y=calc(x),vals=[];
 for(let j=0;j<=65;j++) vals.push(calc(lo+(hi-lo)*j/65));
 const ymin=Math.min(...vals),ymax=Math.max(...vals),span=Math.max(1e-12,ymax-ymin),fx=(xx)=>36+xx*470,fy=(v)=>188-(v-ymin)/span*145;
 const points=vals.map((v,j)=>fx(j/65).toFixed(2)+','+fy(v).toFixed(2)).join(' ');
 const markerX=fx((x-lo)/(hi-lo)),markerY=fy(y);
 chart.innerHTML='<polyline fill="none" stroke="#0b8593" stroke-width="3.4" points="'+points+'"/><circle cx="'+markerX.toFixed(2)+'" cy="'+markerY.toFixed(2)+'" r="7" fill="#d27424" stroke="white" stroke-width="2"/>';
 out.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' N';
 xread.textContent=x.toLocaleString('en-US',{maximumFractionDigits:2})+' (external separation load (N))';
 yl.textContent='Range '+ymin.toLocaleString('en-US',{maximumFractionDigits:3})+' to '+ymax.toLocaleString('en-US',{maximumFractionDigits:3})+' N';
}
inp.addEventListener('input',draw); draw();
window.modelCalc=calc;
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  MODELS.push({
    idx: 9,
    unit: 5,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 09 / 16</span><h3>Bearing basic rating life</h3><p>Ball bearing L10 in million revolutions, based on equivalent dynamic load and rating.</p><div class=\"flex\"></div></section><div class=\"notice\">Educational demonstration only. No material, machine or industrial process has been experimentally validated.</div><section class=\"sim\"><h2>Explore one variable</h2><label for=\"variable\">P (N)</label><input id=\"variable\" type=\"range\" min=\"1000\" max=\"6000\" step=\"100\" value=\"3000\" aria-describedby=\"readout\"><div class=\"flex\"><strong id=\"readout\"></strong></div><output id=\"answer\" for=\"variable\"></output><svg viewBox=\"0 0 545 225\" role=\"img\" aria-label=\"Graph of predicted response over slider range\"><line x1=\"36\" y1=\"15\" x2=\"36\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><line x1=\"36\" y1=\"192\" x2=\"510\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><g id=\"curve\"></g><text x=\"35\" y=\"213\" fill=\"#467181\" font-size=\"12\">1000</text><text x=\"460\" y=\"213\" fill=\"#467181\" font-size=\"12\">6000</text></svg><p class=\"muted\" id=\"ymax\"></p></section><section class=\"paper\"><h2>Equation and domain</h2><p>This intentionally simplified model demonstrates one physical relationship. Ball bearing L10 in million revolutions, based on equivalent dynamic load and rating. Assumptions: C=15,000 N; p=3; clean ideal rating assumption. Other loading, geometry, fatigue, thermal effects and manufacturing scatter are not represented. Do not use as an industrial selection or safety approval.</p><p>Move the control toward both limits; compare the direction and curvature of the response. For a real design, obtain independent strength or life data, evaluate load cases and verify physical dimensions and units.</p><h2>Suggested analysis exercise</h2><p>Record three values of P (N) and their outputs. Calculate a finite-difference sensitivity and explain whether the response changes linearly. State one neglected effect that might make the actual measured response different.</p></section>",
    init: function(card) {
      try {
const calc = (x) => Math.pow(15000/x,3);
const lo=1000, hi=6000;
const inp=card.querySelector("#" + 'variable'.replace(/^#/, ""));
const out=card.querySelector("#" + 'answer'.replace(/^#/, ""));
const chart=card.querySelector("#" + 'curve'.replace(/^#/, ""));
const xread=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const yl=card.querySelector("#" + 'ymax'.replace(/^#/, ""));
function draw(){
 const x=Number(inp.value),y=calc(x),vals=[];
 for(let j=0;j<=65;j++) vals.push(calc(lo+(hi-lo)*j/65));
 const ymin=Math.min(...vals),ymax=Math.max(...vals),span=Math.max(1e-12,ymax-ymin),fx=(xx)=>36+xx*470,fy=(v)=>188-(v-ymin)/span*145;
 const points=vals.map((v,j)=>fx(j/65).toFixed(2)+','+fy(v).toFixed(2)).join(' ');
 const markerX=fx((x-lo)/(hi-lo)),markerY=fy(y);
 chart.innerHTML='<polyline fill="none" stroke="#0b8593" stroke-width="3.4" points="'+points+'"/><circle cx="'+markerX.toFixed(2)+'" cy="'+markerY.toFixed(2)+'" r="7" fill="#d27424" stroke="white" stroke-width="2"/>';
 out.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' million rev';
 xread.textContent=x.toLocaleString('en-US',{maximumFractionDigits:2})+' (P (N))';
 yl.textContent='Range '+ymin.toLocaleString('en-US',{maximumFractionDigits:3})+' to '+ymax.toLocaleString('en-US',{maximumFractionDigits:3})+' million rev';
}
inp.addEventListener('input',draw); draw();
window.modelCalc=calc;
      } catch (err) {
        console.warn('Sim init error in model 9:', err);
      }
    }
  });

  MODELS.push({
    idx: 10,
    unit: 5,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 10 / 16</span><h3>Plain bearing PV</h3><p>Pressure \u00d7 sliding speed, a first-pass tribology screen, not an approval criterion.</p><div class=\"flex\"></div></section><div class=\"notice\">Educational demonstration only. No material, machine or industrial process has been experimentally validated.</div><section class=\"sim\"><h2>Explore one variable</h2><label for=\"variable\">radial force (N)</label><input id=\"variable\" type=\"range\" min=\"100\" max=\"1400\" step=\"25\" value=\"600\" aria-describedby=\"readout\"><div class=\"flex\"><strong id=\"readout\"></strong></div><output id=\"answer\" for=\"variable\"></output><svg viewBox=\"0 0 545 225\" role=\"img\" aria-label=\"Graph of predicted response over slider range\"><line x1=\"36\" y1=\"15\" x2=\"36\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><line x1=\"36\" y1=\"192\" x2=\"510\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><g id=\"curve\"></g><text x=\"35\" y=\"213\" fill=\"#467181\" font-size=\"12\">100</text><text x=\"460\" y=\"213\" fill=\"#467181\" font-size=\"12\">1400</text></svg><p class=\"muted\" id=\"ymax\"></p></section><section class=\"paper\"><h2>Equation and domain</h2><p>This intentionally simplified model demonstrates one physical relationship. Pressure \u00d7 sliding speed, a first-pass tribology screen, not an approval criterion. Assumptions: d=25 mm; L=40 mm; n=600 rpm. Other loading, geometry, fatigue, thermal effects and manufacturing scatter are not represented. Do not use as an industrial selection or safety approval.</p><p>Move the control toward both limits; compare the direction and curvature of the response. For a real design, obtain independent strength or life data, evaluate load cases and verify physical dimensions and units.</p><h2>Suggested analysis exercise</h2><p>Record three values of radial force (N) and their outputs. Calculate a finite-difference sensitivity and explain whether the response changes linearly. State one neglected effect that might make the actual measured response different.</p></section>",
    init: function(card) {
      try {
const calc = (x) => (x/(0.025*0.04))*(Math.PI*0.025*600/60)/1e6;
const lo=100, hi=1400;
const inp=card.querySelector("#" + 'variable'.replace(/^#/, ""));
const out=card.querySelector("#" + 'answer'.replace(/^#/, ""));
const chart=card.querySelector("#" + 'curve'.replace(/^#/, ""));
const xread=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const yl=card.querySelector("#" + 'ymax'.replace(/^#/, ""));
function draw(){
 const x=Number(inp.value),y=calc(x),vals=[];
 for(let j=0;j<=65;j++) vals.push(calc(lo+(hi-lo)*j/65));
 const ymin=Math.min(...vals),ymax=Math.max(...vals),span=Math.max(1e-12,ymax-ymin),fx=(xx)=>36+xx*470,fy=(v)=>188-(v-ymin)/span*145;
 const points=vals.map((v,j)=>fx(j/65).toFixed(2)+','+fy(v).toFixed(2)).join(' ');
 const markerX=fx((x-lo)/(hi-lo)),markerY=fy(y);
 chart.innerHTML='<polyline fill="none" stroke="#0b8593" stroke-width="3.4" points="'+points+'"/><circle cx="'+markerX.toFixed(2)+'" cy="'+markerY.toFixed(2)+'" r="7" fill="#d27424" stroke="white" stroke-width="2"/>';
 out.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' MPa·m/s';
 xread.textContent=x.toLocaleString('en-US',{maximumFractionDigits:2})+' (radial force (N))';
 yl.textContent='Range '+ymin.toLocaleString('en-US',{maximumFractionDigits:3})+' to '+ymax.toLocaleString('en-US',{maximumFractionDigits:3})+' MPa·m/s';
}
inp.addEventListener('input',draw); draw();
window.modelCalc=calc;
      } catch (err) {
        console.warn('Sim init error in model 10:', err);
      }
    }
  });

  MODELS.push({
    idx: 11,
    unit: 6,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 11 / 16</span><h3>Gear pitch-circle force</h3><p>Tangential force required to transmit torque at the stated pitch diameter.</p><div class=\"flex\"></div></section><div class=\"notice\">Educational demonstration only. No material, machine or industrial process has been experimentally validated.</div><section class=\"sim\"><h2>Explore one variable</h2><label for=\"variable\">T (N\u00b7m)</label><input id=\"variable\" type=\"range\" min=\"10\" max=\"240\" step=\"5\" value=\"100\" aria-describedby=\"readout\"><div class=\"flex\"><strong id=\"readout\"></strong></div><output id=\"answer\" for=\"variable\"></output><svg viewBox=\"0 0 545 225\" role=\"img\" aria-label=\"Graph of predicted response over slider range\"><line x1=\"36\" y1=\"15\" x2=\"36\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><line x1=\"36\" y1=\"192\" x2=\"510\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><g id=\"curve\"></g><text x=\"35\" y=\"213\" fill=\"#467181\" font-size=\"12\">10</text><text x=\"460\" y=\"213\" fill=\"#467181\" font-size=\"12\">240</text></svg><p class=\"muted\" id=\"ymax\"></p></section><section class=\"paper\"><h2>Equation and domain</h2><p>This intentionally simplified model demonstrates one physical relationship. Tangential force required to transmit torque at the stated pitch diameter. Assumptions: pitch diameter=0.12 m; bearing forces omitted. Other loading, geometry, fatigue, thermal effects and manufacturing scatter are not represented. Do not use as an industrial selection or safety approval.</p><p>Move the control toward both limits; compare the direction and curvature of the response. For a real design, obtain independent strength or life data, evaluate load cases and verify physical dimensions and units.</p><h2>Suggested analysis exercise</h2><p>Record three values of T (N\u00b7m) and their outputs. Calculate a finite-difference sensitivity and explain whether the response changes linearly. State one neglected effect that might make the actual measured response different.</p></section>",
    init: function(card) {
      try {
const calc = (x) => 2*x/0.12;
const lo=10, hi=240;
const inp=card.querySelector("#" + 'variable'.replace(/^#/, ""));
const out=card.querySelector("#" + 'answer'.replace(/^#/, ""));
const chart=card.querySelector("#" + 'curve'.replace(/^#/, ""));
const xread=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const yl=card.querySelector("#" + 'ymax'.replace(/^#/, ""));
function draw(){
 const x=Number(inp.value),y=calc(x),vals=[];
 for(let j=0;j<=65;j++) vals.push(calc(lo+(hi-lo)*j/65));
 const ymin=Math.min(...vals),ymax=Math.max(...vals),span=Math.max(1e-12,ymax-ymin),fx=(xx)=>36+xx*470,fy=(v)=>188-(v-ymin)/span*145;
 const points=vals.map((v,j)=>fx(j/65).toFixed(2)+','+fy(v).toFixed(2)).join(' ');
 const markerX=fx((x-lo)/(hi-lo)),markerY=fy(y);
 chart.innerHTML='<polyline fill="none" stroke="#0b8593" stroke-width="3.4" points="'+points+'"/><circle cx="'+markerX.toFixed(2)+'" cy="'+markerY.toFixed(2)+'" r="7" fill="#d27424" stroke="white" stroke-width="2"/>';
 out.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' N';
 xread.textContent=x.toLocaleString('en-US',{maximumFractionDigits:2})+' (T (N·m))';
 yl.textContent='Range '+ymin.toLocaleString('en-US',{maximumFractionDigits:3})+' to '+ymax.toLocaleString('en-US',{maximumFractionDigits:3})+' N';
}
inp.addEventListener('input',draw); draw();
window.modelCalc=calc;
      } catch (err) {
        console.warn('Sim init error in model 11:', err);
      }
    }
  });

  MODELS.push({
    idx: 12,
    unit: 6,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 12 / 16</span><h3>Ideal pair output speed</h3><p>No-slip ideal involute tooth-count speed ratio. Does not predict losses or tooth stresses.</p><div class=\"flex\"></div></section><div class=\"notice\">Educational demonstration only. No material, machine or industrial process has been experimentally validated.</div><section class=\"sim\"><h2>Explore one variable</h2><label for=\"variable\">driven tooth count</label><input id=\"variable\" type=\"range\" min=\"24\" max=\"100\" step=\"2\" value=\"60\" aria-describedby=\"readout\"><div class=\"flex\"><strong id=\"readout\"></strong></div><output id=\"answer\" for=\"variable\"></output><svg viewBox=\"0 0 545 225\" role=\"img\" aria-label=\"Graph of predicted response over slider range\"><line x1=\"36\" y1=\"15\" x2=\"36\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><line x1=\"36\" y1=\"192\" x2=\"510\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><g id=\"curve\"></g><text x=\"35\" y=\"213\" fill=\"#467181\" font-size=\"12\">24</text><text x=\"460\" y=\"213\" fill=\"#467181\" font-size=\"12\">100</text></svg><p class=\"muted\" id=\"ymax\"></p></section><section class=\"paper\"><h2>Equation and domain</h2><p>This intentionally simplified model demonstrates one physical relationship. No-slip ideal involute tooth-count speed ratio. Does not predict losses or tooth stresses. Assumptions: input=1200 rpm; driver=20 teeth. Other loading, geometry, fatigue, thermal effects and manufacturing scatter are not represented. Do not use as an industrial selection or safety approval.</p><p>Move the control toward both limits; compare the direction and curvature of the response. For a real design, obtain independent strength or life data, evaluate load cases and verify physical dimensions and units.</p><h2>Suggested analysis exercise</h2><p>Record three values of driven tooth count and their outputs. Calculate a finite-difference sensitivity and explain whether the response changes linearly. State one neglected effect that might make the actual measured response different.</p></section>",
    init: function(card) {
      try {
const calc = (x) => 1200*20/x;
const lo=24, hi=100;
const inp=card.querySelector("#" + 'variable'.replace(/^#/, ""));
const out=card.querySelector("#" + 'answer'.replace(/^#/, ""));
const chart=card.querySelector("#" + 'curve'.replace(/^#/, ""));
const xread=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const yl=card.querySelector("#" + 'ymax'.replace(/^#/, ""));
function draw(){
 const x=Number(inp.value),y=calc(x),vals=[];
 for(let j=0;j<=65;j++) vals.push(calc(lo+(hi-lo)*j/65));
 const ymin=Math.min(...vals),ymax=Math.max(...vals),span=Math.max(1e-12,ymax-ymin),fx=(xx)=>36+xx*470,fy=(v)=>188-(v-ymin)/span*145;
 const points=vals.map((v,j)=>fx(j/65).toFixed(2)+','+fy(v).toFixed(2)).join(' ');
 const markerX=fx((x-lo)/(hi-lo)),markerY=fy(y);
 chart.innerHTML='<polyline fill="none" stroke="#0b8593" stroke-width="3.4" points="'+points+'"/><circle cx="'+markerX.toFixed(2)+'" cy="'+markerY.toFixed(2)+'" r="7" fill="#d27424" stroke="white" stroke-width="2"/>';
 out.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' rpm';
 xread.textContent=x.toLocaleString('en-US',{maximumFractionDigits:2})+' (driven tooth count)';
 yl.textContent='Range '+ymin.toLocaleString('en-US',{maximumFractionDigits:3})+' to '+ymax.toLocaleString('en-US',{maximumFractionDigits:3})+' rpm';
}
inp.addEventListener('input',draw); draw();
window.modelCalc=calc;
      } catch (err) {
        console.warn('Sim init error in model 12:', err);
      }
    }
  });

  MODELS.push({
    idx: 13,
    unit: 7,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 13 / 16</span><h3>Capstan belt tension ratio</h3><p>Euler\u2013Eytelwein relation for an ideal flexible belt under limiting friction.</p><div class=\"flex\"></div></section><div class=\"notice\">Educational demonstration only. No material, machine or industrial process has been experimentally validated.</div><section class=\"sim\"><h2>Explore one variable</h2><label for=\"variable\">mu</label><input id=\"variable\" type=\"range\" min=\"0.1\" max=\"0.5\" step=\"0.01\" value=\"0.3\" aria-describedby=\"readout\"><div class=\"flex\"><strong id=\"readout\"></strong></div><output id=\"answer\" for=\"variable\"></output><svg viewBox=\"0 0 545 225\" role=\"img\" aria-label=\"Graph of predicted response over slider range\"><line x1=\"36\" y1=\"15\" x2=\"36\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><line x1=\"36\" y1=\"192\" x2=\"510\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><g id=\"curve\"></g><text x=\"35\" y=\"213\" fill=\"#467181\" font-size=\"12\">0.1</text><text x=\"460\" y=\"213\" fill=\"#467181\" font-size=\"12\">0.5</text></svg><p class=\"muted\" id=\"ymax\"></p></section><section class=\"paper\"><h2>Equation and domain</h2><p>This intentionally simplified model demonstrates one physical relationship. Euler\u2013Eytelwein relation for an ideal flexible belt under limiting friction. Assumptions: wrap=2.9 rad; friction assumed constant. Other loading, geometry, fatigue, thermal effects and manufacturing scatter are not represented. Do not use as an industrial selection or safety approval.</p><p>Move the control toward both limits; compare the direction and curvature of the response. For a real design, obtain independent strength or life data, evaluate load cases and verify physical dimensions and units.</p><h2>Suggested analysis exercise</h2><p>Record three values of mu and their outputs. Calculate a finite-difference sensitivity and explain whether the response changes linearly. State one neglected effect that might make the actual measured response different.</p></section>",
    init: function(card) {
      try {
const calc = (x) => Math.exp(x*2.9);
const lo=0.1, hi=0.5;
const inp=card.querySelector("#" + 'variable'.replace(/^#/, ""));
const out=card.querySelector("#" + 'answer'.replace(/^#/, ""));
const chart=card.querySelector("#" + 'curve'.replace(/^#/, ""));
const xread=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const yl=card.querySelector("#" + 'ymax'.replace(/^#/, ""));
function draw(){
 const x=Number(inp.value),y=calc(x),vals=[];
 for(let j=0;j<=65;j++) vals.push(calc(lo+(hi-lo)*j/65));
 const ymin=Math.min(...vals),ymax=Math.max(...vals),span=Math.max(1e-12,ymax-ymin),fx=(xx)=>36+xx*470,fy=(v)=>188-(v-ymin)/span*145;
 const points=vals.map((v,j)=>fx(j/65).toFixed(2)+','+fy(v).toFixed(2)).join(' ');
 const markerX=fx((x-lo)/(hi-lo)),markerY=fy(y);
 chart.innerHTML='<polyline fill="none" stroke="#0b8593" stroke-width="3.4" points="'+points+'"/><circle cx="'+markerX.toFixed(2)+'" cy="'+markerY.toFixed(2)+'" r="7" fill="#d27424" stroke="white" stroke-width="2"/>';
 out.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' ratio';
 xread.textContent=x.toLocaleString('en-US',{maximumFractionDigits:2})+' (mu)';
 yl.textContent='Range '+ymin.toLocaleString('en-US',{maximumFractionDigits:3})+' to '+ymax.toLocaleString('en-US',{maximumFractionDigits:3})+' ratio';
}
inp.addEventListener('input',draw); draw();
window.modelCalc=calc;
      } catch (err) {
        console.warn('Sim init error in model 13:', err);
      }
    }
  });

  MODELS.push({
    idx: 14,
    unit: 7,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 14 / 16</span><h3>Spring elastic stiffness</h3><p>Nominal helical compression spring stiffness in N/mm.</p><div class=\"flex\"></div></section><div class=\"notice\">Educational demonstration only. No material, machine or industrial process has been experimentally validated.</div><section class=\"sim\"><h2>Explore one variable</h2><label for=\"variable\">active coils</label><input id=\"variable\" type=\"range\" min=\"4\" max=\"14\" step=\"1\" value=\"8\" aria-describedby=\"readout\"><div class=\"flex\"><strong id=\"readout\"></strong></div><output id=\"answer\" for=\"variable\"></output><svg viewBox=\"0 0 545 225\" role=\"img\" aria-label=\"Graph of predicted response over slider range\"><line x1=\"36\" y1=\"15\" x2=\"36\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><line x1=\"36\" y1=\"192\" x2=\"510\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><g id=\"curve\"></g><text x=\"35\" y=\"213\" fill=\"#467181\" font-size=\"12\">4</text><text x=\"460\" y=\"213\" fill=\"#467181\" font-size=\"12\">14</text></svg><p class=\"muted\" id=\"ymax\"></p></section><section class=\"paper\"><h2>Equation and domain</h2><p>This intentionally simplified model demonstrates one physical relationship. Nominal helical compression spring stiffness in N/mm. Assumptions: G=79,000 N/mm\u00b2; wire=3 mm; mean coil=22 mm. Other loading, geometry, fatigue, thermal effects and manufacturing scatter are not represented. Do not use as an industrial selection or safety approval.</p><p>Move the control toward both limits; compare the direction and curvature of the response. For a real design, obtain independent strength or life data, evaluate load cases and verify physical dimensions and units.</p><h2>Suggested analysis exercise</h2><p>Record three values of active coils and their outputs. Calculate a finite-difference sensitivity and explain whether the response changes linearly. State one neglected effect that might make the actual measured response different.</p></section>",
    init: function(card) {
      try {
const calc = (x) => 79000*Math.pow(3,4)/(8*Math.pow(22,3)*x);
const lo=4, hi=14;
const inp=card.querySelector("#" + 'variable'.replace(/^#/, ""));
const out=card.querySelector("#" + 'answer'.replace(/^#/, ""));
const chart=card.querySelector("#" + 'curve'.replace(/^#/, ""));
const xread=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const yl=card.querySelector("#" + 'ymax'.replace(/^#/, ""));
function draw(){
 const x=Number(inp.value),y=calc(x),vals=[];
 for(let j=0;j<=65;j++) vals.push(calc(lo+(hi-lo)*j/65));
 const ymin=Math.min(...vals),ymax=Math.max(...vals),span=Math.max(1e-12,ymax-ymin),fx=(xx)=>36+xx*470,fy=(v)=>188-(v-ymin)/span*145;
 const points=vals.map((v,j)=>fx(j/65).toFixed(2)+','+fy(v).toFixed(2)).join(' ');
 const markerX=fx((x-lo)/(hi-lo)),markerY=fy(y);
 chart.innerHTML='<polyline fill="none" stroke="#0b8593" stroke-width="3.4" points="'+points+'"/><circle cx="'+markerX.toFixed(2)+'" cy="'+markerY.toFixed(2)+'" r="7" fill="#d27424" stroke="white" stroke-width="2"/>';
 out.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' N/mm';
 xread.textContent=x.toLocaleString('en-US',{maximumFractionDigits:2})+' (active coils)';
 yl.textContent='Range '+ymin.toLocaleString('en-US',{maximumFractionDigits:3})+' to '+ymax.toLocaleString('en-US',{maximumFractionDigits:3})+' N/mm';
}
inp.addEventListener('input',draw); draw();
window.modelCalc=calc;
      } catch (err) {
        console.warn('Sim init error in model 14:', err);
      }
    }
  });

  MODELS.push({
    idx: 15,
    unit: 8,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 15 / 16</span><h3>Flywheel stored energy</h3><p>Rotational kinetic energy. Overspeed hazards increase quadratically with speed.</p><div class=\"flex\"></div></section><div class=\"notice\">Educational demonstration only. No material, machine or industrial process has been experimentally validated.</div><section class=\"sim\"><h2>Explore one variable</h2><label for=\"variable\">omega (rad/s)</label><input id=\"variable\" type=\"range\" min=\"10\" max=\"120\" step=\"2\" value=\"50\" aria-describedby=\"readout\"><div class=\"flex\"><strong id=\"readout\"></strong></div><output id=\"answer\" for=\"variable\"></output><svg viewBox=\"0 0 545 225\" role=\"img\" aria-label=\"Graph of predicted response over slider range\"><line x1=\"36\" y1=\"15\" x2=\"36\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><line x1=\"36\" y1=\"192\" x2=\"510\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><g id=\"curve\"></g><text x=\"35\" y=\"213\" fill=\"#467181\" font-size=\"12\">10</text><text x=\"460\" y=\"213\" fill=\"#467181\" font-size=\"12\">120</text></svg><p class=\"muted\" id=\"ymax\"></p></section><section class=\"paper\"><h2>Equation and domain</h2><p>This intentionally simplified model demonstrates one physical relationship. Rotational kinetic energy. Overspeed hazards increase quadratically with speed. Assumptions: mass moment of inertia J=0.8 kg\u00b7m\u00b2. Other loading, geometry, fatigue, thermal effects and manufacturing scatter are not represented. Do not use as an industrial selection or safety approval.</p><p>Move the control toward both limits; compare the direction and curvature of the response. For a real design, obtain independent strength or life data, evaluate load cases and verify physical dimensions and units.</p><h2>Suggested analysis exercise</h2><p>Record three values of omega (rad/s) and their outputs. Calculate a finite-difference sensitivity and explain whether the response changes linearly. State one neglected effect that might make the actual measured response different.</p></section>",
    init: function(card) {
      try {
const calc = (x) => 0.5*0.8*x*x;
const lo=10, hi=120;
const inp=card.querySelector("#" + 'variable'.replace(/^#/, ""));
const out=card.querySelector("#" + 'answer'.replace(/^#/, ""));
const chart=card.querySelector("#" + 'curve'.replace(/^#/, ""));
const xread=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const yl=card.querySelector("#" + 'ymax'.replace(/^#/, ""));
function draw(){
 const x=Number(inp.value),y=calc(x),vals=[];
 for(let j=0;j<=65;j++) vals.push(calc(lo+(hi-lo)*j/65));
 const ymin=Math.min(...vals),ymax=Math.max(...vals),span=Math.max(1e-12,ymax-ymin),fx=(xx)=>36+xx*470,fy=(v)=>188-(v-ymin)/span*145;
 const points=vals.map((v,j)=>fx(j/65).toFixed(2)+','+fy(v).toFixed(2)).join(' ');
 const markerX=fx((x-lo)/(hi-lo)),markerY=fy(y);
 chart.innerHTML='<polyline fill="none" stroke="#0b8593" stroke-width="3.4" points="'+points+'"/><circle cx="'+markerX.toFixed(2)+'" cy="'+markerY.toFixed(2)+'" r="7" fill="#d27424" stroke="white" stroke-width="2"/>';
 out.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' J';
 xread.textContent=x.toLocaleString('en-US',{maximumFractionDigits:2})+' (omega (rad/s))';
 yl.textContent='Range '+ymin.toLocaleString('en-US',{maximumFractionDigits:3})+' to '+ymax.toLocaleString('en-US',{maximumFractionDigits:3})+' J';
}
inp.addEventListener('input',draw); draw();
window.modelCalc=calc;
      } catch (err) {
        console.warn('Sim init error in model 15:', err);
      }
    }
  });

  MODELS.push({
    idx: 16,
    unit: 8,
    html: "<section class=\"hero\"><span class=\"tag\">INTERACTIVE MODEL 16 / 16</span><h3>Beam stiffness and diameter</h3><p>Simply supported elastic beam midpoint deflection with central point load.</p><div class=\"flex\"></div></section><div class=\"notice\">Educational demonstration only. No material, machine or industrial process has been experimentally validated.</div><section class=\"sim\"><h2>Explore one variable</h2><label for=\"variable\">d (mm)</label><input id=\"variable\" type=\"range\" min=\"10\" max=\"40\" step=\"1\" value=\"24\" aria-describedby=\"readout\"><div class=\"flex\"><strong id=\"readout\"></strong></div><output id=\"answer\" for=\"variable\"></output><svg viewBox=\"0 0 545 225\" role=\"img\" aria-label=\"Graph of predicted response over slider range\"><line x1=\"36\" y1=\"15\" x2=\"36\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><line x1=\"36\" y1=\"192\" x2=\"510\" y2=\"192\" stroke=\"#8ba4b4\" stroke-width=\"1.5\"/><g id=\"curve\"></g><text x=\"35\" y=\"213\" fill=\"#467181\" font-size=\"12\">10</text><text x=\"460\" y=\"213\" fill=\"#467181\" font-size=\"12\">40</text></svg><p class=\"muted\" id=\"ymax\"></p></section><section class=\"paper\"><h2>Equation and domain</h2><p>This intentionally simplified model demonstrates one physical relationship. Simply supported elastic beam midpoint deflection with central point load. Assumptions: F=400 N; L=0.5 m; E=210 GPa; ideal supports. Other loading, geometry, fatigue, thermal effects and manufacturing scatter are not represented. Do not use as an industrial selection or safety approval.</p><p>Move the control toward both limits; compare the direction and curvature of the response. For a real design, obtain independent strength or life data, evaluate load cases and verify physical dimensions and units.</p><h2>Suggested analysis exercise</h2><p>Record three values of d (mm) and their outputs. Calculate a finite-difference sensitivity and explain whether the response changes linearly. State one neglected effect that might make the actual measured response different.</p></section>",
    init: function(card) {
      try {
const calc = (x) => (400*Math.pow(0.5,3)/(48*210e9*(Math.PI*Math.pow(x/1000,4)/64)))*1000;
const lo=10, hi=40;
const inp=card.querySelector("#" + 'variable'.replace(/^#/, ""));
const out=card.querySelector("#" + 'answer'.replace(/^#/, ""));
const chart=card.querySelector("#" + 'curve'.replace(/^#/, ""));
const xread=card.querySelector("#" + 'readout'.replace(/^#/, ""));
const yl=card.querySelector("#" + 'ymax'.replace(/^#/, ""));
function draw(){
 const x=Number(inp.value),y=calc(x),vals=[];
 for(let j=0;j<=65;j++) vals.push(calc(lo+(hi-lo)*j/65));
 const ymin=Math.min(...vals),ymax=Math.max(...vals),span=Math.max(1e-12,ymax-ymin),fx=(xx)=>36+xx*470,fy=(v)=>188-(v-ymin)/span*145;
 const points=vals.map((v,j)=>fx(j/65).toFixed(2)+','+fy(v).toFixed(2)).join(' ');
 const markerX=fx((x-lo)/(hi-lo)),markerY=fy(y);
 chart.innerHTML='<polyline fill="none" stroke="#0b8593" stroke-width="3.4" points="'+points+'"/><circle cx="'+markerX.toFixed(2)+'" cy="'+markerY.toFixed(2)+'" r="7" fill="#d27424" stroke="white" stroke-width="2"/>';
 out.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' mm';
 xread.textContent=x.toLocaleString('en-US',{maximumFractionDigits:2})+' (d (mm))';
 yl.textContent='Range '+ymin.toLocaleString('en-US',{maximumFractionDigits:3})+' to '+ymax.toLocaleString('en-US',{maximumFractionDigits:3})+' mm';
}
inp.addEventListener('input',draw); draw();
window.modelCalc=calc;
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
