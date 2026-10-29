/* Actuarial Statistics and Mathematical Demography interactive teaching models and SVG visualizers. */
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

  // --- SIMULATION 1: ANNUITIES-CERTAIN & COMPOUND INTEREST MECHANICS ---
  function actAnnuityCertainModel(interestPct, termN, paymentP){
    range(interestPct, 0.5, 20.0, 'Interest rate i (%)');
    range(termN, 1, 50, 'Term n (years)');
    range(paymentP, 100, 100000, 'Annual Payment P');

    const i = interestPct / 100;
    const v = 1 / (1 + i);
    const d = i / (1 + i);
    const delta = Math.log(1 + i);

    // Level annuity immediate a_n| and due a_dot_n|
    const a_n = (1 - Math.pow(v, termN)) / i;
    const a_dot_n = (1 - Math.pow(v, termN)) / d;
    const a_bar_n = (1 - Math.pow(v, termN)) / delta;

    const pvImmediate = paymentP * a_n;
    const pvDue = paymentP * a_dot_n;
    const fvImmediate = pvImmediate * Math.pow(1 + i, termN);

    // Arithmetically increasing annuity (Ia)_n| = (a_dot_n| - n * v^n) / i
    const ia_n = (a_dot_n - termN * Math.pow(v, termN)) / i;
    const pvIncreasing = paymentP * ia_n;

    // Cash flow discount curve
    const dcfCurve = [];
    for(let t = 1; t <= termN; t++){
      dcfCurve.push([t, paymentP * Math.pow(v, t)]);
    }

    return {
      v, d, delta, a_n, a_dot_n, a_bar_n, pvImmediate, pvDue, fvImmediate, pvIncreasing,
      dcfCurve
    };
  }

  // --- SIMULATION 2: GOMPERTZ-MAKEHAM LIFE TABLE & SURVIVAL MODEL ---
  function actLifeTableModel(paramA, paramB, paramC){
    range(paramA, 0.0001, 0.01, 'Makeham A');
    range(paramB, 0.00001, 0.001, 'Gompertz B');
    range(paramC, 1.05, 1.15, 'Gompertz c');

    // Makeham survival function: S(x) = exp(-A*x - (B/ln(c)) * (c^x - 1))
    const lnC = Math.log(paramC);
    function survival(x){
      const val = -paramA * x - (paramB / lnC) * (Math.pow(paramC, x) - 1);
      return Math.exp(val);
    }

    const radix = 100000;
    const lxCurve = [];
    const muCurve = [];

    let sumLx = 0;
    for(let age = 0; age <= 100; age++){
      const s = survival(age);
      const lx = radix * s;
      lxCurve.push([age, lx]);
      const mu = paramA + paramB * Math.pow(paramC, age);
      muCurve.push([age, mu * 1000]); // scaled per 1000 lives
      if(age >= 0 && age < 100) sumLx += lx;
    }

    const e0 = sumLx / radix; // expectation of life at birth e_0
    const s65 = survival(65);
    const l65 = radix * s65;
    const q65 = 1 - survival(66) / s65;

    return {
      e0, l65, q65: (q65 * 1000).toFixed(2) + ' per 1,000',
      lxCurve, muCurve
    };
  }

  // --- SIMULATION 3: BENEFIT PREMIUMS & FUTURE LOSS-AT-ISSUE ---
  function actPremiumModel(issueAge, interestPct, sumAssured, paramB, paramC){
    range(issueAge, 20, 75, 'Issue Age x');
    range(interestPct, 1.0, 10.0, 'Interest rate i (%)');
    range(sumAssured, 1000, 1000000, 'Sum Assured S');
    range(paramB, 0.00002, 0.0005, 'Mortality B');
    range(paramC, 1.06, 1.12, 'Mortality c');

    const i = interestPct / 100;
    const v = 1 / (1 + i);
    const d = i / (1 + i);
    const lnC = Math.log(paramC);

    function survival(x){
      return Math.exp(-(paramB / lnC) * (Math.pow(paramC, x) - 1));
    }

    // Evaluate whole life annuity-due a_dot_x = sum_{k=0}^infinity v^k k_p_x
    let a_dot_x = 0;
    let a_dot_x_20 = 0; // 20-year temporary annuity
    const sx = survival(issueAge);

    for(let k = 0; k <= 100 - issueAge; k++){
      const kp = survival(issueAge + k) / sx;
      const disc = Math.pow(v, k) * kp;
      a_dot_x += disc;
      if(k < 20) a_dot_x_20 += disc;
    }

    // Actuarial Present Value of whole life insurance: A_x = 1 - d * a_dot_x
    const Ax = 1 - d * a_dot_x;
    // Whole life net level annual premium P_x = A_x / a_dot_x
    const Px = (Ax / a_dot_x) * sumAssured;

    // 20-Year Term Insurance A_x:20|^1 and premium
    const v20 = Math.pow(v, 20);
    const p20 = survival(issueAge + 20) / sx;
    const nEx = v20 * p20;
    const Ax_endow20 = 1 - d * a_dot_x_20;
    const Ax_term20 = Ax_endow20 - nEx;
    const P_term20 = (Ax_term20 / a_dot_x_20) * sumAssured;
    const P_endow20 = (Ax_endow20 / a_dot_x_20) * sumAssured;

    // Premium comparison curve across issue ages 20 to 70
    const premWholeCurve = [], premTermCurve = [];
    for(let a = 20; a <= 70; a += 2){
      let ad = 0, ad20 = 0;
      const sa = survival(a);
      for(let k = 0; k <= 100 - a; k++){
        const kp = survival(a + k) / sa;
        const disc = Math.pow(v, k) * kp;
        ad += disc;
        if(k < 20) ad20 += disc;
      }
      const aVal = 1 - d * ad;
      premWholeCurve.push([a, (aVal / ad) * sumAssured]);
      const p20a = survival(a + 20) / sa;
      const aValEndow = 1 - d * ad20;
      const aValTerm = aValEndow - v20 * p20a;
      premTermCurve.push([a, (aValTerm / ad20) * sumAssured]);
    }

    return {
      Ax, a_dot_x, Px, P_term20, P_endow20,
      premWholeCurve, premTermCurve
    };
  }

  // --- SIMULATION 4: BENEFIT RESERVES & THIELE'S TRAJECTORY ---
  function actReservesModel(issueAge, termYears, interestPct, sumAssured){
    range(issueAge, 20, 60, 'Issue Age');
    range(termYears, 10, 40, 'Policy Term (years)');
    range(interestPct, 1.0, 10.0, 'Interest rate i (%)');
    range(sumAssured, 1000, 500000, 'Sum Assured');

    const i = interestPct / 100;
    const v = 1 / (1 + i);
    const d = i / (1 + i);

    // Makeham mortality parameters
    const paramA = 0.001, paramB = 0.00005, paramC = 1.09;
    const lnC = Math.log(paramC);
    function survival(x){
      return Math.exp(-paramA * x - (paramB / lnC) * (Math.pow(paramC, x) - 1));
    }

    // Temporary life annuity for Endowment policy of term n
    function tempAnnuity(x, n){
      let sum = 0;
      const sx = survival(x);
      for(let k = 0; k < n; k++){
        sum += Math.pow(v, k) * (survival(x + k) / sx);
      }
      return sum;
    }

    const n = termYears;
    const a_dot_xn = tempAnnuity(issueAge, n);
    const Axn = 1 - d * a_dot_xn;
    const P_endow = Axn / a_dot_xn; // net level premium per unit sum assured

    // Prospective terminal reserves: _t V = A_{x+t : n-t|} - P * a_dot_{x+t : n-t|}
    const reserveEndowCurve = [];
    const reserveWholeCurve = [];

    // Whole life comparison
    function wholeAnnuity(x){
      let sum = 0;
      const sx = survival(x);
      for(let k = 0; k <= 100 - x; k++){
        sum += Math.pow(v, k) * (survival(x + k) / sx);
      }
      return sum;
    }
    const a_dot_whole = wholeAnnuity(issueAge);
    const P_whole = (1 - d * a_dot_whole) / a_dot_whole;

    for(let t = 0; t <= n; t++){
      const ageNow = issueAge + t;
      const remainingTerm = n - t;
      const a_dot_now = tempAnnuity(ageNow, remainingTerm);
      const Ax_now = remainingTerm > 0 ? (1 - d * a_dot_now) : 1.0;
      const vt = (Ax_now - P_endow * a_dot_now) * sumAssured;
      reserveEndowCurve.push([t, vt]);

      const a_dot_w_now = wholeAnnuity(ageNow);
      const Ax_w_now = 1 - d * a_dot_w_now;
      const vt_whole = (Ax_w_now - P_whole * a_dot_w_now) * sumAssured;
      reserveWholeCurve.push([t, vt_whole]);
    }

    const midReserve = reserveEndowCurve[Math.floor(n / 2)][1];

    return {
      annualPremium: P_endow * sumAssured,
      wholePremium: P_whole * sumAssured,
      maturityReserve: sumAssured,
      midReserve,
      reserveEndowCurve, reserveWholeCurve
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

    if(simType === 'act-annuity-certain'){
      title = 'Compound Interest, Discount Factors & Annuities-Certain Valuation';
      note = 'Calculate present value and accumulated value of level annuities-immediate a_n|, annuities-due ä_n|, and arithmetically increasing cash flows (Ia)_n| under compound interest.';
      controls = f('interestPct', 'Annual Interest Rate i (%)', 5.0, 1.0, 15.0, 0.5)
        + f('termN', 'Term in Years (n)', 20, 5, 40, 1)
        + f('paymentP', 'Annual Payment (P)', 1000.0, 100.0, 10000.0, 100.0);
    }else if(simType === 'act-life-table-survival'){
      title = 'Gompertz–Makeham Mortality Law & Life Table Cohort Survival Simulator';
      note = 'Explore how aging accelerates the instantaneous force of mortality μ(x) = A + B·cˣ and shapes cohort survivorship l_x and remaining life expectancy.';
      controls = f('paramA', 'Makeham Accidental Risk (A)', 0.0010, 0.0002, 0.0050, 0.0002)
        + f('paramB', 'Gompertz Senescence Scale (B)', 0.00004, 0.00001, 0.00020, 0.00001)
        + f('paramC', 'Gompertz Aging Rate (c)', 1.095, 1.050, 1.140, 0.005);
    }else if(simType === 'act-insurance-premium'){
      title = 'Life Insurance Net Level Premium & Loss-at-Issue Equivalence Explorer';
      note = 'Compute net annual level premiums under the Equivalence Principle (E[₀L] = 0) comparing Whole Life (P_x), 20-Year Term, and 20-Year Endowment contracts.';
      controls = f('issueAge', 'Issue Age (x)', 35, 20, 65, 1)
        + f('interestPct', 'Valuation Interest Rate i (%)', 4.5, 1.5, 9.0, 0.5)
        + f('sumAssured', 'Sum Assured (Death Benefit)', 100000, 10000, 500000, 10000)
        + f('paramB', 'Mortality Baseline (B)', 0.00004, 0.00001, 0.00015, 0.00001)
        + f('paramC', 'Mortality Base (c)', 1.095, 1.060, 1.130, 0.005);
    }else if(simType === 'act-benefit-reserves'){
      title = 'Prospective & Retrospective Policy Benefit Reserves Simulator';
      note = 'Track the growth of terminal policy reserves ₜV across contract duration t, illustrating the capital accumulation required to cover escalating older-age mortality costs.';
      controls = f('issueAge', 'Issue Age (x)', 30, 20, 55, 1)
        + f('termYears', 'Contract Term (Years)', 25, 10, 35, 1)
        + f('interestPct', 'Valuation Interest Rate i (%)', 5.0, 2.0, 8.0, 0.5)
        + f('sumAssured', 'Policy Face Amount', 50000, 10000, 200000, 5000);
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

        if(simType === 'act-annuity-certain'){
          const m = actAnnuityCertainModel(get('interestPct'), get('termN'), get('paymentP'));
          values = {
            'Discount Factor (v)': fmt(m.v),
            'Annual Discount Rate (d)': (m.d * 100).toFixed(2) + '%',
            'Force of Interest (δ)': (m.delta * 100).toFixed(2) + '%',
            'Present Value Immediate a_n|': fmt(m.pvImmediate),
            'Present Value Due ä_n|': fmt(m.pvDue),
            'Future Value at Term s_n|': fmt(m.fvImmediate),
            'Increasing Annuity (Ia)_n| PV': fmt(m.pvIncreasing)
          };
          plot = chart([
            { values: m.dcfCurve, width: 2.2, color: '#38bdf8' }
          ], 1, get('termN'), 'Discounted Value of Cash Flow vᵗ · P across Time (Years)', null, null);
        }else if(simType === 'act-life-table-survival'){
          const m = actLifeTableModel(get('paramA'), get('paramB'), get('paramC'));
          values = {
            'Life Expectancy at Birth (e₀)': fmt(m.e0) + ' years',
            'Surviving to Age 65 (l₆₅)': `${Math.round(m.l65)} / 100,000`,
            'Mortality Rate at Age 65 (q₆₅)': m.q65
          };
          plot = chart([
            { values: m.lxCurve, width: 2.5, color: '#38bdf8' },
            { values: m.muCurve.map(([x, m]) => [x, m * 50]), width: 2, dashed: true, color: '#ef4444' }
          ], 0, 100, 'Life Table Cohort l_x (Cyan Solid) vs Scaled Force of Mortality μ(x) (Red Dashed)', 65);
        }else if(simType === 'act-insurance-premium'){
          const m = actPremiumModel(get('issueAge'), get('interestPct'), get('sumAssured'), get('paramB'), get('paramC'));
          values = {
            'Whole Life APV (A_x)': fmt(m.Ax),
            'Whole Life Annuity (ä_x)': fmt(m.a_dot_x),
            'Whole Life Level Premium (P_x)': fmt(m.Px),
            '20-Year Term Premium': fmt(m.P_term20),
            '20-Year Endowment Premium': fmt(m.P_endow20)
          };
          plot = chart([
            { values: m.premWholeCurve, width: 2.5, color: '#38bdf8' },
            { values: m.premTermCurve, width: 2.0, dashed: true, color: '#10b981' }
          ], 20, 70, 'Annual Level Premium vs Issue Age: Whole Life P_x (Cyan) vs 20-Yr Term (Green Dashed)', get('issueAge'));
        }else if(simType === 'act-benefit-reserves'){
          const m = actReservesModel(get('issueAge'), get('termYears'), get('interestPct'), get('sumAssured'));
          values = {
            'Endowment Annual Net Premium': fmt(m.annualPremium),
            'Whole Life Annual Net Premium': fmt(m.wholePremium),
            ['Mid-Term Reserve (t=' + Math.floor(get('termYears')/2) + ')']: fmt(m.midReserve),
            'Terminal Maturity Reserve': fmt(m.maturityReserve)
          };
          plot = chart([
            { values: m.reserveEndowCurve, width: 2.5, color: '#38bdf8' },
            { values: m.reserveWholeCurve, width: 2.0, dashed: true, color: '#f59e0b' }
          ], 0, get('termYears'), 'Policy Reserve ₜV: Endowment Insurance (Cyan Solid) vs Whole Life (Amber Dashed)', Math.floor(get('termYears')/2));
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
  root.ActuarialStatisticsSimulationEngine = { initSimulation };
})(typeof window !== 'undefined' ? window : null);
