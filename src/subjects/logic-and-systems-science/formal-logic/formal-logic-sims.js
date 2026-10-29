/* formal-logic Interactive Simulation Suite */
(function(window) {
  'use strict';

  var MODELS = [
  {
    "idx": 1,
    "unit": 1,
    "title": "Argument validity",
    "desc": "Search all four interpretations of P,Q for true premises and false conclusion.",
    "type": "validity",
    "controls": "<label>Inference <select name='inference'><option value='mp'>P\u2192Q, P \u22a8 Q</option><option value='ac'>P\u2192Q, Q \u22a8 P</option></select></label>"
  },
  {
    "idx": 2,
    "unit": 1,
    "title": "Converse failure",
    "desc": "Set P and Q to discover why P\u2192Q does not imply Q\u2192P.",
    "type": "converse",
    "controls": "<div class=\"sim-controls\"><label><input type='checkbox' name='p' checked>P</label><label><input type='checkbox' name='q' checked>Q</label></div></div>"
  },
  {
    "idx": 3,
    "unit": 2,
    "title": "Two-variable truth table",
    "desc": "Select a connective and inspect all truth assignments.",
    "type": "truth",
    "controls": "<label>Select connective <select name='op'><option value='and'>AND</option><option value='or'>OR</option><option value='implies'>IMPLIES</option><option value='iff'>IFF</option><option value='xor'>XOR</option></select></label>"
  },
  {
    "idx": 4,
    "unit": 2,
    "title": "Formula equivalence",
    "desc": "Compare P\u2192Q with \u00acP\u2228Q across all rows.",
    "type": "equivalence",
    "controls": "<label>Comparison <select name='pair'><option value='same'>P\u2192Q versus \u00acP\u2228Q</option><option value='converse'>P\u2192Q versus Q\u2192P</option></select></label>"
  },
  {
    "idx": 5,
    "unit": 3,
    "title": "Proof rule explorer",
    "desc": "Select an inference rule and inspect its premises, result, and justification.",
    "type": "proof",
    "controls": "<label>Select rule <select name='rule'><option value='modusponens'>Modus ponens</option><option value='andintro'>\u2227 Introduction</option><option value='andout'>\u2227 Elimination</option><option value='orintro'>\u2228 Introduction</option></select></label>"
  },
  {
    "idx": 6,
    "unit": 3,
    "title": "Tableau branches",
    "desc": "Expand the negation of a conclusion alongside its premises.",
    "type": "tableau",
    "controls": "<label>Entailment <select name='form'><option value='valid'>P\u2192Q, P \u22a8 Q</option><option value='invalid'>P\u2192Q, Q \u22a8 P</option></select></label>"
  },
  {
    "idx": 7,
    "unit": 4,
    "title": "Quantifier domain model",
    "desc": "Choose which objects satisfy P and evaluate \u2200xP(x) and \u2203xP(x).",
    "type": "quantifier",
    "controls": "<div class=\"sim-controls\"><label><input type='checkbox' name='a' checked>P(a)</label><label><input type='checkbox' name='b'>P(b)</label><label><input type='checkbox' name='c' checked>P(c)</label></div>"
  },
  {
    "idx": 8,
    "unit": 4,
    "title": "Quantifier order",
    "desc": "Edit a finite relation table and compare \u2200x\u2203yR(x,y) to \u2203y\u2200xR(x,y).",
    "type": "order",
    "controls": "<div class=\"sim-controls\"><label><input type='checkbox' name='r11' checked>R(x\u2081,y\u2081)</label><label><input type='checkbox' name='r12'>R(x\u2081,y\u2082)</label><label><input type='checkbox' name='r21'>R(x\u2082,y\u2081)</label><label><input type='checkbox' name='r22' checked>R(x\u2082,y\u2082)</label></div>"
  },
  {
    "idx": 9,
    "unit": 5,
    "title": "Soundness diagnostic",
    "desc": "Contrast an admissible truth-preserving rule with affirming the consequent.",
    "type": "soundness",
    "controls": "<label>Rule <select name='rule'><option value='mp'>Modus ponens</option><option value='bad'>Affirming consequent</option></select></label>"
  },
  {
    "idx": 10,
    "unit": 5,
    "title": "SAT and consistency",
    "desc": "Toggle Boolean requirements and find assignments or a conflict.",
    "type": "sat",
    "controls": "<div class=\"sim-controls\"><label><input type='checkbox' name='req1' checked>Require P</label><label><input type='checkbox' name='req2'>Require \u00acP</label><label><input type='checkbox' name='req3' checked>Require Q</label></div>"
  },
  {
    "idx": 11,
    "unit": 6,
    "title": "Countermodel search",
    "desc": "Select a candidate assignment and check an invalid inference.",
    "type": "counter",
    "controls": "<div class=\"sim-controls\"><label><input type='checkbox' name='p' checked>P</label><label><input type='checkbox' name='q' checked>Q</label></div>"
  },
  {
    "idx": 12,
    "unit": 6,
    "title": "Induction checkpoints",
    "desc": "Select n and see the sum-of-integers identity and inductive bridge.",
    "type": "induction",
    "controls": "<label>n <select name='n'><option value='1'>1</option><option value='2'>2</option><option value='3'>3</option><option value='4'>4</option><option value='5'>5</option><option value='6'>6</option><option value='7'>7</option><option value='8'>8</option><option value='9'>9</option><option value='10'>10</option><option value='11'>11</option><option value='12'>12</option><option value='13'>13</option><option value='14'>14</option><option value='15'>15</option><option value='16'>16</option><option value='17'>17</option><option value='18'>18</option><option value='19'>19</option><option value='20'>20</option></select></label>"
  },
  {
    "idx": 13,
    "unit": 7,
    "title": "Strong Kleene logic",
    "desc": "Explore three-valued conjunction and negation with unknown inputs.",
    "type": "kleene",
    "controls": "<div class=\"sim-controls\"><label>P <select name='p'><option>T</option><option>U</option><option>F</option></select></label><label>Q <select name='q'><option>T</option><option selected>U</option><option>F</option></select></label></div>"
  },
  {
    "idx": 14,
    "unit": 7,
    "title": "Modal frame explorer",
    "desc": "Toggle accessibility to test whether \u25a1P implies P at the current world.",
    "type": "modal",
    "controls": "<div class=\"sim-controls\"><label><input type='checkbox' name='loop'>w\u2192w</label><label><input type='checkbox' name='cur'>P at w</label><label><input type='checkbox' name='other' checked>P at v</label></div>"
  },
  {
    "idx": 15,
    "unit": 8,
    "title": "Access policy checker",
    "desc": "Test authorization, consent and active membership together.",
    "type": "access",
    "controls": "<div class=\"sim-controls\"><label><input type='checkbox' name='auth' checked>Authorized</label><label><input type='checkbox' name='consent' checked>Consented</label><label><input type='checkbox' name='active'>Active</label></div>"
  },
  {
    "idx": 16,
    "unit": 8,
    "title": "Clause satisfiability",
    "desc": "Search three-variable assignments satisfying a small CNF policy.",
    "type": "cnf",
    "controls": "<label>Final clause <select name='last'><option value='notr'>\u00acR</option><option value='r'>R</option></select></label><p>Base clauses: (P\u2228Q) \u2227 (\u00acP\u2228R)</p>"
  }
];

  // Original calculation logic adapted for scoped execution

'use strict';
const $=s=>document.querySelector(s);const table=(heads,rows)=>'<table><thead><tr>'+heads.map(x=>'<th>'+x+'</th>').join('')+'</tr></thead><tbody>'+rows.map(r=>'<tr>'+r.map(x=>'<td>'+x+'</td>').join('')+'</tr>').join('')+'</tbody></table>';
function bool(v){return v?'T':'F'}
function parseBool(name){const e=document.querySelector(`[name="${name}"]`);return !!(e&&e.checked)}
function select(name){const e=document.querySelector(`[name="${name}"]`);return e?e.value:''}
function inputHtml(labels){return '<div class="inputgrid">'+labels.map(([key,label,checked])=>`<label><input type="checkbox" name="${key}" ${checked?'checked':''}>${label}</label>`).join('')+'</div>'}
function text(html){const el=$('#output');if(el)el.innerHTML=html;}
function update(){let t=document.body.dataset.type;
 if(t==='validity'){
  let mode=select('inference'),rows=[],bad=[];for(let p of [false,true])for(let q of [false,true]){let a=!p||q,b=mode==='mp'?p:q,c=mode==='mp'?q:p,v=a&&b&&!c;rows.push([bool(p),bool(q),bool(a),bool(b),bool(c),v?'COUNTERMODEL':'—']);if(v)bad.push([p,q])}text(table(['P','Q','P→Q','Second premise','Conclusion','Invalidating row'],rows)+(bad.length?'<p class="no">Invalid: a displayed countermodel makes the premises true and conclusion false.</p>':'<p class="ok">Valid: exhaustive search found no countermodel.</p>'))}
 else if(t==='converse'){let p=parseBool('p'),q=parseBool('q');text(table(['P','Q','P→Q','Q→P'],[[bool(p),bool(q),bool(!p||q),bool(!q||p)]])+(p===false&&q===true?'<p class="no">Counterexample: original conditional true, converse false.</p>':'<p>Try P=F and Q=T to separate the converse from the original.</p>'))}
 else if(t==='truth'){let op=select('op'),ops={'and':(p,q)=>p&&q,'or':(p,q)=>p||q,'implies':(p,q)=>!p||q,'iff':(p,q)=>p===q,'xor':(p,q)=>p!==q};let rows=[];for(let p of [false,true])for(let q of [false,true])rows.push([bool(p),bool(q),bool(ops[op](p,q))]);text(table(['P','Q',op],rows)+'<p>These four rows exhaust every valuation of two independent propositions.</p>')}
 else if(t==='equivalence'){let rows=[],mode=select('pair'),same=true;for(let p of [false,true])for(let q of [false,true]){let a=!p||q,b=mode==='same'?(!p||q):(!q||p);if(a!==b)same=false;rows.push([bool(p),bool(q),bool(a),bool(b)])}text(table(['P','Q','P→Q',mode==='same'?'¬P∨Q':'Q→P'],rows)+'<p class="'+(same?'ok':'no')+'">'+(same?'Equivalent: every row matches.':'Not equivalent: at least one row differs.')+'</p>')}
 else if(t==='proof'){let cases={'modusponens':['P','P→Q','Q','Implication elimination (modus ponens)'], 'andintro':['P','Q','P∧Q','Conjunction introduction'], 'andout':['P∧Q','—','P','Conjunction elimination'], 'orintro':['P','—','P∨Q','Disjunction introduction']};let [a,b,c,d]=cases[select('rule')];text(table(['Line','Formula','Reason'],[['1',a,'Premise'],['2',b,b==='—'?'Not needed':'Premise'],['3',c,d]])+'<p>Every derived line is justified locally by a named sound rule.</p>')}
 else if(t==='tableau'){let example=select('form');if(example==='valid'){text('<p><strong>Root constraints:</strong> P→Q, P, ¬Q.</p><p>Expand P→Q into branches ¬P | Q. The first contradicts P; the second contradicts ¬Q.</p><p class="ok">Both branches close. The entailment is valid.</p>')}else{text('<p><strong>Root constraints:</strong> P→Q, Q, ¬P.</p><p class="no">Open branch: P=F, Q=T satisfies all three. The proposed conclusion P is not entailed.</p>')}}
 else if(t==='quantifier'){let a=parseBool('a'),b=parseBool('b'),c=parseBool('c'),vals=[a,b,c];text(table(['Element','P(x)'],[['a',bool(a)],['b',bool(b)],['c',bool(c)]])+'<p>∀xP(x) = <b>'+bool(vals.every(Boolean))+'</b>. ∃xP(x) = <b>'+bool(vals.some(Boolean))+'</b>.</p><p>Declared domain D={a,b,c}. These conclusions apply only to this structure.</p>')}
 else if(t==='order'){let vals=['r11','r12','r21','r22'].map(parseBool);let everySome=(vals[0]||vals[1])&&(vals[2]||vals[3]);let someEvery=(vals[0]&&vals[2])||(vals[1]&&vals[3]);text(table(['','y₁','y₂'],[['x₁',bool(vals[0]),bool(vals[1])],['x₂',bool(vals[2]),bool(vals[3])]])+`<p>∀x∃yR(x,y) = <b>${bool(everySome)}</b>. ∃y∀xR(x,y) = <b>${bool(someEvery)}</b>.</p><p>One witness y may differ by x in the first formula; the second requires one common y.</p>`)}
 else if(t==='soundness'){let rule=select('rule');if(rule==='mp'){text('<p>Rule: P, P→Q ⊢ Q. Any assignment making P and P→Q both true must make Q true.</p><p class="ok">Sound rule: no counterexample exists.</p>')}else{text('<p>Proposed rule: P→Q, Q ⊢ P. Assignment P=F, Q=T makes both premises true but conclusion false.</p><p class="no">Unsound inference: affirming the consequent.</p>')}}
 else if(t==='sat'){let a=parseBool('req1'),b=parseBool('req2'),c=parseBool('req3');let req=[];if(a)req.push('P');if(b)req.push('¬P');if(c)req.push('Q');let sat=!(a&&b);text('<p>Selected requirements: <code>'+ (req.join(' ∧ ')||'⊤') +'</code></p><p class="'+(sat?'ok':'no')+'">'+(sat?'Satisfiable. Example: P='+bool(a)+', Q='+bool(c)+'.':'Unsatisfiable: P and ¬P are both required.')+'</p>')}
 else if(t==='counter'){let p=parseBool('p'),q=parseBool('q');let prem1=!p||q,prem2=q,con=p;let fail=prem1&&prem2&&!con;text(table(['P','Q','P→Q','Q','Conclusion P'],[[bool(p),bool(q),bool(prem1),bool(prem2),bool(con)]])+'<p class="'+(fail?'no':'warn')+'">'+(fail?'Actual countermodel: both premises true, conclusion false.':'This assignment is not a countermodel. Try P=F,Q=T.')+'</p>')}
 else if(t==='induction'){let n=Number(select('n'));let lhs=n*(n+1)/2,rhs=n*(n+1)/2,next=(n+1)*(n+2)/2;text(`<p>At n=${n}, 1+…+n = ${lhs} and n(n+1)/2 = ${rhs}.</p><p>Inductive bridge: ${lhs} + ${n+1} = ${next} = (n+1)(n+2)/2.</p><p>Checking finite n is illustrative. The induction proof requires a general symbolic step, not these numerical instances.</p>`)}
 else if(t==='kleene'){let values={F:0,U:1,T:2};let a=select('p'),b=select('q');let rev=['F','U','T'];text(table(['P','Q','P ∧ Q','¬P'],[[a,b,rev[Math.min(values[a],values[b])],rev[2-values[a]]]])+'<p>Strong Kleene semantics shown. U means unknown, not 50% probability.</p>')}
 else if(t==='modal'){let reachable=parseBool('loop'),other=parseBool('other'),cur=parseBool('cur');let reachableTruth=[];if(reachable)reachableTruth.push(cur);reachableTruth.push(other);let necessary=reachableTruth.every(Boolean);text(`<p>At current world w: P=${bool(cur)}. Edge w→w: ${reachable?'yes':'no'}. Edge w→v: yes. At v: P=${bool(other)}.</p><p>□P at w = <b>${bool(necessary)}</b>. P at w = <b>${bool(cur)}</b>.</p><p>${reachable?'Frame is reflexive at w, so □P→P holds there.':'With no self-loop, □P may be true while P at w is false: try current F, other T.'}</p>`)}
 else if(t==='access'){let a=parseBool('auth'),b=parseBool('consent'),c=parseBool('active');let allow=a&&b&&c;text(table(['Authorized','Consent','Active','Permit'],[[bool(a),bool(b),bool(c),bool(allow)]])+'<p class="'+(allow?'ok':'no')+'">Decision: '+(allow?'Permit under the toy policy.':'Deny under the toy policy.')+'</p><p>Implementation of an invented policy; not a production authentication service.</p>')}
 else if(t==='cnf'){let rows=[],solutions=[],mode=select('last');for(let p of [false,true])for(let q of [false,true])for(let r of [false,true]){let ok=(p||q)&&(!p||r)&&(mode==='notr'?!r:r);rows.push([bool(p),bool(q),bool(r),ok?'✓':'—']);if(ok)solutions.push([p,q,r])}text(table(['P','Q','R','Satisfies all clauses'],rows)+'<p class="ok">'+solutions.length+' satisfying assignment(s): '+solutions.map(x=>'('+x.map(bool).join(',')+')').join(', ')+'.</p>')}
}
document.addEventListener('change',update);document.addEventListener('DOMContentLoaded',update);


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
      var bMatch = document.body.dataset.chapterIndex || window.location.pathname.match(/chapter-(\d+)/);
      if (bMatch) {
        unitNum = typeof bMatch === 'string' ? (parseInt(bMatch, 10) + 1) : parseInt(bMatch[1], 10);
      }
    }

    var modelsForUnit = MODELS.filter(function(m) { return m.unit === unitNum; });
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.slice(0, 2);

    modelsForUnit.forEach(function(m, idx) {
      var card = document.createElement('section');
      card.className = 'logic-sim-card';
      card.setAttribute('aria-label', m.title);
      card.id = 'sim-card-' + m.idx;

      var headerHtml = 
        '<div>' +
          '<span class="sim-tag">Unit ' + unitNum + '</span>' +
          '<span class="sim-tag">Interactive Model ' + m.idx + ' of 16</span>' +
        '</div>' +
        '<h3>' + m.title + '</h3>' +
        '<p class="sim-desc">' + m.desc + '</p>';

      var controlsContainer = document.createElement('div');
      controlsContainer.className = 'sim-controls';
      controlsContainer.innerHTML = m.controls || '<div style="color:#94a3b8;font-size:0.88rem;">Model evaluates live parameter derivations.</div>';

      var outputEl = document.createElement('div');
      outputEl.className = 'sim-output';
      outputEl.id = 'output-' + m.idx;
      outputEl.setAttribute('aria-live', 'polite');
      outputEl.innerHTML = '<div style="color:#94a3b8;font-size:0.88rem;">Evaluating local formal semantics…</div>';

      card.innerHTML = headerHtml;
      card.appendChild(controlsContainer);
      card.appendChild(outputEl);
      container.appendChild(card);

      // Scoped update runner
      function runUpdate() {
        document.body.dataset.type = m.type;
        document.body.dataset.kind = m.type;

        // Route document.querySelector / document.getElementById to local card
        var prevOutput = document.getElementById('output');
        var outputWrapper = outputEl;
        
        // Execute update if available
        if (typeof update === 'function') {
          // redirect output
          var oldOut = document.querySelector('#output');
          var tempOut = document.createElement('div');
          tempOut.id = 'output';
          document.body.appendChild(tempOut);
          
          try {
            update();
            outputWrapper.innerHTML = tempOut.innerHTML;
          } catch(e) {
            outputWrapper.innerHTML = '<p class="warn">Evaluating derivation step...</p>';
          } finally {
            tempOut.remove();
          }
        } else if (typeof calculate === 'function') {
          try {
            var num = function(name, defVal) {
              var inp = card.querySelector('[name="' + name + '"], #' + name);
              var v = inp ? Number(inp.value) : defVal;
              return Number.isFinite(v) ? v : defVal;
            };
            var res = calculate(m.type, num('n', 3), num('a', 3), num('b', 2));
            if (res && res.title && res.rows) {
              var h = '<h4 style="margin:0 0 8px;color:#38bdf8;font-size:1rem;">' + res.title + '</h4><ol>';
              res.rows.forEach(function(r) { h += '<li>' + r + '</li>'; });
              h += '</ol>';
              outputWrapper.innerHTML = h;
            }
          } catch(e) {
            outputWrapper.innerHTML = '<p class="warn">Evaluating calculation...</p>';
          }
        } else if (typeof run === 'function') {
          try {
            run();
          } catch(e) {}
        }
      }

      // Attach event listeners
      card.querySelectorAll('input, select').forEach(function(inp) {
        inp.addEventListener('input', runUpdate);
        inp.addEventListener('change', runUpdate);
      });
      var rerunBtn = card.querySelector('#rerun, button');
      if (rerunBtn) rerunBtn.addEventListener('click', runUpdate);

      // Initial run
      runUpdate();
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
