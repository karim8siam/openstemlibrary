"""Assemble the original ten saved drafts without duplicating worked solutions."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SLUG='probability-and-probability-distributions'
DRAFT=ROOT/'publishing/drafts/statistics-probability-probability-and-probability-distributions'
outline=json.loads((ROOT/'publishing/outlines'/f'{SLUG}.json').read_text())
simulations={1:[('Counting finite','prob-finite')],2:[("Bayes' theorem",'prob-bayes')],3:[('Mixed distributions','prob-density')],4:[('Conditional distributions','prob-joint')],6:[('Comparing binomial','prob-sampling')],7:[('Negative binomial waiting','prob-waiting')],8:[('Remaining lifetime','prob-survival')],9:[('The normal CDF','prob-normal'),('Beta CDFs','prob-beta')],10:[('A convergence explorer','prob-convergence')]}
units=[]
for i in range(1,11):
 text=(DRAFT/f'unit-{i}.md').read_text();title=text.splitlines()[0].split(': ',1)[1]
 chunks=re.split(r'^## (.+)\n',text,flags=re.M);sections=[];problems=[]
 for j in range(1,len(chunks),2):
  heading,body=chunks[j],chunks[j+1].strip()
  match=re.fullmatch(r'Fully worked question (\d+): (.+)',heading)
  if match:
   number=int(match[1]);parts=re.split(r'\*\*Solution, step (\d+): (.*?)\*\*\s*',body)
   question=re.sub(r'^\*\*Question\.\*\*\s*','',parts[0]).strip()
   steps=[dict(stepName=parts[k+1].rstrip('.'),explanation=parts[k+2].strip()) for k in range(1,len(parts),3)]
   assert len(steps)>=3,(i,heading,steps)
   problems.append(dict(id=f'prob-{i}-{number}',title=match[2],question=question,difficulty='Solved Problem',steps=steps))
  else:sections.append(dict(secNumber=f'{i}.{len(sections)+1}',heading=heading,content=body))
 assert len(problems)==3,(i,len(problems))
 sims=[]
 for heading,sim in simulations.get(i,[]):
  section=next(s for s in sections if heading in s['heading']);section.setdefault('simulations',[]).append(sim);sims.append(sim)
 # Explicit empty simulation list on first section prevents shared renderer fallback duplication.
 sections[0].setdefault('simulations',[])
 lead=sections[0]['content'].split('\n\n')[0]
 # Use a concise original outline-based summary rather than a long paragraph as metadata.
 summary='; '.join(outline['units'][i-1]['scope'])+'.'
 units.append(dict(id=f'prob-unit-{i}',number=i,title=title,leadSummary=summary,sections=sections,problems=problems,simulations=sims))
data=dict(title='Probability and Probability Distributions',language='en',curriculum='University of Dhaka Statistics B.S. Honours 2023–24: Stat H-102',units=units)
(ROOT/f'{SLUG}-data.js').write_text('// Original OpenSTEM probability teaching text, assembled from saved drafts.\nwindow.COURSE_DATA = '+json.dumps(data,ensure_ascii=False,indent=2)+';\n')
(DRAFT/'worked-solutions.json').write_text(json.dumps([u['problems'] for u in units],ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(units=len(units),worked_questions=sum(len(u['problems']) for u in units),explorers=sum(len(u['simulations']) for u in units),sections=sum(len(u['sections']) for u in units))))
