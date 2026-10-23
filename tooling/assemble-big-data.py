#!/usr/bin/env python3
"""
Assemble the 8 units of Big Data Methods for Statistics
into src/subjects/statistics-probability/big-data-methods-for-statistics/big-data-methods-for-statistics-data.js
and publishing/drafts/statistics-probability-big-data-methods-for-statistics/worked-solutions.json.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "big-data-methods-for-statistics"
DRAFT_DIR = ROOT / f"publishing/drafts/statistics-probability-{SLUG}"
OUTLINE_PATH = ROOT / f"publishing/outlines/{SLUG}.json"
TARGET_DIR = ROOT / "src/subjects/statistics-probability" / SLUG

outline = json.loads(OUTLINE_PATH.read_text(encoding="utf-8"))

simulations_map = {
    1: [("Concentration of Measure", "bigdata-dim-concentration"), ("Curse of Dimensionality", "bigdata-dim-concentration"), ("Statistical Geometry", "bigdata-dim-concentration")],
    3: [("The Lasso", "bigdata-lasso-path"), ("Coordinate Descent", "bigdata-lasso-path"), ("Ridge Regression", "bigdata-lasso-path")],
    5: [("Stochastic Gradient Descent", "bigdata-sgd-optimizer"), ("Mini-Batch", "bigdata-sgd-optimizer"), ("Adam Optimizer", "bigdata-sgd-optimizer")],
    8: [("False Discovery Rate", "bigdata-fdr-benjamini"), ("Benjamini-Hochberg", "bigdata-fdr-benjamini"), ("Storey", "bigdata-fdr-benjamini")]
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
                    "id": f"big-data-{i}-{q_num}",
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
        "id": f"big-data-unit-{i}",
        "number": i,
        "title": title,
        "leadSummary": summary,
        "sections": sections,
        "problems": problems,
        "simulations": unit_sims
    })

course_data = {
    "title": "Big Data Methods for Statistics",
    "language": "en",
    "curriculum": "University of Dhaka Statistics B.S. Honours 2023–24: Stat H-308",
    "units": units
}

TARGET_DIR.mkdir(parents=True, exist_ok=True)
data_js_path = TARGET_DIR / f"{SLUG}-data.js"
data_js_path.write_text(
    "// Original OpenSTEM Big Data Methods for Statistics teaching text, assembled from saved drafts.\n"
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
