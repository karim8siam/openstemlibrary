/* Epidemiological Statistics interactive teaching models and SVG visualizers. */
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
      <text x="${padL}" y="${H - 12}" fill="#94a3b8" text-anchor="middle">${fmt(xMin)}</text>
      <text x="${padL + plotW / 2}" y="${H - 12}" fill="#94a3b8" text-anchor="middle">${fmt(xMid)}</text>
      <text x="${padL + plotW}" y="${H - 12}" fill="#94a3b8" text-anchor="middle">${fmt(xMax)}</text>
      <text x="${padL - 8}" y="${padT + plotH}" fill="#94a3b8" text-anchor="end" dominant-baseline="middle">${fmt(yMin)}</text>
      <text x="${padL - 8}" y="${padT + plotH / 2}" fill="#94a3b8" text-anchor="end" dominant-baseline="middle">${fmt(yMid)}</text>
      <text x="${padL - 8}" y="${padT}" fill="#94a3b8" text-anchor="end" dominant-baseline="middle">${fmt(yMax)}</text>
    `;

    const titleSvg = `<text x="${W / 2}" y="16" fill="#7dd3fc" text-anchor="middle" font-weight="600" font-size="12">${titleStr}</text>`;

    return `<svg class="prob-chart" viewBox="0 0 ${W} ${H}" width="100%" height="auto" aria-label="${titleStr}">${titleSvg}${grid}${extra}${paths}${ticks}</svg>`;
  }

  // --- SIMULATION 1: MEASURES OF ASSOCIATION & CONFIDENCE INTERVALS ---
  function epiMeasuresModel(a, b, c, d){
    range(a, 1, 2000, 'Exposed cases (a)');
    range(b, 1, 5000, 'Exposed non-cases (b)');
    range(c, 1, 2000, 'Unexposed cases (c)');
    range(d, 1, 5000, 'Unexposed non-cases (d)');

    const n1 = a + b;
    const n0 = c + d;
    const r1 = a / n1;
    const r0 = c / n0;
    const rr = r1 / r0;
    const rd = r1 - r0;
    const orVal = (a * d) / (b * c);

    // Delta method CIs
    const seLnRr = Math.sqrt(1/a - 1/n1 + 1/c - 1/n0);
    const rrLow = rr * Math.exp(-1.96 * seLnRr);
    const rrHigh = rr * Math.exp(1.96 * seLnRr);

    const seLnOr = Math.sqrt(1/a + 1/b + 1/c + 1/d);
    const orLow = orVal * Math.exp(-1.96 * seLnOr);
    const orHigh = orVal * Math.exp(1.96 * seLnOr);

    const seRd = Math.sqrt((r1 * (1 - r1)) / n1 + (r0 * (1 - r0)) / n0);
    const rdLow = rd - 1.96 * seRd;
    const rdHigh = rd + 1.96 * seRd;

    const pTotal = (a + c) / (n1 + n0);
    const paf = ((pTotal - r0) / pTotal) * 100;
    const nnt = rd > 0 ? (1 / rd) : Infinity;

    // Visual comparison curve across hypothetical baseline risks r0 in [0.01, 0.40]
    const rrCurve = [], orCurve = [];
    for(let r = 0.01; r <= 0.40; r += 0.01){
      const hypR1 = Math.min(0.95, r * rr);
      rrCurve.push([r, rr]);
      const hypOr = (hypR1 / (1 - hypR1)) / (r / (1 - r));
      orCurve.push([r, hypOr]);
    }

    return {
      r1, r0, rr, rrLow, rrHigh, orVal, orLow, orHigh, rd, rdLow, rdHigh, paf, nnt,
      rrCurve, orCurve
    };
  }

  // --- SIMULATION 2: STRATIFIED CONFOUNDING & MANTEL-HAENSZEL POOLED OR ---
  function epiStratModel(a1, b1, c1, d1, a2, b2, c2, d2){
    range(a1, 1, 1000, 'Stratum 1 a1');
    range(b1, 1, 2000, 'Stratum 1 b1');
    range(c1, 1, 1000, 'Stratum 1 c1');
    range(d1, 1, 2000, 'Stratum 1 d1');
    range(a2, 1, 1000, 'Stratum 2 a2');
    range(b2, 1, 2000, 'Stratum 2 b2');
    range(c2, 1, 1000, 'Stratum 2 c2');
    range(d2, 1, 2000, 'Stratum 2 d2');

    // Stratum-specific odds ratios
    const or1 = (a1 * d1) / (b1 * c1);
    const or2 = (a2 * d2) / (b2 * c2);

    // Crude 2x2 table
    const aTot = a1 + a2, bTot = b1 + b2, cTot = c1 + c2, dTot = d1 + d2;
    const orCrude = (aTot * dTot) / (bTot * cTot);

    // Mantel-Haenszel pooled OR
    const N1 = a1 + b1 + c1 + d1;
    const N2 = a2 + b2 + c2 + d2;
    const numMH = (a1 * d1) / N1 + (a2 * d2) / N2;
    const denMH = (b1 * c1) / N1 + (b2 * c2) / N2;
    const orMH = numMH / denMH;

    // Confounding percentage
    const confoundingPct = ((orCrude - orMH) / orMH) * 100;

    // Robins-Breslow-Greenland variance of ln(OR_MH)
    const P1 = (a1 + d1) / N1, Q1 = (b1 + c1) / N1;
    const P2 = (a2 + d2) / N2, Q2 = (b2 + c2) / N2;
    const R1 = (a1 * d1) / N1, S1 = (b1 * c1) / N1;
    const R2 = (a2 * d2) / N2, S2 = (b2 * c2) / N2;
    const R_sum = R1 + R2, S_sum = S1 + S2;
    const varLnOrMH = ((P1*R1 + P2*R2)/(2*R_sum*R_sum)) + ((P1*S1 + Q1*R1 + P2*S2 + Q2*R2)/(2*R_sum*S_sum)) + ((Q1*S1 + Q2*S2)/(2*S_sum*S_sum));
    const seMH = Math.sqrt(varLnOrMH);
    const orMHLow = orMH * Math.exp(-1.96 * seMH);
    const orMHHigh = orMH * Math.exp(1.96 * seMH);

    // Bar chart points for comparison
    const barSeries = [
      [1, orCrude],
      [2, or1],
      [3, or2],
      [4, orMH]
    ];

    return {
      orCrude, or1, or2, orMH, orMHLow, orMHHigh, confoundingPct, barSeries
    };
  }

  // --- SIMULATION 3: DIAGNOSTIC ROC CURVE & LIKELIHOOD RATIOS ---
  function epiRocModel(deltaMu, cutoff, prevalence){
    range(deltaMu, 0.5, 3.5, 'Separation deltaMu');
    range(cutoff, -2.5, 3.5, 'Cutoff threshold');
    range(prevalence, 0.01, 0.50, 'Prevalence');

    // Standard Gaussian cumulative distribution approximation
    function normalCdf(x){
      const t = 1 / (1 + 0.2316419 * Math.abs(x));
      const d = 0.39894228 * Math.exp(-x * x / 2);
      const prob = d * t * (0.3193815 + t * (-0.3565638 + t * (1.781478 + t * (-1.821256 + t * 1.330274))));
      return x > 0 ? 1 - prob : prob;
    }

    // Diseased: N(deltaMu, 1), Healthy: N(0, 1)
    // Positive test if X >= cutoff
    const sp = normalCdf(cutoff);
    const se = 1 - normalCdf(cutoff - deltaMu);
    const fpr = 1 - sp;

    const ppv = (se * prevalence) / (se * prevalence + fpr * (1 - prevalence));
    const npv = (sp * (1 - prevalence)) / ((1 - se) * prevalence + sp * (1 - prevalence));

    const lrPlus = fpr > 1e-4 ? (se / fpr) : 999;
    const lrMinus = sp > 1e-4 ? ((1 - se) / sp) : 0;
    const youdenJ = se + sp - 1;

    // ROC curve series across cutoff from -3.5 to 3.5 + deltaMu
    const rocCurve = [];
    const diagLine = [];
    for(let c = -3.5; c <= 4.5; c += 0.1){
      const cFpr = 1 - normalCdf(c);
      const cSe = 1 - normalCdf(c - deltaMu);
      rocCurve.push([cFpr, cSe]);
      diagLine.push([cFpr, cFpr]);
    }

    // Area Under Curve (AUC) for two normals with equal variance is Phi(deltaMu / sqrt(2))
    const auc = normalCdf(deltaMu / Math.SQRT2);

    return {
      se, sp, fpr, ppv, npv, lrPlus, lrMinus, youdenJ, auc,
      rocCurve, diagLine, operatingPoint: [fpr, se]
    };
  }

  // --- SIMULATION 4: KERMACK-MCKENDRICK SIR EPIDEMIC TRANSMISSION ---
  function epiSirModel(beta, gamma, popN, initI, days){
    range(beta, 0.05, 1.0, 'Transmission rate beta');
    range(gamma, 0.02, 0.5, 'Recovery rate gamma');
    range(popN, 1000, 1000000, 'Population N');
    range(initI, 1, 100, 'Initial infected I0');
    range(days, 30, 200, 'Simulation days');

    const r0 = beta / gamma;
    const hit = r0 > 1 ? (1 - 1 / r0) * 100 : 0;

    // Runge-Kutta 4th-order ODE integration for SIR
    let S = popN - initI;
    let I = initI;
    let R = 0;
    const dt = 0.2;
    const steps = Math.floor(days / dt);

    const sCurve = [], iCurve = [], rCurve = [];
    let peakI = 0, peakDay = 0;

    for(let step = 0; step <= steps; step++){
      const t = step * dt;
      if(step % 5 === 0){
        sCurve.push([t, S / popN]);
        iCurve.push([t, I / popN]);
        rCurve.push([t, R / popN]);
      }
      if(I > peakI){
        peakI = I;
        peakDay = t;
      }

      // Derivatives f(S, I)
      function dS(s, i){ return -beta * s * i / popN; }
      function dI(s, i){ return beta * s * i / popN - gamma * i; }

      const k1_S = dS(S, I);
      const k1_I = dI(S, I);

      const k2_S = dS(S + 0.5 * dt * k1_S, I + 0.5 * dt * k1_I);
      const k2_I = dI(S + 0.5 * dt * k1_S, I + 0.5 * dt * k1_I);

      const k3_S = dS(S + 0.5 * dt * k2_S, I + 0.5 * dt * k2_I);
      const k3_I = dI(S + 0.5 * dt * k2_S, I + 0.5 * dt * k2_I);

      const k4_S = dS(S + dt * k3_S, I + dt * k3_I);
      const k4_I = dI(S + dt * k3_S, I + dt * k3_I);

      S += (dt / 6) * (k1_S + 2*k2_S + 2*k3_S + k4_S);
      I += (dt / 6) * (k1_I + 2*k2_I + 2*k3_I + k4_I);
      R = popN - S - I;
      if(I < 0) I = 0;
    }

    const finalAttackRate = (R / popN) * 100;

    return {
      r0, hit, peakFraction: (peakI / popN) * 100, peakDay, finalAttackRate,
      sCurve, iCurve, rCurve
    };
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

    if(simType === 'epi-measures-explorer'){
      title = 'Epidemiologic Association & Impact Calculator (RR, OR, AR, PAF & Delta CIs)';
      note = 'Adjust 2x2 cohort counts to compute Risk Ratio, Odds Ratio, Risk Difference, Population Attributable Fraction, and Delta method 95% confidence intervals.';
      controls = f('a', 'Exposed Cases (a)', 80, 1, 1000, 5)
        + f('b', 'Exposed Non-Cases (b)', 920, 10, 5000, 20)
        + f('c', 'Unexposed Cases (c)', 20, 1, 1000, 5)
        + f('d', 'Unexposed Non-Cases (d)', 980, 10, 5000, 20);
    }else if(simType === 'epi-confounding-strat'){
      title = 'Confounding & Mantel–Haenszel Stratified Odds Ratio Calculator';
      note = 'Stratify a study into two strata (e.g. Young vs Old) to observe Simpson’s paradox, evaluate confounding magnitude, and calculate the pooled Mantel-Haenszel OR.';
      controls = f('a1', 'Stratum 1 Exposed Cases (a₁)', 40, 1, 500, 5)
        + f('b1', 'Stratum 1 Exposed Controls (b₁)', 60, 1, 1000, 5)
        + f('c1', 'Stratum 1 Unexposed Cases (c₁)', 20, 1, 500, 5)
        + f('d1', 'Stratum 1 Unexposed Controls (d₁)', 80, 1, 1000, 5)
        + f('a2', 'Stratum 2 Exposed Cases (a₂)', 60, 1, 500, 5)
        + f('b2', 'Stratum 2 Exposed Controls (b₂)', 40, 1, 1000, 5)
        + f('c2', 'Stratum 2 Unexposed Cases (c₂)', 80, 1, 500, 5)
        + f('d2', 'Stratum 2 Unexposed Controls (d₂)', 120, 1, 1000, 5);
    }else if(simType === 'epi-roc-diagnostic'){
      title = 'Diagnostic Screening ROC Curve, Sensitivity, Specificity & Likelihood Ratio Explorer';
      note = 'Vary biomarker separation Δμ, diagnostic decision cutoff c, and disease prevalence to evaluate Sensitivity, Specificity, PPV, NPV, LR+, LR-, and Area Under the Curve (AUC).';
      controls = f('deltaMu', 'Biomarker Separation (Δμ)', 1.80, 0.5, 3.5, 0.1)
        + f('cutoff', 'Decision Cutoff (c)', 0.90, -2.5, 3.5, 0.1)
        + f('prevalence', 'Disease Prevalence (π)', 0.08, 0.01, 0.50, 0.01);
    }else if(simType === 'epi-sir-transmission'){
      title = 'Kermack–McKendrick SIR Epidemic Dynamics, R₀ & Herd Immunity Simulator';
      note = 'Simulate continuous disease transmission over time: observe how the Basic Reproduction Number R₀ governs the peak infectious wave and herd immunity threshold.';
      controls = f('beta', 'Transmission Rate (β)', 0.35, 0.05, 1.0, 0.05)
        + f('gamma', 'Recovery Rate (γ)', 0.14, 0.02, 0.5, 0.02)
        + f('popN', 'Population Size (N)', 100000, 1000, 500000, 10000)
        + f('initI', 'Initial Infected (I₀)', 10, 1, 50, 1)
        + f('days', 'Time Span (Days)', 100, 30, 200, 10);
    }

    el.innerHTML = `<h4>${title}</h4><p class="prob-note">${note}</p><div class="prob-fields">${controls}</div><div class="prob-actions"><button type="button" data-reset>Reset Defaults</button></div><div class="prob-results" aria-live="polite"></div>`;

    const inputs = [...el.querySelectorAll('input, select')];
    const initial = inputs.map(input => input.value);
    const result = el.querySelector('.prob-results');

    function render(){
      try{
        const get = id => {
          const inp = el.querySelector('#' + idPrefix + '-' + id);
          return inp ? (inp.tagName === 'SELECT' ? inp.value : parseFloat(inp.value)) : 0;
        };
        let values = {}, plot = '';

        if(simType === 'epi-measures-explorer'){
          const m = epiMeasuresModel(get('a'), get('b'), get('c'), get('d'));
          values = {
            'Exposed Risk (R₁)': (m.r1 * 100).toFixed(2) + '%',
            'Unexposed Risk (R₀)': (m.r0 * 100).toFixed(2) + '%',
            'Risk Ratio (RR)': fmt(m.rr) + ` [${fmt(m.rrLow)}, ${fmt(m.rrHigh)}]`,
            'Odds Ratio (OR)': fmt(m.orVal) + ` [${fmt(m.orLow)}, ${fmt(m.orHigh)}]`,
            'Risk Difference (AR)': (m.rd * 100).toFixed(2) + '%',
            'Population Attributable Fraction (PAF)': fmt(m.paf) + '%',
            'Number Needed to Treat / Harm (NNT)': Number.isFinite(m.nnt) ? fmt(m.nnt) : 'N/A'
          };
          plot = chart([
            { values: m.rrCurve, width: 2.5, color: '#38bdf8' },
            { values: m.orCurve, width: 2, dashed: true, color: '#f59e0b' }
          ], 0.01, 0.40, 'Risk Ratio (Cyan Solid) vs Odds Ratio (Amber Dashed) as Baseline Risk R₀ Increases', null, 1.0);
        }else if(simType === 'epi-confounding-strat'){
          const m = epiStratModel(get('a1'), get('b1'), get('c1'), get('d1'), get('a2'), get('b2'), get('c2'), get('d2'));
          values = {
            'Crude Odds Ratio': fmt(m.orCrude),
            'Stratum 1 (e.g. Young) OR₁': fmt(m.or1),
            'Stratum 2 (e.g. Old) OR₂': fmt(m.or2),
            'Mantel-Haenszel Pooled OR_MH': fmt(m.orMH) + ` [${fmt(m.orMHLow)}, ${fmt(m.orMHHigh)}]`,
            'Confounding Bias Magnitude': fmt(m.confoundingPct) + '%' + (Math.abs(m.confoundingPct) > 10 ? ' (Confounding Present!)' : ' (Minimal Confounding)')
          };
          plot = chart([
            { values: [[0.5, m.orCrude], [1.5, m.orCrude], [2.5, m.or1], [3.5, m.or2], [4.5, m.orMH]], width: 2.5, color: '#38bdf8' },
            { values: [[0, 1], [5, 1]], width: 1, dashed: true, color: '#94a3b8' }
          ], 0, 5, 'Odds Ratios: Crude (x=1), Stratum 1 (x=2.5), Stratum 2 (x=3.5), Mantel-Haenszel (x=4.5)', null, 1.0);
        }else if(simType === 'epi-roc-diagnostic'){
          const m = epiRocModel(get('deltaMu'), get('cutoff'), get('prevalence'));
          values = {
            'Sensitivity (True Positive Rate)': (m.se * 100).toFixed(1) + '%',
            'Specificity (True Negative Rate)': (m.sp * 100).toFixed(1) + '%',
            'False Positive Rate (1 - Sp)': (m.fpr * 100).toFixed(1) + '%',
            'Positive Predictive Value (PPV)': (m.ppv * 100).toFixed(1) + '%',
            'Negative Predictive Value (NPV)': (m.npv * 100).toFixed(1) + '%',
            'Positive Likelihood Ratio (LR+)': fmt(m.lrPlus),
            'Negative Likelihood Ratio (LR-)': fmt(m.lrMinus),
            'Area Under Curve (AUC)': fmt(m.auc),
            'Youden’s J Statistic': fmt(m.youdenJ)
          };
          plot = chart([
            { values: m.rocCurve, width: 2.5, color: '#38bdf8' },
            { values: m.diagLine, width: 1.2, dashed: true, color: '#64748b' }
          ], 0, 1.0, 'ROC Curve (Cyan Solid) vs Chance Diagonal (Gray Dashed) • Operating Point at Cutoff', m.operatingPoint[0], m.operatingPoint[1]);
        }else if(simType === 'epi-sir-transmission'){
          const m = epiSirModel(get('beta'), get('gamma'), get('popN'), get('initI'), get('days'));
          values = {
            'Basic Reproduction Number R₀': fmt(m.r0) + (m.r0 > 1 ? ' (Epidemic Expansion!)' : ' (Disease Dies Out)'),
            'Herd Immunity Threshold (HIT)': fmt(m.hit) + '%',
            'Peak Infected Proportion': fmt(m.peakFraction) + '%',
            'Peak Infection Day': fmt(m.peakDay) + ' days',
            'Final Epidemic Attack Rate': fmt(m.finalAttackRate) + '%'
          };
          plot = chart([
            { values: m.sCurve, width: 2, color: '#38bdf8' },
            { values: m.iCurve, width: 2.5, color: '#ef4444' },
            { values: m.rCurve, width: 2, color: '#10b981' }
          ], 0, get('days'), 'SIR Epidemic Wave: Susceptible (Cyan), Infected (Red), Recovered (Green)', m.peakDay);
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
  root.EpidemiologicalStatisticsSimulationEngine = { initSimulation };
})(typeof window !== 'undefined' ? window : null);
