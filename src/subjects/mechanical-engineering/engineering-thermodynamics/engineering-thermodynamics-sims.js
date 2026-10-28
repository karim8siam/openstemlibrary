/* engineering-thermodynamics Interactive Simulation Suite */
(function(window) {
  'use strict';

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: "<section class=\"hero\"><span class=\"chip\">UNIT 01 \u00b7 INTERACTIVE MODEL 01</span><h3>Ideal-gas container pressure</h3><p>Explore an idealized relation. Change both sliders and compare with a hand calculation. The plotted curve varies the first control with the second fixed at its current setting.</p></section><section class=\"grid\"><label class=\"card\" for=\"a\"><strong>Amount of gas</strong> <span class=\"small\">(mol)</span><div><output id=\"av\">5</output> <span class=\"small\">mol</span></div><input id=\"a\" type=\"range\" min=\"1\" max=\"12\" value=\"5\" step=\"any\" aria-label=\"Amount of gas\"></label><label class=\"card\" for=\"b\"><strong>Container volume</strong> <span class=\"small\">(m\u00b3)</span><div><output id=\"bv\">1</output> <span class=\"small\">m\u00b3</span></div><input id=\"b\" type=\"range\" min=\"0.2\" max=\"3\" value=\"1\" step=\"any\" aria-label=\"Container volume\"></label></section><section class=\"grid\" style=\"margin-top:16px\"><div class=\"card\"><div class=\"small\">Absolute pressure (kPa)</div><output id=\"r1\"></output></div><div class=\"card\"><div class=\"small\">Molar concentration (mol/m\u00b3)</div><output id=\"r2\"></output></div></section><section><h2>Parameter-response curve</h2><svg class=\"chart\" id=\"curve\" role=\"img\" aria-label=\"Plot of modeled response versus first slider\" viewBox=\"0 0 720 320\"><text class=\"svgtext\" x=\"30\" y=\"30\">Loading curve\u2026</text></svg></section><h2>Teaching interpretation</h2><p>Which direction does the response change when you increase each parameter separately? Calculate one point manually, identify the units and state a parameter range over which this model becomes unreliable. The simulation displays one possible relationship, not a measurement.</p><div class=\"warn\"><strong>Model boundary:</strong> Ideal gas at 300 K, negligible interactions; volume and amount are independent. These controls do not establish equipment ratings, safe operating limits or verified empirical accuracy.</div><p> \u00b7 </p>",
    init: function(card) {
      try {
const calc=(a,b)=>[a*8.314462618*300/b/1000,a/b];
const q=id=>document.getElementById(id), aEl=q('a'),bEl=q('b'),curve=q('curve');
const fmt=x=>(!Number.isFinite(x)?'Undefined':Math.abs(x)<0.0001&&x!==0?x.toExponential(5):x.toLocaleString('en-US',{maximumFractionDigits:6}));
function update(){
 const a=Number(aEl.value),b=Number(bEl.value),r=calc(a,b);q('av').textContent=fmt(a);q('bv').textContent=fmt(b);q('r1').textContent=fmt(r[0]);q('r2').textContent=fmt(r[1]);
 const lo=Number(aEl.min),hi=Number(aEl.max),pts=[];
 for(let i=0;i<=80;i++){let x=lo+i*(hi-lo)/80,y=calc(x,b)[0];if(Number.isFinite(y))pts.push([x,y]);}
 if(!pts.length){curve.textContent='No valid plot values';return;}
 let low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));let pad=Math.max((high-low)*0.12,Math.abs(high)*.01,1e-9);low-=pad;high+=pad;
 const px=x=>74+596*(x-lo)/(hi-lo),py=y=>260-206*(y-low)/(high-low);
 const d=pts.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(2)+' '+py(p[1]).toFixed(2)).join(' ');
 const ynow=Math.max(26,Math.min(262,py(r[0]))),xnow=px(a);
 curve.innerHTML='<line class="axis" x1="74" y1="260" x2="670" y2="260"/><line class="axis" x1="74" y1="45" x2="74" y2="260"/>'+
 '<path class="curve" d="'+d+'"/><circle class="marker" cx="'+xnow+'" cy="'+ynow+'" r="5"/>'+
 '<text class="svgtext" x="74" y="286">'+fmt(lo)+'</text><text class="svgtext" x="629" y="286">'+fmt(hi)+'</text>'+
 '<text class="svgtext" x="88" y="35">'+"Absolute pressure (kPa)"+'</text>'+
 '<text class="svgtext" x="300" y="307">'+"Amount of gas (mol)"+'</text>'+
 '<text class="svgtext" x="10" y="61">'+fmt(high-pad)+'</text><text class="svgtext" x="13" y="258">'+fmt(low+pad)+'</text>';
}
aEl.addEventListener('input',update);bEl.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 1,
    html: "<section class=\"hero\"><span class=\"chip\">UNIT 01 \u00b7 INTERACTIVE MODEL 02</span><h3>Temperature and pressure references</h3><p>Explore an idealized relation. Change both sliders and compare with a hand calculation. The plotted curve varies the first control with the second fixed at its current setting.</p></section><section class=\"grid\"><label class=\"card\" for=\"a\"><strong>Temperature</strong> <span class=\"small\">(\u00b0C)</span><div><output id=\"av\">26.85</output> <span class=\"small\">\u00b0C</span></div><input id=\"a\" type=\"range\" min=\"0\" max=\"120\" value=\"26.85\" step=\"any\" aria-label=\"Temperature\"></label><label class=\"card\" for=\"b\"><strong>Gauge pressure</strong> <span class=\"small\">(kPa)</span><div><output id=\"bv\">0</output> <span class=\"small\">kPa</span></div><input id=\"b\" type=\"range\" min=\"0\" max=\"300\" value=\"0\" step=\"any\" aria-label=\"Gauge pressure\"></label></section><section class=\"grid\" style=\"margin-top:16px\"><div class=\"card\"><div class=\"small\">Illustrative dry-air density (kg/m\u00b3)</div><output id=\"r1\"></output></div><div class=\"card\"><div class=\"small\">Absolute temperature (K)</div><output id=\"r2\"></output></div></section><section><h2>Parameter-response curve</h2><svg class=\"chart\" id=\"curve\" role=\"img\" aria-label=\"Plot of modeled response versus first slider\" viewBox=\"0 0 720 320\"><text class=\"svgtext\" x=\"30\" y=\"30\">Loading curve\u2026</text></svg></section><h2>Teaching interpretation</h2><p>Which direction does the response change when you increase each parameter separately? Calculate one point manually, identify the units and state a parameter range over which this model becomes unreliable. The simulation displays one possible relationship, not a measurement.</p><div class=\"warn\"><strong>Model boundary:</strong> Air ideal at atmospheric reference 101.325 kPa; absolute pressure = gauge + reference. These controls do not establish equipment ratings, safe operating limits or verified empirical accuracy.</div><p> \u00b7 </p>",
    init: function(card) {
      try {
const calc=(a,b)=>[(b+101.325)/(0.287*(a+273.15)),a+273.15];
const q=id=>document.getElementById(id), aEl=q('a'),bEl=q('b'),curve=q('curve');
const fmt=x=>(!Number.isFinite(x)?'Undefined':Math.abs(x)<0.0001&&x!==0?x.toExponential(5):x.toLocaleString('en-US',{maximumFractionDigits:6}));
function update(){
 const a=Number(aEl.value),b=Number(bEl.value),r=calc(a,b);q('av').textContent=fmt(a);q('bv').textContent=fmt(b);q('r1').textContent=fmt(r[0]);q('r2').textContent=fmt(r[1]);
 const lo=Number(aEl.min),hi=Number(aEl.max),pts=[];
 for(let i=0;i<=80;i++){let x=lo+i*(hi-lo)/80,y=calc(x,b)[0];if(Number.isFinite(y))pts.push([x,y]);}
 if(!pts.length){curve.textContent='No valid plot values';return;}
 let low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));let pad=Math.max((high-low)*0.12,Math.abs(high)*.01,1e-9);low-=pad;high+=pad;
 const px=x=>74+596*(x-lo)/(hi-lo),py=y=>260-206*(y-low)/(high-low);
 const d=pts.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(2)+' '+py(p[1]).toFixed(2)).join(' ');
 const ynow=Math.max(26,Math.min(262,py(r[0]))),xnow=px(a);
 curve.innerHTML='<line class="axis" x1="74" y1="260" x2="670" y2="260"/><line class="axis" x1="74" y1="45" x2="74" y2="260"/>'+
 '<path class="curve" d="'+d+'"/><circle class="marker" cx="'+xnow+'" cy="'+ynow+'" r="5"/>'+
 '<text class="svgtext" x="74" y="286">'+fmt(lo)+'</text><text class="svgtext" x="629" y="286">'+fmt(hi)+'</text>'+
 '<text class="svgtext" x="88" y="35">'+"Illustrative dry-air density (kg/m\u00b3)"+'</text>'+
 '<text class="svgtext" x="300" y="307">'+"Temperature (\u00b0C)"+'</text>'+
 '<text class="svgtext" x="10" y="61">'+fmt(high-pad)+'</text><text class="svgtext" x="13" y="258">'+fmt(low+pad)+'</text>';
}
aEl.addEventListener('input',update);bEl.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 2,
    html: "<section class=\"hero\"><span class=\"chip\">UNIT 02 \u00b7 INTERACTIVE MODEL 03</span><h3>Saturated mixture energy</h3><p>Explore an idealized relation. Change both sliders and compare with a hand calculation. The plotted curve varies the first control with the second fixed at its current setting.</p></section><section class=\"grid\"><label class=\"card\" for=\"a\"><strong>Vapor quality</strong> <span class=\"small\">(mass fraction)</span><div><output id=\"av\">0.5</output> <span class=\"small\">mass fraction</span></div><input id=\"a\" type=\"range\" min=\"0\" max=\"1\" value=\"0.5\" step=\"any\" aria-label=\"Vapor quality\"></label><label class=\"card\" for=\"b\"><strong>Total water mass</strong> <span class=\"small\">(kg)</span><div><output id=\"bv\">2</output> <span class=\"small\">kg</span></div><input id=\"b\" type=\"range\" min=\"0.1\" max=\"8\" value=\"2\" step=\"any\" aria-label=\"Total water mass\"></label></section><section class=\"grid\" style=\"margin-top:16px\"><div class=\"card\"><div class=\"small\">Total illustrative enthalpy (kJ)</div><output id=\"r1\"></output></div><div class=\"card\"><div class=\"small\">Equilibrium mixture volume (m\u00b3)</div><output id=\"r2\"></output></div></section><section><h2>Parameter-response curve</h2><svg class=\"chart\" id=\"curve\" role=\"img\" aria-label=\"Plot of modeled response versus first slider\" viewBox=\"0 0 720 320\"><text class=\"svgtext\" x=\"30\" y=\"30\">Loading curve\u2026</text></svg></section><h2>Teaching interpretation</h2><p>Which direction does the response change when you increase each parameter separately? Calculate one point manually, identify the units and state a parameter range over which this model becomes unreliable. The simulation displays one possible relationship, not a measurement.</p><div class=\"warn\"><strong>Model boundary:</strong> Illustrative water properties at 100 \u00b0C near atmospheric pressure; property constants rounded. These controls do not establish equipment ratings, safe operating limits or verified empirical accuracy.</div><p> \u00b7 </p>",
    init: function(card) {
      try {
const calc=(a,b)=>[b*(419+a*2257),b*(0.001043+a*(1.694-0.001043))];
const q=id=>document.getElementById(id), aEl=q('a'),bEl=q('b'),curve=q('curve');
const fmt=x=>(!Number.isFinite(x)?'Undefined':Math.abs(x)<0.0001&&x!==0?x.toExponential(5):x.toLocaleString('en-US',{maximumFractionDigits:6}));
function update(){
 const a=Number(aEl.value),b=Number(bEl.value),r=calc(a,b);q('av').textContent=fmt(a);q('bv').textContent=fmt(b);q('r1').textContent=fmt(r[0]);q('r2').textContent=fmt(r[1]);
 const lo=Number(aEl.min),hi=Number(aEl.max),pts=[];
 for(let i=0;i<=80;i++){let x=lo+i*(hi-lo)/80,y=calc(x,b)[0];if(Number.isFinite(y))pts.push([x,y]);}
 if(!pts.length){curve.textContent='No valid plot values';return;}
 let low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));let pad=Math.max((high-low)*0.12,Math.abs(high)*.01,1e-9);low-=pad;high+=pad;
 const px=x=>74+596*(x-lo)/(hi-lo),py=y=>260-206*(y-low)/(high-low);
 const d=pts.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(2)+' '+py(p[1]).toFixed(2)).join(' ');
 const ynow=Math.max(26,Math.min(262,py(r[0]))),xnow=px(a);
 curve.innerHTML='<line class="axis" x1="74" y1="260" x2="670" y2="260"/><line class="axis" x1="74" y1="45" x2="74" y2="260"/>'+
 '<path class="curve" d="'+d+'"/><circle class="marker" cx="'+xnow+'" cy="'+ynow+'" r="5"/>'+
 '<text class="svgtext" x="74" y="286">'+fmt(lo)+'</text><text class="svgtext" x="629" y="286">'+fmt(hi)+'</text>'+
 '<text class="svgtext" x="88" y="35">'+"Total illustrative enthalpy (kJ)"+'</text>'+
 '<text class="svgtext" x="300" y="307">'+"Vapor quality (mass fraction)"+'</text>'+
 '<text class="svgtext" x="10" y="61">'+fmt(high-pad)+'</text><text class="svgtext" x="13" y="258">'+fmt(low+pad)+'</text>';
}
aEl.addEventListener('input',update);bEl.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 2,
    html: "<section class=\"hero\"><span class=\"chip\">UNIT 02 \u00b7 INTERACTIVE MODEL 04</span><h3>Ideal-gas density</h3><p>Explore an idealized relation. Change both sliders and compare with a hand calculation. The plotted curve varies the first control with the second fixed at its current setting.</p></section><section class=\"grid\"><label class=\"card\" for=\"a\"><strong>Absolute pressure</strong> <span class=\"small\">(kPa)</span><div><output id=\"av\">100</output> <span class=\"small\">kPa</span></div><input id=\"a\" type=\"range\" min=\"60\" max=\"400\" value=\"100\" step=\"any\" aria-label=\"Absolute pressure\"></label><label class=\"card\" for=\"b\"><strong>Absolute temperature</strong> <span class=\"small\">(K)</span><div><output id=\"bv\">300</output> <span class=\"small\">K</span></div><input id=\"b\" type=\"range\" min=\"250\" max=\"600\" value=\"300\" step=\"any\" aria-label=\"Absolute temperature\"></label></section><section class=\"grid\" style=\"margin-top:16px\"><div class=\"card\"><div class=\"small\">Ideal-gas dry-air density (kg/m\u00b3)</div><output id=\"r1\"></output></div><div class=\"card\"><div class=\"small\">Specific volume (m\u00b3/kg)</div><output id=\"r2\"></output></div></section><section><h2>Parameter-response curve</h2><svg class=\"chart\" id=\"curve\" role=\"img\" aria-label=\"Plot of modeled response versus first slider\" viewBox=\"0 0 720 320\"><text class=\"svgtext\" x=\"30\" y=\"30\">Loading curve\u2026</text></svg></section><h2>Teaching interpretation</h2><p>Which direction does the response change when you increase each parameter separately? Calculate one point manually, identify the units and state a parameter range over which this model becomes unreliable. The simulation displays one possible relationship, not a measurement.</p><div class=\"warn\"><strong>Model boundary:</strong> Dry air with R = 0.287 kJ/(kg K); not valid near phase transition or substantial nonideality. These controls do not establish equipment ratings, safe operating limits or verified empirical accuracy.</div><p> \u00b7 </p>",
    init: function(card) {
      try {
const calc=(a,b)=>[a/(0.287*b),0.287*b/a];
const q=id=>document.getElementById(id), aEl=q('a'),bEl=q('b'),curve=q('curve');
const fmt=x=>(!Number.isFinite(x)?'Undefined':Math.abs(x)<0.0001&&x!==0?x.toExponential(5):x.toLocaleString('en-US',{maximumFractionDigits:6}));
function update(){
 const a=Number(aEl.value),b=Number(bEl.value),r=calc(a,b);q('av').textContent=fmt(a);q('bv').textContent=fmt(b);q('r1').textContent=fmt(r[0]);q('r2').textContent=fmt(r[1]);
 const lo=Number(aEl.min),hi=Number(aEl.max),pts=[];
 for(let i=0;i<=80;i++){let x=lo+i*(hi-lo)/80,y=calc(x,b)[0];if(Number.isFinite(y))pts.push([x,y]);}
 if(!pts.length){curve.textContent='No valid plot values';return;}
 let low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));let pad=Math.max((high-low)*0.12,Math.abs(high)*.01,1e-9);low-=pad;high+=pad;
 const px=x=>74+596*(x-lo)/(hi-lo),py=y=>260-206*(y-low)/(high-low);
 const d=pts.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(2)+' '+py(p[1]).toFixed(2)).join(' ');
 const ynow=Math.max(26,Math.min(262,py(r[0]))),xnow=px(a);
 curve.innerHTML='<line class="axis" x1="74" y1="260" x2="670" y2="260"/><line class="axis" x1="74" y1="45" x2="74" y2="260"/>'+
 '<path class="curve" d="'+d+'"/><circle class="marker" cx="'+xnow+'" cy="'+ynow+'" r="5"/>'+
 '<text class="svgtext" x="74" y="286">'+fmt(lo)+'</text><text class="svgtext" x="629" y="286">'+fmt(hi)+'</text>'+
 '<text class="svgtext" x="88" y="35">'+"Ideal-gas dry-air density (kg/m\u00b3)"+'</text>'+
 '<text class="svgtext" x="300" y="307">'+"Absolute pressure (kPa)"+'</text>'+
 '<text class="svgtext" x="10" y="61">'+fmt(high-pad)+'</text><text class="svgtext" x="13" y="258">'+fmt(low+pad)+'</text>';
}
aEl.addEventListener('input',update);bEl.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 3,
    html: "<section class=\"hero\"><span class=\"chip\">UNIT 03 \u00b7 INTERACTIVE MODEL 05</span><h3>Closed gas heating</h3><p>Explore an idealized relation. Change both sliders and compare with a hand calculation. The plotted curve varies the first control with the second fixed at its current setting.</p></section><section class=\"grid\"><label class=\"card\" for=\"a\"><strong>Gas mass</strong> <span class=\"small\">(kg)</span><div><output id=\"av\">2</output> <span class=\"small\">kg</span></div><input id=\"a\" type=\"range\" min=\"0.1\" max=\"12\" value=\"2\" step=\"any\" aria-label=\"Gas mass\"></label><label class=\"card\" for=\"b\"><strong>Temperature rise</strong> <span class=\"small\">(K)</span><div><output id=\"bv\">50</output> <span class=\"small\">K</span></div><input id=\"b\" type=\"range\" min=\"5\" max=\"200\" value=\"50\" step=\"any\" aria-label=\"Temperature rise\"></label></section><section class=\"grid\" style=\"margin-top:16px\"><div class=\"card\"><div class=\"small\">Ideal-gas enthalpy change (kJ)</div><output id=\"r1\"></output></div><div class=\"card\"><div class=\"small\">Ideal-gas internal-energy change (kJ)</div><output id=\"r2\"></output></div></section><section><h2>Parameter-response curve</h2><svg class=\"chart\" id=\"curve\" role=\"img\" aria-label=\"Plot of modeled response versus first slider\" viewBox=\"0 0 720 320\"><text class=\"svgtext\" x=\"30\" y=\"30\">Loading curve\u2026</text></svg></section><h2>Teaching interpretation</h2><p>Which direction does the response change when you increase each parameter separately? Calculate one point manually, identify the units and state a parameter range over which this model becomes unreliable. The simulation displays one possible relationship, not a measurement.</p><div class=\"warn\"><strong>Model boundary:</strong> Constant cp = 1.005, cv = 0.718 kJ/(kg K); distinguish heat transfer from property change. These controls do not establish equipment ratings, safe operating limits or verified empirical accuracy.</div><p> \u00b7 </p>",
    init: function(card) {
      try {
const calc=(a,b)=>[a*1.005*b,a*0.718*b];
const q=id=>document.getElementById(id), aEl=q('a'),bEl=q('b'),curve=q('curve');
const fmt=x=>(!Number.isFinite(x)?'Undefined':Math.abs(x)<0.0001&&x!==0?x.toExponential(5):x.toLocaleString('en-US',{maximumFractionDigits:6}));
function update(){
 const a=Number(aEl.value),b=Number(bEl.value),r=calc(a,b);q('av').textContent=fmt(a);q('bv').textContent=fmt(b);q('r1').textContent=fmt(r[0]);q('r2').textContent=fmt(r[1]);
 const lo=Number(aEl.min),hi=Number(aEl.max),pts=[];
 for(let i=0;i<=80;i++){let x=lo+i*(hi-lo)/80,y=calc(x,b)[0];if(Number.isFinite(y))pts.push([x,y]);}
 if(!pts.length){curve.textContent='No valid plot values';return;}
 let low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));let pad=Math.max((high-low)*0.12,Math.abs(high)*.01,1e-9);low-=pad;high+=pad;
 const px=x=>74+596*(x-lo)/(hi-lo),py=y=>260-206*(y-low)/(high-low);
 const d=pts.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(2)+' '+py(p[1]).toFixed(2)).join(' ');
 const ynow=Math.max(26,Math.min(262,py(r[0]))),xnow=px(a);
 curve.innerHTML='<line class="axis" x1="74" y1="260" x2="670" y2="260"/><line class="axis" x1="74" y1="45" x2="74" y2="260"/>'+
 '<path class="curve" d="'+d+'"/><circle class="marker" cx="'+xnow+'" cy="'+ynow+'" r="5"/>'+
 '<text class="svgtext" x="74" y="286">'+fmt(lo)+'</text><text class="svgtext" x="629" y="286">'+fmt(hi)+'</text>'+
 '<text class="svgtext" x="88" y="35">'+"Ideal-gas enthalpy change (kJ)"+'</text>'+
 '<text class="svgtext" x="300" y="307">'+"Gas mass (kg)"+'</text>'+
 '<text class="svgtext" x="10" y="61">'+fmt(high-pad)+'</text><text class="svgtext" x="13" y="258">'+fmt(low+pad)+'</text>';
}
aEl.addEventListener('input',update);bEl.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 3,
    html: "<section class=\"hero\"><span class=\"chip\">UNIT 03 \u00b7 INTERACTIVE MODEL 06</span><h3>Polytropic boundary work</h3><p>Explore an idealized relation. Change both sliders and compare with a hand calculation. The plotted curve varies the first control with the second fixed at its current setting.</p></section><section class=\"grid\"><label class=\"card\" for=\"a\"><strong>Initial pressure</strong> <span class=\"small\">(kPa)</span><div><output id=\"av\">200</output> <span class=\"small\">kPa</span></div><input id=\"a\" type=\"range\" min=\"100\" max=\"700\" value=\"200\" step=\"any\" aria-label=\"Initial pressure\"></label><label class=\"card\" for=\"b\"><strong>Volume ratio V\u2082/V\u2081</strong> <span class=\"small\">(\u2014)</span><div><output id=\"bv\">2</output> <span class=\"small\">\u2014</span></div><input id=\"b\" type=\"range\" min=\"1.05\" max=\"3\" value=\"2\" step=\"any\" aria-label=\"Volume ratio V\u2082/V\u2081\"></label></section><section class=\"grid\" style=\"margin-top:16px\"><div class=\"card\"><div class=\"small\">Boundary work done by gas (kJ)</div><output id=\"r1\"></output></div><div class=\"card\"><div class=\"small\">Final gas pressure (kPa)</div><output id=\"r2\"></output></div></section><section><h2>Parameter-response curve</h2><svg class=\"chart\" id=\"curve\" role=\"img\" aria-label=\"Plot of modeled response versus first slider\" viewBox=\"0 0 720 320\"><text class=\"svgtext\" x=\"30\" y=\"30\">Loading curve\u2026</text></svg></section><h2>Teaching interpretation</h2><p>Which direction does the response change when you increase each parameter separately? Calculate one point manually, identify the units and state a parameter range over which this model becomes unreliable. The simulation displays one possible relationship, not a measurement.</p><div class=\"warn\"><strong>Model boundary:</strong> Quasistatic pV^1.3=constant; initial volume 0.1 m\u00b3; expansion only. These controls do not establish equipment ratings, safe operating limits or verified empirical accuracy.</div><p> \u00b7 </p>",
    init: function(card) {
      try {
const calc=(a,b)=>[a*0.1*(Math.pow(b,1-1.3)-1)/(1-1.3),a*Math.pow(b,-1.3)];
const q=id=>document.getElementById(id), aEl=q('a'),bEl=q('b'),curve=q('curve');
const fmt=x=>(!Number.isFinite(x)?'Undefined':Math.abs(x)<0.0001&&x!==0?x.toExponential(5):x.toLocaleString('en-US',{maximumFractionDigits:6}));
function update(){
 const a=Number(aEl.value),b=Number(bEl.value),r=calc(a,b);q('av').textContent=fmt(a);q('bv').textContent=fmt(b);q('r1').textContent=fmt(r[0]);q('r2').textContent=fmt(r[1]);
 const lo=Number(aEl.min),hi=Number(aEl.max),pts=[];
 for(let i=0;i<=80;i++){let x=lo+i*(hi-lo)/80,y=calc(x,b)[0];if(Number.isFinite(y))pts.push([x,y]);}
 if(!pts.length){curve.textContent='No valid plot values';return;}
 let low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));let pad=Math.max((high-low)*0.12,Math.abs(high)*.01,1e-9);low-=pad;high+=pad;
 const px=x=>74+596*(x-lo)/(hi-lo),py=y=>260-206*(y-low)/(high-low);
 const d=pts.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(2)+' '+py(p[1]).toFixed(2)).join(' ');
 const ynow=Math.max(26,Math.min(262,py(r[0]))),xnow=px(a);
 curve.innerHTML='<line class="axis" x1="74" y1="260" x2="670" y2="260"/><line class="axis" x1="74" y1="45" x2="74" y2="260"/>'+
 '<path class="curve" d="'+d+'"/><circle class="marker" cx="'+xnow+'" cy="'+ynow+'" r="5"/>'+
 '<text class="svgtext" x="74" y="286">'+fmt(lo)+'</text><text class="svgtext" x="629" y="286">'+fmt(hi)+'</text>'+
 '<text class="svgtext" x="88" y="35">'+"Boundary work done by gas (kJ)"+'</text>'+
 '<text class="svgtext" x="300" y="307">'+"Initial pressure (kPa)"+'</text>'+
 '<text class="svgtext" x="10" y="61">'+fmt(high-pad)+'</text><text class="svgtext" x="13" y="258">'+fmt(low+pad)+'</text>';
}
aEl.addEventListener('input',update);bEl.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 4,
    html: "<section class=\"hero\"><span class=\"chip\">UNIT 04 \u00b7 INTERACTIVE MODEL 07</span><h3>Adiabatic nozzle speed</h3><p>Explore an idealized relation. Change both sliders and compare with a hand calculation. The plotted curve varies the first control with the second fixed at its current setting.</p></section><section class=\"grid\"><label class=\"card\" for=\"a\"><strong>Enthalpy drop</strong> <span class=\"small\">(kJ/kg)</span><div><output id=\"av\">20</output> <span class=\"small\">kJ/kg</span></div><input id=\"a\" type=\"range\" min=\"1\" max=\"120\" value=\"20\" step=\"any\" aria-label=\"Enthalpy drop\"></label><label class=\"card\" for=\"b\"><strong>Inlet velocity</strong> <span class=\"small\">(m/s)</span><div><output id=\"bv\">40</output> <span class=\"small\">m/s</span></div><input id=\"b\" type=\"range\" min=\"0\" max=\"200\" value=\"40\" step=\"any\" aria-label=\"Inlet velocity\"></label></section><section class=\"grid\" style=\"margin-top:16px\"><div class=\"card\"><div class=\"small\">Predicted exit velocity (m/s)</div><output id=\"r1\"></output></div><div class=\"card\"><div class=\"small\">Specific kinetic-energy gain (J/kg)</div><output id=\"r2\"></output></div></section><section><h2>Parameter-response curve</h2><svg class=\"chart\" id=\"curve\" role=\"img\" aria-label=\"Plot of modeled response versus first slider\" viewBox=\"0 0 720 320\"><text class=\"svgtext\" x=\"30\" y=\"30\">Loading curve\u2026</text></svg></section><h2>Teaching interpretation</h2><p>Which direction does the response change when you increase each parameter separately? Calculate one point manually, identify the units and state a parameter range over which this model becomes unreliable. The simulation displays one possible relationship, not a measurement.</p><div class=\"warn\"><strong>Model boundary:</strong> Idealized adiabatic nozzle, no shaft work/elevation effect; ignores friction and compressible flow constraints. These controls do not establish equipment ratings, safe operating limits or verified empirical accuracy.</div><p> \u00b7 </p>",
    init: function(card) {
      try {
const calc=(a,b)=>[Math.sqrt(b*b+2000*a),1000*a];
const q=id=>document.getElementById(id), aEl=q('a'),bEl=q('b'),curve=q('curve');
const fmt=x=>(!Number.isFinite(x)?'Undefined':Math.abs(x)<0.0001&&x!==0?x.toExponential(5):x.toLocaleString('en-US',{maximumFractionDigits:6}));
function update(){
 const a=Number(aEl.value),b=Number(bEl.value),r=calc(a,b);q('av').textContent=fmt(a);q('bv').textContent=fmt(b);q('r1').textContent=fmt(r[0]);q('r2').textContent=fmt(r[1]);
 const lo=Number(aEl.min),hi=Number(aEl.max),pts=[];
 for(let i=0;i<=80;i++){let x=lo+i*(hi-lo)/80,y=calc(x,b)[0];if(Number.isFinite(y))pts.push([x,y]);}
 if(!pts.length){curve.textContent='No valid plot values';return;}
 let low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));let pad=Math.max((high-low)*0.12,Math.abs(high)*.01,1e-9);low-=pad;high+=pad;
 const px=x=>74+596*(x-lo)/(hi-lo),py=y=>260-206*(y-low)/(high-low);
 const d=pts.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(2)+' '+py(p[1]).toFixed(2)).join(' ');
 const ynow=Math.max(26,Math.min(262,py(r[0]))),xnow=px(a);
 curve.innerHTML='<line class="axis" x1="74" y1="260" x2="670" y2="260"/><line class="axis" x1="74" y1="45" x2="74" y2="260"/>'+
 '<path class="curve" d="'+d+'"/><circle class="marker" cx="'+xnow+'" cy="'+ynow+'" r="5"/>'+
 '<text class="svgtext" x="74" y="286">'+fmt(lo)+'</text><text class="svgtext" x="629" y="286">'+fmt(hi)+'</text>'+
 '<text class="svgtext" x="88" y="35">'+"Predicted exit velocity (m/s)"+'</text>'+
 '<text class="svgtext" x="300" y="307">'+"Enthalpy drop (kJ/kg)"+'</text>'+
 '<text class="svgtext" x="10" y="61">'+fmt(high-pad)+'</text><text class="svgtext" x="13" y="258">'+fmt(low+pad)+'</text>';
}
aEl.addEventListener('input',update);bEl.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 4,
    html: "<section class=\"hero\"><span class=\"chip\">UNIT 04 \u00b7 INTERACTIVE MODEL 08</span><h3>Steady turbine power</h3><p>Explore an idealized relation. Change both sliders and compare with a hand calculation. The plotted curve varies the first control with the second fixed at its current setting.</p></section><section class=\"grid\"><label class=\"card\" for=\"a\"><strong>Mass flow</strong> <span class=\"small\">(kg/s)</span><div><output id=\"av\">3</output> <span class=\"small\">kg/s</span></div><input id=\"a\" type=\"range\" min=\"0.1\" max=\"15\" value=\"3\" step=\"any\" aria-label=\"Mass flow\"></label><label class=\"card\" for=\"b\"><strong>Specific enthalpy drop</strong> <span class=\"small\">(kJ/kg)</span><div><output id=\"bv\">80</output> <span class=\"small\">kJ/kg</span></div><input id=\"b\" type=\"range\" min=\"10\" max=\"400\" value=\"80\" step=\"any\" aria-label=\"Specific enthalpy drop\"></label></section><section class=\"grid\" style=\"margin-top:16px\"><div class=\"card\"><div class=\"small\">Shaft power (kW)</div><output id=\"r1\"></output></div><div class=\"card\"><div class=\"small\">Shaft power (MW)</div><output id=\"r2\"></output></div></section><section><h2>Parameter-response curve</h2><svg class=\"chart\" id=\"curve\" role=\"img\" aria-label=\"Plot of modeled response versus first slider\" viewBox=\"0 0 720 320\"><text class=\"svgtext\" x=\"30\" y=\"30\">Loading curve\u2026</text></svg></section><h2>Teaching interpretation</h2><p>Which direction does the response change when you increase each parameter separately? Calculate one point manually, identify the units and state a parameter range over which this model becomes unreliable. The simulation displays one possible relationship, not a measurement.</p><div class=\"warn\"><strong>Model boundary:</strong> Ideal adiabatic steady turbine; no heat/velocity/elevation terms or machine losses. These controls do not establish equipment ratings, safe operating limits or verified empirical accuracy.</div><p> \u00b7 </p>",
    init: function(card) {
      try {
const calc=(a,b)=>[a*b,0.001*a*b];
const q=id=>document.getElementById(id), aEl=q('a'),bEl=q('b'),curve=q('curve');
const fmt=x=>(!Number.isFinite(x)?'Undefined':Math.abs(x)<0.0001&&x!==0?x.toExponential(5):x.toLocaleString('en-US',{maximumFractionDigits:6}));
function update(){
 const a=Number(aEl.value),b=Number(bEl.value),r=calc(a,b);q('av').textContent=fmt(a);q('bv').textContent=fmt(b);q('r1').textContent=fmt(r[0]);q('r2').textContent=fmt(r[1]);
 const lo=Number(aEl.min),hi=Number(aEl.max),pts=[];
 for(let i=0;i<=80;i++){let x=lo+i*(hi-lo)/80,y=calc(x,b)[0];if(Number.isFinite(y))pts.push([x,y]);}
 if(!pts.length){curve.textContent='No valid plot values';return;}
 let low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));let pad=Math.max((high-low)*0.12,Math.abs(high)*.01,1e-9);low-=pad;high+=pad;
 const px=x=>74+596*(x-lo)/(hi-lo),py=y=>260-206*(y-low)/(high-low);
 const d=pts.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(2)+' '+py(p[1]).toFixed(2)).join(' ');
 const ynow=Math.max(26,Math.min(262,py(r[0]))),xnow=px(a);
 curve.innerHTML='<line class="axis" x1="74" y1="260" x2="670" y2="260"/><line class="axis" x1="74" y1="45" x2="74" y2="260"/>'+
 '<path class="curve" d="'+d+'"/><circle class="marker" cx="'+xnow+'" cy="'+ynow+'" r="5"/>'+
 '<text class="svgtext" x="74" y="286">'+fmt(lo)+'</text><text class="svgtext" x="629" y="286">'+fmt(hi)+'</text>'+
 '<text class="svgtext" x="88" y="35">'+"Shaft power (kW)"+'</text>'+
 '<text class="svgtext" x="300" y="307">'+"Mass flow (kg/s)"+'</text>'+
 '<text class="svgtext" x="10" y="61">'+fmt(high-pad)+'</text><text class="svgtext" x="13" y="258">'+fmt(low+pad)+'</text>';
}
aEl.addEventListener('input',update);bEl.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  MODELS.push({
    idx: 9,
    unit: 5,
    html: "<section class=\"hero\"><span class=\"chip\">UNIT 05 \u00b7 INTERACTIVE MODEL 09</span><h3>Carnot maximum efficiency</h3><p>Explore an idealized relation. Change both sliders and compare with a hand calculation. The plotted curve varies the first control with the second fixed at its current setting.</p></section><section class=\"grid\"><label class=\"card\" for=\"a\"><strong>Hot reservoir temperature</strong> <span class=\"small\">(K)</span><div><output id=\"av\">600</output> <span class=\"small\">K</span></div><input id=\"a\" type=\"range\" min=\"350\" max=\"1000\" value=\"600\" step=\"any\" aria-label=\"Hot reservoir temperature\"></label><label class=\"card\" for=\"b\"><strong>Cold reservoir temperature</strong> <span class=\"small\">(K)</span><div><output id=\"bv\">300</output> <span class=\"small\">K</span></div><input id=\"b\" type=\"range\" min=\"220\" max=\"330\" value=\"300\" step=\"any\" aria-label=\"Cold reservoir temperature\"></label></section><section class=\"grid\" style=\"margin-top:16px\"><div class=\"card\"><div class=\"small\">Maximum thermal efficiency (%)</div><output id=\"r1\"></output></div><div class=\"card\"><div class=\"small\">Minimum rejected fraction (%)</div><output id=\"r2\"></output></div></section><section><h2>Parameter-response curve</h2><svg class=\"chart\" id=\"curve\" role=\"img\" aria-label=\"Plot of modeled response versus first slider\" viewBox=\"0 0 720 320\"><text class=\"svgtext\" x=\"30\" y=\"30\">Loading curve\u2026</text></svg></section><h2>Teaching interpretation</h2><p>Which direction does the response change when you increase each parameter separately? Calculate one point manually, identify the units and state a parameter range over which this model becomes unreliable. The simulation displays one possible relationship, not a measurement.</p><div class=\"warn\"><strong>Model boundary:</strong> Two constant-temperature reservoirs; applies only if T_hot &gt; T_cold; not actual engine performance. These controls do not establish equipment ratings, safe operating limits or verified empirical accuracy.</div><p> \u00b7 </p>",
    init: function(card) {
      try {
const calc=(a,b)=>[100*(1-b/a),100* (b/a)];
const q=id=>document.getElementById(id), aEl=q('a'),bEl=q('b'),curve=q('curve');
const fmt=x=>(!Number.isFinite(x)?'Undefined':Math.abs(x)<0.0001&&x!==0?x.toExponential(5):x.toLocaleString('en-US',{maximumFractionDigits:6}));
function update(){
 const a=Number(aEl.value),b=Number(bEl.value),r=calc(a,b);q('av').textContent=fmt(a);q('bv').textContent=fmt(b);q('r1').textContent=fmt(r[0]);q('r2').textContent=fmt(r[1]);
 const lo=Number(aEl.min),hi=Number(aEl.max),pts=[];
 for(let i=0;i<=80;i++){let x=lo+i*(hi-lo)/80,y=calc(x,b)[0];if(Number.isFinite(y))pts.push([x,y]);}
 if(!pts.length){curve.textContent='No valid plot values';return;}
 let low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));let pad=Math.max((high-low)*0.12,Math.abs(high)*.01,1e-9);low-=pad;high+=pad;
 const px=x=>74+596*(x-lo)/(hi-lo),py=y=>260-206*(y-low)/(high-low);
 const d=pts.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(2)+' '+py(p[1]).toFixed(2)).join(' ');
 const ynow=Math.max(26,Math.min(262,py(r[0]))),xnow=px(a);
 curve.innerHTML='<line class="axis" x1="74" y1="260" x2="670" y2="260"/><line class="axis" x1="74" y1="45" x2="74" y2="260"/>'+
 '<path class="curve" d="'+d+'"/><circle class="marker" cx="'+xnow+'" cy="'+ynow+'" r="5"/>'+
 '<text class="svgtext" x="74" y="286">'+fmt(lo)+'</text><text class="svgtext" x="629" y="286">'+fmt(hi)+'</text>'+
 '<text class="svgtext" x="88" y="35">'+"Maximum thermal efficiency (%)"+'</text>'+
 '<text class="svgtext" x="300" y="307">'+"Hot reservoir temperature (K)"+'</text>'+
 '<text class="svgtext" x="10" y="61">'+fmt(high-pad)+'</text><text class="svgtext" x="13" y="258">'+fmt(low+pad)+'</text>';
}
aEl.addEventListener('input',update);bEl.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 9:', err);
      }
    }
  });

  MODELS.push({
    idx: 10,
    unit: 5,
    html: "<section class=\"hero\"><span class=\"chip\">UNIT 05 \u00b7 INTERACTIVE MODEL 10</span><h3>Carnot refrigerator COP</h3><p>Explore an idealized relation. Change both sliders and compare with a hand calculation. The plotted curve varies the first control with the second fixed at its current setting.</p></section><section class=\"grid\"><label class=\"card\" for=\"a\"><strong>Cold reservoir temperature</strong> <span class=\"small\">(K)</span><div><output id=\"av\">270</output> <span class=\"small\">K</span></div><input id=\"a\" type=\"range\" min=\"225\" max=\"295\" value=\"270\" step=\"any\" aria-label=\"Cold reservoir temperature\"></label><label class=\"card\" for=\"b\"><strong>Hot reservoir temperature</strong> <span class=\"small\">(K)</span><div><output id=\"bv\">310</output> <span class=\"small\">K</span></div><input id=\"b\" type=\"range\" min=\"300\" max=\"360\" value=\"310\" step=\"any\" aria-label=\"Hot reservoir temperature\"></label></section><section class=\"grid\" style=\"margin-top:16px\"><div class=\"card\"><div class=\"small\">Maximum refrigerator COP (\u2014)</div><output id=\"r1\"></output></div><div class=\"card\"><div class=\"small\">Maximum heat-pump COP (\u2014)</div><output id=\"r2\"></output></div></section><section><h2>Parameter-response curve</h2><svg class=\"chart\" id=\"curve\" role=\"img\" aria-label=\"Plot of modeled response versus first slider\" viewBox=\"0 0 720 320\"><text class=\"svgtext\" x=\"30\" y=\"30\">Loading curve\u2026</text></svg></section><h2>Teaching interpretation</h2><p>Which direction does the response change when you increase each parameter separately? Calculate one point manually, identify the units and state a parameter range over which this model becomes unreliable. The simulation displays one possible relationship, not a measurement.</p><div class=\"warn\"><strong>Model boundary:</strong> Two reservoirs, reversible ideal cycle; cold temperature must remain less than hot. These controls do not establish equipment ratings, safe operating limits or verified empirical accuracy.</div><p> \u00b7 </p>",
    init: function(card) {
      try {
const calc=(a,b)=>[a/(b-a),b/(b-a)];
const q=id=>document.getElementById(id), aEl=q('a'),bEl=q('b'),curve=q('curve');
const fmt=x=>(!Number.isFinite(x)?'Undefined':Math.abs(x)<0.0001&&x!==0?x.toExponential(5):x.toLocaleString('en-US',{maximumFractionDigits:6}));
function update(){
 const a=Number(aEl.value),b=Number(bEl.value),r=calc(a,b);q('av').textContent=fmt(a);q('bv').textContent=fmt(b);q('r1').textContent=fmt(r[0]);q('r2').textContent=fmt(r[1]);
 const lo=Number(aEl.min),hi=Number(aEl.max),pts=[];
 for(let i=0;i<=80;i++){let x=lo+i*(hi-lo)/80,y=calc(x,b)[0];if(Number.isFinite(y))pts.push([x,y]);}
 if(!pts.length){curve.textContent='No valid plot values';return;}
 let low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));let pad=Math.max((high-low)*0.12,Math.abs(high)*.01,1e-9);low-=pad;high+=pad;
 const px=x=>74+596*(x-lo)/(hi-lo),py=y=>260-206*(y-low)/(high-low);
 const d=pts.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(2)+' '+py(p[1]).toFixed(2)).join(' ');
 const ynow=Math.max(26,Math.min(262,py(r[0]))),xnow=px(a);
 curve.innerHTML='<line class="axis" x1="74" y1="260" x2="670" y2="260"/><line class="axis" x1="74" y1="45" x2="74" y2="260"/>'+
 '<path class="curve" d="'+d+'"/><circle class="marker" cx="'+xnow+'" cy="'+ynow+'" r="5"/>'+
 '<text class="svgtext" x="74" y="286">'+fmt(lo)+'</text><text class="svgtext" x="629" y="286">'+fmt(hi)+'</text>'+
 '<text class="svgtext" x="88" y="35">'+"Maximum refrigerator COP (\u2014)"+'</text>'+
 '<text class="svgtext" x="300" y="307">'+"Cold reservoir temperature (K)"+'</text>'+
 '<text class="svgtext" x="10" y="61">'+fmt(high-pad)+'</text><text class="svgtext" x="13" y="258">'+fmt(low+pad)+'</text>';
}
aEl.addEventListener('input',update);bEl.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 10:', err);
      }
    }
  });

  MODELS.push({
    idx: 11,
    unit: 6,
    html: "<section class=\"hero\"><span class=\"chip\">UNIT 06 \u00b7 INTERACTIVE MODEL 11</span><h3>Entropy created by heat flow</h3><p>Explore an idealized relation. Change both sliders and compare with a hand calculation. The plotted curve varies the first control with the second fixed at its current setting.</p></section><section class=\"grid\"><label class=\"card\" for=\"a\"><strong>Heat transferred</strong> <span class=\"small\">(kJ)</span><div><output id=\"av\">100</output> <span class=\"small\">kJ</span></div><input id=\"a\" type=\"range\" min=\"5\" max=\"500\" value=\"100\" step=\"any\" aria-label=\"Heat transferred\"></label><label class=\"card\" for=\"b\"><strong>Hot reservoir</strong> <span class=\"small\">(K)</span><div><output id=\"bv\">500</output> <span class=\"small\">K</span></div><input id=\"b\" type=\"range\" min=\"350\" max=\"900\" value=\"500\" step=\"any\" aria-label=\"Hot reservoir\"></label></section><section class=\"grid\" style=\"margin-top:16px\"><div class=\"card\"><div class=\"small\">Entropy generation (kJ/K)</div><output id=\"r1\"></output></div><div class=\"card\"><div class=\"small\">Exergy destroyed at 300 K (kJ)</div><output id=\"r2\"></output></div></section><section><h2>Parameter-response curve</h2><svg class=\"chart\" id=\"curve\" role=\"img\" aria-label=\"Plot of modeled response versus first slider\" viewBox=\"0 0 720 320\"><text class=\"svgtext\" x=\"30\" y=\"30\">Loading curve\u2026</text></svg></section><h2>Teaching interpretation</h2><p>Which direction does the response change when you increase each parameter separately? Calculate one point manually, identify the units and state a parameter range over which this model becomes unreliable. The simulation displays one possible relationship, not a measurement.</p><div class=\"warn\"><strong>Model boundary:</strong> Heat between 2 reservoirs, fixed cold reservoir 300 K; complete exchange; no external work. These controls do not establish equipment ratings, safe operating limits or verified empirical accuracy.</div><p> \u00b7 </p>",
    init: function(card) {
      try {
const calc=(a,b)=>[a*(1/300-1/b),300*a*(1/300-1/b)];
const q=id=>document.getElementById(id), aEl=q('a'),bEl=q('b'),curve=q('curve');
const fmt=x=>(!Number.isFinite(x)?'Undefined':Math.abs(x)<0.0001&&x!==0?x.toExponential(5):x.toLocaleString('en-US',{maximumFractionDigits:6}));
function update(){
 const a=Number(aEl.value),b=Number(bEl.value),r=calc(a,b);q('av').textContent=fmt(a);q('bv').textContent=fmt(b);q('r1').textContent=fmt(r[0]);q('r2').textContent=fmt(r[1]);
 const lo=Number(aEl.min),hi=Number(aEl.max),pts=[];
 for(let i=0;i<=80;i++){let x=lo+i*(hi-lo)/80,y=calc(x,b)[0];if(Number.isFinite(y))pts.push([x,y]);}
 if(!pts.length){curve.textContent='No valid plot values';return;}
 let low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));let pad=Math.max((high-low)*0.12,Math.abs(high)*.01,1e-9);low-=pad;high+=pad;
 const px=x=>74+596*(x-lo)/(hi-lo),py=y=>260-206*(y-low)/(high-low);
 const d=pts.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(2)+' '+py(p[1]).toFixed(2)).join(' ');
 const ynow=Math.max(26,Math.min(262,py(r[0]))),xnow=px(a);
 curve.innerHTML='<line class="axis" x1="74" y1="260" x2="670" y2="260"/><line class="axis" x1="74" y1="45" x2="74" y2="260"/>'+
 '<path class="curve" d="'+d+'"/><circle class="marker" cx="'+xnow+'" cy="'+ynow+'" r="5"/>'+
 '<text class="svgtext" x="74" y="286">'+fmt(lo)+'</text><text class="svgtext" x="629" y="286">'+fmt(hi)+'</text>'+
 '<text class="svgtext" x="88" y="35">'+"Entropy generation (kJ/K)"+'</text>'+
 '<text class="svgtext" x="300" y="307">'+"Heat transferred (kJ)"+'</text>'+
 '<text class="svgtext" x="10" y="61">'+fmt(high-pad)+'</text><text class="svgtext" x="13" y="258">'+fmt(low+pad)+'</text>';
}
aEl.addEventListener('input',update);bEl.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 11:', err);
      }
    }
  });

  MODELS.push({
    idx: 12,
    unit: 6,
    html: "<section class=\"hero\"><span class=\"chip\">UNIT 06 \u00b7 INTERACTIVE MODEL 12</span><h3>Available work from heat</h3><p>Explore an idealized relation. Change both sliders and compare with a hand calculation. The plotted curve varies the first control with the second fixed at its current setting.</p></section><section class=\"grid\"><label class=\"card\" for=\"a\"><strong>Heat supplied</strong> <span class=\"small\">(kJ)</span><div><output id=\"av\">100</output> <span class=\"small\">kJ</span></div><input id=\"a\" type=\"range\" min=\"10\" max=\"500\" value=\"100\" step=\"any\" aria-label=\"Heat supplied\"></label><label class=\"card\" for=\"b\"><strong>Heat-source temperature</strong> <span class=\"small\">(K)</span><div><output id=\"bv\">500</output> <span class=\"small\">K</span></div><input id=\"b\" type=\"range\" min=\"320\" max=\"1000\" value=\"500\" step=\"any\" aria-label=\"Heat-source temperature\"></label></section><section class=\"grid\" style=\"margin-top:16px\"><div class=\"card\"><div class=\"small\">Maximum heat-derived work (kJ)</div><output id=\"r1\"></output></div><div class=\"card\"><div class=\"small\">Carnot work fraction (%)</div><output id=\"r2\"></output></div></section><section><h2>Parameter-response curve</h2><svg class=\"chart\" id=\"curve\" role=\"img\" aria-label=\"Plot of modeled response versus first slider\" viewBox=\"0 0 720 320\"><text class=\"svgtext\" x=\"30\" y=\"30\">Loading curve\u2026</text></svg></section><h2>Teaching interpretation</h2><p>Which direction does the response change when you increase each parameter separately? Calculate one point manually, identify the units and state a parameter range over which this model becomes unreliable. The simulation displays one possible relationship, not a measurement.</p><div class=\"warn\"><strong>Model boundary:</strong> Uniform reservoir at T_s, ambient 300 K; theoretical reversible limit only. These controls do not establish equipment ratings, safe operating limits or verified empirical accuracy.</div><p> \u00b7 </p>",
    init: function(card) {
      try {
const calc=(a,b)=>[a*(1-300/b),100*(1-300/b)];
const q=id=>document.getElementById(id), aEl=q('a'),bEl=q('b'),curve=q('curve');
const fmt=x=>(!Number.isFinite(x)?'Undefined':Math.abs(x)<0.0001&&x!==0?x.toExponential(5):x.toLocaleString('en-US',{maximumFractionDigits:6}));
function update(){
 const a=Number(aEl.value),b=Number(bEl.value),r=calc(a,b);q('av').textContent=fmt(a);q('bv').textContent=fmt(b);q('r1').textContent=fmt(r[0]);q('r2').textContent=fmt(r[1]);
 const lo=Number(aEl.min),hi=Number(aEl.max),pts=[];
 for(let i=0;i<=80;i++){let x=lo+i*(hi-lo)/80,y=calc(x,b)[0];if(Number.isFinite(y))pts.push([x,y]);}
 if(!pts.length){curve.textContent='No valid plot values';return;}
 let low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));let pad=Math.max((high-low)*0.12,Math.abs(high)*.01,1e-9);low-=pad;high+=pad;
 const px=x=>74+596*(x-lo)/(hi-lo),py=y=>260-206*(y-low)/(high-low);
 const d=pts.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(2)+' '+py(p[1]).toFixed(2)).join(' ');
 const ynow=Math.max(26,Math.min(262,py(r[0]))),xnow=px(a);
 curve.innerHTML='<line class="axis" x1="74" y1="260" x2="670" y2="260"/><line class="axis" x1="74" y1="45" x2="74" y2="260"/>'+
 '<path class="curve" d="'+d+'"/><circle class="marker" cx="'+xnow+'" cy="'+ynow+'" r="5"/>'+
 '<text class="svgtext" x="74" y="286">'+fmt(lo)+'</text><text class="svgtext" x="629" y="286">'+fmt(hi)+'</text>'+
 '<text class="svgtext" x="88" y="35">'+"Maximum heat-derived work (kJ)"+'</text>'+
 '<text class="svgtext" x="300" y="307">'+"Heat supplied (kJ)"+'</text>'+
 '<text class="svgtext" x="10" y="61">'+fmt(high-pad)+'</text><text class="svgtext" x="13" y="258">'+fmt(low+pad)+'</text>';
}
aEl.addEventListener('input',update);bEl.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 12:', err);
      }
    }
  });

  MODELS.push({
    idx: 13,
    unit: 7,
    html: "<section class=\"hero\"><span class=\"chip\">UNIT 07 \u00b7 INTERACTIVE MODEL 13</span><h3>Otto-cycle air standard</h3><p>Explore an idealized relation. Change both sliders and compare with a hand calculation. The plotted curve varies the first control with the second fixed at its current setting.</p></section><section class=\"grid\"><label class=\"card\" for=\"a\"><strong>Compression ratio</strong> <span class=\"small\">(\u2014)</span><div><output id=\"av\">8</output> <span class=\"small\">\u2014</span></div><input id=\"a\" type=\"range\" min=\"4\" max=\"16\" value=\"8\" step=\"any\" aria-label=\"Compression ratio\"></label><label class=\"card\" for=\"b\"><strong>Heat-capacity ratio</strong> <span class=\"small\">(\u2014)</span><div><output id=\"bv\">1.4</output> <span class=\"small\">\u2014</span></div><input id=\"b\" type=\"range\" min=\"1.26\" max=\"1.42\" value=\"1.4\" step=\"any\" aria-label=\"Heat-capacity ratio\"></label></section><section class=\"grid\" style=\"margin-top:16px\"><div class=\"card\"><div class=\"small\">Ideal Otto efficiency (%)</div><output id=\"r1\"></output></div><div class=\"card\"><div class=\"small\">Heat-rejection fraction (%)</div><output id=\"r2\"></output></div></section><section><h2>Parameter-response curve</h2><svg class=\"chart\" id=\"curve\" role=\"img\" aria-label=\"Plot of modeled response versus first slider\" viewBox=\"0 0 720 320\"><text class=\"svgtext\" x=\"30\" y=\"30\">Loading curve\u2026</text></svg></section><h2>Teaching interpretation</h2><p>Which direction does the response change when you increase each parameter separately? Calculate one point manually, identify the units and state a parameter range over which this model becomes unreliable. The simulation displays one possible relationship, not a measurement.</p><div class=\"warn\"><strong>Model boundary:</strong> Cold-air-standard reversible Otto model; not fuel-to-shaft engine efficiency. These controls do not establish equipment ratings, safe operating limits or verified empirical accuracy.</div><p> \u00b7 </p>",
    init: function(card) {
      try {
const calc=(a,b)=>[100*(1-Math.pow(a,1-b)),100*Math.pow(a,1-b)];
const q=id=>document.getElementById(id), aEl=q('a'),bEl=q('b'),curve=q('curve');
const fmt=x=>(!Number.isFinite(x)?'Undefined':Math.abs(x)<0.0001&&x!==0?x.toExponential(5):x.toLocaleString('en-US',{maximumFractionDigits:6}));
function update(){
 const a=Number(aEl.value),b=Number(bEl.value),r=calc(a,b);q('av').textContent=fmt(a);q('bv').textContent=fmt(b);q('r1').textContent=fmt(r[0]);q('r2').textContent=fmt(r[1]);
 const lo=Number(aEl.min),hi=Number(aEl.max),pts=[];
 for(let i=0;i<=80;i++){let x=lo+i*(hi-lo)/80,y=calc(x,b)[0];if(Number.isFinite(y))pts.push([x,y]);}
 if(!pts.length){curve.textContent='No valid plot values';return;}
 let low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));let pad=Math.max((high-low)*0.12,Math.abs(high)*.01,1e-9);low-=pad;high+=pad;
 const px=x=>74+596*(x-lo)/(hi-lo),py=y=>260-206*(y-low)/(high-low);
 const d=pts.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(2)+' '+py(p[1]).toFixed(2)).join(' ');
 const ynow=Math.max(26,Math.min(262,py(r[0]))),xnow=px(a);
 curve.innerHTML='<line class="axis" x1="74" y1="260" x2="670" y2="260"/><line class="axis" x1="74" y1="45" x2="74" y2="260"/>'+
 '<path class="curve" d="'+d+'"/><circle class="marker" cx="'+xnow+'" cy="'+ynow+'" r="5"/>'+
 '<text class="svgtext" x="74" y="286">'+fmt(lo)+'</text><text class="svgtext" x="629" y="286">'+fmt(hi)+'</text>'+
 '<text class="svgtext" x="88" y="35">'+"Ideal Otto efficiency (%)"+'</text>'+
 '<text class="svgtext" x="300" y="307">'+"Compression ratio (\u2014)"+'</text>'+
 '<text class="svgtext" x="10" y="61">'+fmt(high-pad)+'</text><text class="svgtext" x="13" y="258">'+fmt(low+pad)+'</text>';
}
aEl.addEventListener('input',update);bEl.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 13:', err);
      }
    }
  });

  MODELS.push({
    idx: 14,
    unit: 7,
    html: "<section class=\"hero\"><span class=\"chip\">UNIT 07 \u00b7 INTERACTIVE MODEL 14</span><h3>Vapor-compression performance</h3><p>Explore an idealized relation. Change both sliders and compare with a hand calculation. The plotted curve varies the first control with the second fixed at its current setting.</p></section><section class=\"grid\"><label class=\"card\" for=\"a\"><strong>Cooling duty</strong> <span class=\"small\">(kW)</span><div><output id=\"av\">8</output> <span class=\"small\">kW</span></div><input id=\"a\" type=\"range\" min=\"1\" max=\"25\" value=\"8\" step=\"any\" aria-label=\"Cooling duty\"></label><label class=\"card\" for=\"b\"><strong>Compressor power</strong> <span class=\"small\">(kW)</span><div><output id=\"bv\">2</output> <span class=\"small\">kW</span></div><input id=\"b\" type=\"range\" min=\"1\" max=\"10\" value=\"2\" step=\"any\" aria-label=\"Compressor power\"></label></section><section class=\"grid\" style=\"margin-top:16px\"><div class=\"card\"><div class=\"small\">Measured-input COP surrogate (\u2014)</div><output id=\"r1\"></output></div><div class=\"card\"><div class=\"small\">Heat rejection by condenser (kW)</div><output id=\"r2\"></output></div></section><section><h2>Parameter-response curve</h2><svg class=\"chart\" id=\"curve\" role=\"img\" aria-label=\"Plot of modeled response versus first slider\" viewBox=\"0 0 720 320\"><text class=\"svgtext\" x=\"30\" y=\"30\">Loading curve\u2026</text></svg></section><h2>Teaching interpretation</h2><p>Which direction does the response change when you increase each parameter separately? Calculate one point manually, identify the units and state a parameter range over which this model becomes unreliable. The simulation displays one possible relationship, not a measurement.</p><div class=\"warn\"><strong>Model boundary:</strong> Simple steady energy accounting; excludes auxiliaries, cycling and transients; no refrigerant state data. These controls do not establish equipment ratings, safe operating limits or verified empirical accuracy.</div><p> \u00b7 </p>",
    init: function(card) {
      try {
const calc=(a,b)=>[a/b,a+b];
const q=id=>document.getElementById(id), aEl=q('a'),bEl=q('b'),curve=q('curve');
const fmt=x=>(!Number.isFinite(x)?'Undefined':Math.abs(x)<0.0001&&x!==0?x.toExponential(5):x.toLocaleString('en-US',{maximumFractionDigits:6}));
function update(){
 const a=Number(aEl.value),b=Number(bEl.value),r=calc(a,b);q('av').textContent=fmt(a);q('bv').textContent=fmt(b);q('r1').textContent=fmt(r[0]);q('r2').textContent=fmt(r[1]);
 const lo=Number(aEl.min),hi=Number(aEl.max),pts=[];
 for(let i=0;i<=80;i++){let x=lo+i*(hi-lo)/80,y=calc(x,b)[0];if(Number.isFinite(y))pts.push([x,y]);}
 if(!pts.length){curve.textContent='No valid plot values';return;}
 let low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));let pad=Math.max((high-low)*0.12,Math.abs(high)*.01,1e-9);low-=pad;high+=pad;
 const px=x=>74+596*(x-lo)/(hi-lo),py=y=>260-206*(y-low)/(high-low);
 const d=pts.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(2)+' '+py(p[1]).toFixed(2)).join(' ');
 const ynow=Math.max(26,Math.min(262,py(r[0]))),xnow=px(a);
 curve.innerHTML='<line class="axis" x1="74" y1="260" x2="670" y2="260"/><line class="axis" x1="74" y1="45" x2="74" y2="260"/>'+
 '<path class="curve" d="'+d+'"/><circle class="marker" cx="'+xnow+'" cy="'+ynow+'" r="5"/>'+
 '<text class="svgtext" x="74" y="286">'+fmt(lo)+'</text><text class="svgtext" x="629" y="286">'+fmt(hi)+'</text>'+
 '<text class="svgtext" x="88" y="35">'+"Measured-input COP surrogate (\u2014)"+'</text>'+
 '<text class="svgtext" x="300" y="307">'+"Cooling duty (kW)"+'</text>'+
 '<text class="svgtext" x="10" y="61">'+fmt(high-pad)+'</text><text class="svgtext" x="13" y="258">'+fmt(low+pad)+'</text>';
}
aEl.addEventListener('input',update);bEl.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 14:', err);
      }
    }
  });

  MODELS.push({
    idx: 15,
    unit: 8,
    html: "<section class=\"hero\"><span class=\"chip\">UNIT 08 \u00b7 INTERACTIVE MODEL 15</span><h3>Moist-air humidity ratio</h3><p>Explore an idealized relation. Change both sliders and compare with a hand calculation. The plotted curve varies the first control with the second fixed at its current setting.</p></section><section class=\"grid\"><label class=\"card\" for=\"a\"><strong>Water vapor partial pressure</strong> <span class=\"small\">(kPa)</span><div><output id=\"av\">2</output> <span class=\"small\">kPa</span></div><input id=\"a\" type=\"range\" min=\"0.2\" max=\"4\" value=\"2\" step=\"any\" aria-label=\"Water vapor partial pressure\"></label><label class=\"card\" for=\"b\"><strong>Total absolute pressure</strong> <span class=\"small\">(kPa)</span><div><output id=\"bv\">101.325</output> <span class=\"small\">kPa</span></div><input id=\"b\" type=\"range\" min=\"90\" max=\"110\" value=\"101.325\" step=\"any\" aria-label=\"Total absolute pressure\"></label></section><section class=\"grid\" style=\"margin-top:16px\"><div class=\"card\"><div class=\"small\">Humidity ratio (kg/kg dry air)</div><output id=\"r1\"></output></div><div class=\"card\"><div class=\"small\">Humidity ratio (g/kg dry air)</div><output id=\"r2\"></output></div></section><section><h2>Parameter-response curve</h2><svg class=\"chart\" id=\"curve\" role=\"img\" aria-label=\"Plot of modeled response versus first slider\" viewBox=\"0 0 720 320\"><text class=\"svgtext\" x=\"30\" y=\"30\">Loading curve\u2026</text></svg></section><h2>Teaching interpretation</h2><p>Which direction does the response change when you increase each parameter separately? Calculate one point manually, identify the units and state a parameter range over which this model becomes unreliable. The simulation displays one possible relationship, not a measurement.</p><div class=\"warn\"><strong>Model boundary:</strong> Ideal-gas partial-pressure psychrometrics; assumes p_v &lt; p and neglects condensate. These controls do not establish equipment ratings, safe operating limits or verified empirical accuracy.</div><p> \u00b7 </p>",
    init: function(card) {
      try {
const calc=(a,b)=>[0.62198*a/(b-a),1000*0.62198*a/(b-a)];
const q=id=>document.getElementById(id), aEl=q('a'),bEl=q('b'),curve=q('curve');
const fmt=x=>(!Number.isFinite(x)?'Undefined':Math.abs(x)<0.0001&&x!==0?x.toExponential(5):x.toLocaleString('en-US',{maximumFractionDigits:6}));
function update(){
 const a=Number(aEl.value),b=Number(bEl.value),r=calc(a,b);q('av').textContent=fmt(a);q('bv').textContent=fmt(b);q('r1').textContent=fmt(r[0]);q('r2').textContent=fmt(r[1]);
 const lo=Number(aEl.min),hi=Number(aEl.max),pts=[];
 for(let i=0;i<=80;i++){let x=lo+i*(hi-lo)/80,y=calc(x,b)[0];if(Number.isFinite(y))pts.push([x,y]);}
 if(!pts.length){curve.textContent='No valid plot values';return;}
 let low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));let pad=Math.max((high-low)*0.12,Math.abs(high)*.01,1e-9);low-=pad;high+=pad;
 const px=x=>74+596*(x-lo)/(hi-lo),py=y=>260-206*(y-low)/(high-low);
 const d=pts.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(2)+' '+py(p[1]).toFixed(2)).join(' ');
 const ynow=Math.max(26,Math.min(262,py(r[0]))),xnow=px(a);
 curve.innerHTML='<line class="axis" x1="74" y1="260" x2="670" y2="260"/><line class="axis" x1="74" y1="45" x2="74" y2="260"/>'+
 '<path class="curve" d="'+d+'"/><circle class="marker" cx="'+xnow+'" cy="'+ynow+'" r="5"/>'+
 '<text class="svgtext" x="74" y="286">'+fmt(lo)+'</text><text class="svgtext" x="629" y="286">'+fmt(hi)+'</text>'+
 '<text class="svgtext" x="88" y="35">'+"Humidity ratio (kg/kg dry air)"+'</text>'+
 '<text class="svgtext" x="300" y="307">'+"Water vapor partial pressure (kPa)"+'</text>'+
 '<text class="svgtext" x="10" y="61">'+fmt(high-pad)+'</text><text class="svgtext" x="13" y="258">'+fmt(low+pad)+'</text>';
}
aEl.addEventListener('input',update);bEl.addEventListener('input',update);update();
      } catch (err) {
        console.warn('Sim init error in model 15:', err);
      }
    }
  });

  MODELS.push({
    idx: 16,
    unit: 8,
    html: "<section class=\"hero\"><span class=\"chip\">UNIT 08 \u00b7 INTERACTIVE MODEL 16</span><h3>Methane combustion CO\u2082</h3><p>Explore an idealized relation. Change both sliders and compare with a hand calculation. The plotted curve varies the first control with the second fixed at its current setting.</p></section><section class=\"grid\"><label class=\"card\" for=\"a\"><strong>Methane feed</strong> <span class=\"small\">(kg)</span><div><output id=\"av\">5</output> <span class=\"small\">kg</span></div><input id=\"a\" type=\"range\" min=\"0.1\" max=\"100\" value=\"5\" step=\"any\" aria-label=\"Methane feed\"></label><label class=\"card\" for=\"b\"><strong>Complete combustion fraction</strong> <span class=\"small\">(\u2014)</span><div><output id=\"bv\">0.95</output> <span class=\"small\">\u2014</span></div><input id=\"b\" type=\"range\" min=\"0\" max=\"1\" value=\"0.95\" step=\"any\" aria-label=\"Complete combustion fraction\"></label></section><section class=\"grid\" style=\"margin-top:16px\"><div class=\"card\"><div class=\"small\">Stoichiometric CO\u2082 produced (kg)</div><output id=\"r1\"></output></div><div class=\"card\"><div class=\"small\">O\u2082 consumed (kg)</div><output id=\"r2\"></output></div></section><section><h2>Parameter-response curve</h2><svg class=\"chart\" id=\"curve\" role=\"img\" aria-label=\"Plot of modeled response versus first slider\" viewBox=\"0 0 720 320\"><text class=\"svgtext\" x=\"30\" y=\"30\">Loading curve\u2026</text></svg></section><h2>Teaching interpretation</h2><p>Which direction does the response change when you increase each parameter separately? Calculate one point manually, identify the units and state a parameter range over which this model becomes unreliable. The simulation displays one possible relationship, not a measurement.</p><div class=\"warn\"><strong>Model boundary:</strong> Ideal stoichiometric CH\u2084+2O\u2082\u2192CO\u2082+2H\u2082O for fully burned fraction; excludes lifecycle impacts. These controls do not establish equipment ratings, safe operating limits or verified empirical accuracy.</div><p> \u00b7 </p>",
    init: function(card) {
      try {
const calc=(a,b)=>[a*b*2.75,a*b*4];
const q=id=>document.getElementById(id), aEl=q('a'),bEl=q('b'),curve=q('curve');
const fmt=x=>(!Number.isFinite(x)?'Undefined':Math.abs(x)<0.0001&&x!==0?x.toExponential(5):x.toLocaleString('en-US',{maximumFractionDigits:6}));
function update(){
 const a=Number(aEl.value),b=Number(bEl.value),r=calc(a,b);q('av').textContent=fmt(a);q('bv').textContent=fmt(b);q('r1').textContent=fmt(r[0]);q('r2').textContent=fmt(r[1]);
 const lo=Number(aEl.min),hi=Number(aEl.max),pts=[];
 for(let i=0;i<=80;i++){let x=lo+i*(hi-lo)/80,y=calc(x,b)[0];if(Number.isFinite(y))pts.push([x,y]);}
 if(!pts.length){curve.textContent='No valid plot values';return;}
 let low=Math.min(...pts.map(p=>p[1])),high=Math.max(...pts.map(p=>p[1]));let pad=Math.max((high-low)*0.12,Math.abs(high)*.01,1e-9);low-=pad;high+=pad;
 const px=x=>74+596*(x-lo)/(hi-lo),py=y=>260-206*(y-low)/(high-low);
 const d=pts.map((p,i)=>(i?'L':'M')+px(p[0]).toFixed(2)+' '+py(p[1]).toFixed(2)).join(' ');
 const ynow=Math.max(26,Math.min(262,py(r[0]))),xnow=px(a);
 curve.innerHTML='<line class="axis" x1="74" y1="260" x2="670" y2="260"/><line class="axis" x1="74" y1="45" x2="74" y2="260"/>'+
 '<path class="curve" d="'+d+'"/><circle class="marker" cx="'+xnow+'" cy="'+ynow+'" r="5"/>'+
 '<text class="svgtext" x="74" y="286">'+fmt(lo)+'</text><text class="svgtext" x="629" y="286">'+fmt(hi)+'</text>'+
 '<text class="svgtext" x="88" y="35">'+"Stoichiometric CO\u2082 produced (kg)"+'</text>'+
 '<text class="svgtext" x="300" y="307">'+"Methane feed (kg)"+'</text>'+
 '<text class="svgtext" x="10" y="61">'+fmt(high-pad)+'</text><text class="svgtext" x="13" y="258">'+fmt(low+pad)+'</text>';
}
aEl.addEventListener('input',update);bEl.addEventListener('input',update);update();
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
