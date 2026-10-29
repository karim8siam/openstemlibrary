/* Digital Electronics Interactive Simulation Suite */
(function(window) {
  'use strict';
  const MODEL = {
 base:x=>{let w=Math.round(x.width),v=Math.round(x.n);if(w<2||w>24)throw Error('Width must be 2–24.');let m=2**w,u=((v%m)+m)%m,s=u>=2**(w-1)?u-m:u;return [['Binary word',u.toString(2).padStart(w,'0')],['Hexadecimal','0x'+u.toString(16).toUpperCase()],['Unsigned',u],['Signed two’s-complement',s],['Overflow/truncation?',v!==s && v!==u?'Input outside direct range; reduced modulo 2^w':'Review signedness']];},
 gates:x=>{let a=bit(x.a),b=bit(x.b);return [['A AND B',a&b],['A OR B',a|b],['A XOR B',a^b],['A NAND B',1-(a&b)],['A NOR B',1-(a|b)]];},
 mux:x=>{let s=bit(x.s);return [['Selected source',s?'D1':'D0'],['Output Y',bit(s?x.d1:x.d0)],['Equation','Y = ¬S·D0 + S·D1']];},
 adder:x=>{let a=intRange(x.a,0,15),b=intRange(x.b,0,15),raw=a+b,sum=raw&15,c=raw>15?1:0,ov=(((~(a^b))&(a^sum)&8)!==0)?1:0;return [['4-bit sum',sum.toString(2).padStart(4,'0')],['Unsigned result',sum],['Carry-out',c],['Signed overflow',ov],['Raw arithmetic sum',raw]];},
 noise:x=>{let hi=x.voh-x.vih,lo=x.vil-x.vol;if(![hi,lo].every(Number.isFinite))throw Error('Invalid voltages');return [['HIGH margin (V)',fixed(hi)],['LOW margin (V)',fixed(lo)],['Guaranteed interface?',hi>=0&&lo>=0?'Margins nonnegative':'No—negative margin']];},
 power:x=>{if(x.alpha<0||x.alpha>1||x.cap<0||x.freq<0||x.volt<0)throw Error('Use α between 0 and 1; other entries nonnegative.');return [['Switching power (mW)',fixed(x.alpha*x.cap*x.volt*x.volt*x.freq/1000)],['Capacitance (F)',(x.cap*1e-12).toExponential(3)],['Qualification','Excludes leakage and short-circuit current']];},
 dff:x=>{let q=bit(x.q),d=bit(x.d),edge=bit(x.edge);return [['Old Q',q],['Sampled D',d],['New Q',edge?d:q],['Event',edge?'Clock rising edge':'No active edge']];},
 counter:x=>{let n=intRange(x.mod,2,65536),q=intRange(x.count,0,n-1),en=bit(x.enable),nxt=en?(q+1)%n:q;return [['Next count',nxt],['Wrap pulse',en&&q===n-1?1:0],['Count width (minimum)',Math.ceil(Math.log2(n))+' bits']];},
 fsm:x=>{let s=bit(x.state),r=bit(x.req),next=s?(r?1:0):(r?1:0);return [['Old state',s?'ACK':'WAIT'],['Next state',next?'ACK':'WAIT'],['Output acknowledgement',next?'1':'0'],['Contract','ACK remains active while request is asserted']];},
 traffic:x=>{if([x.main,x.side,x.yellow,x.allred].some(a=>a<0))throw Error('Durations must be nonnegative.');let total=x.main+x.side+2*x.yellow+2*x.allred;return [['Full cycle (seconds)',fixed(total)],['Main green fraction',total?fixed(100*x.main/total)+'%':'not defined'],['Protected clearance time',fixed(2*x.allred)+' s']];},
 memory:x=>{let a=intRange(x.address,1,24),d=intRange(x.data,1,256),locations=2**a;return [['Locations',locations],['Capacity (bits)',locations*d],['Capacity (bytes)',fixed(locations*d/8)],['Address range','0 to '+(locations-1)]];},
 sat:x=>{let a=intRange(x.a,0,255),b=intRange(x.b,0,255),v=a+b;return [['Unrestricted sum',v],['8-bit wrapped sum',v%256],['8-bit saturated sum',Math.min(v,255)],['Overflow',v>255?'Yes':'No']];},
 slack:x=>{if([x.period,x.cq,x.logic,x.setup,x.uncertain].some(a=>a<0))throw Error('All timing entries must be nonnegative.');let arrival=x.cq+x.logic, required=x.period-x.setup-x.uncertain;return [['Arrival (ns)',fixed(arrival)],['Latest permitted arrival (ns)',fixed(required)],['Setup slack (ns)',fixed(required-arrival)],['Interpretation',required-arrival>=0?'Pass under assumptions':'Setup violation under assumptions']];},
 debounce:x=>{if(x.stable<0||x.sample<=0)throw Error('Stable time must be nonnegative; sample period positive.');let n=Math.ceil(x.stable/x.sample);return [['Consecutive samples',n],['Effective threshold (ms)',fixed(n*x.sample)],['Input frequency (samples/s)',fixed(1000/x.sample)]];},
 swap:x=>{let a=intRange(x.a,-1e9,1e9),b=intRange(x.b,-1e9,1e9);return [['Before','A='+a+', B='+b],['After one edge','A='+b+', B='+a],['Reason','Nonblocking assignments sample previous state']];},
 timer:x=>{let p=intRange(x.period,1,65536),c=intRange(x.count,0,p-1),e=bit(x.enable),done=e&&c===p-1;return [['Next count',e?(done?0:c+1):c],['Completion pulse',done?1:0],['Period (cycles)',p]];}
};

  var MODELS = [];

  MODELS.push({
    idx: 1,
    unit: 1,
    html: '<div class="sim-header"><span class="badge">Model 01</span><h3>Radix and Signed Words</h3><p>Explore binary, hexadecimal, and two’s-complement interpretations.</p></div>' +
          '<div class="sim-controls"><label for="p-1-n">Decimal value<input type="number" id="p-1-n" data-param="n" value="214" step="any"></label><label for="p-1-width">Word width (bits)<input type="number" id="p-1-width" data-param="width" value="8" step="any"></label></div>' +
          '<div class="readouts" id="out-1"></div>',
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        var out = card.querySelector('#out-1');
        function update() {
          var p = {};
          inputs.forEach(function(el) { p[el.dataset.param] = Number(el.value); });
          var fn = MODEL['base'];
          if (fn && out) {
            try {
              var res = fn(p);
              if (Array.isArray(res)) {
                out.innerHTML = res.map(function(item) {
                  return '<div class="stat-box"><small>' + item[0] + '</small><output>' + item[1] + '</output></div>';
                }).join('');
              } else {
                out.innerHTML = '<div class="stat-box"><output>' + JSON.stringify(res) + '</output></div>';
              }
            } catch (err) {
              out.innerHTML = '<div class="stat-box" style="color:#ef4444"><small>Error</small><output>' + err.message + '</output></div>';
            }
          }
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Digital Electronics sim error in model 1:', err);
      }
    }
  });
  MODELS.push({
    idx: 2,
    unit: 1,
    html: '<div class="sim-header"><span class="badge">Model 02</span><h3>Logic Gates Truth Table</h3><p>Generate truth tables for primary two-input logic gates.</p></div>' +
          '<div class="sim-controls"><label for="p-2-gate">Gate (0:AND, 1:OR, 2:NAND, 3:NOR, 4:XOR)<input type="number" id="p-2-gate" data-param="gate" value="0" step="any"></label><label for="p-2-a">Input A (0 or 1)<input type="number" id="p-2-a" data-param="a" value="1" step="any"></label><label for="p-2-b">Input B (0 or 1)<input type="number" id="p-2-b" data-param="b" value="0" step="any"></label></div>' +
          '<div class="readouts" id="out-2"></div>',
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        var out = card.querySelector('#out-2');
        function update() {
          var p = {};
          inputs.forEach(function(el) { p[el.dataset.param] = Number(el.value); });
          var fn = MODEL['gates'];
          if (fn && out) {
            try {
              var res = fn(p);
              if (Array.isArray(res)) {
                out.innerHTML = res.map(function(item) {
                  return '<div class="stat-box"><small>' + item[0] + '</small><output>' + item[1] + '</output></div>';
                }).join('');
              } else {
                out.innerHTML = '<div class="stat-box"><output>' + JSON.stringify(res) + '</output></div>';
              }
            } catch (err) {
              out.innerHTML = '<div class="stat-box" style="color:#ef4444"><small>Error</small><output>' + err.message + '</output></div>';
            }
          }
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Digital Electronics sim error in model 2:', err);
      }
    }
  });
  MODELS.push({
    idx: 3,
    unit: 2,
    html: '<div class="sim-header"><span class="badge">Model 03</span><h3>De Morgan Theorem Duals</h3><p>Verify equivalence of NAND/NOR expressions against inverted sums.</p></div>' +
          '<div class="sim-controls"><label for="p-3-a">Input A<input type="number" id="p-3-a" data-param="a" value="1" step="any"></label><label for="p-3-b">Input B<input type="number" id="p-3-b" data-param="b" value="0" step="any"></label></div>' +
          '<div class="readouts" id="out-3"></div>',
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        var out = card.querySelector('#out-3');
        function update() {
          var p = {};
          inputs.forEach(function(el) { p[el.dataset.param] = Number(el.value); });
          var fn = MODEL['demorgan'];
          if (fn && out) {
            try {
              var res = fn(p);
              if (Array.isArray(res)) {
                out.innerHTML = res.map(function(item) {
                  return '<div class="stat-box"><small>' + item[0] + '</small><output>' + item[1] + '</output></div>';
                }).join('');
              } else {
                out.innerHTML = '<div class="stat-box"><output>' + JSON.stringify(res) + '</output></div>';
              }
            } catch (err) {
              out.innerHTML = '<div class="stat-box" style="color:#ef4444"><small>Error</small><output>' + err.message + '</output></div>';
            }
          }
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Digital Electronics sim error in model 3:', err);
      }
    }
  });
  MODELS.push({
    idx: 4,
    unit: 2,
    html: '<div class="sim-header"><span class="badge">Model 04</span><h3>4-Variable K-Map Minimizer</h3><p>Sum-of-products minimization across gray-code minterm grids.</p></div>' +
          '<div class="sim-controls"><label for="p-4-minterms">Minterm mask (0-65535)<input type="number" id="p-4-minterms" data-param="minterms" value="4369" step="any"></label></div>' +
          '<div class="readouts" id="out-4"></div>',
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        var out = card.querySelector('#out-4');
        function update() {
          var p = {};
          inputs.forEach(function(el) { p[el.dataset.param] = Number(el.value); });
          var fn = MODEL['kmap'];
          if (fn && out) {
            try {
              var res = fn(p);
              if (Array.isArray(res)) {
                out.innerHTML = res.map(function(item) {
                  return '<div class="stat-box"><small>' + item[0] + '</small><output>' + item[1] + '</output></div>';
                }).join('');
              } else {
                out.innerHTML = '<div class="stat-box"><output>' + JSON.stringify(res) + '</output></div>';
              }
            } catch (err) {
              out.innerHTML = '<div class="stat-box" style="color:#ef4444"><small>Error</small><output>' + err.message + '</output></div>';
            }
          }
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Digital Electronics sim error in model 4:', err);
      }
    }
  });
  MODELS.push({
    idx: 5,
    unit: 3,
    html: '<div class="sim-header"><span class="badge">Model 05</span><h3>2-to-1 and 4-to-1 Multiplexer</h3><p>Data routing and selection with binary address control lines.</p></div>' +
          '<div class="sim-controls"><label for="p-5-sel">Select input (0-3)<input type="number" id="p-5-sel" data-param="sel" value="2" step="any"></label><label for="p-5-d0">D0<input type="number" id="p-5-d0" data-param="d0" value="1" step="any"></label><label for="p-5-d1">D1<input type="number" id="p-5-d1" data-param="d1" value="0" step="any"></label><label for="p-5-d2">D2<input type="number" id="p-5-d2" data-param="d2" value="1" step="any"></label><label for="p-5-d3">D3<input type="number" id="p-5-d3" data-param="d3" value="0" step="any"></label></div>' +
          '<div class="readouts" id="out-5"></div>',
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        var out = card.querySelector('#out-5');
        function update() {
          var p = {};
          inputs.forEach(function(el) { p[el.dataset.param] = Number(el.value); });
          var fn = MODEL['mux'];
          if (fn && out) {
            try {
              var res = fn(p);
              if (Array.isArray(res)) {
                out.innerHTML = res.map(function(item) {
                  return '<div class="stat-box"><small>' + item[0] + '</small><output>' + item[1] + '</output></div>';
                }).join('');
              } else {
                out.innerHTML = '<div class="stat-box"><output>' + JSON.stringify(res) + '</output></div>';
              }
            } catch (err) {
              out.innerHTML = '<div class="stat-box" style="color:#ef4444"><small>Error</small><output>' + err.message + '</output></div>';
            }
          }
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Digital Electronics sim error in model 5:', err);
      }
    }
  });
  MODELS.push({
    idx: 6,
    unit: 3,
    html: '<div class="sim-header"><span class="badge">Model 06</span><h3>Full Adder Binary Arithmetic</h3><p>Calculate sum and carry-out bits for two operands and carry-in.</p></div>' +
          '<div class="sim-controls"><label for="p-6-a">Bit A<input type="number" id="p-6-a" data-param="a" value="1" step="any"></label><label for="p-6-b">Bit B<input type="number" id="p-6-b" data-param="b" value="1" step="any"></label><label for="p-6-cin">Carry-in<input type="number" id="p-6-cin" data-param="cin" value="1" step="any"></label></div>' +
          '<div class="readouts" id="out-6"></div>',
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        var out = card.querySelector('#out-6');
        function update() {
          var p = {};
          inputs.forEach(function(el) { p[el.dataset.param] = Number(el.value); });
          var fn = MODEL['adder'];
          if (fn && out) {
            try {
              var res = fn(p);
              if (Array.isArray(res)) {
                out.innerHTML = res.map(function(item) {
                  return '<div class="stat-box"><small>' + item[0] + '</small><output>' + item[1] + '</output></div>';
                }).join('');
              } else {
                out.innerHTML = '<div class="stat-box"><output>' + JSON.stringify(res) + '</output></div>';
              }
            } catch (err) {
              out.innerHTML = '<div class="stat-box" style="color:#ef4444"><small>Error</small><output>' + err.message + '</output></div>';
            }
          }
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Digital Electronics sim error in model 6:', err);
      }
    }
  });
  MODELS.push({
    idx: 7,
    unit: 4,
    html: '<div class="sim-header"><span class="badge">Model 07</span><h3>Active-Low SR Latch</h3><p>Set, reset, hold, and prohibited metastable states.</p></div>' +
          '<div class="sim-controls"><label for="p-7-s">Set bit (0=active)<input type="number" id="p-7-s" data-param="s" value="0" step="any"></label><label for="p-7-r">Reset bit (0=active)<input type="number" id="p-7-r" data-param="r" value="1" step="any"></label><label for="p-7-qprev">Previous Q<input type="number" id="p-7-qprev" data-param="qprev" value="0" step="any"></label></div>' +
          '<div class="readouts" id="out-7"></div>',
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        var out = card.querySelector('#out-7');
        function update() {
          var p = {};
          inputs.forEach(function(el) { p[el.dataset.param] = Number(el.value); });
          var fn = MODEL['srlatch'];
          if (fn && out) {
            try {
              var res = fn(p);
              if (Array.isArray(res)) {
                out.innerHTML = res.map(function(item) {
                  return '<div class="stat-box"><small>' + item[0] + '</small><output>' + item[1] + '</output></div>';
                }).join('');
              } else {
                out.innerHTML = '<div class="stat-box"><output>' + JSON.stringify(res) + '</output></div>';
              }
            } catch (err) {
              out.innerHTML = '<div class="stat-box" style="color:#ef4444"><small>Error</small><output>' + err.message + '</output></div>';
            }
          }
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Digital Electronics sim error in model 7:', err);
      }
    }
  });
  MODELS.push({
    idx: 8,
    unit: 4,
    html: '<div class="sim-header"><span class="badge">Model 08</span><h3>D Flip-Flop Edge Trigger</h3><p>Positive edge-triggered data latching and setup/hold timing margin.</p></div>' +
          '<div class="sim-controls"><label for="p-8-d">Data D<input type="number" id="p-8-d" data-param="d" value="1" step="any"></label><label for="p-8-clk">Clock transition (1=edge)<input type="number" id="p-8-clk" data-param="clk" value="1" step="any"></label></div>' +
          '<div class="readouts" id="out-8"></div>',
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        var out = card.querySelector('#out-8');
        function update() {
          var p = {};
          inputs.forEach(function(el) { p[el.dataset.param] = Number(el.value); });
          var fn = MODEL['dff'];
          if (fn && out) {
            try {
              var res = fn(p);
              if (Array.isArray(res)) {
                out.innerHTML = res.map(function(item) {
                  return '<div class="stat-box"><small>' + item[0] + '</small><output>' + item[1] + '</output></div>';
                }).join('');
              } else {
                out.innerHTML = '<div class="stat-box"><output>' + JSON.stringify(res) + '</output></div>';
              }
            } catch (err) {
              out.innerHTML = '<div class="stat-box" style="color:#ef4444"><small>Error</small><output>' + err.message + '</output></div>';
            }
          }
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Digital Electronics sim error in model 8:', err);
      }
    }
  });
  MODELS.push({
    idx: 9,
    unit: 5,
    html: '<div class="sim-header"><span class="badge">Model 09</span><h3>3-Bit Synchronous Counter</h3><p>Modulo-8 synchronous up/down counter state progression.</p></div>' +
          '<div class="sim-controls"><label for="p-9-dir">Direction (1=Up, 0=Down)<input type="number" id="p-9-dir" data-param="dir" value="1" step="any"></label><label for="p-9-current">Current state (0-7)<input type="number" id="p-9-current" data-param="current" value="3" step="any"></label></div>' +
          '<div class="readouts" id="out-9"></div>',
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        var out = card.querySelector('#out-9');
        function update() {
          var p = {};
          inputs.forEach(function(el) { p[el.dataset.param] = Number(el.value); });
          var fn = MODEL['counter'];
          if (fn && out) {
            try {
              var res = fn(p);
              if (Array.isArray(res)) {
                out.innerHTML = res.map(function(item) {
                  return '<div class="stat-box"><small>' + item[0] + '</small><output>' + item[1] + '</output></div>';
                }).join('');
              } else {
                out.innerHTML = '<div class="stat-box"><output>' + JSON.stringify(res) + '</output></div>';
              }
            } catch (err) {
              out.innerHTML = '<div class="stat-box" style="color:#ef4444"><small>Error</small><output>' + err.message + '</output></div>';
            }
          }
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Digital Electronics sim error in model 9:', err);
      }
    }
  });
  MODELS.push({
    idx: 10,
    unit: 5,
    html: '<div class="sim-header"><span class="badge">Model 10</span><h3>4-Bit Universal Shift Register</h3><p>Parallel load, left shift, right shift, and serial hold.</p></div>' +
          '<div class="sim-controls"><label for="p-10-mode">Mode (0:Hold, 1:Right, 2:Left, 3:Load)<input type="number" id="p-10-mode" data-param="mode" value="1" step="any"></label><label for="p-10-val">Current word (0-15)<input type="number" id="p-10-val" data-param="val" value="9" step="any"></label><label for="p-10-sin">Serial in bit<input type="number" id="p-10-sin" data-param="sin" value="1" step="any"></label></div>' +
          '<div class="readouts" id="out-10"></div>',
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        var out = card.querySelector('#out-10');
        function update() {
          var p = {};
          inputs.forEach(function(el) { p[el.dataset.param] = Number(el.value); });
          var fn = MODEL['shift'];
          if (fn && out) {
            try {
              var res = fn(p);
              if (Array.isArray(res)) {
                out.innerHTML = res.map(function(item) {
                  return '<div class="stat-box"><small>' + item[0] + '</small><output>' + item[1] + '</output></div>';
                }).join('');
              } else {
                out.innerHTML = '<div class="stat-box"><output>' + JSON.stringify(res) + '</output></div>';
              }
            } catch (err) {
              out.innerHTML = '<div class="stat-box" style="color:#ef4444"><small>Error</small><output>' + err.message + '</output></div>';
            }
          }
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Digital Electronics sim error in model 10:', err);
      }
    }
  });
  MODELS.push({
    idx: 11,
    unit: 6,
    html: '<div class="sim-header"><span class="badge">Model 11</span><h3>Mealy vs Moore Sequence Detector</h3><p>101 bit sequence detection with overlapping state memory.</p></div>' +
          '<div class="sim-controls"><label for="p-11-bit">Next input stream bit (0/1)<input type="number" id="p-11-bit" data-param="bit" value="1" step="any"></label><label for="p-11-state">Current state (0-3)<input type="number" id="p-11-state" data-param="state" value="2" step="any"></label></div>' +
          '<div class="readouts" id="out-11"></div>',
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        var out = card.querySelector('#out-11');
        function update() {
          var p = {};
          inputs.forEach(function(el) { p[el.dataset.param] = Number(el.value); });
          var fn = MODEL['fsm'];
          if (fn && out) {
            try {
              var res = fn(p);
              if (Array.isArray(res)) {
                out.innerHTML = res.map(function(item) {
                  return '<div class="stat-box"><small>' + item[0] + '</small><output>' + item[1] + '</output></div>';
                }).join('');
              } else {
                out.innerHTML = '<div class="stat-box"><output>' + JSON.stringify(res) + '</output></div>';
              }
            } catch (err) {
              out.innerHTML = '<div class="stat-box" style="color:#ef4444"><small>Error</small><output>' + err.message + '</output></div>';
            }
          }
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Digital Electronics sim error in model 11:', err);
      }
    }
  });
  MODELS.push({
    idx: 12,
    unit: 6,
    html: '<div class="sim-header"><span class="badge">Model 12</span><h3>State Table Minimizer</h3><p>Identify equivalent states and eliminate redundant rows.</p></div>' +
          '<div class="sim-controls"><label for="p-12-rows">States count (2-8)<input type="number" id="p-12-rows" data-param="rows" value="4" step="any"></label></div>' +
          '<div class="readouts" id="out-12"></div>',
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        var out = card.querySelector('#out-12');
        function update() {
          var p = {};
          inputs.forEach(function(el) { p[el.dataset.param] = Number(el.value); });
          var fn = MODEL['state'];
          if (fn && out) {
            try {
              var res = fn(p);
              if (Array.isArray(res)) {
                out.innerHTML = res.map(function(item) {
                  return '<div class="stat-box"><small>' + item[0] + '</small><output>' + item[1] + '</output></div>';
                }).join('');
              } else {
                out.innerHTML = '<div class="stat-box"><output>' + JSON.stringify(res) + '</output></div>';
              }
            } catch (err) {
              out.innerHTML = '<div class="stat-box" style="color:#ef4444"><small>Error</small><output>' + err.message + '</output></div>';
            }
          }
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Digital Electronics sim error in model 12:', err);
      }
    }
  });
  MODELS.push({
    idx: 13,
    unit: 7,
    html: '<div class="sim-header"><span class="badge">Model 13</span><h3>CMOS Inverter Transfer Curve</h3><p>Voltage transfer characteristic (VTC), VOH, VOL, and noise margins.</p></div>' +
          '<div class="sim-controls"><label for="p-13-vdd">Supply Vdd (V)<input type="number" id="p-13-vdd" data-param="vdd" value="5" step="any"></label><label for="p-13-vtn">Vtn threshold (V)<input type="number" id="p-13-vtn" data-param="vtn" value="0.8" step="any"></label><label for="p-13-vtp">Vtp threshold (V)<input type="number" id="p-13-vtp" data-param="vtp" value="-0.8" step="any"></label></div>' +
          '<div class="readouts" id="out-13"></div>',
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        var out = card.querySelector('#out-13');
        function update() {
          var p = {};
          inputs.forEach(function(el) { p[el.dataset.param] = Number(el.value); });
          var fn = MODEL['cmos'];
          if (fn && out) {
            try {
              var res = fn(p);
              if (Array.isArray(res)) {
                out.innerHTML = res.map(function(item) {
                  return '<div class="stat-box"><small>' + item[0] + '</small><output>' + item[1] + '</output></div>';
                }).join('');
              } else {
                out.innerHTML = '<div class="stat-box"><output>' + JSON.stringify(res) + '</output></div>';
              }
            } catch (err) {
              out.innerHTML = '<div class="stat-box" style="color:#ef4444"><small>Error</small><output>' + err.message + '</output></div>';
            }
          }
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Digital Electronics sim error in model 13:', err);
      }
    }
  });
  MODELS.push({
    idx: 14,
    unit: 7,
    html: '<div class="sim-header"><span class="badge">Model 14</span><h3>Propagation Delay vs Fan-Out</h3><p>Capacitive loading delay scaling with fan-out count.</p></div>' +
          '<div class="sim-controls"><label for="p-14-fanout">Driven load gates count<input type="number" id="p-14-fanout" data-param="fanout" value="4" step="any"></label><label for="p-14-cgate">Gate cap (fF)<input type="number" id="p-14-cgate" data-param="cgate" value="15" step="any"></label></div>' +
          '<div class="readouts" id="out-14"></div>',
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        var out = card.querySelector('#out-14');
        function update() {
          var p = {};
          inputs.forEach(function(el) { p[el.dataset.param] = Number(el.value); });
          var fn = MODEL['fanout'];
          if (fn && out) {
            try {
              var res = fn(p);
              if (Array.isArray(res)) {
                out.innerHTML = res.map(function(item) {
                  return '<div class="stat-box"><small>' + item[0] + '</small><output>' + item[1] + '</output></div>';
                }).join('');
              } else {
                out.innerHTML = '<div class="stat-box"><output>' + JSON.stringify(res) + '</output></div>';
              }
            } catch (err) {
              out.innerHTML = '<div class="stat-box" style="color:#ef4444"><small>Error</small><output>' + err.message + '</output></div>';
            }
          }
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Digital Electronics sim error in model 14:', err);
      }
    }
  });
  MODELS.push({
    idx: 15,
    unit: 8,
    html: '<div class="sim-header"><span class="badge">Model 15</span><h3>SRAM 6-Transistor Cell Array</h3><p>Differential bitline precharge, sense amplifier, and write margin.</p></div>' +
          '<div class="sim-controls"><label for="p-15-word">Wordline active (0/1)<input type="number" id="p-15-word" data-param="word" value="1" step="any"></label><label for="p-15-bit">Data write bit (0/1)<input type="number" id="p-15-bit" data-param="bit" value="1" step="any"></label></div>' +
          '<div class="readouts" id="out-15"></div>',
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        var out = card.querySelector('#out-15');
        function update() {
          var p = {};
          inputs.forEach(function(el) { p[el.dataset.param] = Number(el.value); });
          var fn = MODEL['sram'];
          if (fn && out) {
            try {
              var res = fn(p);
              if (Array.isArray(res)) {
                out.innerHTML = res.map(function(item) {
                  return '<div class="stat-box"><small>' + item[0] + '</small><output>' + item[1] + '</output></div>';
                }).join('');
              } else {
                out.innerHTML = '<div class="stat-box"><output>' + JSON.stringify(res) + '</output></div>';
              }
            } catch (err) {
              out.innerHTML = '<div class="stat-box" style="color:#ef4444"><small>Error</small><output>' + err.message + '</output></div>';
            }
          }
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Digital Electronics sim error in model 15:', err);
      }
    }
  });
  MODELS.push({
    idx: 16,
    unit: 8,
    html: '<div class="sim-header"><span class="badge">Model 16</span><h3>Programmable Logic Array (PLA)</h3><p>AND-OR matrix configuration for sum-of-products mapping.</p></div>' +
          '<div class="sim-controls"><label for="p-16-inputs">Active inputs bitmask (0-15)<input type="number" id="p-16-inputs" data-param="inputs" value="5" step="any"></label></div>' +
          '<div class="readouts" id="out-16"></div>',
    init: function(card) {
      try {
        var inputs = card.querySelectorAll('input[data-param]');
        var out = card.querySelector('#out-16');
        function update() {
          var p = {};
          inputs.forEach(function(el) { p[el.dataset.param] = Number(el.value); });
          var fn = MODEL['pla'];
          if (fn && out) {
            try {
              var res = fn(p);
              if (Array.isArray(res)) {
                out.innerHTML = res.map(function(item) {
                  return '<div class="stat-box"><small>' + item[0] + '</small><output>' + item[1] + '</output></div>';
                }).join('');
              } else {
                out.innerHTML = '<div class="stat-box"><output>' + JSON.stringify(res) + '</output></div>';
              }
            } catch (err) {
              out.innerHTML = '<div class="stat-box" style="color:#ef4444"><small>Error</small><output>' + err.message + '</output></div>';
            }
          }
        }
        inputs.forEach(function(el) { el.addEventListener('input', update); });
        update();
      } catch (err) {
        console.warn('Digital Electronics sim error in model 16:', err);
      }
    }
  });
  if (!window.SimulationEngine) window.SimulationEngine = {};
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId) ||
                    document.getElementById('sim-container') ||
                    document.querySelector('.simulation-slot');
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
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.slice(0, 2);
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
    var autoInit = function() {
      var slot = document.getElementById('sim-container') || document.querySelector('.simulation-slot');
      if (slot && slot.children.length === 0) {
        window.SimulationEngine.initSimulation(slot.id || 'sim-container');
      }
    };
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', autoInit);
    } else {
      autoInit();
    }
  }
})(typeof window === 'undefined' ? globalThis : window);
