/* turbomachinery Interactive Simulation Suite */
(function(window) {
  'use strict';

  var OPENSTEM_SIM_MODELS = [];

  OPENSTEM_SIM_MODELS.push({
    idx: 1,
    unit: 1,
    html: "<header class=\"hero\"><div class=\"eyebrow\">MECHANICAL ENGINEERING \u00b7 BOOK 15</div><h3>Euler work on fluid</h3><p class=\"subtitle\">Offline, mobile-friendly teaching content \u00b7 unreviewed educational draft.</p><div class=\"metrics\"><span>8 units</span><span>40 lessons</span><span>16 simulators</span><span>8 datasets</span></div></header><p class=\"notice\"><strong>Teaching model 01:</strong> A simplified formula evaluator, not a safety-rated digital twin. Validate all state ranges and reference conditions. Never use these outputs to approve machinery.</p><article class=\"model-panel\"><h2>Euler work on fluid</h2><p class=\"small\">Positive = energy added to fluid; turbine extraction has opposite sign.</p><div class=\"fields\"><label>Inlet blade speed (m/s)<input type=\"number\" id=\"u1\" value=\"100\" min=\"1\" max=\"500\" step=\"any\"></label><label>Inlet tangential velocity (m/s)<input type=\"number\" id=\"vt1\" value=\"10\" min=\"-300\" max=\"400\" step=\"any\"></label><label>Exit blade speed (m/s)<input type=\"number\" id=\"u2\" value=\"200\" min=\"1\" max=\"600\" step=\"any\"></label><label>Exit tangential velocity (m/s)<input type=\"number\" id=\"vt2\" value=\"100\" min=\"-300\" max=\"400\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\">\u2014</div><div id=\"result\" class=\"small\">Change any input to recalculate.</div></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 650 190\" role=\"img\" aria-label=\"Illustrative output envelope\"></svg><p class=\"small\">The blue line illustrates scalar output \u00b130% around the computed value. It is not a validated performance curve. Check limits before interpreting signs.</p></article>",
    init: function(card) {
      try {
const __modelIndex=1;
function calculate(){
 const u1=Number(card.querySelector("#" + 'u1'.replace(/^#/, "")).value);
const vt1=Number(card.querySelector("#" + 'vt1'.replace(/^#/, "")).value);
const u2=Number(card.querySelector("#" + 'u2'.replace(/^#/, "")).value);
const vt2=Number(card.querySelector("#" + 'vt2'.replace(/^#/, "")).value);
 const ok=(Number.isFinite(u1) && u1>=1 && u1<=500 && Number.isFinite(vt1) && vt1>=-300 && vt1<=400 && Number.isFinite(u2) && u2>=1 && u2<=600 && Number.isFinite(vt2) && vt2>=-300 && vt2<=400);
 if(!ok){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Invalid values or model assumptions. Check input limits and required state order.';card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent='—';return;}
 const result=(u2*vt2-u1*vt1);
 if(!Number.isFinite(result)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Undefined at these conditions.';return;}
 card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent=result.toLocaleString('en-US',{maximumFractionDigits:4})+' J/kg';
 card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Positive = energy added to fluid; turbine extraction has opposite sign.';
 const vals=[];
 const base=result;
 for(let j=0;j<31;j++){
   let fac=0.7+j*0.02;
   vals.push([j/30,base*fac]);
 }
 const chart=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const Y=vals.map(v=>v[1]);const lo=Math.min(...Y,0), hi=Math.max(...Y,0);const range=Math.max(1e-10,hi-lo);
 let poly=vals.map(v=>`${25+600*v[0]},${170-145*(v[1]-lo)/range}`).join(' ');
 chart.innerHTML=`<line x1="25" y1="170" x2="625" y2="170" stroke="#a0b5c5"/><line x1="25" y1="20" x2="25" y2="170" stroke="#a0b5c5"/><polyline fill="none" stroke="#176b96" stroke-width="3" points="${poly}"/><circle cx="325" cy="${170-145*(base-lo)/range}" r="5" fill="#d46f37"/><text x="30" y="17" font-size="11" fill="#415d76">Illustrative ±30% output envelope, not a physical parameter sweep</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',calculate));calculate();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 2,
    unit: 1,
    html: "<header class=\"hero\"><div class=\"eyebrow\">MECHANICAL ENGINEERING \u00b7 BOOK 15</div><h3>Velocity triangle</h3><p class=\"subtitle\">Offline, mobile-friendly teaching content \u00b7 unreviewed educational draft.</p><div class=\"metrics\"><span>8 units</span><span>40 lessons</span><span>16 simulators</span><span>8 datasets</span></div></header><p class=\"notice\"><strong>Teaching model 02:</strong> A simplified formula evaluator, not a safety-rated digital twin. Validate all state ranges and reference conditions. Never use these outputs to approve machinery.</p><article class=\"model-panel\"><h2>Velocity triangle</h2><p class=\"small\">Relative blade-flow angle beta; negative indicates whirl opposite rotation.</p><div class=\"fields\"><label>Blade speed (m/s)<input type=\"number\" id=\"u\" value=\"150\" min=\"1\" max=\"600\" step=\"any\"></label><label>Absolute whirl (m/s)<input type=\"number\" id=\"vt\" value=\"35\" min=\"-300\" max=\"500\" step=\"any\"></label><label>Axial velocity (m/s)<input type=\"number\" id=\"vx\" value=\"70\" min=\"0.1\" max=\"400\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\">\u2014</div><div id=\"result\" class=\"small\">Change any input to recalculate.</div></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 650 190\" role=\"img\" aria-label=\"Illustrative output envelope\"></svg><p class=\"small\">The blue line illustrates scalar output \u00b130% around the computed value. It is not a validated performance curve. Check limits before interpreting signs.</p></article>",
    init: function(card) {
      try {
const __modelIndex=2;
function calculate(){
 const u=Number(card.querySelector("#" + 'u'.replace(/^#/, "")).value);
const vt=Number(card.querySelector("#" + 'vt'.replace(/^#/, "")).value);
const vx=Number(card.querySelector("#" + 'vx'.replace(/^#/, "")).value);
 const ok=(Number.isFinite(u) && u>=1 && u<=600 && Number.isFinite(vt) && vt>=-300 && vt<=500 && Number.isFinite(vx) && vx>=0.1 && vx<=400);
 if(!ok){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Invalid values or model assumptions. Check input limits and required state order.';card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent='—';return;}
 const result=(Math.atan2((vt-u),vx)*180/Math.PI);
 if(!Number.isFinite(result)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Undefined at these conditions.';return;}
 card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent=result.toLocaleString('en-US',{maximumFractionDigits:4})+' deg';
 card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Relative blade-flow angle beta; negative indicates whirl opposite rotation.';
 const vals=[];
 const base=result;
 for(let j=0;j<31;j++){
   let fac=0.7+j*0.02;
   vals.push([j/30,base*fac]);
 }
 const chart=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const Y=vals.map(v=>v[1]);const lo=Math.min(...Y,0), hi=Math.max(...Y,0);const range=Math.max(1e-10,hi-lo);
 let poly=vals.map(v=>`${25+600*v[0]},${170-145*(v[1]-lo)/range}`).join(' ');
 chart.innerHTML=`<line x1="25" y1="170" x2="625" y2="170" stroke="#a0b5c5"/><line x1="25" y1="20" x2="25" y2="170" stroke="#a0b5c5"/><polyline fill="none" stroke="#176b96" stroke-width="3" points="${poly}"/><circle cx="325" cy="${170-145*(base-lo)/range}" r="5" fill="#d46f37"/><text x="30" y="17" font-size="11" fill="#415d76">Illustrative ±30% output envelope, not a physical parameter sweep</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',calculate));calculate();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 3,
    unit: 2,
    html: "<header class=\"hero\"><div class=\"eyebrow\">MECHANICAL ENGINEERING \u00b7 BOOK 15</div><h3>Pump head from pressure rise</h3><p class=\"subtitle\">Offline, mobile-friendly teaching content \u00b7 unreviewed educational draft.</p><div class=\"metrics\"><span>8 units</span><span>40 lessons</span><span>16 simulators</span><span>8 datasets</span></div></header><p class=\"notice\"><strong>Teaching model 03:</strong> A simplified formula evaluator, not a safety-rated digital twin. Validate all state ranges and reference conditions. Never use these outputs to approve machinery.</p><article class=\"model-panel\"><h2>Pump head from pressure rise</h2><p class=\"small\">Velocity and elevation corrections are excluded.</p><div class=\"fields\"><label>Differential pressure (kPa)<input type=\"number\" id=\"dp\" value=\"180\" min=\"-200\" max=\"1000\" step=\"any\"></label><label>Density (kg/m\u00b3)<input type=\"number\" id=\"rho\" value=\"998\" min=\"300\" max=\"2000\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\">\u2014</div><div id=\"result\" class=\"small\">Change any input to recalculate.</div></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 650 190\" role=\"img\" aria-label=\"Illustrative output envelope\"></svg><p class=\"small\">The blue line illustrates scalar output \u00b130% around the computed value. It is not a validated performance curve. Check limits before interpreting signs.</p></article>",
    init: function(card) {
      try {
const __modelIndex=3;
function calculate(){
 const dp=Number(card.querySelector("#" + 'dp'.replace(/^#/, "")).value);
const rho=Number(card.querySelector("#" + 'rho'.replace(/^#/, "")).value);
 const ok=(Number.isFinite(dp) && dp>=-200 && dp<=1000 && Number.isFinite(rho) && rho>=300 && rho<=2000);
 if(!ok){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Invalid values or model assumptions. Check input limits and required state order.';card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent='—';return;}
 const result=(dp*1000/(rho*9.81));
 if(!Number.isFinite(result)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Undefined at these conditions.';return;}
 card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent=result.toLocaleString('en-US',{maximumFractionDigits:4})+' m';
 card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Velocity and elevation corrections are excluded.';
 const vals=[];
 const base=result;
 for(let j=0;j<31;j++){
   let fac=0.7+j*0.02;
   vals.push([j/30,base*fac]);
 }
 const chart=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const Y=vals.map(v=>v[1]);const lo=Math.min(...Y,0), hi=Math.max(...Y,0);const range=Math.max(1e-10,hi-lo);
 let poly=vals.map(v=>`${25+600*v[0]},${170-145*(v[1]-lo)/range}`).join(' ');
 chart.innerHTML=`<line x1="25" y1="170" x2="625" y2="170" stroke="#a0b5c5"/><line x1="25" y1="20" x2="25" y2="170" stroke="#a0b5c5"/><polyline fill="none" stroke="#176b96" stroke-width="3" points="${poly}"/><circle cx="325" cy="${170-145*(base-lo)/range}" r="5" fill="#d46f37"/><text x="30" y="17" font-size="11" fill="#415d76">Illustrative ±30% output envelope, not a physical parameter sweep</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',calculate));calculate();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 4,
    unit: 2,
    html: "<header class=\"hero\"><div class=\"eyebrow\">MECHANICAL ENGINEERING \u00b7 BOOK 15</div><h3>Pump electrical power</h3><p class=\"subtitle\">Offline, mobile-friendly teaching content \u00b7 unreviewed educational draft.</p><div class=\"metrics\"><span>8 units</span><span>40 lessons</span><span>16 simulators</span><span>8 datasets</span></div></header><p class=\"notice\"><strong>Teaching model 04:</strong> A simplified formula evaluator, not a safety-rated digital twin. Validate all state ranges and reference conditions. Never use these outputs to approve machinery.</p><article class=\"model-panel\"><h2>Pump electrical power</h2><p class=\"small\">Overall efficiency here includes mechanical and motor losses.</p><div class=\"fields\"><label>Volume flow (m\u00b3/s)<input type=\"number\" id=\"Q\" value=\"0.035\" min=\"0.001\" max=\"1\" step=\"any\"></label><label>Head (m)<input type=\"number\" id=\"H\" value=\"25\" min=\"1\" max=\"500\" step=\"any\"></label><label>Overall efficiency (0\u20131)<input type=\"number\" id=\"eta\" value=\"0.7\" min=\"0.05\" max=\"1\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\">\u2014</div><div id=\"result\" class=\"small\">Change any input to recalculate.</div></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 650 190\" role=\"img\" aria-label=\"Illustrative output envelope\"></svg><p class=\"small\">The blue line illustrates scalar output \u00b130% around the computed value. It is not a validated performance curve. Check limits before interpreting signs.</p></article>",
    init: function(card) {
      try {
const __modelIndex=4;
function calculate(){
 const Q=Number(card.querySelector("#" + 'Q'.replace(/^#/, "")).value);
const H=Number(card.querySelector("#" + 'H'.replace(/^#/, "")).value);
const eta=Number(card.querySelector("#" + 'eta'.replace(/^#/, "")).value);
 const ok=(Number.isFinite(Q) && Q>=0.001 && Q<=1 && Number.isFinite(H) && H>=1 && H<=500 && Number.isFinite(eta) && eta>=0.05 && eta<=1);
 if(!ok){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Invalid values or model assumptions. Check input limits and required state order.';card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent='—';return;}
 const result=(1000*9.81*Q*H/eta/1000);
 if(!Number.isFinite(result)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Undefined at these conditions.';return;}
 card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent=result.toLocaleString('en-US',{maximumFractionDigits:4})+' kW';
 card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Overall efficiency here includes mechanical and motor losses.';
 const vals=[];
 const base=result;
 for(let j=0;j<31;j++){
   let fac=0.7+j*0.02;
   vals.push([j/30,base*fac]);
 }
 const chart=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const Y=vals.map(v=>v[1]);const lo=Math.min(...Y,0), hi=Math.max(...Y,0);const range=Math.max(1e-10,hi-lo);
 let poly=vals.map(v=>`${25+600*v[0]},${170-145*(v[1]-lo)/range}`).join(' ');
 chart.innerHTML=`<line x1="25" y1="170" x2="625" y2="170" stroke="#a0b5c5"/><line x1="25" y1="20" x2="25" y2="170" stroke="#a0b5c5"/><polyline fill="none" stroke="#176b96" stroke-width="3" points="${poly}"/><circle cx="325" cy="${170-145*(base-lo)/range}" r="5" fill="#d46f37"/><text x="30" y="17" font-size="11" fill="#415d76">Illustrative ±30% output envelope, not a physical parameter sweep</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',calculate));calculate();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 5,
    unit: 3,
    html: "<header class=\"hero\"><div class=\"eyebrow\">MECHANICAL ENGINEERING \u00b7 BOOK 15</div><h3>Axial stage flow coefficient</h3><p class=\"subtitle\">Offline, mobile-friendly teaching content \u00b7 unreviewed educational draft.</p><div class=\"metrics\"><span>8 units</span><span>40 lessons</span><span>16 simulators</span><span>8 datasets</span></div></header><p class=\"notice\"><strong>Teaching model 05:</strong> A simplified formula evaluator, not a safety-rated digital twin. Validate all state ranges and reference conditions. Never use these outputs to approve machinery.</p><article class=\"model-panel\"><h2>Axial stage flow coefficient</h2><p class=\"small\">Uses representative radius; spanwise variation ignored.</p><div class=\"fields\"><label>Axial velocity (m/s)<input type=\"number\" id=\"vx\" value=\"90\" min=\"0\" max=\"400\" step=\"any\"></label><label>Blade speed (m/s)<input type=\"number\" id=\"u\" value=\"180\" min=\"1\" max=\"600\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\">\u2014</div><div id=\"result\" class=\"small\">Change any input to recalculate.</div></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 650 190\" role=\"img\" aria-label=\"Illustrative output envelope\"></svg><p class=\"small\">The blue line illustrates scalar output \u00b130% around the computed value. It is not a validated performance curve. Check limits before interpreting signs.</p></article>",
    init: function(card) {
      try {
const __modelIndex=5;
function calculate(){
 const vx=Number(card.querySelector("#" + 'vx'.replace(/^#/, "")).value);
const u=Number(card.querySelector("#" + 'u'.replace(/^#/, "")).value);
 const ok=(Number.isFinite(vx) && vx>=0 && vx<=400 && Number.isFinite(u) && u>=1 && u<=600);
 if(!ok){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Invalid values or model assumptions. Check input limits and required state order.';card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent='—';return;}
 const result=(vx/u);
 if(!Number.isFinite(result)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Undefined at these conditions.';return;}
 card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent=result.toLocaleString('en-US',{maximumFractionDigits:4})+' –';
 card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Uses representative radius; spanwise variation ignored.';
 const vals=[];
 const base=result;
 for(let j=0;j<31;j++){
   let fac=0.7+j*0.02;
   vals.push([j/30,base*fac]);
 }
 const chart=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const Y=vals.map(v=>v[1]);const lo=Math.min(...Y,0), hi=Math.max(...Y,0);const range=Math.max(1e-10,hi-lo);
 let poly=vals.map(v=>`${25+600*v[0]},${170-145*(v[1]-lo)/range}`).join(' ');
 chart.innerHTML=`<line x1="25" y1="170" x2="625" y2="170" stroke="#a0b5c5"/><line x1="25" y1="20" x2="25" y2="170" stroke="#a0b5c5"/><polyline fill="none" stroke="#176b96" stroke-width="3" points="${poly}"/><circle cx="325" cy="${170-145*(base-lo)/range}" r="5" fill="#d46f37"/><text x="30" y="17" font-size="11" fill="#415d76">Illustrative ±30% output envelope, not a physical parameter sweep</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',calculate));calculate();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 6,
    unit: 3,
    html: "<header class=\"hero\"><div class=\"eyebrow\">MECHANICAL ENGINEERING \u00b7 BOOK 15</div><h3>Compressor isentropic efficiency</h3><p class=\"subtitle\">Offline, mobile-friendly teaching content \u00b7 unreviewed educational draft.</p><div class=\"metrics\"><span>8 units</span><span>40 lessons</span><span>16 simulators</span><span>8 datasets</span></div></header><p class=\"notice\"><strong>Teaching model 06:</strong> A simplified formula evaluator, not a safety-rated digital twin. Validate all state ranges and reference conditions. Never use these outputs to approve machinery.</p><article class=\"model-panel\"><h2>Compressor isentropic efficiency</h2><p class=\"small\">Only valid for positive temperature rise and air-like constant gamma; otherwise flagged.</p><div class=\"fields\"><label>Total pressure ratio<input type=\"number\" id=\"pi\" value=\"2.5\" min=\"1.001\" max=\"20\" step=\"any\"></label><label>Inlet total temperature (K)<input type=\"number\" id=\"t1\" value=\"300\" min=\"200\" max=\"1200\" step=\"any\"></label><label>Exit total temperature (K)<input type=\"number\" id=\"t2\" value=\"415\" min=\"201\" max=\"1900\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\">\u2014</div><div id=\"result\" class=\"small\">Change any input to recalculate.</div></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 650 190\" role=\"img\" aria-label=\"Illustrative output envelope\"></svg><p class=\"small\">The blue line illustrates scalar output \u00b130% around the computed value. It is not a validated performance curve. Check limits before interpreting signs.</p></article>",
    init: function(card) {
      try {
const __modelIndex=6;
function calculate(){
 const pi=Number(card.querySelector("#" + 'pi'.replace(/^#/, "")).value);
const t1=Number(card.querySelector("#" + 't1'.replace(/^#/, "")).value);
const t2=Number(card.querySelector("#" + 't2'.replace(/^#/, "")).value);
 const ok=(Number.isFinite(pi) && pi>=1.001 && pi<=20 && Number.isFinite(t1) && t1>=200 && t1<=1200 && Number.isFinite(t2) && t2>=201 && t2<=1900) && t2>t1 && (Math.pow(pi,(1.4-1)/1.4)-1)/(t2/t1-1)<=1;
 if(!ok){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Invalid values or model assumptions. Check input limits and required state order.';card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent='—';return;}
 const result=((Math.pow(pi,(1.4-1)/1.4)-1)/(t2/t1-1));
 if(!Number.isFinite(result)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Undefined at these conditions.';return;}
 card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent=result.toLocaleString('en-US',{maximumFractionDigits:4})+' –';
 card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Only valid for positive temperature rise and air-like constant gamma; otherwise flagged.';
 const vals=[];
 const base=result;
 for(let j=0;j<31;j++){
   let fac=0.7+j*0.02;
   vals.push([j/30,base*fac]);
 }
 const chart=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const Y=vals.map(v=>v[1]);const lo=Math.min(...Y,0), hi=Math.max(...Y,0);const range=Math.max(1e-10,hi-lo);
 let poly=vals.map(v=>`${25+600*v[0]},${170-145*(v[1]-lo)/range}`).join(' ');
 chart.innerHTML=`<line x1="25" y1="170" x2="625" y2="170" stroke="#a0b5c5"/><line x1="25" y1="20" x2="25" y2="170" stroke="#a0b5c5"/><polyline fill="none" stroke="#176b96" stroke-width="3" points="${poly}"/><circle cx="325" cy="${170-145*(base-lo)/range}" r="5" fill="#d46f37"/><text x="30" y="17" font-size="11" fill="#415d76">Illustrative ±30% output envelope, not a physical parameter sweep</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',calculate));calculate();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 7,
    unit: 4,
    html: "<header class=\"hero\"><div class=\"eyebrow\">MECHANICAL ENGINEERING \u00b7 BOOK 15</div><h3>Radial impeller tip specific work</h3><p class=\"subtitle\">Offline, mobile-friendly teaching content \u00b7 unreviewed educational draft.</p><div class=\"metrics\"><span>8 units</span><span>40 lessons</span><span>16 simulators</span><span>8 datasets</span></div></header><p class=\"notice\"><strong>Teaching model 07:</strong> A simplified formula evaluator, not a safety-rated digital twin. Validate all state ranges and reference conditions. Never use these outputs to approve machinery.</p><article class=\"model-panel\"><h2>Radial impeller tip specific work</h2><p class=\"small\">Real diffusers introduce entropy; ideal Euler work is not stage static pressure rise.</p><div class=\"fields\"><label>Exit blade speed (m/s)<input type=\"number\" id=\"u2\" value=\"300\" min=\"1\" max=\"700\" step=\"any\"></label><label>Exit whirl (m/s)<input type=\"number\" id=\"vt2\" value=\"210\" min=\"-500\" max=\"500\" step=\"any\"></label><label>Inlet blade speed (m/s)<input type=\"number\" id=\"u1\" value=\"90\" min=\"1\" max=\"400\" step=\"any\"></label><label>Inlet whirl (m/s)<input type=\"number\" id=\"vt1\" value=\"0\" min=\"-300\" max=\"300\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\">\u2014</div><div id=\"result\" class=\"small\">Change any input to recalculate.</div></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 650 190\" role=\"img\" aria-label=\"Illustrative output envelope\"></svg><p class=\"small\">The blue line illustrates scalar output \u00b130% around the computed value. It is not a validated performance curve. Check limits before interpreting signs.</p></article>",
    init: function(card) {
      try {
const __modelIndex=7;
function calculate(){
 const u2=Number(card.querySelector("#" + 'u2'.replace(/^#/, "")).value);
const vt2=Number(card.querySelector("#" + 'vt2'.replace(/^#/, "")).value);
const u1=Number(card.querySelector("#" + 'u1'.replace(/^#/, "")).value);
const vt1=Number(card.querySelector("#" + 'vt1'.replace(/^#/, "")).value);
 const ok=(Number.isFinite(u2) && u2>=1 && u2<=700 && Number.isFinite(vt2) && vt2>=-500 && vt2<=500 && Number.isFinite(u1) && u1>=1 && u1<=400 && Number.isFinite(vt1) && vt1>=-300 && vt1<=300);
 if(!ok){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Invalid values or model assumptions. Check input limits and required state order.';card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent='—';return;}
 const result=(u2*vt2-u1*vt1);
 if(!Number.isFinite(result)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Undefined at these conditions.';return;}
 card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent=result.toLocaleString('en-US',{maximumFractionDigits:4})+' J/kg';
 card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Real diffusers introduce entropy; ideal Euler work is not stage static pressure rise.';
 const vals=[];
 const base=result;
 for(let j=0;j<31;j++){
   let fac=0.7+j*0.02;
   vals.push([j/30,base*fac]);
 }
 const chart=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const Y=vals.map(v=>v[1]);const lo=Math.min(...Y,0), hi=Math.max(...Y,0);const range=Math.max(1e-10,hi-lo);
 let poly=vals.map(v=>`${25+600*v[0]},${170-145*(v[1]-lo)/range}`).join(' ');
 chart.innerHTML=`<line x1="25" y1="170" x2="625" y2="170" stroke="#a0b5c5"/><line x1="25" y1="20" x2="25" y2="170" stroke="#a0b5c5"/><polyline fill="none" stroke="#176b96" stroke-width="3" points="${poly}"/><circle cx="325" cy="${170-145*(base-lo)/range}" r="5" fill="#d46f37"/><text x="30" y="17" font-size="11" fill="#415d76">Illustrative ±30% output envelope, not a physical parameter sweep</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',calculate));calculate();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 8,
    unit: 4,
    html: "<header class=\"hero\"><div class=\"eyebrow\">MECHANICAL ENGINEERING \u00b7 BOOK 15</div><h3>Compressor corrected flow</h3><p class=\"subtitle\">Offline, mobile-friendly teaching content \u00b7 unreviewed educational draft.</p><div class=\"metrics\"><span>8 units</span><span>40 lessons</span><span>16 simulators</span><span>8 datasets</span></div></header><p class=\"notice\"><strong>Teaching model 08:</strong> A simplified formula evaluator, not a safety-rated digital twin. Validate all state ranges and reference conditions. Never use these outputs to approve machinery.</p><article class=\"model-panel\"><h2>Compressor corrected flow</h2><p class=\"small\">Reference T=288.15 K, p=101.325 kPa; do not treat as actual throughput.</p><div class=\"fields\"><label>Physical mass flow (kg/s)<input type=\"number\" id=\"m\" value=\"8\" min=\"0.1\" max=\"100\" step=\"any\"></label><label>Inlet total T (K)<input type=\"number\" id=\"t\" value=\"330\" min=\"150\" max=\"1500\" step=\"any\"></label><label>Inlet total p (kPa abs)<input type=\"number\" id=\"p\" value=\"95\" min=\"10\" max=\"1000\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\">\u2014</div><div id=\"result\" class=\"small\">Change any input to recalculate.</div></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 650 190\" role=\"img\" aria-label=\"Illustrative output envelope\"></svg><p class=\"small\">The blue line illustrates scalar output \u00b130% around the computed value. It is not a validated performance curve. Check limits before interpreting signs.</p></article>",
    init: function(card) {
      try {
const __modelIndex=8;
function calculate(){
 const m=Number(card.querySelector("#" + 'm'.replace(/^#/, "")).value);
const t=Number(card.querySelector("#" + 't'.replace(/^#/, "")).value);
const p=Number(card.querySelector("#" + 'p'.replace(/^#/, "")).value);
 const ok=(Number.isFinite(m) && m>=0.1 && m<=100 && Number.isFinite(t) && t>=150 && t<=1500 && Number.isFinite(p) && p>=10 && p<=1000);
 if(!ok){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Invalid values or model assumptions. Check input limits and required state order.';card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent='—';return;}
 const result=(m*Math.sqrt(t/288.15)/(p/101.325));
 if(!Number.isFinite(result)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Undefined at these conditions.';return;}
 card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent=result.toLocaleString('en-US',{maximumFractionDigits:4})+' kg/s (corr)';
 card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Reference T=288.15 K, p=101.325 kPa; do not treat as actual throughput.';
 const vals=[];
 const base=result;
 for(let j=0;j<31;j++){
   let fac=0.7+j*0.02;
   vals.push([j/30,base*fac]);
 }
 const chart=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const Y=vals.map(v=>v[1]);const lo=Math.min(...Y,0), hi=Math.max(...Y,0);const range=Math.max(1e-10,hi-lo);
 let poly=vals.map(v=>`${25+600*v[0]},${170-145*(v[1]-lo)/range}`).join(' ');
 chart.innerHTML=`<line x1="25" y1="170" x2="625" y2="170" stroke="#a0b5c5"/><line x1="25" y1="20" x2="25" y2="170" stroke="#a0b5c5"/><polyline fill="none" stroke="#176b96" stroke-width="3" points="${poly}"/><circle cx="325" cy="${170-145*(base-lo)/range}" r="5" fill="#d46f37"/><text x="30" y="17" font-size="11" fill="#415d76">Illustrative ±30% output envelope, not a physical parameter sweep</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',calculate));calculate();
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 9,
    unit: 5,
    html: "<header class=\"hero\"><div class=\"eyebrow\">MECHANICAL ENGINEERING \u00b7 BOOK 15</div><h3>Turbine fluid power</h3><p class=\"subtitle\">Offline, mobile-friendly teaching content \u00b7 unreviewed educational draft.</p><div class=\"metrics\"><span>8 units</span><span>40 lessons</span><span>16 simulators</span><span>8 datasets</span></div></header><p class=\"notice\"><strong>Teaching model 09:</strong> A simplified formula evaluator, not a safety-rated digital twin. Validate all state ranges and reference conditions. Never use these outputs to approve machinery.</p><article class=\"model-panel\"><h2>Turbine fluid power</h2><p class=\"small\">Positive power extracted before shaft mechanical losses.</p><div class=\"fields\"><label>Mass flow (kg/s)<input type=\"number\" id=\"m\" value=\"18\" min=\"0.1\" max=\"150\" step=\"any\"></label><label>Mean cp (kJ/kg\u00b7K)<input type=\"number\" id=\"cp\" value=\"1.15\" min=\"0.5\" max=\"4\" step=\"any\"></label><label>Total temperature drop (K)<input type=\"number\" id=\"dt\" value=\"210\" min=\"0\" max=\"1000\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\">\u2014</div><div id=\"result\" class=\"small\">Change any input to recalculate.</div></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 650 190\" role=\"img\" aria-label=\"Illustrative output envelope\"></svg><p class=\"small\">The blue line illustrates scalar output \u00b130% around the computed value. It is not a validated performance curve. Check limits before interpreting signs.</p></article>",
    init: function(card) {
      try {
const __modelIndex=9;
function calculate(){
 const m=Number(card.querySelector("#" + 'm'.replace(/^#/, "")).value);
const cp=Number(card.querySelector("#" + 'cp'.replace(/^#/, "")).value);
const dt=Number(card.querySelector("#" + 'dt'.replace(/^#/, "")).value);
 const ok=(Number.isFinite(m) && m>=0.1 && m<=150 && Number.isFinite(cp) && cp>=0.5 && cp<=4 && Number.isFinite(dt) && dt>=0 && dt<=1000);
 if(!ok){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Invalid values or model assumptions. Check input limits and required state order.';card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent='—';return;}
 const result=(m*cp*dt);
 if(!Number.isFinite(result)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Undefined at these conditions.';return;}
 card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent=result.toLocaleString('en-US',{maximumFractionDigits:4})+' kW';
 card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Positive power extracted before shaft mechanical losses.';
 const vals=[];
 const base=result;
 for(let j=0;j<31;j++){
   let fac=0.7+j*0.02;
   vals.push([j/30,base*fac]);
 }
 const chart=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const Y=vals.map(v=>v[1]);const lo=Math.min(...Y,0), hi=Math.max(...Y,0);const range=Math.max(1e-10,hi-lo);
 let poly=vals.map(v=>`${25+600*v[0]},${170-145*(v[1]-lo)/range}`).join(' ');
 chart.innerHTML=`<line x1="25" y1="170" x2="625" y2="170" stroke="#a0b5c5"/><line x1="25" y1="20" x2="25" y2="170" stroke="#a0b5c5"/><polyline fill="none" stroke="#176b96" stroke-width="3" points="${poly}"/><circle cx="325" cy="${170-145*(base-lo)/range}" r="5" fill="#d46f37"/><text x="30" y="17" font-size="11" fill="#415d76">Illustrative ±30% output envelope, not a physical parameter sweep</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',calculate));calculate();
      } catch (err) {
        console.warn('Sim init error in model 9:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 10,
    unit: 5,
    html: "<header class=\"hero\"><div class=\"eyebrow\">MECHANICAL ENGINEERING \u00b7 BOOK 15</div><h3>Turbine efficiency</h3><p class=\"subtitle\">Offline, mobile-friendly teaching content \u00b7 unreviewed educational draft.</p><div class=\"metrics\"><span>8 units</span><span>40 lessons</span><span>16 simulators</span><span>8 datasets</span></div></header><p class=\"notice\"><strong>Teaching model 10:</strong> A simplified formula evaluator, not a safety-rated digital twin. Validate all state ranges and reference conditions. Never use these outputs to approve machinery.</p><article class=\"model-panel\"><h2>Turbine efficiency</h2><p class=\"small\">Constant-cp approximation; station pressure ratio held fixed.</p><div class=\"fields\"><label>Inlet total T (K)<input type=\"number\" id=\"tin\" value=\"1100\" min=\"300\" max=\"2000\" step=\"any\"></label><label>Actual exit total T (K)<input type=\"number\" id=\"tout\" value=\"900\" min=\"100\" max=\"1900\" step=\"any\"></label><label>Isentropic exit total T (K)<input type=\"number\" id=\"ts\" value=\"865\" min=\"100\" max=\"1900\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\">\u2014</div><div id=\"result\" class=\"small\">Change any input to recalculate.</div></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 650 190\" role=\"img\" aria-label=\"Illustrative output envelope\"></svg><p class=\"small\">The blue line illustrates scalar output \u00b130% around the computed value. It is not a validated performance curve. Check limits before interpreting signs.</p></article>",
    init: function(card) {
      try {
const __modelIndex=10;
function calculate(){
 const tin=Number(card.querySelector("#" + 'tin'.replace(/^#/, "")).value);
const tout=Number(card.querySelector("#" + 'tout'.replace(/^#/, "")).value);
const ts=Number(card.querySelector("#" + 'ts'.replace(/^#/, "")).value);
 const ok=(Number.isFinite(tin) && tin>=300 && tin<=2000 && Number.isFinite(tout) && tout>=100 && tout<=1900 && Number.isFinite(ts) && ts>=100 && ts<=1900) && tin>tout && tout>=ts && tin>ts;
 if(!ok){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Invalid values or model assumptions. Check input limits and required state order.';card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent='—';return;}
 const result=((tin-tout)/(tin-ts));
 if(!Number.isFinite(result)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Undefined at these conditions.';return;}
 card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent=result.toLocaleString('en-US',{maximumFractionDigits:4})+' –';
 card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Constant-cp approximation; station pressure ratio held fixed.';
 const vals=[];
 const base=result;
 for(let j=0;j<31;j++){
   let fac=0.7+j*0.02;
   vals.push([j/30,base*fac]);
 }
 const chart=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const Y=vals.map(v=>v[1]);const lo=Math.min(...Y,0), hi=Math.max(...Y,0);const range=Math.max(1e-10,hi-lo);
 let poly=vals.map(v=>`${25+600*v[0]},${170-145*(v[1]-lo)/range}`).join(' ');
 chart.innerHTML=`<line x1="25" y1="170" x2="625" y2="170" stroke="#a0b5c5"/><line x1="25" y1="20" x2="25" y2="170" stroke="#a0b5c5"/><polyline fill="none" stroke="#176b96" stroke-width="3" points="${poly}"/><circle cx="325" cy="${170-145*(base-lo)/range}" r="5" fill="#d46f37"/><text x="30" y="17" font-size="11" fill="#415d76">Illustrative ±30% output envelope, not a physical parameter sweep</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',calculate));calculate();
      } catch (err) {
        console.warn('Sim init error in model 10:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 11,
    unit: 6,
    html: "<header class=\"hero\"><div class=\"eyebrow\">MECHANICAL ENGINEERING \u00b7 BOOK 15</div><h3>Net hydraulic power</h3><p class=\"subtitle\">Offline, mobile-friendly teaching content \u00b7 unreviewed educational draft.</p><div class=\"metrics\"><span>8 units</span><span>40 lessons</span><span>16 simulators</span><span>8 datasets</span></div></header><p class=\"notice\"><strong>Teaching model 11:</strong> A simplified formula evaluator, not a safety-rated digital twin. Validate all state ranges and reference conditions. Never use these outputs to approve machinery.</p><article class=\"model-panel\"><h2>Net hydraulic power</h2><p class=\"small\">Hydraulic head after penstock losses; eco bypass excluded from Q.</p><div class=\"fields\"><label>Flow rate (m\u00b3/s)<input type=\"number\" id=\"Q\" value=\"2.4\" min=\"0.001\" max=\"200\" step=\"any\"></label><label>Net head (m)<input type=\"number\" id=\"H\" value=\"28\" min=\"0.1\" max=\"900\" step=\"any\"></label><label>Overall efficiency (0\u20131)<input type=\"number\" id=\"eta\" value=\"0.87\" min=\"0.05\" max=\"1\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\">\u2014</div><div id=\"result\" class=\"small\">Change any input to recalculate.</div></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 650 190\" role=\"img\" aria-label=\"Illustrative output envelope\"></svg><p class=\"small\">The blue line illustrates scalar output \u00b130% around the computed value. It is not a validated performance curve. Check limits before interpreting signs.</p></article>",
    init: function(card) {
      try {
const __modelIndex=11;
function calculate(){
 const Q=Number(card.querySelector("#" + 'Q'.replace(/^#/, "")).value);
const H=Number(card.querySelector("#" + 'H'.replace(/^#/, "")).value);
const eta=Number(card.querySelector("#" + 'eta'.replace(/^#/, "")).value);
 const ok=(Number.isFinite(Q) && Q>=0.001 && Q<=200 && Number.isFinite(H) && H>=0.1 && H<=900 && Number.isFinite(eta) && eta>=0.05 && eta<=1);
 if(!ok){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Invalid values or model assumptions. Check input limits and required state order.';card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent='—';return;}
 const result=(1000*9.81*Q*H*eta/1000);
 if(!Number.isFinite(result)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Undefined at these conditions.';return;}
 card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent=result.toLocaleString('en-US',{maximumFractionDigits:4})+' kW';
 card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Hydraulic head after penstock losses; eco bypass excluded from Q.';
 const vals=[];
 const base=result;
 for(let j=0;j<31;j++){
   let fac=0.7+j*0.02;
   vals.push([j/30,base*fac]);
 }
 const chart=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const Y=vals.map(v=>v[1]);const lo=Math.min(...Y,0), hi=Math.max(...Y,0);const range=Math.max(1e-10,hi-lo);
 let poly=vals.map(v=>`${25+600*v[0]},${170-145*(v[1]-lo)/range}`).join(' ');
 chart.innerHTML=`<line x1="25" y1="170" x2="625" y2="170" stroke="#a0b5c5"/><line x1="25" y1="20" x2="25" y2="170" stroke="#a0b5c5"/><polyline fill="none" stroke="#176b96" stroke-width="3" points="${poly}"/><circle cx="325" cy="${170-145*(base-lo)/range}" r="5" fill="#d46f37"/><text x="30" y="17" font-size="11" fill="#415d76">Illustrative ±30% output envelope, not a physical parameter sweep</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',calculate));calculate();
      } catch (err) {
        console.warn('Sim init error in model 11:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 12,
    unit: 6,
    html: "<header class=\"hero\"><div class=\"eyebrow\">MECHANICAL ENGINEERING \u00b7 BOOK 15</div><h3>Jet speed from net head</h3><p class=\"subtitle\">Offline, mobile-friendly teaching content \u00b7 unreviewed educational draft.</p><div class=\"metrics\"><span>8 units</span><span>40 lessons</span><span>16 simulators</span><span>8 datasets</span></div></header><p class=\"notice\"><strong>Teaching model 12:</strong> A simplified formula evaluator, not a safety-rated digital twin. Validate all state ranges and reference conditions. Never use these outputs to approve machinery.</p><article class=\"model-panel\"><h2>Jet speed from net head</h2><p class=\"small\">Impulse turbine jet before runner speed; loss coefficient illustrative.</p><div class=\"fields\"><label>Head (m)<input type=\"number\" id=\"H\" value=\"80\" min=\"0.1\" max=\"900\" step=\"any\"></label><label>Nozzle velocity coefficient<input type=\"number\" id=\"cv\" value=\"0.97\" min=\"0.1\" max=\"1\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\">\u2014</div><div id=\"result\" class=\"small\">Change any input to recalculate.</div></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 650 190\" role=\"img\" aria-label=\"Illustrative output envelope\"></svg><p class=\"small\">The blue line illustrates scalar output \u00b130% around the computed value. It is not a validated performance curve. Check limits before interpreting signs.</p></article>",
    init: function(card) {
      try {
const __modelIndex=12;
function calculate(){
 const H=Number(card.querySelector("#" + 'H'.replace(/^#/, "")).value);
const cv=Number(card.querySelector("#" + 'cv'.replace(/^#/, "")).value);
 const ok=(Number.isFinite(H) && H>=0.1 && H<=900 && Number.isFinite(cv) && cv>=0.1 && cv<=1);
 if(!ok){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Invalid values or model assumptions. Check input limits and required state order.';card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent='—';return;}
 const result=(cv*Math.sqrt(2*9.81*H));
 if(!Number.isFinite(result)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Undefined at these conditions.';return;}
 card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent=result.toLocaleString('en-US',{maximumFractionDigits:4})+' m/s';
 card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Impulse turbine jet before runner speed; loss coefficient illustrative.';
 const vals=[];
 const base=result;
 for(let j=0;j<31;j++){
   let fac=0.7+j*0.02;
   vals.push([j/30,base*fac]);
 }
 const chart=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const Y=vals.map(v=>v[1]);const lo=Math.min(...Y,0), hi=Math.max(...Y,0);const range=Math.max(1e-10,hi-lo);
 let poly=vals.map(v=>`${25+600*v[0]},${170-145*(v[1]-lo)/range}`).join(' ');
 chart.innerHTML=`<line x1="25" y1="170" x2="625" y2="170" stroke="#a0b5c5"/><line x1="25" y1="20" x2="25" y2="170" stroke="#a0b5c5"/><polyline fill="none" stroke="#176b96" stroke-width="3" points="${poly}"/><circle cx="325" cy="${170-145*(base-lo)/range}" r="5" fill="#d46f37"/><text x="30" y="17" font-size="11" fill="#415d76">Illustrative ±30% output envelope, not a physical parameter sweep</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',calculate));calculate();
      } catch (err) {
        console.warn('Sim init error in model 12:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 13,
    unit: 7,
    html: "<header class=\"hero\"><div class=\"eyebrow\">MECHANICAL ENGINEERING \u00b7 BOOK 15</div><h3>Rotor unbalance force</h3><p class=\"subtitle\">Offline, mobile-friendly teaching content \u00b7 unreviewed educational draft.</p><div class=\"metrics\"><span>8 units</span><span>40 lessons</span><span>16 simulators</span><span>8 datasets</span></div></header><p class=\"notice\"><strong>Teaching model 13:</strong> A simplified formula evaluator, not a safety-rated digital twin. Validate all state ranges and reference conditions. Never use these outputs to approve machinery.</p><article class=\"model-panel\"><h2>Rotor unbalance force</h2><p class=\"small\">Simple rigid eccentric mass; not a safe operating speed decision.</p><div class=\"fields\"><label>Eccentric mass (kg)<input type=\"number\" id=\"m\" value=\"0.02\" min=\"1e-05\" max=\"10\" step=\"any\"></label><label>Eccentricity (mm)<input type=\"number\" id=\"e\" value=\"1\" min=\"0.001\" max=\"100\" step=\"any\"></label><label>Rotational speed (rpm)<input type=\"number\" id=\"n\" value=\"3000\" min=\"0\" max=\"30000\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\">\u2014</div><div id=\"result\" class=\"small\">Change any input to recalculate.</div></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 650 190\" role=\"img\" aria-label=\"Illustrative output envelope\"></svg><p class=\"small\">The blue line illustrates scalar output \u00b130% around the computed value. It is not a validated performance curve. Check limits before interpreting signs.</p></article>",
    init: function(card) {
      try {
const __modelIndex=13;
function calculate(){
 const m=Number(card.querySelector("#" + 'm'.replace(/^#/, "")).value);
const e=Number(card.querySelector("#" + 'e'.replace(/^#/, "")).value);
const n=Number(card.querySelector("#" + 'n'.replace(/^#/, "")).value);
 const ok=(Number.isFinite(m) && m>=1e-05 && m<=10 && Number.isFinite(e) && e>=0.001 && e<=100 && Number.isFinite(n) && n>=0 && n<=30000);
 if(!ok){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Invalid values or model assumptions. Check input limits and required state order.';card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent='—';return;}
 const result=(m*(e/1000)*Math.pow(2*Math.PI*n/60,2));
 if(!Number.isFinite(result)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Undefined at these conditions.';return;}
 card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent=result.toLocaleString('en-US',{maximumFractionDigits:4})+' N';
 card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Simple rigid eccentric mass; not a safe operating speed decision.';
 const vals=[];
 const base=result;
 for(let j=0;j<31;j++){
   let fac=0.7+j*0.02;
   vals.push([j/30,base*fac]);
 }
 const chart=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const Y=vals.map(v=>v[1]);const lo=Math.min(...Y,0), hi=Math.max(...Y,0);const range=Math.max(1e-10,hi-lo);
 let poly=vals.map(v=>`${25+600*v[0]},${170-145*(v[1]-lo)/range}`).join(' ');
 chart.innerHTML=`<line x1="25" y1="170" x2="625" y2="170" stroke="#a0b5c5"/><line x1="25" y1="20" x2="25" y2="170" stroke="#a0b5c5"/><polyline fill="none" stroke="#176b96" stroke-width="3" points="${poly}"/><circle cx="325" cy="${170-145*(base-lo)/range}" r="5" fill="#d46f37"/><text x="30" y="17" font-size="11" fill="#415d76">Illustrative ±30% output envelope, not a physical parameter sweep</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',calculate));calculate();
      } catch (err) {
        console.warn('Sim init error in model 13:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 14,
    unit: 7,
    html: "<header class=\"hero\"><div class=\"eyebrow\">MECHANICAL ENGINEERING \u00b7 BOOK 15</div><h3>Simple critical speed</h3><p class=\"subtitle\">Offline, mobile-friendly teaching content \u00b7 unreviewed educational draft.</p><div class=\"metrics\"><span>8 units</span><span>40 lessons</span><span>16 simulators</span><span>8 datasets</span></div></header><p class=\"notice\"><strong>Teaching model 14:</strong> A simplified formula evaluator, not a safety-rated digital twin. Validate all state ranges and reference conditions. Never use these outputs to approve machinery.</p><article class=\"model-panel\"><h2>Simple critical speed</h2><p class=\"small\">Single-degree-of-freedom estimate, not rotor-bearing certification.</p><div class=\"fields\"><label>Effective stiffness (N/m)<input type=\"number\" id=\"k\" value=\"2000000\" min=\"100\" max=\"100000000.0\" step=\"any\"></label><label>Equivalent mass (kg)<input type=\"number\" id=\"m\" value=\"50\" min=\"0.1\" max=\"10000\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\">\u2014</div><div id=\"result\" class=\"small\">Change any input to recalculate.</div></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 650 190\" role=\"img\" aria-label=\"Illustrative output envelope\"></svg><p class=\"small\">The blue line illustrates scalar output \u00b130% around the computed value. It is not a validated performance curve. Check limits before interpreting signs.</p></article>",
    init: function(card) {
      try {
const __modelIndex=14;
function calculate(){
 const k=Number(card.querySelector("#" + 'k'.replace(/^#/, "")).value);
const m=Number(card.querySelector("#" + 'm'.replace(/^#/, "")).value);
 const ok=(Number.isFinite(k) && k>=100 && k<=100000000.0 && Number.isFinite(m) && m>=0.1 && m<=10000);
 if(!ok){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Invalid values or model assumptions. Check input limits and required state order.';card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent='—';return;}
 const result=(Math.sqrt(k/m)*60/(2*Math.PI));
 if(!Number.isFinite(result)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Undefined at these conditions.';return;}
 card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent=result.toLocaleString('en-US',{maximumFractionDigits:4})+' rpm';
 card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Single-degree-of-freedom estimate, not rotor-bearing certification.';
 const vals=[];
 const base=result;
 for(let j=0;j<31;j++){
   let fac=0.7+j*0.02;
   vals.push([j/30,base*fac]);
 }
 const chart=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const Y=vals.map(v=>v[1]);const lo=Math.min(...Y,0), hi=Math.max(...Y,0);const range=Math.max(1e-10,hi-lo);
 let poly=vals.map(v=>`${25+600*v[0]},${170-145*(v[1]-lo)/range}`).join(' ');
 chart.innerHTML=`<line x1="25" y1="170" x2="625" y2="170" stroke="#a0b5c5"/><line x1="25" y1="20" x2="25" y2="170" stroke="#a0b5c5"/><polyline fill="none" stroke="#176b96" stroke-width="3" points="${poly}"/><circle cx="325" cy="${170-145*(base-lo)/range}" r="5" fill="#d46f37"/><text x="30" y="17" font-size="11" fill="#415d76">Illustrative ±30% output envelope, not a physical parameter sweep</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',calculate));calculate();
      } catch (err) {
        console.warn('Sim init error in model 14:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 15,
    unit: 8,
    html: "<header class=\"hero\"><div class=\"eyebrow\">MECHANICAL ENGINEERING \u00b7 BOOK 15</div><h3>Flow and head uncertainty</h3><p class=\"subtitle\">Offline, mobile-friendly teaching content \u00b7 unreviewed educational draft.</p><div class=\"metrics\"><span>8 units</span><span>40 lessons</span><span>16 simulators</span><span>8 datasets</span></div></header><p class=\"notice\"><strong>Teaching model 15:</strong> A simplified formula evaluator, not a safety-rated digital twin. Validate all state ranges and reference conditions. Never use these outputs to approve machinery.</p><article class=\"model-panel\"><h2>Flow and head uncertainty</h2><p class=\"small\">Independent uncertainty only; ignores correlations.</p><div class=\"fields\"><label>Flow relative std uncertainty (%)<input type=\"number\" id=\"uf\" value=\"2\" min=\"0\" max=\"20\" step=\"any\"></label><label>Head relative std uncertainty (%)<input type=\"number\" id=\"uh\" value=\"1\" min=\"0\" max=\"20\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\">\u2014</div><div id=\"result\" class=\"small\">Change any input to recalculate.</div></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 650 190\" role=\"img\" aria-label=\"Illustrative output envelope\"></svg><p class=\"small\">The blue line illustrates scalar output \u00b130% around the computed value. It is not a validated performance curve. Check limits before interpreting signs.</p></article>",
    init: function(card) {
      try {
const __modelIndex=15;
function calculate(){
 const uf=Number(card.querySelector("#" + 'uf'.replace(/^#/, "")).value);
const uh=Number(card.querySelector("#" + 'uh'.replace(/^#/, "")).value);
 const ok=(Number.isFinite(uf) && uf>=0 && uf<=20 && Number.isFinite(uh) && uh>=0 && uh<=20);
 if(!ok){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Invalid values or model assumptions. Check input limits and required state order.';card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent='—';return;}
 const result=(Math.sqrt(uf*uf+uh*uh));
 if(!Number.isFinite(result)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Undefined at these conditions.';return;}
 card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent=result.toLocaleString('en-US',{maximumFractionDigits:4})+' %';
 card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Independent uncertainty only; ignores correlations.';
 const vals=[];
 const base=result;
 for(let j=0;j<31;j++){
   let fac=0.7+j*0.02;
   vals.push([j/30,base*fac]);
 }
 const chart=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const Y=vals.map(v=>v[1]);const lo=Math.min(...Y,0), hi=Math.max(...Y,0);const range=Math.max(1e-10,hi-lo);
 let poly=vals.map(v=>`${25+600*v[0]},${170-145*(v[1]-lo)/range}`).join(' ');
 chart.innerHTML=`<line x1="25" y1="170" x2="625" y2="170" stroke="#a0b5c5"/><line x1="25" y1="20" x2="25" y2="170" stroke="#a0b5c5"/><polyline fill="none" stroke="#176b96" stroke-width="3" points="${poly}"/><circle cx="325" cy="${170-145*(base-lo)/range}" r="5" fill="#d46f37"/><text x="30" y="17" font-size="11" fill="#415d76">Illustrative ±30% output envelope, not a physical parameter sweep</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',calculate));calculate();
      } catch (err) {
        console.warn('Sim init error in model 15:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 16,
    unit: 8,
    html: "<header class=\"hero\"><div class=\"eyebrow\">MECHANICAL ENGINEERING \u00b7 BOOK 15</div><h3>Annual auxiliary energy</h3><p class=\"subtitle\">Offline, mobile-friendly teaching content \u00b7 unreviewed educational draft.</p><div class=\"metrics\"><span>8 units</span><span>40 lessons</span><span>16 simulators</span><span>8 datasets</span></div></header><p class=\"notice\"><strong>Teaching model 16:</strong> A simplified formula evaluator, not a safety-rated digital twin. Validate all state ranges and reference conditions. Never use these outputs to approve machinery.</p><article class=\"model-panel\"><h2>Annual auxiliary energy</h2><p class=\"small\">Annualized single duty point; includes no discounting or repairs.</p><div class=\"fields\"><label>Mean auxiliary load (kW)<input type=\"number\" id=\"P\" value=\"12\" min=\"0\" max=\"1000\" step=\"any\"></label><label>Operating hours/year<input type=\"number\" id=\"h\" value=\"5000\" min=\"0\" max=\"8760\" step=\"any\"></label><label>Electricity tariff (USD/kWh)<input type=\"number\" id=\"tariff\" value=\"0.12\" min=\"0\" max=\"5\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\">\u2014</div><div id=\"result\" class=\"small\">Change any input to recalculate.</div></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 650 190\" role=\"img\" aria-label=\"Illustrative output envelope\"></svg><p class=\"small\">The blue line illustrates scalar output \u00b130% around the computed value. It is not a validated performance curve. Check limits before interpreting signs.</p></article>",
    init: function(card) {
      try {
const __modelIndex=16;
function calculate(){
 const P=Number(card.querySelector("#" + 'P'.replace(/^#/, "")).value);
const h=Number(card.querySelector("#" + 'h'.replace(/^#/, "")).value);
const tariff=Number(card.querySelector("#" + 'tariff'.replace(/^#/, "")).value);
 const ok=(Number.isFinite(P) && P>=0 && P<=1000 && Number.isFinite(h) && h>=0 && h<=8760 && Number.isFinite(tariff) && tariff>=0 && tariff<=5);
 if(!ok){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Invalid values or model assumptions. Check input limits and required state order.';card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent='—';return;}
 const result=(P*h*tariff);
 if(!Number.isFinite(result)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Undefined at these conditions.';return;}
 card.querySelector("#" + 'metric'.replace(/^#/, "")).textContent=result.toLocaleString('en-US',{maximumFractionDigits:4})+' USD/year';
 card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Annualized single duty point; includes no discounting or repairs.';
 const vals=[];
 const base=result;
 for(let j=0;j<31;j++){
   let fac=0.7+j*0.02;
   vals.push([j/30,base*fac]);
 }
 const chart=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const Y=vals.map(v=>v[1]);const lo=Math.min(...Y,0), hi=Math.max(...Y,0);const range=Math.max(1e-10,hi-lo);
 let poly=vals.map(v=>`${25+600*v[0]},${170-145*(v[1]-lo)/range}`).join(' ');
 chart.innerHTML=`<line x1="25" y1="170" x2="625" y2="170" stroke="#a0b5c5"/><line x1="25" y1="20" x2="25" y2="170" stroke="#a0b5c5"/><polyline fill="none" stroke="#176b96" stroke-width="3" points="${poly}"/><circle cx="325" cy="${170-145*(base-lo)/range}" r="5" fill="#d46f37"/><text x="30" y="17" font-size="11" fill="#415d76">Illustrative ±30% output envelope, not a physical parameter sweep</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',calculate));calculate();
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
