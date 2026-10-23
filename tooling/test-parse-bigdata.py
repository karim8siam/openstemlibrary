import re
from pathlib import Path

ROOT = Path(".")
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-big-data-methods-for-statistics"

for u in range(1, 9):
    text = (DRAFT_DIR / f"unit-{u}.md").read_text(encoding="utf-8")
    chunks = re.split(r"^## (.+)\n", text, flags=re.M)
    sections = []
    problems = []

    for j in range(1, len(chunks), 2):
        heading = chunks[j].strip()
        body = chunks[j+1].strip()

        if "worked problem" in heading.lower():
            # Parse the 3 worked questions from this chunk
            q_matches = re.finditer(r"### Fully worked question (\d+): (.*?)\n(.*?)(?=(?:### Fully worked question|\Z))", body, flags=re.S)
            for qm in q_matches:
                q_num = int(qm.group(1))
                q_title = qm.group(2).strip()
                q_body = qm.group(3).strip()

                # Parse steps
                step_chunks = re.finditer(r"### Solution, step (\d+): (.*?)\n(.*?)(?=(?:### Solution, step|---|\Z))", q_body, flags=re.S)
                steps = []
                for sm in step_chunks:
                    steps.append({
                        "stepName": sm.group(2).strip(),
                        "explanation": sm.group(3).strip()
                    })
                
                # Question text is everything before the first step
                first_step_match = re.search(r"### Solution, step", q_body)
                q_text = q_body[:first_step_match.start()].strip() if first_step_match else q_body

                problems.append({
                    "id": f"big-data-{u}-{q_num}",
                    "title": q_title,
                    "question": q_text,
                    "difficulty": "Solved Problem",
                    "steps": steps
                })
        else:
            sec_match = re.match(r"^(\d+\.\d+)\s+(.+)", heading)
            if sec_match:
                sec_number = sec_match[1]
                clean_heading = sec_match[2].strip()
            else:
                sec_number = f"{u}.{len(sections)+1}"
                clean_heading = heading
            sections.append({
                "secNumber": sec_number,
                "heading": clean_heading,
                "content": body,
                "simulations": []
            })

    print(f"Unit {u}: {len(sections)} sections, {len(problems)} problems")
    for p in problems:
        print(f"   {p['id']}: {p['title']} ({len(p['steps'])} steps)")
