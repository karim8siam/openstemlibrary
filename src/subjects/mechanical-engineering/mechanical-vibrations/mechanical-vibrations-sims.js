/* mechanical-vibrations Interactive Simulation Suite */
(function(window) {
  'use strict';

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: "<p> \u00b7 </p><div class=\"panel\"><p class=\"tag\">INTERACTIVE MODEL 01 / 16 \u2014 OFFLINE</p><h3>Natural frequency of a supported mass</h3><p>f_n = (1/2\u03c0)\u221a(k/m); linear single-degree-of-freedom system.</p><label for=\"a\">stiffness k (N/m): <output id=\"aout\"></output></label><input class=\"sl\" type=\"range\" id=\"a\" min=\"100\" max=\"25000\" step=\"0.1\" value=\"5000\"><label for=\"b\">mass m (kg): <output id=\"bout\"></output></label><input class=\"sl\" type=\"range\" id=\"b\" min=\"1\" max=\"100\" step=\"0.01\" value=\"12\"><div class=\"reading\">Illustrative response <div id=\"result\" aria-live=\"polite\"></div></div><svg id=\"plot\" viewBox=\"0 0 810 255\" role=\"img\" aria-label=\"Computed response curve as the first parameter varies\"><rect x=\"26\" y=\"26\" width=\"758\" height=\"203\" fill=\"none\" stroke=\"#a1b4c6\" stroke-width=\"1\"/><polyline id=\"curve\" points=\"\" stroke=\"#127ca4\" stroke-width=\"3\" fill=\"none\"/><circle id=\"dot\" r=\"7\" cx=\"0\" cy=\"0\" fill=\"#d76329\" stroke=\"white\" stroke-width=\"2\"/></svg><small id=\"axes\"></small><p><button id=\"reset\" type=\"button\">Reset inputs</button> <small id=\"status\" aria-live=\"polite\"></small></p><div class=\"warning\">This is a simplified illustrative equation, not a digital twin. No fatigue, equipment acceptance, safe excitation level or measured machine performance is implied. A real installation needs independently measured parameters and qualified review.</div></div>",
    init: function(card) {
      try {
const aEl=card.querySelector("#" + 'a'.replace(/^#/, "")),bEl=card.querySelector("#" + 'b'.replace(/^#/, "")),r=card.querySelector("#" + 'result'.replace(/^#/, "")),curve=card.querySelector("#" + 'curve'.replace(/^#/, "")),dot=card.querySelector("#" + 'dot'.replace(/^#/, "")),axes=card.querySelector("#" + 'axes'.replace(/^#/, "")),status=card.querySelector("#" + 'status'.replace(/^#/, ""));
function calc(a,b){return Math.sqrt(a/b)/(2*Math.PI);}
function fmt(v){if(!Number.isFinite(v))return 'undefined';if(Math.abs(v)>=1000)return v.toFixed(1);if(Math.abs(v)>=1)return v.toFixed(3);return v.toPrecision(4)}
function render(){const a=+aEl.value,b=+bEl.value;card.querySelector("#" + 'aout'.replace(/^#/, "")).textContent=fmt(a);card.querySelector("#" + 'bout'.replace(/^#/, "")).textContent=fmt(b);const value=calc(a,b);r.textContent=fmt(value)+' Hz';const amin=+aEl.min,amax=+aEl.max,W=810,H=255,pad=26;const samples=[];for(let i=0;i<140;i++){const x=amin+(amax-amin)*i/139,y=calc(x,b);if(Number.isFinite(y))samples.push({x,y});}const ymin=Math.min(...samples.map(p=>p.y)),ymax=Math.max(...samples.map(p=>p.y)),range=Math.max(1e-10,ymax-ymin),xx=x=>pad+(W-2*pad)*(x-amin)/(amax-amin),yy=y=>H-pad-(H-2*pad)*(y-ymin)/range;curve.setAttribute('points',samples.map(p=>xx(p.x).toFixed(1)+','+yy(p.y).toFixed(1)).join(' '));dot.setAttribute('cx',xx(a));dot.setAttribute('cy',yy(value));axes.textContent='Horizontal: '+aEl.previousElementSibling.textContent.split(':')[0]+' | vertical response: '+fmt(ymin)+' – '+fmt(ymax);status.textContent=Number.isFinite(value)?'Interactive calculation updated.':'Chosen parameters outside model bounds';}
aEl.addEventListener('input',render);bEl.addEventListener('input',render);card.querySelector("#" + 'reset'.replace(/^#/, "")).addEventListener('click',()=>{aEl.value='5000';bEl.value='12';render()});render();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 1,
    html: "<p> \u00b7 </p><div class=\"panel\"><p class=\"tag\">INTERACTIVE MODEL 02 / 16 \u2014 OFFLINE</p><h3>Maximum elastic energy</h3><p>E = kX\u00b2/2, for a linear spring in free vibration; amplitude converted to metres.</p><label for=\"a\">stiffness k (N/m): <output id=\"aout\"></output></label><input class=\"sl\" type=\"range\" id=\"a\" min=\"100\" max=\"20000\" step=\"0.1\" value=\"1600\"><label for=\"b\">motion amplitude X (mm): <output id=\"bout\"></output></label><input class=\"sl\" type=\"range\" id=\"b\" min=\"1\" max=\"30\" step=\"0.01\" value=\"12\"><div class=\"reading\">Illustrative response <div id=\"result\" aria-live=\"polite\"></div></div><svg id=\"plot\" viewBox=\"0 0 810 255\" role=\"img\" aria-label=\"Computed response curve as the first parameter varies\"><rect x=\"26\" y=\"26\" width=\"758\" height=\"203\" fill=\"none\" stroke=\"#a1b4c6\" stroke-width=\"1\"/><polyline id=\"curve\" points=\"\" stroke=\"#127ca4\" stroke-width=\"3\" fill=\"none\"/><circle id=\"dot\" r=\"7\" cx=\"0\" cy=\"0\" fill=\"#d76329\" stroke=\"white\" stroke-width=\"2\"/></svg><small id=\"axes\"></small><p><button id=\"reset\" type=\"button\">Reset inputs</button> <small id=\"status\" aria-live=\"polite\"></small></p><div class=\"warning\">This is a simplified illustrative equation, not a digital twin. No fatigue, equipment acceptance, safe excitation level or measured machine performance is implied. A real installation needs independently measured parameters and qualified review.</div></div>",
    init: function(card) {
      try {
const aEl=card.querySelector("#" + 'a'.replace(/^#/, "")),bEl=card.querySelector("#" + 'b'.replace(/^#/, "")),r=card.querySelector("#" + 'result'.replace(/^#/, "")),curve=card.querySelector("#" + 'curve'.replace(/^#/, "")),dot=card.querySelector("#" + 'dot'.replace(/^#/, "")),axes=card.querySelector("#" + 'axes'.replace(/^#/, "")),status=card.querySelector("#" + 'status'.replace(/^#/, ""));
function calc(a,b){return 0.5*a*(b/1000)**2;}
function fmt(v){if(!Number.isFinite(v))return 'undefined';if(Math.abs(v)>=1000)return v.toFixed(1);if(Math.abs(v)>=1)return v.toFixed(3);return v.toPrecision(4)}
function render(){const a=+aEl.value,b=+bEl.value;card.querySelector("#" + 'aout'.replace(/^#/, "")).textContent=fmt(a);card.querySelector("#" + 'bout'.replace(/^#/, "")).textContent=fmt(b);const value=calc(a,b);r.textContent=fmt(value)+' J';const amin=+aEl.min,amax=+aEl.max,W=810,H=255,pad=26;const samples=[];for(let i=0;i<140;i++){const x=amin+(amax-amin)*i/139,y=calc(x,b);if(Number.isFinite(y))samples.push({x,y});}const ymin=Math.min(...samples.map(p=>p.y)),ymax=Math.max(...samples.map(p=>p.y)),range=Math.max(1e-10,ymax-ymin),xx=x=>pad+(W-2*pad)*(x-amin)/(amax-amin),yy=y=>H-pad-(H-2*pad)*(y-ymin)/range;curve.setAttribute('points',samples.map(p=>xx(p.x).toFixed(1)+','+yy(p.y).toFixed(1)).join(' '));dot.setAttribute('cx',xx(a));dot.setAttribute('cy',yy(value));axes.textContent='Horizontal: '+aEl.previousElementSibling.textContent.split(':')[0]+' | vertical response: '+fmt(ymin)+' – '+fmt(ymax);status.textContent=Number.isFinite(value)?'Interactive calculation updated.':'Chosen parameters outside model bounds';}
aEl.addEventListener('input',render);bEl.addEventListener('input',render);card.querySelector("#" + 'reset'.replace(/^#/, "")).addEventListener('click',()=>{aEl.value='1600';bEl.value='12';render()});render();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 2,
    html: "<p> \u00b7 </p><div class=\"panel\"><p class=\"tag\">INTERACTIVE MODEL 03 / 16 \u2014 OFFLINE</p><h3>Viscous damping ratio</h3><p>\u03b6 = c/(2\u221a(km)) with mass fixed at 10 kg.</p><label for=\"a\">damping c (N\u00b7s/m): <output id=\"aout\"></output></label><input class=\"sl\" type=\"range\" id=\"a\" min=\"1\" max=\"400\" step=\"0.1\" value=\"80\"><label for=\"b\">stiffness k (N/m): <output id=\"bout\"></output></label><input class=\"sl\" type=\"range\" id=\"b\" min=\"100\" max=\"15000\" step=\"0.1\" value=\"4000\"><div class=\"reading\">Illustrative response <div id=\"result\" aria-live=\"polite\"></div></div><svg id=\"plot\" viewBox=\"0 0 810 255\" role=\"img\" aria-label=\"Computed response curve as the first parameter varies\"><rect x=\"26\" y=\"26\" width=\"758\" height=\"203\" fill=\"none\" stroke=\"#a1b4c6\" stroke-width=\"1\"/><polyline id=\"curve\" points=\"\" stroke=\"#127ca4\" stroke-width=\"3\" fill=\"none\"/><circle id=\"dot\" r=\"7\" cx=\"0\" cy=\"0\" fill=\"#d76329\" stroke=\"white\" stroke-width=\"2\"/></svg><small id=\"axes\"></small><p><button id=\"reset\" type=\"button\">Reset inputs</button> <small id=\"status\" aria-live=\"polite\"></small></p><div class=\"warning\">This is a simplified illustrative equation, not a digital twin. No fatigue, equipment acceptance, safe excitation level or measured machine performance is implied. A real installation needs independently measured parameters and qualified review.</div></div>",
    init: function(card) {
      try {
const aEl=card.querySelector("#" + 'a'.replace(/^#/, "")),bEl=card.querySelector("#" + 'b'.replace(/^#/, "")),r=card.querySelector("#" + 'result'.replace(/^#/, "")),curve=card.querySelector("#" + 'curve'.replace(/^#/, "")),dot=card.querySelector("#" + 'dot'.replace(/^#/, "")),axes=card.querySelector("#" + 'axes'.replace(/^#/, "")),status=card.querySelector("#" + 'status'.replace(/^#/, ""));
function calc(a,b){return a/(2*Math.sqrt(10*b));}
function fmt(v){if(!Number.isFinite(v))return 'undefined';if(Math.abs(v)>=1000)return v.toFixed(1);if(Math.abs(v)>=1)return v.toFixed(3);return v.toPrecision(4)}
function render(){const a=+aEl.value,b=+bEl.value;card.querySelector("#" + 'aout'.replace(/^#/, "")).textContent=fmt(a);card.querySelector("#" + 'bout'.replace(/^#/, "")).textContent=fmt(b);const value=calc(a,b);r.textContent=fmt(value)+' dimensionless';const amin=+aEl.min,amax=+aEl.max,W=810,H=255,pad=26;const samples=[];for(let i=0;i<140;i++){const x=amin+(amax-amin)*i/139,y=calc(x,b);if(Number.isFinite(y))samples.push({x,y});}const ymin=Math.min(...samples.map(p=>p.y)),ymax=Math.max(...samples.map(p=>p.y)),range=Math.max(1e-10,ymax-ymin),xx=x=>pad+(W-2*pad)*(x-amin)/(amax-amin),yy=y=>H-pad-(H-2*pad)*(y-ymin)/range;curve.setAttribute('points',samples.map(p=>xx(p.x).toFixed(1)+','+yy(p.y).toFixed(1)).join(' '));dot.setAttribute('cx',xx(a));dot.setAttribute('cy',yy(value));axes.textContent='Horizontal: '+aEl.previousElementSibling.textContent.split(':')[0]+' | vertical response: '+fmt(ymin)+' – '+fmt(ymax);status.textContent=Number.isFinite(value)?'Interactive calculation updated.':'Chosen parameters outside model bounds';}
aEl.addEventListener('input',render);bEl.addEventListener('input',render);card.querySelector("#" + 'reset'.replace(/^#/, "")).addEventListener('click',()=>{aEl.value='80';bEl.value='4000';render()});render();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 2,
    html: "<p> \u00b7 </p><div class=\"panel\"><p class=\"tag\">INTERACTIVE MODEL 04 / 16 \u2014 OFFLINE</p><h3>Underdamped natural frequency</h3><p>f_d = f_n\u221a(1\u2212\u03b6\u00b2); valid only for \u03b6 less than 1.</p><label for=\"a\">undamped f_n (Hz): <output id=\"aout\"></output></label><input class=\"sl\" type=\"range\" id=\"a\" min=\"1\" max=\"80\" step=\"0.01\" value=\"8\"><label for=\"b\">damping ratio \u03b6: <output id=\"bout\"></output></label><input class=\"sl\" type=\"range\" id=\"b\" min=\"0.01\" max=\"0.95\" step=\"0.001\" value=\"0.05\"><div class=\"reading\">Illustrative response <div id=\"result\" aria-live=\"polite\"></div></div><svg id=\"plot\" viewBox=\"0 0 810 255\" role=\"img\" aria-label=\"Computed response curve as the first parameter varies\"><rect x=\"26\" y=\"26\" width=\"758\" height=\"203\" fill=\"none\" stroke=\"#a1b4c6\" stroke-width=\"1\"/><polyline id=\"curve\" points=\"\" stroke=\"#127ca4\" stroke-width=\"3\" fill=\"none\"/><circle id=\"dot\" r=\"7\" cx=\"0\" cy=\"0\" fill=\"#d76329\" stroke=\"white\" stroke-width=\"2\"/></svg><small id=\"axes\"></small><p><button id=\"reset\" type=\"button\">Reset inputs</button> <small id=\"status\" aria-live=\"polite\"></small></p><div class=\"warning\">This is a simplified illustrative equation, not a digital twin. No fatigue, equipment acceptance, safe excitation level or measured machine performance is implied. A real installation needs independently measured parameters and qualified review.</div></div>",
    init: function(card) {
      try {
const aEl=card.querySelector("#" + 'a'.replace(/^#/, "")),bEl=card.querySelector("#" + 'b'.replace(/^#/, "")),r=card.querySelector("#" + 'result'.replace(/^#/, "")),curve=card.querySelector("#" + 'curve'.replace(/^#/, "")),dot=card.querySelector("#" + 'dot'.replace(/^#/, "")),axes=card.querySelector("#" + 'axes'.replace(/^#/, "")),status=card.querySelector("#" + 'status'.replace(/^#/, ""));
function calc(a,b){return a*Math.sqrt(1-b*b);}
function fmt(v){if(!Number.isFinite(v))return 'undefined';if(Math.abs(v)>=1000)return v.toFixed(1);if(Math.abs(v)>=1)return v.toFixed(3);return v.toPrecision(4)}
function render(){const a=+aEl.value,b=+bEl.value;card.querySelector("#" + 'aout'.replace(/^#/, "")).textContent=fmt(a);card.querySelector("#" + 'bout'.replace(/^#/, "")).textContent=fmt(b);const value=calc(a,b);r.textContent=fmt(value)+' Hz';const amin=+aEl.min,amax=+aEl.max,W=810,H=255,pad=26;const samples=[];for(let i=0;i<140;i++){const x=amin+(amax-amin)*i/139,y=calc(x,b);if(Number.isFinite(y))samples.push({x,y});}const ymin=Math.min(...samples.map(p=>p.y)),ymax=Math.max(...samples.map(p=>p.y)),range=Math.max(1e-10,ymax-ymin),xx=x=>pad+(W-2*pad)*(x-amin)/(amax-amin),yy=y=>H-pad-(H-2*pad)*(y-ymin)/range;curve.setAttribute('points',samples.map(p=>xx(p.x).toFixed(1)+','+yy(p.y).toFixed(1)).join(' '));dot.setAttribute('cx',xx(a));dot.setAttribute('cy',yy(value));axes.textContent='Horizontal: '+aEl.previousElementSibling.textContent.split(':')[0]+' | vertical response: '+fmt(ymin)+' – '+fmt(ymax);status.textContent=Number.isFinite(value)?'Interactive calculation updated.':'Chosen parameters outside model bounds';}
aEl.addEventListener('input',render);bEl.addEventListener('input',render);card.querySelector("#" + 'reset'.replace(/^#/, "")).addEventListener('click',()=>{aEl.value='8';bEl.value='0.05';render()});render();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 3,
    html: "<p> \u00b7 </p><div class=\"panel\"><p class=\"tag\">INTERACTIVE MODEL 05 / 16 \u2014 OFFLINE</p><h3>Forced displacement amplitude</h3><p>X = (F0/k) /\u221a((1\u2212r\u00b2)\u00b2+(2\u03b6r)\u00b2); F0/k fixed at 4 mm.</p><label for=\"a\">frequency ratio r: <output id=\"aout\"></output></label><input class=\"sl\" type=\"range\" id=\"a\" min=\"0.05\" max=\"4\" step=\"0.01\" value=\"1\"><label for=\"b\">damping ratio \u03b6: <output id=\"bout\"></output></label><input class=\"sl\" type=\"range\" id=\"b\" min=\"0.02\" max=\"0.6\" step=\"0.001\" value=\"0.1\"><div class=\"reading\">Illustrative response <div id=\"result\" aria-live=\"polite\"></div></div><svg id=\"plot\" viewBox=\"0 0 810 255\" role=\"img\" aria-label=\"Computed response curve as the first parameter varies\"><rect x=\"26\" y=\"26\" width=\"758\" height=\"203\" fill=\"none\" stroke=\"#a1b4c6\" stroke-width=\"1\"/><polyline id=\"curve\" points=\"\" stroke=\"#127ca4\" stroke-width=\"3\" fill=\"none\"/><circle id=\"dot\" r=\"7\" cx=\"0\" cy=\"0\" fill=\"#d76329\" stroke=\"white\" stroke-width=\"2\"/></svg><small id=\"axes\"></small><p><button id=\"reset\" type=\"button\">Reset inputs</button> <small id=\"status\" aria-live=\"polite\"></small></p><div class=\"warning\">This is a simplified illustrative equation, not a digital twin. No fatigue, equipment acceptance, safe excitation level or measured machine performance is implied. A real installation needs independently measured parameters and qualified review.</div></div>",
    init: function(card) {
      try {
const aEl=card.querySelector("#" + 'a'.replace(/^#/, "")),bEl=card.querySelector("#" + 'b'.replace(/^#/, "")),r=card.querySelector("#" + 'result'.replace(/^#/, "")),curve=card.querySelector("#" + 'curve'.replace(/^#/, "")),dot=card.querySelector("#" + 'dot'.replace(/^#/, "")),axes=card.querySelector("#" + 'axes'.replace(/^#/, "")),status=card.querySelector("#" + 'status'.replace(/^#/, ""));
function calc(a,b){return 4/Math.sqrt((1-a*a)**2+(2*b*a)**2);}
function fmt(v){if(!Number.isFinite(v))return 'undefined';if(Math.abs(v)>=1000)return v.toFixed(1);if(Math.abs(v)>=1)return v.toFixed(3);return v.toPrecision(4)}
function render(){const a=+aEl.value,b=+bEl.value;card.querySelector("#" + 'aout'.replace(/^#/, "")).textContent=fmt(a);card.querySelector("#" + 'bout'.replace(/^#/, "")).textContent=fmt(b);const value=calc(a,b);r.textContent=fmt(value)+' mm';const amin=+aEl.min,amax=+aEl.max,W=810,H=255,pad=26;const samples=[];for(let i=0;i<140;i++){const x=amin+(amax-amin)*i/139,y=calc(x,b);if(Number.isFinite(y))samples.push({x,y});}const ymin=Math.min(...samples.map(p=>p.y)),ymax=Math.max(...samples.map(p=>p.y)),range=Math.max(1e-10,ymax-ymin),xx=x=>pad+(W-2*pad)*(x-amin)/(amax-amin),yy=y=>H-pad-(H-2*pad)*(y-ymin)/range;curve.setAttribute('points',samples.map(p=>xx(p.x).toFixed(1)+','+yy(p.y).toFixed(1)).join(' '));dot.setAttribute('cx',xx(a));dot.setAttribute('cy',yy(value));axes.textContent='Horizontal: '+aEl.previousElementSibling.textContent.split(':')[0]+' | vertical response: '+fmt(ymin)+' – '+fmt(ymax);status.textContent=Number.isFinite(value)?'Interactive calculation updated.':'Chosen parameters outside model bounds';}
aEl.addEventListener('input',render);bEl.addEventListener('input',render);card.querySelector("#" + 'reset'.replace(/^#/, "")).addEventListener('click',()=>{aEl.value='1';bEl.value='0.1';render()});render();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 3,
    html: "<p> \u00b7 </p><div class=\"panel\"><p class=\"tag\">INTERACTIVE MODEL 06 / 16 \u2014 OFFLINE</p><h3>Excitation phase lag</h3><p>\u03c6 = atan2(2\u03b6r,1\u2212r\u00b2); force-to-displacement phase lag, 0\u2013180 degrees.</p><label for=\"a\">frequency ratio r: <output id=\"aout\"></output></label><input class=\"sl\" type=\"range\" id=\"a\" min=\"0.05\" max=\"4\" step=\"0.01\" value=\"1\"><label for=\"b\">damping ratio \u03b6: <output id=\"bout\"></output></label><input class=\"sl\" type=\"range\" id=\"b\" min=\"0.02\" max=\"0.6\" step=\"0.001\" value=\"0.08\"><div class=\"reading\">Illustrative response <div id=\"result\" aria-live=\"polite\"></div></div><svg id=\"plot\" viewBox=\"0 0 810 255\" role=\"img\" aria-label=\"Computed response curve as the first parameter varies\"><rect x=\"26\" y=\"26\" width=\"758\" height=\"203\" fill=\"none\" stroke=\"#a1b4c6\" stroke-width=\"1\"/><polyline id=\"curve\" points=\"\" stroke=\"#127ca4\" stroke-width=\"3\" fill=\"none\"/><circle id=\"dot\" r=\"7\" cx=\"0\" cy=\"0\" fill=\"#d76329\" stroke=\"white\" stroke-width=\"2\"/></svg><small id=\"axes\"></small><p><button id=\"reset\" type=\"button\">Reset inputs</button> <small id=\"status\" aria-live=\"polite\"></small></p><div class=\"warning\">This is a simplified illustrative equation, not a digital twin. No fatigue, equipment acceptance, safe excitation level or measured machine performance is implied. A real installation needs independently measured parameters and qualified review.</div></div>",
    init: function(card) {
      try {
const aEl=card.querySelector("#" + 'a'.replace(/^#/, "")),bEl=card.querySelector("#" + 'b'.replace(/^#/, "")),r=card.querySelector("#" + 'result'.replace(/^#/, "")),curve=card.querySelector("#" + 'curve'.replace(/^#/, "")),dot=card.querySelector("#" + 'dot'.replace(/^#/, "")),axes=card.querySelector("#" + 'axes'.replace(/^#/, "")),status=card.querySelector("#" + 'status'.replace(/^#/, ""));
function calc(a,b){return Math.atan2(2*b*a,1-a*a)*180/Math.PI;}
function fmt(v){if(!Number.isFinite(v))return 'undefined';if(Math.abs(v)>=1000)return v.toFixed(1);if(Math.abs(v)>=1)return v.toFixed(3);return v.toPrecision(4)}
function render(){const a=+aEl.value,b=+bEl.value;card.querySelector("#" + 'aout'.replace(/^#/, "")).textContent=fmt(a);card.querySelector("#" + 'bout'.replace(/^#/, "")).textContent=fmt(b);const value=calc(a,b);r.textContent=fmt(value)+' deg';const amin=+aEl.min,amax=+aEl.max,W=810,H=255,pad=26;const samples=[];for(let i=0;i<140;i++){const x=amin+(amax-amin)*i/139,y=calc(x,b);if(Number.isFinite(y))samples.push({x,y});}const ymin=Math.min(...samples.map(p=>p.y)),ymax=Math.max(...samples.map(p=>p.y)),range=Math.max(1e-10,ymax-ymin),xx=x=>pad+(W-2*pad)*(x-amin)/(amax-amin),yy=y=>H-pad-(H-2*pad)*(y-ymin)/range;curve.setAttribute('points',samples.map(p=>xx(p.x).toFixed(1)+','+yy(p.y).toFixed(1)).join(' '));dot.setAttribute('cx',xx(a));dot.setAttribute('cy',yy(value));axes.textContent='Horizontal: '+aEl.previousElementSibling.textContent.split(':')[0]+' | vertical response: '+fmt(ymin)+' – '+fmt(ymax);status.textContent=Number.isFinite(value)?'Interactive calculation updated.':'Chosen parameters outside model bounds';}
aEl.addEventListener('input',render);bEl.addEventListener('input',render);card.querySelector("#" + 'reset'.replace(/^#/, "")).addEventListener('click',()=>{aEl.value='1';bEl.value='0.08';render()});render();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 4,
    html: "<p> \u00b7 </p><div class=\"panel\"><p class=\"tag\">INTERACTIVE MODEL 07 / 16 \u2014 OFFLINE</p><h3>Absolute base displacement ratio</h3><p>T_x = |X/Y| for a linear SDOF system with harmonic imposed base displacement.</p><label for=\"a\">base-motion frequency ratio r: <output id=\"aout\"></output></label><input class=\"sl\" type=\"range\" id=\"a\" min=\"0.05\" max=\"5\" step=\"0.01\" value=\"2\"><label for=\"b\">damping ratio \u03b6: <output id=\"bout\"></output></label><input class=\"sl\" type=\"range\" id=\"b\" min=\"0.02\" max=\"0.7\" step=\"0.001\" value=\"0.1\"><div class=\"reading\">Illustrative response <div id=\"result\" aria-live=\"polite\"></div></div><svg id=\"plot\" viewBox=\"0 0 810 255\" role=\"img\" aria-label=\"Computed response curve as the first parameter varies\"><rect x=\"26\" y=\"26\" width=\"758\" height=\"203\" fill=\"none\" stroke=\"#a1b4c6\" stroke-width=\"1\"/><polyline id=\"curve\" points=\"\" stroke=\"#127ca4\" stroke-width=\"3\" fill=\"none\"/><circle id=\"dot\" r=\"7\" cx=\"0\" cy=\"0\" fill=\"#d76329\" stroke=\"white\" stroke-width=\"2\"/></svg><small id=\"axes\"></small><p><button id=\"reset\" type=\"button\">Reset inputs</button> <small id=\"status\" aria-live=\"polite\"></small></p><div class=\"warning\">This is a simplified illustrative equation, not a digital twin. No fatigue, equipment acceptance, safe excitation level or measured machine performance is implied. A real installation needs independently measured parameters and qualified review.</div></div>",
    init: function(card) {
      try {
const aEl=card.querySelector("#" + 'a'.replace(/^#/, "")),bEl=card.querySelector("#" + 'b'.replace(/^#/, "")),r=card.querySelector("#" + 'result'.replace(/^#/, "")),curve=card.querySelector("#" + 'curve'.replace(/^#/, "")),dot=card.querySelector("#" + 'dot'.replace(/^#/, "")),axes=card.querySelector("#" + 'axes'.replace(/^#/, "")),status=card.querySelector("#" + 'status'.replace(/^#/, ""));
function calc(a,b){return Math.sqrt(1+(2*b*a)**2)/Math.sqrt((1-a*a)**2+(2*b*a)**2);}
function fmt(v){if(!Number.isFinite(v))return 'undefined';if(Math.abs(v)>=1000)return v.toFixed(1);if(Math.abs(v)>=1)return v.toFixed(3);return v.toPrecision(4)}
function render(){const a=+aEl.value,b=+bEl.value;card.querySelector("#" + 'aout'.replace(/^#/, "")).textContent=fmt(a);card.querySelector("#" + 'bout'.replace(/^#/, "")).textContent=fmt(b);const value=calc(a,b);r.textContent=fmt(value)+' dimensionless';const amin=+aEl.min,amax=+aEl.max,W=810,H=255,pad=26;const samples=[];for(let i=0;i<140;i++){const x=amin+(amax-amin)*i/139,y=calc(x,b);if(Number.isFinite(y))samples.push({x,y});}const ymin=Math.min(...samples.map(p=>p.y)),ymax=Math.max(...samples.map(p=>p.y)),range=Math.max(1e-10,ymax-ymin),xx=x=>pad+(W-2*pad)*(x-amin)/(amax-amin),yy=y=>H-pad-(H-2*pad)*(y-ymin)/range;curve.setAttribute('points',samples.map(p=>xx(p.x).toFixed(1)+','+yy(p.y).toFixed(1)).join(' '));dot.setAttribute('cx',xx(a));dot.setAttribute('cy',yy(value));axes.textContent='Horizontal: '+aEl.previousElementSibling.textContent.split(':')[0]+' | vertical response: '+fmt(ymin)+' – '+fmt(ymax);status.textContent=Number.isFinite(value)?'Interactive calculation updated.':'Chosen parameters outside model bounds';}
aEl.addEventListener('input',render);bEl.addEventListener('input',render);card.querySelector("#" + 'reset'.replace(/^#/, "")).addEventListener('click',()=>{aEl.value='2';bEl.value='0.1';render()});render();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 4,
    html: "<p> \u00b7 </p><div class=\"panel\"><p class=\"tag\">INTERACTIVE MODEL 08 / 16 \u2014 OFFLINE</p><h3>Relative stroke from base motion</h3><p>Relative stroke |X\u2212Y| = Y0 r\u00b2/\u221a((1\u2212r\u00b2)\u00b2+(2\u03b6r)\u00b2), Y0=2 mm.</p><label for=\"a\">base-motion frequency ratio r: <output id=\"aout\"></output></label><input class=\"sl\" type=\"range\" id=\"a\" min=\"0.05\" max=\"5\" step=\"0.01\" value=\"2\"><label for=\"b\">damping ratio \u03b6: <output id=\"bout\"></output></label><input class=\"sl\" type=\"range\" id=\"b\" min=\"0.02\" max=\"0.7\" step=\"0.001\" value=\"0.1\"><div class=\"reading\">Illustrative response <div id=\"result\" aria-live=\"polite\"></div></div><svg id=\"plot\" viewBox=\"0 0 810 255\" role=\"img\" aria-label=\"Computed response curve as the first parameter varies\"><rect x=\"26\" y=\"26\" width=\"758\" height=\"203\" fill=\"none\" stroke=\"#a1b4c6\" stroke-width=\"1\"/><polyline id=\"curve\" points=\"\" stroke=\"#127ca4\" stroke-width=\"3\" fill=\"none\"/><circle id=\"dot\" r=\"7\" cx=\"0\" cy=\"0\" fill=\"#d76329\" stroke=\"white\" stroke-width=\"2\"/></svg><small id=\"axes\"></small><p><button id=\"reset\" type=\"button\">Reset inputs</button> <small id=\"status\" aria-live=\"polite\"></small></p><div class=\"warning\">This is a simplified illustrative equation, not a digital twin. No fatigue, equipment acceptance, safe excitation level or measured machine performance is implied. A real installation needs independently measured parameters and qualified review.</div></div>",
    init: function(card) {
      try {
const aEl=card.querySelector("#" + 'a'.replace(/^#/, "")),bEl=card.querySelector("#" + 'b'.replace(/^#/, "")),r=card.querySelector("#" + 'result'.replace(/^#/, "")),curve=card.querySelector("#" + 'curve'.replace(/^#/, "")),dot=card.querySelector("#" + 'dot'.replace(/^#/, "")),axes=card.querySelector("#" + 'axes'.replace(/^#/, "")),status=card.querySelector("#" + 'status'.replace(/^#/, ""));
function calc(a,b){return 2*a*a/Math.sqrt((1-a*a)**2+(2*b*a)**2);}
function fmt(v){if(!Number.isFinite(v))return 'undefined';if(Math.abs(v)>=1000)return v.toFixed(1);if(Math.abs(v)>=1)return v.toFixed(3);return v.toPrecision(4)}
function render(){const a=+aEl.value,b=+bEl.value;card.querySelector("#" + 'aout'.replace(/^#/, "")).textContent=fmt(a);card.querySelector("#" + 'bout'.replace(/^#/, "")).textContent=fmt(b);const value=calc(a,b);r.textContent=fmt(value)+' mm';const amin=+aEl.min,amax=+aEl.max,W=810,H=255,pad=26;const samples=[];for(let i=0;i<140;i++){const x=amin+(amax-amin)*i/139,y=calc(x,b);if(Number.isFinite(y))samples.push({x,y});}const ymin=Math.min(...samples.map(p=>p.y)),ymax=Math.max(...samples.map(p=>p.y)),range=Math.max(1e-10,ymax-ymin),xx=x=>pad+(W-2*pad)*(x-amin)/(amax-amin),yy=y=>H-pad-(H-2*pad)*(y-ymin)/range;curve.setAttribute('points',samples.map(p=>xx(p.x).toFixed(1)+','+yy(p.y).toFixed(1)).join(' '));dot.setAttribute('cx',xx(a));dot.setAttribute('cy',yy(value));axes.textContent='Horizontal: '+aEl.previousElementSibling.textContent.split(':')[0]+' | vertical response: '+fmt(ymin)+' – '+fmt(ymax);status.textContent=Number.isFinite(value)?'Interactive calculation updated.':'Chosen parameters outside model bounds';}
aEl.addEventListener('input',render);bEl.addEventListener('input',render);card.querySelector("#" + 'reset'.replace(/^#/, "")).addEventListener('click',()=>{aEl.value='2';bEl.value='0.1';render()});render();
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  MODELS.push({
    idx: 9,
    unit: 5,
    html: "<p> \u00b7 </p><div class=\"panel\"><p class=\"tag\">INTERACTIVE MODEL 09 / 16 \u2014 OFFLINE</p><h3>Lower mode frequency, 2 DOF</h3><p>For M=m I and K=k[[2,\u22121],[\u22121,1]], lower eigenvalue=(3\u2212\u221a5)k/(2m).</p><label for=\"a\">spring stiffness k (N/m): <output id=\"aout\"></output></label><input class=\"sl\" type=\"range\" id=\"a\" min=\"100\" max=\"10000\" step=\"0.1\" value=\"1000\"><label for=\"b\">each mass m (kg): <output id=\"bout\"></output></label><input class=\"sl\" type=\"range\" id=\"b\" min=\"0.5\" max=\"20\" step=\"0.01\" value=\"2\"><div class=\"reading\">Illustrative response <div id=\"result\" aria-live=\"polite\"></div></div><svg id=\"plot\" viewBox=\"0 0 810 255\" role=\"img\" aria-label=\"Computed response curve as the first parameter varies\"><rect x=\"26\" y=\"26\" width=\"758\" height=\"203\" fill=\"none\" stroke=\"#a1b4c6\" stroke-width=\"1\"/><polyline id=\"curve\" points=\"\" stroke=\"#127ca4\" stroke-width=\"3\" fill=\"none\"/><circle id=\"dot\" r=\"7\" cx=\"0\" cy=\"0\" fill=\"#d76329\" stroke=\"white\" stroke-width=\"2\"/></svg><small id=\"axes\"></small><p><button id=\"reset\" type=\"button\">Reset inputs</button> <small id=\"status\" aria-live=\"polite\"></small></p><div class=\"warning\">This is a simplified illustrative equation, not a digital twin. No fatigue, equipment acceptance, safe excitation level or measured machine performance is implied. A real installation needs independently measured parameters and qualified review.</div></div>",
    init: function(card) {
      try {
const aEl=card.querySelector("#" + 'a'.replace(/^#/, "")),bEl=card.querySelector("#" + 'b'.replace(/^#/, "")),r=card.querySelector("#" + 'result'.replace(/^#/, "")),curve=card.querySelector("#" + 'curve'.replace(/^#/, "")),dot=card.querySelector("#" + 'dot'.replace(/^#/, "")),axes=card.querySelector("#" + 'axes'.replace(/^#/, "")),status=card.querySelector("#" + 'status'.replace(/^#/, ""));
function calc(a,b){return Math.sqrt(((3-Math.sqrt(5))/2)*a/b)/(2*Math.PI);}
function fmt(v){if(!Number.isFinite(v))return 'undefined';if(Math.abs(v)>=1000)return v.toFixed(1);if(Math.abs(v)>=1)return v.toFixed(3);return v.toPrecision(4)}
function render(){const a=+aEl.value,b=+bEl.value;card.querySelector("#" + 'aout'.replace(/^#/, "")).textContent=fmt(a);card.querySelector("#" + 'bout'.replace(/^#/, "")).textContent=fmt(b);const value=calc(a,b);r.textContent=fmt(value)+' Hz';const amin=+aEl.min,amax=+aEl.max,W=810,H=255,pad=26;const samples=[];for(let i=0;i<140;i++){const x=amin+(amax-amin)*i/139,y=calc(x,b);if(Number.isFinite(y))samples.push({x,y});}const ymin=Math.min(...samples.map(p=>p.y)),ymax=Math.max(...samples.map(p=>p.y)),range=Math.max(1e-10,ymax-ymin),xx=x=>pad+(W-2*pad)*(x-amin)/(amax-amin),yy=y=>H-pad-(H-2*pad)*(y-ymin)/range;curve.setAttribute('points',samples.map(p=>xx(p.x).toFixed(1)+','+yy(p.y).toFixed(1)).join(' '));dot.setAttribute('cx',xx(a));dot.setAttribute('cy',yy(value));axes.textContent='Horizontal: '+aEl.previousElementSibling.textContent.split(':')[0]+' | vertical response: '+fmt(ymin)+' – '+fmt(ymax);status.textContent=Number.isFinite(value)?'Interactive calculation updated.':'Chosen parameters outside model bounds';}
aEl.addEventListener('input',render);bEl.addEventListener('input',render);card.querySelector("#" + 'reset'.replace(/^#/, "")).addEventListener('click',()=>{aEl.value='1000';bEl.value='2';render()});render();
      } catch (err) {
        console.warn('Sim init error in model 9:', err);
      }
    }
  });

  MODELS.push({
    idx: 10,
    unit: 5,
    html: "<p> \u00b7 </p><div class=\"panel\"><p class=\"tag\">INTERACTIVE MODEL 10 / 16 \u2014 OFFLINE</p><h3>Higher mode frequency, 2 DOF</h3><p>For M=m I and K=k[[2,\u22121],[\u22121,1]], upper eigenvalue=(3+\u221a5)k/(2m).</p><label for=\"a\">spring stiffness k (N/m): <output id=\"aout\"></output></label><input class=\"sl\" type=\"range\" id=\"a\" min=\"100\" max=\"10000\" step=\"0.1\" value=\"1000\"><label for=\"b\">each mass m (kg): <output id=\"bout\"></output></label><input class=\"sl\" type=\"range\" id=\"b\" min=\"0.5\" max=\"20\" step=\"0.01\" value=\"2\"><div class=\"reading\">Illustrative response <div id=\"result\" aria-live=\"polite\"></div></div><svg id=\"plot\" viewBox=\"0 0 810 255\" role=\"img\" aria-label=\"Computed response curve as the first parameter varies\"><rect x=\"26\" y=\"26\" width=\"758\" height=\"203\" fill=\"none\" stroke=\"#a1b4c6\" stroke-width=\"1\"/><polyline id=\"curve\" points=\"\" stroke=\"#127ca4\" stroke-width=\"3\" fill=\"none\"/><circle id=\"dot\" r=\"7\" cx=\"0\" cy=\"0\" fill=\"#d76329\" stroke=\"white\" stroke-width=\"2\"/></svg><small id=\"axes\"></small><p><button id=\"reset\" type=\"button\">Reset inputs</button> <small id=\"status\" aria-live=\"polite\"></small></p><div class=\"warning\">This is a simplified illustrative equation, not a digital twin. No fatigue, equipment acceptance, safe excitation level or measured machine performance is implied. A real installation needs independently measured parameters and qualified review.</div></div>",
    init: function(card) {
      try {
const aEl=card.querySelector("#" + 'a'.replace(/^#/, "")),bEl=card.querySelector("#" + 'b'.replace(/^#/, "")),r=card.querySelector("#" + 'result'.replace(/^#/, "")),curve=card.querySelector("#" + 'curve'.replace(/^#/, "")),dot=card.querySelector("#" + 'dot'.replace(/^#/, "")),axes=card.querySelector("#" + 'axes'.replace(/^#/, "")),status=card.querySelector("#" + 'status'.replace(/^#/, ""));
function calc(a,b){return Math.sqrt(((3+Math.sqrt(5))/2)*a/b)/(2*Math.PI);}
function fmt(v){if(!Number.isFinite(v))return 'undefined';if(Math.abs(v)>=1000)return v.toFixed(1);if(Math.abs(v)>=1)return v.toFixed(3);return v.toPrecision(4)}
function render(){const a=+aEl.value,b=+bEl.value;card.querySelector("#" + 'aout'.replace(/^#/, "")).textContent=fmt(a);card.querySelector("#" + 'bout'.replace(/^#/, "")).textContent=fmt(b);const value=calc(a,b);r.textContent=fmt(value)+' Hz';const amin=+aEl.min,amax=+aEl.max,W=810,H=255,pad=26;const samples=[];for(let i=0;i<140;i++){const x=amin+(amax-amin)*i/139,y=calc(x,b);if(Number.isFinite(y))samples.push({x,y});}const ymin=Math.min(...samples.map(p=>p.y)),ymax=Math.max(...samples.map(p=>p.y)),range=Math.max(1e-10,ymax-ymin),xx=x=>pad+(W-2*pad)*(x-amin)/(amax-amin),yy=y=>H-pad-(H-2*pad)*(y-ymin)/range;curve.setAttribute('points',samples.map(p=>xx(p.x).toFixed(1)+','+yy(p.y).toFixed(1)).join(' '));dot.setAttribute('cx',xx(a));dot.setAttribute('cy',yy(value));axes.textContent='Horizontal: '+aEl.previousElementSibling.textContent.split(':')[0]+' | vertical response: '+fmt(ymin)+' – '+fmt(ymax);status.textContent=Number.isFinite(value)?'Interactive calculation updated.':'Chosen parameters outside model bounds';}
aEl.addEventListener('input',render);bEl.addEventListener('input',render);card.querySelector("#" + 'reset'.replace(/^#/, "")).addEventListener('click',()=>{aEl.value='1000';bEl.value='2';render()});render();
      } catch (err) {
        console.warn('Sim init error in model 10:', err);
      }
    }
  });

  MODELS.push({
    idx: 11,
    unit: 6,
    html: "<p> \u00b7 </p><div class=\"panel\"><p class=\"tag\">INTERACTIVE MODEL 11 / 16 \u2014 OFFLINE</p><h3>Tensioned-string fundamental</h3><p>f1=\u221a(T/\u03bc)/(2L); fixed-end ideal string and \u03bc=0.01 kg/m.</p><label for=\"a\">tension T (N): <output id=\"aout\"></output></label><input class=\"sl\" type=\"range\" id=\"a\" min=\"10\" max=\"900\" step=\"0.1\" value=\"100\"><label for=\"b\">length L (m): <output id=\"bout\"></output></label><input class=\"sl\" type=\"range\" id=\"b\" min=\"0.5\" max=\"10\" step=\"0.01\" value=\"2\"><div class=\"reading\">Illustrative response <div id=\"result\" aria-live=\"polite\"></div></div><svg id=\"plot\" viewBox=\"0 0 810 255\" role=\"img\" aria-label=\"Computed response curve as the first parameter varies\"><rect x=\"26\" y=\"26\" width=\"758\" height=\"203\" fill=\"none\" stroke=\"#a1b4c6\" stroke-width=\"1\"/><polyline id=\"curve\" points=\"\" stroke=\"#127ca4\" stroke-width=\"3\" fill=\"none\"/><circle id=\"dot\" r=\"7\" cx=\"0\" cy=\"0\" fill=\"#d76329\" stroke=\"white\" stroke-width=\"2\"/></svg><small id=\"axes\"></small><p><button id=\"reset\" type=\"button\">Reset inputs</button> <small id=\"status\" aria-live=\"polite\"></small></p><div class=\"warning\">This is a simplified illustrative equation, not a digital twin. No fatigue, equipment acceptance, safe excitation level or measured machine performance is implied. A real installation needs independently measured parameters and qualified review.</div></div>",
    init: function(card) {
      try {
const aEl=card.querySelector("#" + 'a'.replace(/^#/, "")),bEl=card.querySelector("#" + 'b'.replace(/^#/, "")),r=card.querySelector("#" + 'result'.replace(/^#/, "")),curve=card.querySelector("#" + 'curve'.replace(/^#/, "")),dot=card.querySelector("#" + 'dot'.replace(/^#/, "")),axes=card.querySelector("#" + 'axes'.replace(/^#/, "")),status=card.querySelector("#" + 'status'.replace(/^#/, ""));
function calc(a,b){return Math.sqrt(a/0.01)/(2*b);}
function fmt(v){if(!Number.isFinite(v))return 'undefined';if(Math.abs(v)>=1000)return v.toFixed(1);if(Math.abs(v)>=1)return v.toFixed(3);return v.toPrecision(4)}
function render(){const a=+aEl.value,b=+bEl.value;card.querySelector("#" + 'aout'.replace(/^#/, "")).textContent=fmt(a);card.querySelector("#" + 'bout'.replace(/^#/, "")).textContent=fmt(b);const value=calc(a,b);r.textContent=fmt(value)+' Hz';const amin=+aEl.min,amax=+aEl.max,W=810,H=255,pad=26;const samples=[];for(let i=0;i<140;i++){const x=amin+(amax-amin)*i/139,y=calc(x,b);if(Number.isFinite(y))samples.push({x,y});}const ymin=Math.min(...samples.map(p=>p.y)),ymax=Math.max(...samples.map(p=>p.y)),range=Math.max(1e-10,ymax-ymin),xx=x=>pad+(W-2*pad)*(x-amin)/(amax-amin),yy=y=>H-pad-(H-2*pad)*(y-ymin)/range;curve.setAttribute('points',samples.map(p=>xx(p.x).toFixed(1)+','+yy(p.y).toFixed(1)).join(' '));dot.setAttribute('cx',xx(a));dot.setAttribute('cy',yy(value));axes.textContent='Horizontal: '+aEl.previousElementSibling.textContent.split(':')[0]+' | vertical response: '+fmt(ymin)+' – '+fmt(ymax);status.textContent=Number.isFinite(value)?'Interactive calculation updated.':'Chosen parameters outside model bounds';}
aEl.addEventListener('input',render);bEl.addEventListener('input',render);card.querySelector("#" + 'reset'.replace(/^#/, "")).addEventListener('click',()=>{aEl.value='100';bEl.value='2';render()});render();
      } catch (err) {
        console.warn('Sim init error in model 11:', err);
      }
    }
  });

  MODELS.push({
    idx: 12,
    unit: 6,
    html: "<p> \u00b7 </p><div class=\"panel\"><p class=\"tag\">INTERACTIVE MODEL 12 / 16 \u2014 OFFLINE</p><h3>Rotating imbalance force</h3><p>F=U\u03c9\u00b2, U=m_e e. This is centrifugal excitation amplitude, not necessarily bearing reaction.</p><label for=\"a\">rotational speed (rpm): <output id=\"aout\"></output></label><input class=\"sl\" type=\"range\" id=\"a\" min=\"100\" max=\"8000\" step=\"0.1\" value=\"3000\"><label for=\"b\">unbalance mass-radius (kg\u00b7m): <output id=\"bout\"></output></label><input class=\"sl\" type=\"range\" id=\"b\" min=\"1e-05\" max=\"0.003\" step=\"0.00001\" value=\"0.0002\"><div class=\"reading\">Illustrative response <div id=\"result\" aria-live=\"polite\"></div></div><svg id=\"plot\" viewBox=\"0 0 810 255\" role=\"img\" aria-label=\"Computed response curve as the first parameter varies\"><rect x=\"26\" y=\"26\" width=\"758\" height=\"203\" fill=\"none\" stroke=\"#a1b4c6\" stroke-width=\"1\"/><polyline id=\"curve\" points=\"\" stroke=\"#127ca4\" stroke-width=\"3\" fill=\"none\"/><circle id=\"dot\" r=\"7\" cx=\"0\" cy=\"0\" fill=\"#d76329\" stroke=\"white\" stroke-width=\"2\"/></svg><small id=\"axes\"></small><p><button id=\"reset\" type=\"button\">Reset inputs</button> <small id=\"status\" aria-live=\"polite\"></small></p><div class=\"warning\">This is a simplified illustrative equation, not a digital twin. No fatigue, equipment acceptance, safe excitation level or measured machine performance is implied. A real installation needs independently measured parameters and qualified review.</div></div>",
    init: function(card) {
      try {
const aEl=card.querySelector("#" + 'a'.replace(/^#/, "")),bEl=card.querySelector("#" + 'b'.replace(/^#/, "")),r=card.querySelector("#" + 'result'.replace(/^#/, "")),curve=card.querySelector("#" + 'curve'.replace(/^#/, "")),dot=card.querySelector("#" + 'dot'.replace(/^#/, "")),axes=card.querySelector("#" + 'axes'.replace(/^#/, "")),status=card.querySelector("#" + 'status'.replace(/^#/, ""));
function calc(a,b){return b*(2*Math.PI*a/60)**2;}
function fmt(v){if(!Number.isFinite(v))return 'undefined';if(Math.abs(v)>=1000)return v.toFixed(1);if(Math.abs(v)>=1)return v.toFixed(3);return v.toPrecision(4)}
function render(){const a=+aEl.value,b=+bEl.value;card.querySelector("#" + 'aout'.replace(/^#/, "")).textContent=fmt(a);card.querySelector("#" + 'bout'.replace(/^#/, "")).textContent=fmt(b);const value=calc(a,b);r.textContent=fmt(value)+' N';const amin=+aEl.min,amax=+aEl.max,W=810,H=255,pad=26;const samples=[];for(let i=0;i<140;i++){const x=amin+(amax-amin)*i/139,y=calc(x,b);if(Number.isFinite(y))samples.push({x,y});}const ymin=Math.min(...samples.map(p=>p.y)),ymax=Math.max(...samples.map(p=>p.y)),range=Math.max(1e-10,ymax-ymin),xx=x=>pad+(W-2*pad)*(x-amin)/(amax-amin),yy=y=>H-pad-(H-2*pad)*(y-ymin)/range;curve.setAttribute('points',samples.map(p=>xx(p.x).toFixed(1)+','+yy(p.y).toFixed(1)).join(' '));dot.setAttribute('cx',xx(a));dot.setAttribute('cy',yy(value));axes.textContent='Horizontal: '+aEl.previousElementSibling.textContent.split(':')[0]+' | vertical response: '+fmt(ymin)+' – '+fmt(ymax);status.textContent=Number.isFinite(value)?'Interactive calculation updated.':'Chosen parameters outside model bounds';}
aEl.addEventListener('input',render);bEl.addEventListener('input',render);card.querySelector("#" + 'reset'.replace(/^#/, "")).addEventListener('click',()=>{aEl.value='3000';bEl.value='0.0002';render()});render();
      } catch (err) {
        console.warn('Sim init error in model 12:', err);
      }
    }
  });

  MODELS.push({
    idx: 13,
    unit: 7,
    html: "<p> \u00b7 </p><div class=\"panel\"><p class=\"tag\">INTERACTIVE MODEL 13 / 16 \u2014 OFFLINE</p><h3>Displacement inferred from sinusoidal acceleration</h3><p>X_peak = a_peak/\u03c9\u00b2 for one stationary harmonic component.</p><label for=\"a\">acceleration peak (m/s\u00b2): <output id=\"aout\"></output></label><input class=\"sl\" type=\"range\" id=\"a\" min=\"0.05\" max=\"30\" step=\"0.01\" value=\"2\"><label for=\"b\">frequency (Hz): <output id=\"bout\"></output></label><input class=\"sl\" type=\"range\" id=\"b\" min=\"1\" max=\"100\" step=\"0.01\" value=\"10\"><div class=\"reading\">Illustrative response <div id=\"result\" aria-live=\"polite\"></div></div><svg id=\"plot\" viewBox=\"0 0 810 255\" role=\"img\" aria-label=\"Computed response curve as the first parameter varies\"><rect x=\"26\" y=\"26\" width=\"758\" height=\"203\" fill=\"none\" stroke=\"#a1b4c6\" stroke-width=\"1\"/><polyline id=\"curve\" points=\"\" stroke=\"#127ca4\" stroke-width=\"3\" fill=\"none\"/><circle id=\"dot\" r=\"7\" cx=\"0\" cy=\"0\" fill=\"#d76329\" stroke=\"white\" stroke-width=\"2\"/></svg><small id=\"axes\"></small><p><button id=\"reset\" type=\"button\">Reset inputs</button> <small id=\"status\" aria-live=\"polite\"></small></p><div class=\"warning\">This is a simplified illustrative equation, not a digital twin. No fatigue, equipment acceptance, safe excitation level or measured machine performance is implied. A real installation needs independently measured parameters and qualified review.</div></div>",
    init: function(card) {
      try {
const aEl=card.querySelector("#" + 'a'.replace(/^#/, "")),bEl=card.querySelector("#" + 'b'.replace(/^#/, "")),r=card.querySelector("#" + 'result'.replace(/^#/, "")),curve=card.querySelector("#" + 'curve'.replace(/^#/, "")),dot=card.querySelector("#" + 'dot'.replace(/^#/, "")),axes=card.querySelector("#" + 'axes'.replace(/^#/, "")),status=card.querySelector("#" + 'status'.replace(/^#/, ""));
function calc(a,b){return 1000*a/(2*Math.PI*b)**2;}
function fmt(v){if(!Number.isFinite(v))return 'undefined';if(Math.abs(v)>=1000)return v.toFixed(1);if(Math.abs(v)>=1)return v.toFixed(3);return v.toPrecision(4)}
function render(){const a=+aEl.value,b=+bEl.value;card.querySelector("#" + 'aout'.replace(/^#/, "")).textContent=fmt(a);card.querySelector("#" + 'bout'.replace(/^#/, "")).textContent=fmt(b);const value=calc(a,b);r.textContent=fmt(value)+' mm';const amin=+aEl.min,amax=+aEl.max,W=810,H=255,pad=26;const samples=[];for(let i=0;i<140;i++){const x=amin+(amax-amin)*i/139,y=calc(x,b);if(Number.isFinite(y))samples.push({x,y});}const ymin=Math.min(...samples.map(p=>p.y)),ymax=Math.max(...samples.map(p=>p.y)),range=Math.max(1e-10,ymax-ymin),xx=x=>pad+(W-2*pad)*(x-amin)/(amax-amin),yy=y=>H-pad-(H-2*pad)*(y-ymin)/range;curve.setAttribute('points',samples.map(p=>xx(p.x).toFixed(1)+','+yy(p.y).toFixed(1)).join(' '));dot.setAttribute('cx',xx(a));dot.setAttribute('cy',yy(value));axes.textContent='Horizontal: '+aEl.previousElementSibling.textContent.split(':')[0]+' | vertical response: '+fmt(ymin)+' – '+fmt(ymax);status.textContent=Number.isFinite(value)?'Interactive calculation updated.':'Chosen parameters outside model bounds';}
aEl.addEventListener('input',render);bEl.addEventListener('input',render);card.querySelector("#" + 'reset'.replace(/^#/, "")).addEventListener('click',()=>{aEl.value='2';bEl.value='10';render()});render();
      } catch (err) {
        console.warn('Sim init error in model 13:', err);
      }
    }
  });

  MODELS.push({
    idx: 14,
    unit: 7,
    html: "<p> \u00b7 </p><div class=\"panel\"><p class=\"tag\">INTERACTIVE MODEL 14 / 16 \u2014 OFFLINE</p><h3>Idealized alias frequency</h3><p>Discrete-time alias magnitude |f\u2212n f_s| with n the nearest integer; requires anti-alias filters in real acquisition.</p><label for=\"a\">signal frequency (Hz): <output id=\"aout\"></output></label><input class=\"sl\" type=\"range\" id=\"a\" min=\"1\" max=\"500\" step=\"0.1\" value=\"70\"><label for=\"b\">sampling frequency (Hz): <output id=\"bout\"></output></label><input class=\"sl\" type=\"range\" id=\"b\" min=\"30\" max=\"250\" step=\"0.1\" value=\"100\"><div class=\"reading\">Illustrative response <div id=\"result\" aria-live=\"polite\"></div></div><svg id=\"plot\" viewBox=\"0 0 810 255\" role=\"img\" aria-label=\"Computed response curve as the first parameter varies\"><rect x=\"26\" y=\"26\" width=\"758\" height=\"203\" fill=\"none\" stroke=\"#a1b4c6\" stroke-width=\"1\"/><polyline id=\"curve\" points=\"\" stroke=\"#127ca4\" stroke-width=\"3\" fill=\"none\"/><circle id=\"dot\" r=\"7\" cx=\"0\" cy=\"0\" fill=\"#d76329\" stroke=\"white\" stroke-width=\"2\"/></svg><small id=\"axes\"></small><p><button id=\"reset\" type=\"button\">Reset inputs</button> <small id=\"status\" aria-live=\"polite\"></small></p><div class=\"warning\">This is a simplified illustrative equation, not a digital twin. No fatigue, equipment acceptance, safe excitation level or measured machine performance is implied. A real installation needs independently measured parameters and qualified review.</div></div>",
    init: function(card) {
      try {
const aEl=card.querySelector("#" + 'a'.replace(/^#/, "")),bEl=card.querySelector("#" + 'b'.replace(/^#/, "")),r=card.querySelector("#" + 'result'.replace(/^#/, "")),curve=card.querySelector("#" + 'curve'.replace(/^#/, "")),dot=card.querySelector("#" + 'dot'.replace(/^#/, "")),axes=card.querySelector("#" + 'axes'.replace(/^#/, "")),status=card.querySelector("#" + 'status'.replace(/^#/, ""));
function calc(a,b){return Math.abs(a-Math.round(a/b)*b);}
function fmt(v){if(!Number.isFinite(v))return 'undefined';if(Math.abs(v)>=1000)return v.toFixed(1);if(Math.abs(v)>=1)return v.toFixed(3);return v.toPrecision(4)}
function render(){const a=+aEl.value,b=+bEl.value;card.querySelector("#" + 'aout'.replace(/^#/, "")).textContent=fmt(a);card.querySelector("#" + 'bout'.replace(/^#/, "")).textContent=fmt(b);const value=calc(a,b);r.textContent=fmt(value)+' Hz';const amin=+aEl.min,amax=+aEl.max,W=810,H=255,pad=26;const samples=[];for(let i=0;i<140;i++){const x=amin+(amax-amin)*i/139,y=calc(x,b);if(Number.isFinite(y))samples.push({x,y});}const ymin=Math.min(...samples.map(p=>p.y)),ymax=Math.max(...samples.map(p=>p.y)),range=Math.max(1e-10,ymax-ymin),xx=x=>pad+(W-2*pad)*(x-amin)/(amax-amin),yy=y=>H-pad-(H-2*pad)*(y-ymin)/range;curve.setAttribute('points',samples.map(p=>xx(p.x).toFixed(1)+','+yy(p.y).toFixed(1)).join(' '));dot.setAttribute('cx',xx(a));dot.setAttribute('cy',yy(value));axes.textContent='Horizontal: '+aEl.previousElementSibling.textContent.split(':')[0]+' | vertical response: '+fmt(ymin)+' – '+fmt(ymax);status.textContent=Number.isFinite(value)?'Interactive calculation updated.':'Chosen parameters outside model bounds';}
aEl.addEventListener('input',render);bEl.addEventListener('input',render);card.querySelector("#" + 'reset'.replace(/^#/, "")).addEventListener('click',()=>{aEl.value='70';bEl.value='100';render()});render();
      } catch (err) {
        console.warn('Sim init error in model 14:', err);
      }
    }
  });

  MODELS.push({
    idx: 15,
    unit: 8,
    html: "<p> \u00b7 </p><div class=\"panel\"><p class=\"tag\">INTERACTIVE MODEL 15 / 16 \u2014 OFFLINE</p><h3>Auxiliary oscillator tuning stiffness</h3><p>k_t=m_t(2\u03c0f_t)\u00b2; not a complete tuned-mass-damper design.</p><label for=\"a\">target frequency (Hz): <output id=\"aout\"></output></label><input class=\"sl\" type=\"range\" id=\"a\" min=\"2\" max=\"60\" step=\"0.01\" value=\"18\"><label for=\"b\">auxiliary mass (kg): <output id=\"bout\"></output></label><input class=\"sl\" type=\"range\" id=\"b\" min=\"0.2\" max=\"15\" step=\"0.01\" value=\"2\"><div class=\"reading\">Illustrative response <div id=\"result\" aria-live=\"polite\"></div></div><svg id=\"plot\" viewBox=\"0 0 810 255\" role=\"img\" aria-label=\"Computed response curve as the first parameter varies\"><rect x=\"26\" y=\"26\" width=\"758\" height=\"203\" fill=\"none\" stroke=\"#a1b4c6\" stroke-width=\"1\"/><polyline id=\"curve\" points=\"\" stroke=\"#127ca4\" stroke-width=\"3\" fill=\"none\"/><circle id=\"dot\" r=\"7\" cx=\"0\" cy=\"0\" fill=\"#d76329\" stroke=\"white\" stroke-width=\"2\"/></svg><small id=\"axes\"></small><p><button id=\"reset\" type=\"button\">Reset inputs</button> <small id=\"status\" aria-live=\"polite\"></small></p><div class=\"warning\">This is a simplified illustrative equation, not a digital twin. No fatigue, equipment acceptance, safe excitation level or measured machine performance is implied. A real installation needs independently measured parameters and qualified review.</div></div>",
    init: function(card) {
      try {
const aEl=card.querySelector("#" + 'a'.replace(/^#/, "")),bEl=card.querySelector("#" + 'b'.replace(/^#/, "")),r=card.querySelector("#" + 'result'.replace(/^#/, "")),curve=card.querySelector("#" + 'curve'.replace(/^#/, "")),dot=card.querySelector("#" + 'dot'.replace(/^#/, "")),axes=card.querySelector("#" + 'axes'.replace(/^#/, "")),status=card.querySelector("#" + 'status'.replace(/^#/, ""));
function calc(a,b){return b*(2*Math.PI*a)**2;}
function fmt(v){if(!Number.isFinite(v))return 'undefined';if(Math.abs(v)>=1000)return v.toFixed(1);if(Math.abs(v)>=1)return v.toFixed(3);return v.toPrecision(4)}
function render(){const a=+aEl.value,b=+bEl.value;card.querySelector("#" + 'aout'.replace(/^#/, "")).textContent=fmt(a);card.querySelector("#" + 'bout'.replace(/^#/, "")).textContent=fmt(b);const value=calc(a,b);r.textContent=fmt(value)+' N/m';const amin=+aEl.min,amax=+aEl.max,W=810,H=255,pad=26;const samples=[];for(let i=0;i<140;i++){const x=amin+(amax-amin)*i/139,y=calc(x,b);if(Number.isFinite(y))samples.push({x,y});}const ymin=Math.min(...samples.map(p=>p.y)),ymax=Math.max(...samples.map(p=>p.y)),range=Math.max(1e-10,ymax-ymin),xx=x=>pad+(W-2*pad)*(x-amin)/(amax-amin),yy=y=>H-pad-(H-2*pad)*(y-ymin)/range;curve.setAttribute('points',samples.map(p=>xx(p.x).toFixed(1)+','+yy(p.y).toFixed(1)).join(' '));dot.setAttribute('cx',xx(a));dot.setAttribute('cy',yy(value));axes.textContent='Horizontal: '+aEl.previousElementSibling.textContent.split(':')[0]+' | vertical response: '+fmt(ymin)+' – '+fmt(ymax);status.textContent=Number.isFinite(value)?'Interactive calculation updated.':'Chosen parameters outside model bounds';}
aEl.addEventListener('input',render);bEl.addEventListener('input',render);card.querySelector("#" + 'reset'.replace(/^#/, "")).addEventListener('click',()=>{aEl.value='18';bEl.value='2';render()});render();
      } catch (err) {
        console.warn('Sim init error in model 15:', err);
      }
    }
  });

  MODELS.push({
    idx: 16,
    unit: 8,
    html: "<p> \u00b7 </p><div class=\"panel\"><p class=\"tag\">INTERACTIVE MODEL 16 / 16 \u2014 OFFLINE</p><h3>Frequency after stiffness change</h3><p>f_new=f_old\u221a(1+\u0394k/k) at constant mass and boundary conditions.</p><label for=\"a\">stiffness change (%): <output id=\"aout\"></output></label><input class=\"sl\" type=\"range\" id=\"a\" min=\"-45\" max=\"75\" step=\"0.01\" value=\"10\"><label for=\"b\">baseline frequency (Hz): <output id=\"bout\"></output></label><input class=\"sl\" type=\"range\" id=\"b\" min=\"1\" max=\"100\" step=\"0.01\" value=\"25\"><div class=\"reading\">Illustrative response <div id=\"result\" aria-live=\"polite\"></div></div><svg id=\"plot\" viewBox=\"0 0 810 255\" role=\"img\" aria-label=\"Computed response curve as the first parameter varies\"><rect x=\"26\" y=\"26\" width=\"758\" height=\"203\" fill=\"none\" stroke=\"#a1b4c6\" stroke-width=\"1\"/><polyline id=\"curve\" points=\"\" stroke=\"#127ca4\" stroke-width=\"3\" fill=\"none\"/><circle id=\"dot\" r=\"7\" cx=\"0\" cy=\"0\" fill=\"#d76329\" stroke=\"white\" stroke-width=\"2\"/></svg><small id=\"axes\"></small><p><button id=\"reset\" type=\"button\">Reset inputs</button> <small id=\"status\" aria-live=\"polite\"></small></p><div class=\"warning\">This is a simplified illustrative equation, not a digital twin. No fatigue, equipment acceptance, safe excitation level or measured machine performance is implied. A real installation needs independently measured parameters and qualified review.</div></div>",
    init: function(card) {
      try {
const aEl=card.querySelector("#" + 'a'.replace(/^#/, "")),bEl=card.querySelector("#" + 'b'.replace(/^#/, "")),r=card.querySelector("#" + 'result'.replace(/^#/, "")),curve=card.querySelector("#" + 'curve'.replace(/^#/, "")),dot=card.querySelector("#" + 'dot'.replace(/^#/, "")),axes=card.querySelector("#" + 'axes'.replace(/^#/, "")),status=card.querySelector("#" + 'status'.replace(/^#/, ""));
function calc(a,b){return b*Math.sqrt(1+a/100);}
function fmt(v){if(!Number.isFinite(v))return 'undefined';if(Math.abs(v)>=1000)return v.toFixed(1);if(Math.abs(v)>=1)return v.toFixed(3);return v.toPrecision(4)}
function render(){const a=+aEl.value,b=+bEl.value;card.querySelector("#" + 'aout'.replace(/^#/, "")).textContent=fmt(a);card.querySelector("#" + 'bout'.replace(/^#/, "")).textContent=fmt(b);const value=calc(a,b);r.textContent=fmt(value)+' Hz';const amin=+aEl.min,amax=+aEl.max,W=810,H=255,pad=26;const samples=[];for(let i=0;i<140;i++){const x=amin+(amax-amin)*i/139,y=calc(x,b);if(Number.isFinite(y))samples.push({x,y});}const ymin=Math.min(...samples.map(p=>p.y)),ymax=Math.max(...samples.map(p=>p.y)),range=Math.max(1e-10,ymax-ymin),xx=x=>pad+(W-2*pad)*(x-amin)/(amax-amin),yy=y=>H-pad-(H-2*pad)*(y-ymin)/range;curve.setAttribute('points',samples.map(p=>xx(p.x).toFixed(1)+','+yy(p.y).toFixed(1)).join(' '));dot.setAttribute('cx',xx(a));dot.setAttribute('cy',yy(value));axes.textContent='Horizontal: '+aEl.previousElementSibling.textContent.split(':')[0]+' | vertical response: '+fmt(ymin)+' – '+fmt(ymax);status.textContent=Number.isFinite(value)?'Interactive calculation updated.':'Chosen parameters outside model bounds';}
aEl.addEventListener('input',render);bEl.addEventListener('input',render);card.querySelector("#" + 'reset'.replace(/^#/, "")).addEventListener('click',()=>{aEl.value='10';bEl.value='25';render()});render();
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
