/* symbolic-and-predicate-logic Interactive Simulation Suite */
(function(window) {
  'use strict';

  var MODELS = [
  {
    "idx": 1,
    "unit": 1,
    "title": "Quantifier scope explorer",
    "desc": "Compare bound and free occurrences; observe why parentheses matter.",
    "type": "scope",
    "controls": "<div class=\"sim-controls\"><label><input type=\"checkbox\" name=\"P0\" checked> P(a)</label><label><input type=\"checkbox\" name=\"P1\"> P(b)</label><label><input type=\"checkbox\" name=\"Q0\" checked> Q(a)</label><label><input type=\"checkbox\" name=\"Q1\"> Q(b)</label><label>free x: <select name=\"x\"><option value=\"0\">a</option><option value=\"1\">b</option></select></label></div>"
  },
  {
    "idx": 2,
    "unit": 1,
    "title": "Capture-avoiding substitution",
    "desc": "See the difference between renaming a binder and naive text replacement.",
    "type": "sub",
    "controls": "<div class=\"sim-controls\"><label><select name=\"choice\"><option value=\"safe\">Rename bound y to fresh z</option><option value=\"naive\">Naive substitution x \u2192 y</option></select></label><p>Source formula: \u2200y R(x,y). Replacement requested: y for free x.</p></div>"
  },
  {
    "idx": 3,
    "unit": 2,
    "title": "Restricted quantification",
    "desc": "Inspect universal and existential readings on two candidate objects.",
    "type": "restrict",
    "controls": "<div class=\"sim-controls\"><label><input type=\"checkbox\" name=\"A0\" checked> Student(a)</label><label><input type=\"checkbox\" name=\"B0\" checked> Approved(a)</label><label><input type=\"checkbox\" name=\"A1\"> Student(b)</label><label><input type=\"checkbox\" name=\"B1\"> Approved(b)</label></div>"
  },
  {
    "idx": 4,
    "unit": 2,
    "title": "Exactly-one verifier",
    "desc": "Check existence, at-most-one, and exactly-one separately.",
    "type": "unique",
    "controls": "<div class=\"sim-controls\"><label><input type=\"checkbox\" name=\"A0\" checked> P(a)</label><label><input type=\"checkbox\" name=\"A1\"> P(b)</label></div>"
  },
  {
    "idx": 5,
    "unit": 3,
    "title": "Finite relation semantics",
    "desc": "Edit a 2 \u00d7 2 predicate and calculate nested quantified assertions.",
    "type": "rel",
    "controls": "<div class=\"sim-controls\"><label><input type=\"checkbox\" name=\"R00\" checked> R(a,a)</label><label><input type=\"checkbox\" name=\"R01\"> R(a,b)</label><label><input type=\"checkbox\" name=\"R10\"> R(b,a)</label><label><input type=\"checkbox\" name=\"R11\" checked> R(b,b)</label></div>"
  },
  {
    "idx": 6,
    "unit": 3,
    "title": "Open formula assignments",
    "desc": "Change the value of x in a fixed structure and compare an open formula with a sentence.",
    "type": "assign",
    "controls": "<div class=\"sim-controls\"><p>Fixed domain {a,b}, c=b, R={(a,b)}.</p><label>x assignment: <select name=\"x\"><option value=\"0\">a</option><option value=\"1\">b</option></select></label></div>"
  },
  {
    "idx": 7,
    "unit": 4,
    "title": "Quantifier order countermodel",
    "desc": "Search a tiny relation for per-object versus common witnesses.",
    "type": "order",
    "controls": "<div class=\"sim-controls\"><label><input type=\"checkbox\" name=\"R00\" checked> R(a,a)</label><label><input type=\"checkbox\" name=\"R01\"> R(a,b)</label><label><input type=\"checkbox\" name=\"R10\"> R(b,a)</label><label><input type=\"checkbox\" name=\"R11\" checked> R(b,b)</label></div>"
  },
  {
    "idx": 8,
    "unit": 4,
    "title": "Countermodel audit",
    "desc": "Check every premise and the disputed universal conclusion in the same model.",
    "type": "counter",
    "controls": "<div class=\"sim-controls\"><label><input type=\"checkbox\" name=\"P0\" checked> P(a)</label><label><input type=\"checkbox\" name=\"P1\"> P(b)</label><label><input type=\"checkbox\" name=\"Q0\"> Q(a)</label><label><input type=\"checkbox\" name=\"Q1\"> Q(b)</label></div>"
  },
  {
    "idx": 9,
    "unit": 5,
    "title": "Universal introduction restriction",
    "desc": "Observe what a named example proves and what a universal claim requires.",
    "type": "forallintro",
    "controls": "<div class=\"sim-controls\"><label><input type=\"checkbox\" name=\"P0\" checked> P(a)</label><label><input type=\"checkbox\" name=\"P1\"> P(b)</label></div>"
  },
  {
    "idx": 10,
    "unit": 5,
    "title": "Existential witness isolation",
    "desc": "Contrast a local witness with a globally asserted named conclusion.",
    "type": "existelim",
    "controls": "<div class=\"sim-controls\"><label><input type=\"checkbox\" name=\"P0\" checked> P(a)</label><label><input type=\"checkbox\" name=\"P1\"> P(b)</label><label><input type=\"checkbox\" name=\"Q0\" checked> Q(a)</label><label><input type=\"checkbox\" name=\"Q1\" checked> Q(b)</label></div>"
  },
  {
    "idx": 11,
    "unit": 6,
    "title": "Prenex step side conditions",
    "desc": "Test a safe quantifier move and a move where the side condition fails.",
    "type": "prenex",
    "controls": "<div class=\"sim-controls\"><label><input type=\"checkbox\" name=\"free\"> Q contains a free occurrence of x</label><p>Compare (\u2200xP(x)) \u2227 Q with \u2200x(P(x) \u2227 Q). The equivalence requires x not free in Q.</p></div>"
  },
  {
    "idx": 12,
    "unit": 6,
    "title": "Resolution refutation trace",
    "desc": "Follow a three-clause refutation including its substitution.",
    "type": "resolution",
    "controls": "<div class=\"sim-controls\"><label><select name=\"premise\"><option value=\"P\">P(a)</option><option value=\"notP\">\u00acP(a)</option></select></label><p>Rule clause: {\u00acP(x), Q(x)}; denied target: {\u00acQ(a)}.</p></div>"
  },
  {
    "idx": 13,
    "unit": 7,
    "title": "Partial-order axioms",
    "desc": "Check reflexivity, antisymmetry and transitivity over a finite relation.",
    "type": "poset",
    "controls": "<div class=\"sim-controls\"><label><input type=\"checkbox\" name=\"R00\" checked> R(a,a)</label><label><input type=\"checkbox\" name=\"R01\" checked> R(a,b)</label><label><input type=\"checkbox\" name=\"R10\"> R(b,a)</label><label><input type=\"checkbox\" name=\"R11\" checked> R(b,b)</label></div>"
  },
  {
    "idx": 14,
    "unit": 7,
    "title": "Bounded versus transitive reachability",
    "desc": "Contrast two-step paths with arbitrary-length graph reachability.",
    "type": "paths",
    "controls": "<div class=\"sim-controls\"><label><input type=\"checkbox\" name=\"R00\"> a\u2192a</label><label><input type=\"checkbox\" name=\"R01\" checked> a\u2192b</label><label><input type=\"checkbox\" name=\"R02\"> a\u2192c</label><label><input type=\"checkbox\" name=\"R10\"> b\u2192a</label><label><input type=\"checkbox\" name=\"R11\"> b\u2192b</label><label><input type=\"checkbox\" name=\"R12\" checked> b\u2192c</label><label><input type=\"checkbox\" name=\"R20\"> c\u2192a</label><label><input type=\"checkbox\" name=\"R21\"> c\u2192b</label><label><input type=\"checkbox\" name=\"R22\"> c\u2192c</label></div>"
  },
  {
    "idx": 15,
    "unit": 8,
    "title": "Research eligibility invariant",
    "desc": "Evaluate prerequisites under a sample policy with transparent assumptions.",
    "type": "policy",
    "controls": "<div class=\"sim-controls\"><label><input type=\"checkbox\" name=\"assigned\" checked> Assigned(s,p)</label><label><input type=\"checkbox\" name=\"eligible\" checked> Eligible(s,p)</label><label><input type=\"checkbox\" name=\"consent\"> Consented(s,p)</label><label><input type=\"checkbox\" name=\"capacity\" checked> CapacityAvailable(p)</label></div>"
  },
  {
    "idx": 16,
    "unit": 8,
    "title": "Datalog fixed-point closure",
    "desc": "Iterate a positive recursive reachability rule until no new tuples appear.",
    "type": "datalog",
    "controls": "<div class=\"sim-controls\"><label><input type=\"checkbox\" name=\"R00\"> a\u2192a</label><label><input type=\"checkbox\" name=\"R01\" checked> a\u2192b</label><label><input type=\"checkbox\" name=\"R02\"> a\u2192c</label><label><input type=\"checkbox\" name=\"R10\"> b\u2192a</label><label><input type=\"checkbox\" name=\"R11\"> b\u2192b</label><label><input type=\"checkbox\" name=\"R12\" checked> b\u2192c</label><label><input type=\"checkbox\" name=\"R20\"> c\u2192a</label><label><input type=\"checkbox\" name=\"R21\"> c\u2192b</label><label><input type=\"checkbox\" name=\"R22\"> c\u2192c</label></div>"
  }
];

  // Original calculation logic adapted for scoped execution
"use strict";
(function () {
function run(){

const $ = (sel) => document.querySelector(sel);
const kind = document.body.dataset.kind;
const input = (key) => document.querySelector('[name="'+key+'"]');
const yes = (key) => !!(input(key) && input(key).checked);
const val = (key) => input(key) ? input(key).value : '';
const flag = (b) => b ? 'TRUE' : 'FALSE';
const arr = (pre,n) => Array.from({length:n}, (_,i)=>yes(pre+i));
function relation(n) {return Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>yes('R'+i+j)));}
function fe(R) {return R.every(row=>row.some(Boolean));}
function ef(R) {return R.some((_,j)=>R.every(row=>row[j]));}
function transitive(R){let n=R.length;for(let i=0;i<n;i++)for(let j=0;j<n;j++)for(let k=0;k<n;k++)if(R[i][j]&&R[j][k]&&!R[i][k])return false;return true;}
function closure(R){let C=R.map(row=>row.slice()),steps=[];for(let n=0;n<R.length;n++){let N=C.map(row=>row.slice());for(let i=0;i<C.length;i++)for(let j=0;j<C.length;j++)for(let k=0;k<C.length;k++)if(C[i][k]&&C[k][j])N[i][j]=true;let count=N.flat().filter(Boolean).length;steps.push('iteration '+(n+1)+': '+count+' reachable ordered pairs');if(JSON.stringify(N)===JSON.stringify(C))break;C=N;}return [C,steps];}
let title='', lines=[];
switch(kind){
case 'scope': {let P=arr('P',2),Q=arr('Q',2),x=Number(val('x'));let full=P.every((p,i)=>!p||Q[i]),split=(!P.some(p=>!p))?Q[x]:true;title='Scope changes the formula';lines=[`∀x(P(x)→Q(x)) = ${flag(full)}`,`(∀xP(x))→Q(x) with free x=${x?'b':'a'} = ${flag(split)}`,'The second expression has x free. Changing the assignment can change its truth, unlike the first sentence.'];break;}
case 'sub': {let safe=val('choice')==='safe';title='Capture test';lines=[safe?'Correct: ∀zR(y,z), where z is fresh.':'Incorrect: ∀yR(y,y), produced by naive replacement.','The source ∀yR(x,y) has x free and y bound. The requested replacement term y must remain free.','A captured substitution changes which values are compared and may change truth.'];break;}
case 'restrict': {let A=arr('A',2),B=arr('B',2),univ=A.every((a,i)=>!a||B[i]),exist=A.some((a,i)=>a&&B[i]);title='Restricted quantifiers';lines=[`∀x(Student(x)→Approved(x)): ${flag(univ)}`,`∃x(Student(x)∧Approved(x)): ${flag(exist)}`,`Students in the domain: ${A.filter(Boolean).length}. If none exist, the universal is vacuously true.`];break;}
case 'unique': {let A=arr('A',2),n=A.filter(Boolean).length;title='How many witnesses?';lines=[`∃xP(x): ${flag(n>=1)}`,`At most one x satisfies P(x): ${flag(n<=1)}`,`Exactly one x satisfies P(x): ${flag(n===1)}`,`Witness count in D={a,b}: ${n}`];break;}
case 'rel':
case 'order': {let R=relation(2);title='Quantifier dependency';lines=[`∀x∃yR(x,y): ${flag(fe(R))}`,`∃y∀xR(x,y): ${flag(ef(R))}`,`Explicit true tuples: ${JSON.stringify(R.flatMap((row,i)=>row.flatMap((v,j)=>v?[[i?'b':'a',j?'b':'a']]:[])))}`];break;}
case 'assign': {let x=Number(val('x'));title='Truth under assignment';lines=[`R(x,c): ${flag(x===0)}`,`∃xR(x,c): TRUE`, 'The first expression is open and depends on the supplied value of x. The second is a sentence with witness a.'];break;}
case 'counter': {let P=arr('P',2),Q=arr('Q',2),prem=P.some(Boolean),concl=P.every((p,i)=>p||Q[i]),witness= prem&&!concl;title='Premise-versus-conclusion audit';lines=[`Premise ∃xP(x): ${flag(prem)}`,`Candidate conclusion ∀x(P(x)∨Q(x)): ${flag(concl)}`,`Genuine countermodel to entailment: ${flag(witness)}`,'A countermodel requires true premise and false conclusion in one and the same structure.'];break;}
case 'forallintro': {let P=arr('P',2);title='Generalization restriction';lines=[`P(a): ${flag(P[0])}`,`∀xP(x): ${flag(P.every(Boolean))}`,'P(a) follows from a claim about a. Generalizing to all x requires an arbitrary parameter not dependent on a-specific assumptions.'];break;}
case 'existelim': {let P=arr('P',2),Q=arr('Q',2),exist=P.some(Boolean),univ=P.every((p,i)=>!p||Q[i]);title='Fresh witness discipline';lines=[`∃xP(x): ${flag(exist)}`,`∀x(P(x)→Q(x)): ${flag(univ)}`,`∃xQ(x) follows if both premises hold: ${flag(exist&&univ)}`,'This derivation does not justify globally naming an unknown existential witness k.'];break;}
case 'prenex': {let free=yes('free');title='Quantifier movement';lines=[`Side condition x∉FV(Q): ${flag(!free)}`,free?'The transformation is not generally an equivalence; Q may depend on x.':'The transformation is valid in standard nonempty-domain semantics.', 'When side conditions fail, rename binders and reconsider the intended formula.'];break;}
case 'resolution': {let P=val('premise')==='P';title='Resolution certificate';lines=[`Input unit clause: {${P?'P(a)':'¬P(a)'}}`,`Rule clause: {¬P(x),Q(x)}; negated goal: {¬Q(a)}`,P?'Resolve using x↦a: {Q(a)}; then derive empty clause □.':'No complementary positive P(a) unit is available from these inputs. No refutation is shown.','An absent refutation in this toy case must not be reported as a general proof of invalidity.'];break;}
case 'poset': {let R=relation(2);let refl=R.every((row,i)=>row[i]),antis=R.every((row,i)=>row.every((x,j)=>i===j||!(x&&R[j][i]))),trans=transitive(R);title='Partial-order axioms';lines=[`Reflexive: ${flag(refl)}`,`Antisymmetric: ${flag(antis)}`,`Transitive: ${flag(trans)}`,`Partial order: ${flag(refl&&antis&&trans)}`];break;}
case 'paths':
case 'datalog': {let R=relation(3), [C,steps]=closure(R),two=R.some((row,k)=>R[0][k]&&R[k][2]);title='Graph path semantics';lines=[`Exactly two-step path from a to c: ${flag(two)}`,`Reachable by path of length ≥1 from a to c: ${flag(C[0][2])}`,...(kind==='datalog'?steps:['The two-step first-order formula is not arbitrary-length transitive closure.'])];break;}
case 'policy': {let assigned=yes('assigned'),eligible=yes('eligible'),consent=yes('consent'),cap=yes('capacity'),pass=!assigned||(eligible&&consent&&cap);title='Synthetic policy invariant';lines=[`Assigned(s,p) → (Eligible(s,p) ∧ Consented(s,p) ∧ CapacityAvailable(p)): ${flag(pass)}`,assigned?'An active assignment must satisfy every prerequisite.':'No assignment is present: the implication is true, but no matching activity is established.','All entries are illustrative toggles; they are not authenticated approvals or a production entitlement decision.'];break;}
default: {title='Unsupported example';lines=['No computation is defined for this model.'];}
}
$('#output').innerHTML='<h2>'+title+'</h2><ul>'+lines.map(s=>'<li>'+s+'</li>').join('')+'</ul><p class="small">Computed locally with the declared finite example; academic review pending.</p>';
}
run();
document.querySelectorAll('#controls input, #controls select').forEach(el=>el.addEventListener('change',run));
})();


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
