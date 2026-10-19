#!/usr/bin/env python3
"""
Assemble the 8 units of Economic Statistics
into economic-statistics-data.js and worked-solutions.json.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "economic-statistics"
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-economic-statistics"
OUTLINE_PATH = ROOT / f"publishing/outlines/{SLUG}.json"

outline = json.loads(OUTLINE_PATH.read_text(encoding="utf-8"))

simulations_map = {
    2: [("Axiomatic", "econ-index-axioms"), ("Fisher", "econ-index-axioms")],
    4: [("Seasonal", "econ-timeseries-decomp"), ("Decomposition", "econ-timeseries-decomp")],
    5: [("Lorenz", "econ-lorenz-gini"), ("Gini", "econ-lorenz-gini")],
    7: [("Leontief", "econ-leontief-io"), ("Input-Output", "econ-leontief-io")]
}

units = []

for i in range(1, 9):
    unit_path = DRAFT_DIR / f"unit-{i}.md"
    text = unit_path.read_text(encoding="utf-8")
    
    first_line = text.splitlines()[0]
    title = first_line.split(": ", 1)[1] if ": " in first_line else first_line.lstrip("# ")
    
    chunks = re.split(r"^## (.+)\n", text, flags=re.M)
    sections = []
    problems = []
    
    for j in range(1, len(chunks), 2):
        heading = chunks[j].strip()
        body = chunks[j+1].strip()
        
        # Check if heading is "Fully worked question N: Title"
        match = re.fullmatch(r"Fully worked question (\d+): (.+)", heading)
        if match:
            number = int(match[1])
            q_title = match[2].strip()
            
            # Split into question and steps
            step_chunks = re.split(r"^### Solution, step (\d+): (.*?)\n", body, flags=re.M)
            q_part = step_chunks[0]
            question = re.sub(r"^### Question\s*\n*", "", q_part).strip()
            
            steps = []
            for k in range(1, len(step_chunks), 3):
                s_num = int(step_chunks[k])
                s_name = step_chunks[k+1].strip()
                s_expl = step_chunks[k+2].strip()
                steps.append({
                    "stepName": s_name,
                    "explanation": s_expl
                })
            
            problems.append({
                "id": f"econ-stat-{i}-{number}",
                "title": q_title,
                "question": question,
                "difficulty": "Solved Problem",
                "steps": steps
            })
        elif heading == "Worked Questions and Solutions":
            # In units 3-8, problems are inside this section
            q_blocks = re.split(r"^### Question (\d+): (.+)\n", body, flags=re.M)
            for q_idx in range(1, len(q_blocks), 3):
                number = int(q_blocks[q_idx])
                q_title = q_blocks[q_idx+1].strip()
                q_body = q_blocks[q_idx+2].strip()
                
                step_chunks = re.split(r"^### Solution, step (\d+): (.*?)\n", q_body, flags=re.M)
                question = step_chunks[0].strip()
                
                steps = []
                for k in range(1, len(step_chunks), 3):
                    s_num = int(step_chunks[k])
                    s_name = step_chunks[k+1].strip()
                    s_expl = step_chunks[k+2].strip()
                    steps.append({
                        "stepName": s_name,
                        "explanation": s_expl
                    })
                
                problems.append({
                    "id": f"econ-stat-{i}-{number}",
                    "title": q_title,
                    "question": question,
                    "difficulty": "Solved Problem",
                    "steps": steps
                })
        else:
            sec_match = re.match(r"^(\d+\.\d+)\s+(.+)", heading)
            if sec_match:
                sec_number = sec_match[1]
                clean_heading = sec_match[2].strip()
            else:
                sec_number = f"{i}.{len(sections)+1}"
                clean_heading = heading
            
            sections.append({
                "secNumber": sec_number,
                "heading": clean_heading,
                "content": body,
                "simulations": []
            })
    
    assert len(problems) == 3, f"Unit {i} expected 3 problems, got {len(problems)}"
    
    # Assign simulations
    unit_sims = []
    for heading_sub, sim_id in simulations_map.get(i, []):
        matched_sec = next((s for s in sections if heading_sub.lower() in s["heading"].lower()), None)
        if matched_sec:
            if sim_id not in matched_sec["simulations"]:
                matched_sec["simulations"].append(sim_id)
            if sim_id not in unit_sims:
                unit_sims.append(sim_id)
        else:
            if sim_id not in sections[0]["simulations"]:
                sections[0]["simulations"].append(sim_id)
            if sim_id not in unit_sims:
                unit_sims.append(sim_id)
    
    scope_list = outline["units"][i-1].get("scope", [])
    summary = "; ".join(scope_list) + "."
    
    units.append({
        "id": f"econ-stat-unit-{i}",
        "number": i,
        "title": title,
        "leadSummary": summary,
        "sections": sections,
        "problems": problems,
        "simulations": unit_sims
    })

course_data = {
    "title": "Economic Statistics",
    "language": "en",
    "curriculum": "University of Dhaka Statistics B.S. Honours 2023–24: Stat H-204 & Stat H-210",
    "units": units
}

# Write economic-statistics-data.js
js_content = "window.COURSE_DATA = " + json.dumps(course_data, indent=2, ensure_ascii=False) + ";\n"
(ROOT / f"{SLUG}-data.js").write_text(js_content, encoding="utf-8")
print(f"Generated {SLUG}-data.js: {len(units)} units, {sum(len(u['problems']) for u in units)} problems, {sum(len(u['sections']) for u in units)} sections.")

# Write worked-solutions.json
all_problems = []
for u in units:
    for p in u["problems"]:
        all_problems.append({
            "unit": u["number"],
            "unitTitle": u["title"],
            "id": p["id"],
            "title": p["title"],
            "question": p["question"],
            "steps": p["steps"]
        })

(DRAFT_DIR / "worked-solutions.json").write_text(json.dumps(all_problems, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Generated worked-solutions.json with {len(all_problems)} worked solutions.")
