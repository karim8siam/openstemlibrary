/* automotive-engineering Interactive Simulation Suite */
(function(window) {
  'use strict';

  var OPENSTEM_SIM_MODELS = [];

  OPENSTEM_SIM_MODELS.push({
    idx: 1,
    unit: 1,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 17</div><h3>Aerodynamic drag</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 working offline interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Editorial and safety status:</strong> Unreviewed teaching draft. Vehicle control, brakes, batteries and safety systems require competent independent engineering review and official compliance testing.</p><article class=\"model\"><h2>Model 01: Aerodynamic drag</h2><p><strong>Simplified relation:</strong> <code>F=0.5*rho*Cd*A*v^2</code></p><p class=\"small\">Constant Cd and density; wind yaw and detailed body airflow omitted.</p><div class=\"inputs\"><label for=\"rho\">Air density (kg/m\u00b3)<input id=\"rho\" type=\"number\" min=\"0.8\" max=\"1.5\" value=\"1.2\" step=\"any\"></label><label for=\"cd\">Drag coefficient (\u2014)<input id=\"cd\" type=\"number\" min=\"0.1\" max=\"1.5\" value=\"0.29\" step=\"any\"></label><label for=\"area\">Frontal area (m\u00b2)<input id=\"area\" type=\"number\" min=\"0.8\" max=\"5\" value=\"2.3\" step=\"any\"></label><label for=\"speed\">Air-relative speed (m/s)<input id=\"speed\" type=\"number\" min=\"0\" max=\"60\" value=\"25\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change an input.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 215\" role=\"img\" aria-label=\"Sensitivity plot showing recalculated results\"></svg><p class=\"small\">Curve recalculates as first input varies \u00b120%, bounded by its input limits. All numbers are educational synthetic scenarios, never measured vehicle performance.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 No certification or engineering guarantee.</p>",
    init: function(card) {
      try {
// OpenSTEM mechanical engineering, Book 17 model 01. Educational calculation only.
// Aerodynamic drag: F=0.5*rho*Cd*A*v^2
function compute(rho,cd,area,speed){return 0.5*rho*cd*area*speed*speed;}
function update(){
 const rho=Number(card.querySelector("#" + "rho".replace(/^#/, "")).value);
 const cd=Number(card.querySelector("#" + "cd".replace(/^#/, "")).value);
 const area=Number(card.querySelector("#" + "area".replace(/^#/, "")).value);
 const speed=Number(card.querySelector("#" + "speed".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")); const details=card.querySelector("#" + 'details'.replace(/^#/, ""));
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const valid=Number.isFinite(rho) && rho>=0.8 && rho<=1.5 && Number.isFinite(cd) && cd>=0.1 && cd<=1.5 && Number.isFinite(area) && area>=0.8 && area<=5 && Number.isFinite(speed) && speed>=0 && speed<=60 && (true);
 if(!valid){metric.textContent='Invalid inputs';details.textContent='Use bounded values and maintain physical ordering.';plot.textContent='';return;}
 const y=compute(rho,cd,area,speed);
 if(!Number.isFinite(y) || Math.abs(y)>1e12){metric.textContent='Undefined';details.textContent='The simplified relation is outside its numerical domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' N';
 details.textContent="Constant Cd and density; wind yaw and detailed body airflow omitted.";
 const xMin=Math.max(0.8,rho===0?0:rho*0.8);
 const xMax=Math.min(1.5,rho===0?1.5*0.2:rho*1.2);
 const pts=[];
 for(let k=0;k<=40;k++){ const x=xMin+(xMax-xMin)*k/40;const out=compute(x,cd,area,speed);if(Number.isFinite(out))pts.push([x,out]); }
 if(pts.length<2){plot.textContent='';return;}
 const low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));
 const scale=Math.max(1e-9,high-low);
 const xy=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${178-135*(p[1]-low)/scale}`).join(' ');
 const yNow=178-135*(y-low)/scale;
 plot.innerHTML=`<line x1="45" y1="183" x2="647" y2="183" stroke="#94a8b2"/><line x1="45" y1="22" x2="45" y2="183" stroke="#94a8b2"/><polyline points="${xy}" fill="none" stroke="#126e7a" stroke-width="3"/><circle cx="${45+600*(rho-xMin)/Math.max(1e-9,xMax-xMin)}" cy="${yNow}" r="5" fill="#d29232"/><text x="53" y="16" fill="#315667" font-size="13">Air density sensitivity</text><text x="52" y="205" fill="#315667" font-size="12">${xMin.toPrecision(4)}</text><text x="587" y="205" fill="#315667" font-size="12">${xMax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 2,
    unit: 1,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 17</div><h3>Rolling resistance</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 working offline interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Editorial and safety status:</strong> Unreviewed teaching draft. Vehicle control, brakes, batteries and safety systems require competent independent engineering review and official compliance testing.</p><article class=\"model\"><h2>Model 02: Rolling resistance</h2><p><strong>Simplified relation:</strong> <code>F=Crr*m*g</code></p><p class=\"small\">Level surface assumed; not measured tire resistance.</p><div class=\"inputs\"><label for=\"crr\">Rolling coefficient (\u2014)<input id=\"crr\" type=\"number\" min=\"0.002\" max=\"0.05\" value=\"0.011\" step=\"any\"></label><label for=\"mass\">Mass (kg)<input id=\"mass\" type=\"number\" min=\"500\" max=\"4000\" value=\"1600\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change an input.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 215\" role=\"img\" aria-label=\"Sensitivity plot showing recalculated results\"></svg><p class=\"small\">Curve recalculates as first input varies \u00b120%, bounded by its input limits. All numbers are educational synthetic scenarios, never measured vehicle performance.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 No certification or engineering guarantee.</p>",
    init: function(card) {
      try {
// OpenSTEM mechanical engineering, Book 17 model 02. Educational calculation only.
// Rolling resistance: F=Crr*m*g
function compute(crr,mass){return crr*mass*9.81;}
function update(){
 const crr=Number(card.querySelector("#" + "crr".replace(/^#/, "")).value);
 const mass=Number(card.querySelector("#" + "mass".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")); const details=card.querySelector("#" + 'details'.replace(/^#/, ""));
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const valid=Number.isFinite(crr) && crr>=0.002 && crr<=0.05 && Number.isFinite(mass) && mass>=500 && mass<=4000 && (true);
 if(!valid){metric.textContent='Invalid inputs';details.textContent='Use bounded values and maintain physical ordering.';plot.textContent='';return;}
 const y=compute(crr,mass);
 if(!Number.isFinite(y) || Math.abs(y)>1e12){metric.textContent='Undefined';details.textContent='The simplified relation is outside its numerical domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' N';
 details.textContent="Level surface assumed; not measured tire resistance.";
 const xMin=Math.max(0.002,crr===0?0:crr*0.8);
 const xMax=Math.min(0.05,crr===0?0.05*0.2:crr*1.2);
 const pts=[];
 for(let k=0;k<=40;k++){ const x=xMin+(xMax-xMin)*k/40;const out=compute(x,mass);if(Number.isFinite(out))pts.push([x,out]); }
 if(pts.length<2){plot.textContent='';return;}
 const low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));
 const scale=Math.max(1e-9,high-low);
 const xy=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${178-135*(p[1]-low)/scale}`).join(' ');
 const yNow=178-135*(y-low)/scale;
 plot.innerHTML=`<line x1="45" y1="183" x2="647" y2="183" stroke="#94a8b2"/><line x1="45" y1="22" x2="45" y2="183" stroke="#94a8b2"/><polyline points="${xy}" fill="none" stroke="#126e7a" stroke-width="3"/><circle cx="${45+600*(crr-xMin)/Math.max(1e-9,xMax-xMin)}" cy="${yNow}" r="5" fill="#d29232"/><text x="53" y="16" fill="#315667" font-size="13">Rolling coefficient sensitivity</text><text x="52" y="205" fill="#315667" font-size="12">${xMin.toPrecision(4)}</text><text x="587" y="205" fill="#315667" font-size="12">${xMax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 3,
    unit: 2,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 17</div><h3>Hill climbing force</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 working offline interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Editorial and safety status:</strong> Unreviewed teaching draft. Vehicle control, brakes, batteries and safety systems require competent independent engineering review and official compliance testing.</p><article class=\"model\"><h2>Model 03: Hill climbing force</h2><p><strong>Simplified relation:</strong> <code>F=m*g*grade/sqrt(1+grade\u00b2)</code></p><p class=\"small\">Uphill gravity component only; drag and rolling losses excluded.</p><div class=\"inputs\"><label for=\"mass\">Vehicle mass (kg)<input id=\"mass\" type=\"number\" min=\"500\" max=\"10000\" value=\"1800\" step=\"any\"></label><label for=\"grade\">Road grade (%)<input id=\"grade\" type=\"number\" min=\"0\" max=\"30\" value=\"8\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change an input.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 215\" role=\"img\" aria-label=\"Sensitivity plot showing recalculated results\"></svg><p class=\"small\">Curve recalculates as first input varies \u00b120%, bounded by its input limits. All numbers are educational synthetic scenarios, never measured vehicle performance.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 No certification or engineering guarantee.</p>",
    init: function(card) {
      try {
// OpenSTEM mechanical engineering, Book 17 model 03. Educational calculation only.
// Hill climbing force: F=m*g*grade/sqrt(1+grade²)
function compute(mass,grade){return mass*9.81*(grade/100)/Math.sqrt(1+(grade/100)**2);}
function update(){
 const mass=Number(card.querySelector("#" + "mass".replace(/^#/, "")).value);
 const grade=Number(card.querySelector("#" + "grade".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")); const details=card.querySelector("#" + 'details'.replace(/^#/, ""));
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const valid=Number.isFinite(mass) && mass>=500 && mass<=10000 && Number.isFinite(grade) && grade>=0 && grade<=30 && (true);
 if(!valid){metric.textContent='Invalid inputs';details.textContent='Use bounded values and maintain physical ordering.';plot.textContent='';return;}
 const y=compute(mass,grade);
 if(!Number.isFinite(y) || Math.abs(y)>1e12){metric.textContent='Undefined';details.textContent='The simplified relation is outside its numerical domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' N';
 details.textContent="Uphill gravity component only; drag and rolling losses excluded.";
 const xMin=Math.max(500,mass===0?0:mass*0.8);
 const xMax=Math.min(10000,mass===0?10000*0.2:mass*1.2);
 const pts=[];
 for(let k=0;k<=40;k++){ const x=xMin+(xMax-xMin)*k/40;const out=compute(x,grade);if(Number.isFinite(out))pts.push([x,out]); }
 if(pts.length<2){plot.textContent='';return;}
 const low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));
 const scale=Math.max(1e-9,high-low);
 const xy=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${178-135*(p[1]-low)/scale}`).join(' ');
 const yNow=178-135*(y-low)/scale;
 plot.innerHTML=`<line x1="45" y1="183" x2="647" y2="183" stroke="#94a8b2"/><line x1="45" y1="22" x2="45" y2="183" stroke="#94a8b2"/><polyline points="${xy}" fill="none" stroke="#126e7a" stroke-width="3"/><circle cx="${45+600*(mass-xMin)/Math.max(1e-9,xMax-xMin)}" cy="${yNow}" r="5" fill="#d29232"/><text x="53" y="16" fill="#315667" font-size="13">Vehicle mass sensitivity</text><text x="52" y="205" fill="#315667" font-size="12">${xMin.toPrecision(4)}</text><text x="587" y="205" fill="#315667" font-size="12">${xMax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 4,
    unit: 2,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 17</div><h3>Required tractive force</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 working offline interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Editorial and safety status:</strong> Unreviewed teaching draft. Vehicle control, brakes, batteries and safety systems require competent independent engineering review and official compliance testing.</p><article class=\"model\"><h2>Model 04: Required tractive force</h2><p><strong>Simplified relation:</strong> <code>F=m*a+F_resist</code></p><p class=\"small\">Not necessarily achievable because tire friction and power limits are not included.</p><div class=\"inputs\"><label for=\"mass\">Vehicle mass (kg)<input id=\"mass\" type=\"number\" min=\"500\" max=\"8000\" value=\"1700\" step=\"any\"></label><label for=\"acc\">Desired acceleration (m/s\u00b2)<input id=\"acc\" type=\"number\" min=\"0\" max=\"6\" value=\"1.5\" step=\"any\"></label><label for=\"resist\">Combined resistances (N)<input id=\"resist\" type=\"number\" min=\"0\" max=\"6000\" value=\"360\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change an input.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 215\" role=\"img\" aria-label=\"Sensitivity plot showing recalculated results\"></svg><p class=\"small\">Curve recalculates as first input varies \u00b120%, bounded by its input limits. All numbers are educational synthetic scenarios, never measured vehicle performance.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 No certification or engineering guarantee.</p>",
    init: function(card) {
      try {
// OpenSTEM mechanical engineering, Book 17 model 04. Educational calculation only.
// Required tractive force: F=m*a+F_resist
function compute(mass,acc,resist){return mass*acc+resist;}
function update(){
 const mass=Number(card.querySelector("#" + "mass".replace(/^#/, "")).value);
 const acc=Number(card.querySelector("#" + "acc".replace(/^#/, "")).value);
 const resist=Number(card.querySelector("#" + "resist".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")); const details=card.querySelector("#" + 'details'.replace(/^#/, ""));
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const valid=Number.isFinite(mass) && mass>=500 && mass<=8000 && Number.isFinite(acc) && acc>=0 && acc<=6 && Number.isFinite(resist) && resist>=0 && resist<=6000 && (true);
 if(!valid){metric.textContent='Invalid inputs';details.textContent='Use bounded values and maintain physical ordering.';plot.textContent='';return;}
 const y=compute(mass,acc,resist);
 if(!Number.isFinite(y) || Math.abs(y)>1e12){metric.textContent='Undefined';details.textContent='The simplified relation is outside its numerical domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' N';
 details.textContent="Not necessarily achievable because tire friction and power limits are not included.";
 const xMin=Math.max(500,mass===0?0:mass*0.8);
 const xMax=Math.min(8000,mass===0?8000*0.2:mass*1.2);
 const pts=[];
 for(let k=0;k<=40;k++){ const x=xMin+(xMax-xMin)*k/40;const out=compute(x,acc,resist);if(Number.isFinite(out))pts.push([x,out]); }
 if(pts.length<2){plot.textContent='';return;}
 const low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));
 const scale=Math.max(1e-9,high-low);
 const xy=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${178-135*(p[1]-low)/scale}`).join(' ');
 const yNow=178-135*(y-low)/scale;
 plot.innerHTML=`<line x1="45" y1="183" x2="647" y2="183" stroke="#94a8b2"/><line x1="45" y1="22" x2="45" y2="183" stroke="#94a8b2"/><polyline points="${xy}" fill="none" stroke="#126e7a" stroke-width="3"/><circle cx="${45+600*(mass-xMin)/Math.max(1e-9,xMax-xMin)}" cy="${yNow}" r="5" fill="#d29232"/><text x="53" y="16" fill="#315667" font-size="13">Vehicle mass sensitivity</text><text x="52" y="205" fill="#315667" font-size="12">${xMin.toPrecision(4)}</text><text x="587" y="205" fill="#315667" font-size="12">${xMax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 5,
    unit: 3,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 17</div><h3>Engine torque from power</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 working offline interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Editorial and safety status:</strong> Unreviewed teaching draft. Vehicle control, brakes, batteries and safety systems require competent independent engineering review and official compliance testing.</p><article class=\"model\"><h2>Model 05: Engine torque from power</h2><p><strong>Simplified relation:</strong> <code>T=9550*P_kW/rpm</code></p><p class=\"small\">Brake shaft power, not wheel output.</p><div class=\"inputs\"><label for=\"power\">Engine shaft power (kW)<input id=\"power\" type=\"number\" min=\"1\" max=\"500\" value=\"70\" step=\"any\"></label><label for=\"rpm\">Engine speed (rpm)<input id=\"rpm\" type=\"number\" min=\"500\" max=\"10000\" value=\"3000\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change an input.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 215\" role=\"img\" aria-label=\"Sensitivity plot showing recalculated results\"></svg><p class=\"small\">Curve recalculates as first input varies \u00b120%, bounded by its input limits. All numbers are educational synthetic scenarios, never measured vehicle performance.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 No certification or engineering guarantee.</p>",
    init: function(card) {
      try {
// OpenSTEM mechanical engineering, Book 17 model 05. Educational calculation only.
// Engine torque from power: T=9550*P_kW/rpm
function compute(power,rpm){return power*60000/(2*Math.PI*rpm);}
function update(){
 const power=Number(card.querySelector("#" + "power".replace(/^#/, "")).value);
 const rpm=Number(card.querySelector("#" + "rpm".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")); const details=card.querySelector("#" + 'details'.replace(/^#/, ""));
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const valid=Number.isFinite(power) && power>=1 && power<=500 && Number.isFinite(rpm) && rpm>=500 && rpm<=10000 && (true);
 if(!valid){metric.textContent='Invalid inputs';details.textContent='Use bounded values and maintain physical ordering.';plot.textContent='';return;}
 const y=compute(power,rpm);
 if(!Number.isFinite(y) || Math.abs(y)>1e12){metric.textContent='Undefined';details.textContent='The simplified relation is outside its numerical domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' N·m';
 details.textContent="Brake shaft power, not wheel output.";
 const xMin=Math.max(1,power===0?0:power*0.8);
 const xMax=Math.min(500,power===0?500*0.2:power*1.2);
 const pts=[];
 for(let k=0;k<=40;k++){ const x=xMin+(xMax-xMin)*k/40;const out=compute(x,rpm);if(Number.isFinite(out))pts.push([x,out]); }
 if(pts.length<2){plot.textContent='';return;}
 const low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));
 const scale=Math.max(1e-9,high-low);
 const xy=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${178-135*(p[1]-low)/scale}`).join(' ');
 const yNow=178-135*(y-low)/scale;
 plot.innerHTML=`<line x1="45" y1="183" x2="647" y2="183" stroke="#94a8b2"/><line x1="45" y1="22" x2="45" y2="183" stroke="#94a8b2"/><polyline points="${xy}" fill="none" stroke="#126e7a" stroke-width="3"/><circle cx="${45+600*(power-xMin)/Math.max(1e-9,xMax-xMin)}" cy="${yNow}" r="5" fill="#d29232"/><text x="53" y="16" fill="#315667" font-size="13">Engine shaft power sensitivity</text><text x="52" y="205" fill="#315667" font-size="12">${xMin.toPrecision(4)}</text><text x="587" y="205" fill="#315667" font-size="12">${xMax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 6,
    unit: 3,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 17</div><h3>Driveline wheel torque</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 working offline interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Editorial and safety status:</strong> Unreviewed teaching draft. Vehicle control, brakes, batteries and safety systems require competent independent engineering review and official compliance testing.</p><article class=\"model\"><h2>Model 06: Driveline wheel torque</h2><p><strong>Simplified relation:</strong> <code>T_w=T_e*i_g*i_f*eta</code></p><p class=\"small\">No clutch slip or driveability transient; tire adhesion limits omitted.</p><div class=\"inputs\"><label for=\"torque\">Input shaft torque (N\u00b7m)<input id=\"torque\" type=\"number\" min=\"0\" max=\"1000\" value=\"180\" step=\"any\"></label><label for=\"gear\">Selected gear ratio (\u2014)<input id=\"gear\" type=\"number\" min=\"0.3\" max=\"8\" value=\"3.0\" step=\"any\"></label><label for=\"final\">Final drive ratio (\u2014)<input id=\"final\" type=\"number\" min=\"1\" max=\"7\" value=\"3.4\" step=\"any\"></label><label for=\"eff\">Mechanical efficiency (%)<input id=\"eff\" type=\"number\" min=\"30\" max=\"100\" value=\"90\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change an input.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 215\" role=\"img\" aria-label=\"Sensitivity plot showing recalculated results\"></svg><p class=\"small\">Curve recalculates as first input varies \u00b120%, bounded by its input limits. All numbers are educational synthetic scenarios, never measured vehicle performance.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 No certification or engineering guarantee.</p>",
    init: function(card) {
      try {
// OpenSTEM mechanical engineering, Book 17 model 06. Educational calculation only.
// Driveline wheel torque: T_w=T_e*i_g*i_f*eta
function compute(torque,gear,final,eff){return torque*gear*final*(eff/100);}
function update(){
 const torque=Number(card.querySelector("#" + "torque".replace(/^#/, "")).value);
 const gear=Number(card.querySelector("#" + "gear".replace(/^#/, "")).value);
 const final=Number(card.querySelector("#" + "final".replace(/^#/, "")).value);
 const eff=Number(card.querySelector("#" + "eff".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")); const details=card.querySelector("#" + 'details'.replace(/^#/, ""));
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const valid=Number.isFinite(torque) && torque>=0 && torque<=1000 && Number.isFinite(gear) && gear>=0.3 && gear<=8 && Number.isFinite(final) && final>=1 && final<=7 && Number.isFinite(eff) && eff>=30 && eff<=100 && (true);
 if(!valid){metric.textContent='Invalid inputs';details.textContent='Use bounded values and maintain physical ordering.';plot.textContent='';return;}
 const y=compute(torque,gear,final,eff);
 if(!Number.isFinite(y) || Math.abs(y)>1e12){metric.textContent='Undefined';details.textContent='The simplified relation is outside its numerical domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' N·m';
 details.textContent="No clutch slip or driveability transient; tire adhesion limits omitted.";
 const xMin=Math.max(0,torque===0?0:torque*0.8);
 const xMax=Math.min(1000,torque===0?1000*0.2:torque*1.2);
 const pts=[];
 for(let k=0;k<=40;k++){ const x=xMin+(xMax-xMin)*k/40;const out=compute(x,gear,final,eff);if(Number.isFinite(out))pts.push([x,out]); }
 if(pts.length<2){plot.textContent='';return;}
 const low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));
 const scale=Math.max(1e-9,high-low);
 const xy=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${178-135*(p[1]-low)/scale}`).join(' ');
 const yNow=178-135*(y-low)/scale;
 plot.innerHTML=`<line x1="45" y1="183" x2="647" y2="183" stroke="#94a8b2"/><line x1="45" y1="22" x2="45" y2="183" stroke="#94a8b2"/><polyline points="${xy}" fill="none" stroke="#126e7a" stroke-width="3"/><circle cx="${45+600*(torque-xMin)/Math.max(1e-9,xMax-xMin)}" cy="${yNow}" r="5" fill="#d29232"/><text x="53" y="16" fill="#315667" font-size="13">Input shaft torque sensitivity</text><text x="52" y="205" fill="#315667" font-size="12">${xMin.toPrecision(4)}</text><text x="587" y="205" fill="#315667" font-size="12">${xMax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 7,
    unit: 4,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 17</div><h3>Ideal braking distance</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 working offline interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Editorial and safety status:</strong> Unreviewed teaching draft. Vehicle control, brakes, batteries and safety systems require competent independent engineering review and official compliance testing.</p><article class=\"model\"><h2>Model 07: Ideal braking distance</h2><p><strong>Simplified relation:</strong> <code>d=v\u00b2/(2*mu*g)</code></p><p class=\"small\">Ideal constant deceleration without reaction time or grade; not a stop-distance guarantee.</p><div class=\"inputs\"><label for=\"speed\">Initial road speed (m/s)<input id=\"speed\" type=\"number\" min=\"0\" max=\"55\" value=\"20\" step=\"any\"></label><label for=\"mu\">Assumed effective adhesion (\u2014)<input id=\"mu\" type=\"number\" min=\"0.1\" max=\"1.1\" value=\"0.7\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change an input.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 215\" role=\"img\" aria-label=\"Sensitivity plot showing recalculated results\"></svg><p class=\"small\">Curve recalculates as first input varies \u00b120%, bounded by its input limits. All numbers are educational synthetic scenarios, never measured vehicle performance.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 No certification or engineering guarantee.</p>",
    init: function(card) {
      try {
// OpenSTEM mechanical engineering, Book 17 model 07. Educational calculation only.
// Ideal braking distance: d=v²/(2*mu*g)
function compute(speed,mu){return speed*speed/(2*mu*9.81);}
function update(){
 const speed=Number(card.querySelector("#" + "speed".replace(/^#/, "")).value);
 const mu=Number(card.querySelector("#" + "mu".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")); const details=card.querySelector("#" + 'details'.replace(/^#/, ""));
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const valid=Number.isFinite(speed) && speed>=0 && speed<=55 && Number.isFinite(mu) && mu>=0.1 && mu<=1.1 && (true);
 if(!valid){metric.textContent='Invalid inputs';details.textContent='Use bounded values and maintain physical ordering.';plot.textContent='';return;}
 const y=compute(speed,mu);
 if(!Number.isFinite(y) || Math.abs(y)>1e12){metric.textContent='Undefined';details.textContent='The simplified relation is outside its numerical domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' m';
 details.textContent="Ideal constant deceleration without reaction time or grade; not a stop-distance guarantee.";
 const xMin=Math.max(0,speed===0?0:speed*0.8);
 const xMax=Math.min(55,speed===0?55*0.2:speed*1.2);
 const pts=[];
 for(let k=0;k<=40;k++){ const x=xMin+(xMax-xMin)*k/40;const out=compute(x,mu);if(Number.isFinite(out))pts.push([x,out]); }
 if(pts.length<2){plot.textContent='';return;}
 const low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));
 const scale=Math.max(1e-9,high-low);
 const xy=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${178-135*(p[1]-low)/scale}`).join(' ');
 const yNow=178-135*(y-low)/scale;
 plot.innerHTML=`<line x1="45" y1="183" x2="647" y2="183" stroke="#94a8b2"/><line x1="45" y1="22" x2="45" y2="183" stroke="#94a8b2"/><polyline points="${xy}" fill="none" stroke="#126e7a" stroke-width="3"/><circle cx="${45+600*(speed-xMin)/Math.max(1e-9,xMax-xMin)}" cy="${yNow}" r="5" fill="#d29232"/><text x="53" y="16" fill="#315667" font-size="13">Initial road speed sensitivity</text><text x="52" y="205" fill="#315667" font-size="12">${xMin.toPrecision(4)}</text><text x="587" y="205" fill="#315667" font-size="12">${xMax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 8,
    unit: 4,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 17</div><h3>Kinetic energy removed</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 working offline interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Editorial and safety status:</strong> Unreviewed teaching draft. Vehicle control, brakes, batteries and safety systems require competent independent engineering review and official compliance testing.</p><article class=\"model\"><h2>Model 08: Kinetic energy removed</h2><p><strong>Simplified relation:</strong> <code>Delta E=0.5*m*(v1\u00b2-v2\u00b2)</code></p><p class=\"small\">Translational energy only; rotating parts, grade and cooling omitted.</p><div class=\"inputs\"><label for=\"mass\">Vehicle mass (kg)<input id=\"mass\" type=\"number\" min=\"500\" max=\"10000\" value=\"1800\" step=\"any\"></label><label for=\"v1\">Initial speed (m/s)<input id=\"v1\" type=\"number\" min=\"0\" max=\"60\" value=\"25\" step=\"any\"></label><label for=\"v2\">Final speed (m/s)<input id=\"v2\" type=\"number\" min=\"0\" max=\"60\" value=\"5\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change an input.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 215\" role=\"img\" aria-label=\"Sensitivity plot showing recalculated results\"></svg><p class=\"small\">Curve recalculates as first input varies \u00b120%, bounded by its input limits. All numbers are educational synthetic scenarios, never measured vehicle performance.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 No certification or engineering guarantee.</p>",
    init: function(card) {
      try {
// OpenSTEM mechanical engineering, Book 17 model 08. Educational calculation only.
// Kinetic energy removed: Delta E=0.5*m*(v1²-v2²)
function compute(mass,v1,v2){return 0.5*mass*(v1*v1-v2*v2)/1000;}
function update(){
 const mass=Number(card.querySelector("#" + "mass".replace(/^#/, "")).value);
 const v1=Number(card.querySelector("#" + "v1".replace(/^#/, "")).value);
 const v2=Number(card.querySelector("#" + "v2".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")); const details=card.querySelector("#" + 'details'.replace(/^#/, ""));
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const valid=Number.isFinite(mass) && mass>=500 && mass<=10000 && Number.isFinite(v1) && v1>=0 && v1<=60 && Number.isFinite(v2) && v2>=0 && v2<=60 && (v1>=v2);
 if(!valid){metric.textContent='Invalid inputs';details.textContent='Use bounded values and maintain physical ordering.';plot.textContent='';return;}
 const y=compute(mass,v1,v2);
 if(!Number.isFinite(y) || Math.abs(y)>1e12){metric.textContent='Undefined';details.textContent='The simplified relation is outside its numerical domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' kJ';
 details.textContent="Translational energy only; rotating parts, grade and cooling omitted.";
 const xMin=Math.max(500,mass===0?0:mass*0.8);
 const xMax=Math.min(10000,mass===0?10000*0.2:mass*1.2);
 const pts=[];
 for(let k=0;k<=40;k++){ const x=xMin+(xMax-xMin)*k/40;const out=compute(x,v1,v2);if(Number.isFinite(out))pts.push([x,out]); }
 if(pts.length<2){plot.textContent='';return;}
 const low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));
 const scale=Math.max(1e-9,high-low);
 const xy=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${178-135*(p[1]-low)/scale}`).join(' ');
 const yNow=178-135*(y-low)/scale;
 plot.innerHTML=`<line x1="45" y1="183" x2="647" y2="183" stroke="#94a8b2"/><line x1="45" y1="22" x2="45" y2="183" stroke="#94a8b2"/><polyline points="${xy}" fill="none" stroke="#126e7a" stroke-width="3"/><circle cx="${45+600*(mass-xMin)/Math.max(1e-9,xMax-xMin)}" cy="${yNow}" r="5" fill="#d29232"/><text x="53" y="16" fill="#315667" font-size="13">Vehicle mass sensitivity</text><text x="52" y="205" fill="#315667" font-size="12">${xMin.toPrecision(4)}</text><text x="587" y="205" fill="#315667" font-size="12">${xMax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 9,
    unit: 5,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 17</div><h3>Steady corner lateral acceleration</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 working offline interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Editorial and safety status:</strong> Unreviewed teaching draft. Vehicle control, brakes, batteries and safety systems require competent independent engineering review and official compliance testing.</p><article class=\"model\"><h2>Model 09: Steady corner lateral acceleration</h2><p><strong>Simplified relation:</strong> <code>a_y=v\u00b2/R</code></p><p class=\"small\">Kinematic target only; no proof of tire grip, stability or rollover margin.</p><div class=\"inputs\"><label for=\"speed\">Vehicle speed (m/s)<input id=\"speed\" type=\"number\" min=\"0\" max=\"55\" value=\"15\" step=\"any\"></label><label for=\"radius\">Path radius (m)<input id=\"radius\" type=\"number\" min=\"5\" max=\"1000\" value=\"75\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change an input.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 215\" role=\"img\" aria-label=\"Sensitivity plot showing recalculated results\"></svg><p class=\"small\">Curve recalculates as first input varies \u00b120%, bounded by its input limits. All numbers are educational synthetic scenarios, never measured vehicle performance.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 No certification or engineering guarantee.</p>",
    init: function(card) {
      try {
// OpenSTEM mechanical engineering, Book 17 model 09. Educational calculation only.
// Steady corner lateral acceleration: a_y=v²/R
function compute(speed,radius){return speed*speed/radius;}
function update(){
 const speed=Number(card.querySelector("#" + "speed".replace(/^#/, "")).value);
 const radius=Number(card.querySelector("#" + "radius".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")); const details=card.querySelector("#" + 'details'.replace(/^#/, ""));
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const valid=Number.isFinite(speed) && speed>=0 && speed<=55 && Number.isFinite(radius) && radius>=5 && radius<=1000 && (true);
 if(!valid){metric.textContent='Invalid inputs';details.textContent='Use bounded values and maintain physical ordering.';plot.textContent='';return;}
 const y=compute(speed,radius);
 if(!Number.isFinite(y) || Math.abs(y)>1e12){metric.textContent='Undefined';details.textContent='The simplified relation is outside its numerical domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' m/s²';
 details.textContent="Kinematic target only; no proof of tire grip, stability or rollover margin.";
 const xMin=Math.max(0,speed===0?0:speed*0.8);
 const xMax=Math.min(55,speed===0?55*0.2:speed*1.2);
 const pts=[];
 for(let k=0;k<=40;k++){ const x=xMin+(xMax-xMin)*k/40;const out=compute(x,radius);if(Number.isFinite(out))pts.push([x,out]); }
 if(pts.length<2){plot.textContent='';return;}
 const low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));
 const scale=Math.max(1e-9,high-low);
 const xy=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${178-135*(p[1]-low)/scale}`).join(' ');
 const yNow=178-135*(y-low)/scale;
 plot.innerHTML=`<line x1="45" y1="183" x2="647" y2="183" stroke="#94a8b2"/><line x1="45" y1="22" x2="45" y2="183" stroke="#94a8b2"/><polyline points="${xy}" fill="none" stroke="#126e7a" stroke-width="3"/><circle cx="${45+600*(speed-xMin)/Math.max(1e-9,xMax-xMin)}" cy="${yNow}" r="5" fill="#d29232"/><text x="53" y="16" fill="#315667" font-size="13">Vehicle speed sensitivity</text><text x="52" y="205" fill="#315667" font-size="12">${xMin.toPrecision(4)}</text><text x="587" y="205" fill="#315667" font-size="12">${xMax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 9:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 10,
    unit: 5,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 17</div><h3>Low-speed bicycle steer angle</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 working offline interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Editorial and safety status:</strong> Unreviewed teaching draft. Vehicle control, brakes, batteries and safety systems require competent independent engineering review and official compliance testing.</p><article class=\"model\"><h2>Model 10: Low-speed bicycle steer angle</h2><p><strong>Simplified relation:</strong> <code>delta=atan(L/R)</code></p><p class=\"small\">Idealized road-wheel angle at low speed, not steering-wheel angle.</p><div class=\"inputs\"><label for=\"wheelbase\">Wheelbase (m)<input id=\"wheelbase\" type=\"number\" min=\"1.5\" max=\"5\" value=\"2.7\" step=\"any\"></label><label for=\"radius\">Turn radius (m)<input id=\"radius\" type=\"number\" min=\"2\" max=\"100\" value=\"9\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change an input.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 215\" role=\"img\" aria-label=\"Sensitivity plot showing recalculated results\"></svg><p class=\"small\">Curve recalculates as first input varies \u00b120%, bounded by its input limits. All numbers are educational synthetic scenarios, never measured vehicle performance.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 No certification or engineering guarantee.</p>",
    init: function(card) {
      try {
// OpenSTEM mechanical engineering, Book 17 model 10. Educational calculation only.
// Low-speed bicycle steer angle: delta=atan(L/R)
function compute(wheelbase,radius){return Math.atan(wheelbase/radius)*180/Math.PI;}
function update(){
 const wheelbase=Number(card.querySelector("#" + "wheelbase".replace(/^#/, "")).value);
 const radius=Number(card.querySelector("#" + "radius".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")); const details=card.querySelector("#" + 'details'.replace(/^#/, ""));
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const valid=Number.isFinite(wheelbase) && wheelbase>=1.5 && wheelbase<=5 && Number.isFinite(radius) && radius>=2 && radius<=100 && (true);
 if(!valid){metric.textContent='Invalid inputs';details.textContent='Use bounded values and maintain physical ordering.';plot.textContent='';return;}
 const y=compute(wheelbase,radius);
 if(!Number.isFinite(y) || Math.abs(y)>1e12){metric.textContent='Undefined';details.textContent='The simplified relation is outside its numerical domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' degree';
 details.textContent="Idealized road-wheel angle at low speed, not steering-wheel angle.";
 const xMin=Math.max(1.5,wheelbase===0?0:wheelbase*0.8);
 const xMax=Math.min(5,wheelbase===0?5*0.2:wheelbase*1.2);
 const pts=[];
 for(let k=0;k<=40;k++){ const x=xMin+(xMax-xMin)*k/40;const out=compute(x,radius);if(Number.isFinite(out))pts.push([x,out]); }
 if(pts.length<2){plot.textContent='';return;}
 const low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));
 const scale=Math.max(1e-9,high-low);
 const xy=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${178-135*(p[1]-low)/scale}`).join(' ');
 const yNow=178-135*(y-low)/scale;
 plot.innerHTML=`<line x1="45" y1="183" x2="647" y2="183" stroke="#94a8b2"/><line x1="45" y1="22" x2="45" y2="183" stroke="#94a8b2"/><polyline points="${xy}" fill="none" stroke="#126e7a" stroke-width="3"/><circle cx="${45+600*(wheelbase-xMin)/Math.max(1e-9,xMax-xMin)}" cy="${yNow}" r="5" fill="#d29232"/><text x="53" y="16" fill="#315667" font-size="13">Wheelbase sensitivity</text><text x="52" y="205" fill="#315667" font-size="12">${xMin.toPrecision(4)}</text><text x="587" y="205" fill="#315667" font-size="12">${xMax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 10:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 11,
    unit: 6,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 17</div><h3>Quarter-car natural frequency</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 working offline interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Editorial and safety status:</strong> Unreviewed teaching draft. Vehicle control, brakes, batteries and safety systems require competent independent engineering review and official compliance testing.</p><article class=\"model\"><h2>Model 11: Quarter-car natural frequency</h2><p><strong>Simplified relation:</strong> <code>f=sqrt(k/m)/(2*pi)</code></p><p class=\"small\">One-degree-of-freedom estimate without tire, damper or geometry effects.</p><div class=\"inputs\"><label for=\"stiff\">Spring wheel rate (N/m)<input id=\"stiff\" type=\"number\" min=\"1000\" max=\"100000\" value=\"20000\" step=\"any\"></label><label for=\"mass\">Corner sprung mass (kg)<input id=\"mass\" type=\"number\" min=\"40\" max=\"1500\" value=\"300\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change an input.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 215\" role=\"img\" aria-label=\"Sensitivity plot showing recalculated results\"></svg><p class=\"small\">Curve recalculates as first input varies \u00b120%, bounded by its input limits. All numbers are educational synthetic scenarios, never measured vehicle performance.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 No certification or engineering guarantee.</p>",
    init: function(card) {
      try {
// OpenSTEM mechanical engineering, Book 17 model 11. Educational calculation only.
// Quarter-car natural frequency: f=sqrt(k/m)/(2*pi)
function compute(stiff,mass){return Math.sqrt(stiff/mass)/(2*Math.PI);}
function update(){
 const stiff=Number(card.querySelector("#" + "stiff".replace(/^#/, "")).value);
 const mass=Number(card.querySelector("#" + "mass".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")); const details=card.querySelector("#" + 'details'.replace(/^#/, ""));
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const valid=Number.isFinite(stiff) && stiff>=1000 && stiff<=100000 && Number.isFinite(mass) && mass>=40 && mass<=1500 && (true);
 if(!valid){metric.textContent='Invalid inputs';details.textContent='Use bounded values and maintain physical ordering.';plot.textContent='';return;}
 const y=compute(stiff,mass);
 if(!Number.isFinite(y) || Math.abs(y)>1e12){metric.textContent='Undefined';details.textContent='The simplified relation is outside its numerical domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' Hz';
 details.textContent="One-degree-of-freedom estimate without tire, damper or geometry effects.";
 const xMin=Math.max(1000,stiff===0?0:stiff*0.8);
 const xMax=Math.min(100000,stiff===0?100000*0.2:stiff*1.2);
 const pts=[];
 for(let k=0;k<=40;k++){ const x=xMin+(xMax-xMin)*k/40;const out=compute(x,mass);if(Number.isFinite(out))pts.push([x,out]); }
 if(pts.length<2){plot.textContent='';return;}
 const low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));
 const scale=Math.max(1e-9,high-low);
 const xy=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${178-135*(p[1]-low)/scale}`).join(' ');
 const yNow=178-135*(y-low)/scale;
 plot.innerHTML=`<line x1="45" y1="183" x2="647" y2="183" stroke="#94a8b2"/><line x1="45" y1="22" x2="45" y2="183" stroke="#94a8b2"/><polyline points="${xy}" fill="none" stroke="#126e7a" stroke-width="3"/><circle cx="${45+600*(stiff-xMin)/Math.max(1e-9,xMax-xMin)}" cy="${yNow}" r="5" fill="#d29232"/><text x="53" y="16" fill="#315667" font-size="13">Spring wheel rate sensitivity</text><text x="52" y="205" fill="#315667" font-size="12">${xMin.toPrecision(4)}</text><text x="587" y="205" fill="#315667" font-size="12">${xMax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 11:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 12,
    unit: 6,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 17</div><h3>Longitudinal load transfer</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 working offline interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Editorial and safety status:</strong> Unreviewed teaching draft. Vehicle control, brakes, batteries and safety systems require competent independent engineering review and official compliance testing.</p><article class=\"model\"><h2>Model 12: Longitudinal load transfer</h2><p><strong>Simplified relation:</strong> <code>Delta F=m*a*h/L</code></p><p class=\"small\">Magnitude of ideal frontward transfer on level ground, not full axle load.</p><div class=\"inputs\"><label for=\"mass\">Vehicle mass (kg)<input id=\"mass\" type=\"number\" min=\"500\" max=\"10000\" value=\"1800\" step=\"any\"></label><label for=\"acc\">Longitudinal deceleration (m/s\u00b2)<input id=\"acc\" type=\"number\" min=\"0\" max=\"12\" value=\"5\" step=\"any\"></label><label for=\"height\">CG height (m)<input id=\"height\" type=\"number\" min=\"0.2\" max=\"1.5\" value=\"0.55\" step=\"any\"></label><label for=\"wheelbase\">Wheelbase (m)<input id=\"wheelbase\" type=\"number\" min=\"1.5\" max=\"5\" value=\"2.8\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change an input.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 215\" role=\"img\" aria-label=\"Sensitivity plot showing recalculated results\"></svg><p class=\"small\">Curve recalculates as first input varies \u00b120%, bounded by its input limits. All numbers are educational synthetic scenarios, never measured vehicle performance.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 No certification or engineering guarantee.</p>",
    init: function(card) {
      try {
// OpenSTEM mechanical engineering, Book 17 model 12. Educational calculation only.
// Longitudinal load transfer: Delta F=m*a*h/L
function compute(mass,acc,height,wheelbase){return mass*acc*height/wheelbase;}
function update(){
 const mass=Number(card.querySelector("#" + "mass".replace(/^#/, "")).value);
 const acc=Number(card.querySelector("#" + "acc".replace(/^#/, "")).value);
 const height=Number(card.querySelector("#" + "height".replace(/^#/, "")).value);
 const wheelbase=Number(card.querySelector("#" + "wheelbase".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")); const details=card.querySelector("#" + 'details'.replace(/^#/, ""));
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const valid=Number.isFinite(mass) && mass>=500 && mass<=10000 && Number.isFinite(acc) && acc>=0 && acc<=12 && Number.isFinite(height) && height>=0.2 && height<=1.5 && Number.isFinite(wheelbase) && wheelbase>=1.5 && wheelbase<=5 && (true);
 if(!valid){metric.textContent='Invalid inputs';details.textContent='Use bounded values and maintain physical ordering.';plot.textContent='';return;}
 const y=compute(mass,acc,height,wheelbase);
 if(!Number.isFinite(y) || Math.abs(y)>1e12){metric.textContent='Undefined';details.textContent='The simplified relation is outside its numerical domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' N';
 details.textContent="Magnitude of ideal frontward transfer on level ground, not full axle load.";
 const xMin=Math.max(500,mass===0?0:mass*0.8);
 const xMax=Math.min(10000,mass===0?10000*0.2:mass*1.2);
 const pts=[];
 for(let k=0;k<=40;k++){ const x=xMin+(xMax-xMin)*k/40;const out=compute(x,acc,height,wheelbase);if(Number.isFinite(out))pts.push([x,out]); }
 if(pts.length<2){plot.textContent='';return;}
 const low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));
 const scale=Math.max(1e-9,high-low);
 const xy=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${178-135*(p[1]-low)/scale}`).join(' ');
 const yNow=178-135*(y-low)/scale;
 plot.innerHTML=`<line x1="45" y1="183" x2="647" y2="183" stroke="#94a8b2"/><line x1="45" y1="22" x2="45" y2="183" stroke="#94a8b2"/><polyline points="${xy}" fill="none" stroke="#126e7a" stroke-width="3"/><circle cx="${45+600*(mass-xMin)/Math.max(1e-9,xMax-xMin)}" cy="${yNow}" r="5" fill="#d29232"/><text x="53" y="16" fill="#315667" font-size="13">Vehicle mass sensitivity</text><text x="52" y="205" fill="#315667" font-size="12">${xMin.toPrecision(4)}</text><text x="587" y="205" fill="#315667" font-size="12">${xMax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 12:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 13,
    unit: 7,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 17</div><h3>Simplified EV energy range</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 working offline interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Editorial and safety status:</strong> Unreviewed teaching draft. Vehicle control, brakes, batteries and safety systems require competent independent engineering review and official compliance testing.</p><article class=\"model\"><h2>Model 13: Simplified EV energy range</h2><p><strong>Simplified relation:</strong> <code>R=E_usable/(Wh/km)</code></p><p class=\"small\">No reserve, weather adjustment, pack aging or uncertainty.</p><div class=\"inputs\"><label for=\"energy\">Usable energy (kWh)<input id=\"energy\" type=\"number\" min=\"5\" max=\"250\" value=\"62\" step=\"any\"></label><label for=\"cons\">Pack consumption (Wh/km)<input id=\"cons\" type=\"number\" min=\"50\" max=\"600\" value=\"180\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change an input.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 215\" role=\"img\" aria-label=\"Sensitivity plot showing recalculated results\"></svg><p class=\"small\">Curve recalculates as first input varies \u00b120%, bounded by its input limits. All numbers are educational synthetic scenarios, never measured vehicle performance.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 No certification or engineering guarantee.</p>",
    init: function(card) {
      try {
// OpenSTEM mechanical engineering, Book 17 model 13. Educational calculation only.
// Simplified EV energy range: R=E_usable/(Wh/km)
function compute(energy,cons){return energy*1000/cons;}
function update(){
 const energy=Number(card.querySelector("#" + "energy".replace(/^#/, "")).value);
 const cons=Number(card.querySelector("#" + "cons".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")); const details=card.querySelector("#" + 'details'.replace(/^#/, ""));
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const valid=Number.isFinite(energy) && energy>=5 && energy<=250 && Number.isFinite(cons) && cons>=50 && cons<=600 && (true);
 if(!valid){metric.textContent='Invalid inputs';details.textContent='Use bounded values and maintain physical ordering.';plot.textContent='';return;}
 const y=compute(energy,cons);
 if(!Number.isFinite(y) || Math.abs(y)>1e12){metric.textContent='Undefined';details.textContent='The simplified relation is outside its numerical domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' km';
 details.textContent="No reserve, weather adjustment, pack aging or uncertainty.";
 const xMin=Math.max(5,energy===0?0:energy*0.8);
 const xMax=Math.min(250,energy===0?250*0.2:energy*1.2);
 const pts=[];
 for(let k=0;k<=40;k++){ const x=xMin+(xMax-xMin)*k/40;const out=compute(x,cons);if(Number.isFinite(out))pts.push([x,out]); }
 if(pts.length<2){plot.textContent='';return;}
 const low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));
 const scale=Math.max(1e-9,high-low);
 const xy=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${178-135*(p[1]-low)/scale}`).join(' ');
 const yNow=178-135*(y-low)/scale;
 plot.innerHTML=`<line x1="45" y1="183" x2="647" y2="183" stroke="#94a8b2"/><line x1="45" y1="22" x2="45" y2="183" stroke="#94a8b2"/><polyline points="${xy}" fill="none" stroke="#126e7a" stroke-width="3"/><circle cx="${45+600*(energy-xMin)/Math.max(1e-9,xMax-xMin)}" cy="${yNow}" r="5" fill="#d29232"/><text x="53" y="16" fill="#315667" font-size="13">Usable energy sensitivity</text><text x="52" y="205" fill="#315667" font-size="12">${xMin.toPrecision(4)}</text><text x="587" y="205" fill="#315667" font-size="12">${xMax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 13:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 14,
    unit: 7,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 17</div><h3>Ideal constant-power charging time</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 working offline interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Editorial and safety status:</strong> Unreviewed teaching draft. Vehicle control, brakes, batteries and safety systems require competent independent engineering review and official compliance testing.</p><article class=\"model\"><h2>Model 14: Ideal constant-power charging time</h2><p><strong>Simplified relation:</strong> <code>t=DeltaE/(P*eta)</code></p><p class=\"small\">Actual charging usually tapers; battery limits and thermal management omitted.</p><div class=\"inputs\"><label for=\"energy\">Energy delivered to pack (kWh)<input id=\"energy\" type=\"number\" min=\"1\" max=\"150\" value=\"30\" step=\"any\"></label><label for=\"power\">Charger input power (kW)<input id=\"power\" type=\"number\" min=\"1\" max=\"350\" value=\"50\" step=\"any\"></label><label for=\"eff\">Charging efficiency (%)<input id=\"eff\" type=\"number\" min=\"40\" max=\"100\" value=\"90\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change an input.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 215\" role=\"img\" aria-label=\"Sensitivity plot showing recalculated results\"></svg><p class=\"small\">Curve recalculates as first input varies \u00b120%, bounded by its input limits. All numbers are educational synthetic scenarios, never measured vehicle performance.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 No certification or engineering guarantee.</p>",
    init: function(card) {
      try {
// OpenSTEM mechanical engineering, Book 17 model 14. Educational calculation only.
// Ideal constant-power charging time: t=DeltaE/(P*eta)
function compute(energy,power,eff){return energy/(power*(eff/100))*60;}
function update(){
 const energy=Number(card.querySelector("#" + "energy".replace(/^#/, "")).value);
 const power=Number(card.querySelector("#" + "power".replace(/^#/, "")).value);
 const eff=Number(card.querySelector("#" + "eff".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")); const details=card.querySelector("#" + 'details'.replace(/^#/, ""));
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const valid=Number.isFinite(energy) && energy>=1 && energy<=150 && Number.isFinite(power) && power>=1 && power<=350 && Number.isFinite(eff) && eff>=40 && eff<=100 && (true);
 if(!valid){metric.textContent='Invalid inputs';details.textContent='Use bounded values and maintain physical ordering.';plot.textContent='';return;}
 const y=compute(energy,power,eff);
 if(!Number.isFinite(y) || Math.abs(y)>1e12){metric.textContent='Undefined';details.textContent='The simplified relation is outside its numerical domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' min';
 details.textContent="Actual charging usually tapers; battery limits and thermal management omitted.";
 const xMin=Math.max(1,energy===0?0:energy*0.8);
 const xMax=Math.min(150,energy===0?150*0.2:energy*1.2);
 const pts=[];
 for(let k=0;k<=40;k++){ const x=xMin+(xMax-xMin)*k/40;const out=compute(x,power,eff);if(Number.isFinite(out))pts.push([x,out]); }
 if(pts.length<2){plot.textContent='';return;}
 const low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));
 const scale=Math.max(1e-9,high-low);
 const xy=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${178-135*(p[1]-low)/scale}`).join(' ');
 const yNow=178-135*(y-low)/scale;
 plot.innerHTML=`<line x1="45" y1="183" x2="647" y2="183" stroke="#94a8b2"/><line x1="45" y1="22" x2="45" y2="183" stroke="#94a8b2"/><polyline points="${xy}" fill="none" stroke="#126e7a" stroke-width="3"/><circle cx="${45+600*(energy-xMin)/Math.max(1e-9,xMax-xMin)}" cy="${yNow}" r="5" fill="#d29232"/><text x="53" y="16" fill="#315667" font-size="13">Energy delivered to pack sensitivity</text><text x="52" y="205" fill="#315667" font-size="12">${xMin.toPrecision(4)}</text><text x="587" y="205" fill="#315667" font-size="12">${xMax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 14:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 15,
    unit: 8,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 17</div><h3>Wheel speed from engine speed</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 working offline interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Editorial and safety status:</strong> Unreviewed teaching draft. Vehicle control, brakes, batteries and safety systems require competent independent engineering review and official compliance testing.</p><article class=\"model\"><h2>Model 15: Wheel speed from engine speed</h2><p><strong>Simplified relation:</strong> <code>v=r*2*pi*(rpm/(gear*final))/60</code></p><p class=\"small\">Assumes locked drivetrain and no wheel slip; not valid during clutch or converter slip.</p><div class=\"inputs\"><label for=\"rpm\">Engine speed (rpm)<input id=\"rpm\" type=\"number\" min=\"500\" max=\"10000\" value=\"2400\" step=\"any\"></label><label for=\"gear\">Gear ratio (\u2014)<input id=\"gear\" type=\"number\" min=\"0.2\" max=\"8\" value=\"2\" step=\"any\"></label><label for=\"final\">Final drive (\u2014)<input id=\"final\" type=\"number\" min=\"1\" max=\"7\" value=\"4\" step=\"any\"></label><label for=\"radius\">Rolling radius (m)<input id=\"radius\" type=\"number\" min=\"0.2\" max=\"0.6\" value=\"0.31\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change an input.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 215\" role=\"img\" aria-label=\"Sensitivity plot showing recalculated results\"></svg><p class=\"small\">Curve recalculates as first input varies \u00b120%, bounded by its input limits. All numbers are educational synthetic scenarios, never measured vehicle performance.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 No certification or engineering guarantee.</p>",
    init: function(card) {
      try {
// OpenSTEM mechanical engineering, Book 17 model 15. Educational calculation only.
// Wheel speed from engine speed: v=r*2*pi*(rpm/(gear*final))/60
function compute(rpm,gear,final,radius){return 2*Math.PI*radius*rpm/(60*gear*final)*3.6;}
function update(){
 const rpm=Number(card.querySelector("#" + "rpm".replace(/^#/, "")).value);
 const gear=Number(card.querySelector("#" + "gear".replace(/^#/, "")).value);
 const final=Number(card.querySelector("#" + "final".replace(/^#/, "")).value);
 const radius=Number(card.querySelector("#" + "radius".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")); const details=card.querySelector("#" + 'details'.replace(/^#/, ""));
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const valid=Number.isFinite(rpm) && rpm>=500 && rpm<=10000 && Number.isFinite(gear) && gear>=0.2 && gear<=8 && Number.isFinite(final) && final>=1 && final<=7 && Number.isFinite(radius) && radius>=0.2 && radius<=0.6 && (true);
 if(!valid){metric.textContent='Invalid inputs';details.textContent='Use bounded values and maintain physical ordering.';plot.textContent='';return;}
 const y=compute(rpm,gear,final,radius);
 if(!Number.isFinite(y) || Math.abs(y)>1e12){metric.textContent='Undefined';details.textContent='The simplified relation is outside its numerical domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' km/h';
 details.textContent="Assumes locked drivetrain and no wheel slip; not valid during clutch or converter slip.";
 const xMin=Math.max(500,rpm===0?0:rpm*0.8);
 const xMax=Math.min(10000,rpm===0?10000*0.2:rpm*1.2);
 const pts=[];
 for(let k=0;k<=40;k++){ const x=xMin+(xMax-xMin)*k/40;const out=compute(x,gear,final,radius);if(Number.isFinite(out))pts.push([x,out]); }
 if(pts.length<2){plot.textContent='';return;}
 const low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));
 const scale=Math.max(1e-9,high-low);
 const xy=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${178-135*(p[1]-low)/scale}`).join(' ');
 const yNow=178-135*(y-low)/scale;
 plot.innerHTML=`<line x1="45" y1="183" x2="647" y2="183" stroke="#94a8b2"/><line x1="45" y1="22" x2="45" y2="183" stroke="#94a8b2"/><polyline points="${xy}" fill="none" stroke="#126e7a" stroke-width="3"/><circle cx="${45+600*(rpm-xMin)/Math.max(1e-9,xMax-xMin)}" cy="${yNow}" r="5" fill="#d29232"/><text x="53" y="16" fill="#315667" font-size="13">Engine speed sensitivity</text><text x="52" y="205" fill="#315667" font-size="12">${xMin.toPrecision(4)}</text><text x="587" y="205" fill="#315667" font-size="12">${xMax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));
update();
      } catch (err) {
        console.warn('Sim init error in model 15:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 16,
    unit: 8,
    html: "<header class=\"hero\"><div class=\"eyebrow\">OpenSTEM \u00b7 Mechanical Engineering \u00b7 Book 17</div><h3>Battery resistive heating</h3><p class=\"subtitle\">8 units \u00b7 40 lessons \u00b7 16 working offline interactive models \u00b7 8 synthetic datasets</p></header><p class=\"notice\"><strong>Editorial and safety status:</strong> Unreviewed teaching draft. Vehicle control, brakes, batteries and safety systems require competent independent engineering review and official compliance testing.</p><article class=\"model\"><h2>Model 16: Battery resistive heating</h2><p><strong>Simplified relation:</strong> <code>P_heat=I\u00b2R</code></p><p class=\"small\">Only ohmic heating; battery electrical safety and electrochemical heat omitted.</p><div class=\"inputs\"><label for=\"current\">Pack current (A)<input id=\"current\" type=\"number\" min=\"0\" max=\"1200\" value=\"200\" step=\"any\"></label><label for=\"resistance\">Equivalent pack resistance (ohm)<input id=\"resistance\" type=\"number\" min=\"0.001\" max=\"0.3\" value=\"0.05\" step=\"any\"></label></div><div class=\"result\"><div id=\"metric\" aria-live=\"polite\">\u2014</div><p id=\"details\" aria-live=\"polite\">Change an input.</p></div><svg id=\"plot\" class=\"plot\" viewBox=\"0 0 700 215\" role=\"img\" aria-label=\"Sensitivity plot showing recalculated results\"></svg><p class=\"small\">Curve recalculates as first input varies \u00b120%, bounded by its input limits. All numbers are educational synthetic scenarios, never measured vehicle performance.</p></article><p class=\"footer\">OpenSTEM educational draft \u00b7 No certification or engineering guarantee.</p>",
    init: function(card) {
      try {
// OpenSTEM mechanical engineering, Book 17 model 16. Educational calculation only.
// Battery resistive heating: P_heat=I²R
function compute(current,resistance){return current*current*resistance;}
function update(){
 const current=Number(card.querySelector("#" + "current".replace(/^#/, "")).value);
 const resistance=Number(card.querySelector("#" + "resistance".replace(/^#/, "")).value);
 const metric=card.querySelector("#" + 'metric'.replace(/^#/, "")); const details=card.querySelector("#" + 'details'.replace(/^#/, ""));
 const plot=card.querySelector("#" + 'plot'.replace(/^#/, ""));
 const valid=Number.isFinite(current) && current>=0 && current<=1200 && Number.isFinite(resistance) && resistance>=0.001 && resistance<=0.3 && (true);
 if(!valid){metric.textContent='Invalid inputs';details.textContent='Use bounded values and maintain physical ordering.';plot.textContent='';return;}
 const y=compute(current,resistance);
 if(!Number.isFinite(y) || Math.abs(y)>1e12){metric.textContent='Undefined';details.textContent='The simplified relation is outside its numerical domain.';plot.textContent='';return;}
 metric.textContent=y.toLocaleString('en-US',{maximumFractionDigits:4})+' W';
 details.textContent="Only ohmic heating; battery electrical safety and electrochemical heat omitted.";
 const xMin=Math.max(0,current===0?0:current*0.8);
 const xMax=Math.min(1200,current===0?1200*0.2:current*1.2);
 const pts=[];
 for(let k=0;k<=40;k++){ const x=xMin+(xMax-xMin)*k/40;const out=compute(x,resistance);if(Number.isFinite(out))pts.push([x,out]); }
 if(pts.length<2){plot.textContent='';return;}
 const low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));
 const scale=Math.max(1e-9,high-low);
 const xy=pts.map((p,j)=>`${45+j*600/(pts.length-1)},${178-135*(p[1]-low)/scale}`).join(' ');
 const yNow=178-135*(y-low)/scale;
 plot.innerHTML=`<line x1="45" y1="183" x2="647" y2="183" stroke="#94a8b2"/><line x1="45" y1="22" x2="45" y2="183" stroke="#94a8b2"/><polyline points="${xy}" fill="none" stroke="#126e7a" stroke-width="3"/><circle cx="${45+600*(current-xMin)/Math.max(1e-9,xMax-xMin)}" cy="${yNow}" r="5" fill="#d29232"/><text x="53" y="16" fill="#315667" font-size="13">Pack current sensitivity</text><text x="52" y="205" fill="#315667" font-size="12">${xMin.toPrecision(4)}</text><text x="587" y="205" fill="#315667" font-size="12">${xMax.toPrecision(4)}</text>`;
}
card.querySelectorAll('.inputs input').forEach(el=>el.addEventListener('input',update));
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
