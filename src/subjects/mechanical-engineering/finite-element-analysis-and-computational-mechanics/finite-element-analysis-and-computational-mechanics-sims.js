/* finite-element-analysis-and-computational-mechanics Interactive Simulation Suite */
(function(window) {
  'use strict';

  var OPENSTEM_SIM_MODELS = [];

  OPENSTEM_SIM_MODELS.push({
    idx: 1,
    unit: 1,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 18</div><h3>Axial element stiffness</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Educational status:</strong> Editorial draft; not independently peer reviewed or validated for design approval. A simple calculator is not a general finite element solver.</p><article class=\"model\"><h2>Interactive analytical model 01</h2><p><strong>Benchmark relation:</strong> <code>k=EA/L</code></p><div class=\"inputs\"><label for=\"E\">Young modulus (GPa)<input id=\"E\" type=\"number\" min=\"1\" max=\"300\" value=\"200\" step=\"any\"></label><label for=\"A\">Cross section (mm\u00b2)<input id=\"A\" type=\"number\" min=\"5\" max=\"1500\" value=\"120\" step=\"any\"></label><label for=\"L\">Element length (m)<input id=\"L\" type=\"number\" min=\"0.05\" max=\"5\" value=\"0.7\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change a parameter to recalculate.</p></div><svg class=\"plot\" id=\"plot\" viewBox=\"0 0 700 220\" role=\"img\" aria-label=\"Output sensitivity to first parameter\"></svg><p class=\"small\">Assumes linear elastic constant axial section. No FE solver is run in this calculator; use the assembled bar lab for the discretized example.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 Model assumptions and all safety limits must be checked.</p>",
    init: function(card) {
      try {
// OpenSTEM Book 18, benchmark model 01: Axial element stiffness
function compute(E,A,L){return E*1e9*A*1e-6/L;}
function update(){
 const E=Number(card.querySelector("#" + "E".replace(/^#/, "")).value);
 const A=Number(card.querySelector("#" + "A".replace(/^#/, "")).value);
 const L=Number(card.querySelector("#" + "L".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")),details=card.querySelector("#" + 'details'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(!(Number.isFinite(E) && E>=1 && E<=300 && Number.isFinite(A) && A>=5 && A<=1500 && Number.isFinite(L) && L>=0.05 && L<=5)){metric.textContent='Invalid inputs';details.textContent='Use the bounded input ranges.';plot.textContent='';return;}
 const y=compute(E,A,L);
 if(!Number.isFinite(y)||Math.abs(y)>1e15){metric.textContent='Undefined';details.textContent='Expression outside its supported domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:6})+' N/m';details.textContent="Assumes linear elastic constant axial section.";
 const lo=Math.max(1,E===0?-1:E*0.8),hi=Math.min(300,E===0?1:E*1.2);
 const xLo=Math.min(lo,hi-1e-9),xHi=Math.max(hi,lo+1e-9); const pts=[];
 for(let j=0;j<=35;j++){const x=xLo+(xHi-xLo)*j/35;const out=compute(x,A,L);if(Number.isFinite(out))pts.push([x,out]);}
 if(pts.length<2){plot.textContent='';return;}
 const min=Math.min(...pts.map(p=>p[1])),max=Math.max(...pts.map(p=>p[1])),scale=Math.max(1e-9,max-min);
 const poly=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${182-135*(p[1]-min)/scale}`).join(' ');
 plot.innerHTML=`<line x1="45" y1="186" x2="647" y2="186" stroke="#94a8b2"/><line x1="45" y1="18" x2="45" y2="186" stroke="#94a8b2"/><polyline points="${poly}" stroke="#126e7a" stroke-width="3" fill="none"/><text x="50" y="16" font-size="13" fill="#315667">Input sensitivity (first parameter)</text><text x="50" y="209" font-size="12" fill="#315667">${xLo.toPrecision(3)}</text><text x="585" y="209" font-size="12" fill="#315667">${xHi.toPrecision(3)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));update();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 2,
    unit: 1,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 18</div><h3>Axial two-element stiffness in series</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Educational status:</strong> Editorial draft; not independently peer reviewed or validated for design approval. A simple calculator is not a general finite element solver.</p><article class=\"model\"><h2>Interactive analytical model 02</h2><p><strong>Benchmark relation:</strong> <code>1/k_eq=L1/(EA1)+L2/(EA2)</code></p><div class=\"inputs\"><label for=\"E\">Young modulus (GPa)<input id=\"E\" type=\"number\" min=\"1\" max=\"300\" value=\"200\" step=\"any\"></label><label for=\"A1\">Element 1 area (mm\u00b2)<input id=\"A1\" type=\"number\" min=\"5\" max=\"1000\" value=\"200\" step=\"any\"></label><label for=\"A2\">Element 2 area (mm\u00b2)<input id=\"A2\" type=\"number\" min=\"5\" max=\"1000\" value=\"300\" step=\"any\"></label><label for=\"L1\">Element 1 length (m)<input id=\"L1\" type=\"number\" min=\"0.01\" max=\"5\" value=\"0.8\" step=\"any\"></label><label for=\"L2\">Element 2 length (m)<input id=\"L2\" type=\"number\" min=\"0.01\" max=\"5\" value=\"0.6\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change a parameter to recalculate.</p></div><svg class=\"plot\" id=\"plot\" viewBox=\"0 0 700 220\" role=\"img\" aria-label=\"Output sensitivity to first parameter\"></svg><p class=\"small\">Axial elements assumed in series, same material and force. No FE solver is run in this calculator; use the assembled bar lab for the discretized example.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 Model assumptions and all safety limits must be checked.</p>",
    init: function(card) {
      try {
// OpenSTEM Book 18, benchmark model 02: Axial two-element stiffness in series
function compute(E,A1,A2,L1,L2){return 1/(L1/(E*1e9*A1*1e-6)+L2/(E*1e9*A2*1e-6));}
function update(){
 const E=Number(card.querySelector("#" + "E".replace(/^#/, "")).value);
 const A1=Number(card.querySelector("#" + "A1".replace(/^#/, "")).value);
 const A2=Number(card.querySelector("#" + "A2".replace(/^#/, "")).value);
 const L1=Number(card.querySelector("#" + "L1".replace(/^#/, "")).value);
 const L2=Number(card.querySelector("#" + "L2".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")),details=card.querySelector("#" + 'details'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(!(Number.isFinite(E) && E>=1 && E<=300 && Number.isFinite(A1) && A1>=5 && A1<=1000 && Number.isFinite(A2) && A2>=5 && A2<=1000 && Number.isFinite(L1) && L1>=0.01 && L1<=5 && Number.isFinite(L2) && L2>=0.01 && L2<=5)){metric.textContent='Invalid inputs';details.textContent='Use the bounded input ranges.';plot.textContent='';return;}
 const y=compute(E,A1,A2,L1,L2);
 if(!Number.isFinite(y)||Math.abs(y)>1e15){metric.textContent='Undefined';details.textContent='Expression outside its supported domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:6})+' N/m';details.textContent="Axial elements assumed in series, same material and force.";
 const lo=Math.max(1,E===0?-1:E*0.8),hi=Math.min(300,E===0?1:E*1.2);
 const xLo=Math.min(lo,hi-1e-9),xHi=Math.max(hi,lo+1e-9); const pts=[];
 for(let j=0;j<=35;j++){const x=xLo+(xHi-xLo)*j/35;const out=compute(x,A1,A2,L1,L2);if(Number.isFinite(out))pts.push([x,out]);}
 if(pts.length<2){plot.textContent='';return;}
 const min=Math.min(...pts.map(p=>p[1])),max=Math.max(...pts.map(p=>p[1])),scale=Math.max(1e-9,max-min);
 const poly=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${182-135*(p[1]-min)/scale}`).join(' ');
 plot.innerHTML=`<line x1="45" y1="186" x2="647" y2="186" stroke="#94a8b2"/><line x1="45" y1="18" x2="45" y2="186" stroke="#94a8b2"/><polyline points="${poly}" stroke="#126e7a" stroke-width="3" fill="none"/><text x="50" y="16" font-size="13" fill="#315667">Input sensitivity (first parameter)</text><text x="50" y="209" font-size="12" fill="#315667">${xLo.toPrecision(3)}</text><text x="585" y="209" font-size="12" fill="#315667">${xHi.toPrecision(3)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));update();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 3,
    unit: 2,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 18</div><h3>Truss displacement</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Educational status:</strong> Editorial draft; not independently peer reviewed or validated for design approval. A simple calculator is not a general finite element solver.</p><article class=\"model\"><h2>Interactive analytical model 03</h2><p><strong>Benchmark relation:</strong> <code>delta=FL/(EA)</code></p><div class=\"inputs\"><label for=\"F\">Axial load (N)<input id=\"F\" type=\"number\" min=\"-50000\" max=\"50000\" value=\"12000\" step=\"any\"></label><label for=\"L\">Bar length (m)<input id=\"L\" type=\"number\" min=\"0.05\" max=\"8\" value=\"1.2\" step=\"any\"></label><label for=\"E\">Young modulus (GPa)<input id=\"E\" type=\"number\" min=\"1\" max=\"300\" value=\"70\" step=\"any\"></label><label for=\"A\">Area (mm\u00b2)<input id=\"A\" type=\"number\" min=\"5\" max=\"3000\" value=\"250\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change a parameter to recalculate.</p></div><svg class=\"plot\" id=\"plot\" viewBox=\"0 0 700 220\" role=\"img\" aria-label=\"Output sensitivity to first parameter\"></svg><p class=\"small\">Pure axial elastic deformation; no buckling or bending. No FE solver is run in this calculator; use the assembled bar lab for the discretized example.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 Model assumptions and all safety limits must be checked.</p>",
    init: function(card) {
      try {
// OpenSTEM Book 18, benchmark model 03: Truss displacement
function compute(F,L,E,A){return F*L/(E*1e9*A*1e-6)*1000;}
function update(){
 const F=Number(card.querySelector("#" + "F".replace(/^#/, "")).value);
 const L=Number(card.querySelector("#" + "L".replace(/^#/, "")).value);
 const E=Number(card.querySelector("#" + "E".replace(/^#/, "")).value);
 const A=Number(card.querySelector("#" + "A".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")),details=card.querySelector("#" + 'details'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(!(Number.isFinite(F) && F>=-50000 && F<=50000 && Number.isFinite(L) && L>=0.05 && L<=8 && Number.isFinite(E) && E>=1 && E<=300 && Number.isFinite(A) && A>=5 && A<=3000)){metric.textContent='Invalid inputs';details.textContent='Use the bounded input ranges.';plot.textContent='';return;}
 const y=compute(F,L,E,A);
 if(!Number.isFinite(y)||Math.abs(y)>1e15){metric.textContent='Undefined';details.textContent='Expression outside its supported domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:6})+' mm';details.textContent="Pure axial elastic deformation; no buckling or bending.";
 const lo=Math.max(-50000,F===0?-1:F*0.8),hi=Math.min(50000,F===0?1:F*1.2);
 const xLo=Math.min(lo,hi-1e-9),xHi=Math.max(hi,lo+1e-9); const pts=[];
 for(let j=0;j<=35;j++){const x=xLo+(xHi-xLo)*j/35;const out=compute(x,L,E,A);if(Number.isFinite(out))pts.push([x,out]);}
 if(pts.length<2){plot.textContent='';return;}
 const min=Math.min(...pts.map(p=>p[1])),max=Math.max(...pts.map(p=>p[1])),scale=Math.max(1e-9,max-min);
 const poly=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${182-135*(p[1]-min)/scale}`).join(' ');
 plot.innerHTML=`<line x1="45" y1="186" x2="647" y2="186" stroke="#94a8b2"/><line x1="45" y1="18" x2="45" y2="186" stroke="#94a8b2"/><polyline points="${poly}" stroke="#126e7a" stroke-width="3" fill="none"/><text x="50" y="16" font-size="13" fill="#315667">Input sensitivity (first parameter)</text><text x="50" y="209" font-size="12" fill="#315667">${xLo.toPrecision(3)}</text><text x="585" y="209" font-size="12" fill="#315667">${xHi.toPrecision(3)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));update();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 4,
    unit: 2,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 18</div><h3>Cantilever bending tip deflection</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Educational status:</strong> Editorial draft; not independently peer reviewed or validated for design approval. A simple calculator is not a general finite element solver.</p><article class=\"model\"><h2>Interactive analytical model 04</h2><p><strong>Benchmark relation:</strong> <code>delta=FL^3/(3EI)</code></p><div class=\"inputs\"><label for=\"F\">End force (N)<input id=\"F\" type=\"number\" min=\"0\" max=\"8000\" value=\"250\" step=\"any\"></label><label for=\"L\">Length (m)<input id=\"L\" type=\"number\" min=\"0.05\" max=\"2\" value=\"0.5\" step=\"any\"></label><label for=\"E\">Young modulus (GPa)<input id=\"E\" type=\"number\" min=\"1\" max=\"300\" value=\"200\" step=\"any\"></label><label for=\"I\">Area moment (mm\u2074)<input id=\"I\" type=\"number\" min=\"100\" max=\"100000000.0\" value=\"15000\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change a parameter to recalculate.</p></div><svg class=\"plot\" id=\"plot\" viewBox=\"0 0 700 220\" role=\"img\" aria-label=\"Output sensitivity to first parameter\"></svg><p class=\"small\">Euler\u2013Bernoulli cantilever with small deflections. No FE solver is run in this calculator; use the assembled bar lab for the discretized example.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 Model assumptions and all safety limits must be checked.</p>",
    init: function(card) {
      try {
// OpenSTEM Book 18, benchmark model 04: Cantilever bending tip deflection
function compute(F,L,E,I){return F*L**3/(3*E*1e9*I*1e-12)*1000;}
function update(){
 const F=Number(card.querySelector("#" + "F".replace(/^#/, "")).value);
 const L=Number(card.querySelector("#" + "L".replace(/^#/, "")).value);
 const E=Number(card.querySelector("#" + "E".replace(/^#/, "")).value);
 const I=Number(card.querySelector("#" + "I".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")),details=card.querySelector("#" + 'details'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(!(Number.isFinite(F) && F>=0 && F<=8000 && Number.isFinite(L) && L>=0.05 && L<=2 && Number.isFinite(E) && E>=1 && E<=300 && Number.isFinite(I) && I>=100 && I<=100000000.0)){metric.textContent='Invalid inputs';details.textContent='Use the bounded input ranges.';plot.textContent='';return;}
 const y=compute(F,L,E,I);
 if(!Number.isFinite(y)||Math.abs(y)>1e15){metric.textContent='Undefined';details.textContent='Expression outside its supported domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:6})+' mm';details.textContent="Euler\u2013Bernoulli cantilever with small deflections.";
 const lo=Math.max(0,F===0?-1:F*0.8),hi=Math.min(8000,F===0?1:F*1.2);
 const xLo=Math.min(lo,hi-1e-9),xHi=Math.max(hi,lo+1e-9); const pts=[];
 for(let j=0;j<=35;j++){const x=xLo+(xHi-xLo)*j/35;const out=compute(x,L,E,I);if(Number.isFinite(out))pts.push([x,out]);}
 if(pts.length<2){plot.textContent='';return;}
 const min=Math.min(...pts.map(p=>p[1])),max=Math.max(...pts.map(p=>p[1])),scale=Math.max(1e-9,max-min);
 const poly=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${182-135*(p[1]-min)/scale}`).join(' ');
 plot.innerHTML=`<line x1="45" y1="186" x2="647" y2="186" stroke="#94a8b2"/><line x1="45" y1="18" x2="45" y2="186" stroke="#94a8b2"/><polyline points="${poly}" stroke="#126e7a" stroke-width="3" fill="none"/><text x="50" y="16" font-size="13" fill="#315667">Input sensitivity (first parameter)</text><text x="50" y="209" font-size="12" fill="#315667">${xLo.toPrecision(3)}</text><text x="585" y="209" font-size="12" fill="#315667">${xHi.toPrecision(3)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));update();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 5,
    unit: 3,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 18</div><h3>Plane-stress von Mises</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Educational status:</strong> Editorial draft; not independently peer reviewed or validated for design approval. A simple calculator is not a general finite element solver.</p><article class=\"model\"><h2>Interactive analytical model 05</h2><p><strong>Benchmark relation:</strong> <code>sigma_vm=sqrt(sx\u00b2-sx*sy+sy\u00b2+3*txy\u00b2)</code></p><div class=\"inputs\"><label for=\"sx\">Normal stress x (MPa)<input id=\"sx\" type=\"number\" min=\"-400\" max=\"400\" value=\"80\" step=\"any\"></label><label for=\"sy\">Normal stress y (MPa)<input id=\"sy\" type=\"number\" min=\"-400\" max=\"400\" value=\"20\" step=\"any\"></label><label for=\"txy\">In-plane shear (MPa)<input id=\"txy\" type=\"number\" min=\"-300\" max=\"300\" value=\"15\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change a parameter to recalculate.</p></div><svg class=\"plot\" id=\"plot\" viewBox=\"0 0 700 220\" role=\"img\" aria-label=\"Output sensitivity to first parameter\"></svg><p class=\"small\">Plane-stress equivalent stress, not a universal failure criterion. No FE solver is run in this calculator; use the assembled bar lab for the discretized example.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 Model assumptions and all safety limits must be checked.</p>",
    init: function(card) {
      try {
// OpenSTEM Book 18, benchmark model 05: Plane-stress von Mises
function compute(sx,sy,txy){return Math.sqrt(sx*sx-sx*sy+sy*sy+3*txy*txy);}
function update(){
 const sx=Number(card.querySelector("#" + "sx".replace(/^#/, "")).value);
 const sy=Number(card.querySelector("#" + "sy".replace(/^#/, "")).value);
 const txy=Number(card.querySelector("#" + "txy".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")),details=card.querySelector("#" + 'details'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(!(Number.isFinite(sx) && sx>=-400 && sx<=400 && Number.isFinite(sy) && sy>=-400 && sy<=400 && Number.isFinite(txy) && txy>=-300 && txy<=300)){metric.textContent='Invalid inputs';details.textContent='Use the bounded input ranges.';plot.textContent='';return;}
 const y=compute(sx,sy,txy);
 if(!Number.isFinite(y)||Math.abs(y)>1e15){metric.textContent='Undefined';details.textContent='Expression outside its supported domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:6})+' MPa';details.textContent="Plane-stress equivalent stress, not a universal failure criterion.";
 const lo=Math.max(-400,sx===0?-1:sx*0.8),hi=Math.min(400,sx===0?1:sx*1.2);
 const xLo=Math.min(lo,hi-1e-9),xHi=Math.max(hi,lo+1e-9); const pts=[];
 for(let j=0;j<=35;j++){const x=xLo+(xHi-xLo)*j/35;const out=compute(x,sy,txy);if(Number.isFinite(out))pts.push([x,out]);}
 if(pts.length<2){plot.textContent='';return;}
 const min=Math.min(...pts.map(p=>p[1])),max=Math.max(...pts.map(p=>p[1])),scale=Math.max(1e-9,max-min);
 const poly=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${182-135*(p[1]-min)/scale}`).join(' ');
 plot.innerHTML=`<line x1="45" y1="186" x2="647" y2="186" stroke="#94a8b2"/><line x1="45" y1="18" x2="45" y2="186" stroke="#94a8b2"/><polyline points="${poly}" stroke="#126e7a" stroke-width="3" fill="none"/><text x="50" y="16" font-size="13" fill="#315667">Input sensitivity (first parameter)</text><text x="50" y="209" font-size="12" fill="#315667">${xLo.toPrecision(3)}</text><text x="585" y="209" font-size="12" fill="#315667">${xHi.toPrecision(3)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));update();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 6,
    unit: 3,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 18</div><h3>Membrane force per width</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Educational status:</strong> Editorial draft; not independently peer reviewed or validated for design approval. A simple calculator is not a general finite element solver.</p><article class=\"model\"><h2>Interactive analytical model 06</h2><p><strong>Benchmark relation:</strong> <code>N_x=sigma_x*t</code></p><div class=\"inputs\"><label for=\"stress\">In-plane stress (MPa)<input id=\"stress\" type=\"number\" min=\"-500\" max=\"500\" value=\"120\" step=\"any\"></label><label for=\"thickness\">Plate thickness (mm)<input id=\"thickness\" type=\"number\" min=\"0.1\" max=\"100\" value=\"3\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change a parameter to recalculate.</p></div><svg class=\"plot\" id=\"plot\" viewBox=\"0 0 700 220\" role=\"img\" aria-label=\"Output sensitivity to first parameter\"></svg><p class=\"small\">Force resultant per unit width in a uniform thin plate. No FE solver is run in this calculator; use the assembled bar lab for the discretized example.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 Model assumptions and all safety limits must be checked.</p>",
    init: function(card) {
      try {
// OpenSTEM Book 18, benchmark model 06: Membrane force per width
function compute(stress,thickness){return stress*thickness;}
function update(){
 const stress=Number(card.querySelector("#" + "stress".replace(/^#/, "")).value);
 const thickness=Number(card.querySelector("#" + "thickness".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")),details=card.querySelector("#" + 'details'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(!(Number.isFinite(stress) && stress>=-500 && stress<=500 && Number.isFinite(thickness) && thickness>=0.1 && thickness<=100)){metric.textContent='Invalid inputs';details.textContent='Use the bounded input ranges.';plot.textContent='';return;}
 const y=compute(stress,thickness);
 if(!Number.isFinite(y)||Math.abs(y)>1e15){metric.textContent='Undefined';details.textContent='Expression outside its supported domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:6})+' N/mm';details.textContent="Force resultant per unit width in a uniform thin plate.";
 const lo=Math.max(-500,stress===0?-1:stress*0.8),hi=Math.min(500,stress===0?1:stress*1.2);
 const xLo=Math.min(lo,hi-1e-9),xHi=Math.max(hi,lo+1e-9); const pts=[];
 for(let j=0;j<=35;j++){const x=xLo+(xHi-xLo)*j/35;const out=compute(x,thickness);if(Number.isFinite(out))pts.push([x,out]);}
 if(pts.length<2){plot.textContent='';return;}
 const min=Math.min(...pts.map(p=>p[1])),max=Math.max(...pts.map(p=>p[1])),scale=Math.max(1e-9,max-min);
 const poly=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${182-135*(p[1]-min)/scale}`).join(' ');
 plot.innerHTML=`<line x1="45" y1="186" x2="647" y2="186" stroke="#94a8b2"/><line x1="45" y1="18" x2="45" y2="186" stroke="#94a8b2"/><polyline points="${poly}" stroke="#126e7a" stroke-width="3" fill="none"/><text x="50" y="16" font-size="13" fill="#315667">Input sensitivity (first parameter)</text><text x="50" y="209" font-size="12" fill="#315667">${xLo.toPrecision(3)}</text><text x="585" y="209" font-size="12" fill="#315667">${xHi.toPrecision(3)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));update();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 7,
    unit: 4,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 18</div><h3>Uniform element size</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Educational status:</strong> Editorial draft; not independently peer reviewed or validated for design approval. A simple calculator is not a general finite element solver.</p><article class=\"model\"><h2>Interactive analytical model 07</h2><p><strong>Benchmark relation:</strong> <code>h=L/n</code></p><div class=\"inputs\"><label for=\"L\">Domain length (m)<input id=\"L\" type=\"number\" min=\"0.01\" max=\"10\" value=\"1\" step=\"any\"></label><label for=\"n\">Number of elements (\u2014)<input id=\"n\" type=\"number\" min=\"2\" max=\"500\" value=\"20\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change a parameter to recalculate.</p></div><svg class=\"plot\" id=\"plot\" viewBox=\"0 0 700 220\" role=\"img\" aria-label=\"Output sensitivity to first parameter\"></svg><p class=\"small\">Mean interval only; quality and refinement patterns vary. No FE solver is run in this calculator; use the assembled bar lab for the discretized example.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 Model assumptions and all safety limits must be checked.</p>",
    init: function(card) {
      try {
// OpenSTEM Book 18, benchmark model 07: Uniform element size
function compute(L,n){return L/n*1000;}
function update(){
 const L=Number(card.querySelector("#" + "L".replace(/^#/, "")).value);
 const n=Number(card.querySelector("#" + "n".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")),details=card.querySelector("#" + 'details'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(!(Number.isFinite(L) && L>=0.01 && L<=10 && Number.isFinite(n) && n>=2 && n<=500)){metric.textContent='Invalid inputs';details.textContent='Use the bounded input ranges.';plot.textContent='';return;}
 const y=compute(L,n);
 if(!Number.isFinite(y)||Math.abs(y)>1e15){metric.textContent='Undefined';details.textContent='Expression outside its supported domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:6})+' mm';details.textContent="Mean interval only; quality and refinement patterns vary.";
 const lo=Math.max(0.01,L===0?-1:L*0.8),hi=Math.min(10,L===0?1:L*1.2);
 const xLo=Math.min(lo,hi-1e-9),xHi=Math.max(hi,lo+1e-9); const pts=[];
 for(let j=0;j<=35;j++){const x=xLo+(xHi-xLo)*j/35;const out=compute(x,n);if(Number.isFinite(out))pts.push([x,out]);}
 if(pts.length<2){plot.textContent='';return;}
 const min=Math.min(...pts.map(p=>p[1])),max=Math.max(...pts.map(p=>p[1])),scale=Math.max(1e-9,max-min);
 const poly=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${182-135*(p[1]-min)/scale}`).join(' ');
 plot.innerHTML=`<line x1="45" y1="186" x2="647" y2="186" stroke="#94a8b2"/><line x1="45" y1="18" x2="45" y2="186" stroke="#94a8b2"/><polyline points="${poly}" stroke="#126e7a" stroke-width="3" fill="none"/><text x="50" y="16" font-size="13" fill="#315667">Input sensitivity (first parameter)</text><text x="50" y="209" font-size="12" fill="#315667">${xLo.toPrecision(3)}</text><text x="585" y="209" font-size="12" fill="#315667">${xHi.toPrecision(3)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));update();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 8,
    unit: 4,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 18</div><h3>Richardson extrapolation</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Educational status:</strong> Editorial draft; not independently peer reviewed or validated for design approval. A simple calculator is not a general finite element solver.</p><article class=\"model\"><h2>Interactive analytical model 08</h2><p><strong>Benchmark relation:</strong> <code>Q*=Q_f+(Q_f-Q_c)/(r^p-1)</code></p><div class=\"inputs\"><label for=\"fine\">Fine-grid displacement (mm)<input id=\"fine\" type=\"number\" min=\"0\" max=\"100\" value=\"1.96\" step=\"any\"></label><label for=\"coarse\">Coarse-grid displacement (mm)<input id=\"coarse\" type=\"number\" min=\"0\" max=\"100\" value=\"1.84\" step=\"any\"></label><label for=\"r\">Refinement ratio (\u2014)<input id=\"r\" type=\"number\" min=\"1.1\" max=\"4\" value=\"2\" step=\"any\"></label><label for=\"p\">Assumed convergence order (\u2014)<input id=\"p\" type=\"number\" min=\"0.5\" max=\"4\" value=\"2\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change a parameter to recalculate.</p></div><svg class=\"plot\" id=\"plot\" viewBox=\"0 0 700 220\" role=\"img\" aria-label=\"Output sensitivity to first parameter\"></svg><p class=\"small\">Requires asymptotic refinement and a known effective order. No FE solver is run in this calculator; use the assembled bar lab for the discretized example.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 Model assumptions and all safety limits must be checked.</p>",
    init: function(card) {
      try {
// OpenSTEM Book 18, benchmark model 08: Richardson extrapolation
function compute(fine,coarse,r,p){return fine+(fine-coarse)/(r**p-1);}
function update(){
 const fine=Number(card.querySelector("#" + "fine".replace(/^#/, "")).value);
 const coarse=Number(card.querySelector("#" + "coarse".replace(/^#/, "")).value);
 const r=Number(card.querySelector("#" + "r".replace(/^#/, "")).value);
 const p=Number(card.querySelector("#" + "p".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")),details=card.querySelector("#" + 'details'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(!(Number.isFinite(fine) && fine>=0 && fine<=100 && Number.isFinite(coarse) && coarse>=0 && coarse<=100 && Number.isFinite(r) && r>=1.1 && r<=4 && Number.isFinite(p) && p>=0.5 && p<=4)){metric.textContent='Invalid inputs';details.textContent='Use the bounded input ranges.';plot.textContent='';return;}
 const y=compute(fine,coarse,r,p);
 if(!Number.isFinite(y)||Math.abs(y)>1e15){metric.textContent='Undefined';details.textContent='Expression outside its supported domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:6})+' mm';details.textContent="Requires asymptotic refinement and a known effective order.";
 const lo=Math.max(0,fine===0?-1:fine*0.8),hi=Math.min(100,fine===0?1:fine*1.2);
 const xLo=Math.min(lo,hi-1e-9),xHi=Math.max(hi,lo+1e-9); const pts=[];
 for(let j=0;j<=35;j++){const x=xLo+(xHi-xLo)*j/35;const out=compute(x,coarse,r,p);if(Number.isFinite(out))pts.push([x,out]);}
 if(pts.length<2){plot.textContent='';return;}
 const min=Math.min(...pts.map(p=>p[1])),max=Math.max(...pts.map(p=>p[1])),scale=Math.max(1e-9,max-min);
 const poly=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${182-135*(p[1]-min)/scale}`).join(' ');
 plot.innerHTML=`<line x1="45" y1="186" x2="647" y2="186" stroke="#94a8b2"/><line x1="45" y1="18" x2="45" y2="186" stroke="#94a8b2"/><polyline points="${poly}" stroke="#126e7a" stroke-width="3" fill="none"/><text x="50" y="16" font-size="13" fill="#315667">Input sensitivity (first parameter)</text><text x="50" y="209" font-size="12" fill="#315667">${xLo.toPrecision(3)}</text><text x="585" y="209" font-size="12" fill="#315667">${xHi.toPrecision(3)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));update();
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 9,
    unit: 5,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 18</div><h3>Thermal free expansion</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Educational status:</strong> Editorial draft; not independently peer reviewed or validated for design approval. A simple calculator is not a general finite element solver.</p><article class=\"model\"><h2>Interactive analytical model 09</h2><p><strong>Benchmark relation:</strong> <code>delta=alpha*DeltaT*L</code></p><div class=\"inputs\"><label for=\"alpha\">Thermal coefficient (\u00b5strain/K)<input id=\"alpha\" type=\"number\" min=\"0\" max=\"100\" value=\"23\" step=\"any\"></label><label for=\"dT\">Temperature rise (K)<input id=\"dT\" type=\"number\" min=\"-200\" max=\"500\" value=\"65\" step=\"any\"></label><label for=\"L\">Initial length (m)<input id=\"L\" type=\"number\" min=\"0.01\" max=\"20\" value=\"1.2\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change a parameter to recalculate.</p></div><svg class=\"plot\" id=\"plot\" viewBox=\"0 0 700 220\" role=\"img\" aria-label=\"Output sensitivity to first parameter\"></svg><p class=\"small\">Free expansion creates no thermal stress in an unconstrained uniform bar. No FE solver is run in this calculator; use the assembled bar lab for the discretized example.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 Model assumptions and all safety limits must be checked.</p>",
    init: function(card) {
      try {
// OpenSTEM Book 18, benchmark model 09: Thermal free expansion
function compute(alpha,dT,L){return alpha*1e-6*dT*L*1000;}
function update(){
 const alpha=Number(card.querySelector("#" + "alpha".replace(/^#/, "")).value);
 const dT=Number(card.querySelector("#" + "dT".replace(/^#/, "")).value);
 const L=Number(card.querySelector("#" + "L".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")),details=card.querySelector("#" + 'details'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(!(Number.isFinite(alpha) && alpha>=0 && alpha<=100 && Number.isFinite(dT) && dT>=-200 && dT<=500 && Number.isFinite(L) && L>=0.01 && L<=20)){metric.textContent='Invalid inputs';details.textContent='Use the bounded input ranges.';plot.textContent='';return;}
 const y=compute(alpha,dT,L);
 if(!Number.isFinite(y)||Math.abs(y)>1e15){metric.textContent='Undefined';details.textContent='Expression outside its supported domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:6})+' mm';details.textContent="Free expansion creates no thermal stress in an unconstrained uniform bar.";
 const lo=Math.max(0,alpha===0?-1:alpha*0.8),hi=Math.min(100,alpha===0?1:alpha*1.2);
 const xLo=Math.min(lo,hi-1e-9),xHi=Math.max(hi,lo+1e-9); const pts=[];
 for(let j=0;j<=35;j++){const x=xLo+(xHi-xLo)*j/35;const out=compute(x,dT,L);if(Number.isFinite(out))pts.push([x,out]);}
 if(pts.length<2){plot.textContent='';return;}
 const min=Math.min(...pts.map(p=>p[1])),max=Math.max(...pts.map(p=>p[1])),scale=Math.max(1e-9,max-min);
 const poly=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${182-135*(p[1]-min)/scale}`).join(' ');
 plot.innerHTML=`<line x1="45" y1="186" x2="647" y2="186" stroke="#94a8b2"/><line x1="45" y1="18" x2="45" y2="186" stroke="#94a8b2"/><polyline points="${poly}" stroke="#126e7a" stroke-width="3" fill="none"/><text x="50" y="16" font-size="13" fill="#315667">Input sensitivity (first parameter)</text><text x="50" y="209" font-size="12" fill="#315667">${xLo.toPrecision(3)}</text><text x="585" y="209" font-size="12" fill="#315667">${xHi.toPrecision(3)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));update();
      } catch (err) {
        console.warn('Sim init error in model 9:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 10,
    unit: 5,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 18</div><h3>Bending outer-fiber stress</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Educational status:</strong> Editorial draft; not independently peer reviewed or validated for design approval. A simple calculator is not a general finite element solver.</p><article class=\"model\"><h2>Interactive analytical model 10</h2><p><strong>Benchmark relation:</strong> <code>sigma=M*c/I</code></p><div class=\"inputs\"><label for=\"M\">Bending moment (N\u00b7m)<input id=\"M\" type=\"number\" min=\"-10000\" max=\"10000\" value=\"600\" step=\"any\"></label><label for=\"c\">Outer fiber distance (mm)<input id=\"c\" type=\"number\" min=\"1\" max=\"200\" value=\"30\" step=\"any\"></label><label for=\"I\">Second moment (mm\u2074)<input id=\"I\" type=\"number\" min=\"1000\" max=\"1000000000.0\" value=\"800000.0\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change a parameter to recalculate.</p></div><svg class=\"plot\" id=\"plot\" viewBox=\"0 0 700 220\" role=\"img\" aria-label=\"Output sensitivity to first parameter\"></svg><p class=\"small\">Linear elastic beam section with valid Bernoulli assumptions. No FE solver is run in this calculator; use the assembled bar lab for the discretized example.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 Model assumptions and all safety limits must be checked.</p>",
    init: function(card) {
      try {
// OpenSTEM Book 18, benchmark model 10: Bending outer-fiber stress
function compute(M,c,I){return (M*1000)*c/I;}
function update(){
 const M=Number(card.querySelector("#" + "M".replace(/^#/, "")).value);
 const c=Number(card.querySelector("#" + "c".replace(/^#/, "")).value);
 const I=Number(card.querySelector("#" + "I".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")),details=card.querySelector("#" + 'details'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(!(Number.isFinite(M) && M>=-10000 && M<=10000 && Number.isFinite(c) && c>=1 && c<=200 && Number.isFinite(I) && I>=1000 && I<=1000000000.0)){metric.textContent='Invalid inputs';details.textContent='Use the bounded input ranges.';plot.textContent='';return;}
 const y=compute(M,c,I);
 if(!Number.isFinite(y)||Math.abs(y)>1e15){metric.textContent='Undefined';details.textContent='Expression outside its supported domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:6})+' MPa';details.textContent="Linear elastic beam section with valid Bernoulli assumptions.";
 const lo=Math.max(-10000,M===0?-1:M*0.8),hi=Math.min(10000,M===0?1:M*1.2);
 const xLo=Math.min(lo,hi-1e-9),xHi=Math.max(hi,lo+1e-9); const pts=[];
 for(let j=0;j<=35;j++){const x=xLo+(xHi-xLo)*j/35;const out=compute(x,c,I);if(Number.isFinite(out))pts.push([x,out]);}
 if(pts.length<2){plot.textContent='';return;}
 const min=Math.min(...pts.map(p=>p[1])),max=Math.max(...pts.map(p=>p[1])),scale=Math.max(1e-9,max-min);
 const poly=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${182-135*(p[1]-min)/scale}`).join(' ');
 plot.innerHTML=`<line x1="45" y1="186" x2="647" y2="186" stroke="#94a8b2"/><line x1="45" y1="18" x2="45" y2="186" stroke="#94a8b2"/><polyline points="${poly}" stroke="#126e7a" stroke-width="3" fill="none"/><text x="50" y="16" font-size="13" fill="#315667">Input sensitivity (first parameter)</text><text x="50" y="209" font-size="12" fill="#315667">${xLo.toPrecision(3)}</text><text x="585" y="209" font-size="12" fill="#315667">${xHi.toPrecision(3)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));update();
      } catch (err) {
        console.warn('Sim init error in model 10:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 11,
    unit: 6,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 18</div><h3>One-dimensional heat conduction</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Educational status:</strong> Editorial draft; not independently peer reviewed or validated for design approval. A simple calculator is not a general finite element solver.</p><article class=\"model\"><h2>Interactive analytical model 11</h2><p><strong>Benchmark relation:</strong> <code>Q=k*A*DeltaT/L</code></p><div class=\"inputs\"><label for=\"k\">Thermal conductivity (W/(mK))<input id=\"k\" type=\"number\" min=\"0.1\" max=\"400\" value=\"45\" step=\"any\"></label><label for=\"A\">Cross section (m\u00b2)<input id=\"A\" type=\"number\" min=\"0.0001\" max=\"2\" value=\"0.04\" step=\"any\"></label><label for=\"dT\">Temperature difference (K)<input id=\"dT\" type=\"number\" min=\"-200\" max=\"300\" value=\"40\" step=\"any\"></label><label for=\"L\">Thickness (m)<input id=\"L\" type=\"number\" min=\"0.001\" max=\"1\" value=\"0.02\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change a parameter to recalculate.</p></div><svg class=\"plot\" id=\"plot\" viewBox=\"0 0 700 220\" role=\"img\" aria-label=\"Output sensitivity to first parameter\"></svg><p class=\"small\">Steady 1D conduction and constant conductivity. No FE solver is run in this calculator; use the assembled bar lab for the discretized example.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 Model assumptions and all safety limits must be checked.</p>",
    init: function(card) {
      try {
// OpenSTEM Book 18, benchmark model 11: One-dimensional heat conduction
function compute(k,A,dT,L){return k*A*dT/L;}
function update(){
 const k=Number(card.querySelector("#" + "k".replace(/^#/, "")).value);
 const A=Number(card.querySelector("#" + "A".replace(/^#/, "")).value);
 const dT=Number(card.querySelector("#" + "dT".replace(/^#/, "")).value);
 const L=Number(card.querySelector("#" + "L".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")),details=card.querySelector("#" + 'details'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(!(Number.isFinite(k) && k>=0.1 && k<=400 && Number.isFinite(A) && A>=0.0001 && A<=2 && Number.isFinite(dT) && dT>=-200 && dT<=300 && Number.isFinite(L) && L>=0.001 && L<=1)){metric.textContent='Invalid inputs';details.textContent='Use the bounded input ranges.';plot.textContent='';return;}
 const y=compute(k,A,dT,L);
 if(!Number.isFinite(y)||Math.abs(y)>1e15){metric.textContent='Undefined';details.textContent='Expression outside its supported domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:6})+' W';details.textContent="Steady 1D conduction and constant conductivity.";
 const lo=Math.max(0.1,k===0?-1:k*0.8),hi=Math.min(400,k===0?1:k*1.2);
 const xLo=Math.min(lo,hi-1e-9),xHi=Math.max(hi,lo+1e-9); const pts=[];
 for(let j=0;j<=35;j++){const x=xLo+(xHi-xLo)*j/35;const out=compute(x,A,dT,L);if(Number.isFinite(out))pts.push([x,out]);}
 if(pts.length<2){plot.textContent='';return;}
 const min=Math.min(...pts.map(p=>p[1])),max=Math.max(...pts.map(p=>p[1])),scale=Math.max(1e-9,max-min);
 const poly=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${182-135*(p[1]-min)/scale}`).join(' ');
 plot.innerHTML=`<line x1="45" y1="186" x2="647" y2="186" stroke="#94a8b2"/><line x1="45" y1="18" x2="45" y2="186" stroke="#94a8b2"/><polyline points="${poly}" stroke="#126e7a" stroke-width="3" fill="none"/><text x="50" y="16" font-size="13" fill="#315667">Input sensitivity (first parameter)</text><text x="50" y="209" font-size="12" fill="#315667">${xLo.toPrecision(3)}</text><text x="585" y="209" font-size="12" fill="#315667">${xHi.toPrecision(3)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));update();
      } catch (err) {
        console.warn('Sim init error in model 11:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 12,
    unit: 6,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 18</div><h3>Conduction plus convection resistance</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Educational status:</strong> Editorial draft; not independently peer reviewed or validated for design approval. A simple calculator is not a general finite element solver.</p><article class=\"model\"><h2>Interactive analytical model 12</h2><p><strong>Benchmark relation:</strong> <code>R=L/(kA)+1/(hA)</code></p><div class=\"inputs\"><label for=\"L\">Solid thickness (m)<input id=\"L\" type=\"number\" min=\"0.001\" max=\"0.5\" value=\"0.015\" step=\"any\"></label><label for=\"k\">Conductivity (W/(mK))<input id=\"k\" type=\"number\" min=\"0.1\" max=\"400\" value=\"12\" step=\"any\"></label><label for=\"h\">Film coefficient (W/(m\u00b2K))<input id=\"h\" type=\"number\" min=\"1\" max=\"1000\" value=\"25\" step=\"any\"></label><label for=\"A\">Area (m\u00b2)<input id=\"A\" type=\"number\" min=\"0.001\" max=\"4\" value=\"0.15\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change a parameter to recalculate.</p></div><svg class=\"plot\" id=\"plot\" viewBox=\"0 0 700 220\" role=\"img\" aria-label=\"Output sensitivity to first parameter\"></svg><p class=\"small\">Single steady heat-flow path; excludes contact resistance. No FE solver is run in this calculator; use the assembled bar lab for the discretized example.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 Model assumptions and all safety limits must be checked.</p>",
    init: function(card) {
      try {
// OpenSTEM Book 18, benchmark model 12: Conduction plus convection resistance
function compute(L,k,h,A){return L/(k*A)+1/(h*A);}
function update(){
 const L=Number(card.querySelector("#" + "L".replace(/^#/, "")).value);
 const k=Number(card.querySelector("#" + "k".replace(/^#/, "")).value);
 const h=Number(card.querySelector("#" + "h".replace(/^#/, "")).value);
 const A=Number(card.querySelector("#" + "A".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")),details=card.querySelector("#" + 'details'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(!(Number.isFinite(L) && L>=0.001 && L<=0.5 && Number.isFinite(k) && k>=0.1 && k<=400 && Number.isFinite(h) && h>=1 && h<=1000 && Number.isFinite(A) && A>=0.001 && A<=4)){metric.textContent='Invalid inputs';details.textContent='Use the bounded input ranges.';plot.textContent='';return;}
 const y=compute(L,k,h,A);
 if(!Number.isFinite(y)||Math.abs(y)>1e15){metric.textContent='Undefined';details.textContent='Expression outside its supported domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:6})+' K/W';details.textContent="Single steady heat-flow path; excludes contact resistance.";
 const lo=Math.max(0.001,L===0?-1:L*0.8),hi=Math.min(0.5,L===0?1:L*1.2);
 const xLo=Math.min(lo,hi-1e-9),xHi=Math.max(hi,lo+1e-9); const pts=[];
 for(let j=0;j<=35;j++){const x=xLo+(xHi-xLo)*j/35;const out=compute(x,k,h,A);if(Number.isFinite(out))pts.push([x,out]);}
 if(pts.length<2){plot.textContent='';return;}
 const min=Math.min(...pts.map(p=>p[1])),max=Math.max(...pts.map(p=>p[1])),scale=Math.max(1e-9,max-min);
 const poly=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${182-135*(p[1]-min)/scale}`).join(' ');
 plot.innerHTML=`<line x1="45" y1="186" x2="647" y2="186" stroke="#94a8b2"/><line x1="45" y1="18" x2="45" y2="186" stroke="#94a8b2"/><polyline points="${poly}" stroke="#126e7a" stroke-width="3" fill="none"/><text x="50" y="16" font-size="13" fill="#315667">Input sensitivity (first parameter)</text><text x="50" y="209" font-size="12" fill="#315667">${xLo.toPrecision(3)}</text><text x="585" y="209" font-size="12" fill="#315667">${xHi.toPrecision(3)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));update();
      } catch (err) {
        console.warn('Sim init error in model 12:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 13,
    unit: 7,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 18</div><h3>Natural frequency of one mode</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Educational status:</strong> Editorial draft; not independently peer reviewed or validated for design approval. A simple calculator is not a general finite element solver.</p><article class=\"model\"><h2>Interactive analytical model 13</h2><p><strong>Benchmark relation:</strong> <code>f=sqrt(k/m)/(2pi)</code></p><div class=\"inputs\"><label for=\"k\">Equivalent stiffness (N/m)<input id=\"k\" type=\"number\" min=\"100\" max=\"100000000.0\" value=\"80000\" step=\"any\"></label><label for=\"m\">Modal mass (kg)<input id=\"m\" type=\"number\" min=\"0.1\" max=\"5000\" value=\"35\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change a parameter to recalculate.</p></div><svg class=\"plot\" id=\"plot\" viewBox=\"0 0 700 220\" role=\"img\" aria-label=\"Output sensitivity to first parameter\"></svg><p class=\"small\">Single-degree-of-freedom estimate, not a full FE modal solution. No FE solver is run in this calculator; use the assembled bar lab for the discretized example.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 Model assumptions and all safety limits must be checked.</p>",
    init: function(card) {
      try {
// OpenSTEM Book 18, benchmark model 13: Natural frequency of one mode
function compute(k,m){return Math.sqrt(k/m)/(2*Math.PI);}
function update(){
 const k=Number(card.querySelector("#" + "k".replace(/^#/, "")).value);
 const m=Number(card.querySelector("#" + "m".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")),details=card.querySelector("#" + 'details'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(!(Number.isFinite(k) && k>=100 && k<=100000000.0 && Number.isFinite(m) && m>=0.1 && m<=5000)){metric.textContent='Invalid inputs';details.textContent='Use the bounded input ranges.';plot.textContent='';return;}
 const y=compute(k,m);
 if(!Number.isFinite(y)||Math.abs(y)>1e15){metric.textContent='Undefined';details.textContent='Expression outside its supported domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:6})+' Hz';details.textContent="Single-degree-of-freedom estimate, not a full FE modal solution.";
 const lo=Math.max(100,k===0?-1:k*0.8),hi=Math.min(100000000.0,k===0?1:k*1.2);
 const xLo=Math.min(lo,hi-1e-9),xHi=Math.max(hi,lo+1e-9); const pts=[];
 for(let j=0;j<=35;j++){const x=xLo+(xHi-xLo)*j/35;const out=compute(x,m);if(Number.isFinite(out))pts.push([x,out]);}
 if(pts.length<2){plot.textContent='';return;}
 const min=Math.min(...pts.map(p=>p[1])),max=Math.max(...pts.map(p=>p[1])),scale=Math.max(1e-9,max-min);
 const poly=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${182-135*(p[1]-min)/scale}`).join(' ');
 plot.innerHTML=`<line x1="45" y1="186" x2="647" y2="186" stroke="#94a8b2"/><line x1="45" y1="18" x2="45" y2="186" stroke="#94a8b2"/><polyline points="${poly}" stroke="#126e7a" stroke-width="3" fill="none"/><text x="50" y="16" font-size="13" fill="#315667">Input sensitivity (first parameter)</text><text x="50" y="209" font-size="12" fill="#315667">${xLo.toPrecision(3)}</text><text x="585" y="209" font-size="12" fill="#315667">${xHi.toPrecision(3)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));update();
      } catch (err) {
        console.warn('Sim init error in model 13:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 14,
    unit: 7,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 18</div><h3>Viscous damping ratio</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Educational status:</strong> Editorial draft; not independently peer reviewed or validated for design approval. A simple calculator is not a general finite element solver.</p><article class=\"model\"><h2>Interactive analytical model 14</h2><p><strong>Benchmark relation:</strong> <code>zeta=c/(2sqrt(km))</code></p><div class=\"inputs\"><label for=\"c\">Damping coefficient (N\u00b7s/m)<input id=\"c\" type=\"number\" min=\"0\" max=\"50000\" value=\"130\" step=\"any\"></label><label for=\"k\">Stiffness (N/m)<input id=\"k\" type=\"number\" min=\"100\" max=\"100000000.0\" value=\"90000\" step=\"any\"></label><label for=\"m\">Mass (kg)<input id=\"m\" type=\"number\" min=\"0.1\" max=\"5000\" value=\"24\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change a parameter to recalculate.</p></div><svg class=\"plot\" id=\"plot\" viewBox=\"0 0 700 220\" role=\"img\" aria-label=\"Output sensitivity to first parameter\"></svg><p class=\"small\">Assumes linear viscous damping and positive mass and stiffness. No FE solver is run in this calculator; use the assembled bar lab for the discretized example.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 Model assumptions and all safety limits must be checked.</p>",
    init: function(card) {
      try {
// OpenSTEM Book 18, benchmark model 14: Viscous damping ratio
function compute(c,k,m){return c/(2*Math.sqrt(k*m));}
function update(){
 const c=Number(card.querySelector("#" + "c".replace(/^#/, "")).value);
 const k=Number(card.querySelector("#" + "k".replace(/^#/, "")).value);
 const m=Number(card.querySelector("#" + "m".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")),details=card.querySelector("#" + 'details'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(!(Number.isFinite(c) && c>=0 && c<=50000 && Number.isFinite(k) && k>=100 && k<=100000000.0 && Number.isFinite(m) && m>=0.1 && m<=5000)){metric.textContent='Invalid inputs';details.textContent='Use the bounded input ranges.';plot.textContent='';return;}
 const y=compute(c,k,m);
 if(!Number.isFinite(y)||Math.abs(y)>1e15){metric.textContent='Undefined';details.textContent='Expression outside its supported domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:6})+' —';details.textContent="Assumes linear viscous damping and positive mass and stiffness.";
 const lo=Math.max(0,c===0?-1:c*0.8),hi=Math.min(50000,c===0?1:c*1.2);
 const xLo=Math.min(lo,hi-1e-9),xHi=Math.max(hi,lo+1e-9); const pts=[];
 for(let j=0;j<=35;j++){const x=xLo+(xHi-xLo)*j/35;const out=compute(x,k,m);if(Number.isFinite(out))pts.push([x,out]);}
 if(pts.length<2){plot.textContent='';return;}
 const min=Math.min(...pts.map(p=>p[1])),max=Math.max(...pts.map(p=>p[1])),scale=Math.max(1e-9,max-min);
 const poly=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${182-135*(p[1]-min)/scale}`).join(' ');
 plot.innerHTML=`<line x1="45" y1="186" x2="647" y2="186" stroke="#94a8b2"/><line x1="45" y1="18" x2="45" y2="186" stroke="#94a8b2"/><polyline points="${poly}" stroke="#126e7a" stroke-width="3" fill="none"/><text x="50" y="16" font-size="13" fill="#315667">Input sensitivity (first parameter)</text><text x="50" y="209" font-size="12" fill="#315667">${xLo.toPrecision(3)}</text><text x="585" y="209" font-size="12" fill="#315667">${xHi.toPrecision(3)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));update();
      } catch (err) {
        console.warn('Sim init error in model 14:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 15,
    unit: 8,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 18</div><h3>Normalized equilibrium residual</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Educational status:</strong> Editorial draft; not independently peer reviewed or validated for design approval. A simple calculator is not a general finite element solver.</p><article class=\"model\"><h2>Interactive analytical model 15</h2><p><strong>Benchmark relation:</strong> <code>r_norm=abs(R)/max(abs(F),1)</code></p><div class=\"inputs\"><label for=\"R\">Unbalanced nodal force (N)<input id=\"R\" type=\"number\" min=\"-50000\" max=\"50000\" value=\"15\" step=\"any\"></label><label for=\"F\">Applied force scale (N)<input id=\"F\" type=\"number\" min=\"-50000\" max=\"50000\" value=\"7000\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change a parameter to recalculate.</p></div><svg class=\"plot\" id=\"plot\" viewBox=\"0 0 700 220\" role=\"img\" aria-label=\"Output sensitivity to first parameter\"></svg><p class=\"small\">Small solver residual does not establish solution accuracy. No FE solver is run in this calculator; use the assembled bar lab for the discretized example.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 Model assumptions and all safety limits must be checked.</p>",
    init: function(card) {
      try {
// OpenSTEM Book 18, benchmark model 15: Normalized equilibrium residual
function compute(R,F){return Math.abs(R)/Math.max(Math.abs(F),1)*100;}
function update(){
 const R=Number(card.querySelector("#" + "R".replace(/^#/, "")).value);
 const F=Number(card.querySelector("#" + "F".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")),details=card.querySelector("#" + 'details'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(!(Number.isFinite(R) && R>=-50000 && R<=50000 && Number.isFinite(F) && F>=-50000 && F<=50000)){metric.textContent='Invalid inputs';details.textContent='Use the bounded input ranges.';plot.textContent='';return;}
 const y=compute(R,F);
 if(!Number.isFinite(y)||Math.abs(y)>1e15){metric.textContent='Undefined';details.textContent='Expression outside its supported domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:6})+' %';details.textContent="Small solver residual does not establish solution accuracy.";
 const lo=Math.max(-50000,R===0?-1:R*0.8),hi=Math.min(50000,R===0?1:R*1.2);
 const xLo=Math.min(lo,hi-1e-9),xHi=Math.max(hi,lo+1e-9); const pts=[];
 for(let j=0;j<=35;j++){const x=xLo+(xHi-xLo)*j/35;const out=compute(x,F);if(Number.isFinite(out))pts.push([x,out]);}
 if(pts.length<2){plot.textContent='';return;}
 const min=Math.min(...pts.map(p=>p[1])),max=Math.max(...pts.map(p=>p[1])),scale=Math.max(1e-9,max-min);
 const poly=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${182-135*(p[1]-min)/scale}`).join(' ');
 plot.innerHTML=`<line x1="45" y1="186" x2="647" y2="186" stroke="#94a8b2"/><line x1="45" y1="18" x2="45" y2="186" stroke="#94a8b2"/><polyline points="${poly}" stroke="#126e7a" stroke-width="3" fill="none"/><text x="50" y="16" font-size="13" fill="#315667">Input sensitivity (first parameter)</text><text x="50" y="209" font-size="12" fill="#315667">${xLo.toPrecision(3)}</text><text x="585" y="209" font-size="12" fill="#315667">${xHi.toPrecision(3)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));update();
      } catch (err) {
        console.warn('Sim init error in model 15:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 16,
    unit: 8,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 18</div><h3>Model-to-test relative discrepancy</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Educational status:</strong> Editorial draft; not independently peer reviewed or validated for design approval. A simple calculator is not a general finite element solver.</p><article class=\"model\"><h2>Interactive analytical model 16</h2><p><strong>Benchmark relation:</strong> <code>e=abs(Q_FE-Q_test)/abs(Q_test)</code></p><div class=\"inputs\"><label for=\"pred\">FE prediction (mm)<input id=\"pred\" type=\"number\" min=\"-100\" max=\"100\" value=\"2.45\" step=\"any\"></label><label for=\"test\">Measured response (mm)<input id=\"test\" type=\"number\" min=\"0.01\" max=\"100\" value=\"2.38\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change a parameter to recalculate.</p></div><svg class=\"plot\" id=\"plot\" viewBox=\"0 0 700 220\" role=\"img\" aria-label=\"Output sensitivity to first parameter\"></svg><p class=\"small\">Requires independent measurements and nonzero tested reference. No FE solver is run in this calculator; use the assembled bar lab for the discretized example.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 Model assumptions and all safety limits must be checked.</p>",
    init: function(card) {
      try {
// OpenSTEM Book 18, benchmark model 16: Model-to-test relative discrepancy
function compute(pred,test){return Math.abs(pred-test)/Math.abs(test)*100;}
function update(){
 const pred=Number(card.querySelector("#" + "pred".replace(/^#/, "")).value);
 const test=Number(card.querySelector("#" + "test".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")),details=card.querySelector("#" + 'details'.replace(/^#/, "")),plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(!(Number.isFinite(pred) && pred>=-100 && pred<=100 && Number.isFinite(test) && test>=0.01 && test<=100)){metric.textContent='Invalid inputs';details.textContent='Use the bounded input ranges.';plot.textContent='';return;}
 const y=compute(pred,test);
 if(!Number.isFinite(y)||Math.abs(y)>1e15){metric.textContent='Undefined';details.textContent='Expression outside its supported domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:6})+' %';details.textContent="Requires independent measurements and nonzero tested reference.";
 const lo=Math.max(-100,pred===0?-1:pred*0.8),hi=Math.min(100,pred===0?1:pred*1.2);
 const xLo=Math.min(lo,hi-1e-9),xHi=Math.max(hi,lo+1e-9); const pts=[];
 for(let j=0;j<=35;j++){const x=xLo+(xHi-xLo)*j/35;const out=compute(x,test);if(Number.isFinite(out))pts.push([x,out]);}
 if(pts.length<2){plot.textContent='';return;}
 const min=Math.min(...pts.map(p=>p[1])),max=Math.max(...pts.map(p=>p[1])),scale=Math.max(1e-9,max-min);
 const poly=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${182-135*(p[1]-min)/scale}`).join(' ');
 plot.innerHTML=`<line x1="45" y1="186" x2="647" y2="186" stroke="#94a8b2"/><line x1="45" y1="18" x2="45" y2="186" stroke="#94a8b2"/><polyline points="${poly}" stroke="#126e7a" stroke-width="3" fill="none"/><text x="50" y="16" font-size="13" fill="#315667">Input sensitivity (first parameter)</text><text x="50" y="209" font-size="12" fill="#315667">${xLo.toPrecision(3)}</text><text x="585" y="209" font-size="12" fill="#315667">${xHi.toPrecision(3)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));update();
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
