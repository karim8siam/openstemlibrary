/* engineering-reliability-and-maintenance Interactive Simulation Suite */
(function(window) {
  'use strict';

  var OPENSTEM_SIM_MODELS = [];

  OPENSTEM_SIM_MODELS.push({
    idx: 1,
    unit: 1,
    html: "<div class=\"hero\"><div class=\"eyebrow\">Interactive model 01 / Educational demonstration</div><h3>Exponential mission reliability</h3><p class=\"subtitle\">Modify assumptions and inspect how the idealized result changes.</p></div><p class=\"notice\">Not certified engineering software. Do not rely on this calculator for safety-critical or operational decisions.</p><div class=\"card\"><h2>Inputs</h2><div class=\"inputs\"><div class=\"input\"><label for=\"rate\">Failure intensity \u03bb (per hour)</label><input aria-label=\"Failure intensity \u03bb (per hour)\" type=\"number\" id=\"rate\" value=\"0.0002\" min=\"0\" max=\"0.004\" step=\"0.0001\"><input aria-label=\"Slide Failure intensity \u03bb (per hour)\" id=\"slider-rate\" type=\"range\" value=\"0.0002\" min=\"0\" max=\"0.004\" step=\"0.0001\"></div><div class=\"input\"><label for=\"time\">Mission duration (hours)</label><input aria-label=\"Mission duration (hours)\" type=\"number\" id=\"time\" value=\"1000\" min=\"0\" max=\"10000\" step=\"100\"><input aria-label=\"Slide Mission duration (hours)\" id=\"slider-time\" type=\"range\" value=\"1000\" min=\"0\" max=\"10000\" step=\"100\"></div></div><p class=\"math\">R(t)=exp(-\u03bbt)</p><div class=\"result\"><div class=\"small\">Calculated output</div><div class=\"value\" id=\"result\" aria-live=\"polite\">Loading</div></div><div class=\"plot\"><svg viewBox=\"0 0 620 220\" aria-label=\"Model sensitivity chart\" role=\"img\"><path d=\"M20 25V190H600\" fill=\"none\" stroke=\"#adbfc1\" stroke-width=\"1.5\"/><path id=\"curve\" d=\"M20 170L600 30\" fill=\"none\" stroke=\"#12796e\" stroke-width=\"3\" stroke-linecap=\"round\"/></svg><div id=\"x-label\" class=\"small\"></div><div id=\"y-label\" class=\"small\"></div></div></div><div class=\"hint\"><strong>Model limitation:</strong> Assumes independent first-failure time and constant hazard. A lifetime distribution, not a repairable-plant availability prediction.</div><p class=\"small\">Trend plot changes the first input while holding the others constant. All values are illustrative and user-controlled.</p>",
    init: function(card) {
      try {
"use strict";
const names=["rate", "time"];
function calc(p){return Math.exp(-p.rate*p.time);}
function format(v){return (100*v).toFixed(2)+'%';}
function read(){let p={};p.rate=parseFloat(card.querySelector("#" + 'rate'.replace(/^#/, "")).value);p.time=parseFloat(card.querySelector("#" + 'time'.replace(/^#/, "")).value);return p;}
function update(){let p=read();if(!(Number.isFinite(p.rate) && p.rate>=0 && p.rate<=0.004&&Number.isFinite(p.time) && p.time>=0 && p.time<=10000)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Input outside permitted range';return;}let v=calc(p);card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?format(v):'Model not defined at this input';
const xmin=0,xmax=0.004;let pts=[];for(let n=0;n<=80;n++){let x=xmin+(xmax-xmin)*n/80;let q={...p};q['rate']=x;let y=calc(q);if(Number.isFinite(y))pts.push([x,y]);}
if(pts.length>1){let ymin=Math.min(...pts.map(a=>a[1])),ymax=Math.max(...pts.map(a=>a[1]));if(Math.abs(ymax-ymin)<1e-12)ymax=ymin+1;let path=pts.map((a,n)=>`${n===0?'M':'L'}${(a[0]-xmin)/(xmax-xmin)*580+20},${190-(a[1]-ymin)/(ymax-ymin)*150}`).join(' ');card.querySelector("#" + 'curve'.replace(/^#/, "")).setAttribute('d',path);card.querySelector("#" + 'x-label'.replace(/^#/, "")).textContent='Failure intensity λ (per hour): '+xmin+' to '+xmax;card.querySelector("#" + 'y-label'.replace(/^#/, "")).textContent='Output range: '+format(ymin)+' to '+format(ymax);}
}
for(const name of names){let field=document.getElementById(name),slider=document.getElementById('slider-'+name);field.addEventListener('input',()=>{slider.value=field.value;update();});slider.addEventListener('input',()=>{field.value=slider.value;update();});}update();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 2,
    unit: 1,
    html: "<div class=\"hero\"><div class=\"eyebrow\">Interactive model 02 / Educational demonstration</div><h3>Weibull lifetime survival</h3><p class=\"subtitle\">Modify assumptions and inspect how the idealized result changes.</p></div><p class=\"notice\">Not certified engineering software. Do not rely on this calculator for safety-critical or operational decisions.</p><div class=\"card\"><h2>Inputs</h2><div class=\"inputs\"><div class=\"input\"><label for=\"time\">Age t (hours)</label><input aria-label=\"Age t (hours)\" type=\"number\" id=\"time\" value=\"2000\" min=\"0\" max=\"8000\" step=\"100\"><input aria-label=\"Slide Age t (hours)\" id=\"slider-time\" type=\"range\" value=\"2000\" min=\"0\" max=\"8000\" step=\"100\"></div><div class=\"input\"><label for=\"eta\">Scale \u03b7 (hours)</label><input aria-label=\"Scale \u03b7 (hours)\" type=\"number\" id=\"eta\" value=\"4000\" min=\"100\" max=\"15000\" step=\"100\"><input aria-label=\"Slide Scale \u03b7 (hours)\" id=\"slider-eta\" type=\"range\" value=\"4000\" min=\"100\" max=\"15000\" step=\"100\"></div><div class=\"input\"><label for=\"beta\">Shape \u03b2</label><input aria-label=\"Shape \u03b2\" type=\"number\" id=\"beta\" value=\"2\" min=\"0.2\" max=\"5\" step=\"0.1\"><input aria-label=\"Slide Shape \u03b2\" id=\"slider-beta\" type=\"range\" value=\"2\" min=\"0.2\" max=\"5\" step=\"0.1\"></div></div><p class=\"math\">R(t)=exp[-(t/\u03b7)^\u03b2]</p><div class=\"result\"><div class=\"small\">Calculated output</div><div class=\"value\" id=\"result\" aria-live=\"polite\">Loading</div></div><div class=\"plot\"><svg viewBox=\"0 0 620 220\" aria-label=\"Model sensitivity chart\" role=\"img\"><path d=\"M20 25V190H600\" fill=\"none\" stroke=\"#adbfc1\" stroke-width=\"1.5\"/><path id=\"curve\" d=\"M20 170L600 30\" fill=\"none\" stroke=\"#12796e\" stroke-width=\"3\" stroke-linecap=\"round\"/></svg><div id=\"x-label\" class=\"small\"></div><div id=\"y-label\" class=\"small\"></div></div></div><div class=\"hint\"><strong>Model limitation:</strong> \u03b2 greater than one has increasing modeled hazard, not proven wear mechanism. \u03b7 is the 36.8% survival point.</div><p class=\"small\">Trend plot changes the first input while holding the others constant. All values are illustrative and user-controlled.</p>",
    init: function(card) {
      try {
"use strict";
const names=["time", "eta", "beta"];
function calc(p){return Math.exp(-Math.pow(p.time/p.eta,p.beta));}
function format(v){return (100*v).toFixed(2)+'%';}
function read(){let p={};p.time=parseFloat(card.querySelector("#" + 'time'.replace(/^#/, "")).value);p.eta=parseFloat(card.querySelector("#" + 'eta'.replace(/^#/, "")).value);p.beta=parseFloat(card.querySelector("#" + 'beta'.replace(/^#/, "")).value);return p;}
function update(){let p=read();if(!(Number.isFinite(p.time) && p.time>=0 && p.time<=8000&&Number.isFinite(p.eta) && p.eta>=100 && p.eta<=15000&&Number.isFinite(p.beta) && p.beta>=0.2 && p.beta<=5)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Input outside permitted range';return;}let v=calc(p);card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?format(v):'Model not defined at this input';
const xmin=0,xmax=8000;let pts=[];for(let n=0;n<=80;n++){let x=xmin+(xmax-xmin)*n/80;let q={...p};q['time']=x;let y=calc(q);if(Number.isFinite(y))pts.push([x,y]);}
if(pts.length>1){let ymin=Math.min(...pts.map(a=>a[1])),ymax=Math.max(...pts.map(a=>a[1]));if(Math.abs(ymax-ymin)<1e-12)ymax=ymin+1;let path=pts.map((a,n)=>`${n===0?'M':'L'}${(a[0]-xmin)/(xmax-xmin)*580+20},${190-(a[1]-ymin)/(ymax-ymin)*150}`).join(' ');card.querySelector("#" + 'curve'.replace(/^#/, "")).setAttribute('d',path);card.querySelector("#" + 'x-label'.replace(/^#/, "")).textContent='Age t (hours): '+xmin+' to '+xmax;card.querySelector("#" + 'y-label'.replace(/^#/, "")).textContent='Output range: '+format(ymin)+' to '+format(ymax);}
}
for(const name of names){let field=document.getElementById(name),slider=document.getElementById('slider-'+name);field.addEventListener('input',()=>{slider.value=field.value;update();});slider.addEventListener('input',()=>{field.value=slider.value;update();});}update();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 3,
    unit: 2,
    html: "<div class=\"hero\"><div class=\"eyebrow\">Interactive model 03 / Educational demonstration</div><h3>Weibull instantaneous hazard</h3><p class=\"subtitle\">Modify assumptions and inspect how the idealized result changes.</p></div><p class=\"notice\">Not certified engineering software. Do not rely on this calculator for safety-critical or operational decisions.</p><div class=\"card\"><h2>Inputs</h2><div class=\"inputs\"><div class=\"input\"><label for=\"time\">Age (hours)</label><input aria-label=\"Age (hours)\" type=\"number\" id=\"time\" value=\"2000\" min=\"1\" max=\"8000\" step=\"100\"><input aria-label=\"Slide Age (hours)\" id=\"slider-time\" type=\"range\" value=\"2000\" min=\"1\" max=\"8000\" step=\"100\"></div><div class=\"input\"><label for=\"eta\">Scale (hours)</label><input aria-label=\"Scale (hours)\" type=\"number\" id=\"eta\" value=\"4000\" min=\"100\" max=\"15000\" step=\"100\"><input aria-label=\"Slide Scale (hours)\" id=\"slider-eta\" type=\"range\" value=\"4000\" min=\"100\" max=\"15000\" step=\"100\"></div><div class=\"input\"><label for=\"beta\">Shape</label><input aria-label=\"Shape\" type=\"number\" id=\"beta\" value=\"2\" min=\"0.2\" max=\"5\" step=\"0.1\"><input aria-label=\"Slide Shape\" id=\"slider-beta\" type=\"range\" value=\"2\" min=\"0.2\" max=\"5\" step=\"0.1\"></div></div><p class=\"math\">h(t)=(\u03b2/\u03b7)(t/\u03b7)^(\u03b2-1)</p><div class=\"result\"><div class=\"small\">Calculated output</div><div class=\"value\" id=\"result\" aria-live=\"polite\">Loading</div></div><div class=\"plot\"><svg viewBox=\"0 0 620 220\" aria-label=\"Model sensitivity chart\" role=\"img\"><path d=\"M20 25V190H600\" fill=\"none\" stroke=\"#adbfc1\" stroke-width=\"1.5\"/><path id=\"curve\" d=\"M20 170L600 30\" fill=\"none\" stroke=\"#12796e\" stroke-width=\"3\" stroke-linecap=\"round\"/></svg><div id=\"x-label\" class=\"small\"></div><div id=\"y-label\" class=\"small\"></div></div></div><div class=\"hint\"><strong>Model limitation:</strong> Hazard is an instantaneous conditional rate, not a cumulative failure probability.</div><p class=\"small\">Trend plot changes the first input while holding the others constant. All values are illustrative and user-controlled.</p>",
    init: function(card) {
      try {
"use strict";
const names=["time", "eta", "beta"];
function calc(p){return (p.beta/p.eta)*Math.pow(p.time/p.eta,p.beta-1);}
function format(v){return v.toFixed(6);}
function read(){let p={};p.time=parseFloat(card.querySelector("#" + 'time'.replace(/^#/, "")).value);p.eta=parseFloat(card.querySelector("#" + 'eta'.replace(/^#/, "")).value);p.beta=parseFloat(card.querySelector("#" + 'beta'.replace(/^#/, "")).value);return p;}
function update(){let p=read();if(!(Number.isFinite(p.time) && p.time>=1 && p.time<=8000&&Number.isFinite(p.eta) && p.eta>=100 && p.eta<=15000&&Number.isFinite(p.beta) && p.beta>=0.2 && p.beta<=5)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Input outside permitted range';return;}let v=calc(p);card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?format(v):'Model not defined at this input';
const xmin=1,xmax=8000;let pts=[];for(let n=0;n<=80;n++){let x=xmin+(xmax-xmin)*n/80;let q={...p};q['time']=x;let y=calc(q);if(Number.isFinite(y))pts.push([x,y]);}
if(pts.length>1){let ymin=Math.min(...pts.map(a=>a[1])),ymax=Math.max(...pts.map(a=>a[1]));if(Math.abs(ymax-ymin)<1e-12)ymax=ymin+1;let path=pts.map((a,n)=>`${n===0?'M':'L'}${(a[0]-xmin)/(xmax-xmin)*580+20},${190-(a[1]-ymin)/(ymax-ymin)*150}`).join(' ');card.querySelector("#" + 'curve'.replace(/^#/, "")).setAttribute('d',path);card.querySelector("#" + 'x-label'.replace(/^#/, "")).textContent='Age (hours): '+xmin+' to '+xmax;card.querySelector("#" + 'y-label'.replace(/^#/, "")).textContent='Output range: '+format(ymin)+' to '+format(ymax);}
}
for(const name of names){let field=document.getElementById(name),slider=document.getElementById('slider-'+name);field.addEventListener('input',()=>{slider.value=field.value;update();});slider.addEventListener('input',()=>{field.value=slider.value;update();});}update();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 4,
    unit: 2,
    html: "<div class=\"hero\"><div class=\"eyebrow\">Interactive model 04 / Educational demonstration</div><h3>Series system</h3><p class=\"subtitle\">Modify assumptions and inspect how the idealized result changes.</p></div><p class=\"notice\">Not certified engineering software. Do not rely on this calculator for safety-critical or operational decisions.</p><div class=\"card\"><h2>Inputs</h2><div class=\"inputs\"><div class=\"input\"><label for=\"r1\">Component 1 reliability</label><input aria-label=\"Component 1 reliability\" type=\"number\" id=\"r1\" value=\"0.98\" min=\"0\" max=\"1\" step=\"0.01\"><input aria-label=\"Slide Component 1 reliability\" id=\"slider-r1\" type=\"range\" value=\"0.98\" min=\"0\" max=\"1\" step=\"0.01\"></div><div class=\"input\"><label for=\"r2\">Component 2 reliability</label><input aria-label=\"Component 2 reliability\" type=\"number\" id=\"r2\" value=\"0.97\" min=\"0\" max=\"1\" step=\"0.01\"><input aria-label=\"Slide Component 2 reliability\" id=\"slider-r2\" type=\"range\" value=\"0.97\" min=\"0\" max=\"1\" step=\"0.01\"></div><div class=\"input\"><label for=\"r3\">Component 3 reliability</label><input aria-label=\"Component 3 reliability\" type=\"number\" id=\"r3\" value=\"0.95\" min=\"0\" max=\"1\" step=\"0.01\"><input aria-label=\"Slide Component 3 reliability\" id=\"slider-r3\" type=\"range\" value=\"0.95\" min=\"0\" max=\"1\" step=\"0.01\"></div></div><p class=\"math\">R=R1\u00d7R2\u00d7R3</p><div class=\"result\"><div class=\"small\">Calculated output</div><div class=\"value\" id=\"result\" aria-live=\"polite\">Loading</div></div><div class=\"plot\"><svg viewBox=\"0 0 620 220\" aria-label=\"Model sensitivity chart\" role=\"img\"><path d=\"M20 25V190H600\" fill=\"none\" stroke=\"#adbfc1\" stroke-width=\"1.5\"/><path id=\"curve\" d=\"M20 170L600 30\" fill=\"none\" stroke=\"#12796e\" stroke-width=\"3\" stroke-linecap=\"round\"/></svg><div id=\"x-label\" class=\"small\"></div><div id=\"y-label\" class=\"small\"></div></div></div><div class=\"hint\"><strong>Model limitation:</strong> Only valid when all three are required, reliability is mission-aligned and failures are independent.</div><p class=\"small\">Trend plot changes the first input while holding the others constant. All values are illustrative and user-controlled.</p>",
    init: function(card) {
      try {
"use strict";
const names=["r1", "r2", "r3"];
function calc(p){return p.r1*p.r2*p.r3;}
function format(v){return (100*v).toFixed(2)+'%';}
function read(){let p={};p.r1=parseFloat(card.querySelector("#" + 'r1'.replace(/^#/, "")).value);p.r2=parseFloat(card.querySelector("#" + 'r2'.replace(/^#/, "")).value);p.r3=parseFloat(card.querySelector("#" + 'r3'.replace(/^#/, "")).value);return p;}
function update(){let p=read();if(!(Number.isFinite(p.r1) && p.r1>=0 && p.r1<=1&&Number.isFinite(p.r2) && p.r2>=0 && p.r2<=1&&Number.isFinite(p.r3) && p.r3>=0 && p.r3<=1)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Input outside permitted range';return;}let v=calc(p);card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?format(v):'Model not defined at this input';
const xmin=0,xmax=1;let pts=[];for(let n=0;n<=80;n++){let x=xmin+(xmax-xmin)*n/80;let q={...p};q['r1']=x;let y=calc(q);if(Number.isFinite(y))pts.push([x,y]);}
if(pts.length>1){let ymin=Math.min(...pts.map(a=>a[1])),ymax=Math.max(...pts.map(a=>a[1]));if(Math.abs(ymax-ymin)<1e-12)ymax=ymin+1;let path=pts.map((a,n)=>`${n===0?'M':'L'}${(a[0]-xmin)/(xmax-xmin)*580+20},${190-(a[1]-ymin)/(ymax-ymin)*150}`).join(' ');card.querySelector("#" + 'curve'.replace(/^#/, "")).setAttribute('d',path);card.querySelector("#" + 'x-label'.replace(/^#/, "")).textContent='Component 1 reliability: '+xmin+' to '+xmax;card.querySelector("#" + 'y-label'.replace(/^#/, "")).textContent='Output range: '+format(ymin)+' to '+format(ymax);}
}
for(const name of names){let field=document.getElementById(name),slider=document.getElementById('slider-'+name);field.addEventListener('input',()=>{slider.value=field.value;update();});slider.addEventListener('input',()=>{field.value=slider.value;update();});}update();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 5,
    unit: 3,
    html: "<div class=\"hero\"><div class=\"eyebrow\">Interactive model 05 / Educational demonstration</div><h3>Parallel active redundancy</h3><p class=\"subtitle\">Modify assumptions and inspect how the idealized result changes.</p></div><p class=\"notice\">Not certified engineering software. Do not rely on this calculator for safety-critical or operational decisions.</p><div class=\"card\"><h2>Inputs</h2><div class=\"inputs\"><div class=\"input\"><label for=\"r1\">Branch 1 reliability</label><input aria-label=\"Branch 1 reliability\" type=\"number\" id=\"r1\" value=\"0.9\" min=\"0\" max=\"1\" step=\"0.01\"><input aria-label=\"Slide Branch 1 reliability\" id=\"slider-r1\" type=\"range\" value=\"0.9\" min=\"0\" max=\"1\" step=\"0.01\"></div><div class=\"input\"><label for=\"r2\">Branch 2 reliability</label><input aria-label=\"Branch 2 reliability\" type=\"number\" id=\"r2\" value=\"0.9\" min=\"0\" max=\"1\" step=\"0.01\"><input aria-label=\"Slide Branch 2 reliability\" id=\"slider-r2\" type=\"range\" value=\"0.9\" min=\"0\" max=\"1\" step=\"0.01\"></div></div><p class=\"math\">R=1-(1-R1)(1-R2)</p><div class=\"result\"><div class=\"small\">Calculated output</div><div class=\"value\" id=\"result\" aria-live=\"polite\">Loading</div></div><div class=\"plot\"><svg viewBox=\"0 0 620 220\" aria-label=\"Model sensitivity chart\" role=\"img\"><path d=\"M20 25V190H600\" fill=\"none\" stroke=\"#adbfc1\" stroke-width=\"1.5\"/><path id=\"curve\" d=\"M20 170L600 30\" fill=\"none\" stroke=\"#12796e\" stroke-width=\"3\" stroke-linecap=\"round\"/></svg><div id=\"x-label\" class=\"small\"></div><div id=\"y-label\" class=\"small\"></div></div></div><div class=\"hint\"><strong>Model limitation:</strong> The independent-branch idealization ignores common supplies, shared disturbances and load-sharing performance.</div><p class=\"small\">Trend plot changes the first input while holding the others constant. All values are illustrative and user-controlled.</p>",
    init: function(card) {
      try {
"use strict";
const names=["r1", "r2"];
function calc(p){return 1-(1-p.r1)*(1-p.r2);}
function format(v){return (100*v).toFixed(2)+'%';}
function read(){let p={};p.r1=parseFloat(card.querySelector("#" + 'r1'.replace(/^#/, "")).value);p.r2=parseFloat(card.querySelector("#" + 'r2'.replace(/^#/, "")).value);return p;}
function update(){let p=read();if(!(Number.isFinite(p.r1) && p.r1>=0 && p.r1<=1&&Number.isFinite(p.r2) && p.r2>=0 && p.r2<=1)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Input outside permitted range';return;}let v=calc(p);card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?format(v):'Model not defined at this input';
const xmin=0,xmax=1;let pts=[];for(let n=0;n<=80;n++){let x=xmin+(xmax-xmin)*n/80;let q={...p};q['r1']=x;let y=calc(q);if(Number.isFinite(y))pts.push([x,y]);}
if(pts.length>1){let ymin=Math.min(...pts.map(a=>a[1])),ymax=Math.max(...pts.map(a=>a[1]));if(Math.abs(ymax-ymin)<1e-12)ymax=ymin+1;let path=pts.map((a,n)=>`${n===0?'M':'L'}${(a[0]-xmin)/(xmax-xmin)*580+20},${190-(a[1]-ymin)/(ymax-ymin)*150}`).join(' ');card.querySelector("#" + 'curve'.replace(/^#/, "")).setAttribute('d',path);card.querySelector("#" + 'x-label'.replace(/^#/, "")).textContent='Branch 1 reliability: '+xmin+' to '+xmax;card.querySelector("#" + 'y-label'.replace(/^#/, "")).textContent='Output range: '+format(ymin)+' to '+format(ymax);}
}
for(const name of names){let field=document.getElementById(name),slider=document.getElementById('slider-'+name);field.addEventListener('input',()=>{slider.value=field.value;update();});slider.addEventListener('input',()=>{field.value=slider.value;update();});}update();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 6,
    unit: 3,
    html: "<div class=\"hero\"><div class=\"eyebrow\">Interactive model 06 / Educational demonstration</div><h3>Steady inherent availability</h3><p class=\"subtitle\">Modify assumptions and inspect how the idealized result changes.</p></div><p class=\"notice\">Not certified engineering software. Do not rely on this calculator for safety-critical or operational decisions.</p><div class=\"card\"><h2>Inputs</h2><div class=\"inputs\"><div class=\"input\"><label for=\"mtbf\">MTBF (hours)</label><input aria-label=\"MTBF (hours)\" type=\"number\" id=\"mtbf\" value=\"500\" min=\"1\" max=\"5000\" step=\"50\"><input aria-label=\"Slide MTBF (hours)\" id=\"slider-mtbf\" type=\"range\" value=\"500\" min=\"1\" max=\"5000\" step=\"50\"></div><div class=\"input\"><label for=\"mttr\">MTTR (hours)</label><input aria-label=\"MTTR (hours)\" type=\"number\" id=\"mttr\" value=\"8\" min=\"0.1\" max=\"100\" step=\"1\"><input aria-label=\"Slide MTTR (hours)\" id=\"slider-mttr\" type=\"range\" value=\"8\" min=\"0.1\" max=\"100\" step=\"1\"></div></div><p class=\"math\">A=MTBF/(MTBF+MTTR)</p><div class=\"result\"><div class=\"small\">Calculated output</div><div class=\"value\" id=\"result\" aria-live=\"polite\">Loading</div></div><div class=\"plot\"><svg viewBox=\"0 0 620 220\" aria-label=\"Model sensitivity chart\" role=\"img\"><path d=\"M20 25V190H600\" fill=\"none\" stroke=\"#adbfc1\" stroke-width=\"1.5\"/><path id=\"curve\" d=\"M20 170L600 30\" fill=\"none\" stroke=\"#12796e\" stroke-width=\"3\" stroke-linecap=\"round\"/></svg><div id=\"x-label\" class=\"small\"></div><div id=\"y-label\" class=\"small\"></div></div></div><div class=\"hint\"><strong>Model limitation:</strong> Steady inherent approximation under compatible failure and active repair assumptions; waiting for parts may be excluded.</div><p class=\"small\">Trend plot changes the first input while holding the others constant. All values are illustrative and user-controlled.</p>",
    init: function(card) {
      try {
"use strict";
const names=["mtbf", "mttr"];
function calc(p){return p.mtbf/(p.mtbf+p.mttr);}
function format(v){return (100*v).toFixed(2)+'%';}
function read(){let p={};p.mtbf=parseFloat(card.querySelector("#" + 'mtbf'.replace(/^#/, "")).value);p.mttr=parseFloat(card.querySelector("#" + 'mttr'.replace(/^#/, "")).value);return p;}
function update(){let p=read();if(!(Number.isFinite(p.mtbf) && p.mtbf>=1 && p.mtbf<=5000&&Number.isFinite(p.mttr) && p.mttr>=0.1 && p.mttr<=100)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Input outside permitted range';return;}let v=calc(p);card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?format(v):'Model not defined at this input';
const xmin=1,xmax=5000;let pts=[];for(let n=0;n<=80;n++){let x=xmin+(xmax-xmin)*n/80;let q={...p};q['mtbf']=x;let y=calc(q);if(Number.isFinite(y))pts.push([x,y]);}
if(pts.length>1){let ymin=Math.min(...pts.map(a=>a[1])),ymax=Math.max(...pts.map(a=>a[1]));if(Math.abs(ymax-ymin)<1e-12)ymax=ymin+1;let path=pts.map((a,n)=>`${n===0?'M':'L'}${(a[0]-xmin)/(xmax-xmin)*580+20},${190-(a[1]-ymin)/(ymax-ymin)*150}`).join(' ');card.querySelector("#" + 'curve'.replace(/^#/, "")).setAttribute('d',path);card.querySelector("#" + 'x-label'.replace(/^#/, "")).textContent='MTBF (hours): '+xmin+' to '+xmax;card.querySelector("#" + 'y-label'.replace(/^#/, "")).textContent='Output range: '+format(ymin)+' to '+format(ymax);}
}
for(const name of names){let field=document.getElementById(name),slider=document.getElementById('slider-'+name);field.addEventListener('input',()=>{slider.value=field.value;update();});slider.addEventListener('input',()=>{field.value=slider.value;update();});}update();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 7,
    unit: 4,
    html: "<div class=\"hero\"><div class=\"eyebrow\">Interactive model 07 / Educational demonstration</div><h3>Probability of repair within a deadline</h3><p class=\"subtitle\">Modify assumptions and inspect how the idealized result changes.</p></div><p class=\"notice\">Not certified engineering software. Do not rely on this calculator for safety-critical or operational decisions.</p><div class=\"card\"><h2>Inputs</h2><div class=\"inputs\"><div class=\"input\"><label for=\"time\">Repair deadline (hours)</label><input aria-label=\"Repair deadline (hours)\" type=\"number\" id=\"time\" value=\"4\" min=\"0\" max=\"40\" step=\"1\"><input aria-label=\"Slide Repair deadline (hours)\" id=\"slider-time\" type=\"range\" value=\"4\" min=\"0\" max=\"40\" step=\"1\"></div><div class=\"input\"><label for=\"mttr\">Mean repair time (hours)</label><input aria-label=\"Mean repair time (hours)\" type=\"number\" id=\"mttr\" value=\"8\" min=\"0.1\" max=\"100\" step=\"1\"><input aria-label=\"Slide Mean repair time (hours)\" id=\"slider-mttr\" type=\"range\" value=\"8\" min=\"0.1\" max=\"100\" step=\"1\"></div></div><p class=\"math\">M(t)=1-exp(-t/MTTR)</p><div class=\"result\"><div class=\"small\">Calculated output</div><div class=\"value\" id=\"result\" aria-live=\"polite\">Loading</div></div><div class=\"plot\"><svg viewBox=\"0 0 620 220\" aria-label=\"Model sensitivity chart\" role=\"img\"><path d=\"M20 25V190H600\" fill=\"none\" stroke=\"#adbfc1\" stroke-width=\"1.5\"/><path id=\"curve\" d=\"M20 170L600 30\" fill=\"none\" stroke=\"#12796e\" stroke-width=\"3\" stroke-linecap=\"round\"/></svg><div id=\"x-label\" class=\"small\"></div><div id=\"y-label\" class=\"small\"></div></div></div><div class=\"hint\"><strong>Model limitation:</strong> Uses exponential repair-time distribution; not valid for fixed-length job tasks or long parts queues.</div><p class=\"small\">Trend plot changes the first input while holding the others constant. All values are illustrative and user-controlled.</p>",
    init: function(card) {
      try {
"use strict";
const names=["time", "mttr"];
function calc(p){return 1-Math.exp(-p.time/p.mttr);}
function format(v){return (100*v).toFixed(2)+'%';}
function read(){let p={};p.time=parseFloat(card.querySelector("#" + 'time'.replace(/^#/, "")).value);p.mttr=parseFloat(card.querySelector("#" + 'mttr'.replace(/^#/, "")).value);return p;}
function update(){let p=read();if(!(Number.isFinite(p.time) && p.time>=0 && p.time<=40&&Number.isFinite(p.mttr) && p.mttr>=0.1 && p.mttr<=100)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Input outside permitted range';return;}let v=calc(p);card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?format(v):'Model not defined at this input';
const xmin=0,xmax=40;let pts=[];for(let n=0;n<=80;n++){let x=xmin+(xmax-xmin)*n/80;let q={...p};q['time']=x;let y=calc(q);if(Number.isFinite(y))pts.push([x,y]);}
if(pts.length>1){let ymin=Math.min(...pts.map(a=>a[1])),ymax=Math.max(...pts.map(a=>a[1]));if(Math.abs(ymax-ymin)<1e-12)ymax=ymin+1;let path=pts.map((a,n)=>`${n===0?'M':'L'}${(a[0]-xmin)/(xmax-xmin)*580+20},${190-(a[1]-ymin)/(ymax-ymin)*150}`).join(' ');card.querySelector("#" + 'curve'.replace(/^#/, "")).setAttribute('d',path);card.querySelector("#" + 'x-label'.replace(/^#/, "")).textContent='Repair deadline (hours): '+xmin+' to '+xmax;card.querySelector("#" + 'y-label'.replace(/^#/, "")).textContent='Output range: '+format(ymin)+' to '+format(ymax);}
}
for(const name of names){let field=document.getElementById(name),slider=document.getElementById('slider-'+name);field.addEventListener('input',()=>{slider.value=field.value;update();});slider.addEventListener('input',()=>{field.value=slider.value;update();});}update();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 8,
    unit: 4,
    html: "<div class=\"hero\"><div class=\"eyebrow\">Interactive model 08 / Educational demonstration</div><h3>Standby transfer coverage</h3><p class=\"subtitle\">Modify assumptions and inspect how the idealized result changes.</p></div><p class=\"notice\">Not certified engineering software. Do not rely on this calculator for safety-critical or operational decisions.</p><div class=\"card\"><h2>Inputs</h2><div class=\"inputs\"><div class=\"input\"><label for=\"primary\">Primary survival</label><input aria-label=\"Primary survival\" type=\"number\" id=\"primary\" value=\"0.9\" min=\"0\" max=\"1\" step=\"0.01\"><input aria-label=\"Slide Primary survival\" id=\"slider-primary\" type=\"range\" value=\"0.9\" min=\"0\" max=\"1\" step=\"0.01\"></div><div class=\"input\"><label for=\"backup\">Backup successful start</label><input aria-label=\"Backup successful start\" type=\"number\" id=\"backup\" value=\"0.85\" min=\"0\" max=\"1\" step=\"0.01\"><input aria-label=\"Slide Backup successful start\" id=\"slider-backup\" type=\"range\" value=\"0.85\" min=\"0\" max=\"1\" step=\"0.01\"></div><div class=\"input\"><label for=\"coverage\">Detection/transfer coverage</label><input aria-label=\"Detection/transfer coverage\" type=\"number\" id=\"coverage\" value=\"0.95\" min=\"0\" max=\"1\" step=\"0.01\"><input aria-label=\"Slide Detection/transfer coverage\" id=\"slider-coverage\" type=\"range\" value=\"0.95\" min=\"0\" max=\"1\" step=\"0.01\"></div></div><p class=\"math\">R=Rp+(1-Rp)cRb</p><div class=\"result\"><div class=\"small\">Calculated output</div><div class=\"value\" id=\"result\" aria-live=\"polite\">Loading</div></div><div class=\"plot\"><svg viewBox=\"0 0 620 220\" aria-label=\"Model sensitivity chart\" role=\"img\"><path d=\"M20 25V190H600\" fill=\"none\" stroke=\"#adbfc1\" stroke-width=\"1.5\"/><path id=\"curve\" d=\"M20 170L600 30\" fill=\"none\" stroke=\"#12796e\" stroke-width=\"3\" stroke-linecap=\"round\"/></svg><div id=\"x-label\" class=\"small\"></div><div id=\"y-label\" class=\"small\"></div></div></div><div class=\"hint\"><strong>Model limitation:</strong> One-demand idealization. It omits shared causes, backup aging, subsequent failures and dynamic repair.</div><p class=\"small\">Trend plot changes the first input while holding the others constant. All values are illustrative and user-controlled.</p>",
    init: function(card) {
      try {
"use strict";
const names=["primary", "backup", "coverage"];
function calc(p){return p.primary+(1-p.primary)*p.coverage*p.backup;}
function format(v){return (100*v).toFixed(2)+'%';}
function read(){let p={};p.primary=parseFloat(card.querySelector("#" + 'primary'.replace(/^#/, "")).value);p.backup=parseFloat(card.querySelector("#" + 'backup'.replace(/^#/, "")).value);p.coverage=parseFloat(card.querySelector("#" + 'coverage'.replace(/^#/, "")).value);return p;}
function update(){let p=read();if(!(Number.isFinite(p.primary) && p.primary>=0 && p.primary<=1&&Number.isFinite(p.backup) && p.backup>=0 && p.backup<=1&&Number.isFinite(p.coverage) && p.coverage>=0 && p.coverage<=1)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Input outside permitted range';return;}let v=calc(p);card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?format(v):'Model not defined at this input';
const xmin=0,xmax=1;let pts=[];for(let n=0;n<=80;n++){let x=xmin+(xmax-xmin)*n/80;let q={...p};q['primary']=x;let y=calc(q);if(Number.isFinite(y))pts.push([x,y]);}
if(pts.length>1){let ymin=Math.min(...pts.map(a=>a[1])),ymax=Math.max(...pts.map(a=>a[1]));if(Math.abs(ymax-ymin)<1e-12)ymax=ymin+1;let path=pts.map((a,n)=>`${n===0?'M':'L'}${(a[0]-xmin)/(xmax-xmin)*580+20},${190-(a[1]-ymin)/(ymax-ymin)*150}`).join(' ');card.querySelector("#" + 'curve'.replace(/^#/, "")).setAttribute('d',path);card.querySelector("#" + 'x-label'.replace(/^#/, "")).textContent='Primary survival: '+xmin+' to '+xmax;card.querySelector("#" + 'y-label'.replace(/^#/, "")).textContent='Output range: '+format(ymin)+' to '+format(ymax);}
}
for(const name of names){let field=document.getElementById(name),slider=document.getElementById('slider-'+name);field.addEventListener('input',()=>{slider.value=field.value;update();});slider.addEventListener('input',()=>{field.value=slider.value;update();});}update();
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 9,
    unit: 5,
    html: "<div class=\"hero\"><div class=\"eyebrow\">Interactive model 09 / Educational demonstration</div><h3>Spares demand Poisson tail</h3><p class=\"subtitle\">Modify assumptions and inspect how the idealized result changes.</p></div><p class=\"notice\">Not certified engineering software. Do not rely on this calculator for safety-critical or operational decisions.</p><div class=\"card\"><h2>Inputs</h2><div class=\"inputs\"><div class=\"input\"><label for=\"mean\">Expected lead-time demand m</label><input aria-label=\"Expected lead-time demand m\" type=\"number\" id=\"mean\" value=\"0.5\" min=\"0\" max=\"8\" step=\"0.1\"><input aria-label=\"Slide Expected lead-time demand m\" id=\"slider-mean\" type=\"range\" value=\"0.5\" min=\"0\" max=\"8\" step=\"0.1\"></div><div class=\"input\"><label for=\"stock\">Spares on hand k</label><input aria-label=\"Spares on hand k\" type=\"number\" id=\"stock\" value=\"1\" min=\"0\" max=\"12\" step=\"1\"><input aria-label=\"Slide Spares on hand k\" id=\"slider-stock\" type=\"range\" value=\"1\" min=\"0\" max=\"12\" step=\"1\"></div></div><p class=\"math\">P(demand &gt; stock)=1-\u03a3_(j=0)^k exp(-m)m^j/j!</p><div class=\"result\"><div class=\"small\">Calculated output</div><div class=\"value\" id=\"result\" aria-live=\"polite\">Loading</div></div><div class=\"plot\"><svg viewBox=\"0 0 620 220\" aria-label=\"Model sensitivity chart\" role=\"img\"><path d=\"M20 25V190H600\" fill=\"none\" stroke=\"#adbfc1\" stroke-width=\"1.5\"/><path id=\"curve\" d=\"M20 170L600 30\" fill=\"none\" stroke=\"#12796e\" stroke-width=\"3\" stroke-linecap=\"round\"/></svg><div id=\"x-label\" class=\"small\"></div><div id=\"y-label\" class=\"small\"></div></div></div><div class=\"hint\"><strong>Model limitation:</strong> Shows probability of more requests than available parts under independent Poisson demand. Replenishment dynamics are omitted.</div><p class=\"small\">Trend plot changes the first input while holding the others constant. All values are illustrative and user-controlled.</p>",
    init: function(card) {
      try {
"use strict";
const names=["mean", "stock"];
function calc(p){return (()=>{let sum=0,term=Math.exp(-p.mean);for(let j=0;j<=Math.round(p.stock);j++){if(j>0)term*=p.mean/j;sum+=term;}return 1-sum;})();}
function format(v){return (100*v).toFixed(2)+'%';}
function read(){let p={};p.mean=parseFloat(card.querySelector("#" + 'mean'.replace(/^#/, "")).value);p.stock=parseFloat(card.querySelector("#" + 'stock'.replace(/^#/, "")).value);return p;}
function update(){let p=read();if(!(Number.isFinite(p.mean) && p.mean>=0 && p.mean<=8&&Number.isFinite(p.stock) && p.stock>=0 && p.stock<=12)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Input outside permitted range';return;}let v=calc(p);card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?format(v):'Model not defined at this input';
const xmin=0,xmax=8;let pts=[];for(let n=0;n<=80;n++){let x=xmin+(xmax-xmin)*n/80;let q={...p};q['mean']=x;let y=calc(q);if(Number.isFinite(y))pts.push([x,y]);}
if(pts.length>1){let ymin=Math.min(...pts.map(a=>a[1])),ymax=Math.max(...pts.map(a=>a[1]));if(Math.abs(ymax-ymin)<1e-12)ymax=ymin+1;let path=pts.map((a,n)=>`${n===0?'M':'L'}${(a[0]-xmin)/(xmax-xmin)*580+20},${190-(a[1]-ymin)/(ymax-ymin)*150}`).join(' ');card.querySelector("#" + 'curve'.replace(/^#/, "")).setAttribute('d',path);card.querySelector("#" + 'x-label'.replace(/^#/, "")).textContent='Expected lead-time demand m: '+xmin+' to '+xmax;card.querySelector("#" + 'y-label'.replace(/^#/, "")).textContent='Output range: '+format(ymin)+' to '+format(ymax);}
}
for(const name of names){let field=document.getElementById(name),slider=document.getElementById('slider-'+name);field.addEventListener('input',()=>{slider.value=field.value;update();});slider.addEventListener('input',()=>{field.value=slider.value;update();});}update();
      } catch (err) {
        console.warn('Sim init error in model 9:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 10,
    unit: 5,
    html: "<div class=\"hero\"><div class=\"eyebrow\">Interactive model 10 / Educational demonstration</div><h3>Overall equipment effectiveness</h3><p class=\"subtitle\">Modify assumptions and inspect how the idealized result changes.</p></div><p class=\"notice\">Not certified engineering software. Do not rely on this calculator for safety-critical or operational decisions.</p><div class=\"card\"><h2>Inputs</h2><div class=\"inputs\"><div class=\"input\"><label for=\"availability\">Production availability</label><input aria-label=\"Production availability\" type=\"number\" id=\"availability\" value=\"0.9\" min=\"0\" max=\"1\" step=\"0.01\"><input aria-label=\"Slide Production availability\" id=\"slider-availability\" type=\"range\" value=\"0.9\" min=\"0\" max=\"1\" step=\"0.01\"></div><div class=\"input\"><label for=\"performance\">Performance factor</label><input aria-label=\"Performance factor\" type=\"number\" id=\"performance\" value=\"0.95\" min=\"0\" max=\"1\" step=\"0.01\"><input aria-label=\"Slide Performance factor\" id=\"slider-performance\" type=\"range\" value=\"0.95\" min=\"0\" max=\"1\" step=\"0.01\"></div><div class=\"input\"><label for=\"quality\">Good quality proportion</label><input aria-label=\"Good quality proportion\" type=\"number\" id=\"quality\" value=\"0.98\" min=\"0\" max=\"1\" step=\"0.01\"><input aria-label=\"Slide Good quality proportion\" id=\"slider-quality\" type=\"range\" value=\"0.98\" min=\"0\" max=\"1\" step=\"0.01\"></div></div><p class=\"math\">OEE=Availability\u00d7Performance\u00d7Quality</p><div class=\"result\"><div class=\"small\">Calculated output</div><div class=\"value\" id=\"result\" aria-live=\"polite\">Loading</div></div><div class=\"plot\"><svg viewBox=\"0 0 620 220\" aria-label=\"Model sensitivity chart\" role=\"img\"><path d=\"M20 25V190H600\" fill=\"none\" stroke=\"#adbfc1\" stroke-width=\"1.5\"/><path id=\"curve\" d=\"M20 170L600 30\" fill=\"none\" stroke=\"#12796e\" stroke-width=\"3\" stroke-linecap=\"round\"/></svg><div id=\"x-label\" class=\"small\"></div><div id=\"y-label\" class=\"small\"></div></div></div><div class=\"hint\"><strong>Model limitation:</strong> A production KPI; it is not a direct estimate of first-failure reliability or system hazard.</div><p class=\"small\">Trend plot changes the first input while holding the others constant. All values are illustrative and user-controlled.</p>",
    init: function(card) {
      try {
"use strict";
const names=["availability", "performance", "quality"];
function calc(p){return p.availability*p.performance*p.quality;}
function format(v){return (100*v).toFixed(2)+'%';}
function read(){let p={};p.availability=parseFloat(card.querySelector("#" + 'availability'.replace(/^#/, "")).value);p.performance=parseFloat(card.querySelector("#" + 'performance'.replace(/^#/, "")).value);p.quality=parseFloat(card.querySelector("#" + 'quality'.replace(/^#/, "")).value);return p;}
function update(){let p=read();if(!(Number.isFinite(p.availability) && p.availability>=0 && p.availability<=1&&Number.isFinite(p.performance) && p.performance>=0 && p.performance<=1&&Number.isFinite(p.quality) && p.quality>=0 && p.quality<=1)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Input outside permitted range';return;}let v=calc(p);card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?format(v):'Model not defined at this input';
const xmin=0,xmax=1;let pts=[];for(let n=0;n<=80;n++){let x=xmin+(xmax-xmin)*n/80;let q={...p};q['availability']=x;let y=calc(q);if(Number.isFinite(y))pts.push([x,y]);}
if(pts.length>1){let ymin=Math.min(...pts.map(a=>a[1])),ymax=Math.max(...pts.map(a=>a[1]));if(Math.abs(ymax-ymin)<1e-12)ymax=ymin+1;let path=pts.map((a,n)=>`${n===0?'M':'L'}${(a[0]-xmin)/(xmax-xmin)*580+20},${190-(a[1]-ymin)/(ymax-ymin)*150}`).join(' ');card.querySelector("#" + 'curve'.replace(/^#/, "")).setAttribute('d',path);card.querySelector("#" + 'x-label'.replace(/^#/, "")).textContent='Production availability: '+xmin+' to '+xmax;card.querySelector("#" + 'y-label'.replace(/^#/, "")).textContent='Output range: '+format(ymin)+' to '+format(ymax);}
}
for(const name of names){let field=document.getElementById(name),slider=document.getElementById('slider-'+name);field.addEventListener('input',()=>{slider.value=field.value;update();});slider.addEventListener('input',()=>{field.value=slider.value;update();});}update();
      } catch (err) {
        console.warn('Sim init error in model 10:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 11,
    unit: 6,
    html: "<div class=\"hero\"><div class=\"eyebrow\">Interactive model 11 / Educational demonstration</div><h3>Independent OR fault-tree gate</h3><p class=\"subtitle\">Modify assumptions and inspect how the idealized result changes.</p></div><p class=\"notice\">Not certified engineering software. Do not rely on this calculator for safety-critical or operational decisions.</p><div class=\"card\"><h2>Inputs</h2><div class=\"inputs\"><div class=\"input\"><label for=\"pa\">Basic event A probability</label><input aria-label=\"Basic event A probability\" type=\"number\" id=\"pa\" value=\"0.1\" min=\"0\" max=\"1\" step=\"0.01\"><input aria-label=\"Slide Basic event A probability\" id=\"slider-pa\" type=\"range\" value=\"0.1\" min=\"0\" max=\"1\" step=\"0.01\"></div><div class=\"input\"><label for=\"pb\">Basic event B probability</label><input aria-label=\"Basic event B probability\" type=\"number\" id=\"pb\" value=\"0.2\" min=\"0\" max=\"1\" step=\"0.01\"><input aria-label=\"Slide Basic event B probability\" id=\"slider-pb\" type=\"range\" value=\"0.2\" min=\"0\" max=\"1\" step=\"0.01\"></div></div><p class=\"math\">P(A OR B)=PA+PB-PAPB</p><div class=\"result\"><div class=\"small\">Calculated output</div><div class=\"value\" id=\"result\" aria-live=\"polite\">Loading</div></div><div class=\"plot\"><svg viewBox=\"0 0 620 220\" aria-label=\"Model sensitivity chart\" role=\"img\"><path d=\"M20 25V190H600\" fill=\"none\" stroke=\"#adbfc1\" stroke-width=\"1.5\"/><path id=\"curve\" d=\"M20 170L600 30\" fill=\"none\" stroke=\"#12796e\" stroke-width=\"3\" stroke-linecap=\"round\"/></svg><div id=\"x-label\" class=\"small\"></div><div id=\"y-label\" class=\"small\"></div></div></div><div class=\"hint\"><strong>Model limitation:</strong> Only appropriate for independent basic event probabilities over a common time and boundary.</div><p class=\"small\">Trend plot changes the first input while holding the others constant. All values are illustrative and user-controlled.</p>",
    init: function(card) {
      try {
"use strict";
const names=["pa", "pb"];
function calc(p){return p.pa+p.pb-p.pa*p.pb;}
function format(v){return (100*v).toFixed(2)+'%';}
function read(){let p={};p.pa=parseFloat(card.querySelector("#" + 'pa'.replace(/^#/, "")).value);p.pb=parseFloat(card.querySelector("#" + 'pb'.replace(/^#/, "")).value);return p;}
function update(){let p=read();if(!(Number.isFinite(p.pa) && p.pa>=0 && p.pa<=1&&Number.isFinite(p.pb) && p.pb>=0 && p.pb<=1)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Input outside permitted range';return;}let v=calc(p);card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?format(v):'Model not defined at this input';
const xmin=0,xmax=1;let pts=[];for(let n=0;n<=80;n++){let x=xmin+(xmax-xmin)*n/80;let q={...p};q['pa']=x;let y=calc(q);if(Number.isFinite(y))pts.push([x,y]);}
if(pts.length>1){let ymin=Math.min(...pts.map(a=>a[1])),ymax=Math.max(...pts.map(a=>a[1]));if(Math.abs(ymax-ymin)<1e-12)ymax=ymin+1;let path=pts.map((a,n)=>`${n===0?'M':'L'}${(a[0]-xmin)/(xmax-xmin)*580+20},${190-(a[1]-ymin)/(ymax-ymin)*150}`).join(' ');card.querySelector("#" + 'curve'.replace(/^#/, "")).setAttribute('d',path);card.querySelector("#" + 'x-label'.replace(/^#/, "")).textContent='Basic event A probability: '+xmin+' to '+xmax;card.querySelector("#" + 'y-label'.replace(/^#/, "")).textContent='Output range: '+format(ymin)+' to '+format(ymax);}
}
for(const name of names){let field=document.getElementById(name),slider=document.getElementById('slider-'+name);field.addEventListener('input',()=>{slider.value=field.value;update();});slider.addEventListener('input',()=>{field.value=slider.value;update();});}update();
      } catch (err) {
        console.warn('Sim init error in model 11:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 12,
    unit: 6,
    html: "<div class=\"hero\"><div class=\"eyebrow\">Interactive model 12 / Educational demonstration</div><h3>Weibull age-replacement cost rate</h3><p class=\"subtitle\">Modify assumptions and inspect how the idealized result changes.</p></div><p class=\"notice\">Not certified engineering software. Do not rely on this calculator for safety-critical or operational decisions.</p><div class=\"card\"><h2>Inputs</h2><div class=\"inputs\"><div class=\"input\"><label for=\"tau\">Replacement age \u03c4 (hours)</label><input aria-label=\"Replacement age \u03c4 (hours)\" type=\"number\" id=\"tau\" value=\"1000\" min=\"20\" max=\"6000\" step=\"100\"><input aria-label=\"Slide Replacement age \u03c4 (hours)\" id=\"slider-tau\" type=\"range\" value=\"1000\" min=\"20\" max=\"6000\" step=\"100\"></div><div class=\"input\"><label for=\"eta\">Weibull scale (hours)</label><input aria-label=\"Weibull scale (hours)\" type=\"number\" id=\"eta\" value=\"4000\" min=\"200\" max=\"10000\" step=\"100\"><input aria-label=\"Slide Weibull scale (hours)\" id=\"slider-eta\" type=\"range\" value=\"4000\" min=\"200\" max=\"10000\" step=\"100\"></div><div class=\"input\"><label for=\"beta\">Weibull shape</label><input aria-label=\"Weibull shape\" type=\"number\" id=\"beta\" value=\"2\" min=\"0.5\" max=\"5\" step=\"0.1\"><input aria-label=\"Slide Weibull shape\" id=\"slider-beta\" type=\"range\" value=\"2\" min=\"0.5\" max=\"5\" step=\"0.1\"></div><div class=\"input\"><label for=\"cp\">Planned replacement cost</label><input aria-label=\"Planned replacement cost\" type=\"number\" id=\"cp\" value=\"100\" min=\"1\" max=\"3000\" step=\"50\"><input aria-label=\"Slide Planned replacement cost\" id=\"slider-cp\" type=\"range\" value=\"100\" min=\"1\" max=\"3000\" step=\"50\"></div><div class=\"input\"><label for=\"cf\">Failure replacement cost</label><input aria-label=\"Failure replacement cost\" type=\"number\" id=\"cf\" value=\"1000\" min=\"1\" max=\"10000\" step=\"100\"><input aria-label=\"Slide Failure replacement cost\" id=\"slider-cf\" type=\"range\" value=\"1000\" min=\"1\" max=\"10000\" step=\"100\"></div></div><p class=\"math\">C(\u03c4)=[CpR(\u03c4)+Cf(1-R(\u03c4))]/\u222b[0,\u03c4]R(t)dt</p><div class=\"result\"><div class=\"small\">Calculated output</div><div class=\"value\" id=\"result\" aria-live=\"polite\">Loading</div></div><div class=\"plot\"><svg viewBox=\"0 0 620 220\" aria-label=\"Model sensitivity chart\" role=\"img\"><path d=\"M20 25V190H600\" fill=\"none\" stroke=\"#adbfc1\" stroke-width=\"1.5\"/><path id=\"curve\" d=\"M20 170L600 30\" fill=\"none\" stroke=\"#12796e\" stroke-width=\"3\" stroke-linecap=\"round\"/></svg><div id=\"x-label\" class=\"small\"></div><div id=\"y-label\" class=\"small\"></div></div></div><div class=\"hint\"><strong>Model limitation:</strong> Simplified renewal model, as-good-as-new replacement, Weibull life, failure replacement at event and no additional costs.</div><p class=\"small\">Trend plot changes the first input while holding the others constant. All values are illustrative and user-controlled.</p>",
    init: function(card) {
      try {
"use strict";
const names=["tau", "eta", "beta", "cp", "cf"];
function calc(p){return (()=>{let s=0,n=400,step=p.tau/n;for(let i=0;i<=n;i++){let t=i*step;let y=Math.exp(-Math.pow(t/p.eta,p.beta));s+=(i===0||i===n?0.5:1)*y;}let area=s*step;let r=Math.exp(-Math.pow(p.tau/p.eta,p.beta));return (p.cp*r+p.cf*(1-r))/Math.max(1e-12,area);})();}
function format(v){return v.toFixed(4)+' cost units per hour';}
function read(){let p={};p.tau=parseFloat(card.querySelector("#" + 'tau'.replace(/^#/, "")).value);p.eta=parseFloat(card.querySelector("#" + 'eta'.replace(/^#/, "")).value);p.beta=parseFloat(card.querySelector("#" + 'beta'.replace(/^#/, "")).value);p.cp=parseFloat(card.querySelector("#" + 'cp'.replace(/^#/, "")).value);p.cf=parseFloat(card.querySelector("#" + 'cf'.replace(/^#/, "")).value);return p;}
function update(){let p=read();if(!(Number.isFinite(p.tau) && p.tau>=20 && p.tau<=6000&&Number.isFinite(p.eta) && p.eta>=200 && p.eta<=10000&&Number.isFinite(p.beta) && p.beta>=0.5 && p.beta<=5&&Number.isFinite(p.cp) && p.cp>=1 && p.cp<=3000&&Number.isFinite(p.cf) && p.cf>=1 && p.cf<=10000)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Input outside permitted range';return;}let v=calc(p);card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?format(v):'Model not defined at this input';
const xmin=20,xmax=6000;let pts=[];for(let n=0;n<=80;n++){let x=xmin+(xmax-xmin)*n/80;let q={...p};q['tau']=x;let y=calc(q);if(Number.isFinite(y))pts.push([x,y]);}
if(pts.length>1){let ymin=Math.min(...pts.map(a=>a[1])),ymax=Math.max(...pts.map(a=>a[1]));if(Math.abs(ymax-ymin)<1e-12)ymax=ymin+1;let path=pts.map((a,n)=>`${n===0?'M':'L'}${(a[0]-xmin)/(xmax-xmin)*580+20},${190-(a[1]-ymin)/(ymax-ymin)*150}`).join(' ');card.querySelector("#" + 'curve'.replace(/^#/, "")).setAttribute('d',path);card.querySelector("#" + 'x-label'.replace(/^#/, "")).textContent='Replacement age τ (hours): '+xmin+' to '+xmax;card.querySelector("#" + 'y-label'.replace(/^#/, "")).textContent='Output range: '+format(ymin)+' to '+format(ymax);}
}
for(const name of names){let field=document.getElementById(name),slider=document.getElementById('slider-'+name);field.addEventListener('input',()=>{slider.value=field.value;update();});slider.addEventListener('input',()=>{field.value=slider.value;update();});}update();
      } catch (err) {
        console.warn('Sim init error in model 12:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 13,
    unit: 7,
    html: "<div class=\"hero\"><div class=\"eyebrow\">Interactive model 13 / Educational demonstration</div><h3>RMS vibration indicator</h3><p class=\"subtitle\">Modify assumptions and inspect how the idealized result changes.</p></div><p class=\"notice\">Not certified engineering software. Do not rely on this calculator for safety-critical or operational decisions.</p><div class=\"card\"><h2>Inputs</h2><div class=\"inputs\"><div class=\"input\"><label for=\"x1\">Sample 1 (mm/s)</label><input aria-label=\"Sample 1 (mm/s)\" type=\"number\" id=\"x1\" value=\"1\" min=\"-20\" max=\"20\" step=\"0.5\"><input aria-label=\"Slide Sample 1 (mm/s)\" id=\"slider-x1\" type=\"range\" value=\"1\" min=\"-20\" max=\"20\" step=\"0.5\"></div><div class=\"input\"><label for=\"x2\">Sample 2 (mm/s)</label><input aria-label=\"Sample 2 (mm/s)\" type=\"number\" id=\"x2\" value=\"-1\" min=\"-20\" max=\"20\" step=\"0.5\"><input aria-label=\"Slide Sample 2 (mm/s)\" id=\"slider-x2\" type=\"range\" value=\"-1\" min=\"-20\" max=\"20\" step=\"0.5\"></div><div class=\"input\"><label for=\"x3\">Sample 3 (mm/s)</label><input aria-label=\"Sample 3 (mm/s)\" type=\"number\" id=\"x3\" value=\"2\" min=\"-20\" max=\"20\" step=\"0.5\"><input aria-label=\"Slide Sample 3 (mm/s)\" id=\"slider-x3\" type=\"range\" value=\"2\" min=\"-20\" max=\"20\" step=\"0.5\"></div><div class=\"input\"><label for=\"x4\">Sample 4 (mm/s)</label><input aria-label=\"Sample 4 (mm/s)\" type=\"number\" id=\"x4\" value=\"-2\" min=\"-20\" max=\"20\" step=\"0.5\"><input aria-label=\"Slide Sample 4 (mm/s)\" id=\"slider-x4\" type=\"range\" value=\"-2\" min=\"-20\" max=\"20\" step=\"0.5\"></div></div><p class=\"math\">RMS=sqrt((x1\u00b2+x2\u00b2+x3\u00b2+x4\u00b2)/4)</p><div class=\"result\"><div class=\"small\">Calculated output</div><div class=\"value\" id=\"result\" aria-live=\"polite\">Loading</div></div><div class=\"plot\"><svg viewBox=\"0 0 620 220\" aria-label=\"Model sensitivity chart\" role=\"img\"><path d=\"M20 25V190H600\" fill=\"none\" stroke=\"#adbfc1\" stroke-width=\"1.5\"/><path id=\"curve\" d=\"M20 170L600 30\" fill=\"none\" stroke=\"#12796e\" stroke-width=\"3\" stroke-linecap=\"round\"/></svg><div id=\"x-label\" class=\"small\"></div><div id=\"y-label\" class=\"small\"></div></div></div><div class=\"hint\"><strong>Model limitation:</strong> Only an illustrative RMS of four velocity samples. No vibration severity or machinery health certification.</div><p class=\"small\">Trend plot changes the first input while holding the others constant. All values are illustrative and user-controlled.</p>",
    init: function(card) {
      try {
"use strict";
const names=["x1", "x2", "x3", "x4"];
function calc(p){return Math.sqrt((p.x1*p.x1+p.x2*p.x2+p.x3*p.x3+p.x4*p.x4)/4);}
function format(v){return v.toFixed(3)+' mm/s';}
function read(){let p={};p.x1=parseFloat(card.querySelector("#" + 'x1'.replace(/^#/, "")).value);p.x2=parseFloat(card.querySelector("#" + 'x2'.replace(/^#/, "")).value);p.x3=parseFloat(card.querySelector("#" + 'x3'.replace(/^#/, "")).value);p.x4=parseFloat(card.querySelector("#" + 'x4'.replace(/^#/, "")).value);return p;}
function update(){let p=read();if(!(Number.isFinite(p.x1) && p.x1>=-20 && p.x1<=20&&Number.isFinite(p.x2) && p.x2>=-20 && p.x2<=20&&Number.isFinite(p.x3) && p.x3>=-20 && p.x3<=20&&Number.isFinite(p.x4) && p.x4>=-20 && p.x4<=20)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Input outside permitted range';return;}let v=calc(p);card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?format(v):'Model not defined at this input';
const xmin=-20,xmax=20;let pts=[];for(let n=0;n<=80;n++){let x=xmin+(xmax-xmin)*n/80;let q={...p};q['x1']=x;let y=calc(q);if(Number.isFinite(y))pts.push([x,y]);}
if(pts.length>1){let ymin=Math.min(...pts.map(a=>a[1])),ymax=Math.max(...pts.map(a=>a[1]));if(Math.abs(ymax-ymin)<1e-12)ymax=ymin+1;let path=pts.map((a,n)=>`${n===0?'M':'L'}${(a[0]-xmin)/(xmax-xmin)*580+20},${190-(a[1]-ymin)/(ymax-ymin)*150}`).join(' ');card.querySelector("#" + 'curve'.replace(/^#/, "")).setAttribute('d',path);card.querySelector("#" + 'x-label'.replace(/^#/, "")).textContent='Sample 1 (mm/s): '+xmin+' to '+xmax;card.querySelector("#" + 'y-label'.replace(/^#/, "")).textContent='Output range: '+format(ymin)+' to '+format(ymax);}
}
for(const name of names){let field=document.getElementById(name),slider=document.getElementById('slider-'+name);field.addEventListener('input',()=>{slider.value=field.value;update();});slider.addEventListener('input',()=>{field.value=slider.value;update();});}update();
      } catch (err) {
        console.warn('Sim init error in model 13:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 14,
    unit: 7,
    html: "<div class=\"hero\"><div class=\"eyebrow\">Interactive model 14 / Educational demonstration</div><h3>Zero-failure upper intensity bound</h3><p class=\"subtitle\">Modify assumptions and inspect how the idealized result changes.</p></div><p class=\"notice\">Not certified engineering software. Do not rely on this calculator for safety-critical or operational decisions.</p><div class=\"card\"><h2>Inputs</h2><div class=\"inputs\"><div class=\"input\"><label for=\"hours\">Total independent test hours</label><input aria-label=\"Total independent test hours\" type=\"number\" id=\"hours\" value=\"3000\" min=\"10\" max=\"20000\" step=\"100\"><input aria-label=\"Slide Total independent test hours\" id=\"slider-hours\" type=\"range\" value=\"3000\" min=\"10\" max=\"20000\" step=\"100\"></div><div class=\"input\"><label for=\"confidence\">One-sided confidence level</label><input aria-label=\"One-sided confidence level\" type=\"number\" id=\"confidence\" value=\"0.95\" min=\"0.5\" max=\"0.999\" step=\"0.001\"><input aria-label=\"Slide One-sided confidence level\" id=\"slider-confidence\" type=\"range\" value=\"0.95\" min=\"0.5\" max=\"0.999\" step=\"0.001\"></div></div><p class=\"math\">\u03bb_upper=-ln(1-confidence)/total exposure</p><div class=\"result\"><div class=\"small\">Calculated output</div><div class=\"value\" id=\"result\" aria-live=\"polite\">Loading</div></div><div class=\"plot\"><svg viewBox=\"0 0 620 220\" aria-label=\"Model sensitivity chart\" role=\"img\"><path d=\"M20 25V190H600\" fill=\"none\" stroke=\"#adbfc1\" stroke-width=\"1.5\"/><path id=\"curve\" d=\"M20 170L600 30\" fill=\"none\" stroke=\"#12796e\" stroke-width=\"3\" stroke-linecap=\"round\"/></svg><div id=\"x-label\" class=\"small\"></div><div id=\"y-label\" class=\"small\"></div></div></div><div class=\"hint\"><strong>Model limitation:</strong> Assumes independent items and exponential first-failure time with no events; a confidence bound is not a lifetime guarantee.</div><p class=\"small\">Trend plot changes the first input while holding the others constant. All values are illustrative and user-controlled.</p>",
    init: function(card) {
      try {
"use strict";
const names=["hours", "confidence"];
function calc(p){return -Math.log(1-p.confidence)/p.hours;}
function format(v){return v.toFixed(6);}
function read(){let p={};p.hours=parseFloat(card.querySelector("#" + 'hours'.replace(/^#/, "")).value);p.confidence=parseFloat(card.querySelector("#" + 'confidence'.replace(/^#/, "")).value);return p;}
function update(){let p=read();if(!(Number.isFinite(p.hours) && p.hours>=10 && p.hours<=20000&&Number.isFinite(p.confidence) && p.confidence>=0.5 && p.confidence<=0.999)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Input outside permitted range';return;}let v=calc(p);card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?format(v):'Model not defined at this input';
const xmin=10,xmax=20000;let pts=[];for(let n=0;n<=80;n++){let x=xmin+(xmax-xmin)*n/80;let q={...p};q['hours']=x;let y=calc(q);if(Number.isFinite(y))pts.push([x,y]);}
if(pts.length>1){let ymin=Math.min(...pts.map(a=>a[1])),ymax=Math.max(...pts.map(a=>a[1]));if(Math.abs(ymax-ymin)<1e-12)ymax=ymin+1;let path=pts.map((a,n)=>`${n===0?'M':'L'}${(a[0]-xmin)/(xmax-xmin)*580+20},${190-(a[1]-ymin)/(ymax-ymin)*150}`).join(' ');card.querySelector("#" + 'curve'.replace(/^#/, "")).setAttribute('d',path);card.querySelector("#" + 'x-label'.replace(/^#/, "")).textContent='Total independent test hours: '+xmin+' to '+xmax;card.querySelector("#" + 'y-label'.replace(/^#/, "")).textContent='Output range: '+format(ymin)+' to '+format(ymax);}
}
for(const name of names){let field=document.getElementById(name),slider=document.getElementById('slider-'+name);field.addEventListener('input',()=>{slider.value=field.value;update();});slider.addEventListener('input',()=>{field.value=slider.value;update();});}update();
      } catch (err) {
        console.warn('Sim init error in model 14:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 15,
    unit: 8,
    html: "<div class=\"hero\"><div class=\"eyebrow\">Interactive model 15 / Educational demonstration</div><h3>Discounted net benefit</h3><p class=\"subtitle\">Modify assumptions and inspect how the idealized result changes.</p></div><p class=\"notice\">Not certified engineering software. Do not rely on this calculator for safety-critical or operational decisions.</p><div class=\"card\"><h2>Inputs</h2><div class=\"inputs\"><div class=\"input\"><label for=\"capital\">Initial investment</label><input aria-label=\"Initial investment\" type=\"number\" id=\"capital\" value=\"20000\" min=\"0\" max=\"50000\" step=\"1000\"><input aria-label=\"Slide Initial investment\" id=\"slider-capital\" type=\"range\" value=\"20000\" min=\"0\" max=\"50000\" step=\"1000\"></div><div class=\"input\"><label for=\"annual\">Annual saving</label><input aria-label=\"Annual saving\" type=\"number\" id=\"annual\" value=\"5000\" min=\"0\" max=\"20000\" step=\"500\"><input aria-label=\"Slide Annual saving\" id=\"slider-annual\" type=\"range\" value=\"5000\" min=\"0\" max=\"20000\" step=\"500\"></div><div class=\"input\"><label for=\"rate\">Discount rate</label><input aria-label=\"Discount rate\" type=\"number\" id=\"rate\" value=\"0.08\" min=\"0\" max=\"0.3\" step=\"0.01\"><input aria-label=\"Slide Discount rate\" id=\"slider-rate\" type=\"range\" value=\"0.08\" min=\"0\" max=\"0.3\" step=\"0.01\"></div><div class=\"input\"><label for=\"years\">Project life (years)</label><input aria-label=\"Project life (years)\" type=\"number\" id=\"years\" value=\"5\" min=\"1\" max=\"15\" step=\"1\"><input aria-label=\"Slide Project life (years)\" id=\"slider-years\" type=\"range\" value=\"5\" min=\"1\" max=\"15\" step=\"1\"></div></div><p class=\"math\">NPV=-capital+\u03a3 savings/(1+r)^year</p><div class=\"result\"><div class=\"small\">Calculated output</div><div class=\"value\" id=\"result\" aria-live=\"polite\">Loading</div></div><div class=\"plot\"><svg viewBox=\"0 0 620 220\" aria-label=\"Model sensitivity chart\" role=\"img\"><path d=\"M20 25V190H600\" fill=\"none\" stroke=\"#adbfc1\" stroke-width=\"1.5\"/><path id=\"curve\" d=\"M20 170L600 30\" fill=\"none\" stroke=\"#12796e\" stroke-width=\"3\" stroke-linecap=\"round\"/></svg><div id=\"x-label\" class=\"small\"></div><div id=\"y-label\" class=\"small\"></div></div></div><div class=\"hint\"><strong>Model limitation:</strong> Assumes fixed annual end-of-year savings and one initial investment; excludes taxes, residual value, uncertainty and safety constraints.</div><p class=\"small\">Trend plot changes the first input while holding the others constant. All values are illustrative and user-controlled.</p>",
    init: function(card) {
      try {
"use strict";
const names=["capital", "annual", "rate", "years"];
function calc(p){return (()=>{let total=-p.capital;for(let i=1;i<=Math.round(p.years);i++)total+=p.annual/Math.pow(1+p.rate,i);return total;})();}
function format(v){return v.toFixed(2)+' currency units';}
function read(){let p={};p.capital=parseFloat(card.querySelector("#" + 'capital'.replace(/^#/, "")).value);p.annual=parseFloat(card.querySelector("#" + 'annual'.replace(/^#/, "")).value);p.rate=parseFloat(card.querySelector("#" + 'rate'.replace(/^#/, "")).value);p.years=parseFloat(card.querySelector("#" + 'years'.replace(/^#/, "")).value);return p;}
function update(){let p=read();if(!(Number.isFinite(p.capital) && p.capital>=0 && p.capital<=50000&&Number.isFinite(p.annual) && p.annual>=0 && p.annual<=20000&&Number.isFinite(p.rate) && p.rate>=0 && p.rate<=0.3&&Number.isFinite(p.years) && p.years>=1 && p.years<=15)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Input outside permitted range';return;}let v=calc(p);card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?format(v):'Model not defined at this input';
const xmin=0,xmax=50000;let pts=[];for(let n=0;n<=80;n++){let x=xmin+(xmax-xmin)*n/80;let q={...p};q['capital']=x;let y=calc(q);if(Number.isFinite(y))pts.push([x,y]);}
if(pts.length>1){let ymin=Math.min(...pts.map(a=>a[1])),ymax=Math.max(...pts.map(a=>a[1]));if(Math.abs(ymax-ymin)<1e-12)ymax=ymin+1;let path=pts.map((a,n)=>`${n===0?'M':'L'}${(a[0]-xmin)/(xmax-xmin)*580+20},${190-(a[1]-ymin)/(ymax-ymin)*150}`).join(' ');card.querySelector("#" + 'curve'.replace(/^#/, "")).setAttribute('d',path);card.querySelector("#" + 'x-label'.replace(/^#/, "")).textContent='Initial investment: '+xmin+' to '+xmax;card.querySelector("#" + 'y-label'.replace(/^#/, "")).textContent='Output range: '+format(ymin)+' to '+format(ymax);}
}
for(const name of names){let field=document.getElementById(name),slider=document.getElementById('slider-'+name);field.addEventListener('input',()=>{slider.value=field.value;update();});slider.addEventListener('input',()=>{field.value=slider.value;update();});}update();
      } catch (err) {
        console.warn('Sim init error in model 15:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 16,
    unit: 8,
    html: "<div class=\"hero\"><div class=\"eyebrow\">Interactive model 16 / Educational demonstration</div><h3>Pump power and efficiency</h3><p class=\"subtitle\">Modify assumptions and inspect how the idealized result changes.</p></div><p class=\"notice\">Not certified engineering software. Do not rely on this calculator for safety-critical or operational decisions.</p><div class=\"card\"><h2>Inputs</h2><div class=\"inputs\"><div class=\"input\"><label for=\"rho\">Fluid density (kg/m\u00b3)</label><input aria-label=\"Fluid density (kg/m\u00b3)\" type=\"number\" id=\"rho\" value=\"1000\" min=\"200\" max=\"1500\" step=\"50\"><input aria-label=\"Slide Fluid density (kg/m\u00b3)\" id=\"slider-rho\" type=\"range\" value=\"1000\" min=\"200\" max=\"1500\" step=\"50\"></div><div class=\"input\"><label for=\"flow\">Volumetric flow (m\u00b3/s)</label><input aria-label=\"Volumetric flow (m\u00b3/s)\" type=\"number\" id=\"flow\" value=\"0.02\" min=\"0.001\" max=\"0.2\" step=\"0.005\"><input aria-label=\"Slide Volumetric flow (m\u00b3/s)\" id=\"slider-flow\" type=\"range\" value=\"0.02\" min=\"0.001\" max=\"0.2\" step=\"0.005\"></div><div class=\"input\"><label for=\"head\">Head (m)</label><input aria-label=\"Head (m)\" type=\"number\" id=\"head\" value=\"30\" min=\"1\" max=\"200\" step=\"1\"><input aria-label=\"Slide Head (m)\" id=\"slider-head\" type=\"range\" value=\"30\" min=\"1\" max=\"200\" step=\"1\"></div><div class=\"input\"><label for=\"eff\">Pump efficiency</label><input aria-label=\"Pump efficiency\" type=\"number\" id=\"eff\" value=\"0.7\" min=\"0.1\" max=\"1\" step=\"0.05\"><input aria-label=\"Slide Pump efficiency\" id=\"slider-eff\" type=\"range\" value=\"0.7\" min=\"0.1\" max=\"1\" step=\"0.05\"></div></div><p class=\"math\">Pshaft=\u03c1gQH/\u03b7</p><div class=\"result\"><div class=\"small\">Calculated output</div><div class=\"value\" id=\"result\" aria-live=\"polite\">Loading</div></div><div class=\"plot\"><svg viewBox=\"0 0 620 220\" aria-label=\"Model sensitivity chart\" role=\"img\"><path d=\"M20 25V190H600\" fill=\"none\" stroke=\"#adbfc1\" stroke-width=\"1.5\"/><path id=\"curve\" d=\"M20 170L600 30\" fill=\"none\" stroke=\"#12796e\" stroke-width=\"3\" stroke-linecap=\"round\"/></svg><div id=\"x-label\" class=\"small\"></div><div id=\"y-label\" class=\"small\"></div></div></div><div class=\"hint\"><strong>Model limitation:</strong> Idealized steady pump shaft-power estimate. Check real pump curves, measured operating point, motor efficiency and cavitation risk.</div><p class=\"small\">Trend plot changes the first input while holding the others constant. All values are illustrative and user-controlled.</p>",
    init: function(card) {
      try {
"use strict";
const names=["rho", "flow", "head", "eff"];
function calc(p){return p.rho*9.81*p.flow*p.head/(p.eff*1000);}
function format(v){return v.toFixed(3)+' kW';}
function read(){let p={};p.rho=parseFloat(card.querySelector("#" + 'rho'.replace(/^#/, "")).value);p.flow=parseFloat(card.querySelector("#" + 'flow'.replace(/^#/, "")).value);p.head=parseFloat(card.querySelector("#" + 'head'.replace(/^#/, "")).value);p.eff=parseFloat(card.querySelector("#" + 'eff'.replace(/^#/, "")).value);return p;}
function update(){let p=read();if(!(Number.isFinite(p.rho) && p.rho>=200 && p.rho<=1500&&Number.isFinite(p.flow) && p.flow>=0.001 && p.flow<=0.2&&Number.isFinite(p.head) && p.head>=1 && p.head<=200&&Number.isFinite(p.eff) && p.eff>=0.1 && p.eff<=1)){card.querySelector("#" + 'result'.replace(/^#/, "")).textContent='Input outside permitted range';return;}let v=calc(p);card.querySelector("#" + 'result'.replace(/^#/, "")).textContent=Number.isFinite(v)?format(v):'Model not defined at this input';
const xmin=200,xmax=1500;let pts=[];for(let n=0;n<=80;n++){let x=xmin+(xmax-xmin)*n/80;let q={...p};q['rho']=x;let y=calc(q);if(Number.isFinite(y))pts.push([x,y]);}
if(pts.length>1){let ymin=Math.min(...pts.map(a=>a[1])),ymax=Math.max(...pts.map(a=>a[1]));if(Math.abs(ymax-ymin)<1e-12)ymax=ymin+1;let path=pts.map((a,n)=>`${n===0?'M':'L'}${(a[0]-xmin)/(xmax-xmin)*580+20},${190-(a[1]-ymin)/(ymax-ymin)*150}`).join(' ');card.querySelector("#" + 'curve'.replace(/^#/, "")).setAttribute('d',path);card.querySelector("#" + 'x-label'.replace(/^#/, "")).textContent='Fluid density (kg/m³): '+xmin+' to '+xmax;card.querySelector("#" + 'y-label'.replace(/^#/, "")).textContent='Output range: '+format(ymin)+' to '+format(ymax);}
}
for(const name of names){let field=document.getElementById(name),slider=document.getElementById('slider-'+name);field.addEventListener('input',()=>{slider.value=field.value;update();});slider.addEventListener('input',()=>{field.value=slider.value;update();});}update();
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
