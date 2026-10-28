/* power-plant-engineering Interactive Simulation Suite */
(function(window) {
  'use strict';

  var OPENSTEM_SIM_MODELS = [];

  OPENSTEM_SIM_MODELS.push({
    idx: 1,
    unit: 1,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 16</div><h3>Net plant thermal efficiency</h3><p class=\"subtitle\">An offline educational reader \u00b7 original draft \u00b7 8 units \u00b7 40 lessons \u00b7 16 interactive calculators.</p></header><p class=\"notice\"><strong>Limitations:</strong> P_net and Q_fuel must be for the same operating interval and heating-value basis.</p><article class=\"model-panel\"><h2>Model 01 \u00b7 Net plant thermal efficiency</h2><p><strong>Model relation:</strong> <code>eta = P_net/Q_fuel</code></p><p class=\"small\">P_net and Q_fuel must be for the same operating interval and heating-value basis.</p><div class=\"fields\"><label for=\"p\">Net electric power (MW(e))<input id=\"p\" type=\"number\" min=\"1\" max=\"1500\" step=\"any\" value=\"140\"></label><label for=\"q\">Fuel input (MW(th))<input id=\"q\" type=\"number\" min=\"1\" max=\"4000\" step=\"any\" value=\"380\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" class=\"small\" aria-live=\"polite\">Change an input to update.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 220\" aria-label=\"Output sensitivity as the first input varies\"></svg><p class=\"small\">Actual input sweep: first input \u00b120%, bounded by its declared limits. Dots represent recalculated model output; the curve is not measured plant behavior.</p></article><p class=\"footer\">\u00a9 OpenSTEM \u00b7 Educational draft \u00b7 Engineering calculations are simplified and not certified for real facilities.</p>",
    init: function(card) {
      try {
// OpenSTEM educational model 01; local, offline and self-contained.
// Formula: eta = P_net/Q_fuel
const modelIndex=1;
function compute(p,q){ return (p/q)*100; }
function update(){
 const p = Number(card.querySelector("#" + "p".replace(/^#/, "")).value);
const q = Number(card.querySelector("#" + "q".replace(/^#/, "")).value);
 const valid=Number.isFinite(p) && p>=1 && p<=1500 && Number.isFinite(q) && q>=1 && q<=4000 && (p<=q);
 const display=card.querySelector("#" + 'metric'.replace(/^#/, "")); const desc=card.querySelector("#" + 'details'.replace(/^#/, ""));
 if(!valid){display.textContent='—';desc.textContent='Invalid parameters: inspect the input limits and physical state order.';card.querySelector("#" + 'plot'.replace(/^#/, "")).textContent='';return;}
 const y=compute(p,q);
 if(!Number.isFinite(y)||Math.abs(y)>1e12){display.textContent='—';desc.textContent='Unphysical or undefined result.';return;}
 display.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' %';
 desc.textContent="P_net and Q_fuel must be for the same operating interval and heating-value basis.";
 const xmin=Math.max(1,p*0.8),xmax=Math.min(1500,p*1.2);
 const vals=[];
 for(let k=0;k<=40;k++){
   const x=xmin+(xmax-xmin)*k/40;
   const val=compute(x,q);
   if(Number.isFinite(val)) vals.push([x,val]);
 }
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(vals.length<2){plot.textContent='';return;}
 const low=Math.min(...vals.map(p=>p[1])),high=Math.max(...vals.map(p=>p[1]));
 const delta=Math.max(1e-9,high-low);
 const points=vals.map((p,j)=>`${45+605*j/(vals.length-1)},${179-128*(p[1]-low)/delta}`).join(' ');
 const cy=179-128*(y-low)/delta;
 plot.innerHTML=`<line x1="45" y1="184" x2="652" y2="184" stroke="#99adb9"/><line x1="45" y1="26" x2="45" y2="184" stroke="#99adb9"/><polyline points="${points}" stroke="#147d89" stroke-width="3" fill="none"/><circle cx="${45+605*(p-xmin)/Math.max(1e-10,xmax-xmin)}" cy="${cy}" r="5" fill="#e19a32"/><text x="52" y="20" font-size="13" fill="#335667">Net electric power sensitivity (units MW(e))</text><text x="55" y="205" font-size="12" fill="#335667">${xmin.toPrecision(4)}</text><text x="595" y="205" font-size="12" fill="#335667">${xmax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 2,
    unit: 1,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 16</div><h3>Net heat rate</h3><p class=\"subtitle\">An offline educational reader \u00b7 original draft \u00b7 8 units \u00b7 40 lessons \u00b7 16 interactive calculators.</p></header><p class=\"notice\"><strong>Limitations:</strong> Heat rate refers to net electricity and requires a consistent LHV or HHV fuel basis.</p><article class=\"model-panel\"><h2>Model 02 \u00b7 Net heat rate</h2><p><strong>Model relation:</strong> <code>Heat rate = 3600/eta</code></p><p class=\"small\">Heat rate refers to net electricity and requires a consistent LHV or HHV fuel basis.</p><div class=\"fields\"><label for=\"e\">Net thermal efficiency (%)<input id=\"e\" type=\"number\" min=\"1\" max=\"90\" step=\"any\" value=\"38\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" class=\"small\" aria-live=\"polite\">Change an input to update.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 220\" aria-label=\"Output sensitivity as the first input varies\"></svg><p class=\"small\">Actual input sweep: first input \u00b120%, bounded by its declared limits. Dots represent recalculated model output; the curve is not measured plant behavior.</p></article><p class=\"footer\">\u00a9 OpenSTEM \u00b7 Educational draft \u00b7 Engineering calculations are simplified and not certified for real facilities.</p>",
    init: function(card) {
      try {
// OpenSTEM educational model 02; local, offline and self-contained.
// Formula: Heat rate = 3600/eta
const modelIndex=2;
function compute(e){ return 360000/e; }
function update(){
 const e = Number(card.querySelector("#" + "e".replace(/^#/, "")).value);
 const valid=Number.isFinite(e) && e>=1 && e<=90 && (true);
 const display=card.querySelector("#" + 'metric'.replace(/^#/, "")); const desc=card.querySelector("#" + 'details'.replace(/^#/, ""));
 if(!valid){display.textContent='—';desc.textContent='Invalid parameters: inspect the input limits and physical state order.';card.querySelector("#" + 'plot'.replace(/^#/, "")).textContent='';return;}
 const y=compute(e);
 if(!Number.isFinite(y)||Math.abs(y)>1e12){display.textContent='—';desc.textContent='Unphysical or undefined result.';return;}
 display.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' kJ/kWh';
 desc.textContent="Heat rate refers to net electricity and requires a consistent LHV or HHV fuel basis.";
 const xmin=Math.max(1,e*0.8),xmax=Math.min(90,e*1.2);
 const vals=[];
 for(let k=0;k<=40;k++){
   const x=xmin+(xmax-xmin)*k/40;
   const val=compute(x);
   if(Number.isFinite(val)) vals.push([x,val]);
 }
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(vals.length<2){plot.textContent='';return;}
 const low=Math.min(...vals.map(p=>p[1])),high=Math.max(...vals.map(p=>p[1]));
 const delta=Math.max(1e-9,high-low);
 const points=vals.map((p,j)=>`${45+605*j/(vals.length-1)},${179-128*(p[1]-low)/delta}`).join(' ');
 const cy=179-128*(y-low)/delta;
 plot.innerHTML=`<line x1="45" y1="184" x2="652" y2="184" stroke="#99adb9"/><line x1="45" y1="26" x2="45" y2="184" stroke="#99adb9"/><polyline points="${points}" stroke="#147d89" stroke-width="3" fill="none"/><circle cx="${45+605*(e-xmin)/Math.max(1e-10,xmax-xmin)}" cy="${cy}" r="5" fill="#e19a32"/><text x="52" y="20" font-size="13" fill="#335667">Net thermal efficiency sensitivity (units %)</text><text x="55" y="205" font-size="12" fill="#335667">${xmin.toPrecision(4)}</text><text x="595" y="205" font-size="12" fill="#335667">${xmax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 3,
    unit: 2,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 16</div><h3>Annual energy and capacity factor</h3><p class=\"subtitle\">An offline educational reader \u00b7 original draft \u00b7 8 units \u00b7 40 lessons \u00b7 16 interactive calculators.</p></header><p class=\"notice\"><strong>Limitations:</strong> 8760 hours represents a conventional 365-day analysis year.</p><article class=\"model-panel\"><h2>Model 03 \u00b7 Annual energy and capacity factor</h2><p><strong>Model relation:</strong> <code>E = P*CF*8760</code></p><p class=\"small\">8760 hours represents a conventional 365-day analysis year.</p><div class=\"fields\"><label for=\"p\">Rated net power (MW)<input id=\"p\" type=\"number\" min=\"1\" max=\"1500\" step=\"any\" value=\"150\"></label><label for=\"c\">Capacity factor (%)<input id=\"c\" type=\"number\" min=\"0\" max=\"100\" step=\"any\" value=\"65\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" class=\"small\" aria-live=\"polite\">Change an input to update.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 220\" aria-label=\"Output sensitivity as the first input varies\"></svg><p class=\"small\">Actual input sweep: first input \u00b120%, bounded by its declared limits. Dots represent recalculated model output; the curve is not measured plant behavior.</p></article><p class=\"footer\">\u00a9 OpenSTEM \u00b7 Educational draft \u00b7 Engineering calculations are simplified and not certified for real facilities.</p>",
    init: function(card) {
      try {
// OpenSTEM educational model 03; local, offline and self-contained.
// Formula: E = P*CF*8760
const modelIndex=3;
function compute(p,c){ return p*c/100*8760; }
function update(){
 const p = Number(card.querySelector("#" + "p".replace(/^#/, "")).value);
const c = Number(card.querySelector("#" + "c".replace(/^#/, "")).value);
 const valid=Number.isFinite(p) && p>=1 && p<=1500 && Number.isFinite(c) && c>=0 && c<=100 && (true);
 const display=card.querySelector("#" + 'metric'.replace(/^#/, "")); const desc=card.querySelector("#" + 'details'.replace(/^#/, ""));
 if(!valid){display.textContent='—';desc.textContent='Invalid parameters: inspect the input limits and physical state order.';card.querySelector("#" + 'plot'.replace(/^#/, "")).textContent='';return;}
 const y=compute(p,c);
 if(!Number.isFinite(y)||Math.abs(y)>1e12){display.textContent='—';desc.textContent='Unphysical or undefined result.';return;}
 display.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' MWh/year';
 desc.textContent="8760 hours represents a conventional 365-day analysis year.";
 const xmin=Math.max(1,p*0.8),xmax=Math.min(1500,p*1.2);
 const vals=[];
 for(let k=0;k<=40;k++){
   const x=xmin+(xmax-xmin)*k/40;
   const val=compute(x,c);
   if(Number.isFinite(val)) vals.push([x,val]);
 }
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(vals.length<2){plot.textContent='';return;}
 const low=Math.min(...vals.map(p=>p[1])),high=Math.max(...vals.map(p=>p[1]));
 const delta=Math.max(1e-9,high-low);
 const points=vals.map((p,j)=>`${45+605*j/(vals.length-1)},${179-128*(p[1]-low)/delta}`).join(' ');
 const cy=179-128*(y-low)/delta;
 plot.innerHTML=`<line x1="45" y1="184" x2="652" y2="184" stroke="#99adb9"/><line x1="45" y1="26" x2="45" y2="184" stroke="#99adb9"/><polyline points="${points}" stroke="#147d89" stroke-width="3" fill="none"/><circle cx="${45+605*(p-xmin)/Math.max(1e-10,xmax-xmin)}" cy="${cy}" r="5" fill="#e19a32"/><text x="52" y="20" font-size="13" fill="#335667">Rated net power sensitivity (units MW)</text><text x="55" y="205" font-size="12" fill="#335667">${xmin.toPrecision(4)}</text><text x="595" y="205" font-size="12" fill="#335667">${xmax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 4,
    unit: 2,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 16</div><h3>Steam generator heat duty</h3><p class=\"subtitle\">An offline educational reader \u00b7 original draft \u00b7 8 units \u00b7 40 lessons \u00b7 16 interactive calculators.</p></header><p class=\"notice\"><strong>Limitations:</strong> An illustrative enthalpy difference, not a calculation of steam state properties.</p><article class=\"model-panel\"><h2>Model 04 \u00b7 Steam generator heat duty</h2><p><strong>Model relation:</strong> <code>Q = m_dot*(h_out-h_in)</code></p><p class=\"small\">An illustrative enthalpy difference, not a calculation of steam state properties.</p><div class=\"fields\"><label for=\"m\">Steam mass flow (kg/s)<input id=\"m\" type=\"number\" min=\"0.1\" max=\"2000\" step=\"any\" value=\"25\"></label><label for=\"h1\">Feedwater enthalpy (kJ/kg)<input id=\"h1\" type=\"number\" min=\"0\" max=\"3800\" step=\"any\" value=\"800\"></label><label for=\"h2\">Steam enthalpy (kJ/kg)<input id=\"h2\" type=\"number\" min=\"0\" max=\"4500\" step=\"any\" value=\"3200\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" class=\"small\" aria-live=\"polite\">Change an input to update.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 220\" aria-label=\"Output sensitivity as the first input varies\"></svg><p class=\"small\">Actual input sweep: first input \u00b120%, bounded by its declared limits. Dots represent recalculated model output; the curve is not measured plant behavior.</p></article><p class=\"footer\">\u00a9 OpenSTEM \u00b7 Educational draft \u00b7 Engineering calculations are simplified and not certified for real facilities.</p>",
    init: function(card) {
      try {
// OpenSTEM educational model 04; local, offline and self-contained.
// Formula: Q = m_dot*(h_out-h_in)
const modelIndex=4;
function compute(m,h1,h2){ return m*(h2-h1); }
function update(){
 const m = Number(card.querySelector("#" + "m".replace(/^#/, "")).value);
const h1 = Number(card.querySelector("#" + "h1".replace(/^#/, "")).value);
const h2 = Number(card.querySelector("#" + "h2".replace(/^#/, "")).value);
 const valid=Number.isFinite(m) && m>=0.1 && m<=2000 && Number.isFinite(h1) && h1>=0 && h1<=3800 && Number.isFinite(h2) && h2>=0 && h2<=4500 && (h2>h1);
 const display=card.querySelector("#" + 'metric'.replace(/^#/, "")); const desc=card.querySelector("#" + 'details'.replace(/^#/, ""));
 if(!valid){display.textContent='—';desc.textContent='Invalid parameters: inspect the input limits and physical state order.';card.querySelector("#" + 'plot'.replace(/^#/, "")).textContent='';return;}
 const y=compute(m,h1,h2);
 if(!Number.isFinite(y)||Math.abs(y)>1e12){display.textContent='—';desc.textContent='Unphysical or undefined result.';return;}
 display.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' kW';
 desc.textContent="An illustrative enthalpy difference, not a calculation of steam state properties.";
 const xmin=Math.max(0.1,m*0.8),xmax=Math.min(2000,m*1.2);
 const vals=[];
 for(let k=0;k<=40;k++){
   const x=xmin+(xmax-xmin)*k/40;
   const val=compute(x,h1,h2);
   if(Number.isFinite(val)) vals.push([x,val]);
 }
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(vals.length<2){plot.textContent='';return;}
 const low=Math.min(...vals.map(p=>p[1])),high=Math.max(...vals.map(p=>p[1]));
 const delta=Math.max(1e-9,high-low);
 const points=vals.map((p,j)=>`${45+605*j/(vals.length-1)},${179-128*(p[1]-low)/delta}`).join(' ');
 const cy=179-128*(y-low)/delta;
 plot.innerHTML=`<line x1="45" y1="184" x2="652" y2="184" stroke="#99adb9"/><line x1="45" y1="26" x2="45" y2="184" stroke="#99adb9"/><polyline points="${points}" stroke="#147d89" stroke-width="3" fill="none"/><circle cx="${45+605*(m-xmin)/Math.max(1e-10,xmax-xmin)}" cy="${cy}" r="5" fill="#e19a32"/><text x="52" y="20" font-size="13" fill="#335667">Steam mass flow sensitivity (units kg/s)</text><text x="55" y="205" font-size="12" fill="#335667">${xmin.toPrecision(4)}</text><text x="595" y="205" font-size="12" fill="#335667">${xmax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 5,
    unit: 3,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 16</div><h3>Steam turbine indicated power</h3><p class=\"subtitle\">An offline educational reader \u00b7 original draft \u00b7 8 units \u00b7 40 lessons \u00b7 16 interactive calculators.</p></header><p class=\"notice\"><strong>Limitations:</strong> Neglects extraction branches, mechanical losses and kinetic-energy changes.</p><article class=\"model-panel\"><h2>Model 05 \u00b7 Steam turbine indicated power</h2><p><strong>Model relation:</strong> <code>P = m_dot*(h_in-h_out)</code></p><p class=\"small\">Neglects extraction branches, mechanical losses and kinetic-energy changes.</p><div class=\"fields\"><label for=\"m\">Steam flow (kg/s)<input id=\"m\" type=\"number\" min=\"0.1\" max=\"2000\" step=\"any\" value=\"40\"></label><label for=\"h1\">Inlet enthalpy (kJ/kg)<input id=\"h1\" type=\"number\" min=\"100\" max=\"4500\" step=\"any\" value=\"3400\"></label><label for=\"h2\">Outlet enthalpy (kJ/kg)<input id=\"h2\" type=\"number\" min=\"100\" max=\"4500\" step=\"any\" value=\"2500\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" class=\"small\" aria-live=\"polite\">Change an input to update.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 220\" aria-label=\"Output sensitivity as the first input varies\"></svg><p class=\"small\">Actual input sweep: first input \u00b120%, bounded by its declared limits. Dots represent recalculated model output; the curve is not measured plant behavior.</p></article><p class=\"footer\">\u00a9 OpenSTEM \u00b7 Educational draft \u00b7 Engineering calculations are simplified and not certified for real facilities.</p>",
    init: function(card) {
      try {
// OpenSTEM educational model 05; local, offline and self-contained.
// Formula: P = m_dot*(h_in-h_out)
const modelIndex=5;
function compute(m,h1,h2){ return m*(h1-h2); }
function update(){
 const m = Number(card.querySelector("#" + "m".replace(/^#/, "")).value);
const h1 = Number(card.querySelector("#" + "h1".replace(/^#/, "")).value);
const h2 = Number(card.querySelector("#" + "h2".replace(/^#/, "")).value);
 const valid=Number.isFinite(m) && m>=0.1 && m<=2000 && Number.isFinite(h1) && h1>=100 && h1<=4500 && Number.isFinite(h2) && h2>=100 && h2<=4500 && (h1>h2);
 const display=card.querySelector("#" + 'metric'.replace(/^#/, "")); const desc=card.querySelector("#" + 'details'.replace(/^#/, ""));
 if(!valid){display.textContent='—';desc.textContent='Invalid parameters: inspect the input limits and physical state order.';card.querySelector("#" + 'plot'.replace(/^#/, "")).textContent='';return;}
 const y=compute(m,h1,h2);
 if(!Number.isFinite(y)||Math.abs(y)>1e12){display.textContent='—';desc.textContent='Unphysical or undefined result.';return;}
 display.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' kW';
 desc.textContent="Neglects extraction branches, mechanical losses and kinetic-energy changes.";
 const xmin=Math.max(0.1,m*0.8),xmax=Math.min(2000,m*1.2);
 const vals=[];
 for(let k=0;k<=40;k++){
   const x=xmin+(xmax-xmin)*k/40;
   const val=compute(x,h1,h2);
   if(Number.isFinite(val)) vals.push([x,val]);
 }
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(vals.length<2){plot.textContent='';return;}
 const low=Math.min(...vals.map(p=>p[1])),high=Math.max(...vals.map(p=>p[1]));
 const delta=Math.max(1e-9,high-low);
 const points=vals.map((p,j)=>`${45+605*j/(vals.length-1)},${179-128*(p[1]-low)/delta}`).join(' ');
 const cy=179-128*(y-low)/delta;
 plot.innerHTML=`<line x1="45" y1="184" x2="652" y2="184" stroke="#99adb9"/><line x1="45" y1="26" x2="45" y2="184" stroke="#99adb9"/><polyline points="${points}" stroke="#147d89" stroke-width="3" fill="none"/><circle cx="${45+605*(m-xmin)/Math.max(1e-10,xmax-xmin)}" cy="${cy}" r="5" fill="#e19a32"/><text x="52" y="20" font-size="13" fill="#335667">Steam flow sensitivity (units kg/s)</text><text x="55" y="205" font-size="12" fill="#335667">${xmin.toPrecision(4)}</text><text x="595" y="205" font-size="12" fill="#335667">${xmax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 6,
    unit: 3,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 16</div><h3>Liquid feedwater pump power</h3><p class=\"subtitle\">An offline educational reader \u00b7 original draft \u00b7 8 units \u00b7 40 lessons \u00b7 16 interactive calculators.</p></header><p class=\"notice\"><strong>Limitations:</strong> Near-incompressible liquid approximation; pressure is entered in MPa.</p><article class=\"model-panel\"><h2>Model 06 \u00b7 Liquid feedwater pump power</h2><p><strong>Model relation:</strong> <code>P = m_dot*v*DeltaP/eta</code></p><p class=\"small\">Near-incompressible liquid approximation; pressure is entered in MPa.</p><div class=\"fields\"><label for=\"m\">Liquid flow (kg/s)<input id=\"m\" type=\"number\" min=\"0.1\" max=\"2000\" step=\"any\" value=\"20\"></label><label for=\"v\">Specific volume (m\u00b3/kg)<input id=\"v\" type=\"number\" min=\"0.0005\" max=\"0.003\" step=\"any\" value=\"0.001\"></label><label for=\"dp\">Pressure rise (MPa)<input id=\"dp\" type=\"number\" min=\"0.01\" max=\"40\" step=\"any\" value=\"12\"></label><label for=\"eta\">Pump efficiency (%)<input id=\"eta\" type=\"number\" min=\"20\" max=\"100\" step=\"any\" value=\"75\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" class=\"small\" aria-live=\"polite\">Change an input to update.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 220\" aria-label=\"Output sensitivity as the first input varies\"></svg><p class=\"small\">Actual input sweep: first input \u00b120%, bounded by its declared limits. Dots represent recalculated model output; the curve is not measured plant behavior.</p></article><p class=\"footer\">\u00a9 OpenSTEM \u00b7 Educational draft \u00b7 Engineering calculations are simplified and not certified for real facilities.</p>",
    init: function(card) {
      try {
// OpenSTEM educational model 06; local, offline and self-contained.
// Formula: P = m_dot*v*DeltaP/eta
const modelIndex=6;
function compute(m,v,dp,eta){ return m*v*dp*1000/(eta/100); }
function update(){
 const m = Number(card.querySelector("#" + "m".replace(/^#/, "")).value);
const v = Number(card.querySelector("#" + "v".replace(/^#/, "")).value);
const dp = Number(card.querySelector("#" + "dp".replace(/^#/, "")).value);
const eta = Number(card.querySelector("#" + "eta".replace(/^#/, "")).value);
 const valid=Number.isFinite(m) && m>=0.1 && m<=2000 && Number.isFinite(v) && v>=0.0005 && v<=0.003 && Number.isFinite(dp) && dp>=0.01 && dp<=40 && Number.isFinite(eta) && eta>=20 && eta<=100 && (true);
 const display=card.querySelector("#" + 'metric'.replace(/^#/, "")); const desc=card.querySelector("#" + 'details'.replace(/^#/, ""));
 if(!valid){display.textContent='—';desc.textContent='Invalid parameters: inspect the input limits and physical state order.';card.querySelector("#" + 'plot'.replace(/^#/, "")).textContent='';return;}
 const y=compute(m,v,dp,eta);
 if(!Number.isFinite(y)||Math.abs(y)>1e12){display.textContent='—';desc.textContent='Unphysical or undefined result.';return;}
 display.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' kW';
 desc.textContent="Near-incompressible liquid approximation; pressure is entered in MPa.";
 const xmin=Math.max(0.1,m*0.8),xmax=Math.min(2000,m*1.2);
 const vals=[];
 for(let k=0;k<=40;k++){
   const x=xmin+(xmax-xmin)*k/40;
   const val=compute(x,v,dp,eta);
   if(Number.isFinite(val)) vals.push([x,val]);
 }
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(vals.length<2){plot.textContent='';return;}
 const low=Math.min(...vals.map(p=>p[1])),high=Math.max(...vals.map(p=>p[1]));
 const delta=Math.max(1e-9,high-low);
 const points=vals.map((p,j)=>`${45+605*j/(vals.length-1)},${179-128*(p[1]-low)/delta}`).join(' ');
 const cy=179-128*(y-low)/delta;
 plot.innerHTML=`<line x1="45" y1="184" x2="652" y2="184" stroke="#99adb9"/><line x1="45" y1="26" x2="45" y2="184" stroke="#99adb9"/><polyline points="${points}" stroke="#147d89" stroke-width="3" fill="none"/><circle cx="${45+605*(m-xmin)/Math.max(1e-10,xmax-xmin)}" cy="${cy}" r="5" fill="#e19a32"/><text x="52" y="20" font-size="13" fill="#335667">Liquid flow sensitivity (units kg/s)</text><text x="55" y="205" font-size="12" fill="#335667">${xmin.toPrecision(4)}</text><text x="595" y="205" font-size="12" fill="#335667">${xmax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 7,
    unit: 4,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 16</div><h3>Ideal Brayton efficiency</h3><p class=\"subtitle\">An offline educational reader \u00b7 original draft \u00b7 8 units \u00b7 40 lessons \u00b7 16 interactive calculators.</p></header><p class=\"notice\"><strong>Limitations:</strong> Assumes reversible constant-property air-standard cycle; not actual gas-turbine efficiency.</p><article class=\"model-panel\"><h2>Model 07 \u00b7 Ideal Brayton efficiency</h2><p><strong>Model relation:</strong> <code>eta = 1-r_p^(-(gamma-1)/gamma)</code></p><p class=\"small\">Assumes reversible constant-property air-standard cycle; not actual gas-turbine efficiency.</p><div class=\"fields\"><label for=\"rp\">Pressure ratio (ratio)<input id=\"rp\" type=\"number\" min=\"1.01\" max=\"50\" step=\"any\" value=\"12\"></label><label for=\"g\">Heat-capacity ratio (ratio)<input id=\"g\" type=\"number\" min=\"1.1\" max=\"1.67\" step=\"any\" value=\"1.4\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" class=\"small\" aria-live=\"polite\">Change an input to update.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 220\" aria-label=\"Output sensitivity as the first input varies\"></svg><p class=\"small\">Actual input sweep: first input \u00b120%, bounded by its declared limits. Dots represent recalculated model output; the curve is not measured plant behavior.</p></article><p class=\"footer\">\u00a9 OpenSTEM \u00b7 Educational draft \u00b7 Engineering calculations are simplified and not certified for real facilities.</p>",
    init: function(card) {
      try {
// OpenSTEM educational model 07; local, offline and self-contained.
// Formula: eta = 1-r_p^(-(gamma-1)/gamma)
const modelIndex=7;
function compute(rp,g){ return (1-Math.pow(rp,-(g-1)/g))*100; }
function update(){
 const rp = Number(card.querySelector("#" + "rp".replace(/^#/, "")).value);
const g = Number(card.querySelector("#" + "g".replace(/^#/, "")).value);
 const valid=Number.isFinite(rp) && rp>=1.01 && rp<=50 && Number.isFinite(g) && g>=1.1 && g<=1.67 && (true);
 const display=card.querySelector("#" + 'metric'.replace(/^#/, "")); const desc=card.querySelector("#" + 'details'.replace(/^#/, ""));
 if(!valid){display.textContent='—';desc.textContent='Invalid parameters: inspect the input limits and physical state order.';card.querySelector("#" + 'plot'.replace(/^#/, "")).textContent='';return;}
 const y=compute(rp,g);
 if(!Number.isFinite(y)||Math.abs(y)>1e12){display.textContent='—';desc.textContent='Unphysical or undefined result.';return;}
 display.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' %';
 desc.textContent="Assumes reversible constant-property air-standard cycle; not actual gas-turbine efficiency.";
 const xmin=Math.max(1.01,rp*0.8),xmax=Math.min(50,rp*1.2);
 const vals=[];
 for(let k=0;k<=40;k++){
   const x=xmin+(xmax-xmin)*k/40;
   const val=compute(x,g);
   if(Number.isFinite(val)) vals.push([x,val]);
 }
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(vals.length<2){plot.textContent='';return;}
 const low=Math.min(...vals.map(p=>p[1])),high=Math.max(...vals.map(p=>p[1]));
 const delta=Math.max(1e-9,high-low);
 const points=vals.map((p,j)=>`${45+605*j/(vals.length-1)},${179-128*(p[1]-low)/delta}`).join(' ');
 const cy=179-128*(y-low)/delta;
 plot.innerHTML=`<line x1="45" y1="184" x2="652" y2="184" stroke="#99adb9"/><line x1="45" y1="26" x2="45" y2="184" stroke="#99adb9"/><polyline points="${points}" stroke="#147d89" stroke-width="3" fill="none"/><circle cx="${45+605*(rp-xmin)/Math.max(1e-10,xmax-xmin)}" cy="${cy}" r="5" fill="#e19a32"/><text x="52" y="20" font-size="13" fill="#335667">Pressure ratio sensitivity (units ratio)</text><text x="55" y="205" font-size="12" fill="#335667">${xmin.toPrecision(4)}</text><text x="595" y="205" font-size="12" fill="#335667">${xmax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 8,
    unit: 4,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 16</div><h3>Gas-turbine specific net work</h3><p class=\"subtitle\">An offline educational reader \u00b7 original draft \u00b7 8 units \u00b7 40 lessons \u00b7 16 interactive calculators.</p></header><p class=\"notice\"><strong>Limitations:</strong> Simplified cycle; real turbines involve fuel-air mass differences and varying specific heat.</p><article class=\"model-panel\"><h2>Model 08 \u00b7 Gas-turbine specific net work</h2><p><strong>Model relation:</strong> <code>w_net = cp*(T3-T4-T2+T1)</code></p><p class=\"small\">Simplified cycle; real turbines involve fuel-air mass differences and varying specific heat.</p><div class=\"fields\"><label for=\"cp\">Specific heat (kJ/(kg K))<input id=\"cp\" type=\"number\" min=\"0.8\" max=\"1.3\" step=\"any\" value=\"1.05\"></label><label for=\"t1\">Compressor inlet (K)<input id=\"t1\" type=\"number\" min=\"220\" max=\"450\" step=\"any\" value=\"300\"></label><label for=\"t2\">Compressor outlet (K)<input id=\"t2\" type=\"number\" min=\"250\" max=\"1100\" step=\"any\" value=\"600\"></label><label for=\"t3\">Turbine inlet (K)<input id=\"t3\" type=\"number\" min=\"700\" max=\"2000\" step=\"any\" value=\"1350\"></label><label for=\"t4\">Turbine outlet (K)<input id=\"t4\" type=\"number\" min=\"300\" max=\"1500\" step=\"any\" value=\"850\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" class=\"small\" aria-live=\"polite\">Change an input to update.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 220\" aria-label=\"Output sensitivity as the first input varies\"></svg><p class=\"small\">Actual input sweep: first input \u00b120%, bounded by its declared limits. Dots represent recalculated model output; the curve is not measured plant behavior.</p></article><p class=\"footer\">\u00a9 OpenSTEM \u00b7 Educational draft \u00b7 Engineering calculations are simplified and not certified for real facilities.</p>",
    init: function(card) {
      try {
// OpenSTEM educational model 08; local, offline and self-contained.
// Formula: w_net = cp*(T3-T4-T2+T1)
const modelIndex=8;
function compute(cp,t1,t2,t3,t4){ return cp*((t3-t4)-(t2-t1)); }
function update(){
 const cp = Number(card.querySelector("#" + "cp".replace(/^#/, "")).value);
const t1 = Number(card.querySelector("#" + "t1".replace(/^#/, "")).value);
const t2 = Number(card.querySelector("#" + "t2".replace(/^#/, "")).value);
const t3 = Number(card.querySelector("#" + "t3".replace(/^#/, "")).value);
const t4 = Number(card.querySelector("#" + "t4".replace(/^#/, "")).value);
 const valid=Number.isFinite(cp) && cp>=0.8 && cp<=1.3 && Number.isFinite(t1) && t1>=220 && t1<=450 && Number.isFinite(t2) && t2>=250 && t2<=1100 && Number.isFinite(t3) && t3>=700 && t3<=2000 && Number.isFinite(t4) && t4>=300 && t4<=1500 && (t2>t1 && t3>t4 && t3>t2);
 const display=card.querySelector("#" + 'metric'.replace(/^#/, "")); const desc=card.querySelector("#" + 'details'.replace(/^#/, ""));
 if(!valid){display.textContent='—';desc.textContent='Invalid parameters: inspect the input limits and physical state order.';card.querySelector("#" + 'plot'.replace(/^#/, "")).textContent='';return;}
 const y=compute(cp,t1,t2,t3,t4);
 if(!Number.isFinite(y)||Math.abs(y)>1e12){display.textContent='—';desc.textContent='Unphysical or undefined result.';return;}
 display.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' kJ/kg';
 desc.textContent="Simplified cycle; real turbines involve fuel-air mass differences and varying specific heat.";
 const xmin=Math.max(0.8,cp*0.8),xmax=Math.min(1.3,cp*1.2);
 const vals=[];
 for(let k=0;k<=40;k++){
   const x=xmin+(xmax-xmin)*k/40;
   const val=compute(x,t1,t2,t3,t4);
   if(Number.isFinite(val)) vals.push([x,val]);
 }
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(vals.length<2){plot.textContent='';return;}
 const low=Math.min(...vals.map(p=>p[1])),high=Math.max(...vals.map(p=>p[1]));
 const delta=Math.max(1e-9,high-low);
 const points=vals.map((p,j)=>`${45+605*j/(vals.length-1)},${179-128*(p[1]-low)/delta}`).join(' ');
 const cy=179-128*(y-low)/delta;
 plot.innerHTML=`<line x1="45" y1="184" x2="652" y2="184" stroke="#99adb9"/><line x1="45" y1="26" x2="45" y2="184" stroke="#99adb9"/><polyline points="${points}" stroke="#147d89" stroke-width="3" fill="none"/><circle cx="${45+605*(cp-xmin)/Math.max(1e-10,xmax-xmin)}" cy="${cy}" r="5" fill="#e19a32"/><text x="52" y="20" font-size="13" fill="#335667">Specific heat sensitivity (units kJ/(kg K))</text><text x="55" y="205" font-size="12" fill="#335667">${xmin.toPrecision(4)}</text><text x="595" y="205" font-size="12" fill="#335667">${xmax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 9,
    unit: 5,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 16</div><h3>HRSG exhaust recovery</h3><p class=\"subtitle\">An offline educational reader \u00b7 original draft \u00b7 8 units \u00b7 40 lessons \u00b7 16 interactive calculators.</p></header><p class=\"notice\"><strong>Limitations:</strong> A sensible-heat estimate, not a minimum-temperature-approach design.</p><article class=\"model-panel\"><h2>Model 09 \u00b7 HRSG exhaust recovery</h2><p><strong>Model relation:</strong> <code>Q = m_dot*cp*(T_in-T_out)</code></p><p class=\"small\">A sensible-heat estimate, not a minimum-temperature-approach design.</p><div class=\"fields\"><label for=\"m\">Exhaust flow (kg/s)<input id=\"m\" type=\"number\" min=\"0.1\" max=\"3000\" step=\"any\" value=\"220\"></label><label for=\"cp\">Exhaust cp (kJ/(kg K))<input id=\"cp\" type=\"number\" min=\"0.7\" max=\"1.5\" step=\"any\" value=\"1.1\"></label><label for=\"ti\">Exhaust inlet (\u00b0C)<input id=\"ti\" type=\"number\" min=\"150\" max=\"950\" step=\"any\" value=\"560\"></label><label for=\"to\">Stack outlet (\u00b0C)<input id=\"to\" type=\"number\" min=\"40\" max=\"800\" step=\"any\" value=\"130\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" class=\"small\" aria-live=\"polite\">Change an input to update.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 220\" aria-label=\"Output sensitivity as the first input varies\"></svg><p class=\"small\">Actual input sweep: first input \u00b120%, bounded by its declared limits. Dots represent recalculated model output; the curve is not measured plant behavior.</p></article><p class=\"footer\">\u00a9 OpenSTEM \u00b7 Educational draft \u00b7 Engineering calculations are simplified and not certified for real facilities.</p>",
    init: function(card) {
      try {
// OpenSTEM educational model 09; local, offline and self-contained.
// Formula: Q = m_dot*cp*(T_in-T_out)
const modelIndex=9;
function compute(m,cp,ti,to){ return m*cp*(ti-to); }
function update(){
 const m = Number(card.querySelector("#" + "m".replace(/^#/, "")).value);
const cp = Number(card.querySelector("#" + "cp".replace(/^#/, "")).value);
const ti = Number(card.querySelector("#" + "ti".replace(/^#/, "")).value);
const to = Number(card.querySelector("#" + "to".replace(/^#/, "")).value);
 const valid=Number.isFinite(m) && m>=0.1 && m<=3000 && Number.isFinite(cp) && cp>=0.7 && cp<=1.5 && Number.isFinite(ti) && ti>=150 && ti<=950 && Number.isFinite(to) && to>=40 && to<=800 && (ti>to);
 const display=card.querySelector("#" + 'metric'.replace(/^#/, "")); const desc=card.querySelector("#" + 'details'.replace(/^#/, ""));
 if(!valid){display.textContent='—';desc.textContent='Invalid parameters: inspect the input limits and physical state order.';card.querySelector("#" + 'plot'.replace(/^#/, "")).textContent='';return;}
 const y=compute(m,cp,ti,to);
 if(!Number.isFinite(y)||Math.abs(y)>1e12){display.textContent='—';desc.textContent='Unphysical or undefined result.';return;}
 display.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' kW';
 desc.textContent="A sensible-heat estimate, not a minimum-temperature-approach design.";
 const xmin=Math.max(0.1,m*0.8),xmax=Math.min(3000,m*1.2);
 const vals=[];
 for(let k=0;k<=40;k++){
   const x=xmin+(xmax-xmin)*k/40;
   const val=compute(x,cp,ti,to);
   if(Number.isFinite(val)) vals.push([x,val]);
 }
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(vals.length<2){plot.textContent='';return;}
 const low=Math.min(...vals.map(p=>p[1])),high=Math.max(...vals.map(p=>p[1]));
 const delta=Math.max(1e-9,high-low);
 const points=vals.map((p,j)=>`${45+605*j/(vals.length-1)},${179-128*(p[1]-low)/delta}`).join(' ');
 const cy=179-128*(y-low)/delta;
 plot.innerHTML=`<line x1="45" y1="184" x2="652" y2="184" stroke="#99adb9"/><line x1="45" y1="26" x2="45" y2="184" stroke="#99adb9"/><polyline points="${points}" stroke="#147d89" stroke-width="3" fill="none"/><circle cx="${45+605*(m-xmin)/Math.max(1e-10,xmax-xmin)}" cy="${cy}" r="5" fill="#e19a32"/><text x="52" y="20" font-size="13" fill="#335667">Exhaust flow sensitivity (units kg/s)</text><text x="55" y="205" font-size="12" fill="#335667">${xmin.toPrecision(4)}</text><text x="595" y="205" font-size="12" fill="#335667">${xmax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 9:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 10,
    unit: 5,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 16</div><h3>Combined-cycle net efficiency</h3><p class=\"subtitle\">An offline educational reader \u00b7 original draft \u00b7 8 units \u00b7 40 lessons \u00b7 16 interactive calculators.</p></header><p class=\"notice\"><strong>Limitations:</strong> Uses primary fuel once; recovered exhaust heat is not new fuel energy.</p><article class=\"model-panel\"><h2>Model 10 \u00b7 Combined-cycle net efficiency</h2><p><strong>Model relation:</strong> <code>eta = (P_GT+P_ST-P_aux)/Q_in</code></p><p class=\"small\">Uses primary fuel once; recovered exhaust heat is not new fuel energy.</p><div class=\"fields\"><label for=\"gt\">Gas-turbine output (MW)<input id=\"gt\" type=\"number\" min=\"1\" max=\"2000\" step=\"any\" value=\"180\"></label><label for=\"st\">Steam-turbine output (MW)<input id=\"st\" type=\"number\" min=\"0\" max=\"1500\" step=\"any\" value=\"90\"></label><label for=\"aux\">Station service (MW)<input id=\"aux\" type=\"number\" min=\"0\" max=\"300\" step=\"any\" value=\"12\"></label><label for=\"qin\">Fuel input (MW(th))<input id=\"qin\" type=\"number\" min=\"1\" max=\"4000\" step=\"any\" value=\"450\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" class=\"small\" aria-live=\"polite\">Change an input to update.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 220\" aria-label=\"Output sensitivity as the first input varies\"></svg><p class=\"small\">Actual input sweep: first input \u00b120%, bounded by its declared limits. Dots represent recalculated model output; the curve is not measured plant behavior.</p></article><p class=\"footer\">\u00a9 OpenSTEM \u00b7 Educational draft \u00b7 Engineering calculations are simplified and not certified for real facilities.</p>",
    init: function(card) {
      try {
// OpenSTEM educational model 10; local, offline and self-contained.
// Formula: eta = (P_GT+P_ST-P_aux)/Q_in
const modelIndex=10;
function compute(gt,st,aux,qin){ return ((gt+st-aux)/qin)*100; }
function update(){
 const gt = Number(card.querySelector("#" + "gt".replace(/^#/, "")).value);
const st = Number(card.querySelector("#" + "st".replace(/^#/, "")).value);
const aux = Number(card.querySelector("#" + "aux".replace(/^#/, "")).value);
const qin = Number(card.querySelector("#" + "qin".replace(/^#/, "")).value);
 const valid=Number.isFinite(gt) && gt>=1 && gt<=2000 && Number.isFinite(st) && st>=0 && st<=1500 && Number.isFinite(aux) && aux>=0 && aux<=300 && Number.isFinite(qin) && qin>=1 && qin<=4000 && (gt+st>aux && gt+st-aux<=qin);
 const display=card.querySelector("#" + 'metric'.replace(/^#/, "")); const desc=card.querySelector("#" + 'details'.replace(/^#/, ""));
 if(!valid){display.textContent='—';desc.textContent='Invalid parameters: inspect the input limits and physical state order.';card.querySelector("#" + 'plot'.replace(/^#/, "")).textContent='';return;}
 const y=compute(gt,st,aux,qin);
 if(!Number.isFinite(y)||Math.abs(y)>1e12){display.textContent='—';desc.textContent='Unphysical or undefined result.';return;}
 display.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' %';
 desc.textContent="Uses primary fuel once; recovered exhaust heat is not new fuel energy.";
 const xmin=Math.max(1,gt*0.8),xmax=Math.min(2000,gt*1.2);
 const vals=[];
 for(let k=0;k<=40;k++){
   const x=xmin+(xmax-xmin)*k/40;
   const val=compute(x,st,aux,qin);
   if(Number.isFinite(val)) vals.push([x,val]);
 }
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(vals.length<2){plot.textContent='';return;}
 const low=Math.min(...vals.map(p=>p[1])),high=Math.max(...vals.map(p=>p[1]));
 const delta=Math.max(1e-9,high-low);
 const points=vals.map((p,j)=>`${45+605*j/(vals.length-1)},${179-128*(p[1]-low)/delta}`).join(' ');
 const cy=179-128*(y-low)/delta;
 plot.innerHTML=`<line x1="45" y1="184" x2="652" y2="184" stroke="#99adb9"/><line x1="45" y1="26" x2="45" y2="184" stroke="#99adb9"/><polyline points="${points}" stroke="#147d89" stroke-width="3" fill="none"/><circle cx="${45+605*(gt-xmin)/Math.max(1e-10,xmax-xmin)}" cy="${cy}" r="5" fill="#e19a32"/><text x="52" y="20" font-size="13" fill="#335667">Gas-turbine output sensitivity (units MW)</text><text x="55" y="205" font-size="12" fill="#335667">${xmin.toPrecision(4)}</text><text x="595" y="205" font-size="12" fill="#335667">${xmax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 10:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 11,
    unit: 6,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 16</div><h3>Cooling water heat duty</h3><p class=\"subtitle\">An offline educational reader \u00b7 original draft \u00b7 8 units \u00b7 40 lessons \u00b7 16 interactive calculators.</p></header><p class=\"notice\"><strong>Limitations:</strong> Single-phase sensible heating only; instruments and flow accuracy matter.</p><article class=\"model-panel\"><h2>Model 11 \u00b7 Cooling water heat duty</h2><p><strong>Model relation:</strong> <code>Q = m_dot*cp*DeltaT</code></p><p class=\"small\">Single-phase sensible heating only; instruments and flow accuracy matter.</p><div class=\"fields\"><label for=\"m\">Cooling-water flow (kg/s)<input id=\"m\" type=\"number\" min=\"1\" max=\"20000\" step=\"any\" value=\"2600\"></label><label for=\"cp\">Water cp (kJ/(kg K))<input id=\"cp\" type=\"number\" min=\"3.5\" max=\"4.5\" step=\"any\" value=\"4.18\"></label><label for=\"dt\">Temperature rise (K)<input id=\"dt\" type=\"number\" min=\"0.1\" max=\"25\" step=\"any\" value=\"7\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" class=\"small\" aria-live=\"polite\">Change an input to update.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 220\" aria-label=\"Output sensitivity as the first input varies\"></svg><p class=\"small\">Actual input sweep: first input \u00b120%, bounded by its declared limits. Dots represent recalculated model output; the curve is not measured plant behavior.</p></article><p class=\"footer\">\u00a9 OpenSTEM \u00b7 Educational draft \u00b7 Engineering calculations are simplified and not certified for real facilities.</p>",
    init: function(card) {
      try {
// OpenSTEM educational model 11; local, offline and self-contained.
// Formula: Q = m_dot*cp*DeltaT
const modelIndex=11;
function compute(m,cp,dt){ return m*cp*dt; }
function update(){
 const m = Number(card.querySelector("#" + "m".replace(/^#/, "")).value);
const cp = Number(card.querySelector("#" + "cp".replace(/^#/, "")).value);
const dt = Number(card.querySelector("#" + "dt".replace(/^#/, "")).value);
 const valid=Number.isFinite(m) && m>=1 && m<=20000 && Number.isFinite(cp) && cp>=3.5 && cp<=4.5 && Number.isFinite(dt) && dt>=0.1 && dt<=25 && (true);
 const display=card.querySelector("#" + 'metric'.replace(/^#/, "")); const desc=card.querySelector("#" + 'details'.replace(/^#/, ""));
 if(!valid){display.textContent='—';desc.textContent='Invalid parameters: inspect the input limits and physical state order.';card.querySelector("#" + 'plot'.replace(/^#/, "")).textContent='';return;}
 const y=compute(m,cp,dt);
 if(!Number.isFinite(y)||Math.abs(y)>1e12){display.textContent='—';desc.textContent='Unphysical or undefined result.';return;}
 display.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' kW';
 desc.textContent="Single-phase sensible heating only; instruments and flow accuracy matter.";
 const xmin=Math.max(1,m*0.8),xmax=Math.min(20000,m*1.2);
 const vals=[];
 for(let k=0;k<=40;k++){
   const x=xmin+(xmax-xmin)*k/40;
   const val=compute(x,cp,dt);
   if(Number.isFinite(val)) vals.push([x,val]);
 }
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(vals.length<2){plot.textContent='';return;}
 const low=Math.min(...vals.map(p=>p[1])),high=Math.max(...vals.map(p=>p[1]));
 const delta=Math.max(1e-9,high-low);
 const points=vals.map((p,j)=>`${45+605*j/(vals.length-1)},${179-128*(p[1]-low)/delta}`).join(' ');
 const cy=179-128*(y-low)/delta;
 plot.innerHTML=`<line x1="45" y1="184" x2="652" y2="184" stroke="#99adb9"/><line x1="45" y1="26" x2="45" y2="184" stroke="#99adb9"/><polyline points="${points}" stroke="#147d89" stroke-width="3" fill="none"/><circle cx="${45+605*(m-xmin)/Math.max(1e-10,xmax-xmin)}" cy="${cy}" r="5" fill="#e19a32"/><text x="52" y="20" font-size="13" fill="#335667">Cooling-water flow sensitivity (units kg/s)</text><text x="55" y="205" font-size="12" fill="#335667">${xmin.toPrecision(4)}</text><text x="595" y="205" font-size="12" fill="#335667">${xmax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 11:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 12,
    unit: 6,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 16</div><h3>Required cooling-water flow</h3><p class=\"subtitle\">An offline educational reader \u00b7 original draft \u00b7 8 units \u00b7 40 lessons \u00b7 16 interactive calculators.</p></header><p class=\"notice\"><strong>Limitations:</strong> The allowed temperature rise requires site-specific ecological and permit review.</p><article class=\"model-panel\"><h2>Model 12 \u00b7 Required cooling-water flow</h2><p><strong>Model relation:</strong> <code>m_dot = Q/(cp*DeltaT)</code></p><p class=\"small\">The allowed temperature rise requires site-specific ecological and permit review.</p><div class=\"fields\"><label for=\"q\">Required cooling duty (MW(th))<input id=\"q\" type=\"number\" min=\"0.1\" max=\"3000\" step=\"any\" value=\"100\"></label><label for=\"cp\">Water cp (kJ/(kg K))<input id=\"cp\" type=\"number\" min=\"3.5\" max=\"4.5\" step=\"any\" value=\"4.18\"></label><label for=\"dt\">Allowed temperature rise (K)<input id=\"dt\" type=\"number\" min=\"0.1\" max=\"25\" step=\"any\" value=\"8\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" class=\"small\" aria-live=\"polite\">Change an input to update.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 220\" aria-label=\"Output sensitivity as the first input varies\"></svg><p class=\"small\">Actual input sweep: first input \u00b120%, bounded by its declared limits. Dots represent recalculated model output; the curve is not measured plant behavior.</p></article><p class=\"footer\">\u00a9 OpenSTEM \u00b7 Educational draft \u00b7 Engineering calculations are simplified and not certified for real facilities.</p>",
    init: function(card) {
      try {
// OpenSTEM educational model 12; local, offline and self-contained.
// Formula: m_dot = Q/(cp*DeltaT)
const modelIndex=12;
function compute(q,cp,dt){ return (q*1000)/(cp*dt); }
function update(){
 const q = Number(card.querySelector("#" + "q".replace(/^#/, "")).value);
const cp = Number(card.querySelector("#" + "cp".replace(/^#/, "")).value);
const dt = Number(card.querySelector("#" + "dt".replace(/^#/, "")).value);
 const valid=Number.isFinite(q) && q>=0.1 && q<=3000 && Number.isFinite(cp) && cp>=3.5 && cp<=4.5 && Number.isFinite(dt) && dt>=0.1 && dt<=25 && (true);
 const display=card.querySelector("#" + 'metric'.replace(/^#/, "")); const desc=card.querySelector("#" + 'details'.replace(/^#/, ""));
 if(!valid){display.textContent='—';desc.textContent='Invalid parameters: inspect the input limits and physical state order.';card.querySelector("#" + 'plot'.replace(/^#/, "")).textContent='';return;}
 const y=compute(q,cp,dt);
 if(!Number.isFinite(y)||Math.abs(y)>1e12){display.textContent='—';desc.textContent='Unphysical or undefined result.';return;}
 display.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' kg/s';
 desc.textContent="The allowed temperature rise requires site-specific ecological and permit review.";
 const xmin=Math.max(0.1,q*0.8),xmax=Math.min(3000,q*1.2);
 const vals=[];
 for(let k=0;k<=40;k++){
   const x=xmin+(xmax-xmin)*k/40;
   const val=compute(x,cp,dt);
   if(Number.isFinite(val)) vals.push([x,val]);
 }
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(vals.length<2){plot.textContent='';return;}
 const low=Math.min(...vals.map(p=>p[1])),high=Math.max(...vals.map(p=>p[1]));
 const delta=Math.max(1e-9,high-low);
 const points=vals.map((p,j)=>`${45+605*j/(vals.length-1)},${179-128*(p[1]-low)/delta}`).join(' ');
 const cy=179-128*(y-low)/delta;
 plot.innerHTML=`<line x1="45" y1="184" x2="652" y2="184" stroke="#99adb9"/><line x1="45" y1="26" x2="45" y2="184" stroke="#99adb9"/><polyline points="${points}" stroke="#147d89" stroke-width="3" fill="none"/><circle cx="${45+605*(q-xmin)/Math.max(1e-10,xmax-xmin)}" cy="${cy}" r="5" fill="#e19a32"/><text x="52" y="20" font-size="13" fill="#335667">Required cooling duty sensitivity (units MW(th))</text><text x="55" y="205" font-size="12" fill="#335667">${xmin.toPrecision(4)}</text><text x="595" y="205" font-size="12" fill="#335667">${xmax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 12:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 13,
    unit: 7,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 16</div><h3>CHP utilization factor</h3><p class=\"subtitle\">An offline educational reader \u00b7 original draft \u00b7 8 units \u00b7 40 lessons \u00b7 16 interactive calculators.</p></header><p class=\"notice\"><strong>Limitations:</strong> Only metered useful heat exported to a customer is included; electrical efficiency differs.</p><article class=\"model-panel\"><h2>Model 13 \u00b7 CHP utilization factor</h2><p><strong>Model relation:</strong> <code>U = (P_e+Q_useful)/Q_fuel</code></p><p class=\"small\">Only metered useful heat exported to a customer is included; electrical efficiency differs.</p><div class=\"fields\"><label for=\"pe\">Electric output (MW(e))<input id=\"pe\" type=\"number\" min=\"0\" max=\"2000\" step=\"any\" value=\"35\"></label><label for=\"qu\">Useful delivered heat (MW(th))<input id=\"qu\" type=\"number\" min=\"0\" max=\"2500\" step=\"any\" value=\"60\"></label><label for=\"qin\">Fuel input (MW(th))<input id=\"qin\" type=\"number\" min=\"1\" max=\"4000\" step=\"any\" value=\"120\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" class=\"small\" aria-live=\"polite\">Change an input to update.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 220\" aria-label=\"Output sensitivity as the first input varies\"></svg><p class=\"small\">Actual input sweep: first input \u00b120%, bounded by its declared limits. Dots represent recalculated model output; the curve is not measured plant behavior.</p></article><p class=\"footer\">\u00a9 OpenSTEM \u00b7 Educational draft \u00b7 Engineering calculations are simplified and not certified for real facilities.</p>",
    init: function(card) {
      try {
// OpenSTEM educational model 13; local, offline and self-contained.
// Formula: U = (P_e+Q_useful)/Q_fuel
const modelIndex=13;
function compute(pe,qu,qin){ return ((pe+qu)/qin)*100; }
function update(){
 const pe = Number(card.querySelector("#" + "pe".replace(/^#/, "")).value);
const qu = Number(card.querySelector("#" + "qu".replace(/^#/, "")).value);
const qin = Number(card.querySelector("#" + "qin".replace(/^#/, "")).value);
 const valid=Number.isFinite(pe) && pe>=0 && pe<=2000 && Number.isFinite(qu) && qu>=0 && qu<=2500 && Number.isFinite(qin) && qin>=1 && qin<=4000 && (pe+qu<=qin);
 const display=card.querySelector("#" + 'metric'.replace(/^#/, "")); const desc=card.querySelector("#" + 'details'.replace(/^#/, ""));
 if(!valid){display.textContent='—';desc.textContent='Invalid parameters: inspect the input limits and physical state order.';card.querySelector("#" + 'plot'.replace(/^#/, "")).textContent='';return;}
 const y=compute(pe,qu,qin);
 if(!Number.isFinite(y)||Math.abs(y)>1e12){display.textContent='—';desc.textContent='Unphysical or undefined result.';return;}
 display.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' %';
 desc.textContent="Only metered useful heat exported to a customer is included; electrical efficiency differs.";
 const xmin=Math.max(0,pe*0.8),xmax=Math.min(2000,pe*1.2);
 const vals=[];
 for(let k=0;k<=40;k++){
   const x=xmin+(xmax-xmin)*k/40;
   const val=compute(x,qu,qin);
   if(Number.isFinite(val)) vals.push([x,val]);
 }
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(vals.length<2){plot.textContent='';return;}
 const low=Math.min(...vals.map(p=>p[1])),high=Math.max(...vals.map(p=>p[1]));
 const delta=Math.max(1e-9,high-low);
 const points=vals.map((p,j)=>`${45+605*j/(vals.length-1)},${179-128*(p[1]-low)/delta}`).join(' ');
 const cy=179-128*(y-low)/delta;
 plot.innerHTML=`<line x1="45" y1="184" x2="652" y2="184" stroke="#99adb9"/><line x1="45" y1="26" x2="45" y2="184" stroke="#99adb9"/><polyline points="${points}" stroke="#147d89" stroke-width="3" fill="none"/><circle cx="${45+605*(pe-xmin)/Math.max(1e-10,xmax-xmin)}" cy="${cy}" r="5" fill="#e19a32"/><text x="52" y="20" font-size="13" fill="#335667">Electric output sensitivity (units MW(e))</text><text x="55" y="205" font-size="12" fill="#335667">${xmin.toPrecision(4)}</text><text x="595" y="205" font-size="12" fill="#335667">${xmax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 13:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 14,
    unit: 7,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 16</div><h3>Generator shaft torque</h3><p class=\"subtitle\">An offline educational reader \u00b7 original draft \u00b7 8 units \u00b7 40 lessons \u00b7 16 interactive calculators.</p></header><p class=\"notice\"><strong>Limitations:</strong> Use rpm-to-rad/s conversion; neglects startup and rotor dynamic stresses.</p><article class=\"model-panel\"><h2>Model 14 \u00b7 Generator shaft torque</h2><p><strong>Model relation:</strong> <code>tau = P/omega</code></p><p class=\"small\">Use rpm-to-rad/s conversion; neglects startup and rotor dynamic stresses.</p><div class=\"fields\"><label for=\"p\">Shaft power (MW)<input id=\"p\" type=\"number\" min=\"0.01\" max=\"2000\" step=\"any\" value=\"100\"></label><label for=\"n\">Rotational speed (rpm)<input id=\"n\" type=\"number\" min=\"10\" max=\"12000\" step=\"any\" value=\"3000\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" class=\"small\" aria-live=\"polite\">Change an input to update.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 220\" aria-label=\"Output sensitivity as the first input varies\"></svg><p class=\"small\">Actual input sweep: first input \u00b120%, bounded by its declared limits. Dots represent recalculated model output; the curve is not measured plant behavior.</p></article><p class=\"footer\">\u00a9 OpenSTEM \u00b7 Educational draft \u00b7 Engineering calculations are simplified and not certified for real facilities.</p>",
    init: function(card) {
      try {
// OpenSTEM educational model 14; local, offline and self-contained.
// Formula: tau = P/omega
const modelIndex=14;
function compute(p,n){ return (p*1e6)/(2*Math.PI*n/60); }
function update(){
 const p = Number(card.querySelector("#" + "p".replace(/^#/, "")).value);
const n = Number(card.querySelector("#" + "n".replace(/^#/, "")).value);
 const valid=Number.isFinite(p) && p>=0.01 && p<=2000 && Number.isFinite(n) && n>=10 && n<=12000 && (true);
 const display=card.querySelector("#" + 'metric'.replace(/^#/, "")); const desc=card.querySelector("#" + 'details'.replace(/^#/, ""));
 if(!valid){display.textContent='—';desc.textContent='Invalid parameters: inspect the input limits and physical state order.';card.querySelector("#" + 'plot'.replace(/^#/, "")).textContent='';return;}
 const y=compute(p,n);
 if(!Number.isFinite(y)||Math.abs(y)>1e12){display.textContent='—';desc.textContent='Unphysical or undefined result.';return;}
 display.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' N·m';
 desc.textContent="Use rpm-to-rad/s conversion; neglects startup and rotor dynamic stresses.";
 const xmin=Math.max(0.01,p*0.8),xmax=Math.min(2000,p*1.2);
 const vals=[];
 for(let k=0;k<=40;k++){
   const x=xmin+(xmax-xmin)*k/40;
   const val=compute(x,n);
   if(Number.isFinite(val)) vals.push([x,val]);
 }
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(vals.length<2){plot.textContent='';return;}
 const low=Math.min(...vals.map(p=>p[1])),high=Math.max(...vals.map(p=>p[1]));
 const delta=Math.max(1e-9,high-low);
 const points=vals.map((p,j)=>`${45+605*j/(vals.length-1)},${179-128*(p[1]-low)/delta}`).join(' ');
 const cy=179-128*(y-low)/delta;
 plot.innerHTML=`<line x1="45" y1="184" x2="652" y2="184" stroke="#99adb9"/><line x1="45" y1="26" x2="45" y2="184" stroke="#99adb9"/><polyline points="${points}" stroke="#147d89" stroke-width="3" fill="none"/><circle cx="${45+605*(p-xmin)/Math.max(1e-10,xmax-xmin)}" cy="${cy}" r="5" fill="#e19a32"/><text x="52" y="20" font-size="13" fill="#335667">Shaft power sensitivity (units MW)</text><text x="55" y="205" font-size="12" fill="#335667">${xmin.toPrecision(4)}</text><text x="595" y="205" font-size="12" fill="#335667">${xmax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 14:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 15,
    unit: 8,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 16</div><h3>Simplified operational availability</h3><p class=\"subtitle\">An offline educational reader \u00b7 original draft \u00b7 8 units \u00b7 40 lessons \u00b7 16 interactive calculators.</p></header><p class=\"notice\"><strong>Limitations:</strong> Does not include planned outage, partial derate or common-cause failure.</p><article class=\"model-panel\"><h2>Model 15 \u00b7 Simplified operational availability</h2><p><strong>Model relation:</strong> <code>A = MTBF/(MTBF+MTTR)</code></p><p class=\"small\">Does not include planned outage, partial derate or common-cause failure.</p><div class=\"fields\"><label for=\"bf\">Mean time between failure (h)<input id=\"bf\" type=\"number\" min=\"1\" max=\"100000\" step=\"any\" value=\"5000\"></label><label for=\"tr\">Mean repair time (h)<input id=\"tr\" type=\"number\" min=\"0.1\" max=\"5000\" step=\"any\" value=\"80\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" class=\"small\" aria-live=\"polite\">Change an input to update.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 220\" aria-label=\"Output sensitivity as the first input varies\"></svg><p class=\"small\">Actual input sweep: first input \u00b120%, bounded by its declared limits. Dots represent recalculated model output; the curve is not measured plant behavior.</p></article><p class=\"footer\">\u00a9 OpenSTEM \u00b7 Educational draft \u00b7 Engineering calculations are simplified and not certified for real facilities.</p>",
    init: function(card) {
      try {
// OpenSTEM educational model 15; local, offline and self-contained.
// Formula: A = MTBF/(MTBF+MTTR)
const modelIndex=15;
function compute(bf,tr){ return (bf/(bf+tr))*100; }
function update(){
 const bf = Number(card.querySelector("#" + "bf".replace(/^#/, "")).value);
const tr = Number(card.querySelector("#" + "tr".replace(/^#/, "")).value);
 const valid=Number.isFinite(bf) && bf>=1 && bf<=100000 && Number.isFinite(tr) && tr>=0.1 && tr<=5000 && (true);
 const display=card.querySelector("#" + 'metric'.replace(/^#/, "")); const desc=card.querySelector("#" + 'details'.replace(/^#/, ""));
 if(!valid){display.textContent='—';desc.textContent='Invalid parameters: inspect the input limits and physical state order.';card.querySelector("#" + 'plot'.replace(/^#/, "")).textContent='';return;}
 const y=compute(bf,tr);
 if(!Number.isFinite(y)||Math.abs(y)>1e12){display.textContent='—';desc.textContent='Unphysical or undefined result.';return;}
 display.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' %';
 desc.textContent="Does not include planned outage, partial derate or common-cause failure.";
 const xmin=Math.max(1,bf*0.8),xmax=Math.min(100000,bf*1.2);
 const vals=[];
 for(let k=0;k<=40;k++){
   const x=xmin+(xmax-xmin)*k/40;
   const val=compute(x,tr);
   if(Number.isFinite(val)) vals.push([x,val]);
 }
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(vals.length<2){plot.textContent='';return;}
 const low=Math.min(...vals.map(p=>p[1])),high=Math.max(...vals.map(p=>p[1]));
 const delta=Math.max(1e-9,high-low);
 const points=vals.map((p,j)=>`${45+605*j/(vals.length-1)},${179-128*(p[1]-low)/delta}`).join(' ');
 const cy=179-128*(y-low)/delta;
 plot.innerHTML=`<line x1="45" y1="184" x2="652" y2="184" stroke="#99adb9"/><line x1="45" y1="26" x2="45" y2="184" stroke="#99adb9"/><polyline points="${points}" stroke="#147d89" stroke-width="3" fill="none"/><circle cx="${45+605*(bf-xmin)/Math.max(1e-10,xmax-xmin)}" cy="${cy}" r="5" fill="#e19a32"/><text x="52" y="20" font-size="13" fill="#335667">Mean time between failure sensitivity (units h)</text><text x="55" y="205" font-size="12" fill="#335667">${xmin.toPrecision(4)}</text><text x="595" y="205" font-size="12" fill="#335667">${xmax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 15:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 16,
    unit: 8,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 16</div><h3>Simplified annual cost of energy</h3><p class=\"subtitle\">An offline educational reader \u00b7 original draft \u00b7 8 units \u00b7 40 lessons \u00b7 16 interactive calculators.</p></header><p class=\"notice\"><strong>Limitations:</strong> Simplified annualized LCOE-like metric; excludes tax, grid value, financing detail and externalities.</p><article class=\"model-panel\"><h2>Model 16 \u00b7 Simplified annual cost of energy</h2><p><strong>Model relation:</strong> <code>Cost = annual costs/annual MWh</code></p><p class=\"small\">Simplified annualized LCOE-like metric; excludes tax, grid value, financing detail and externalities.</p><div class=\"fields\"><label for=\"cap\">Annualized capital (million USD/year)<input id=\"cap\" type=\"number\" min=\"0\" max=\"1000\" step=\"any\" value=\"24\"></label><label for=\"opex\">Annual operating + fuel (million USD/year)<input id=\"opex\" type=\"number\" min=\"0\" max=\"1000\" step=\"any\" value=\"37\"></label><label for=\"mw\">Net rated capacity (MW)<input id=\"mw\" type=\"number\" min=\"1\" max=\"3000\" step=\"any\" value=\"200\"></label><label for=\"cf\">Capacity factor (%)<input id=\"cf\" type=\"number\" min=\"1\" max=\"100\" step=\"any\" value=\"70\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" class=\"small\" aria-live=\"polite\">Change an input to update.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 220\" aria-label=\"Output sensitivity as the first input varies\"></svg><p class=\"small\">Actual input sweep: first input \u00b120%, bounded by its declared limits. Dots represent recalculated model output; the curve is not measured plant behavior.</p></article><p class=\"footer\">\u00a9 OpenSTEM \u00b7 Educational draft \u00b7 Engineering calculations are simplified and not certified for real facilities.</p>",
    init: function(card) {
      try {
// OpenSTEM educational model 16; local, offline and self-contained.
// Formula: Cost = annual costs/annual MWh
const modelIndex=16;
function compute(cap,opex,mw,cf){ return ((cap+opex)*1e6)/(mw*cf/100*8760); }
function update(){
 const cap = Number(card.querySelector("#" + "cap".replace(/^#/, "")).value);
const opex = Number(card.querySelector("#" + "opex".replace(/^#/, "")).value);
const mw = Number(card.querySelector("#" + "mw".replace(/^#/, "")).value);
const cf = Number(card.querySelector("#" + "cf".replace(/^#/, "")).value);
 const valid=Number.isFinite(cap) && cap>=0 && cap<=1000 && Number.isFinite(opex) && opex>=0 && opex<=1000 && Number.isFinite(mw) && mw>=1 && mw<=3000 && Number.isFinite(cf) && cf>=1 && cf<=100 && (true);
 const display=card.querySelector("#" + 'metric'.replace(/^#/, "")); const desc=card.querySelector("#" + 'details'.replace(/^#/, ""));
 if(!valid){display.textContent='—';desc.textContent='Invalid parameters: inspect the input limits and physical state order.';card.querySelector("#" + 'plot'.replace(/^#/, "")).textContent='';return;}
 const y=compute(cap,opex,mw,cf);
 if(!Number.isFinite(y)||Math.abs(y)>1e12){display.textContent='—';desc.textContent='Unphysical or undefined result.';return;}
 display.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' $ / MWh';
 desc.textContent="Simplified annualized LCOE-like metric; excludes tax, grid value, financing detail and externalities.";
 const xmin=Math.max(0,cap*0.8),xmax=Math.min(1000,cap*1.2);
 const vals=[];
 for(let k=0;k<=40;k++){
   const x=xmin+(xmax-xmin)*k/40;
   const val=compute(x,opex,mw,cf);
   if(Number.isFinite(val)) vals.push([x,val]);
 }
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 if(vals.length<2){plot.textContent='';return;}
 const low=Math.min(...vals.map(p=>p[1])),high=Math.max(...vals.map(p=>p[1]));
 const delta=Math.max(1e-9,high-low);
 const points=vals.map((p,j)=>`${45+605*j/(vals.length-1)},${179-128*(p[1]-low)/delta}`).join(' ');
 const cy=179-128*(y-low)/delta;
 plot.innerHTML=`<line x1="45" y1="184" x2="652" y2="184" stroke="#99adb9"/><line x1="45" y1="26" x2="45" y2="184" stroke="#99adb9"/><polyline points="${points}" stroke="#147d89" stroke-width="3" fill="none"/><circle cx="${45+605*(cap-xmin)/Math.max(1e-10,xmax-xmin)}" cy="${cy}" r="5" fill="#e19a32"/><text x="52" y="20" font-size="13" fill="#335667">Annualized capital sensitivity (units million USD/year)</text><text x="55" y="205" font-size="12" fill="#335667">${xmin.toPrecision(4)}</text><text x="595" y="205" font-size="12" fill="#335667">${xmax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.fields input').forEach(el=>el.addEventListener('input',update));
update();
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
