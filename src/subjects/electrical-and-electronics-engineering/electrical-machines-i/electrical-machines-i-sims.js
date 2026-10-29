/* electrical-machines-i Interactive Simulation Suite */
(function(window) {
  'use strict';

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: "<a href=\"index.html\">All models</a><h3>Magnetic circuit flux</h3><p>MMF N\u00d7I [A-turn]. Idealized and intended only to explore equation sensitivity.</p><div class=\"lab\"><label>Turns N <strong id=\"va\"></strong><input id=\"a\" type=\"range\" min=\"100\" max=\"1000\" step=\"any\" value=\"300\"></label><label>Current A <strong id=\"vb\"></strong><input id=\"b\" type=\"range\" min=\"0.1\" max=\"5\" step=\"any\" value=\"0.8\"></label><p>Flux [mWb]: <strong id=\"out\"></strong></p><canvas aria-label=\"Plot of model output versus first parameter\" width=\"900\" height=\"260\"></canvas></div><p><small>Horizontal sweep: first parameter; second parameter held at slider value. Results exclude saturation, temperature variation, leakage and other nonidealities unless modeled explicitly.</small></p>",
    init: function(card) {
      try {
const a=card.querySelector('#a'),b=card.querySelector('#b'),out=card.querySelector('#out'),va=card.querySelector('#va'),vb=card.querySelector('#vb'),c=card.querySelector('canvas'),ctx=c.getContext('2d');function calc(a,b){var R_core=5e5, R_gap=2e6; return (a*b/(R_core+R_gap))*1e3;}function draw(){let x=+a.value,y=+b.value;va.textContent=x.toPrecision(4);vb.textContent=y.toPrecision(4);let value=calc(x,y);out.textContent=Number.isFinite(value)?value.toFixed(4):'undefined';let w=c.width=900,h=c.height=260;ctx.fillStyle='#fff';ctx.fillRect(0,0,w,h);ctx.strokeStyle='#e5e9ee';for(let k=0;k<=4;k++){ctx.beginPath();ctx.moveTo(55,20+k*50);ctx.lineTo(870,20+k*50);ctx.stroke()}let pts=[];for(let k=0;k<=100;k++){let ax=+a.min+(+a.max- +a.min)*k/100;let yy=calc(ax,y);if(Number.isFinite(yy))pts.push([ax,yy])}let vals=pts.map(p=>p[1]),lo=Math.min(...vals),hi=Math.max(...vals);if(hi===lo)hi=lo+1;ctx.strokeStyle='#1967a6';ctx.lineWidth=3;ctx.beginPath();pts.forEach((p,k)=>{let px=55+815*(p[0]- +a.min)/(+a.max- +a.min),py=225-205*(p[1]-lo)/(hi-lo);k?ctx.lineTo(px,py):ctx.moveTo(px,py)});ctx.stroke();ctx.fillStyle='#172438';ctx.font='14px system-ui';ctx.fillText('Sweep of first parameter, second held fixed',65,16);ctx.fillText(hi.toPrecision(4),8,28);ctx.fillText(lo.toPrecision(4),8,226)}a.addEventListener('input',draw);b.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 2,
    html: "<a href=\"index.html\">All models</a><h3>Magnetic coenergy force</h3><p>F=\u00bd I\u00b2 dL/dx. Idealized and intended only to explore equation sensitivity.</p><div class=\"lab\"><label>Current A <strong id=\"va\"></strong><input id=\"a\" type=\"range\" min=\"0\" max=\"10\" step=\"any\" value=\"3\"></label><label>Inductance gradient H/m <strong id=\"vb\"></strong><input id=\"b\" type=\"range\" min=\"0.001\" max=\"0.1\" step=\"any\" value=\"0.02\"></label><p>Force [N]: <strong id=\"out\"></strong></p><canvas aria-label=\"Plot of model output versus first parameter\" width=\"900\" height=\"260\"></canvas></div><p><small>Horizontal sweep: first parameter; second parameter held at slider value. Results exclude saturation, temperature variation, leakage and other nonidealities unless modeled explicitly.</small></p>",
    init: function(card) {
      try {
const a=card.querySelector('#a'),b=card.querySelector('#b'),out=card.querySelector('#out'),va=card.querySelector('#va'),vb=card.querySelector('#vb'),c=card.querySelector('canvas'),ctx=c.getContext('2d');function calc(a,b){return .5*a*a*b;}function draw(){let x=+a.value,y=+b.value;va.textContent=x.toPrecision(4);vb.textContent=y.toPrecision(4);let value=calc(x,y);out.textContent=Number.isFinite(value)?value.toFixed(4):'undefined';let w=c.width=900,h=c.height=260;ctx.fillStyle='#fff';ctx.fillRect(0,0,w,h);ctx.strokeStyle='#e5e9ee';for(let k=0;k<=4;k++){ctx.beginPath();ctx.moveTo(55,20+k*50);ctx.lineTo(870,20+k*50);ctx.stroke()}let pts=[];for(let k=0;k<=100;k++){let ax=+a.min+(+a.max- +a.min)*k/100;let yy=calc(ax,y);if(Number.isFinite(yy))pts.push([ax,yy])}let vals=pts.map(p=>p[1]),lo=Math.min(...vals),hi=Math.max(...vals);if(hi===lo)hi=lo+1;ctx.strokeStyle='#1967a6';ctx.lineWidth=3;ctx.beginPath();pts.forEach((p,k)=>{let px=55+815*(p[0]- +a.min)/(+a.max- +a.min),py=225-205*(p[1]-lo)/(hi-lo);k?ctx.lineTo(px,py):ctx.moveTo(px,py)});ctx.stroke();ctx.fillStyle='#172438';ctx.font='14px system-ui';ctx.fillText('Sweep of first parameter, second held fixed',65,16);ctx.fillText(hi.toPrecision(4),8,28);ctx.fillText(lo.toPrecision(4),8,226)}a.addEventListener('input',draw);b.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 3,
    html: "<a href=\"index.html\">All models</a><h3>Transformer voltage ratio</h3><p>V2=230 \u00d7 N2/N1. Idealized and intended only to explore equation sensitivity.</p><div class=\"lab\"><label>Primary turns <strong id=\"va\"></strong><input id=\"a\" type=\"range\" min=\"100\" max=\"3000\" step=\"any\" value=\"1000\"></label><label>Secondary turns <strong id=\"vb\"></strong><input id=\"b\" type=\"range\" min=\"50\" max=\"3000\" step=\"any\" value=\"250\"></label><p>Secondary ideal voltage [V]: <strong id=\"out\"></strong></p><canvas aria-label=\"Plot of model output versus first parameter\" width=\"900\" height=\"260\"></canvas></div><p><small>Horizontal sweep: first parameter; second parameter held at slider value. Results exclude saturation, temperature variation, leakage and other nonidealities unless modeled explicitly.</small></p>",
    init: function(card) {
      try {
const a=card.querySelector('#a'),b=card.querySelector('#b'),out=card.querySelector('#out'),va=card.querySelector('#va'),vb=card.querySelector('#vb'),c=card.querySelector('canvas'),ctx=c.getContext('2d');function calc(a,b){return 230*b/a;}function draw(){let x=+a.value,y=+b.value;va.textContent=x.toPrecision(4);vb.textContent=y.toPrecision(4);let value=calc(x,y);out.textContent=Number.isFinite(value)?value.toFixed(4):'undefined';let w=c.width=900,h=c.height=260;ctx.fillStyle='#fff';ctx.fillRect(0,0,w,h);ctx.strokeStyle='#e5e9ee';for(let k=0;k<=4;k++){ctx.beginPath();ctx.moveTo(55,20+k*50);ctx.lineTo(870,20+k*50);ctx.stroke()}let pts=[];for(let k=0;k<=100;k++){let ax=+a.min+(+a.max- +a.min)*k/100;let yy=calc(ax,y);if(Number.isFinite(yy))pts.push([ax,yy])}let vals=pts.map(p=>p[1]),lo=Math.min(...vals),hi=Math.max(...vals);if(hi===lo)hi=lo+1;ctx.strokeStyle='#1967a6';ctx.lineWidth=3;ctx.beginPath();pts.forEach((p,k)=>{let px=55+815*(p[0]- +a.min)/(+a.max- +a.min),py=225-205*(p[1]-lo)/(hi-lo);k?ctx.lineTo(px,py):ctx.moveTo(px,py)});ctx.stroke();ctx.fillStyle='#172438';ctx.font='14px system-ui';ctx.fillText('Sweep of first parameter, second held fixed',65,16);ctx.fillText(hi.toPrecision(4),8,28);ctx.fillText(lo.toPrecision(4),8,226)}a.addEventListener('input',draw);b.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 4,
    html: "<a href=\"index.html\">All models</a><h3>Three-phase apparent power</h3><p>S=\u221a3 Vline Iline. Idealized and intended only to explore equation sensitivity.</p><div class=\"lab\"><label>Line voltage V <strong id=\"va\"></strong><input id=\"a\" type=\"range\" min=\"100\" max=\"1000\" step=\"any\" value=\"400\"></label><label>Line current A <strong id=\"vb\"></strong><input id=\"b\" type=\"range\" min=\"1\" max=\"100\" step=\"any\" value=\"10\"></label><p>Apparent power [kVA]: <strong id=\"out\"></strong></p><canvas aria-label=\"Plot of model output versus first parameter\" width=\"900\" height=\"260\"></canvas></div><p><small>Horizontal sweep: first parameter; second parameter held at slider value. Results exclude saturation, temperature variation, leakage and other nonidealities unless modeled explicitly.</small></p>",
    init: function(card) {
      try {
const a=card.querySelector('#a'),b=card.querySelector('#b'),out=card.querySelector('#out'),va=card.querySelector('#va'),vb=card.querySelector('#vb'),c=card.querySelector('canvas'),ctx=c.getContext('2d');function calc(a,b){return Math.sqrt(3)*a*b/1000;}function draw(){let x=+a.value,y=+b.value;va.textContent=x.toPrecision(4);vb.textContent=y.toPrecision(4);let value=calc(x,y);out.textContent=Number.isFinite(value)?value.toFixed(4):'undefined';let w=c.width=900,h=c.height=260;ctx.fillStyle='#fff';ctx.fillRect(0,0,w,h);ctx.strokeStyle='#e5e9ee';for(let k=0;k<=4;k++){ctx.beginPath();ctx.moveTo(55,20+k*50);ctx.lineTo(870,20+k*50);ctx.stroke()}let pts=[];for(let k=0;k<=100;k++){let ax=+a.min+(+a.max- +a.min)*k/100;let yy=calc(ax,y);if(Number.isFinite(yy))pts.push([ax,yy])}let vals=pts.map(p=>p[1]),lo=Math.min(...vals),hi=Math.max(...vals);if(hi===lo)hi=lo+1;ctx.strokeStyle='#1967a6';ctx.lineWidth=3;ctx.beginPath();pts.forEach((p,k)=>{let px=55+815*(p[0]- +a.min)/(+a.max- +a.min),py=225-205*(p[1]-lo)/(hi-lo);k?ctx.lineTo(px,py):ctx.moveTo(px,py)});ctx.stroke();ctx.fillStyle='#172438';ctx.font='14px system-ui';ctx.fillText('Sweep of first parameter, second held fixed',65,16);ctx.fillText(hi.toPrecision(4),8,28);ctx.fillText(lo.toPrecision(4),8,226)}a.addEventListener('input',draw);b.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 5,
    html: "<a href=\"index.html\">All models</a><h3>DC generated voltage</h3><p>E = P\u03a6ZN/(60A), P=4 Z=600 A=4. Idealized and intended only to explore equation sensitivity.</p><div class=\"lab\"><label>Flux per pole Wb <strong id=\"va\"></strong><input id=\"a\" type=\"range\" min=\"0.001\" max=\"0.1\" step=\"any\" value=\"0.02\"></label><label>Speed RPM <strong id=\"vb\"></strong><input id=\"b\" type=\"range\" min=\"100\" max=\"3000\" step=\"any\" value=\"1200\"></label><p>Generated emf [V]: <strong id=\"out\"></strong></p><canvas aria-label=\"Plot of model output versus first parameter\" width=\"900\" height=\"260\"></canvas></div><p><small>Horizontal sweep: first parameter; second parameter held at slider value. Results exclude saturation, temperature variation, leakage and other nonidealities unless modeled explicitly.</small></p>",
    init: function(card) {
      try {
const a=card.querySelector('#a'),b=card.querySelector('#b'),out=card.querySelector('#out'),va=card.querySelector('#va'),vb=card.querySelector('#vb'),c=card.querySelector('canvas'),ctx=c.getContext('2d');function calc(a,b){return 4*a*600*b/(60*4);}function draw(){let x=+a.value,y=+b.value;va.textContent=x.toPrecision(4);vb.textContent=y.toPrecision(4);let value=calc(x,y);out.textContent=Number.isFinite(value)?value.toFixed(4):'undefined';let w=c.width=900,h=c.height=260;ctx.fillStyle='#fff';ctx.fillRect(0,0,w,h);ctx.strokeStyle='#e5e9ee';for(let k=0;k<=4;k++){ctx.beginPath();ctx.moveTo(55,20+k*50);ctx.lineTo(870,20+k*50);ctx.stroke()}let pts=[];for(let k=0;k<=100;k++){let ax=+a.min+(+a.max- +a.min)*k/100;let yy=calc(ax,y);if(Number.isFinite(yy))pts.push([ax,yy])}let vals=pts.map(p=>p[1]),lo=Math.min(...vals),hi=Math.max(...vals);if(hi===lo)hi=lo+1;ctx.strokeStyle='#1967a6';ctx.lineWidth=3;ctx.beginPath();pts.forEach((p,k)=>{let px=55+815*(p[0]- +a.min)/(+a.max- +a.min),py=225-205*(p[1]-lo)/(hi-lo);k?ctx.lineTo(px,py):ctx.moveTo(px,py)});ctx.stroke();ctx.fillStyle='#172438';ctx.font='14px system-ui';ctx.fillText('Sweep of first parameter, second held fixed',65,16);ctx.fillText(hi.toPrecision(4),8,28);ctx.fillText(lo.toPrecision(4),8,226)}a.addEventListener('input',draw);b.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 6,
    html: "<a href=\"index.html\">All models</a><h3>Motor back EMF</h3><p>E=220\u2212Ia Ra. Idealized and intended only to explore equation sensitivity.</p><div class=\"lab\"><label>Armature current A <strong id=\"va\"></strong><input id=\"a\" type=\"range\" min=\"0\" max=\"100\" step=\"any\" value=\"20\"></label><label>Armature resistance \u03a9 <strong id=\"vb\"></strong><input id=\"b\" type=\"range\" min=\"0.1\" max=\"2\" step=\"any\" value=\"0.5\"></label><p>Back EMF [V]: <strong id=\"out\"></strong></p><canvas aria-label=\"Plot of model output versus first parameter\" width=\"900\" height=\"260\"></canvas></div><p><small>Horizontal sweep: first parameter; second parameter held at slider value. Results exclude saturation, temperature variation, leakage and other nonidealities unless modeled explicitly.</small></p>",
    init: function(card) {
      try {
const a=card.querySelector('#a'),b=card.querySelector('#b'),out=card.querySelector('#out'),va=card.querySelector('#va'),vb=card.querySelector('#vb'),c=card.querySelector('canvas'),ctx=c.getContext('2d');function calc(a,b){return 220-a*b;}function draw(){let x=+a.value,y=+b.value;va.textContent=x.toPrecision(4);vb.textContent=y.toPrecision(4);let value=calc(x,y);out.textContent=Number.isFinite(value)?value.toFixed(4):'undefined';let w=c.width=900,h=c.height=260;ctx.fillStyle='#fff';ctx.fillRect(0,0,w,h);ctx.strokeStyle='#e5e9ee';for(let k=0;k<=4;k++){ctx.beginPath();ctx.moveTo(55,20+k*50);ctx.lineTo(870,20+k*50);ctx.stroke()}let pts=[];for(let k=0;k<=100;k++){let ax=+a.min+(+a.max- +a.min)*k/100;let yy=calc(ax,y);if(Number.isFinite(yy))pts.push([ax,yy])}let vals=pts.map(p=>p[1]),lo=Math.min(...vals),hi=Math.max(...vals);if(hi===lo)hi=lo+1;ctx.strokeStyle='#1967a6';ctx.lineWidth=3;ctx.beginPath();pts.forEach((p,k)=>{let px=55+815*(p[0]- +a.min)/(+a.max- +a.min),py=225-205*(p[1]-lo)/(hi-lo);k?ctx.lineTo(px,py):ctx.moveTo(px,py)});ctx.stroke();ctx.fillStyle='#172438';ctx.font='14px system-ui';ctx.fillText('Sweep of first parameter, second held fixed',65,16);ctx.fillText(hi.toPrecision(4),8,28);ctx.fillText(lo.toPrecision(4),8,226)}a.addEventListener('input',draw);b.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 7,
    html: "<a href=\"index.html\">All models</a><h3>DC generator terminal voltage</h3><p>V=250\u2212Ia Ra. Idealized and intended only to explore equation sensitivity.</p><div class=\"lab\"><label>Current A <strong id=\"va\"></strong><input id=\"a\" type=\"range\" min=\"0\" max=\"100\" step=\"any\" value=\"30\"></label><label>Armature resistance \u03a9 <strong id=\"vb\"></strong><input id=\"b\" type=\"range\" min=\"0.05\" max=\"2\" step=\"any\" value=\"0.3\"></label><p>Terminal voltage [V]: <strong id=\"out\"></strong></p><canvas aria-label=\"Plot of model output versus first parameter\" width=\"900\" height=\"260\"></canvas></div><p><small>Horizontal sweep: first parameter; second parameter held at slider value. Results exclude saturation, temperature variation, leakage and other nonidealities unless modeled explicitly.</small></p>",
    init: function(card) {
      try {
const a=card.querySelector('#a'),b=card.querySelector('#b'),out=card.querySelector('#out'),va=card.querySelector('#va'),vb=card.querySelector('#vb'),c=card.querySelector('canvas'),ctx=c.getContext('2d');function calc(a,b){return 250-a*b;}function draw(){let x=+a.value,y=+b.value;va.textContent=x.toPrecision(4);vb.textContent=y.toPrecision(4);let value=calc(x,y);out.textContent=Number.isFinite(value)?value.toFixed(4):'undefined';let w=c.width=900,h=c.height=260;ctx.fillStyle='#fff';ctx.fillRect(0,0,w,h);ctx.strokeStyle='#e5e9ee';for(let k=0;k<=4;k++){ctx.beginPath();ctx.moveTo(55,20+k*50);ctx.lineTo(870,20+k*50);ctx.stroke()}let pts=[];for(let k=0;k<=100;k++){let ax=+a.min+(+a.max- +a.min)*k/100;let yy=calc(ax,y);if(Number.isFinite(yy))pts.push([ax,yy])}let vals=pts.map(p=>p[1]),lo=Math.min(...vals),hi=Math.max(...vals);if(hi===lo)hi=lo+1;ctx.strokeStyle='#1967a6';ctx.lineWidth=3;ctx.beginPath();pts.forEach((p,k)=>{let px=55+815*(p[0]- +a.min)/(+a.max- +a.min),py=225-205*(p[1]-lo)/(hi-lo);k?ctx.lineTo(px,py):ctx.moveTo(px,py)});ctx.stroke();ctx.fillStyle='#172438';ctx.font='14px system-ui';ctx.fillText('Sweep of first parameter, second held fixed',65,16);ctx.fillText(hi.toPrecision(4),8,28);ctx.fillText(lo.toPrecision(4),8,226)}a.addEventListener('input',draw);b.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 8,
    html: "<a href=\"index.html\">All models</a><h3>Thermal rise</h3><p>Steady \u0394T=P_loss Rth. Idealized and intended only to explore equation sensitivity.</p><div class=\"lab\"><label>Loss W <strong id=\"va\"></strong><input id=\"a\" type=\"range\" min=\"0\" max=\"500\" step=\"any\" value=\"100\"></label><label>Thermal resistance K/W <strong id=\"vb\"></strong><input id=\"b\" type=\"range\" min=\"0.05\" max=\"2\" step=\"any\" value=\"0.4\"></label><p>Temperature rise [K]: <strong id=\"out\"></strong></p><canvas aria-label=\"Plot of model output versus first parameter\" width=\"900\" height=\"260\"></canvas></div><p><small>Horizontal sweep: first parameter; second parameter held at slider value. Results exclude saturation, temperature variation, leakage and other nonidealities unless modeled explicitly.</small></p>",
    init: function(card) {
      try {
const a=card.querySelector('#a'),b=card.querySelector('#b'),out=card.querySelector('#out'),va=card.querySelector('#va'),vb=card.querySelector('#vb'),c=card.querySelector('canvas'),ctx=c.getContext('2d');function calc(a,b){return a*b;}function draw(){let x=+a.value,y=+b.value;va.textContent=x.toPrecision(4);vb.textContent=y.toPrecision(4);let value=calc(x,y);out.textContent=Number.isFinite(value)?value.toFixed(4):'undefined';let w=c.width=900,h=c.height=260;ctx.fillStyle='#fff';ctx.fillRect(0,0,w,h);ctx.strokeStyle='#e5e9ee';for(let k=0;k<=4;k++){ctx.beginPath();ctx.moveTo(55,20+k*50);ctx.lineTo(870,20+k*50);ctx.stroke()}let pts=[];for(let k=0;k<=100;k++){let ax=+a.min+(+a.max- +a.min)*k/100;let yy=calc(ax,y);if(Number.isFinite(yy))pts.push([ax,yy])}let vals=pts.map(p=>p[1]),lo=Math.min(...vals),hi=Math.max(...vals);if(hi===lo)hi=lo+1;ctx.strokeStyle='#1967a6';ctx.lineWidth=3;ctx.beginPath();pts.forEach((p,k)=>{let px=55+815*(p[0]- +a.min)/(+a.max- +a.min),py=225-205*(p[1]-lo)/(hi-lo);k?ctx.lineTo(px,py):ctx.moveTo(px,py)});ctx.stroke();ctx.fillStyle='#172438';ctx.font='14px system-ui';ctx.fillText('Sweep of first parameter, second held fixed',65,16);ctx.fillText(hi.toPrecision(4),8,28);ctx.fillText(lo.toPrecision(4),8,226)}a.addEventListener('input',draw);b.addEventListener('input',draw);draw();
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  if (!window.SimulationEngine) window.SimulationEngine = {};
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
      if (bMatch !== undefined && bMatch !== null && bMatch !== '') unitNum = parseInt(bMatch, 10) + 1;
      else {
        var pMatch = window.location.pathname.match(/chapter-(\d+)/);
        if (pMatch) unitNum = parseInt(pMatch[1], 10);
      }
    }
    if (isNaN(unitNum) || unitNum < 1 || unitNum > 8) unitNum = 1;
    var modelsForUnit = MODELS.filter(function(m) { return m.unit === unitNum; });
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.slice(0, 1);
    modelsForUnit.forEach(function(m) {
      var card = document.createElement('section');
      card.className = 'eee-sim-card';
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
        if (document.getElementById('sim-container')) window.SimulationEngine.initSimulation('sim-container');
      });
    } else {
      if (document.getElementById('sim-container')) window.SimulationEngine.initSimulation('sim-container');
    }
  }
})(typeof window === 'undefined' ? globalThis : window);
