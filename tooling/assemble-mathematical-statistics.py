#!/usr/bin/env python3
"""
Assemble the 8 units of Mathematical Statistics
into mathematical-statistics-data.js and worked-solutions.json.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "mathematical-statistics"
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-mathematical-statistics"
OUTLINE_PATH = ROOT / f"publishing/outlines/{SLUG}.json"

outline = json.loads(OUTLINE_PATH.read_text(encoding="utf-8"))

simulations_map = {
    3: [("Exact Sampling Distributions", "stat-sampling-dists")],
    4: [("Order Statistics", "stat-order-stats")],
    7: [("Central Limit Theorem", "stat-clt-convergence")],
    8: [("Delta Method", "stat-delta-method")]
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
        
        match = re.fullmatch(r"Fully worked question (\d+): (.+)", heading)
        if match:
            number = int(match[1])
            q_title = match[2].strip()
            
            # Split into question and steps
            step_chunks = re.split(r"^### Solution, step (\d+): (.*?)\n", body, flags=re.M)
            q_part = step_chunks[0]
            # Strip ### Question
            question = re.sub(r"^### Question\s*\n*", "", q_part).strip()
            
            steps = []
            for k in range(1, len(step_chunks), 3):
                step_num = int(step_chunks[k])
                step_name = step_chunks[k+1].strip()
                step_content = step_chunks[k+2].strip()
                steps.append({
                    "stepName": step_name,
                    "explanation": step_content
                })
            
            assert len(steps) >= 3, f"Unit {i} question {number} has only {len(steps)} steps"
            problems.append({
                "id": f"math-stat-{i}-{number}",
                "title": q_title,
                "question": question,
                "difficulty": "Solved Problem",
                "steps": steps
            })
        else:
            # Normal section
            sec_num_match = re.match(r"^(\d+\.\d+)\s*(.*)", heading)
            if sec_num_match:
                sec_number = sec_num_match[1]
                clean_heading = sec_num_match[2].strip()
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
            matched_sec["simulations"].append(sim_id)
            unit_sims.append(sim_id)
        else:
            # Fallback to first section if heading didn't match
            sections[0]["simulations"].append(sim_id)
            unit_sims.append(sim_id)
    
    scope_list = outline["units"][i-1].get("scope", [])
    summary = "; ".join(scope_list) + "."
    
    units.append({
        "id": f"math-stat-unit-{i}",
        "number": i,
        "title": title,
        "leadSummary": summary,
        "sections": sections,
        "problems": problems,
        "simulations": unit_sims
    })

course_data = {
    "title": "Mathematical Statistics",
    "language": "en",
    "curriculum": "University of Dhaka Statistics B.S. Honours 2023–24: Stat H-202",
    "units": units
}

data_js_path = ROOT / f"{SLUG}-data.js"
data_js_path.write_text(
    "// Original OpenSTEM Mathematical Statistics teaching text, assembled from saved drafts.\n"
    "window.COURSE_DATA = " + json.dumps(course_data, ensure_ascii=False, indent=2) + ";\n",
    encoding="utf-8"
)

worked_solutions_path = DRAFT_DIR / "worked-solutions.json"
worked_solutions_path.write_text(
    json.dumps([u["problems"] for u in units], ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8"
)

print(json.dumps({
    "units": len(units),
    "worked_questions": sum(len(u["problems"]) for u in units),
    "explorers": sum(len(u["simulations"]) for u in units),
    "sections": sum(len(u["sections"]) for u in units),
    "data_js_size_bytes": data_js_path.stat().st_size
}, indent=2))
