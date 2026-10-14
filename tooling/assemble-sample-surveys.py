"""Assemble the original eight saved drafts without duplicating worked solutions."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'sample-surveys-and-sampling-theory'
DRAFT = ROOT / 'publishing/drafts/statistics-probability-sample-surveys-and-sampling-theory'
outline = json.loads((ROOT / 'publishing/outlines' / f'{SLUG}.json').read_text())

simulations = {
    2: [('Finite Population Correction', 'survey-fpc')],
    3: [('Allocation Schemes', 'survey-stratification')],
    4: [('Intracluster (Intraclass) Correlation', 'survey-cluster-deff')],
    5: [('Selection Mechanisms for PPS Sampling', 'survey-pps')]
}

units = []
for i in range(1, 9):
    text = (DRAFT / f'unit-{i}.md').read_text(encoding='utf-8')
    title = text.splitlines()[0].split(': ', 1)[1]
    chunks = re.split(r'^## (.+)\n', text, flags=re.M)
    sections = []
    problems = []

    for j in range(1, len(chunks), 2):
        heading, body = chunks[j], chunks[j+1].strip()
        match = re.fullmatch(r'Fully worked question (\d+): (.+)', heading)
        if match:
            number = int(match[1])
            parts = re.split(r'\*\*Solution, step (\d+): (.*?)\*\*\s*', body)
            question = re.sub(r'^\*\*Question\.\*\*\s*', '', parts[0]).strip()
            steps = [
                dict(stepName=parts[k+1].rstrip('.'), explanation=parts[k+2].strip())
                for k in range(1, len(parts), 3)
            ]
            assert len(steps) >= 3, (i, heading, len(steps))
            problems.append(dict(
                id=f'survey-{i}-{number}',
                title=match[2],
                question=question,
                difficulty='Solved Problem',
                steps=steps
            ))
        else:
            sections.append(dict(
                secNumber=f'{i}.{len(sections)+1}',
                heading=heading,
                content=body
            ))

    assert len(problems) == 3, (i, len(problems))
    sims = []
    for heading_sub, sim in simulations.get(i, []):
        section = next((s for s in sections if heading_sub in s['heading']), None)
        if section:
            section.setdefault('simulations', []).append(sim)
            sims.append(sim)
    sections[0].setdefault('simulations', [])
    summary = '; '.join(outline['units'][i-1]['scope']) + '.'
    units.append(dict(
        id=f'survey-unit-{i}',
        number=i,
        title=title,
        leadSummary=summary,
        sections=sections,
        problems=problems,
        simulations=sims
    ))

data = dict(
    title='Sample Surveys and Sampling Theory',
    language='en',
    curriculum='University of Dhaka Statistics B.S. Honours 2023–24: Stat H-103, H-109, H-302',
    units=units
)

(ROOT / f'{SLUG}-data.js').write_text(
    '// Original OpenSTEM survey sampling teaching text, assembled from saved drafts.\nwindow.COURSE_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n',
    encoding='utf-8'
)
(DRAFT / 'worked-solutions.json').write_text(
    json.dumps([u['problems'] for u in units], ensure_ascii=False, indent=2) + '\n',
    encoding='utf-8'
)
print(json.dumps(dict(
    units=len(units),
    worked_questions=sum(len(u['problems']) for u in units),
    explorers=sum(len(u['simulations']) for u in units),
    sections=sum(len(u['sections']) for u in units)
)))
