/* Hypothesis Testing and Nonparametric Methods interactive teaching models and SVG visualizers. */
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

  function normCdf(x){
    const t = 1 / (1 + 0.2316419 * Math.abs(x));
    const d = 0.3989423 * Math.exp(-x * x / 2);
    const p = d * t * (0.3193815 + t * (-0.3565638 + t * (1.781478 + t * (-1.821256 + t * 1.330274))));
    return x > 0 ? 1 - p : p;
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

  // --- SIMULATION 1: NEYMAN-PEARSON UMP POWER CURVE ---
  function npPowerModel(mu1, n, alpha){
    range(mu1, 0.1, 2.5, 'Alternative Mean mu1');
    range(n, 4, 100, 'Sample Size n');
    range(alpha, 0.005, 0.20, 'Significance Level alpha');

    // Approximate inverse normal for common alpha or rational approx
    function qnorm(p){
      // Acklam-style simple rational approximation for 0.5 < p < 0.999
      const a = p > 0.5 ? 1 - p : p;
      const t = Math.sqrt(-2 * Math.log(a));
      const z = t - (2.515517 + 0.802853*t + 0.010328*t*t) / (1 + 1.432788*t + 0.189269*t*t + 0.001308*t*t*t);
      return p > 0.5 ? z : -z;
    }

    const zAlpha = qnorm(1 - alpha);
    const se = 1 / Math.sqrt(n);
    const critC = zAlpha * se;
    const powerAtMu1 = 1 - normCdf(zAlpha - mu1 * Math.sqrt(n));
    const typeII = 1 - powerAtMu1;

    const powerCurve = [];
    for(let m = -0.5; m <= 2.5; m += 0.06){
      const pwr = 1 - normCdf(zAlpha - m * Math.sqrt(n));
      powerCurve.push([m, pwr]);
    }

    return { zAlpha, critC, powerAtMu1, typeII, powerCurve };
  }

  // --- SIMULATION 2: WALD SPRT BOUNDARIES, OC & ASN ---
  function sprtModel(alpha, beta, theta1){
    range(alpha, 0.01, 0.20, 'Type I Error alpha');
    range(beta, 0.01, 0.20, 'Type II Error beta');
    range(theta1, 0.2, 2.0, 'Alternative Mean theta1');

    const A = (1 - beta) / alpha;
    const B = beta / (1 - alpha);
    const lnA = Math.log(A);
    const lnB = Math.log(B);

    // For N(theta, 1) testing H0: theta=0 vs H1: theta=theta1
    // Z_i = theta1 * X_i - 0.5 * theta1^2
    // Non-zero h(theta) = (theta1 - 2*theta) / theta1
    const asnCurve = [], ocCurve = [];
    for(let i = 0; i <= 50; i++){
      const th = -0.2 + (i / 50) * (theta1 + 0.4);
      const h = (theta1 - 2 * th);
      let L_th, asn;
      const ez = theta1 * th - 0.5 * theta1 * theta1;
      if(Math.abs(h) < 1e-4){
        L_th = lnA / (lnA - lnB);
        asn = (-lnA * lnB) / (theta1 * theta1);
      }else{
        L_th = (Math.exp(h * lnA) - 1) / (Math.exp(h * lnA) - Math.exp(h * lnB));
        const expLog = L_th * lnB + (1 - L_th) * lnA;
        asn = expLog / ez;
      }
      ocCurve.push([th, L_th]);
      asnCurve.push([th, Math.max(1, asn)]);
    }

    const asnH0 = ((1 - alpha) * lnB + alpha * lnA) / (-0.5 * theta1 * theta1);
    const asnH1 = (beta * lnB + (1 - beta) * lnA) / (0.5 * theta1 * theta1);
    // Fixed sample size required for same (alpha, beta)
    const zA = Math.sqrt(-2 * Math.log(alpha)) * 0.82;
    const zB = Math.sqrt(-2 * Math.log(beta)) * 0.82;
    const nFixed = Math.pow((1.645 + 1.282) / theta1, 2);

    return { A, B, lnA, lnB, asnH0, asnH1, nFixed, asnCurve, ocCurve };
  }

  // --- SIMULATION 3: KOLMOGOROV-SMIRNOV EDF SUPREMUM DISTANCE ---
  function ksModel(n, shiftDelta, scaleRatio){
    range(n, 8, 60, 'Sample Size n');
    range(shiftDelta, -1.5, 1.5, 'Location Shift Delta');
    range(scaleRatio, 0.5, 2.5, 'Scale Factor sigma');

    // Deterministic quasi-random quantiles to make smooth interactive EDF
    const sample = [];
    for(let i = 1; i <= n; i++){
      const u = (i - 0.5) / n;
      // Box-Muller deterministic perturbation
      const z = (u > 0.5 ? 1 : -1) * Math.sqrt(-2 * Math.log(Math.min(u, 1 - u))) * 0.72 + 0.12 * Math.sin(i * 2.3);
      sample.push(shiftDelta + scaleRatio * z);
    }
    sample.sort((a, b) => a - b);

    let dPlus = 0, dMinus = 0, xStar = 0;
    for(let i = 0; i < n; i++){
      const fn = (i + 1) / n;
      const fnPrev = i / n;
      const f0 = normCdf(sample[i]);
      if(fn - f0 > dPlus){ dPlus = fn - f0; xStar = sample[i]; }
      if(f0 - fnPrev > dMinus){ dMinus = f0 - fnPrev; if(dMinus > dPlus) xStar = sample[i]; }
    }
    const Dn = Math.max(dPlus, dMinus);
    const crit05 = 1.358 / Math.sqrt(n);

    const nullCurve = [], edfCurve = [];
    for(let x = -3.5; x <= 3.5; x += 0.1){
      nullCurve.push([x, normCdf(x)]);
      const count = sample.filter(v => v <= x).length;
      edfCurve.push([x, count / n]);
    }

    return { Dn, dPlus, dMinus, xStar, crit05, reject: Dn > crit05, nullCurve, edfCurve };
  }

  // --- SIMULATION 4: WILCOXON VS STUDENT T PITMAN ARE & HEAVY-TAIL POWER ---
  function wilcoxonAreModel(shiftDelta, n, contamEps){
    range(shiftDelta, 0.1, 1.5, 'Location Shift Delta');
    range(n, 10, 80, 'Per-Group Sample Size n');
    range(contamEps, 0.0, 0.30, 'Outlier Contamination epsilon');

    // Contaminated normal variance: (1 - eps)*1 + eps*25 = 1 + 24*eps
    const varContam = 1 + 24 * contamEps;
    const areNormal = 3 / Math.PI; // 0.9549
    // Effective ARE under contamination rises dramatically because density at median f(0) stays near 1/sqrt(2*pi) while variance inflates by varContam
    const f0 = (1 - contamEps) * (1 / Math.sqrt(2 * Math.PI)) + contamEps * (1 / (5 * Math.sqrt(2 * Math.PI)));
    const areContam = 12 * varContam * Math.pow(f0, 2);

    const tCurve = [], wCurve = [];
    for(let d = 0; d <= 1.5; d += 0.05){
      const ncpT = d * Math.sqrt(n / (2 * varContam));
      const ncpW = d * Math.sqrt((n / 2) * 12) * f0;
      tCurve.push([d, 1 - normCdf(1.645 - ncpT)]);
      wCurve.push([d, 1 - normCdf(1.645 - ncpW)]);
    }

    const curNcpT = shiftDelta * Math.sqrt(n / (2 * varContam));
    const curNcpW = shiftDelta * Math.sqrt((n / 2) * 12) * f0;
    const powerT = 1 - normCdf(1.645 - curNcpT);
    const powerW = 1 - normCdf(1.645 - curNcpW);

    return { varContam, areNormal, areContam, powerT, powerW, tCurve, wCurve };
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

    if(simType === 'ht-neyman-pearson-power'){
      title = 'Neyman–Pearson Critical Region & UMP Power Function Explorer';
      note = 'Plots the Uniformly Most Powerful (UMP) one-sided power curve β(μ) = P_μ(Reject H₀) for N(μ, 1) and computes exact Type I and Type II error probabilities.';
      controls = f('mu1', 'Alternative Mean μ₁', 0.80, 0.10, 2.20, 0.10)
        + f('n', 'Sample Size n', 25, 5, 100, 5)
        + f('alpha', 'Significance Level α', 0.05, 0.01, 0.20, 0.01);
    }else if(simType === 'ht-sprt-wald-boundary'){
      title = 'Wald Sequential Probability Ratio Test (SPRT) ASN & OC Explorer';
      note = 'Computes Wald’s stopping boundaries (ln B, ln A) and plots the Average Sample Number E_θ[N] (cyan) showing dramatic sample savings over fixed-sample tests.';
      controls = f('alpha', 'Target Type I Error α', 0.05, 0.01, 0.15, 0.01)
        + f('beta', 'Target Type II Error β', 0.05, 0.01, 0.15, 0.01)
        + f('theta1', 'Signal Strength θ₁', 0.60, 0.25, 1.50, 0.05);
    }else if(simType === 'ht-ks-edf-goodness'){
      title = 'Kolmogorov–Smirnov Empirical Distribution Function (EDF) Supremum Explorer';
      note = 'Compares the step-function EDF F_n(x) (yellow) against the theoretical standard normal CDF F₀(x) (cyan) to locate the supremum distance D_n.';
      controls = f('n', 'Sample Size n', 25, 10, 60, 5)
        + f('shiftDelta', 'Location Shift Δ', 0.35, -1.20, 1.20, 0.05)
        + f('scaleRatio', 'Scale Ratio σ', 1.00, 0.50, 2.00, 0.10);
    }else if(simType === 'ht-wilcoxon-are-explorer'){
      title = 'Wilcoxon Rank-Sum vs Student’s t-Test Pitman Efficiency & Robustness Explorer';
      note = 'Demonstrates how the Wilcoxon test retains 95.5% efficiency under pure normality (ε = 0) and vastly outperforms Student’s t-test under heavy-tailed outlier contamination.';
      controls = f('shiftDelta', 'Location Shift Δ', 0.60, 0.10, 1.50, 0.10)
        + f('n', 'Sample Size per Group n', 30, 10, 80, 5)
        + f('contamEps', 'Heavy-Tail Contamination ε', 0.10, 0.00, 0.25, 0.02);
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
        if(simType === 'ht-neyman-pearson-power'){
          const m = npPowerModel(get('mu1'), get('n'), get('alpha'));
          values = {
            'Critical Value z_(1-α)': fmt(m.zAlpha),
            'Sample Mean Cutoff c*': fmt(m.critC),
            'Type I Error α = β(0)': fmt(get('alpha')),
            'Power at μ₁ β(μ₁)': fmt(m.powerAtMu1 * 100) + '%',
            'Type II Error 1 - β(μ₁)': fmt(m.typeII * 100) + '%',
            'Unbiasedness β(μ₁) > α': m.powerAtMu1 > get('alpha') ? 'Verified (Strict)' : 'Boundary'
          };
          plot = chart([
            { values: m.powerCurve, width: 2.5, color: '#10b981' }
          ], -0.5, 2.5, 'UMP Power Function β(μ) across Parameter Space (Red Line = Alternative μ₁)', get('mu1'), get('alpha'));
        }
        if(simType === 'ht-sprt-wald-boundary'){
          const m = sprtModel(get('alpha'), get('beta'), get('theta1'));
          values = {
            'Upper Stopping Boundary ln A': fmt(m.lnA),
            'Lower Stopping Boundary ln B': fmt(m.lnB),
            'Expected Sample Size E₀[N]': fmt(m.asnH0) + ' obs',
            'Expected Sample Size E₁[N]': fmt(m.asnH1) + ' obs',
            'Equivalent Fixed-Sample Size n_fix': fmt(m.nFixed) + ' obs',
            'SPRT Sample Reduction': fmt((1 - m.asnH1 / m.nFixed) * 100) + '% saved'
          };
          plot = chart([
            { values: m.asnCurve, width: 2.5, color: '#38bdf8' }
          ], -0.2, get('theta1') + 0.2, 'Average Sample Number ASN E_θ[N] Curve (Peaks at Intermediate θ ≈ θ₁/2)', get('theta1') / 2);
        }
        if(simType === 'ht-ks-edf-goodness'){
          const m = ksModel(get('n'), get('shiftDelta'), get('scaleRatio'));
          values = {
            'Positive Supremum D_n⁺': fmt(m.dPlus),
            'Negative Supremum D_n⁻': fmt(m.dMinus),
            'Two-Sided K-S Statistic D_n': fmt(m.Dn),
            'Supremum Location x*': fmt(m.xStar),
            '5% Critical Value c_0.05': fmt(m.crit05),
            'Decision at α = 0.05': m.reject ? 'Reject H₀ (Non-Normal)' : 'Fail to Reject H₀'
          };
          plot = chart([
            { values: m.nullCurve, width: 2, dashed: true, color: '#38bdf8' },
            { values: m.edfCurve, width: 2.5, color: '#fbbf24' }
          ], -3.5, 3.5, 'Theoretical CDF F₀(x) (Cyan Dashed) vs Empirical EDF F_n(x) (Yellow Solid)', m.xStar);
        }
        if(simType === 'ht-wilcoxon-are-explorer'){
          const m = wilcoxonAreModel(get('shiftDelta'), get('n'), get('contamEps'));
          values = {
            'Pitman ARE under Pure Normality': fmt(m.areNormal * 100) + '% (3/π)',
            'Effective ARE at Current ε': fmt(m.areContam * 100) + '%',
            'Contaminated Variance σ²_ε': fmt(m.varContam),
            'Student’s t-Test Power': fmt(m.powerT * 100) + '%',
            'Wilcoxon Rank-Sum Power': fmt(m.powerW * 100) + '%',
            'Robustness Advantage': m.powerW >= m.powerT ? 'Wilcoxon Superior' : 'Student t Slightly Higher'
          };
          plot = chart([
            { values: m.tCurve, width: 2, dashed: true, color: '#ef4444' },
            { values: m.wCurve, width: 2.5, color: '#10b981' }
          ], 0, 1.5, 'Power Comparison: Wilcoxon Rank-Sum (Green Solid) vs Student t-Test (Red Dashed)', get('shiftDelta'));
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
  root.HypothesisTestingSimulationEngine = { initSimulation };
})(typeof window !== 'undefined' ? window : null);
