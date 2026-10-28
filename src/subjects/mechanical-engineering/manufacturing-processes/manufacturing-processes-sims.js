/* manufacturing-processes Interactive Simulation Suite */
(function(window) {
  'use strict';

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: "<section class=\"hero\"><span class=\"pill\">Model 01 / 16 \u00b7 editable parameters</span><h3>Tooling amortization</h3><p>Estimated tooling cost allocated per part</p></section>\n <section class=\"model\"><h2>Inputs</h2><label for=\"a\">Tooling cost: <span id=\"al\"></span> USD</label><input id=\"a\" type=\"range\" min=\"1000\" max=\"30000\" step=\"any\" value=\"12000\"><label for=\"b\">Lot size: <span id=\"bl\"></span> parts</label><input id=\"b\" type=\"range\" min=\"100\" max=\"10000\" step=\"any\" value=\"600\"><p>Predicted result <span role=\"status\" aria-live=\"polite\" id=\"value\" class=\"output\"></span></p><svg aria-label=\"Schematic bar of the modeled response against an illustrative plot maximum\" role=\"img\" class=\"plot\" viewBox=\"0 0 540 115\"><text x=\"30\" y=\"23\" fill=\"#4e7181\" font-size=\"16\">Normalized visualization (illustrative scale)</text><rect x=\"30\" y=\"47\" width=\"480\" height=\"28\" fill=\"#dce8ed\" rx=\"7\"/><rect id=\"bar\" x=\"30\" y=\"47\" width=\"0\" height=\"28\" fill=\"#1696a4\" rx=\"7\"/><circle id=\"dot\" cx=\"30\" cy=\"61\" r=\"7\" fill=\"#e4a32a\"/><text x=\"30\" y=\"102\" font-size=\"13\" fill=\"#557688\">0</text><text x=\"510\" y=\"102\" font-size=\"13\" fill=\"#557688\" text-anchor=\"end\">30 USD/part</text></svg><p class=\"small muted\">Expression: <code>a/b</code>. Results are idealized educational estimates; values beyond the illustrative scale are clipped in the bar, not in the reported number.</p></section><section class=\"callout\"><b>Limits and verification:</b> Cost/part decreases as volume increases; this omits maintenance and financing. Use calibrated equipment data and appropriate process tests before engineering release.</section>",
    init: function(card) {
      try {
const A=card.querySelector("#" + 'a'.replace(/^#/, "")),B=card.querySelector("#" + 'b'.replace(/^#/, "")),V=card.querySelector("#" + 'value'.replace(/^#/, "")),AL=card.querySelector("#" + 'al'.replace(/^#/, "")),BL=card.querySelector("#" + 'bl'.replace(/^#/, "")),BAR=card.querySelector("#" + 'bar'.replace(/^#/, "")),DOT=card.querySelector("#" + 'dot'.replace(/^#/, ""));
function compute(a,b){return a/b;}
function redraw(){let a=+A.value,b=+B.value,y=compute(a,b);AL.textContent=a.toLocaleString(undefined,{maximumFractionDigits:4});BL.textContent=b.toLocaleString(undefined,{maximumFractionDigits:4});const safe=Number.isFinite(y);V.textContent=safe?y.toLocaleString(undefined,{maximumFractionDigits:3})+' USD/part':'Out of range';V.dataset.result=String(y);let r=safe?Math.max(0,Math.min(1,y/30)):0;BAR.setAttribute('width',String(480*r));DOT.setAttribute('cx',String(30+480*r));}
A.addEventListener('input',redraw);B.addEventListener('input',redraw);redraw();
      } catch (err) {
        console.warn('Sim init error in model 1:', err);
      }
    }
  });

  MODELS.push({
    idx: 2,
    unit: 1,
    html: "<section class=\"hero\"><span class=\"pill\">Model 02 / 16 \u00b7 editable parameters</span><h3>Process capability Cp</h3><p>Capability under stable, centered normal-process assumptions</p></section>\n <section class=\"model\"><h2>Inputs</h2><label for=\"a\">Specification width: <span id=\"al\"></span> mm</label><input id=\"a\" type=\"range\" min=\"0.05\" max=\"0.3\" step=\"any\" value=\"0.12\"><label for=\"b\">Standard deviation: <span id=\"bl\"></span> mm</label><input id=\"b\" type=\"range\" min=\"0.005\" max=\"0.05\" step=\"any\" value=\"0.015\"><p>Predicted result <span role=\"status\" aria-live=\"polite\" id=\"value\" class=\"output\"></span></p><svg aria-label=\"Schematic bar of the modeled response against an illustrative plot maximum\" role=\"img\" class=\"plot\" viewBox=\"0 0 540 115\"><text x=\"30\" y=\"23\" fill=\"#4e7181\" font-size=\"16\">Normalized visualization (illustrative scale)</text><rect x=\"30\" y=\"47\" width=\"480\" height=\"28\" fill=\"#dce8ed\" rx=\"7\"/><rect id=\"bar\" x=\"30\" y=\"47\" width=\"0\" height=\"28\" fill=\"#1696a4\" rx=\"7\"/><circle id=\"dot\" cx=\"30\" cy=\"61\" r=\"7\" fill=\"#e4a32a\"/><text x=\"30\" y=\"102\" font-size=\"13\" fill=\"#557688\">0</text><text x=\"510\" y=\"102\" font-size=\"13\" fill=\"#557688\" text-anchor=\"end\">2 dimensionless</text></svg><p class=\"small muted\">Expression: <code>a/(6*b)</code>. Results are idealized educational estimates; values beyond the illustrative scale are clipped in the bar, not in the reported number.</p></section><section class=\"callout\"><b>Limits and verification:</b> A Cp result alone cannot establish centering or control. Use calibrated equipment data and appropriate process tests before engineering release.</section>",
    init: function(card) {
      try {
const A=card.querySelector("#" + 'a'.replace(/^#/, "")),B=card.querySelector("#" + 'b'.replace(/^#/, "")),V=card.querySelector("#" + 'value'.replace(/^#/, "")),AL=card.querySelector("#" + 'al'.replace(/^#/, "")),BL=card.querySelector("#" + 'bl'.replace(/^#/, "")),BAR=card.querySelector("#" + 'bar'.replace(/^#/, "")),DOT=card.querySelector("#" + 'dot'.replace(/^#/, ""));
function compute(a,b){return a/(6*b);}
function redraw(){let a=+A.value,b=+B.value,y=compute(a,b);AL.textContent=a.toLocaleString(undefined,{maximumFractionDigits:4});BL.textContent=b.toLocaleString(undefined,{maximumFractionDigits:4});const safe=Number.isFinite(y);V.textContent=safe?y.toLocaleString(undefined,{maximumFractionDigits:3})+' dimensionless':'Out of range';V.dataset.result=String(y);let r=safe?Math.max(0,Math.min(1,y/2)):0;BAR.setAttribute('width',String(480*r));DOT.setAttribute('cx',String(30+480*r));}
A.addEventListener('input',redraw);B.addEventListener('input',redraw);redraw();
      } catch (err) {
        console.warn('Sim init error in model 2:', err);
      }
    }
  });

  MODELS.push({
    idx: 3,
    unit: 2,
    html: "<section class=\"hero\"><span class=\"pill\">Model 03 / 16 \u00b7 editable parameters</span><h3>Casting fill time</h3><p>Constant-rate transfer with negligible pauses</p></section>\n <section class=\"model\"><h2>Inputs</h2><label for=\"a\">Metal mass: <span id=\"al\"></span> kg</label><input id=\"a\" type=\"range\" min=\"1\" max=\"20\" step=\"any\" value=\"3\"><label for=\"b\">Mass flow rate: <span id=\"bl\"></span> kg/s</label><input id=\"b\" type=\"range\" min=\"0.05\" max=\"2\" step=\"any\" value=\"0.25\"><p>Predicted result <span role=\"status\" aria-live=\"polite\" id=\"value\" class=\"output\"></span></p><svg aria-label=\"Schematic bar of the modeled response against an illustrative plot maximum\" role=\"img\" class=\"plot\" viewBox=\"0 0 540 115\"><text x=\"30\" y=\"23\" fill=\"#4e7181\" font-size=\"16\">Normalized visualization (illustrative scale)</text><rect x=\"30\" y=\"47\" width=\"480\" height=\"28\" fill=\"#dce8ed\" rx=\"7\"/><rect id=\"bar\" x=\"30\" y=\"47\" width=\"0\" height=\"28\" fill=\"#1696a4\" rx=\"7\"/><circle id=\"dot\" cx=\"30\" cy=\"61\" r=\"7\" fill=\"#e4a32a\"/><text x=\"30\" y=\"102\" font-size=\"13\" fill=\"#557688\">0</text><text x=\"510\" y=\"102\" font-size=\"13\" fill=\"#557688\" text-anchor=\"end\">40 s</text></svg><p class=\"small muted\">Expression: <code>a/b</code>. Results are idealized educational estimates; values beyond the illustrative scale are clipped in the bar, not in the reported number.</p></section><section class=\"callout\"><b>Limits and verification:</b> Freezing and turbulence are omitted. Use calibrated equipment data and appropriate process tests before engineering release.</section>",
    init: function(card) {
      try {
const A=card.querySelector("#" + 'a'.replace(/^#/, "")),B=card.querySelector("#" + 'b'.replace(/^#/, "")),V=card.querySelector("#" + 'value'.replace(/^#/, "")),AL=card.querySelector("#" + 'al'.replace(/^#/, "")),BL=card.querySelector("#" + 'bl'.replace(/^#/, "")),BAR=card.querySelector("#" + 'bar'.replace(/^#/, "")),DOT=card.querySelector("#" + 'dot'.replace(/^#/, ""));
function compute(a,b){return a/b;}
function redraw(){let a=+A.value,b=+B.value,y=compute(a,b);AL.textContent=a.toLocaleString(undefined,{maximumFractionDigits:4});BL.textContent=b.toLocaleString(undefined,{maximumFractionDigits:4});const safe=Number.isFinite(y);V.textContent=safe?y.toLocaleString(undefined,{maximumFractionDigits:3})+' s':'Out of range';V.dataset.result=String(y);let r=safe?Math.max(0,Math.min(1,y/40)):0;BAR.setAttribute('width',String(480*r));DOT.setAttribute('cx',String(30+480*r));}
A.addEventListener('input',redraw);B.addEventListener('input',redraw);redraw();
      } catch (err) {
        console.warn('Sim init error in model 3:', err);
      }
    }
  });

  MODELS.push({
    idx: 4,
    unit: 2,
    html: "<section class=\"hero\"><span class=\"pill\">Model 04 / 16 \u00b7 editable parameters</span><h3>Chvorinov solidification</h3><p>Empirical screening at fixed mold conditions</p></section>\n <section class=\"model\"><h2>Inputs</h2><label for=\"a\">Casting modulus V/A: <span id=\"al\"></span> cm</label><input id=\"a\" type=\"range\" min=\"0.5\" max=\"4\" step=\"any\" value=\"2\"><label for=\"b\">Mold constant B: <span id=\"bl\"></span> min/cm\u00b2</label><input id=\"b\" type=\"range\" min=\"1\" max=\"8\" step=\"any\" value=\"4\"><p>Predicted result <span role=\"status\" aria-live=\"polite\" id=\"value\" class=\"output\"></span></p><svg aria-label=\"Schematic bar of the modeled response against an illustrative plot maximum\" role=\"img\" class=\"plot\" viewBox=\"0 0 540 115\"><text x=\"30\" y=\"23\" fill=\"#4e7181\" font-size=\"16\">Normalized visualization (illustrative scale)</text><rect x=\"30\" y=\"47\" width=\"480\" height=\"28\" fill=\"#dce8ed\" rx=\"7\"/><rect id=\"bar\" x=\"30\" y=\"47\" width=\"0\" height=\"28\" fill=\"#1696a4\" rx=\"7\"/><circle id=\"dot\" cx=\"30\" cy=\"61\" r=\"7\" fill=\"#e4a32a\"/><text x=\"30\" y=\"102\" font-size=\"13\" fill=\"#557688\">0</text><text x=\"510\" y=\"102\" font-size=\"13\" fill=\"#557688\" text-anchor=\"end\">80 min</text></svg><p class=\"small muted\">Expression: <code>b*a*a</code>. Results are idealized educational estimates; values beyond the illustrative scale are clipped in the bar, not in the reported number.</p></section><section class=\"callout\"><b>Limits and verification:</b> Calibrate B for the particular alloy, mold and geometry. Use calibrated equipment data and appropriate process tests before engineering release.</section>",
    init: function(card) {
      try {
const A=card.querySelector("#" + 'a'.replace(/^#/, "")),B=card.querySelector("#" + 'b'.replace(/^#/, "")),V=card.querySelector("#" + 'value'.replace(/^#/, "")),AL=card.querySelector("#" + 'al'.replace(/^#/, "")),BL=card.querySelector("#" + 'bl'.replace(/^#/, "")),BAR=card.querySelector("#" + 'bar'.replace(/^#/, "")),DOT=card.querySelector("#" + 'dot'.replace(/^#/, ""));
function compute(a,b){return b*a*a;}
function redraw(){let a=+A.value,b=+B.value,y=compute(a,b);AL.textContent=a.toLocaleString(undefined,{maximumFractionDigits:4});BL.textContent=b.toLocaleString(undefined,{maximumFractionDigits:4});const safe=Number.isFinite(y);V.textContent=safe?y.toLocaleString(undefined,{maximumFractionDigits:3})+' min':'Out of range';V.dataset.result=String(y);let r=safe?Math.max(0,Math.min(1,y/80)):0;BAR.setAttribute('width',String(480*r));DOT.setAttribute('cx',String(30+480*r));}
A.addEventListener('input',redraw);B.addEventListener('input',redraw);redraw();
      } catch (err) {
        console.warn('Sim init error in model 4:', err);
      }
    }
  });

  MODELS.push({
    idx: 5,
    unit: 3,
    html: "<section class=\"hero\"><span class=\"pill\">Model 05 / 16 \u00b7 editable parameters</span><h3>Upset forging force</h3><p>Lower-bound force without die friction</p></section>\n <section class=\"model\"><h2>Inputs</h2><label for=\"a\">Mean flow stress: <span id=\"al\"></span> MPa</label><input id=\"a\" type=\"range\" min=\"100\" max=\"400\" step=\"any\" value=\"180\"><label for=\"b\">Contact area: <span id=\"bl\"></span> mm\u00b2</label><input id=\"b\" type=\"range\" min=\"500\" max=\"4000\" step=\"any\" value=\"1500\"><p>Predicted result <span role=\"status\" aria-live=\"polite\" id=\"value\" class=\"output\"></span></p><svg aria-label=\"Schematic bar of the modeled response against an illustrative plot maximum\" role=\"img\" class=\"plot\" viewBox=\"0 0 540 115\"><text x=\"30\" y=\"23\" fill=\"#4e7181\" font-size=\"16\">Normalized visualization (illustrative scale)</text><rect x=\"30\" y=\"47\" width=\"480\" height=\"28\" fill=\"#dce8ed\" rx=\"7\"/><rect id=\"bar\" x=\"30\" y=\"47\" width=\"0\" height=\"28\" fill=\"#1696a4\" rx=\"7\"/><circle id=\"dot\" cx=\"30\" cy=\"61\" r=\"7\" fill=\"#e4a32a\"/><text x=\"30\" y=\"102\" font-size=\"13\" fill=\"#557688\">0</text><text x=\"510\" y=\"102\" font-size=\"13\" fill=\"#557688\" text-anchor=\"end\">1000 kN</text></svg><p class=\"small muted\">Expression: <code>a*b/1000</code>. Results are idealized educational estimates; values beyond the illustrative scale are clipped in the bar, not in the reported number.</p></section><section class=\"callout\"><b>Limits and verification:</b> Press sizing also needs load-stroke history and friction. Use calibrated equipment data and appropriate process tests before engineering release.</section>",
    init: function(card) {
      try {
const A=card.querySelector("#" + 'a'.replace(/^#/, "")),B=card.querySelector("#" + 'b'.replace(/^#/, "")),V=card.querySelector("#" + 'value'.replace(/^#/, "")),AL=card.querySelector("#" + 'al'.replace(/^#/, "")),BL=card.querySelector("#" + 'bl'.replace(/^#/, "")),BAR=card.querySelector("#" + 'bar'.replace(/^#/, "")),DOT=card.querySelector("#" + 'dot'.replace(/^#/, ""));
function compute(a,b){return a*b/1000;}
function redraw(){let a=+A.value,b=+B.value,y=compute(a,b);AL.textContent=a.toLocaleString(undefined,{maximumFractionDigits:4});BL.textContent=b.toLocaleString(undefined,{maximumFractionDigits:4});const safe=Number.isFinite(y);V.textContent=safe?y.toLocaleString(undefined,{maximumFractionDigits:3})+' kN':'Out of range';V.dataset.result=String(y);let r=safe?Math.max(0,Math.min(1,y/1000)):0;BAR.setAttribute('width',String(480*r));DOT.setAttribute('cx',String(30+480*r));}
A.addEventListener('input',redraw);B.addEventListener('input',redraw);redraw();
      } catch (err) {
        console.warn('Sim init error in model 5:', err);
      }
    }
  });

  MODELS.push({
    idx: 6,
    unit: 3,
    html: "<section class=\"hero\"><span class=\"pill\">Model 06 / 16 \u00b7 editable parameters</span><h3>Extrusion true strain</h3><p>Ideal logarithmic area reduction</p></section>\n <section class=\"model\"><h2>Inputs</h2><label for=\"a\">Initial area: <span id=\"al\"></span> mm\u00b2</label><input id=\"a\" type=\"range\" min=\"200\" max=\"1200\" step=\"any\" value=\"600\"><label for=\"b\">Final area: <span id=\"bl\"></span> mm\u00b2</label><input id=\"b\" type=\"range\" min=\"50\" max=\"500\" step=\"any\" value=\"150\"><p>Predicted result <span role=\"status\" aria-live=\"polite\" id=\"value\" class=\"output\"></span></p><svg aria-label=\"Schematic bar of the modeled response against an illustrative plot maximum\" role=\"img\" class=\"plot\" viewBox=\"0 0 540 115\"><text x=\"30\" y=\"23\" fill=\"#4e7181\" font-size=\"16\">Normalized visualization (illustrative scale)</text><rect x=\"30\" y=\"47\" width=\"480\" height=\"28\" fill=\"#dce8ed\" rx=\"7\"/><rect id=\"bar\" x=\"30\" y=\"47\" width=\"0\" height=\"28\" fill=\"#1696a4\" rx=\"7\"/><circle id=\"dot\" cx=\"30\" cy=\"61\" r=\"7\" fill=\"#e4a32a\"/><text x=\"30\" y=\"102\" font-size=\"13\" fill=\"#557688\">0</text><text x=\"510\" y=\"102\" font-size=\"13\" fill=\"#557688\" text-anchor=\"end\">3 dimensionless</text></svg><p class=\"small muted\">Expression: <code>Math.log(a/b)</code>. Results are idealized educational estimates; values beyond the illustrative scale are clipped in the bar, not in the reported number.</p></section><section class=\"callout\"><b>Limits and verification:</b> Valid only when final area is smaller than the starting area; negative outputs denote expansion. Use calibrated equipment data and appropriate process tests before engineering release.</section>",
    init: function(card) {
      try {
const A=card.querySelector("#" + 'a'.replace(/^#/, "")),B=card.querySelector("#" + 'b'.replace(/^#/, "")),V=card.querySelector("#" + 'value'.replace(/^#/, "")),AL=card.querySelector("#" + 'al'.replace(/^#/, "")),BL=card.querySelector("#" + 'bl'.replace(/^#/, "")),BAR=card.querySelector("#" + 'bar'.replace(/^#/, "")),DOT=card.querySelector("#" + 'dot'.replace(/^#/, ""));
function compute(a,b){return Math.log(a/b);}
function redraw(){let a=+A.value,b=+B.value,y=compute(a,b);AL.textContent=a.toLocaleString(undefined,{maximumFractionDigits:4});BL.textContent=b.toLocaleString(undefined,{maximumFractionDigits:4});const safe=Number.isFinite(y);V.textContent=safe?y.toLocaleString(undefined,{maximumFractionDigits:3})+' dimensionless':'Out of range';V.dataset.result=String(y);let r=safe?Math.max(0,Math.min(1,y/3)):0;BAR.setAttribute('width',String(480*r));DOT.setAttribute('cx',String(30+480*r));}
A.addEventListener('input',redraw);B.addEventListener('input',redraw);redraw();
      } catch (err) {
        console.warn('Sim init error in model 6:', err);
      }
    }
  });

  MODELS.push({
    idx: 7,
    unit: 4,
    html: "<section class=\"hero\"><span class=\"pill\">Model 07 / 16 \u00b7 editable parameters</span><h3>Turning cutting speed</h3><p>Surface speed of a rotating cylinder</p></section>\n <section class=\"model\"><h2>Inputs</h2><label for=\"a\">Diameter: <span id=\"al\"></span> mm</label><input id=\"a\" type=\"range\" min=\"10\" max=\"150\" step=\"any\" value=\"50\"><label for=\"b\">Spindle speed: <span id=\"bl\"></span> rev/min</label><input id=\"b\" type=\"range\" min=\"100\" max=\"2000\" step=\"any\" value=\"600\"><p>Predicted result <span role=\"status\" aria-live=\"polite\" id=\"value\" class=\"output\"></span></p><svg aria-label=\"Schematic bar of the modeled response against an illustrative plot maximum\" role=\"img\" class=\"plot\" viewBox=\"0 0 540 115\"><text x=\"30\" y=\"23\" fill=\"#4e7181\" font-size=\"16\">Normalized visualization (illustrative scale)</text><rect x=\"30\" y=\"47\" width=\"480\" height=\"28\" fill=\"#dce8ed\" rx=\"7\"/><rect id=\"bar\" x=\"30\" y=\"47\" width=\"0\" height=\"28\" fill=\"#1696a4\" rx=\"7\"/><circle id=\"dot\" cx=\"30\" cy=\"61\" r=\"7\" fill=\"#e4a32a\"/><text x=\"30\" y=\"102\" font-size=\"13\" fill=\"#557688\">0</text><text x=\"510\" y=\"102\" font-size=\"13\" fill=\"#557688\" text-anchor=\"end\">700 m/min</text></svg><p class=\"small muted\">Expression: <code>Math.PI*a*b/1000</code>. Results are idealized educational estimates; values beyond the illustrative scale are clipped in the bar, not in the reported number.</p></section><section class=\"callout\"><b>Limits and verification:</b> Speed alone is not a tool-life recommendation. Use calibrated equipment data and appropriate process tests before engineering release.</section>",
    init: function(card) {
      try {
const A=card.querySelector("#" + 'a'.replace(/^#/, "")),B=card.querySelector("#" + 'b'.replace(/^#/, "")),V=card.querySelector("#" + 'value'.replace(/^#/, "")),AL=card.querySelector("#" + 'al'.replace(/^#/, "")),BL=card.querySelector("#" + 'bl'.replace(/^#/, "")),BAR=card.querySelector("#" + 'bar'.replace(/^#/, "")),DOT=card.querySelector("#" + 'dot'.replace(/^#/, ""));
function compute(a,b){return Math.PI*a*b/1000;}
function redraw(){let a=+A.value,b=+B.value,y=compute(a,b);AL.textContent=a.toLocaleString(undefined,{maximumFractionDigits:4});BL.textContent=b.toLocaleString(undefined,{maximumFractionDigits:4});const safe=Number.isFinite(y);V.textContent=safe?y.toLocaleString(undefined,{maximumFractionDigits:3})+' m/min':'Out of range';V.dataset.result=String(y);let r=safe?Math.max(0,Math.min(1,y/700)):0;BAR.setAttribute('width',String(480*r));DOT.setAttribute('cx',String(30+480*r));}
A.addEventListener('input',redraw);B.addEventListener('input',redraw);redraw();
      } catch (err) {
        console.warn('Sim init error in model 7:', err);
      }
    }
  });

  MODELS.push({
    idx: 8,
    unit: 4,
    html: "<section class=\"hero\"><span class=\"pill\">Model 08 / 16 \u00b7 editable parameters</span><h3>Milling removal rate</h3><p>Nominal rectangular engagement</p></section>\n <section class=\"model\"><h2>Inputs</h2><label for=\"a\">Axial depth: <span id=\"al\"></span> mm</label><input id=\"a\" type=\"range\" min=\"0.5\" max=\"10\" step=\"any\" value=\"2\"><label for=\"b\">Table feed: <span id=\"bl\"></span> mm/min</label><input id=\"b\" type=\"range\" min=\"100\" max=\"2000\" step=\"any\" value=\"350\"><p>Predicted result <span role=\"status\" aria-live=\"polite\" id=\"value\" class=\"output\"></span></p><svg aria-label=\"Schematic bar of the modeled response against an illustrative plot maximum\" role=\"img\" class=\"plot\" viewBox=\"0 0 540 115\"><text x=\"30\" y=\"23\" fill=\"#4e7181\" font-size=\"16\">Normalized visualization (illustrative scale)</text><rect x=\"30\" y=\"47\" width=\"480\" height=\"28\" fill=\"#dce8ed\" rx=\"7\"/><rect id=\"bar\" x=\"30\" y=\"47\" width=\"0\" height=\"28\" fill=\"#1696a4\" rx=\"7\"/><circle id=\"dot\" cx=\"30\" cy=\"61\" r=\"7\" fill=\"#e4a32a\"/><text x=\"30\" y=\"102\" font-size=\"13\" fill=\"#557688\">0</text><text x=\"510\" y=\"102\" font-size=\"13\" fill=\"#557688\" text-anchor=\"end\">250 cm\u00b3/min</text></svg><p class=\"small muted\">Expression: <code>a*12*b/1000</code>. Results are idealized educational estimates; values beyond the illustrative scale are clipped in the bar, not in the reported number.</p></section><section class=\"callout\"><b>Limits and verification:</b> Assumes fixed radial engagement of 12 mm and steady cutting. Use calibrated equipment data and appropriate process tests before engineering release.</section>",
    init: function(card) {
      try {
const A=card.querySelector("#" + 'a'.replace(/^#/, "")),B=card.querySelector("#" + 'b'.replace(/^#/, "")),V=card.querySelector("#" + 'value'.replace(/^#/, "")),AL=card.querySelector("#" + 'al'.replace(/^#/, "")),BL=card.querySelector("#" + 'bl'.replace(/^#/, "")),BAR=card.querySelector("#" + 'bar'.replace(/^#/, "")),DOT=card.querySelector("#" + 'dot'.replace(/^#/, ""));
function compute(a,b){return a*12*b/1000;}
function redraw(){let a=+A.value,b=+B.value,y=compute(a,b);AL.textContent=a.toLocaleString(undefined,{maximumFractionDigits:4});BL.textContent=b.toLocaleString(undefined,{maximumFractionDigits:4});const safe=Number.isFinite(y);V.textContent=safe?y.toLocaleString(undefined,{maximumFractionDigits:3})+' cm³/min':'Out of range';V.dataset.result=String(y);let r=safe?Math.max(0,Math.min(1,y/250)):0;BAR.setAttribute('width',String(480*r));DOT.setAttribute('cx',String(30+480*r));}
A.addEventListener('input',redraw);B.addEventListener('input',redraw);redraw();
      } catch (err) {
        console.warn('Sim init error in model 8:', err);
      }
    }
  });

  MODELS.push({
    idx: 9,
    unit: 5,
    html: "<section class=\"hero\"><span class=\"pill\">Model 09 / 16 \u00b7 editable parameters</span><h3>Sintering linear shrinkage</h3><p>Uniform change in a reference dimension</p></section>\n <section class=\"model\"><h2>Inputs</h2><label for=\"a\">Green length: <span id=\"al\"></span> mm</label><input id=\"a\" type=\"range\" min=\"20\" max=\"80\" step=\"any\" value=\"50\"><label for=\"b\">Fired length: <span id=\"bl\"></span> mm</label><input id=\"b\" type=\"range\" min=\"10\" max=\"75\" step=\"any\" value=\"45\"><p>Predicted result <span role=\"status\" aria-live=\"polite\" id=\"value\" class=\"output\"></span></p><svg aria-label=\"Schematic bar of the modeled response against an illustrative plot maximum\" role=\"img\" class=\"plot\" viewBox=\"0 0 540 115\"><text x=\"30\" y=\"23\" fill=\"#4e7181\" font-size=\"16\">Normalized visualization (illustrative scale)</text><rect x=\"30\" y=\"47\" width=\"480\" height=\"28\" fill=\"#dce8ed\" rx=\"7\"/><rect id=\"bar\" x=\"30\" y=\"47\" width=\"0\" height=\"28\" fill=\"#1696a4\" rx=\"7\"/><circle id=\"dot\" cx=\"30\" cy=\"61\" r=\"7\" fill=\"#e4a32a\"/><text x=\"30\" y=\"102\" font-size=\"13\" fill=\"#557688\">0</text><text x=\"510\" y=\"102\" font-size=\"13\" fill=\"#557688\" text-anchor=\"end\">35 %</text></svg><p class=\"small muted\">Expression: <code>100*(a-b)/a</code>. Results are idealized educational estimates; values beyond the illustrative scale are clipped in the bar, not in the reported number.</p></section><section class=\"callout\"><b>Limits and verification:</b> Nonuniform shrinkage and distortion may control final defects. Use calibrated equipment data and appropriate process tests before engineering release.</section>",
    init: function(card) {
      try {
const A=card.querySelector("#" + 'a'.replace(/^#/, "")),B=card.querySelector("#" + 'b'.replace(/^#/, "")),V=card.querySelector("#" + 'value'.replace(/^#/, "")),AL=card.querySelector("#" + 'al'.replace(/^#/, "")),BL=card.querySelector("#" + 'bl'.replace(/^#/, "")),BAR=card.querySelector("#" + 'bar'.replace(/^#/, "")),DOT=card.querySelector("#" + 'dot'.replace(/^#/, ""));
function compute(a,b){return 100*(a-b)/a;}
function redraw(){let a=+A.value,b=+B.value,y=compute(a,b);AL.textContent=a.toLocaleString(undefined,{maximumFractionDigits:4});BL.textContent=b.toLocaleString(undefined,{maximumFractionDigits:4});const safe=Number.isFinite(y);V.textContent=safe?y.toLocaleString(undefined,{maximumFractionDigits:3})+' %':'Out of range';V.dataset.result=String(y);let r=safe?Math.max(0,Math.min(1,y/35)):0;BAR.setAttribute('width',String(480*r));DOT.setAttribute('cx',String(30+480*r));}
A.addEventListener('input',redraw);B.addEventListener('input',redraw);redraw();
      } catch (err) {
        console.warn('Sim init error in model 9:', err);
      }
    }
  });

  MODELS.push({
    idx: 10,
    unit: 5,
    html: "<section class=\"hero\"><span class=\"pill\">Model 10 / 16 \u00b7 editable parameters</span><h3>Laser volume energy density</h3><p>Simple LPBF normalized energy metric</p></section>\n <section class=\"model\"><h2>Inputs</h2><label for=\"a\">Laser power: <span id=\"al\"></span> W</label><input id=\"a\" type=\"range\" min=\"80\" max=\"400\" step=\"any\" value=\"200\"><label for=\"b\">Scan speed: <span id=\"bl\"></span> mm/s</label><input id=\"b\" type=\"range\" min=\"250\" max=\"1600\" step=\"any\" value=\"800\"><p>Predicted result <span role=\"status\" aria-live=\"polite\" id=\"value\" class=\"output\"></span></p><svg aria-label=\"Schematic bar of the modeled response against an illustrative plot maximum\" role=\"img\" class=\"plot\" viewBox=\"0 0 540 115\"><text x=\"30\" y=\"23\" fill=\"#4e7181\" font-size=\"16\">Normalized visualization (illustrative scale)</text><rect x=\"30\" y=\"47\" width=\"480\" height=\"28\" fill=\"#dce8ed\" rx=\"7\"/><rect id=\"bar\" x=\"30\" y=\"47\" width=\"0\" height=\"28\" fill=\"#1696a4\" rx=\"7\"/><circle id=\"dot\" cx=\"30\" cy=\"61\" r=\"7\" fill=\"#e4a32a\"/><text x=\"30\" y=\"102\" font-size=\"13\" fill=\"#557688\">0</text><text x=\"510\" y=\"102\" font-size=\"13\" fill=\"#557688\" text-anchor=\"end\">130 J/mm\u00b3</text></svg><p class=\"small muted\">Expression: <code>a/(b*.12*.04)</code>. Results are idealized educational estimates; values beyond the illustrative scale are clipped in the bar, not in the reported number.</p></section><section class=\"callout\"><b>Limits and verification:</b> Fixed hatch 0.12 mm and layer 0.04 mm; not a universal process-quality criterion. Use calibrated equipment data and appropriate process tests before engineering release.</section>",
    init: function(card) {
      try {
const A=card.querySelector("#" + 'a'.replace(/^#/, "")),B=card.querySelector("#" + 'b'.replace(/^#/, "")),V=card.querySelector("#" + 'value'.replace(/^#/, "")),AL=card.querySelector("#" + 'al'.replace(/^#/, "")),BL=card.querySelector("#" + 'bl'.replace(/^#/, "")),BAR=card.querySelector("#" + 'bar'.replace(/^#/, "")),DOT=card.querySelector("#" + 'dot'.replace(/^#/, ""));
function compute(a,b){return a/(b*.12*.04);}
function redraw(){let a=+A.value,b=+B.value,y=compute(a,b);AL.textContent=a.toLocaleString(undefined,{maximumFractionDigits:4});BL.textContent=b.toLocaleString(undefined,{maximumFractionDigits:4});const safe=Number.isFinite(y);V.textContent=safe?y.toLocaleString(undefined,{maximumFractionDigits:3})+' J/mm³':'Out of range';V.dataset.result=String(y);let r=safe?Math.max(0,Math.min(1,y/130)):0;BAR.setAttribute('width',String(480*r));DOT.setAttribute('cx',String(30+480*r));}
A.addEventListener('input',redraw);B.addEventListener('input',redraw);redraw();
      } catch (err) {
        console.warn('Sim init error in model 10:', err);
      }
    }
  });

  MODELS.push({
    idx: 11,
    unit: 6,
    html: "<section class=\"hero\"><span class=\"pill\">Model 11 / 16 \u00b7 editable parameters</span><h3>Mold fill time</h3><p>Constant volume flow during initial polymer injection</p></section>\n <section class=\"model\"><h2>Inputs</h2><label for=\"a\">Shot volume: <span id=\"al\"></span> cm\u00b3</label><input id=\"a\" type=\"range\" min=\"50\" max=\"300\" step=\"any\" value=\"120\"><label for=\"b\">Injection rate: <span id=\"bl\"></span> cm\u00b3/s</label><input id=\"b\" type=\"range\" min=\"15\" max=\"120\" step=\"any\" value=\"40\"><p>Predicted result <span role=\"status\" aria-live=\"polite\" id=\"value\" class=\"output\"></span></p><svg aria-label=\"Schematic bar of the modeled response against an illustrative plot maximum\" role=\"img\" class=\"plot\" viewBox=\"0 0 540 115\"><text x=\"30\" y=\"23\" fill=\"#4e7181\" font-size=\"16\">Normalized visualization (illustrative scale)</text><rect x=\"30\" y=\"47\" width=\"480\" height=\"28\" fill=\"#dce8ed\" rx=\"7\"/><rect id=\"bar\" x=\"30\" y=\"47\" width=\"0\" height=\"28\" fill=\"#1696a4\" rx=\"7\"/><circle id=\"dot\" cx=\"30\" cy=\"61\" r=\"7\" fill=\"#e4a32a\"/><text x=\"30\" y=\"102\" font-size=\"13\" fill=\"#557688\">0</text><text x=\"510\" y=\"102\" font-size=\"13\" fill=\"#557688\" text-anchor=\"end\">20 s</text></svg><p class=\"small muted\">Expression: <code>a/b</code>. Results are idealized educational estimates; values beyond the illustrative scale are clipped in the bar, not in the reported number.</p></section><section class=\"callout\"><b>Limits and verification:</b> Packing, cooling and melt rheology are excluded. Use calibrated equipment data and appropriate process tests before engineering release.</section>",
    init: function(card) {
      try {
const A=card.querySelector("#" + 'a'.replace(/^#/, "")),B=card.querySelector("#" + 'b'.replace(/^#/, "")),V=card.querySelector("#" + 'value'.replace(/^#/, "")),AL=card.querySelector("#" + 'al'.replace(/^#/, "")),BL=card.querySelector("#" + 'bl'.replace(/^#/, "")),BAR=card.querySelector("#" + 'bar'.replace(/^#/, "")),DOT=card.querySelector("#" + 'dot'.replace(/^#/, ""));
function compute(a,b){return a/b;}
function redraw(){let a=+A.value,b=+B.value,y=compute(a,b);AL.textContent=a.toLocaleString(undefined,{maximumFractionDigits:4});BL.textContent=b.toLocaleString(undefined,{maximumFractionDigits:4});const safe=Number.isFinite(y);V.textContent=safe?y.toLocaleString(undefined,{maximumFractionDigits:3})+' s':'Out of range';V.dataset.result=String(y);let r=safe?Math.max(0,Math.min(1,y/20)):0;BAR.setAttribute('width',String(480*r));DOT.setAttribute('cx',String(30+480*r));}
A.addEventListener('input',redraw);B.addEventListener('input',redraw);redraw();
      } catch (err) {
        console.warn('Sim init error in model 11:', err);
      }
    }
  });

  MODELS.push({
    idx: 12,
    unit: 6,
    html: "<section class=\"hero\"><span class=\"pill\">Model 12 / 16 \u00b7 editable parameters</span><h3>Weld heat input</h3><p>Estimated delivered arc energy per weld length</p></section>\n <section class=\"model\"><h2>Inputs</h2><label for=\"a\">Arc voltage: <span id=\"al\"></span> V</label><input id=\"a\" type=\"range\" min=\"12\" max=\"38\" step=\"any\" value=\"22\"><label for=\"b\">Travel speed: <span id=\"bl\"></span> mm/s</label><input id=\"b\" type=\"range\" min=\"2\" max=\"15\" step=\"any\" value=\"5\"><p>Predicted result <span role=\"status\" aria-live=\"polite\" id=\"value\" class=\"output\"></span></p><svg aria-label=\"Schematic bar of the modeled response against an illustrative plot maximum\" role=\"img\" class=\"plot\" viewBox=\"0 0 540 115\"><text x=\"30\" y=\"23\" fill=\"#4e7181\" font-size=\"16\">Normalized visualization (illustrative scale)</text><rect x=\"30\" y=\"47\" width=\"480\" height=\"28\" fill=\"#dce8ed\" rx=\"7\"/><rect id=\"bar\" x=\"30\" y=\"47\" width=\"0\" height=\"28\" fill=\"#1696a4\" rx=\"7\"/><circle id=\"dot\" cx=\"30\" cy=\"61\" r=\"7\" fill=\"#e4a32a\"/><text x=\"30\" y=\"102\" font-size=\"13\" fill=\"#557688\">0</text><text x=\"510\" y=\"102\" font-size=\"13\" fill=\"#557688\" text-anchor=\"end\">2000 J/mm</text></svg><p class=\"small muted\">Expression: <code>0.8*a*180/b</code>. Results are idealized educational estimates; values beyond the illustrative scale are clipped in the bar, not in the reported number.</p></section><section class=\"callout\"><b>Limits and verification:</b> Assumes 180 A current and a constant 80% efficiency. Use calibrated equipment data and appropriate process tests before engineering release.</section>",
    init: function(card) {
      try {
const A=card.querySelector("#" + 'a'.replace(/^#/, "")),B=card.querySelector("#" + 'b'.replace(/^#/, "")),V=card.querySelector("#" + 'value'.replace(/^#/, "")),AL=card.querySelector("#" + 'al'.replace(/^#/, "")),BL=card.querySelector("#" + 'bl'.replace(/^#/, "")),BAR=card.querySelector("#" + 'bar'.replace(/^#/, "")),DOT=card.querySelector("#" + 'dot'.replace(/^#/, ""));
function compute(a,b){return 0.8*a*180/b;}
function redraw(){let a=+A.value,b=+B.value,y=compute(a,b);AL.textContent=a.toLocaleString(undefined,{maximumFractionDigits:4});BL.textContent=b.toLocaleString(undefined,{maximumFractionDigits:4});const safe=Number.isFinite(y);V.textContent=safe?y.toLocaleString(undefined,{maximumFractionDigits:3})+' J/mm':'Out of range';V.dataset.result=String(y);let r=safe?Math.max(0,Math.min(1,y/2000)):0;BAR.setAttribute('width',String(480*r));DOT.setAttribute('cx',String(30+480*r));}
A.addEventListener('input',redraw);B.addEventListener('input',redraw);redraw();
      } catch (err) {
        console.warn('Sim init error in model 12:', err);
      }
    }
  });

  MODELS.push({
    idx: 13,
    unit: 7,
    html: "<section class=\"hero\"><span class=\"pill\">Model 13 / 16 \u00b7 editable parameters</span><h3>Gauge uncertainty budget</h3><p>Root-sum-square for independent standard uncertainties</p></section>\n <section class=\"model\"><h2>Inputs</h2><label for=\"a\">Instrument standard u: <span id=\"al\"></span> mm</label><input id=\"a\" type=\"range\" min=\"0.001\" max=\"0.03\" step=\"any\" value=\"0.006\"><label for=\"b\">Operator standard u: <span id=\"bl\"></span> mm</label><input id=\"b\" type=\"range\" min=\"0.001\" max=\"0.03\" step=\"any\" value=\"0.008\"><p>Predicted result <span role=\"status\" aria-live=\"polite\" id=\"value\" class=\"output\"></span></p><svg aria-label=\"Schematic bar of the modeled response against an illustrative plot maximum\" role=\"img\" class=\"plot\" viewBox=\"0 0 540 115\"><text x=\"30\" y=\"23\" fill=\"#4e7181\" font-size=\"16\">Normalized visualization (illustrative scale)</text><rect x=\"30\" y=\"47\" width=\"480\" height=\"28\" fill=\"#dce8ed\" rx=\"7\"/><rect id=\"bar\" x=\"30\" y=\"47\" width=\"0\" height=\"28\" fill=\"#1696a4\" rx=\"7\"/><circle id=\"dot\" cx=\"30\" cy=\"61\" r=\"7\" fill=\"#e4a32a\"/><text x=\"30\" y=\"102\" font-size=\"13\" fill=\"#557688\">0</text><text x=\"510\" y=\"102\" font-size=\"13\" fill=\"#557688\" text-anchor=\"end\">0.045 mm</text></svg><p class=\"small muted\">Expression: <code>Math.sqrt(a*a+b*b)</code>. Results are idealized educational estimates; values beyond the illustrative scale are clipped in the bar, not in the reported number.</p></section><section class=\"callout\"><b>Limits and verification:</b> Correlations and temperature effects require separate treatment. Use calibrated equipment data and appropriate process tests before engineering release.</section>",
    init: function(card) {
      try {
const A=card.querySelector("#" + 'a'.replace(/^#/, "")),B=card.querySelector("#" + 'b'.replace(/^#/, "")),V=card.querySelector("#" + 'value'.replace(/^#/, "")),AL=card.querySelector("#" + 'al'.replace(/^#/, "")),BL=card.querySelector("#" + 'bl'.replace(/^#/, "")),BAR=card.querySelector("#" + 'bar'.replace(/^#/, "")),DOT=card.querySelector("#" + 'dot'.replace(/^#/, ""));
function compute(a,b){return Math.sqrt(a*a+b*b);}
function redraw(){let a=+A.value,b=+B.value,y=compute(a,b);AL.textContent=a.toLocaleString(undefined,{maximumFractionDigits:4});BL.textContent=b.toLocaleString(undefined,{maximumFractionDigits:4});const safe=Number.isFinite(y);V.textContent=safe?y.toLocaleString(undefined,{maximumFractionDigits:3})+' mm':'Out of range';V.dataset.result=String(y);let r=safe?Math.max(0,Math.min(1,y/0.045)):0;BAR.setAttribute('width',String(480*r));DOT.setAttribute('cx',String(30+480*r));}
A.addEventListener('input',redraw);B.addEventListener('input',redraw);redraw();
      } catch (err) {
        console.warn('Sim init error in model 13:', err);
      }
    }
  });

  MODELS.push({
    idx: 14,
    unit: 7,
    html: "<section class=\"hero\"><span class=\"pill\">Model 14 / 16 \u00b7 editable parameters</span><h3>Accepted material yield</h3><p>Material output normalized by input for one declared boundary</p></section>\n <section class=\"model\"><h2>Inputs</h2><label for=\"a\">Accepted mass: <span id=\"al\"></span> kg</label><input id=\"a\" type=\"range\" min=\"20\" max=\"90\" step=\"any\" value=\"76\"><label for=\"b\">Input material mass: <span id=\"bl\"></span> kg</label><input id=\"b\" type=\"range\" min=\"70\" max=\"150\" step=\"any\" value=\"100\"><p>Predicted result <span role=\"status\" aria-live=\"polite\" id=\"value\" class=\"output\"></span></p><svg aria-label=\"Schematic bar of the modeled response against an illustrative plot maximum\" role=\"img\" class=\"plot\" viewBox=\"0 0 540 115\"><text x=\"30\" y=\"23\" fill=\"#4e7181\" font-size=\"16\">Normalized visualization (illustrative scale)</text><rect x=\"30\" y=\"47\" width=\"480\" height=\"28\" fill=\"#dce8ed\" rx=\"7\"/><rect id=\"bar\" x=\"30\" y=\"47\" width=\"0\" height=\"28\" fill=\"#1696a4\" rx=\"7\"/><circle id=\"dot\" cx=\"30\" cy=\"61\" r=\"7\" fill=\"#e4a32a\"/><text x=\"30\" y=\"102\" font-size=\"13\" fill=\"#557688\">0</text><text x=\"510\" y=\"102\" font-size=\"13\" fill=\"#557688\" text-anchor=\"end\">120 %</text></svg><p class=\"small muted\">Expression: <code>100*a/b</code>. Results are idealized educational estimates; values beyond the illustrative scale are clipped in the bar, not in the reported number.</p></section><section class=\"callout\"><b>Limits and verification:</b> A value above 100% indicates inconsistent mass accounting. Use calibrated equipment data and appropriate process tests before engineering release.</section>",
    init: function(card) {
      try {
const A=card.querySelector("#" + 'a'.replace(/^#/, "")),B=card.querySelector("#" + 'b'.replace(/^#/, "")),V=card.querySelector("#" + 'value'.replace(/^#/, "")),AL=card.querySelector("#" + 'al'.replace(/^#/, "")),BL=card.querySelector("#" + 'bl'.replace(/^#/, "")),BAR=card.querySelector("#" + 'bar'.replace(/^#/, "")),DOT=card.querySelector("#" + 'dot'.replace(/^#/, ""));
function compute(a,b){return 100*a/b;}
function redraw(){let a=+A.value,b=+B.value,y=compute(a,b);AL.textContent=a.toLocaleString(undefined,{maximumFractionDigits:4});BL.textContent=b.toLocaleString(undefined,{maximumFractionDigits:4});const safe=Number.isFinite(y);V.textContent=safe?y.toLocaleString(undefined,{maximumFractionDigits:3})+' %':'Out of range';V.dataset.result=String(y);let r=safe?Math.max(0,Math.min(1,y/120)):0;BAR.setAttribute('width',String(480*r));DOT.setAttribute('cx',String(30+480*r));}
A.addEventListener('input',redraw);B.addEventListener('input',redraw);redraw();
      } catch (err) {
        console.warn('Sim init error in model 14:', err);
      }
    }
  });

  MODELS.push({
    idx: 15,
    unit: 8,
    html: "<section class=\"hero\"><span class=\"pill\">Model 15 / 16 \u00b7 editable parameters</span><h3>Little law production WIP</h3><p>Average work in process under steady-state flow</p></section>\n <section class=\"model\"><h2>Inputs</h2><label for=\"a\">Throughput: <span id=\"al\"></span> parts/hour</label><input id=\"a\" type=\"range\" min=\"10\" max=\"120\" step=\"any\" value=\"48\"><label for=\"b\">Mean flow time: <span id=\"bl\"></span> hours</label><input id=\"b\" type=\"range\" min=\"0.2\" max=\"4\" step=\"any\" value=\"1.5\"><p>Predicted result <span role=\"status\" aria-live=\"polite\" id=\"value\" class=\"output\"></span></p><svg aria-label=\"Schematic bar of the modeled response against an illustrative plot maximum\" role=\"img\" class=\"plot\" viewBox=\"0 0 540 115\"><text x=\"30\" y=\"23\" fill=\"#4e7181\" font-size=\"16\">Normalized visualization (illustrative scale)</text><rect x=\"30\" y=\"47\" width=\"480\" height=\"28\" fill=\"#dce8ed\" rx=\"7\"/><rect id=\"bar\" x=\"30\" y=\"47\" width=\"0\" height=\"28\" fill=\"#1696a4\" rx=\"7\"/><circle id=\"dot\" cx=\"30\" cy=\"61\" r=\"7\" fill=\"#e4a32a\"/><text x=\"30\" y=\"102\" font-size=\"13\" fill=\"#557688\">0</text><text x=\"510\" y=\"102\" font-size=\"13\" fill=\"#557688\" text-anchor=\"end\">400 parts</text></svg><p class=\"small muted\">Expression: <code>a*b</code>. Results are idealized educational estimates; values beyond the illustrative scale are clipped in the bar, not in the reported number.</p></section><section class=\"callout\"><b>Limits and verification:</b> Do not apply blindly to unstable transient production. Use calibrated equipment data and appropriate process tests before engineering release.</section>",
    init: function(card) {
      try {
const A=card.querySelector("#" + 'a'.replace(/^#/, "")),B=card.querySelector("#" + 'b'.replace(/^#/, "")),V=card.querySelector("#" + 'value'.replace(/^#/, "")),AL=card.querySelector("#" + 'al'.replace(/^#/, "")),BL=card.querySelector("#" + 'bl'.replace(/^#/, "")),BAR=card.querySelector("#" + 'bar'.replace(/^#/, "")),DOT=card.querySelector("#" + 'dot'.replace(/^#/, ""));
function compute(a,b){return a*b;}
function redraw(){let a=+A.value,b=+B.value,y=compute(a,b);AL.textContent=a.toLocaleString(undefined,{maximumFractionDigits:4});BL.textContent=b.toLocaleString(undefined,{maximumFractionDigits:4});const safe=Number.isFinite(y);V.textContent=safe?y.toLocaleString(undefined,{maximumFractionDigits:3})+' parts':'Out of range';V.dataset.result=String(y);let r=safe?Math.max(0,Math.min(1,y/400)):0;BAR.setAttribute('width',String(480*r));DOT.setAttribute('cx',String(30+480*r));}
A.addEventListener('input',redraw);B.addEventListener('input',redraw);redraw();
      } catch (err) {
        console.warn('Sim init error in model 15:', err);
      }
    }
  });

  MODELS.push({
    idx: 16,
    unit: 8,
    html: "<section class=\"hero\"><span class=\"pill\">Model 16 / 16 \u00b7 editable parameters</span><h3>Taylor cutting tool life</h3><p>Empirical Taylor speed-life relation at fixed n and C</p></section>\n <section class=\"model\"><h2>Inputs</h2><label for=\"a\">Cutting speed: <span id=\"al\"></span> m/min</label><input id=\"a\" type=\"range\" min=\"90\" max=\"260\" step=\"any\" value=\"160\"><label for=\"b\">Taylor constant C: <span id=\"bl\"></span> m/min \u00b7 min^n</label><input id=\"b\" type=\"range\" min=\"200\" max=\"450\" step=\"any\" value=\"320\"><p>Predicted result <span role=\"status\" aria-live=\"polite\" id=\"value\" class=\"output\"></span></p><svg aria-label=\"Schematic bar of the modeled response against an illustrative plot maximum\" role=\"img\" class=\"plot\" viewBox=\"0 0 540 115\"><text x=\"30\" y=\"23\" fill=\"#4e7181\" font-size=\"16\">Normalized visualization (illustrative scale)</text><rect x=\"30\" y=\"47\" width=\"480\" height=\"28\" fill=\"#dce8ed\" rx=\"7\"/><rect id=\"bar\" x=\"30\" y=\"47\" width=\"0\" height=\"28\" fill=\"#1696a4\" rx=\"7\"/><circle id=\"dot\" cx=\"30\" cy=\"61\" r=\"7\" fill=\"#e4a32a\"/><text x=\"30\" y=\"102\" font-size=\"13\" fill=\"#557688\">0</text><text x=\"510\" y=\"102\" font-size=\"13\" fill=\"#557688\" text-anchor=\"end\">500 min</text></svg><p class=\"small muted\">Expression: <code>Math.pow(b/a,4)</code>. Results are idealized educational estimates; values beyond the illustrative scale are clipped in the bar, not in the reported number.</p></section><section class=\"callout\"><b>Limits and verification:</b> Exponent 0.25 assumed; fit C and n experimentally for the actual tool and workpiece. Use calibrated equipment data and appropriate process tests before engineering release.</section>",
    init: function(card) {
      try {
const A=card.querySelector("#" + 'a'.replace(/^#/, "")),B=card.querySelector("#" + 'b'.replace(/^#/, "")),V=card.querySelector("#" + 'value'.replace(/^#/, "")),AL=card.querySelector("#" + 'al'.replace(/^#/, "")),BL=card.querySelector("#" + 'bl'.replace(/^#/, "")),BAR=card.querySelector("#" + 'bar'.replace(/^#/, "")),DOT=card.querySelector("#" + 'dot'.replace(/^#/, ""));
function compute(a,b){return Math.pow(b/a,4);}
function redraw(){let a=+A.value,b=+B.value,y=compute(a,b);AL.textContent=a.toLocaleString(undefined,{maximumFractionDigits:4});BL.textContent=b.toLocaleString(undefined,{maximumFractionDigits:4});const safe=Number.isFinite(y);V.textContent=safe?y.toLocaleString(undefined,{maximumFractionDigits:3})+' min':'Out of range';V.dataset.result=String(y);let r=safe?Math.max(0,Math.min(1,y/500)):0;BAR.setAttribute('width',String(480*r));DOT.setAttribute('cx',String(30+480*r));}
A.addEventListener('input',redraw);B.addEventListener('input',redraw);redraw();
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
