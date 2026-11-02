/* Water Resources Engineering Interactive Simulation Suite */
(function(window) {
  'use strict';

  const max = Math.max, min = Math.min, exp = Math.exp, log = Math.log, sqrt = Math.sqrt, PI = Math.PI;

  function compute(id, v) {
    
 let [a,b,c]=v, res={},series=[], units='', note='';
 const push=(x,y)=>series.push({x,y});
 if(id===1){let ds=a-b-c;res={'Storage/balance residual':ds,'Runoff fraction (%)':100*c/a};units='mm/year';for(let k=0;k<=20;k++){let p=a*(.7+.03*k);push(p,p-b-c)};note='Residual is not available withdrawal without a time-resolved account.'}
 else if(id===2){let demand=a*Math.pow(1+b/100,c);res={'Projected demand (ML/day)':demand,'Increase (ML/day)':demand-a,'Growth factor':demand/a};units='ML/day';for(let k=0;k<=c;k++)push(k,a*Math.pow(1+b/100,k));note='Steady compound growth; no peak-day or leakage variability.'}
 else if(id===3){let essential=min(a,b),optional=min(max(0,a-essential),c);res={'Essential served (ML/day)':essential,'Optional served (ML/day)':optional,'Shortfall (ML/day)':b-essential+c-optional};units='ML/day';for(let k=0;k<=20;k++){let s=a*(.5+.05*k);push(s,min(s,b)+min(max(s-b,0),c))};note='Single-period priority rule does not model distance or legal rights.'}
 else if(id===4){let m=min(a,c),ag=min(max(0,a-m),b);res={'Municipal served (ML/day)':m,'Agricultural served (ML/day)':ag,'Total shortfall (ML/day)':b+c-m-ag};units='ML/day';for(let k=0;k<=20;k++){let s=a*(.5+.05*k);push(s,min(s,c)+min(max(s-c,0),b))};note='Municipal-first allocation assumes no ecological reserve or return flow.'}
 else if(id===5){let st=c, cap=850,sp=0,del=0,miss=0, ev=0;for(let t=0;t<30;t++){let I=a*(.7+.65*Math.exp(-Math.pow((t-12)/5,2)));let e=1;let water=max(0,st+I-e), r=min(b,water);miss+=b-r;del+=r;let overflow=max(0,water-r-cap);sp+=overflow;st=max(0,min(cap,water-r));push(t+1,st);ev+=Math.min(e,st+I)}res={'Ending storage (ML)':st,'Total spill (ML)':sp,'Target release deficit (ML)':miss,'Total delivered (ML)':del,'Modeled evaporation (ML)':ev};units='ML';note='Daily Euler volume balance with capped storage; synthetic inflow.'}
 else if(id===6){let st=c, peak=0,spill=0,totalin=0,totalout=0;for(let t=0;t<20;t++){let I=15 + a*Math.max(0,1-Math.abs(t-6)/6), out=min(b,st+I), s=max(0,st+I-out-800);st=min(800,max(0,st+I-out-s));peak=max(peak,out+s);spill+=s;totalin+=I;totalout+=out+s;push(t+1,out+s)}res={'Maximum downstream release (ML/day)':peak,'Total spill (ML)':spill,'Ending storage (ML)':st,'Closure error (ML)':c+totalin-totalout-st};units='ML/day';note='Flood pulse and outlet are synthetic; no rating curve or dam-safety model.'}
 else if(id===7){let etc=a*b, net=max(0,etc-c);res={'Crop ET (mm/day)':etc,'Net irrigation (mm/day)':net,'Net volume (m³/day/ha)':net*10};units='mm/day';for(let k=0;k<=20;k++){let kc=b*(.5+.05*k);push(kc,max(0,a*kc-c))}note='1 mm over 1 ha equals 10 m³.'}
 else if(id===8){let out=a*exp(-b*c);res={'Tailflow (m³/s)':out,'Loss (m³/s)':a-out,'Conveyance efficiency (%)':out/a*100};units='m³/s';for(let k=0;k<=30;k++)push(c*k/30,a*exp(-b*c*k/30));note='Distributed fractional loss; seepage may be a groundwater return.'}
 else if(id===9){let z=1.5,base=4,A=a*(base+z*a),P=base+2*a*sqrt(1+z*z),R=A/P,Q=A*Math.pow(R,2/3)*sqrt(b)/c;res={'Discharge (m³/s)':Q,'Area (m²)':A,'Hydraulic radius (m)':R};units='m³/s';for(let k=1;k<=24;k++){let depth=max(.02,a*(.15+.06*k));let area=depth*(base+z*depth),per=base+2*depth*sqrt(1+z*z);push(depth,area*Math.pow(area/per,2/3)*sqrt(b)/c)}note='Uniform-flow Manning estimate, b=4 m, side slope 1.5H:1V.'}
 else if(id===10){let tau=1000*9.81*a*b;res={'Mean boundary shear (Pa)':tau,'Critical shear (Pa)':c,'Threshold ratio':tau/c};units='Pa';for(let k=0;k<=20;k++){let s=b*(.5+.05*k);push(s,9810*a*s)}note='Above-threshold ratio does not quantify sediment transport.'}
 else if(id===11){let S=.001,t=30,u=c*c*S/(4*b*t),s=a/(4*PI*b)*log(2.25*b*t/(c*c*S));res={'Approx. drawdown (m)':s,'Dimensionless u':u,'Approximation applicable (u < 0.01)':u<.01?1:0};units='m';for(let k=0;k<=24;k++){let r=max(5,c*(.3+.06*k));let uk=r*r*S/(4*b*t),ss=a/(4*PI*b)*log(2.25*b*t/(r*r*S));push(r,uk<.01?ss:NaN)}note='Cooper–Jacob late-time approximation valid approximately for u < 0.01; plot masks large-u values.'}
 else if(id===12){let st=c,def=0;for(let t=1;t<=10;t++){let available=st+a;let extracted=min(b,available);def+=b-extracted;st=max(0,available-extracted);push(t,st)}res={'Ending storage (ML)':st,'Unmet abstraction (ML)':def,'Annual net (ML/year)':a-b};units='ML';note='Lumped storage, no river capture or lateral exchange; not sustainable-yield certification.'}
 else if(id===13){let z=(a-b)/c;res={'Rainfall anomaly z-score':z,'Difference from baseline (mm)':a-b};units='z-score';for(let k=0;k<=24;k++){let rain=a+(k-12)*c/4;push(rain,(rain-b)/c)}note='This is a standardized anomaly, NOT the fitted Standardized Precipitation Index.'}
 else if(id===14){let p=1-Math.pow(1-1/a,b);res={'At least one exceedance (%)':100*p,'Annual exceedance (%)':100/a,'Illustrative exposed value':c};units='Probability (%)';for(let t=1;t<=b;t++)push(t,100*(1-Math.pow(1-1/a,t)));note='Stationary independent annual Bernoulli model; value is not expected loss.'}
 else if(id===15){let available=max(0,a-b),served=min(available,c);res={'Human withdrawal (ML/day)':served,'Unmet demand (ML/day)':c-served,'Ecological-flow deficit (ML/day)':max(0,b-a)};units='ML/day';for(let k=0;k<=20;k++){let flow=a*(.5+.05*k);push(flow,min(c,max(0,flow-b)))}note='Static threshold, not a seasonal ecological flow regime.'}
 else if(id===16){let sum=a+b+c,wa=a/sum,wb=b/sum,wc=c/sum,alpha=wa*92+wb*50+wc*42,beta=wa*70+wb*88+wc*65;res={'Option A score':alpha,'Option B score':beta,'Margin A minus B':alpha-beta};units='Score / 100';for(let k=0;k<=20;k++){let w=k/20,rest=(1-w),ec=rest*(b/(b+c)),co=rest*(c/(b+c));push(w*100,w*92+ec*50+co*42-(w*70+ec*88+co*65))}note='Synthetic scores and normalized weights; legal vetoes not modeled.'}
 else throw Error('Unrecognized lab '+id);
 for(let p of series){if(!Number.isFinite(p.y))p.y=null;}
 for(let k in res){if(!Number.isFinite(res[k]))throw Error('Nonfinite result '+k)}
 return {res,series,units,note};
  }

  var WRE_MODELS = [
  {
    "id": 1,
    "title": "Basin Water Balance",
    "unit": 1,
    "params": [
      {
        "name": "Precipitation",
        "unit": "mm/yr",
        "min": 900,
        "max": 1800,
        "step": 25,
        "default": 1200
      },
      {
        "name": "Evapotranspiration",
        "unit": "mm/yr",
        "min": 400,
        "max": 850,
        "step": 25,
        "default": 650
      },
      {
        "name": "Runoff depth",
        "unit": "mm/yr",
        "min": 150,
        "max": 700,
        "step": 5,
        "default": 420
      }
    ],
    "equation": "\u0394S = P \u2212 ET \u2212 Q",
    "assumption": "A closed catchment accounting exercise assuming no lateral groundwater import or export and no other withdrawals. The residual is a storage change or an unclosed balance, not automatically usable supply.",
    "question": "If precipitation increases by 10% with all other terms fixed, should the residual increase by precisely that volume? What physical feedbacks would invalidate holding evapotranspiration and runoff fixed?"
  },
  {
    "id": 2,
    "title": "Demand Growth & Capacity",
    "unit": 1,
    "params": [
      {
        "name": "Current demand",
        "unit": "ML/day",
        "min": 10,
        "max": 80,
        "step": 1,
        "default": 35
      },
      {
        "name": "Annual growth",
        "unit": "%/yr",
        "min": 0,
        "max": 7,
        "step": 0.05,
        "default": 2.2
      },
      {
        "name": "Planning horizon",
        "unit": "years",
        "min": 1,
        "max": 35,
        "step": 1,
        "default": 20
      }
    ],
    "equation": "D(t) = D\u2080 (1+g)^t",
    "assumption": "The growth rate and per-capita use are held constant; demand projections are planning scenarios, not demographic forecasts.",
    "question": "How does reducing leaks alter the baseline independently of population growth, and why can peak-day capacity be more critical than annual demand?"
  },
  {
    "id": 3,
    "title": "Allocation under Minimums",
    "unit": 2,
    "params": [
      {
        "name": "Available water",
        "unit": "ML/day",
        "min": 20,
        "max": 110,
        "step": 2,
        "default": 70
      },
      {
        "name": "Essential minimum",
        "unit": "ML/day",
        "min": 10,
        "max": 45,
        "step": 1,
        "default": 25
      },
      {
        "name": "Other requests",
        "unit": "ML/day",
        "min": 20,
        "max": 100,
        "step": 1,
        "default": 65
      }
    ],
    "equation": "Essential served = min(A,E); optional served = min(max(A\u2212E,0), R)",
    "assumption": "A single-period priority allocation assuming all water is physically interchangeable, with no spatial conveyance, quality or institutional restrictions.",
    "question": "At which supply value does the essential minimum become unmet? Explain why the priority rule must be established outside the numerical model."
  },
  {
    "id": 4,
    "title": "Competing Demand Scenarios",
    "unit": 2,
    "params": [
      {
        "name": "Supply",
        "unit": "ML/day",
        "min": 25,
        "max": 120,
        "step": 5,
        "default": 75
      },
      {
        "name": "Agriculture requested",
        "unit": "ML/day",
        "min": 15,
        "max": 110,
        "step": 5,
        "default": 60
      },
      {
        "name": "Municipal minimum",
        "unit": "ML/day",
        "min": 10,
        "max": 60,
        "step": 2,
        "default": 30
      }
    ],
    "equation": "Municipal first; remaining supply distributed to agriculture",
    "assumption": "The simplified rule is not a general basin optimizer and does not establish water rights. All demands are treated as withdrawals with no return flows.",
    "question": "Which unmet demand rises first when supply falls? What would happen if ecological flows were a binding constraint?"
  },
  {
    "id": 5,
    "title": "Reservoir Storage Routing",
    "unit": 3,
    "params": [
      {
        "name": "Base inflow",
        "unit": "ML/day",
        "min": 4,
        "max": 65,
        "step": 1,
        "default": 25
      },
      {
        "name": "Target release",
        "unit": "ML/day",
        "min": 5,
        "max": 65,
        "step": 1,
        "default": 30
      },
      {
        "name": "Initial storage",
        "unit": "ML",
        "min": 100,
        "max": 900,
        "step": 10,
        "default": 550
      }
    ],
    "equation": "S[t+1] = min(C,max(0,S[t] + I[t]\u2212R[t]\u2212E)); spill tracked",
    "assumption": "Thirty synthetic daily flows use a fixed sinusoidal pulse, a constant target release, evaporation of 1 ML/day and fixed capacity of 850 ML. It is not a real reservoir forecast.",
    "question": "Compare days with spill to days with shortages. Why must mass balance include delivered release, spill and evaporation separately?"
  },
  {
    "id": 6,
    "title": "Flood-Space Operating Rule",
    "unit": 3,
    "params": [
      {
        "name": "Flood pulse peak",
        "unit": "ML/day",
        "min": 30,
        "max": 150,
        "step": 5,
        "default": 85
      },
      {
        "name": "Controlled outlet",
        "unit": "ML/day",
        "min": 15,
        "max": 85,
        "step": 5,
        "default": 45
      },
      {
        "name": "Starting storage",
        "unit": "ML",
        "min": 100,
        "max": 800,
        "step": 10,
        "default": 470
      }
    ],
    "equation": "S[t+1] = S[t] + inflow \u2212 controlled outflow \u2212 spill",
    "assumption": "Capacity is 800 ML; a synthetic ten-day triangular pulse is followed by lower inflow. Real reservoir outlets are stage dependent and have operating and safety constraints.",
    "question": "How does increasing pre-storm drawdown change the downstream peak and later supply reliability?"
  },
  {
    "id": 7,
    "title": "Crop Water Demand",
    "unit": 4,
    "params": [
      {
        "name": "Reference ET",
        "unit": "mm/day",
        "min": 2,
        "max": 9,
        "step": 0.25,
        "default": 5.5
      },
      {
        "name": "Crop coefficient Kc",
        "unit": "ratio",
        "min": 0.35,
        "max": 1.4,
        "step": 0.05,
        "default": 1.1
      },
      {
        "name": "Effective rainfall",
        "unit": "mm/day",
        "min": 0,
        "max": 6,
        "step": 0.05,
        "default": 1.8
      }
    ],
    "equation": "ETc = Kc \u00d7 ETo; net irrigation = max(0, ETc\u2212Pe)",
    "assumption": "Crop coefficient is a teaching input, not an official crop recommendation. No root-zone carryover or capillary rise is modeled.",
    "question": "How does changing Kc for a growth stage influence net water need, and when can rainfall fully cover ET?"
  },
  {
    "id": 8,
    "title": "Canal Conveyance Loss",
    "unit": 4,
    "params": [
      {
        "name": "Headflow",
        "unit": "m\u00b3/s",
        "min": 1,
        "max": 45,
        "step": 1,
        "default": 18
      },
      {
        "name": "Loss coefficient",
        "unit": "1/km",
        "min": 0.002,
        "max": 0.12,
        "step": 0.002,
        "default": 0.028
      },
      {
        "name": "Canal length",
        "unit": "km",
        "min": 1,
        "max": 40,
        "step": 1,
        "default": 16
      }
    ],
    "equation": "Q(L) = Q\u2080 exp(\u2212kL)",
    "assumption": "An exponentially decreasing flow assumes an effective distributed fractional loss, without offtakes or changing geometry. Seepage may recharge groundwater.",
    "question": "If lining halves the loss coefficient, how much extra water reaches the tail, and how could a basin-level account change the interpretation?"
  },
  {
    "id": 9,
    "title": "Trapezoidal Channel Rating",
    "unit": 5,
    "params": [
      {
        "name": "Water depth",
        "unit": "m",
        "min": 0.4,
        "max": 5,
        "step": 0.1,
        "default": 2
      },
      {
        "name": "Bed slope",
        "unit": "m/m",
        "min": 0.0001,
        "max": 0.004,
        "step": 0.0001,
        "default": 0.001
      },
      {
        "name": "Manning n",
        "unit": "s/m\u00b9\u141f\u00b3",
        "min": 0.015,
        "max": 0.065,
        "step": 0.001,
        "default": 0.032
      }
    ],
    "equation": "Q = (1/n) A R^(2/3) \u221aS; A=y(b+zy), P=b+2y\u221a(1+z\u00b2)",
    "assumption": "Trapezoid bottom width b=4 m and 1.5H:1V side slopes. Manning uniform-flow relation; no backwater, changing roughness or sediment movement.",
    "question": "Is doubling depth equivalent to doubling conveyance? Calculate the changes in area and wetted perimeter."
  },
  {
    "id": 10,
    "title": "Channel Boundary Shear",
    "unit": 5,
    "params": [
      {
        "name": "Hydraulic radius",
        "unit": "m",
        "min": 0.3,
        "max": 4,
        "step": 0.1,
        "default": 1.2
      },
      {
        "name": "Energy slope",
        "unit": "m/m",
        "min": 0.0001,
        "max": 0.005,
        "step": 0.0001,
        "default": 0.0012
      },
      {
        "name": "Critical shear",
        "unit": "Pa",
        "min": 2,
        "max": 55,
        "step": 1,
        "default": 17
      }
    ],
    "equation": "\u03c4 = \u03c1gRS; compare \u03c4 with assumed \u03c4critical",
    "assumption": "Mean boundary shear screening with water density 1000 kg/m\u00b3. Grain movement and bank stability require additional information beyond a single threshold.",
    "question": "Why does \u03c4 above a selected threshold not by itself determine a sediment transport rate?"
  },
  {
    "id": 11,
    "title": "Wellfield Drawdown Screen",
    "unit": 6,
    "params": [
      {
        "name": "Pumping rate",
        "unit": "m\u00b3/day",
        "min": 200,
        "max": 1800,
        "step": 50,
        "default": 700
      },
      {
        "name": "Transmissivity",
        "unit": "m\u00b2/day",
        "min": 100,
        "max": 2000,
        "step": 50,
        "default": 750
      },
      {
        "name": "Radius",
        "unit": "m",
        "min": 20,
        "max": 350,
        "step": 10,
        "default": 100
      }
    ],
    "equation": "s \u2248 Q/(4\u03c0T) ln(2.25Tt/(r\u00b2S)) (Cooper\u2013Jacob)",
    "assumption": "Illustrative confined-aquifer, constant-rate, large-time approximation with t=30 days and storativity S=0.001. Validity checked using u=r\u00b2S/(4Tt).",
    "question": "Does drawdown scale linearly with pumping? Which measured aquifer characteristics could invalidate this approximate prediction?"
  },
  {
    "id": 12,
    "title": "Groundwater Storage Scenario",
    "unit": 6,
    "params": [
      {
        "name": "Recharge",
        "unit": "ML/yr",
        "min": 20,
        "max": 180,
        "step": 5,
        "default": 90
      },
      {
        "name": "Abstraction",
        "unit": "ML/yr",
        "min": 20,
        "max": 240,
        "step": 5,
        "default": 110
      },
      {
        "name": "Initial store",
        "unit": "ML",
        "min": 100,
        "max": 1600,
        "step": 50,
        "default": 850
      }
    ],
    "equation": "G[t+1] = max(0,G[t] + recharge\u2212withdrawal)",
    "assumption": "A lumped groundwater bookkeeping model with ten annual steps; stream capture, lateral flow, salinity and variable recharge are omitted. Unmet abstraction is tracked.",
    "question": "Can an aquifer withdraw more than annual recharge temporarily without physically violating mass balance? Why does annual equality not establish sustainability?"
  },
  {
    "id": 13,
    "title": "Drought Anomaly Screen",
    "unit": 7,
    "params": [
      {
        "name": "Observed rainfall",
        "unit": "mm/year",
        "min": 250,
        "max": 1800,
        "step": 5,
        "default": 680
      },
      {
        "name": "Reference mean",
        "unit": "mm/year",
        "min": 600,
        "max": 1400,
        "step": 25,
        "default": 950
      },
      {
        "name": "Reference SD",
        "unit": "mm/year",
        "min": 70,
        "max": 330,
        "step": 10,
        "default": 170
      }
    ],
    "equation": "z = (Pobs\u2212\u03bc)/\u03c3",
    "assumption": "A standardized rainfall anomaly is not a fitted Standardized Precipitation Index. Changes in reference period and rainfall skewness affect classification.",
    "question": "How would changing the baseline period alter drought labeling even with the same observed rainfall?"
  },
  {
    "id": 14,
    "title": "Flood Lifetime Exceedance",
    "unit": 7,
    "params": [
      {
        "name": "Return period",
        "unit": "years",
        "min": 5,
        "max": 500,
        "step": 5,
        "default": 100
      },
      {
        "name": "Exposure horizon",
        "unit": "years",
        "min": 1,
        "max": 100,
        "step": 1,
        "default": 30
      },
      {
        "name": "Asset value",
        "unit": "million currency units",
        "min": 10,
        "max": 500,
        "step": 10,
        "default": 150
      }
    ],
    "equation": "P(at least one) = 1 \u2212 (1\u22121/T)^N",
    "assumption": "Assumes independent annual events and stationary exceedance probability. Asset exposure is illustrative; probability is not expected damage.",
    "question": "Can a 100-year event happen twice in ten years? What breaks the independence or stationarity assumption?"
  },
  {
    "id": 15,
    "title": "Environmental Flow Allocation",
    "unit": 8,
    "params": [
      {
        "name": "Natural flow",
        "unit": "ML/day",
        "min": 20,
        "max": 150,
        "step": 5,
        "default": 85
      },
      {
        "name": "Environmental reserve",
        "unit": "ML/day",
        "min": 10,
        "max": 75,
        "step": 5,
        "default": 35
      },
      {
        "name": "Human demand",
        "unit": "ML/day",
        "min": 20,
        "max": 100,
        "step": 5,
        "default": 65
      }
    ],
    "equation": "Allowed withdrawal = min(demand,max(0,natural flow\u2212reserve))",
    "assumption": "A static environmental threshold is only an educational simplification. Real flow regimes use seasonal ecological objectives and local statutory requirements.",
    "question": "When is the ecological reserve itself infeasible under the natural flow? How should that be reported rather than disguised as compliance?"
  },
  {
    "id": 16,
    "title": "Stakeholder Weight Sensitivity",
    "unit": 8,
    "params": [
      {
        "name": "Reliability weight",
        "unit": "%",
        "min": 10,
        "max": 70,
        "step": 5,
        "default": 45
      },
      {
        "name": "Ecology weight",
        "unit": "%",
        "min": 5,
        "max": 65,
        "step": 5,
        "default": 35
      },
      {
        "name": "Cost score weight",
        "unit": "%",
        "min": 10,
        "max": 70,
        "step": 5,
        "default": 20
      }
    ],
    "equation": "Score = normalized weighted sum of 3 illustrative criteria",
    "assumption": "Two hypothetical options have fixed synthetic 0\u2013100 scores; weight inputs are normalized to 100% rather than assumed to sum perfectly. A noncompensatory legal veto is not included.",
    "question": "Find a weight combination that changes the preferred alternative. Why is a weighted score not legal permission or consensus?"
  }
];

  var MODELS = WRE_MODELS.map(function(mDef) {
    var controlsHtml = mDef.params.map(function(p, pi) {
      return '<div class="param" style="margin-bottom:0.75rem;"><label for="wre_' + mDef.id + '_' + pi + '">' + p.name + ' <span class="unit" style="color:#64748b;">(' + p.unit + ')</span>: <span id="v_wre_' + mDef.id + '_' + pi + '" style="font-weight:700;color:#2563eb;">' + p.default + '</span></label>' +
             '<input id="wre_' + mDef.id + '_' + pi + '" data-pidx="' + pi + '" type="range" min="' + p.min + '" max="' + p.max + '" step="' + p.step + '" value="' + p.default + '" style="width:100%;accent-color:#2563eb;"></div>';
    }).join('');

    var html = '<div class="sim-header"><span class="badge" style="display:inline-block;padding:0.2rem 0.5rem;background:#dbeafe;color:#1e40af;border-radius:4px;font-size:0.75rem;font-weight:600;margin-bottom:0.5rem;">Model ' + mDef.id + ' · Unit ' + mDef.unit + '</span>' +
               '<h3 style="margin:0 0 0.5rem 0;font-size:1.15rem;color:#0f172a;">' + mDef.title + '</h3>' +
               '<div style="background:#eff6ff;padding:0.5rem 0.75rem;border-radius:4px;font-family:monospace;font-size:0.85rem;color:#1e40af;margin-bottom:0.75rem;">' + (mDef.equation || '') + '</div>' +
               '<p style="margin:0 0 1rem 0;color:#475569;font-size:0.9rem;">' + (mDef.assumption || '') + '</p></div>' +
               '<div class="sim-controls" style="background:#f8fafc;padding:1rem;border-radius:8px;margin-bottom:1rem;border:1px solid #e2e8f0;">' + controlsHtml + '</div>' +
               '<div class="readouts" style="background:#f0fdf4;border-left:4px solid #16a34a;padding:0.75rem 1rem;border-radius:4px;margin-bottom:1rem;">' +
                 '<div class="metrics-grid" style="display:flex;flex-wrap:wrap;gap:1rem;"></div>' +
                 '<div class="interp-text" style="font-size:0.85rem;color:#14532d;margin-top:0.5rem;font-style:italic;"></div>' +
               '</div>' +
               '<div class="plot" style="margin:1rem 0;display:block;"><svg class="plot-svg" viewBox="0 0 780 330" style="width:100%;height:auto;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;"></svg></div>';

    return {
      idx: mDef.id,
      unit: mDef.unit,
      html: html,
      init: function(card) {
        try {
          var pVals = mDef.params.map(function(p) { return p.default; });
          var metricsGrid = card.querySelector('.metrics-grid');
          var interpEl = card.querySelector('.interp-text');
          var svgEl = card.querySelector('.plot-svg');

          function drawGraph(series, title) {
            if (!svgEl || !series.length) return;
            svgEl.innerHTML = '';
            var W = 780, H = 330, L = 70, R = 24, T = 27, B = 58;
            var good = series.filter(function(p) { return p.y !== null && Number.isFinite(p.y); });
            if (!good.length) return;
            var xmin = Math.min.apply(null, good.map(function(p) { return p.x; }));
            var xmax = Math.max.apply(null, good.map(function(p) { return p.x; }));
            var ymin = Math.min(0, Math.min.apply(null, good.map(function(p) { return p.y; })));
            var ymax = Math.max.apply(null, good.map(function(p) { return p.y; }));
            if (xmax === xmin) xmax = xmin + 1;
            if (ymax === ymin) ymax = ymin + 1;

            var X = function(x) { return L + (x - xmin) / (xmax - xmin || 1) * (W - L - R); };
            var Y = function(y) { return H - B - (y - ymin) / (ymax - ymin || 1) * (H - T - B); };

            var NS = 'http://www.w3.org/2000/svg';
            function node(tag, attrs, txt) {
              var el = document.createElementNS(NS, tag);
              for (var k in attrs) el.setAttribute(k, String(attrs[k]));
              if (txt !== undefined) el.textContent = txt;
              svgEl.appendChild(el);
              return el;
            }

            for (var i = 0; i < 5; i++) {
              var yVal = ymin + (ymax - ymin) * i / 4, yPos = Y(yVal);
              node('line', { x1: L, y1: yPos, x2: W - R, y2: yPos, stroke: '#e2e8f0', 'stroke-dasharray': '4 6' });
              node('text', { x: L - 10, y: yPos + 4, 'text-anchor': 'end', fill: '#64748b', 'font-size': '11' }, Number(yVal.toPrecision(3)).toString());
            }
            for (var j = 0; j < 5; j++) {
              var xVal = xmin + (xmax - xmin) * j / 4;
              node('text', { x: X(xVal), y: H - B + 20, 'text-anchor': 'middle', fill: '#64748b', 'font-size': '11' }, Number(xVal.toPrecision(3)).toString());
            }

            node('line', { x1: L, y1: T, x2: L, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' });
            node('line', { x1: L, y1: H - B, x2: W - R, y2: H - B, stroke: '#94a3b8', 'stroke-width': '1.5' });

            var pts = good.map(function(p) { return X(p.x).toFixed(1) + ',' + Y(p.y).toFixed(1); }).join(' ');
            node('polyline', { points: pts, fill: 'none', stroke: '#2563eb', 'stroke-width': '2.5' });
          }

          function render() {
            card.querySelectorAll('input[type="range"]').forEach(function(inp) {
              var pi = parseInt(inp.dataset.pidx, 10);
              pVals[pi] = Number(inp.value);
              var vLbl = card.querySelector('#v_wre_' + mDef.id + '_' + pi);
              if (vLbl) vLbl.textContent = inp.value;
            });

            var out = compute(mDef.id, pVals);
            if (metricsGrid && out.res) {
              var resKeys = Object.keys(out.res);
              metricsGrid.innerHTML = resKeys.map(function(k) {
                var val = out.res[k];
                var displayVal = Number.isFinite(val) ? Number(val.toPrecision(4)) : String(val);
                return '<div style="min-width:130px;"><span style="font-size:0.75rem;color:#166534;font-weight:600;display:block;">' + k + '</span><span style="font-size:1.25rem;font-weight:700;color:#15803d;">' + displayVal + '</span></div>';
              }).join('');
            }
            if (interpEl) interpEl.textContent = out.note || '';
            if (out.series) drawGraph(out.series, mDef.title);
          }

          card.querySelectorAll('input[type="range"]').forEach(function(inp) {
            inp.addEventListener('input', render);
          });
          render();
        } catch(err) {
          console.error('WRE sim error on model ' + mDef.id, err);
        }
      }
    };
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
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.filter(function(m) { return m.unit === 1; });
    modelsForUnit.forEach(function(m) {
      var card = document.createElement('section');
      card.className = 'ce-sim-card';
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
