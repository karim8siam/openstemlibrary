"""Independent numerical checks using Python statistics, NumPy and SciPy.
These checks compare explicit answer records, not the JavaScript implementation.
"""
import json, math, statistics as st, itertools
from pathlib import Path
import numpy as np
from scipy import stats

root=Path(__file__).resolve().parents[1]
draft=root/'publishing/drafts/statistics-probability-introduction-to-statistics'
questions=json.loads((draft/'worked-solutions.json').read_text())
checked=[]
def check(unit,number,actual):
    p=questions[unit-1][number-1]
    expected=p['expected_values']
    assert set(actual)==set(expected),(p['id'],'unchecked answer fields')
    for key,value in actual.items():
        assert math.isclose(value,expected[key],rel_tol=1e-11,abs_tol=1e-11),(p['id'],key,value,expected[key])
    checked.append(dict(id=p['id'],status='pass',values=actual))

x=[1,2,3,4];pairs=list(itertools.combinations(x,2))
check(1,1,dict(population_mean=st.mean(x),sample_count=len(pairs),average_sample_mean=st.mean(map(st.mean,pairs))))
check(1,2,dict(observed_proportion=90/100,response_rate=100/1000))
x=[2,4,4,7,13];m=st.mean(x)
check(1,3,dict(total=sum(x),mean=m,sum_deviations=sum(v-m for v in x),range=max(x)-min(x)))
indicator=[1,0,1,1,0]
check(2,1,dict(indicator_mean=st.mean(indicator),alternate_code_mean=st.mean(2+5*v for v in indicator)))
check(2,2,dict(observed_proportion=24/80,lower_bound=24/100,upper_bound=(24+20)/100))
raw=[0,15,20,25,999];valid=[v for v in raw if v!=999]
check(2,3,dict(raw_code_mean=st.mean(raw),observed_mean=st.mean(valid),positive_only_mean=st.mean(v for v in valid if v>0)))
check(3,1,dict(count_density_1=8/10,count_density_2=12/20,relative_density_1=(8/20)/10,relative_density_2=(12/20)/20))
check(3,2,dict(late_given_bus=10/40,joint_bus_late=10/(40+60),bus_given_late=10/(10+6)))
check(3,3,dict(aggregate_A=(90+1)/(100+10),aggregate_B=(19+20)/(20+100),standardized_A=st.mean([90/100,1/10]),standardized_B=st.mean([19/20,20/100])))
q1,med,q3=np.quantile(range(1,9),[.25,.5,.75],method='linear')
check(4,1,dict(q1=float(q1),median=float(med),q3=float(q3),iqr=float(q3-q1),halves_q1=st.median(range(1,5)),halves_q3=st.median(range(5,9))))
x=[1,2,3,4,5,6,7,30];q1,q3=np.quantile(x,[.25,.75]);iqr=q3-q1;lo=q1-1.5*iqr;hi=q3+1.5*iqr;inside=[v for v in x if lo<=v<=hi]
check(4,2,dict(q1=float(q1),q3=float(q3),iqr=float(iqr),lower_fence=float(lo),upper_fence=float(hi),lower_whisker=min(inside),upper_whisker=max(inside),flagged_value=30))
x=np.array([-2,-1,0,1,2]);y=x*x
check(4,3,dict(x_mean=float(np.mean(x)),y_mean=float(np.mean(y)),sxy=float(np.dot(x-x.mean(),y-y.mean())),pearson_r=float(stats.pearsonr(x,y).statistic)))
expanded=[70]*10+[80]*30
check(5,1,dict(combined_mean=st.mean(expanded),equal_group_mean=st.mean([70,80]),combined_total=sum(expanded)))
distance=[60,60];speed=[30,60];hours=[d/v for d,v in zip(distance,speed)]
check(5,2,dict(equal_distance_speed=sum(distance)/sum(hours),equal_time_speed=sum(speed)/2,equal_distance_hours=sum(hours)))
x=[2,4,4,7,113]
check(5,3,dict(new_mean=st.mean(x),new_median=st.median(x),mean_change=st.mean(x)-6))
x=[2,4,4,7,13]
check(6,1,dict(sxx=sum((v-st.mean(x))**2 for v in x),descriptive_variance=st.pvariance(x),sample_variance=st.variance(x),descriptive_sd=st.pstdev(x),sample_sd=st.stdev(x)))
groups=[[1,3],[7,9]];allx=sum(groups,[]);grand=st.mean(allx)
within=sum(sum((v-st.mean(g))**2 for v in g) for g in groups);between=sum(len(g)*(st.mean(g)-grand)**2 for g in groups)
check(6,2,dict(overall_mean=grand,within_ss=within,between_ss=between,total_ss=within+between,descriptive_variance=st.pvariance(allx),sample_variance=st.variance(allx)))
check(6,3,dict(cv=st.stdev(x)/st.mean(x),cv_seconds=st.stdev([v*60 for v in x])/st.mean([v*60 for v in x]),cv_shifted=st.stdev([v+4 for v in x])/st.mean([v+4 for v in x])))
def moments(x):
    a=np.array(x,dtype=float);d=a-a.mean()
    return [float(a.mean())]+[float(np.mean(d**k)) for k in (2,3,4)]
x=[0,0,3];m,m2,m3,m4=moments(x)
check(7,1,dict(mean=m,m2=m2,m3=m3,m4=m4,skewness=float(stats.skew(x,bias=True)),raw_kurtosis=float(stats.kurtosis(x,fisher=False,bias=True)),excess_kurtosis=float(stats.kurtosis(x,fisher=True,bias=True))))
y=[10+2*v for v in x];z=[10-2*v for v in x];my,a,b,c=moments(y);mz,d,e,f=moments(z)
check(7,2,dict(mean_y=my,mean_z=mz,m2_y=a,m3_y=b,m4_y=c,m2_z=d,m3_z=e,m4_z=f,raw_kurtosis_y=float(stats.kurtosis(y,fisher=False)),raw_kurtosis_z=float(stats.kurtosis(z,fisher=False))))
x=[1,2,3,4,5,6,7,30];q1,median,q3=np.quantile(x,[.25,.5,.75]);m,m2,m3,_=moments(x)
check(7,3,dict(bowley=float((q3+q1-2*median)/(q3-q1)),mean=m,m2=m2,m3=m3,skewness=float(stats.skew(x,bias=True))))
x=np.array([1,2,3,4]);y=np.array([2,3,5,4]);dx=x-x.mean();dy=y-y.mean()
check(8,1,dict(sxx=float(dx@dx),syy=float(dy@dy),sxy=float(dx@dy),pearson_r=float(stats.pearsonr(x,y).statistic)))
tx=[10,20,20,40];ty=[1,3,2,4];c=d=t_x=t_y=0
for i,j in itertools.combinations(range(4),2):
    a=tx[j]-tx[i];b=ty[j]-ty[i]
    if a*b>0:c+=1
    elif a*b<0:d+=1
    elif a==0 and b!=0:t_x+=1
    elif b==0 and a!=0:t_y+=1
check(8,2,dict(spearman=float(stats.spearmanr(tx,ty).statistic),concordant=c,discordant=d,ties_x_only=t_x,ties_y_only=t_y,kendall_tau_b=float(stats.kendalltau(tx,ty,variant='b').statistic)))
bx=[1]*40+[0]*60;by=[1]*30+[0]*10+[1]*20+[0]*40
check(8,3,dict(determinant=30*40-10*20,phi=float(stats.pearsonr(bx,by).statistic)))
fit=stats.linregress(x,y);fitted=fit.intercept+fit.slope*x;residuals=y-fitted
sse=float(residuals@residuals);ssr=float(((fitted-y.mean())**2).sum());sst=float(dy@dy)
check(9,1,dict(slope=float(fit.slope),intercept=float(fit.intercept),residual_sum=float(residuals.sum()),sse=sse,ssr=ssr,sst=sst,r_squared=float(fit.rvalue**2)))
rev=stats.linregress(y,x)
check(9,2,dict(reverse_slope=float(rev.slope),reverse_intercept=float(rev.intercept),reciprocal_forward_slope=1/float(fit.slope),slope_product=float(fit.slope*rev.slope)))
check(9,3,dict(response_mean=float(y.mean()),response_median=float(np.median(y)),response_descriptive_variance=float(np.var(y)),response_range=float(np.ptp(y)),fitted_at_2_5=float(fit.intercept+fit.slope*2.5)))
assert len(checked)==27
# Independent fixtures for the actual JS simulations, including constant and offset data.
fixtures=[]
for values in [[2,4,4,7,13],[2,4,4,7,63],[0,0,3],[0,1,2,3,8],[0,0,0],[1,2,3,4,5,6,7,30],[1000000001,1000000002,1000000003],[-3,-2,-1]]:
    a=np.array(values,dtype=float);m,m2,m3,m4=moments(values);q1,median,q3=np.quantile(a,[.25,.5,.75]);iqr=q3-q1;lo=q1-1.5*iqr;hi=q3+1.5*iqr;inside=a[(a>=lo)&(a<=hi)]
    fixtures.append(dict(values=values,expected=dict(mean=m,m2=m2,m3=m3,m4=m4,q1=float(q1),median=float(median),q3=float(q3),iqr=float(iqr),lowerFence=float(lo),upperFence=float(hi),lowerWhisker=float(inside.min()),upperWhisker=float(inside.max()),sampleVariance=float(np.var(a,ddof=1)),skewness=float(stats.skew(a,bias=True)) if m2>0 else None,rawKurtosis=float(stats.kurtosis(a,fisher=False,bias=True)) if m2>0 else None)))
report=dict(status='pass',method='Python standard library statistics, NumPy quantiles and SciPy correlation, moments and regression; independent of JavaScript.',question_count=len(checked),numeric_field_count=sum(len(c['values']) for c in checked),questions=checked,
    supplemental_checks={'Kendall_W_identical':1,'Kendall_W_reversed':0,'point_biserial':float(stats.pointbiserialr([0,0,1,1],[1,3,5,7]).statistic),'eta_squared':between/(within+between),'ICC_1_1':((between/1)-(within/2))/((between/1)+(within/2))})
(draft/'numeric-checks.json').write_text(json.dumps(report,indent=2)+'\n')
(draft/'simulation-fixtures.json').write_text(json.dumps(fixtures,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['status','question_count','numeric_field_count']}))
