/* robotics-and-automation Interactive Simulation Suite */
(function(window) {
  'use strict';

  var OPENSTEM_SIM_MODELS = [];

  // Core models logic
  (function() {
"use strict";
const models = [{"id": 1, "title": "Workspace outer reach", "description": "Two serial planar link lengths add to an outer radial reach; joint stops may reduce attainable workspace.", "x": {"name": "link 1 length", "unit": "m", "min": 0.1, "max": 0.75, "step": 0.01, "default": 0.3}, "z": {"name": "link 2 length", "unit": "m", "min": 0.1, "max": 0.65, "step": 0.01, "default": 0.2}, "expression": "r_max=L1+L2", "formula": "p1+p2", "unit": "m", "warning": "This is only a geometric outer bound, not a collision-free reach."}, {"id": 2, "title": "Two-link arm X coordinate", "description": "Evaluate planar 2R forward kinematics with lengths L1=0.30 m and L2=0.20 m.", "x": {"name": "joint 1 angle", "unit": "deg", "min": -180, "max": 180, "step": 5, "default": 20}, "z": {"name": "joint 2 angle", "unit": "deg", "min": -180, "max": 180, "step": 5, "default": 55}, "expression": "x=.30 cos(q1)+.20 cos(q1+q2)", "formula": "0.30*Math.cos(p1*Math.PI/180)+0.20*Math.cos((p1+p2)*Math.PI/180)", "unit": "m", "warning": "Joint limits and collision constraints are excluded."}, {"id": 3, "title": "Planar Jacobian determinant", "description": "Use determinant to reveal the loss of locally independent Cartesian motion.", "x": {"name": "elbow angle", "unit": "deg", "min": -180, "max": 180, "step": 5, "default": 90}, "z": {"name": "link 2 length", "unit": "m", "min": 0.1, "max": 0.55, "step": 0.01, "default": 0.2}, "expression": "detJ=.30 L2 sin(q2)", "formula": "0.30*p2*Math.sin(p1*Math.PI/180)", "unit": "m²", "warning": "Near zero determinant, inversion can amplify noise."}, {"id": 4, "title": "IK elbow cosine feasibility", "description": "Monitor law-of-cosines value: absolute values over one signal unreachable targets.", "x": {"name": "radial distance", "unit": "m", "min": 0, "max": 0.8, "step": 0.01, "default": 0.4}, "z": {"name": "second-link length", "unit": "m", "min": 0.1, "max": 0.5, "step": 0.01, "default": 0.2}, "expression": "cos(q2)=(r²-L1²-L2²)/(2 L1 L2)", "formula": "(p1*p1-0.30*0.30-p2*p2)/(2*0.30*p2)", "unit": "dimensionless", "warning": "Valid only if absolute value is ≤1 and physical joint limits allow solution."}, {"id": 5, "title": "Gear-reduced joint torque", "description": "Simple output torque from motor torque, transmission ratio and fixed efficiency 0.8.", "x": {"name": "motor torque", "unit": "N m", "min": 0, "max": 1, "step": 0.025, "default": 0.15}, "z": {"name": "gear ratio", "unit": "ratio", "min": 1, "max": 30, "step": 1, "default": 12}, "expression": "tau_out=0.8 G tau_motor", "formula": "0.8*p1*p2", "unit": "N m", "warning": "Do not mistake point efficiency and peak torque for continuous rating."}, {"id": 6, "title": "Single-link gravitational torque", "description": "A horizontal reference makes gravitational torque magnitude m g L |cos(q)| for a lumped tip mass.", "x": {"name": "link angle", "unit": "deg", "min": -90, "max": 90, "step": 5, "default": 0}, "z": {"name": "tip mass", "unit": "kg", "min": 0.1, "max": 5, "step": 0.1, "default": 1.5}, "expression": "|tau|=m g L |cos(q)|", "formula": "p2*9.81*0.3*Math.abs(Math.cos(p1*Math.PI/180))", "unit": "N m", "warning": "Link mass, transmission friction and acceleration are omitted."}, {"id": 7, "title": "Rest-to-rest motion time", "description": "Switch between triangular and trapezoidal profiles; speed cap fixed to 1 m/s.", "x": {"name": "travel distance", "unit": "m", "min": 0.01, "max": 2, "step": 0.01, "default": 0.25}, "z": {"name": "acceleration cap", "unit": "m/s²", "min": 0.2, "max": 3, "step": 0.05, "default": 1}, "expression": "t=2 sqrt(d/a) if d≤1/a else d+1/a", "formula": "p1<=1/p2 ? 2*Math.sqrt(p1/p2) : p1+1/p2", "unit": "s", "warning": "Ideal 1D travel assumes instantaneous acceleration changes and no jerk cap."}, {"id": 8, "title": "Jerk from acceleration ramp", "description": "Compute average jerk as acceleration change divided by transition time.", "x": {"name": "acceleration change", "unit": "m/s²", "min": 0, "max": 10, "step": 0.1, "default": 2}, "z": {"name": "ramp duration", "unit": "s", "min": 0.05, "max": 2, "step": 0.05, "default": 0.2}, "expression": "j=delta_a/delta_t", "formula": "p1/p2", "unit": "m/s³", "warning": "Average jerk is not peak jerk for arbitrary motion profiles."}, {"id": 9, "title": "Differential-drive turn rate", "description": "Right and left linear wheel speeds translate to yaw rate using a fixed 0.50 m track.", "x": {"name": "right-wheel speed", "unit": "m/s", "min": -0.8, "max": 0.8, "step": 0.05, "default": 0.6}, "z": {"name": "left-wheel speed", "unit": "m/s", "min": -0.8, "max": 0.8, "step": 0.05, "default": 0.2}, "expression": "omega=(vR-vL)/.50", "formula": "(p1-p2)/0.5", "unit": "rad/s", "warning": "Wheel slip and geometric calibration errors can dominate."}, {"id": 10, "title": "Two-wheel center travel", "description": "Estimate middle point travel using average wheel displacement.", "x": {"name": "right-wheel distance", "unit": "m", "min": -1, "max": 1, "step": 0.02, "default": 0.5}, "z": {"name": "left-wheel distance", "unit": "m", "min": -1, "max": 1, "step": 0.02, "default": 0.4}, "expression": "Delta_s=(dsR+dsL)/2", "formula": "(p1+p2)/2", "unit": "m", "warning": "Cannot infer absolute position without heading and initial pose."}, {"id": 11, "title": "Positive-detection occupancy posterior", "description": "One Bayesian sensor update with P(z+|occupied)=0.8 and P(z+|free)=0.2.", "x": {"name": "prior occupancy", "unit": "fraction", "min": 0.01, "max": 0.99, "step": 0.01, "default": 0.5}, "z": {"name": "true positive", "unit": "fraction", "min": 0.55, "max": 0.98, "step": 0.01, "default": 0.8}, "expression": "p_post=TP*p/(TP*p+.20*(1-p))", "formula": "p1*p2/(p1*p2+0.20*(1-p1))", "unit": "probability", "warning": "Repeated correlated detections must not be treated as independent."}, {"id": 12, "title": "Localization planar error norm", "description": "Root-mean-square style Euclidean error from two coordinate residuals.", "x": {"name": "x residual", "unit": "m", "min": -0.5, "max": 0.5, "step": 0.01, "default": 0.12}, "z": {"name": "y residual", "unit": "m", "min": -0.5, "max": 0.5, "step": 0.01, "default": 0.05}, "expression": "error=sqrt(dx²+dy²)", "formula": "Math.hypot(p1,p2)", "unit": "m", "warning": "A single endpoint error is not a full localization performance metric."}, {"id": 13, "title": "Stereo camera ideal depth", "description": "Compute depth from disparity using f=500 px and adjustable stereo baseline.", "x": {"name": "disparity", "unit": "pixels", "min": 2, "max": 150, "step": 1, "default": 50}, "z": {"name": "baseline", "unit": "m", "min": 0.03, "max": 0.3, "step": 0.01, "default": 0.1}, "expression": "Z=500 B/d", "formula": "500*p2/p1", "unit": "m", "warning": "Occlusion, mismatched pixels and calibration biases invalidate ideal triangulation."}, {"id": 14, "title": "Ideal obstacle stopping distance", "description": "Includes commanded speed times delay and constant-braking-distance term with deceleration fixed to 1 m/s².", "x": {"name": "speed", "unit": "m/s", "min": 0, "max": 2, "step": 0.025, "default": 0.8}, "z": {"name": "perception + control delay", "unit": "s", "min": 0, "max": 0.5, "step": 0.01, "default": 0.1}, "expression": "d=v*t+v²/2", "formula": "p1*p2+p1*p1/2", "unit": "m", "warning": "No clearance margin, reaction uncertainty, brake fault or obstacle motion is included."}, {"id": 15, "title": "Exponential reliability illustration", "description": "Use constant hazard assumption to illustrate probability of surviving time without failure.", "x": {"name": "operating time", "unit": "hours", "min": 0, "max": 2000, "step": 25, "default": 500}, "z": {"name": "hazard rate", "unit": "1/hour", "min": 1e-05, "max": 0.001, "step": 1e-05, "default": 0.0002}, "expression": "R=exp(-lambda*t)", "formula": "Math.exp(-p1*p2)", "unit": "probability", "warning": "Wear-out processes generally violate constant hazard."}, {"id": 16, "title": "Cycle-time production rate", "description": "Illustrative accepted units per hour with per-cycle time and productive availability.", "x": {"name": "full cycle duration", "unit": "s", "min": 1, "max": 15, "step": 0.25, "default": 5}, "z": {"name": "productive fraction", "unit": "fraction", "min": 0.5, "max": 1, "step": 0.025, "default": 0.9}, "expression": "rate=3600*A/t", "formula": "3600*p2/p1", "unit": "units/hour", "warning": "Excludes rejects, variable part demand, parallel station constraints and correlated interruptions."}];
function calculate(m,p1,p2){switch(m.id){
case 1: return p1+p2;
case 2: return 0.30*Math.cos(p1*Math.PI/180)+0.20*Math.cos((p1+p2)*Math.PI/180);
case 3: return 0.30*p2*Math.sin(p1*Math.PI/180);
case 4: return (p1*p1-0.30*0.30-p2*p2)/(2*0.30*p2);
case 5: return 0.8*p1*p2;
case 6: return p2*9.81*0.3*Math.abs(Math.cos(p1*Math.PI/180));
case 7: return p1<=1/p2 ? 2*Math.sqrt(p1/p2) : p1+1/p2;
case 8: return p1/p2;
case 9: return (p1-p2)/0.5;
case 10: return (p1+p2)/2;
case 11: return p1*p2/(p1*p2+0.20*(1-p1));
case 12: return Math.hypot(p1,p2);
case 13: return 500*p2/p1;
case 14: return p1*p2+p1*p1/2;
case 15: return Math.exp(-p1*p2);
case 16: return 3600*p2/p1;
default: throw new Error("Unknown model")}}
window.OpenSTEMRobotics={models,calculate};
function initialize(){const mount=document.querySelector('[data-model]'); if(!mount)return;
 const m=models[Number(mount.dataset.model)-1];const p1=document.querySelector('#p1'),p2=document.querySelector('#p2'),display=document.querySelector('#answer'),xy=document.querySelector('#xy'),svg=document.querySelector('#plot');
 const p1v=document.querySelector('#p1value'),p2v=document.querySelector('#p2value');
 [[p1,m.x],[p2,m.z]].forEach(([el,p])=>{el.min=p.min;el.max=p.max;el.step=p.step;el.value=p.default});
 const fmt=n=>Number.isFinite(n)?(Math.abs(n)<0.0001 && n!==0?n.toExponential(3):n.toLocaleString('en-US',{maximumFractionDigits:5})):'not defined';
 function graph(){const a=Number(p1.value),b=Number(p2.value),y=calculate(m,a,b);p1v.textContent=fmt(a)+' '+m.x.unit;p2v.textContent=fmt(b)+' '+m.z.unit;display.textContent=fmt(y)+' '+m.unit;
 let pts=[];for(let i=0;i<=100;i++){const x=m.x.min+i*(m.x.max-m.x.min)/100,v=calculate(m,x,b);if(Number.isFinite(v))pts.push([x,v]);}
 if(!pts.length)return;let lo=Math.min(...pts.map(d=>d[1])),hi=Math.max(...pts.map(d=>d[1]));if(hi-lo<1e-12){lo-=1;hi+=1;};const margin=(hi-lo)*.08;lo-=margin;hi+=margin;
 const X=x=>48+640*(x-m.x.min)/(m.x.max-m.x.min),Y=v=>272-230*(v-lo)/(hi-lo);
 svg.replaceChildren();const ns='http://www.w3.org/2000/svg';const add=(tag,attrs,txt)=>{let n=document.createElementNS(ns,tag);for(let k in attrs)n.setAttribute(k,attrs[k]);if(txt!==undefined)n.textContent=txt;svg.appendChild(n);return n};
 add('line',{x1:48,x2:48,y1:32,y2:272,stroke:'#7594a5'});add('line',{x1:48,x2:688,y1:272,y2:272,stroke:'#7594a5'});
 add('polyline',{points:pts.map(t=>X(t[0]).toFixed(2)+','+Y(t[1]).toFixed(2)).join(' '),fill:'none',stroke:'#7ee2ca','stroke-width':3});
 if(Number.isFinite(y)){add('circle',{cx:X(a),cy:Y(y),r:6,fill:'#eac17c'});}
 add('text',{x:50,y:21,fill:'#dce9f1','font-size':13},'Range: '+fmt(lo)+' … '+fmt(hi)+' '+m.unit);
 add('text',{x:50,y:295,fill:'#c3d9e3','font-size':12},'Min '+fmt(m.x.min));add('text',{x:580,y:295,fill:'#c3d9e3','font-size':12},'Max '+fmt(m.x.max));
 if(m.id===2){const rad=Math.PI/180,q1=a*rad,q2=b*rad,l1=.30,l2=.20;const px=l1*Math.cos(q1),py=l1*Math.sin(q1),tx=px+l2*Math.cos(q1+q2),ty=py+l2*Math.sin(q1+q2);
 const toScreen=(x,y)=>[350+320*x,170-320*y];const [x0,y0]=toScreen(0,0),[x1,y1]=toScreen(px,py),[x2,y2]=toScreen(tx,ty);const arm=document.querySelector('#arm');if(arm){arm.replaceChildren();const addArm=(tag,attrs)=>{let n=document.createElementNS(ns,tag);Object.keys(attrs).forEach(k=>n.setAttribute(k,attrs[k]));arm.appendChild(n)}; addArm('line',{x1:x0,y1:y0,x2:x1,y2:y1,stroke:'#7ee2ca','stroke-width':8,'stroke-linecap':'round'});addArm('line',{x1:x1,y1:y1,x2:x2,y2:y2,stroke:'#eac17c','stroke-width':7,'stroke-linecap':'round'}); for(let pair of [[x0,y0],[x1,y1],[x2,y2]])addArm('circle',{cx:pair[0],cy:pair[1],r:7,fill:'#f6fcff'});}}
 xy.textContent=m.id===2?'The top drawing shows the planar two-link arm in the reference frame.':'Curve: response to the first input at the second input’s current setting.';
 }
 [p1,p2].forEach(el=>el.addEventListener('input',graph));graph();}
document.addEventListener('DOMContentLoaded',initialize);

    window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_MODELS = models;
    window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_CALC = typeof calculate !== 'undefined' ? calculate : null;
  })();


  OPENSTEM_SIM_MODELS.push({
    idx: 1,
    unit: 1,
    html: "<header class=\"hero\"><span class=\"chip\">Model 01 / 16</span><h3>Workspace outer reach</h3><p>Two serial planar link lengths add to an outer radial reach; joint stops may reduce attainable workspace.</p></header><div class=\"panel\"><p><strong>Relation:</strong> <code>r_max=L1+L2</code></p><div class=\"controls\"><label>link 1 length<input aria-label=\"link 1 length\" type=\"range\" id=\"p1\"><span id=\"p1value\"></span></label><label>link 2 length<input aria-label=\"link 2 length\" type=\"range\" id=\"p2\"><span id=\"p2value\"></span></label></div><p>Idealized calculated output</p><p class=\"big\" aria-live=\"polite\" id=\"answer\">\u2014</p><p class=\"notice\">This is only a geometric outer bound, not a collision-free reach.</p></div><h2>Interactive response curve</h2><svg id=\"plot\" viewBox=\"0 0 740 320\" role=\"img\" aria-label=\"Output plotted against the first input\"></svg><p id=\"xy\" class=\"muted\"></p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_MODELS;
        var calcFunc = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_CALC;
        var m = models[0];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 2,
    unit: 1,
    html: "<header class=\"hero\"><span class=\"chip\">Model 02 / 16</span><h3>Two-link arm X coordinate</h3><p>Evaluate planar 2R forward kinematics with lengths L1=0.30 m and L2=0.20 m.</p></header><div class=\"panel\"><p><strong>Relation:</strong> <code>x=.30 cos(q1)+.20 cos(q1+q2)</code></p><div class=\"controls\"><label>joint 1 angle<input aria-label=\"joint 1 angle\" type=\"range\" id=\"p1\"><span id=\"p1value\"></span></label><label>joint 2 angle<input aria-label=\"joint 2 angle\" type=\"range\" id=\"p2\"><span id=\"p2value\"></span></label></div><p>Idealized calculated output</p><p class=\"big\" aria-live=\"polite\" id=\"answer\">\u2014</p><p class=\"notice\">Joint limits and collision constraints are excluded.</p></div><h2>Interactive response curve</h2><svg id=\"plot\" viewBox=\"0 0 740 320\" role=\"img\" aria-label=\"Output plotted against the first input\"></svg><p id=\"xy\" class=\"muted\"></p><svg id=\"arm\" viewBox=\"0 0 700 320\" role=\"img\" aria-label=\"Live two-link robotic arm drawing\"></svg>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_MODELS;
        var calcFunc = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_CALC;
        var m = models[1];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 3,
    unit: 2,
    html: "<header class=\"hero\"><span class=\"chip\">Model 03 / 16</span><h3>Planar Jacobian determinant</h3><p>Use determinant to reveal the loss of locally independent Cartesian motion.</p></header><div class=\"panel\"><p><strong>Relation:</strong> <code>detJ=.30 L2 sin(q2)</code></p><div class=\"controls\"><label>elbow angle<input aria-label=\"elbow angle\" type=\"range\" id=\"p1\"><span id=\"p1value\"></span></label><label>link 2 length<input aria-label=\"link 2 length\" type=\"range\" id=\"p2\"><span id=\"p2value\"></span></label></div><p>Idealized calculated output</p><p class=\"big\" aria-live=\"polite\" id=\"answer\">\u2014</p><p class=\"notice\">Near zero determinant, inversion can amplify noise.</p></div><h2>Interactive response curve</h2><svg id=\"plot\" viewBox=\"0 0 740 320\" role=\"img\" aria-label=\"Output plotted against the first input\"></svg><p id=\"xy\" class=\"muted\"></p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_MODELS;
        var calcFunc = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_CALC;
        var m = models[2];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 4,
    unit: 2,
    html: "<header class=\"hero\"><span class=\"chip\">Model 04 / 16</span><h3>IK elbow cosine feasibility</h3><p>Monitor law-of-cosines value: absolute values over one signal unreachable targets.</p></header><div class=\"panel\"><p><strong>Relation:</strong> <code>cos(q2)=(r\u00b2-L1\u00b2-L2\u00b2)/(2 L1 L2)</code></p><div class=\"controls\"><label>radial distance<input aria-label=\"radial distance\" type=\"range\" id=\"p1\"><span id=\"p1value\"></span></label><label>second-link length<input aria-label=\"second-link length\" type=\"range\" id=\"p2\"><span id=\"p2value\"></span></label></div><p>Idealized calculated output</p><p class=\"big\" aria-live=\"polite\" id=\"answer\">\u2014</p><p class=\"notice\">Valid only if absolute value is \u22641 and physical joint limits allow solution.</p></div><h2>Interactive response curve</h2><svg id=\"plot\" viewBox=\"0 0 740 320\" role=\"img\" aria-label=\"Output plotted against the first input\"></svg><p id=\"xy\" class=\"muted\"></p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_MODELS;
        var calcFunc = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_CALC;
        var m = models[3];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 5,
    unit: 3,
    html: "<header class=\"hero\"><span class=\"chip\">Model 05 / 16</span><h3>Gear-reduced joint torque</h3><p>Simple output torque from motor torque, transmission ratio and fixed efficiency 0.8.</p></header><div class=\"panel\"><p><strong>Relation:</strong> <code>tau_out=0.8 G tau_motor</code></p><div class=\"controls\"><label>motor torque<input aria-label=\"motor torque\" type=\"range\" id=\"p1\"><span id=\"p1value\"></span></label><label>gear ratio<input aria-label=\"gear ratio\" type=\"range\" id=\"p2\"><span id=\"p2value\"></span></label></div><p>Idealized calculated output</p><p class=\"big\" aria-live=\"polite\" id=\"answer\">\u2014</p><p class=\"notice\">Do not mistake point efficiency and peak torque for continuous rating.</p></div><h2>Interactive response curve</h2><svg id=\"plot\" viewBox=\"0 0 740 320\" role=\"img\" aria-label=\"Output plotted against the first input\"></svg><p id=\"xy\" class=\"muted\"></p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_MODELS;
        var calcFunc = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_CALC;
        var m = models[4];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 6,
    unit: 3,
    html: "<header class=\"hero\"><span class=\"chip\">Model 06 / 16</span><h3>Single-link gravitational torque</h3><p>A horizontal reference makes gravitational torque magnitude m g L |cos(q)| for a lumped tip mass.</p></header><div class=\"panel\"><p><strong>Relation:</strong> <code>|tau|=m g L |cos(q)|</code></p><div class=\"controls\"><label>link angle<input aria-label=\"link angle\" type=\"range\" id=\"p1\"><span id=\"p1value\"></span></label><label>tip mass<input aria-label=\"tip mass\" type=\"range\" id=\"p2\"><span id=\"p2value\"></span></label></div><p>Idealized calculated output</p><p class=\"big\" aria-live=\"polite\" id=\"answer\">\u2014</p><p class=\"notice\">Link mass, transmission friction and acceleration are omitted.</p></div><h2>Interactive response curve</h2><svg id=\"plot\" viewBox=\"0 0 740 320\" role=\"img\" aria-label=\"Output plotted against the first input\"></svg><p id=\"xy\" class=\"muted\"></p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_MODELS;
        var calcFunc = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_CALC;
        var m = models[5];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 7,
    unit: 4,
    html: "<header class=\"hero\"><span class=\"chip\">Model 07 / 16</span><h3>Rest-to-rest motion time</h3><p>Switch between triangular and trapezoidal profiles; speed cap fixed to 1 m/s.</p></header><div class=\"panel\"><p><strong>Relation:</strong> <code>t=2 sqrt(d/a) if d\u22641/a else d+1/a</code></p><div class=\"controls\"><label>travel distance<input aria-label=\"travel distance\" type=\"range\" id=\"p1\"><span id=\"p1value\"></span></label><label>acceleration cap<input aria-label=\"acceleration cap\" type=\"range\" id=\"p2\"><span id=\"p2value\"></span></label></div><p>Idealized calculated output</p><p class=\"big\" aria-live=\"polite\" id=\"answer\">\u2014</p><p class=\"notice\">Ideal 1D travel assumes instantaneous acceleration changes and no jerk cap.</p></div><h2>Interactive response curve</h2><svg id=\"plot\" viewBox=\"0 0 740 320\" role=\"img\" aria-label=\"Output plotted against the first input\"></svg><p id=\"xy\" class=\"muted\"></p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_MODELS;
        var calcFunc = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_CALC;
        var m = models[6];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 8,
    unit: 4,
    html: "<header class=\"hero\"><span class=\"chip\">Model 08 / 16</span><h3>Jerk from acceleration ramp</h3><p>Compute average jerk as acceleration change divided by transition time.</p></header><div class=\"panel\"><p><strong>Relation:</strong> <code>j=delta_a/delta_t</code></p><div class=\"controls\"><label>acceleration change<input aria-label=\"acceleration change\" type=\"range\" id=\"p1\"><span id=\"p1value\"></span></label><label>ramp duration<input aria-label=\"ramp duration\" type=\"range\" id=\"p2\"><span id=\"p2value\"></span></label></div><p>Idealized calculated output</p><p class=\"big\" aria-live=\"polite\" id=\"answer\">\u2014</p><p class=\"notice\">Average jerk is not peak jerk for arbitrary motion profiles.</p></div><h2>Interactive response curve</h2><svg id=\"plot\" viewBox=\"0 0 740 320\" role=\"img\" aria-label=\"Output plotted against the first input\"></svg><p id=\"xy\" class=\"muted\"></p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_MODELS;
        var calcFunc = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_CALC;
        var m = models[7];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 9,
    unit: 5,
    html: "<header class=\"hero\"><span class=\"chip\">Model 09 / 16</span><h3>Differential-drive turn rate</h3><p>Right and left linear wheel speeds translate to yaw rate using a fixed 0.50 m track.</p></header><div class=\"panel\"><p><strong>Relation:</strong> <code>omega=(vR-vL)/.50</code></p><div class=\"controls\"><label>right-wheel speed<input aria-label=\"right-wheel speed\" type=\"range\" id=\"p1\"><span id=\"p1value\"></span></label><label>left-wheel speed<input aria-label=\"left-wheel speed\" type=\"range\" id=\"p2\"><span id=\"p2value\"></span></label></div><p>Idealized calculated output</p><p class=\"big\" aria-live=\"polite\" id=\"answer\">\u2014</p><p class=\"notice\">Wheel slip and geometric calibration errors can dominate.</p></div><h2>Interactive response curve</h2><svg id=\"plot\" viewBox=\"0 0 740 320\" role=\"img\" aria-label=\"Output plotted against the first input\"></svg><p id=\"xy\" class=\"muted\"></p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_MODELS;
        var calcFunc = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_CALC;
        var m = models[8];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 9:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 10,
    unit: 5,
    html: "<header class=\"hero\"><span class=\"chip\">Model 10 / 16</span><h3>Two-wheel center travel</h3><p>Estimate middle point travel using average wheel displacement.</p></header><div class=\"panel\"><p><strong>Relation:</strong> <code>Delta_s=(dsR+dsL)/2</code></p><div class=\"controls\"><label>right-wheel distance<input aria-label=\"right-wheel distance\" type=\"range\" id=\"p1\"><span id=\"p1value\"></span></label><label>left-wheel distance<input aria-label=\"left-wheel distance\" type=\"range\" id=\"p2\"><span id=\"p2value\"></span></label></div><p>Idealized calculated output</p><p class=\"big\" aria-live=\"polite\" id=\"answer\">\u2014</p><p class=\"notice\">Cannot infer absolute position without heading and initial pose.</p></div><h2>Interactive response curve</h2><svg id=\"plot\" viewBox=\"0 0 740 320\" role=\"img\" aria-label=\"Output plotted against the first input\"></svg><p id=\"xy\" class=\"muted\"></p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_MODELS;
        var calcFunc = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_CALC;
        var m = models[9];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 10:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 11,
    unit: 6,
    html: "<header class=\"hero\"><span class=\"chip\">Model 11 / 16</span><h3>Positive-detection occupancy posterior</h3><p>One Bayesian sensor update with P(z+|occupied)=0.8 and P(z+|free)=0.2.</p></header><div class=\"panel\"><p><strong>Relation:</strong> <code>p_post=TP*p/(TP*p+.20*(1-p))</code></p><div class=\"controls\"><label>prior occupancy<input aria-label=\"prior occupancy\" type=\"range\" id=\"p1\"><span id=\"p1value\"></span></label><label>true positive<input aria-label=\"true positive\" type=\"range\" id=\"p2\"><span id=\"p2value\"></span></label></div><p>Idealized calculated output</p><p class=\"big\" aria-live=\"polite\" id=\"answer\">\u2014</p><p class=\"notice\">Repeated correlated detections must not be treated as independent.</p></div><h2>Interactive response curve</h2><svg id=\"plot\" viewBox=\"0 0 740 320\" role=\"img\" aria-label=\"Output plotted against the first input\"></svg><p id=\"xy\" class=\"muted\"></p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_MODELS;
        var calcFunc = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_CALC;
        var m = models[10];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 11:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 12,
    unit: 6,
    html: "<header class=\"hero\"><span class=\"chip\">Model 12 / 16</span><h3>Localization planar error norm</h3><p>Root-mean-square style Euclidean error from two coordinate residuals.</p></header><div class=\"panel\"><p><strong>Relation:</strong> <code>error=sqrt(dx\u00b2+dy\u00b2)</code></p><div class=\"controls\"><label>x residual<input aria-label=\"x residual\" type=\"range\" id=\"p1\"><span id=\"p1value\"></span></label><label>y residual<input aria-label=\"y residual\" type=\"range\" id=\"p2\"><span id=\"p2value\"></span></label></div><p>Idealized calculated output</p><p class=\"big\" aria-live=\"polite\" id=\"answer\">\u2014</p><p class=\"notice\">A single endpoint error is not a full localization performance metric.</p></div><h2>Interactive response curve</h2><svg id=\"plot\" viewBox=\"0 0 740 320\" role=\"img\" aria-label=\"Output plotted against the first input\"></svg><p id=\"xy\" class=\"muted\"></p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_MODELS;
        var calcFunc = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_CALC;
        var m = models[11];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 12:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 13,
    unit: 7,
    html: "<header class=\"hero\"><span class=\"chip\">Model 13 / 16</span><h3>Stereo camera ideal depth</h3><p>Compute depth from disparity using f=500 px and adjustable stereo baseline.</p></header><div class=\"panel\"><p><strong>Relation:</strong> <code>Z=500 B/d</code></p><div class=\"controls\"><label>disparity<input aria-label=\"disparity\" type=\"range\" id=\"p1\"><span id=\"p1value\"></span></label><label>baseline<input aria-label=\"baseline\" type=\"range\" id=\"p2\"><span id=\"p2value\"></span></label></div><p>Idealized calculated output</p><p class=\"big\" aria-live=\"polite\" id=\"answer\">\u2014</p><p class=\"notice\">Occlusion, mismatched pixels and calibration biases invalidate ideal triangulation.</p></div><h2>Interactive response curve</h2><svg id=\"plot\" viewBox=\"0 0 740 320\" role=\"img\" aria-label=\"Output plotted against the first input\"></svg><p id=\"xy\" class=\"muted\"></p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_MODELS;
        var calcFunc = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_CALC;
        var m = models[12];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 13:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 14,
    unit: 7,
    html: "<header class=\"hero\"><span class=\"chip\">Model 14 / 16</span><h3>Ideal obstacle stopping distance</h3><p>Includes commanded speed times delay and constant-braking-distance term with deceleration fixed to 1 m/s\u00b2.</p></header><div class=\"panel\"><p><strong>Relation:</strong> <code>d=v*t+v\u00b2/2</code></p><div class=\"controls\"><label>speed<input aria-label=\"speed\" type=\"range\" id=\"p1\"><span id=\"p1value\"></span></label><label>perception + control delay<input aria-label=\"perception + control delay\" type=\"range\" id=\"p2\"><span id=\"p2value\"></span></label></div><p>Idealized calculated output</p><p class=\"big\" aria-live=\"polite\" id=\"answer\">\u2014</p><p class=\"notice\">No clearance margin, reaction uncertainty, brake fault or obstacle motion is included.</p></div><h2>Interactive response curve</h2><svg id=\"plot\" viewBox=\"0 0 740 320\" role=\"img\" aria-label=\"Output plotted against the first input\"></svg><p id=\"xy\" class=\"muted\"></p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_MODELS;
        var calcFunc = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_CALC;
        var m = models[13];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 14:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 15,
    unit: 8,
    html: "<header class=\"hero\"><span class=\"chip\">Model 15 / 16</span><h3>Exponential reliability illustration</h3><p>Use constant hazard assumption to illustrate probability of surviving time without failure.</p></header><div class=\"panel\"><p><strong>Relation:</strong> <code>R=exp(-lambda*t)</code></p><div class=\"controls\"><label>operating time<input aria-label=\"operating time\" type=\"range\" id=\"p1\"><span id=\"p1value\"></span></label><label>hazard rate<input aria-label=\"hazard rate\" type=\"range\" id=\"p2\"><span id=\"p2value\"></span></label></div><p>Idealized calculated output</p><p class=\"big\" aria-live=\"polite\" id=\"answer\">\u2014</p><p class=\"notice\">Wear-out processes generally violate constant hazard.</p></div><h2>Interactive response curve</h2><svg id=\"plot\" viewBox=\"0 0 740 320\" role=\"img\" aria-label=\"Output plotted against the first input\"></svg><p id=\"xy\" class=\"muted\"></p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_MODELS;
        var calcFunc = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_CALC;
        var m = models[14];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
      } catch (err) {
        console.warn('Sim init error in model 15:', err);
      }
    }
  });

  OPENSTEM_SIM_MODELS.push({
    idx: 16,
    unit: 8,
    html: "<header class=\"hero\"><span class=\"chip\">Model 16 / 16</span><h3>Cycle-time production rate</h3><p>Illustrative accepted units per hour with per-cycle time and productive availability.</p></header><div class=\"panel\"><p><strong>Relation:</strong> <code>rate=3600*A/t</code></p><div class=\"controls\"><label>full cycle duration<input aria-label=\"full cycle duration\" type=\"range\" id=\"p1\"><span id=\"p1value\"></span></label><label>productive fraction<input aria-label=\"productive fraction\" type=\"range\" id=\"p2\"><span id=\"p2value\"></span></label></div><p>Idealized calculated output</p><p class=\"big\" aria-live=\"polite\" id=\"answer\">\u2014</p><p class=\"notice\">Excludes rejects, variable part demand, parallel station constraints and correlated interruptions.</p></div><h2>Interactive response curve</h2><svg id=\"plot\" viewBox=\"0 0 740 320\" role=\"img\" aria-label=\"Output plotted against the first input\"></svg><p id=\"xy\" class=\"muted\"></p>",
    init: function(card) {
      try {
        var models = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_MODELS;
        var calcFunc = window.__OPENSTEM_ROBOTICS_AND_AUTOMATION_CALC;
        var m = models[15];
        if (!m) return;
        var p1 = card.querySelector('#p1'), p2 = card.querySelector('#p2');
        var display = card.querySelector('#answer');
        var svg = card.querySelector('#plot');
        var p1v = card.querySelector('#p1value'), p2v = card.querySelector('#p2value');
        
        if (p1 && m.x) {
          p1.min = m.x.min; p1.max = m.x.max; p1.step = m.x.step; p1.value = m.x.default;
        }
        if (p2 && m.z) {
          p2.min = m.z.min; p2.max = m.z.max; p2.step = m.z.step; p2.value = m.z.default;
        }

        var fmt = function(n) {
          return Number.isFinite(n) ? (Math.abs(n) < 0.0001 && n !== 0 ? n.toExponential(3) : n.toLocaleString('en-US', { maximumFractionDigits: 5 })) : 'not defined';
        };

        function updateCard() {
          var a = p1 ? Number(p1.value) : 0;
          var b = p2 ? Number(p2.value) : 0;
          var res = calcFunc ? calcFunc(m, a, b) : 0;
          if (p1v && m.x) p1v.textContent = fmt(a) + ' ' + (m.x.unit || '');
          if (p2v && m.z) p2v.textContent = fmt(b) + ' ' + (m.z.unit || '');
          if (display) display.textContent = fmt(res) + ' ' + (m.result_unit || '');

          if (svg && m.x) {
            var series = [];
            for (var step = 0; step <= 40; step++) {
              var x = m.x.min + (m.x.max - m.x.min) * step / 40;
              var y = calcFunc ? calcFunc(m, x, b) : 0;
              if (Number.isFinite(y)) series.push([x, y]);
            }
            if (series.length < 2) return;
            var ymin = Math.min.apply(null, series.map(function(p) { return p[1]; }));
            var ymax = Math.max.apply(null, series.map(function(p) { return p[1]; }));
            if (Math.abs(ymax - ymin) < 1e-10) { ymin -= 1; ymax += 1; }
            var pad = (ymax - ymin) * 0.08;
            ymin -= pad; ymax += pad;
            var X = function(val) { return 52 + 650 * (val - m.x.min) / (m.x.max - m.x.min); };
            var Y = function(val) { return 270 - 235 * (val - ymin) / (ymax - ymin); };
            var pts = series.map(function(p) { return X(p[0]).toFixed(2) + ',' + Y(p[1]).toFixed(2); }).join(' ');
            
            svg.innerHTML = '<line x1="52" y1="35" x2="52" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<line x1="52" y1="270" x2="702" y2="270" stroke="#638ca0" stroke-width="1"/>' +
              '<polyline points="' + pts + '" stroke="#80e3bd" stroke-width="3" fill="none"/>' +
              '<circle cx="' + X(a).toFixed(2) + '" cy="' + Y(res).toFixed(2) + '" r="7" fill="#f2cb85"/>' +
              '<text x="55" y="20" fill="#b9d7e4" font-size="13">Output: ' + fmt(ymax) + '</text>' +
              '<text x="55" y="289" fill="#b9d7e4" font-size="13">Min ' + fmt(m.x.min) + '</text>' +
              '<text x="568" y="289" fill="#b9d7e4" font-size="13">Max ' + fmt(m.x.max) + '</text>';
          }
        }

        if (p1) p1.addEventListener('input', updateCard);
        if (p2) p2.addEventListener('input', updateCard);
        updateCard();
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
