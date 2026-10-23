#!/usr/bin/env python3
"""
Assemble the 8 units of Statistical Simulation and Monte Carlo Methods
into src/subjects/statistics-probability/statistical-simulation-and-monte-carlo-methods/statistical-simulation-and-monte-carlo-methods-data.js
and publishing/drafts/statistics-probability-statistical-simulation-and-monte-carlo-methods/worked-solutions.json.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "statistical-simulation-and-monte-carlo-methods"
DRAFT_DIR = ROOT / f"publishing/drafts/statistics-probability-{SLUG}"
OUTLINE_PATH = ROOT / f"publishing/outlines/{SLUG}.json"
TARGET_DIR = ROOT / "src/subjects/statistics-probability" / SLUG

outline = json.loads(OUTLINE_PATH.read_text(encoding="utf-8"))

simulations_map = {
    1: [("Linear Congruential", "sim-prng-lcg"), ("Uniform Random", "sim-prng-lcg"), ("Pseudorandom", "sim-prng-lcg")],
    3: [("Rejection Sampling", "sim-rejection-sampling"), ("Envelope", "sim-rejection-sampling"), ("Acceptance", "sim-rejection-sampling")],
    5: [("Importance Sampling", "sim-importance-sampling"), ("Variance Reduction", "sim-importance-sampling"), ("Antithetic", "sim-importance-sampling")],
    6: [("Metropolis", "sim-mcmc-metropolis"), ("Markov Chain", "sim-mcmc-metropolis"), ("MCMC", "sim-mcmc-metropolis")]
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
                "id": f"stat-sim-{i}-{number}",
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
        "id": f"stat-sim-unit-{i}",
        "number": i,
        "title": title,
        "leadSummary": summary,
        "sections": sections,
        "problems": problems,
        "simulations": unit_sims
    })

course_data = {
    "title": "Statistical Simulation and Monte Carlo Methods",
    "language": "en",
    "curriculum": "University of Dhaka Statistics B.S. Honours 2023–24: Stat H-307",
    "units": units
}

TARGET_DIR.mkdir(parents=True, exist_ok=True)
data_js_path = TARGET_DIR / f"{SLUG}-data.js"
data_js_path.write_text(
    "// Original OpenSTEM Statistical Simulation and Monte Carlo Methods teaching text, assembled from saved drafts.\n"
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
