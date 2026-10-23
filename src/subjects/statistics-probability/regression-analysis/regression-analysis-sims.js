/* Regression Analysis interactive teaching models and SVG visualizers. */
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

  // --- SIMULATION 1: OLS CONFIDENCE BANDS VS PREDICTION INTERVALS ---
  function olsBandsModel(beta1, sigma, n, x0){
    range(beta1, -3.0, 5.0, 'Slope beta1');
    range(sigma, 0.5, 10.0, 'Error SD sigma');
    range(n, 8, 100, 'Sample Size n');
    range(x0, 0, 20, 'Prediction Point x0');

    const beta0 = 10.0;
    const xBar = 10.0;
    const Sxx = n * 25.0; // Var(X) approx 25
    const tCrit = 2.0 + 2.2 / Math.max(4, n - 2);

    const seMeanAtX0 = sigma * Math.sqrt((1 / n) + Math.pow(x0 - xBar, 2) / Sxx);
    const sePredAtX0 = sigma * Math.sqrt(1 + (1 / n) + Math.pow(x0 - xBar, 2) / Sxx);
    const yHat0 = beta0 + beta1 * x0;
    const rSquared = (beta1 * beta1 * Sxx) / (beta1 * beta1 * Sxx + (n - 2) * sigma * sigma);

    const fitLine = [], ciUpper = [], ciLower = [], piUpper = [], piLower = [];
    for(let x = 0; x <= 20; x += 0.5){
      const yh = beta0 + beta1 * x;
      const sem = sigma * Math.sqrt((1 / n) + Math.pow(x - xBar, 2) / Sxx);
      const sep = sigma * Math.sqrt(1 + (1 / n) + Math.pow(x - xBar, 2) / Sxx);
      fitLine.push([x, yh]);
      ciUpper.push([x, yh + tCrit * sem]);
      ciLower.push([x, yh - tCrit * sem]);
      piUpper.push([x, yh + tCrit * sep]);
      piLower.push([x, yh - tCrit * sep]);
    }

    return { yHat0, seMeanAtX0, sePredAtX0, tCrit, rSquared, fitLine, ciUpper, ciLower, piUpper, piLower };
  }

  // --- SIMULATION 2: LEVERAGE, STUDENTIZED RESIDUALS & COOK'S DISTANCE ---
  function leverageCooksModel(xOut, yOut){
    range(xOut, 1.0, 15.0, 'Contaminated Point X_n');
    range(yOut, -10.0, 35.0, 'Contaminated Point Y_n');

    // 9 clean baseline observations along y = 2 + 1.5*x
    const basePts = [
      [1, 3.6], [2, 4.9], [3, 6.7], [4, 7.8], [5, 9.5],
      [6, 11.2], [7, 12.4], [8, 14.1], [9, 15.4]
    ];
    const allPts = [...basePts, [xOut, yOut]];
    const n = allPts.length;
    const xBar = allPts.reduce((s, p) => s + p[0], 0) / n;
    const yBar = allPts.reduce((s, p) => s + p[1], 0) / n;
    const Sxx = allPts.reduce((s, p) => s + Math.pow(p[0] - xBar, 2), 0);
    const Sxy = allPts.reduce((s, p) => s + (p[0] - xBar) * (p[1] - yBar), 0);

    const b1All = Sxy / Sxx;
    const b0All = yBar - b1All * xBar;

    // Clean fit without point n
    const b1Clean = 1.50;
    const b0Clean = 2.00;

    // Leverage h_nn of the n-th point
    const h_nn = (1 / n) + Math.pow(xOut - xBar, 2) / Sxx;
    const yHatN = b0All + b1All * xOut;
    const eN = yOut - yHatN;
    const sse = allPts.reduce((s, p) => s + Math.pow(p[1] - (b0All + b1All * p[0]), 2), 0);
    const mse = sse / (n - 2) || 0.01;
    const rN = eN / (Math.sqrt(mse * (1 - h_nn)) || 0.01);
    const cooksD = (rN * rN / 2) * (h_nn / Math.max(0.01, 1 - h_nn));
    const dffits = rN * Math.sqrt(h_nn / Math.max(0.01, 1 - h_nn));

    const cleanLine = [[0, b0Clean], [15, b0Clean + 15 * b1Clean]];
    const pertLine = [[0, b0All], [15, b0All + 15 * b1All]];

    return { b0All, b1All, h_nn, eN, rN, cooksD, dffits, cleanLine, pertLine };
  }

  // --- SIMULATION 3: MULTICOLLINEARITY, VIF & RIDGE TRACE ---
  function ridgeTraceModel(rhoCollin, lambda, sigma){
    range(rhoCollin, 0.0, 0.995, 'Predictor Correlation rho');
    range(lambda, 0.0, 2.0, 'Ridge Penalty lambda');
    range(sigma, 0.2, 5.0, 'Error Noise SD sigma');

    // Standardized 2-predictor system: X^T X = [[1, rho], [rho, 1]], true beta = [2.0, 1.5]
    const vif = 1 / (1 - rhoCollin * rhoCollin);
    const condNum = Math.sqrt((1 + rhoCollin) / Math.max(1e-4, 1 - rhoCollin));

    function ridgeAt(lam){
      const d = (1 + lam) * (1 + lam) - rhoCollin * rhoCollin;
      // Under sample perturbation proportional to collinearity
      const c1 = 2.0 + 1.5 * rhoCollin + 0.35 * sigma;
      const c2 = 2.0 * rhoCollin + 1.5 - 0.35 * sigma;
      const b1 = ((1 + lam) * c1 - rhoCollin * c2) / d;
      const b2 = ((1 + lam) * c2 - rhoCollin * c1) / d;
      // Variance trace of beta_ridge: sigma^2 * Tr((X^TX + lam*I)^-2 X^TX)
      const varSum = (sigma * sigma * 2 * ((1 + lam)*(1 + lam)*(1 + rhoCollin*rhoCollin) - 4*(1 + lam)*rhoCollin*rhoCollin + rhoCollin*rhoCollin*(1 + rhoCollin*rhoCollin))) / Math.pow(d, 2);
      const biasSq = Math.pow(b1 - 2.0, 2) + Math.pow(b2 - 1.5, 2);
      return { b1, b2, varSum: Math.max(0, (2 * sigma * sigma * (1 + rhoCollin*rhoCollin)) / (d * d)), biasSq };
    }

    const cur = ridgeAt(lambda);
    const trace1 = [], trace2 = [], mseCurve = [];
    for(let l = 0; l <= 2.0; l += 0.05){
      const r = ridgeAt(l);
      trace1.push([l, r.b1]);
      trace2.push([l, r.b2]);
      mseCurve.push([l, r.varSum + r.biasSq]);
    }

    return { vif, condNum, cur, trace1, trace2, mseCurve };
  }

  // --- SIMULATION 4: LOGISTIC REGRESSION GLM SIGMOID & ODDS RATIO ---
  function logisticGlmModel(beta0, beta1, xEval){
    range(beta0, -6.0, 6.0, 'Intercept beta0');
    range(beta1, -3.0, 3.0, 'Slope beta1');
    range(xEval, -5.0, 5.0, 'Covariate Value x');

    const eta = beta0 + beta1 * xEval;
    const piX = 1 / (1 + Math.exp(-eta));
    const oddsRatio = Math.exp(beta1);
    const ld50 = Math.abs(beta1) > 1e-3 ? (-beta0 / beta1) : 0;
    const marginalEffect = beta1 * piX * (1 - piX);

    const sigCurve = [], varWeightCurve = [];
    for(let x = -5.0; x <= 5.0; x += 0.2){
      const p = 1 / (1 + Math.exp(-(beta0 + beta1 * x)));
      sigCurve.push([x, p]);
      varWeightCurve.push([x, p * (1 - p) * 4]); // scaled IRLS weight 4*p*(1-p)
    }

    return { eta, piX, oddsRatio, ld50, marginalEffect, sigCurve, varWeightCurve };
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

    if(simType === 'reg-ols-confidence-bands'){
      title = 'OLS Regression Line, Mean Confidence Band & Prediction Interval Explorer';
      note = 'Visualizes the hyperbolic flaring of the 95% confidence band for E[Y|x₀] (green dashed) and the wider prediction interval for Y_new (yellow dotted) away from x̄ = 10.';
      controls = f('beta1', 'True Slope β₁', 1.80, -2.0, 4.0, 0.2)
        + f('sigma', 'Error Standard Deviation σ', 3.50, 0.5, 8.0, 0.5)
        + f('n', 'Sample Size n', 20, 8, 80, 4)
        + f('x0', 'Evaluation Point x₀', 16.0, 0.0, 20.0, 1.0);
    }else if(simType === 'reg-leverage-cooks-d'){
      title = 'High-Leverage Point, Studentized Residual & Cook’s Distance Influence Explorer';
      note = 'Perturb the 10th observation (X_n, Y_n) to see how high leverage h_nn combined with a large residual pulls the OLS line (red) away from the clean fit (cyan).';
      controls = f('xOut', 'Outlier Predictor X_n', 13.0, 1.0, 15.0, 0.5)
        + f('yOut', 'Outlier Response Y_n', 6.0, -5.0, 30.0, 1.0);
    }else if(simType === 'reg-ridge-lasso-trace'){
      title = 'Multicollinearity VIF & Hoerl–Kennard Ridge Regression Trace Explorer';
      note = 'Displays the Ridge coefficient paths β̂₁(λ) (cyan) and β̂₂(λ) (green) alongside Total Mean Squared Error (yellow dashed) as penalty λ stabilizes collinear inflation.';
      controls = f('rhoCollin', 'Predictor Correlation ρ₁₂', 0.94, 0.00, 0.99, 0.02)
        + f('lambda', 'Ridge Penalty Parameter λ', 0.20, 0.00, 2.00, 0.05)
        + f('sigma', 'Noise Standard Deviation σ', 1.20, 0.20, 3.00, 0.20);
    }else if(simType === 'reg-logistic-glm-curve'){
      title = 'Binary Logistic Regression Sigmoid Curve, Odds Ratio & IRLS Weight Explorer';
      note = 'Plots the logistic probability curve π(x) = 1/(1 + e^(-(β₀+β₁x))) (cyan) and scaled Fisher Scoring IRLS weight 4π(x)(1-π(x)) (green dashed).';
      controls = f('beta0', 'Log-Odds Intercept β₀', -1.20, -5.0, 5.0, 0.2)
        + f('beta1', 'Log-Odds Slope β₁', 1.10, -2.5, 2.5, 0.1)
        + f('xEval', 'Target Covariate x', 1.50, -5.0, 5.0, 0.25);
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
        if(simType === 'reg-ols-confidence-bands'){
          const m = olsBandsModel(get('beta1'), get('sigma'), get('n'), get('x0'));
          values = {
            'Fitted Value ŷ(x₀)': fmt(m.yHat0),
            'SE of Mean Response SE(μ̂₀)': fmt(m.seMeanAtX0),
            'SE of Prediction SE(Y_new - ŷ₀)': fmt(m.sePredAtX0),
            '95% Mean CI Half-Width': '±' + fmt(m.tCrit * m.seMeanAtX0),
            '95% Prediction Half-Width': '±' + fmt(m.tCrit * m.sePredAtX0),
            'Model R²': fmt(m.rSquared * 100) + '%'
          };
          plot = chart([
            { values: m.fitLine, width: 2.5, color: '#38bdf8' },
            { values: m.ciUpper, width: 1.8, dashed: true, color: '#10b981' },
            { values: m.ciLower, width: 1.8, dashed: true, color: '#10b981' },
            { values: m.piUpper, width: 1.6, dotted: true, color: '#fbbf24' },
            { values: m.piLower, width: 1.6, dotted: true, color: '#fbbf24' }
          ], 0, 20, 'OLS Line (Cyan), 95% Mean Confidence Band (Green), 95% Prediction Band (Yellow)', get('x0'));
        }
        if(simType === 'reg-leverage-cooks-d'){
          const m = leverageCooksModel(get('xOut'), get('yOut'));
          values = {
            'Perturbed OLS Slope β̂₁': fmt(m.b1All) + ' (Clean = 1.500)',
            'Point Leverage h_nn': fmt(m.h_nn) + (m.h_nn > 0.4 ? ' (High Leverage!)' : ' (Moderate)'),
            'Internally Studentized Residual r_n': fmt(m.rN),
            'Cook’s Distance D_n': fmt(m.cooksD) + (m.cooksD > 1.0 ? ' (Highly Influential!)' : ''),
            'DFFITS_n': fmt(m.dffits)
          };
          plot = chart([
            { values: m.cleanLine, width: 2, dashed: true, color: '#38bdf8' },
            { values: m.pertLine, width: 2.5, color: '#ef4444' }
          ], 0, 15, 'Clean OLS Fit (Cyan Dashed) vs Perturbed Fit with Outlier (Red Solid)', get('xOut'));
        }
        if(simType === 'reg-ridge-lasso-trace'){
          const m = ridgeTraceModel(get('rhoCollin'), get('lambda'), get('sigma'));
          values = {
            'Variance Inflation Factor VIF': fmt(m.vif) + (m.vif > 10 ? ' (Severe Collinearity!)' : ''),
            'Spectral Condition Number κ(X)': fmt(m.condNum),
            'Ridge Estimate β̂₁(λ)': fmt(m.cur.b1),
            'Ridge Estimate β̂₂(λ)': fmt(m.cur.b2),
            'Total Estimator Variance': fmt(m.cur.varSum),
            'Squared Shrinkage Bias': fmt(m.cur.biasSq)
          };
          plot = chart([
            { values: m.trace1, width: 2.5, color: '#38bdf8' },
            { values: m.trace2, width: 2.5, color: '#10b981' },
            { values: m.mseCurve, width: 2, dashed: true, color: '#fbbf24' }
          ], 0, 2.0, 'Ridge Trace: β̂₁(λ) (Cyan), β̂₂(λ) (Green) & Total MSE (Yellow Dashed)', get('lambda'));
        }
        if(simType === 'reg-logistic-glm-curve'){
          const m = logisticGlmModel(get('beta0'), get('beta1'), get('xEval'));
          values = {
            'Linear Predictor η = β₀ + β₁x': fmt(m.eta),
            'Predicted Probability π(x)': fmt(m.piX * 100) + '%',
            'Odds Ratio exp(β₁)': fmt(m.oddsRatio),
            'Median Effective Dose LD50 (-β₀/β₁)': fmt(m.ld50),
            'Marginal Effect dπ/dx': fmt(m.marginalEffect)
          };
          plot = chart([
            { values: m.sigCurve, width: 2.5, color: '#38bdf8' },
            { values: m.varWeightCurve, width: 2, dashed: true, color: '#10b981' }
          ], -5, 5, 'Logistic Response Curve π(x) (Cyan) & Scaled IRLS Weight 4π(1-π) (Green Dashed)', get('xEval'), 0.5);
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
  root.RegressionAnalysisSimulationEngine = { initSimulation };
})(typeof window !== 'undefined' ? window : null);
