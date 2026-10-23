/* Statistical Research Methods interactive teaching models and SVG visualizers. */
(function(root){
  'use strict';
  const doc = typeof document !== 'undefined' ? document : null;
  if(!doc) return;

  function range(v, a, b, name){
    if(!Number.isFinite(v) || v < a || v > b) throw Error(name + ' must be between ' + a + ' and ' + b + '.');
    return v;
  }
  function integer(v, a, b, name){
    range(v, a, b, name);
    if(!Number.isInteger(v)) throw Error(name + ' must be an integer.');
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
    return '<div class="prob-summary stat-results" aria-live="polite">' + Object.entries(vals).map(([k, v]) => `<div><strong>${k}:</strong> <span>${v}</span></div>`).join('') + '</div>';
  }
  function fmt(n){
    if(n === null || n === undefined) return 'N/A';
    if(typeof n === 'string') return n;
    return Number.isFinite(n) ? (Math.abs(n) >= 1e4 || (Math.abs(n) < 1e-3 && n !== 0) ? n.toExponential(3) : n.toFixed(4)) : 'NaN';
  }

  // PRNG helper
  function mulberry32(a) {
    return function() {
      var t = a += 0x6D2B79F5;
      t = Math.imul(t ^ t >>> 15, t | 1);
      t ^= t + Math.imul(t ^ t >>> 7, t | 61);
      return ((t ^ t >>> 14) >>> 0) / 4294967296;
    }
  }

  // Standard Normal sampler (Box-Muller)
  function normalRandom(prng) {
    let u = 0, v = 0;
    while(u === 0) u = prng();
    while(v === 0) v = prng();
    return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
  }

  // Standard Normal CDF approximation (Hart's formula)
  function pnorm(z) {
    const a1 =  0.254829592, a2 = -0.284496736, a3 =  1.421413741;
    const a4 = -1.453152027, a5 =  1.061405429, p =  0.3275911;
    const sign = z < 0 ? -1 : 1;
    const x = Math.abs(z) / Math.SQRT2;
    const t = 1.0 / (1.0 + p * x);
    const erf = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * Math.exp(-x * x);
    return 0.5 * (1.0 + sign * erf);
  }

  // Standard Normal inverse CDF approximation
  function qnorm(p) {
    if(p <= 0) return -Infinity;
    if(p >= 1) return Infinity;
    if(p < 0.5) return -qnorm(1 - p);
    const t = Math.sqrt(-2.0 * Math.log(1.0 - p));
    const c0 = 2.515517, c1 = 0.802853, c2 = 0.010328;
    const d1 = 1.432788, d2 = 0.189269, d3 = 0.001308;
    return t - ((c2 * t + c1) * t + c0) / (((d3 * t + d2) * t + d1) * t + 1.0);
  }

  // 1. Statistical Power Calculator Model
  function powerModel(d, n, alpha){
    range(d, 0.05, 2.0, 'Effect size d');
    integer(n, 10, 500, 'Sample size n');
    range(alpha, 0.001, 0.20, 'Significance level alpha');

    const zCrit = qnorm(1.0 - alpha / 2.0);
    const delta = d * Math.sqrt(n / 2.0);

    // Two-tailed power approximation via normal approximation to non-central t
    const power = (1.0 - pnorm(zCrit - delta)) + pnorm(-zCrit - delta);
    const beta = Math.max(0, 1.0 - power);

    // Generate power curve data points across sample sizes n in [10, 300]
    const curve = [];
    for(let curN = 10; curN <= 300; curN += 10){
      const curDelta = d * Math.sqrt(curN / 2.0);
      const curP = (1.0 - pnorm(zCrit - curDelta)) + pnorm(-zCrit - curDelta);
      curve.push([curN, curP]);
    }

    return {
      d, n, alpha, zCrit, delta, power, beta, curve
    };
  }

  // 2. Causal DAG and d-Separation Model
  function dagModel(adjustZ, adjustM, adjustC){
    // Structure:
    // X -> M -> Y (Causal chain through mediator M)
    // X <- Z -> Y (Backdoor fork through confounder Z)
    // X -> C <- Y (Collider path through mutual effect C)
    // S -> Z (Optional)
    const paths = [
      { name: 'X → M → Y', type: 'Causal Chain (Direct/Indirect Effect)', blocked: adjustM, bias: adjustM ? 'Over-controlling (Blocks Causal Effect)' : 'None (Open Causal Path)' },
      { name: 'X ← Z → Y', type: 'Backdoor Path (Confounder Z)', blocked: adjustZ, bias: adjustZ ? 'None (Blocked by Z)' : 'Confounding Bias (Spurious Correlation)' },
      { name: 'X → C ← Y', type: 'Collider Path (Mutual Effect C)', blocked: !adjustC, bias: adjustC ? 'Collider Stratification Bias (M-Bias Opened!)' : 'None (Naturally Blocked by Collider)' }
    ];

    const hasConfounding = !adjustZ;
    const hasColliderBias = adjustC;
    const hasOvercontrol = adjustM;
    const isValidIdentification = adjustZ && !adjustM && !adjustC;

    return {
      adjustZ, adjustM, adjustC, paths, hasConfounding, hasColliderBias, hasOvercontrol, isValidIdentification
    };
  }

  // 3. Difference-in-Differences Model
  function didModel(preSlope, tauEffect, macroShock, groupGap){
    range(preSlope, -5.0, 5.0, 'Pre-trend slope');
    range(tauEffect, -10.0, 10.0, 'Treatment effect');
    range(macroShock, -5.0, 5.0, 'Macro shock');
    range(groupGap, -10.0, 10.0, 'Baseline gap');

    // Time points: t=0 (pre1), t=1 (pre2, policy baseline), t=2 (post)
    const yControlPre1 = 10.0;
    const yControlPre2 = yControlPre1 + preSlope;
    const yControlPost = yControlPre2 + preSlope + macroShock;

    const yTreatPre1 = yControlPre1 + groupGap;
    const yTreatPre2 = yTreatPre1 + preSlope;
    // Counterfactual without treatment:
    const yTreatCounterfactual = yTreatPre2 + preSlope + macroShock;
    // Actual observed with treatment:
    const yTreatPost = yTreatCounterfactual + tauEffect;

    const deltaTreat = yTreatPost - yTreatPre2;
    const deltaControl = yControlPost - yControlPre2;
    const didEstimate = deltaTreat - deltaControl;

    const preDiff1 = yTreatPre1 - yControlPre1;
    const preDiff2 = yTreatPre2 - yControlPre2;
    const parallelTrendsSatisfied = Math.abs(preDiff1 - preDiff2) < 1e-4;

    return {
      yControl: [yControlPre1, yControlPre2, yControlPost],
      yTreat: [yTreatPre1, yTreatPre2, yTreatPost],
      yCounterfactual: [yTreatPre1, yTreatPre2, yTreatCounterfactual],
      tauEffect, didEstimate, parallelTrendsSatisfied, deltaTreat, deltaControl
    };
  }

  // 4. Funnel Plot and Publication Bias Model
  function funnelModel(kStudies, trueTheta, biasSeverity, seed){
    integer(kStudies, 15, 120, 'Number of studies');
    range(trueTheta, -0.5, 1.5, 'True effect theta');
    const prng = mulberry32(seed || 888);

    const studies = [];
    let attempts = 0;

    while(studies.length < kStudies && attempts < kStudies * 20){
      attempts++;
      // Standard error distributed between 0.08 (large trial) and 0.50 (small study)
      const se = 0.08 + 0.42 * (prng() ** 1.5);
      const obsTheta = trueTheta + se * normalRandom(prng);
      const z = obsTheta / se;
      const p = 2 * (1 - pnorm(Math.abs(z)));

      // Publication bias filter:
      let publishProb = 1.0;
      if(obsTheta <= 0 || p > 0.05){
        if(biasSeverity === 'mild') publishProb = 0.40;
        else if(biasSeverity === 'severe') publishProb = 0.08;
      }

      if(prng() <= publishProb){
        studies.push({ theta: obsTheta, se, z, p, orig: true });
      }
    }

    // Egger's regression: Z_i = b0 + b1 * (1/SE_i)
    let sumX = 0, sumY = 0, sumXX = 0, sumXY = 0;
    const n = studies.length;
    for(let s of studies){
      const x = 1.0 / s.se;
      const y = s.z;
      sumX += x;
      sumY += y;
      sumXX += x * x;
      sumXY += x * y;
    }
    const b1 = (n * sumXY - sumX * sumY) / (n * sumXX - sumX * sumX);
    const b0 = (sumY - b1 * sumX) / n;

    // Naive pooled inverse-variance fixed effect
    let sumW = 0, sumWTheta = 0;
    for(let s of studies){
      const w = 1.0 / (s.se * s.se);
      sumW += w;
      sumWTheta += w * s.theta;
    }
    const naivePooled = sumWTheta / sumW;

    return {
      k: n, trueTheta, naivePooled, eggerIntercept: b0, eggerSlope: b1, studies, biasSeverity
    };
  }

  // SVG Chart rendering
  function renderPowerPlot(m){
    const w = 480, h = 220, pad = 40;
    const pts = m.curve.map(([xVal, pVal]) => {
      const x = pad + ((xVal - 10) / (300 - 10)) * (w - 2 * pad);
      const y = h - pad - pVal * (h - 2 * pad);
      return `${x.toFixed(1)},${y.toFixed(1)}`;
    });

    const curX = pad + ((m.n - 10) / (300 - 10)) * (w - 2 * pad);
    const curY = h - pad - m.power * (h - 2 * pad);
    const benchmark80Y = h - pad - 0.80 * (h - 2 * pad);

    return `<svg viewBox="0 0 ${w} ${h}" class="prob-svg" style="width:100%;max-width:540px;background:#0f172a;border-radius:8px;">
      <text x="${w/2}" y="20" fill="#f8fafc" font-size="12" font-weight="600" text-anchor="middle">Statistical Power Curve P(Reject H0 | d = ${m.d}, α = ${m.alpha})</text>
      <line x1="${pad}" y1="${h - pad}" x2="${w - pad}" y2="${h - pad}" stroke="#64748b" stroke-width="1.5"/>
      <line x1="${pad}" y1="${pad}" x2="${pad}" y2="${h - pad}" stroke="#64748b" stroke-width="1.5"/>
      <line x1="${pad}" y1="${benchmark80Y}" x2="${w - pad}" y2="${benchmark80Y}" stroke="#ef4444" stroke-width="1" stroke-dasharray="4"/>
      <text x="${w - pad - 5}" y="${benchmark80Y - 4}" fill="#ef4444" font-size="9" text-anchor="end">80% Target</text>
      <polyline points="${pts.join(' ')}" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      <circle cx="${curX}" cy="${curY}" r="5" fill="#f59e0b"/>
      <text x="${curX + 8}" y="${curY - 6}" fill="#f59e0b" font-size="10" font-weight="600">${(m.power * 100).toFixed(1)}% (n = ${m.n})</text>
      <text x="${pad}" y="${h - 12}" fill="#94a3b8" font-size="10">n = 10</text>
      <text x="${w - pad}" y="${h - 12}" fill="#94a3b8" font-size="10" text-anchor="end">n = 300</text>
    </svg>`;
  }

  function renderDagPlot(m){
    const w = 480, h = 220;
    // Nodes: X (Treatment: 100, 110), Y (Outcome: 380, 110), Z (Confounder: 240, 40), M (Mediator: 240, 110), C (Collider: 240, 180)
    function nodeCol(isAdj){ return isAdj ? '#3b82f6' : '#1e293b'; }
    function strokeCol(isAdj){ return isAdj ? '#60a5fa' : '#475569'; }

    return `<svg viewBox="0 0 ${w} ${h}" class="prob-svg" style="width:100%;max-width:540px;background:#0f172a;border-radius:8px;">
      <defs>
        <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 0 L 10 5 L 0 10 z" fill="#94a3b8"/>
        </marker>
        <marker id="arrow-blue" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/>
        </marker>
      </defs>
      <!-- Edges -->
      <line x1="125" y1="110" x2="215" y2="110" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-blue)"/>
      <line x1="265" y1="110" x2="355" y2="110" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-blue)"/>
      <line x1="225" y1="55" x2="115" y2="95" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#arrow)"/>
      <line x1="255" y1="55" x2="365" y2="95" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#arrow)"/>
      <line x1="115" y1="125" x2="225" y2="165" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#arrow)"/>
      <line x1="365" y1="125" x2="255" y2="165" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#arrow)"/>
      
      <!-- Nodes -->
      <circle cx="100" cy="110" r="22" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
      <text x="100" y="114" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">X</text>
      
      <circle cx="380" cy="110" r="22" fill="#059669" stroke="#34d399" stroke-width="2"/>
      <text x="380" y="114" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">Y</text>
      
      <circle cx="240" cy="40" r="18" fill="${nodeCol(m.adjustZ)}" stroke="${strokeCol(m.adjustZ)}" stroke-width="2"/>
      <text x="240" y="44" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">Z</text>
      <text x="240" y="18" fill="#94a3b8" font-size="9" text-anchor="middle">Confounder</text>
      
      <circle cx="240" cy="110" r="18" fill="${nodeCol(m.adjustM)}" stroke="${strokeCol(m.adjustM)}" stroke-width="2"/>
      <text x="240" y="114" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">M</text>
      <text x="240" y="90" fill="#94a3b8" font-size="9" text-anchor="middle">Mediator</text>
      
      <circle cx="240" cy="180" r="18" fill="${nodeCol(m.adjustC)}" stroke="${strokeCol(m.adjustC)}" stroke-width="2"/>
      <text x="240" y="184" fill="#f8fafc" font-size="11" font-weight="600" text-anchor="middle">C</text>
      <text x="240" y="208" fill="#94a3b8" font-size="9" text-anchor="middle">Collider</text>
    </svg>`;
  }

  function renderDidPlot(m){
    const w = 480, h = 220, pad = 45;
    const x0 = pad, x1 = w / 2, x2 = w - pad;
    const allY = [...m.yControl, ...m.yTreat, ...m.yCounterfactual];
    const minY = Math.min(...allY) - 2;
    const maxY = Math.max(...allY) + 2;

    function scaleY(v){ return h - pad - ((v - minY) / (maxY - minY)) * (h - 2 * pad); }

    const cPts = `${x0},${scaleY(m.yControl[0])} ${x1},${scaleY(m.yControl[1])} ${x2},${scaleY(m.yControl[2])}`;
    const tPts = `${x0},${scaleY(m.yTreat[0])} ${x1},${scaleY(m.yTreat[1])} ${x2},${scaleY(m.yTreat[2])}`;
    const cfPts = `${x1},${scaleY(m.yTreat[1])} ${x2},${scaleY(m.yCounterfactual[2])}`;

    return `<svg viewBox="0 0 ${w} ${h}" class="prob-svg" style="width:100%;max-width:540px;background:#0f172a;border-radius:8px;">
      <text x="${w/2}" y="20" fill="#f8fafc" font-size="12" font-weight="600" text-anchor="middle">Difference-in-Differences Panel Trajectory</text>
      <!-- Policy timing vertical line -->
      <line x1="${x1}" y1="${pad}" x2="${x1}" y2="${h - pad}" stroke="#475569" stroke-width="1.5" stroke-dasharray="3"/>
      <text x="${x1}" y="${pad - 6}" fill="#94a3b8" font-size="9" text-anchor="middle">Intervention (t = 1)</text>

      <!-- Lines -->
      <polyline points="${cPts}" fill="none" stroke="#64748b" stroke-width="2.5"/>
      <polyline points="${tPts}" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      <polyline points="${cfPts}" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4"/>

      <!-- Points -->
      <circle cx="${x2}" cy="${scaleY(m.yTreat[2])}" r="4" fill="#38bdf8"/>
      <circle cx="${x2}" cy="${scaleY(m.yCounterfactual[2])}" r="4" fill="#f59e0b"/>
      <circle cx="${x2}" cy="${scaleY(m.yControl[2])}" r="4" fill="#64748b"/>

      <!-- Labels -->
      <text x="${x0}" y="${h - 12}" fill="#94a3b8" font-size="10">Pre 1 (t=0)</text>
      <text x="${x1}" y="${h - 12}" fill="#94a3b8" font-size="10" text-anchor="middle">Pre 2 (t=1)</text>
      <text x="${x2}" y="${h - 12}" fill="#94a3b8" font-size="10" text-anchor="end">Post (t=2)</text>

      <text x="${pad + 10}" y="${pad + 15}" fill="#38bdf8" font-size="9">■ Treatment Group</text>
      <text x="${pad + 10}" y="${pad + 28}" fill="#64748b" font-size="9">■ Control Group</text>
      <text x="${pad + 10}" y="${pad + 41}" fill="#f59e0b" font-size="9">-- Counterfactual (No Treatment)</text>
    </svg>`;
  }

  function renderFunnelPlot(m){
    const w = 480, h = 220, pad = 40;
    const studies = m.studies;
    const minTheta = -1.0, maxTheta = 2.0;
    const maxSE = 0.55;

    function scaleX(v){ return pad + ((v - minTheta) / (maxTheta - minTheta)) * (w - 2 * pad); }
    function scaleY(se){ return pad + (se / maxSE) * (h - 2 * pad); } // SE increases downward

    // Funnel boundary lines (95% CI around trueTheta)
    const topX = scaleX(m.trueTheta);
    const topY = scaleY(0);
    const botLeftX = scaleX(m.trueTheta - 1.96 * maxSE);
    const botRightX = scaleX(m.trueTheta + 1.96 * maxSE);
    const botY = scaleY(maxSE);

    let dots = '';
    for(let s of studies){
      const cx = scaleX(s.theta);
      const cy = scaleY(s.se);
      const col = s.p < 0.05 ? '#10b981' : '#64748b';
      dots += `<circle cx="${cx.toFixed(1)}" cy="${cy.toFixed(1)}" r="3" fill="${col}" opacity="0.8"/>`;
    }

    return `<svg viewBox="0 0 ${w} ${h}" class="prob-svg" style="width:100%;max-width:540px;background:#0f172a;border-radius:8px;">
      <text x="${w/2}" y="20" fill="#f8fafc" font-size="12" font-weight="600" text-anchor="middle">Inverted Funnel Plot (Effect vs Standard Error)</text>
      <line x1="${topX}" y1="${topY}" x2="${topX}" y2="${botY}" stroke="#38bdf8" stroke-width="1.5"/>
      <line x1="${topX}" y1="${topY}" x2="${botLeftX}" y2="${botY}" stroke="#64748b" stroke-width="1" stroke-dasharray="3"/>
      <line x1="${topX}" y1="${topY}" x2="${botRightX}" y2="${botY}" stroke="#64748b" stroke-width="1" stroke-dasharray="3"/>
      ${dots}
      <text x="${topX}" y="${h - 10}" fill="#38bdf8" font-size="9" text-anchor="middle">True θ = ${fmt(m.trueTheta)}</text>
      <text x="${pad}" y="${pad + 12}" fill="#94a3b8" font-size="9">High Precision (SE ↓)</text>
      <text x="${pad}" y="${h - 24}" fill="#94a3b8" font-size="9">Low Precision (SE ↑)</text>
    </svg>`;
  }

  function initSimulation(el){
    const simType = el.getAttribute('data-sim');
    let controls = '';

    if(simType === 'res-power-calculator'){
      controls = field('pwrD', "Cohen's Effect Size d", 0.50, 0.10, 1.50, 0.05) +
                 field('pwrN', 'Sample Size per Group n', 64, 10, 400, 5) +
                 select('pwrAlpha', 'Significance Level α', [['0.05', 'α = 0.05 (Two-tailed)'], ['0.01', 'α = 0.01 (Strict)'], ['0.10', 'α = 0.10 (Exploratory)']]);
    } else if(simType === 'res-dag-confounding'){
      controls = select('dagZ', 'Condition on Confounder Z', [['0', 'Do NOT Adjust for Z'], ['1', 'Adjust for Z (Blocks Backdoor Path)']]) +
                 select('dagM', 'Condition on Mediator M', [['0', 'Do NOT Adjust for M'], ['1', 'Adjust for M (Over-controlling!)']]) +
                 select('dagC', 'Condition on Collider C', [['0', 'Do NOT Adjust for C'], ['1', 'Adjust for C (Opens Collider Bias / M-Bias!)']]);
    } else if(simType === 'res-did-estimator'){
      controls = field('didTau', 'True Policy Treatment Effect τ', -2.5, -6.0, 6.0, 0.5) +
                 field('didMacro', 'Common Macroeconomic Shock', 1.0, -4.0, 4.0, 0.5) +
                 field('didGap', 'Baseline Group Gap', 3.0, -5.0, 8.0, 0.5);
    } else if(simType === 'res-funnel-publication-bias'){
      controls = field('fnlK', 'Number of Published Studies k', 45, 15, 100, 5) +
                 field('fnlTheta', 'True Population Effect θ', 0.20, -0.20, 1.0, 0.05) +
                 select('fnlBias', 'Publication Bias Severity', [['none', 'None (All Studies Published)'], ['mild', 'Mild (Selective Acceptance)'], ['severe', 'Severe (Heavy File-Drawer Suppression)']]);
    }

    el.innerHTML = `<div class="prob-panel">
      <div class="prob-controls">${controls}</div>
      <div class="prob-actions"><button type="button" class="btn btn-secondary" data-reset>Reset</button></div>
      <div class="prob-output"></div>
    </div>`;

    const result = el.querySelector('.prob-output');
    const inputs = Array.from(el.querySelectorAll('input, select'));
    const initial = inputs.map(input => input.value);

    function get(id){
      const el = doc.getElementById(id);
      return el ? (el.tagName === 'SELECT' ? el.value : parseFloat(el.value)) : 0;
    }

    function render(){
      try{
        let values = {};
        let plot = '';

        if(simType === 'res-power-calculator'){
          const m = powerModel(get('pwrD'), Math.round(get('pwrN')), parseFloat(get('pwrAlpha')));
          values = {
            'Statistical Power (1 - β)': `${(m.power * 100).toFixed(2)}%`,
            'Type II Error Rate (β)': `${(m.beta * 100).toFixed(2)}%`,
            'Non-Centrality Parameter δ': fmt(m.delta),
            'Critical Threshold z_crit': fmt(m.zCrit),
            'Total Trial Sample Size N': m.n * 2
          };
          plot = renderPowerPlot(m);
        } else if(simType === 'res-dag-confounding'){
          const m = dagModel(get('dagZ') === '1', get('dagM') === '1', get('dagC') === '1');
          values = {
            'Causal Identification Status': m.isValidIdentification ? 'VALID IDENTIFICATION (Unbiased)' : 'BIASED ESTIMATOR',
            'Confounding Bias': m.hasConfounding ? 'PRESENT (Backdoor Path X ← Z → Y is Open)' : 'NEUTRALIZED (Blocked by Z)',
            'Collider Stratification Bias (M-Bias)': m.hasColliderBias ? 'ALERT: Collider C is Conditioned! Spurious association induced!' : 'SAFE (Collider C is Unconditioned)',
            'Over-controlling (Mediator Blocking)': m.hasOvercontrol ? 'ALERT: Mediator M is Conditioned! Causal mechanism blocked!' : 'SAFE (Causal mechanism open)'
          };
          plot = renderDagPlot(m);
        } else if(simType === 'res-did-estimator'){
          const m = didModel(0.5, get('didTau'), get('didMacro'), get('didGap'));
          values = {
            'True Causal Policy Effect τ': fmt(m.tauEffect),
            'Estimated Difference-in-Differences (DiD)': fmt(m.didEstimate),
            'Treatment Group Pre-to-Post Change': fmt(m.deltaTreat),
            'Control Group Pre-to-Post Change': fmt(m.deltaControl),
            'Parallel Trends Assumption': m.parallelTrendsSatisfied ? 'SATISFIED (Pre-treatment slopes identical)' : 'VIOLATED'
          };
          plot = renderDidPlot(m);
        } else if(simType === 'res-funnel-publication-bias'){
          const m = funnelModel(Math.round(get('fnlK')), get('fnlTheta'), get('fnlBias'), 888);
          values = {
            'True Population Effect θ': fmt(m.trueTheta),
            'Naive Pooled Meta-Analytic Effect': fmt(m.naivePooled),
            "Egger's Regression Intercept β0": fmt(m.eggerIntercept),
            'Funnel Asymmetry Status': Math.abs(m.eggerIntercept) > 0.8 ? 'ASYMMETRIC (Publication Bias Detected!)' : 'SYMMETRICAL (Low Bias Risk)',
            'Published Studies Analyzed': m.k
          };
          plot = renderFunnelPlot(m);
        }

        result.innerHTML = summary(values) + plot;
      }catch(err){
        result.textContent = err.message;
      }
    }

    inputs.forEach(input => input.addEventListener(input.tagName === 'SELECT' ? 'change' : 'input', render));
    const resetBtn = el.querySelector('[data-reset]');
    if(resetBtn){
      resetBtn.addEventListener('click', () => {
        inputs.forEach((input, i) => input.value = initial[i]);
        render();
      });
    }
    render();
  }

  root.SimulationEngine = root.SimulationEngine || {};
  root.SimulationEngine.initSimulation = initSimulation;
  root.StatisticalResearchSimulationEngine = { initSimulation };
})(typeof window !== 'undefined' ? window : null);
