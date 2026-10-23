/* Operations Research for Statistics interactive teaching models and SVG visualizers. */
(function(root){
  'use strict';
  const doc = typeof document !== 'undefined' ? document : null;
  if(!doc) return;

  function range(v, a, b, name){
    if(!Number.isFinite(v) || v < a || v > b) throw Error(name + ' must be between ' + a + ' and ' + b + '.');
    return v;
  }

  function field(id, label, val, min, max, step){
    return `<label class="prob-control" for="${id}"><span>${label}</span><input type="number" id="${id}" value="${val}" min="${min}" max="${max}" step="${step}"/></label>`;
  }
  function select(id, label, options){
    const opts = options.map(([v, t]) => `<option value="${v}">${t}</option>`).join('');
    return `<label class="prob-control" for="${id}"><span>${label}</span><select id="${id}">${opts}</select></label>`;
  }
  function summary(vals){
    return '<div class="prob-summary">' + Object.entries(vals).map(([k, v]) => `<div><strong>${k}:</strong> <span>${v}</span></div>`).join('') + '</div>';
  }
  function fmt(n){
    if(n === null || n === undefined) return 'N/A';
    if(typeof n === 'string') return n;
    return Number.isFinite(n) ? (Math.abs(n) >= 1e4 || (Math.abs(n) < 1e-3 && n !== 0) ? n.toExponential(3) : n.toFixed(3)) : 'NaN';
  }

  function chart(seriesList, xMin, xMax, titleStr, vRef = null, hRef = null){
    const W = 620, H = 240, padL = 50, padR = 25, padT = 25, padB = 35;
    const plotW = W - padL - padR, plotH = H - padT - padB;

    let yMax = -Infinity, yMin = Infinity;
    seriesList.forEach(s => {
      s.values.forEach(([x, y]) => {
        if(Number.isFinite(y)){
          if(y > yMax) yMax = y;
          if(y < yMin) yMin = y;
        }
      });
    });

    if(!Number.isFinite(yMax) || yMax === yMin){ yMax = 1; yMin = 0; }
    if(yMin > 0 && yMin < yMax * 0.2) yMin = 0;
    const ySpan = (yMax - yMin) || 1;
    yMax += ySpan * 0.05;
    yMin -= ySpan * 0.05;

    function toSvg(x, y){
      const sx = padL + ((x - xMin) / (xMax - xMin || 1)) * plotW;
      const sy = padT + (1 - (y - yMin) / (yMax - yMin)) * plotH;
      return [sx, sy];
    }

    let paths = '';
    seriesList.forEach(s => {
      let d = '';
      s.values.forEach(([x, y], idx) => {
        const [sx, sy] = toSvg(x, y);
        d += (idx === 0 ? `M ${sx.toFixed(1)} ${sy.toFixed(1)}` : ` L ${sx.toFixed(1)} ${sy.toFixed(1)}`);
      });
      const dash = s.dashed ? 'stroke-dasharray="4,4"' : (s.dotted ? 'stroke-dasharray="2,3"' : '');
      paths += `<path d="${d}" fill="none" stroke="${s.color || '#38bdf8'}" stroke-width="${s.width || 2}" ${dash} />`;
    });

    let extra = '';
    if(vRef !== null && Number.isFinite(vRef) && vRef >= xMin && vRef <= xMax){
      const [vx] = toSvg(vRef, yMin);
      extra += `<line x1="${vx.toFixed(1)}" y1="${padT}" x2="${vx.toFixed(1)}" y2="${padT + plotH}" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3" />`;
    }
    if(hRef !== null && Number.isFinite(hRef) && hRef >= yMin && hRef <= yMax){
      const [, hy] = toSvg(xMin, hRef);
      extra += `<line x1="${padL}" y1="${hy.toFixed(1)}" x2="${padL + plotW}" y2="${hy.toFixed(1)}" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="2,2" />`;
    }

    let grid = `<line x1="${padL}" y1="${padT + plotH}" x2="${padL + plotW}" y2="${padT + plotH}" stroke="#334155" stroke-width="1"/>`;
    grid += `<line x1="${padL}" y1="${padT}" x2="${padL}" y2="${padT + plotH}" stroke="#334155" stroke-width="1"/>`;

    const xMid = (xMin + xMax) / 2;
    const yMid = (yMin + yMax) / 2;
    const ticks = `
      <text x="${padL}" y="${padT + plotH + 18}" fill="#94a3b8" font-size="11" text-anchor="middle">${fmt(xMin)}</text>
      <text x="${padL + plotW/2}" y="${padT + plotH + 18}" fill="#94a3b8" font-size="11" text-anchor="middle">${fmt(xMid)}</text>
      <text x="${padL + plotW}" y="${padT + plotH + 18}" fill="#94a3b8" font-size="11" text-anchor="middle">${fmt(xMax)}</text>
      <text x="${padL - 8}" y="${padT + plotH}" fill="#94a3b8" font-size="11" text-anchor="end">${fmt(yMin)}</text>
      <text x="${padL - 8}" y="${padT + plotH/2}" fill="#94a3b8" font-size="11" text-anchor="end">${fmt(yMid)}</text>
      <text x="${padL - 8}" y="${padT + 10}" fill="#94a3b8" font-size="11" text-anchor="end">${fmt(yMax)}</text>
    `;

    return `
      <div class="prob-chart">
        <svg viewBox="0 0 ${W} ${H}" width="100%" height="auto" style="display:block; max-height:280px; font-family:sans-serif;">
          <text x="${W/2}" y="16" fill="#f8fafc" font-size="12" font-weight="600" text-anchor="middle">${titleStr}</text>
          ${grid}
          ${extra}
          ${paths}
          ${ticks}
        </svg>
      </div>
    `;
  }

  // --- SIMULATION 1: 2D LP POLYHEDRAL FEASIBLE REGION & ISO-PROFIT ---
  function lpFeasibleModel(c1, c2, b1, b2){
    range(c1, 1, 100, 'Objective c1');
    range(c2, 1, 100, 'Objective c2');
    range(b1, 10, 120, 'Resource 1 RHS (2x1 + x2 <= b1)');
    range(b2, 10, 120, 'Resource 2 RHS (x1 + 2x2 <= b2)');

    // Constraints: 2*x1 + x2 <= b1, x1 + 2*x2 <= b2, x1,x2 >= 0
    const vertices = [[0, 0]];
    vertices.push([b1 / 2, 0]);
    vertices.push([0, b2 / 2]);
    // Intersection of 2x1+x2=b1 and x1+2x2=b2 => x1 = (2b1 - b2)/3, x2 = (2b2 - b1)/3
    const ix = (2 * b1 - b2) / 3;
    const iy = (2 * b2 - b1) / 3;
    if(ix >= 0 && iy >= 0){
      vertices.push([ix, iy]);
    }
    const feasible = vertices.filter(([x, y]) => (2*x + y <= b1 + 1e-7) && (x + 2*y <= b2 + 1e-7) && x >= -1e-7 && y >= -1e-7);

    let bestV = feasible[0], bestZ = -Infinity;
    feasible.forEach(v => {
      const z = c1 * v[0] + c2 * v[1];
      if(z > bestZ){ bestZ = z; bestV = v; }
    });

    const xMax = Math.max(b1, b2, 20);
    const line1 = [[0, b1], [b1 / 2, 0]];
    const line2 = [[0, b2 / 2], [b2, 0]];
    const isoLine = [[0, bestZ / c2], [bestZ / c1, 0]];

    return { bestV, bestZ, ix: Math.max(0, ix), iy: Math.max(0, iy), xMax, line1, line2, isoLine };
  }

  // --- SIMULATION 2: DUAL SHADOW PRICES & SENSITIVITY RANGE ---
  function sensitivityModel(c1, c2, deltaB1){
    range(c1, 10, 80, 'Profit c1');
    range(c2, 10, 80, 'Profit c2');
    range(deltaB1, -20, 40, 'Perturbation Delta b1');

    // Base problem: Max c1*x1 + c2*x2 s.t. 2x1 + x2 <= 100 + deltaB1, x1 + 2x2 <= 80
    // If both binding: B = [[2,1],[1,2]], B^-1 = (1/3)*[[2,-1],[-1,2]]
    const b1 = 100 + deltaB1, b2 = 80;
    const y1 = (2 * c1 - c2) / 3;
    const y2 = (2 * c2 - c1) / 3;
    const x1 = (2 * b1 - b2) / 3;
    const x2 = (2 * b2 - b1) / 3;
    const basisFeasible = x1 >= 0 && x2 >= 0 && y1 >= 0 && y2 >= 0;
    const zOpt = basisFeasible ? (c1 * x1 + c2 * x2) : Math.max(c1 * Math.min(b1/2, b2), c2 * Math.min(b1, b2/2));

    const curve = [];
    for(let db = -40; db <= 60; db += 4){
      const tb1 = 100 + db;
      // Exact LP optimum for varying tb1
      const cands = [[0,0], [Math.min(tb1/2, b2), 0], [0, Math.min(tb1, b2/2)]];
      const tx1 = (2*tb1 - b2)/3, tx2 = (2*b2 - tb1)/3;
      if(tx1 >= 0 && tx2 >= 0 && (2*tx1+tx2 <= tb1+1e-6) && (tx1+2*tx2 <= b2+1e-6)) cands.push([tx1, tx2]);
      const zVal = Math.max(...cands.map(([u,v]) => c1*u + c2*v));
      curve.push([tb1, zVal]);
    }

    return { b1, x1, x2, y1, y2, zOpt, basisFeasible, curve, minB1: 40, maxB1: 160 };
  }

  // --- SIMULATION 3: PERT CRITICAL PATH & COMPLETION PROBABILITY ---
  function pertModel(a, m, b, targetT){
    range(a, 2, 30, 'Optimistic Time a');
    range(m, a, 50, 'Most Likely Time m');
    range(b, m, 80, 'Pessimistic Time b');
    range(targetT, 10, 120, 'Target Deadline T_d');

    // Critical path consists of 3 sequential critical activities with scaled Beta parameters
    const mu1 = (a + 4*m + b) / 6;
    const var1 = Math.pow((b - a) / 6, 2);
    const totalMu = 3 * mu1;
    const totalVar = 3 * var1;
    const totalSd = Math.sqrt(totalVar) || 0.5;
    const z = (targetT - totalMu) / totalSd;

    // Normal CDF approximation
    function normCdf(x){
      const t = 1 / (1 + 0.2316419 * Math.abs(x));
      const d = 0.3989423 * Math.exp(-x * x / 2);
      const p = d * t * (0.3193815 + t * (-0.3565638 + t * (1.781478 + t * (-1.821256 + t * 1.330274))));
      return x > 0 ? 1 - p : p;
    }
    const prob = normCdf(z);

    const pdfCurve = [];
    const xMin = Math.max(0, totalMu - 4 * totalSd);
    const xMax = totalMu + 4 * totalSd;
    for(let i = 0; i <= 60; i++){
      const x = xMin + (i / 60) * (xMax - xMin);
      const u = (x - totalMu) / totalSd;
      const density = (1 / (totalSd * Math.sqrt(2 * Math.PI))) * Math.exp(-0.5 * u * u);
      pdfCurve.push([x, density]);
    }

    return { mu1, var1, totalMu, totalSd, z, prob, pdfCurve, xMin, xMax };
  }

  // --- SIMULATION 4: M/M/1 QUEUEING & EOQ INVENTORY EXPLORER ---
  function queueingEoqModel(lambda, mu, demandD, orderCostK, holdCostH){
    range(lambda, 0.5, 19.5, 'Arrival Rate lambda');
    range(mu, 1.0, 25.0, 'Service Rate mu');
    range(demandD, 100, 10000, 'Annual Demand D');
    range(orderCostK, 10, 1000, 'Setup Cost K');
    range(holdCostH, 0.5, 100, 'Holding Cost h');

    if(lambda >= mu) throw Error('Steady-state stability requires Arrival Rate λ < Service Rate μ (ρ < 1).');

    const rho = lambda / mu;
    const L = rho / (1 - rho);
    const Lq = (rho * rho) / (1 - rho);
    const W = 1 / (mu - lambda);
    const Wq = lambda / (mu * (mu - lambda));
    const eoq = Math.sqrt((2 * demandD * orderCostK) / holdCostH);
    const minTotalCost = Math.sqrt(2 * demandD * orderCostK * holdCostH);

    const queueCurve = [];
    for(let r = 0.05; r <= 0.95; r += 0.03){
      queueCurve.push([r, (r * r) / (1 - r)]);
    }

    return { rho, L, Lq, W, Wq, eoq, minTotalCost, queueCurve };
  }

  function initSimulation(containerId, type){
    const el = typeof containerId === 'string' ? doc.getElementById(containerId) : containerId;
    if(!el || el.dataset.simMounted) return;
    el.dataset.simMounted = 'true';
    el.classList.add('prob-explorer');

    const simType = type || el.dataset.sim;
    let title = '', note = '', controls = '';
    const idPrefix = typeof containerId === 'string' ? containerId : (el.id || simType);
    const f = (key, label, value, min, max, step) => field(idPrefix + '-' + key, label, value, min, max, step);

    if(simType === 'or-lp-feasible-region'){
      title = '2D Linear Programming Polyhedral Feasible Region & Extreme Point Explorer';
      note = 'Visualizes the boundary hyperplanes 2x₁ + x₂ ≤ b₁ (cyan) and x₁ + 2x₂ ≤ b₂ (green) along with the optimal iso-profit line (yellow dashed).';
      controls = f('c1', 'Unit Profit c₁', 40, 5, 100, 5)
        + f('c2', 'Unit Profit c₂', 30, 5, 100, 5)
        + f('b1', 'Resource 1 Capacity b₁', 60, 20, 120, 5)
        + f('b2', 'Resource 2 Capacity b₂', 48, 20, 120, 4);
    }else if(simType === 'or-sensitivity-shadow'){
      title = 'Primal-Dual Shadow Price & Right-Hand-Side Sensitivity Explorer';
      note = 'Tracks the optimal objective value Z*(b₁) across right-hand-side resource perturbations and shows the piecewise-linear concavity of the value function.';
      controls = f('c1', 'Objective Coefficient c₁', 50, 10, 80, 5)
        + f('c2', 'Objective Coefficient c₂', 40, 10, 80, 5)
        + f('deltaB1', 'RHS Perturbation Δb₁', 0, -20, 40, 5);
    }else if(simType === 'or-pert-critical-path'){
      title = 'Probabilistic PERT Three-Point Beta & Completion Probability Simulator';
      note = 'Computes the expected critical path duration μ_T, variance σ²_T, and Central Limit Theorem probability P(T ≤ T_d) of meeting a target project deadline.';
      controls = f('a', 'Optimistic Time a (days)', 6, 2, 20, 1)
        + f('m', 'Most Likely Time m (days)', 10, 6, 30, 1)
        + f('b', 'Pessimistic Time b (days)', 20, 12, 60, 2)
        + f('targetT', 'Target Deadline T_d (days)', 36, 15, 90, 1);
    }else if(simType === 'or-mm1-eoq-explorer'){
      title = 'Markovian M/M/1 Queue Congestion & Harris-Wilson EOQ Explorer';
      note = 'Evaluates steady-state M/M/1 queue length L_q = ρ²/(1-ρ), Little’s Law waiting times, and the Economic Order Quantity Q* = √(2DK/h).';
      controls = f('lambda', 'Arrival Rate λ (cust/hr)', 8.0, 1.0, 19.0, 0.5)
        + f('mu', 'Service Rate μ (cust/hr)', 10.0, 2.0, 24.0, 0.5)
        + f('demandD', 'Annual Demand D (units)', 2400, 200, 10000, 200)
        + f('orderCostK', 'Setup Cost K ($/order)', 150, 20, 500, 10)
        + f('holdCostH', 'Holding Cost h ($/unit/yr)', 18, 2, 60, 2);
    }else{
      return;
    }

    el.innerHTML = `
      <div class="prob-header">
        <div>
          <h3 class="prob-title">${title}</h3>
          <p class="prob-note">${note}</p>
        </div>
        <button type="button" class="prob-reset" data-reset>Reset</button>
      </div>
      <div class="prob-controls">${controls}</div>
      <div class="prob-result" data-result></div>
    `;

    const inputs = el.querySelectorAll('input, select');
    const result = el.querySelector('[data-result]');
    const initial = Array.from(inputs).map(inp => inp.value);

    function get(k){
      const target = el.querySelector('#' + idPrefix + '-' + k);
      return target ? parseFloat(target.value) : 0;
    }

    function render(){
      try{
        let values = {}, plot = '';
        if(simType === 'or-lp-feasible-region'){
          const m = lpFeasibleModel(get('c1'), get('c2'), get('b1'), get('b2'));
          values = {
            'Optimal Extreme Point (x₁*, x₂*)': `(${fmt(m.bestV[0])}, ${fmt(m.bestV[1])})`,
            'Maximum Objective Value Z*': fmt(m.bestZ),
            'Interior Vertex Intersection': `(${fmt(m.ix)}, ${fmt(m.iy)})`,
            'Slack s₁ (Resource 1)': fmt(Math.max(0, get('b1') - (2*m.bestV[0] + m.bestV[1]))),
            'Slack s₂ (Resource 2)': fmt(Math.max(0, get('b2') - (m.bestV[0] + 2*m.bestV[1])))
          };
          plot = chart([
            { values: m.line1, width: 2.5, color: '#38bdf8' },
            { values: m.line2, width: 2.5, color: '#10b981' },
            { values: m.isoLine, width: 2, dashed: true, color: '#fbbf24' }
          ], 0, m.xMax * 0.75, 'Constraint Lines 1 (Cyan) & 2 (Green) with Optimal Iso-Profit Line (Yellow)', m.bestV[0]);
        }
        if(simType === 'or-sensitivity-shadow'){
          const m = sensitivityModel(get('c1'), get('c2'), get('deltaB1'));
          values = {
            'Perturbed Resource RHS b₁': fmt(m.b1),
            'Dual Shadow Price y₁*': fmt(m.y1),
            'Dual Shadow Price y₂*': fmt(m.y2),
            'Current Optimal Objective Z*': fmt(m.zOpt),
            'Feasibility Range for b₁': `[${m.minB1}, ${m.maxB1}]`,
            'Current Basis Status': m.basisFeasible ? 'Both Constraints Binding' : 'Basis Changed (Corner Shift)'
          };
          plot = chart([
            { values: m.curve, width: 2.5, color: '#10b981' }
          ], 60, 160, 'Piecewise-Linear Concave Value Function Z*(b₁) vs Resource Capacity b₁', m.b1);
        }
        if(simType === 'or-pert-critical-path'){
          const m = pertModel(get('a'), get('m'), get('b'), get('targetT'));
          values = {
            'Single Activity Mean μ_i': fmt(m.mu1) + ' days',
            'Single Activity Variance σ²_i': fmt(m.var1),
            'Expected Project Duration μ_T': fmt(m.totalMu) + ' days',
            'Project Standard Deviation σ_T': fmt(m.totalSd) + ' days',
            'Standard Normal Z-Score': fmt(m.z),
            'Completion Probability P(T ≤ T_d)': fmt(m.prob * 100) + '%'
          };
          plot = chart([
            { values: m.pdfCurve, width: 2.5, color: '#38bdf8' }
          ], m.xMin, m.xMax, 'Normal Approximation of Critical Path Project Duration (Red Line = Deadline T_d)', get('targetT'));
        }
        if(simType === 'or-mm1-eoq-explorer'){
          const m = queueingEoqModel(get('lambda'), get('mu'), get('demandD'), get('orderCostK'), get('holdCostH'));
          values = {
            'Traffic Intensity ρ = λ/μ': fmt(m.rho) + ' (' + fmt(m.rho * 100) + '% util)',
            'Mean Number in System L': fmt(m.L) + ' customers',
            'Mean Queue Length L_q': fmt(m.Lq) + ' customers',
            'Mean Wait in Queue W_q': fmt(m.Wq * 60) + ' minutes',
            'Optimal EOQ Batch Size Q*': fmt(m.eoq) + ' units',
            'Min Annual Inventory Cost TC*': '$' + fmt(m.minTotalCost)
          };
          plot = chart([
            { values: m.queueCurve, width: 2.5, color: '#fbbf24' }
          ], 0.05, 0.95, 'Nonlinear Explosion of M/M/1 Queue Length L_q vs Utilization ρ (Red Line = Current ρ)', m.rho);
        }
        result.innerHTML = summary(values) + plot;
      }catch(err){
        result.textContent = err.message;
      }
    }

    inputs.forEach(input => input.addEventListener(input.tagName === 'SELECT' ? 'change' : 'input', render));
    el.querySelector('[data-reset]').addEventListener('click', () => {
      inputs.forEach((input, i) => input.value = initial[i]);
      render();
    });
    render();
  }

  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = initSimulation;
  root.OperationsResearchSimulationEngine = { initSimulation };
})(typeof window !== 'undefined' ? window : null);
