# -*- coding: utf-8 -*-
"""
Assembles reactor-physics-data.js from rp_u1.json through rp_u8.json
"""
import json

sim_map = {
    "sec-1-3": "reactor-atom-density-breeder-sim",
    "sec-2-4": "reactor-neutron-attenuation-flux-sim",
    "sec-3-5": "reactor-fission-yield-spectrum-sim",
    "sec-3-7": "reactor-fuel-burnup-energy-sim",
    "sec-4-4": "reactor-elastic-moderation-kinematics-sim",
    "sec-4-7": "reactor-slowing-down-density-resonance-sim",
    "sec-5-4": "reactor-fick-diffusion-flux-sim",
    "sec-5-6": "reactor-fermi-age-slowing-sim",
    "sec-6-2": "reactor-four-factor-lifecycle-sim",
    "sec-6-7": "reactor-six-factor-leakage-sim",
    "sec-7-5": "reactor-geometric-buckling-geometries-sim",
    "sec-7-7": "reactor-reflected-core-savings-sim",
    "sec-8-2": "reactor-point-kinetics-delayed-neutrons-sim",
    "sec-8-4": "reactor-inhour-reactivity-period-sim",
    "sec-8-6": "reactor-temperature-feedback-control-sim",
    "sec-8-7": "reactor-xenon-samarium-poisoning-sim",
}

units = []

for i in range(1, 9):
    filename = f"rp_u{i}.json"
    with open(filename, "r", encoding="utf-8") as f:
        u_raw = json.load(f)
    
    # Process sections and ensure simulation tags
    processed_sections = []
    for s in u_raw["sections"]:
        sec_id = s["id"]
        sec_copy = dict(s)
        if sec_id in sim_map:
            sim_name = sim_map[sec_id]
            sec_copy["simulation"] = sim_name
            sec_copy["simulations"] = [sim_name]
        processed_sections.append(sec_copy)
    
    # Process problems / exercises
    problems = u_raw.get("exercises") or u_raw.get("problems", [])
    
    unit_obj = {
        "id": f"unit{i}",
        "number": i,
        "unitNumber": i,
        "unitId": f"unit{i}-rp",
        "title": u_raw["title"],
        "subtitle": u_raw["subtitle"],
        "leadSummary": u_raw.get("leadSummary") or u_raw.get("summary"),
        "sections": processed_sections,
        "problems": problems
    }
    units.append(unit_obj)

course_data = {
    "courseId": "reactor-physics",
    "courseTitle": "Nuclear Reactor Physics: Neutron Diffusion, Chain Reactions, Criticality & Kinetics",
    "courseDescription": "An exhaustive, university honors-level treatment of nuclear reactor theory and engineering physics: Part A establishes microscopic foundations and fission energetics across four units (fundamentals of nuclear energy, mass defects, nucleon separation energies, and atom density calculations; neutron interactions, microscopic and macroscopic cross sections, scalar flux, and reaction rates; liquid drop fission mechanics, Watt prompt neutron spectrum, 6 delayed precursor groups, and fuel burnup in MWd/MTU; elastic scattering kinematics, collision parameter α, logarithmic energy decrement ξ, continuous slowing-down lethargy u, moderating ratios for H2O, D2O, and graphite, and resonance escape probability p). Part B analyzes neutron diffusion, multiplication, core criticality, and kinetics across four comprehensive units (derivation of the Boltzmann transport equation, P1 approximation, Fick's law of diffusion J = -D∇ϕ, extrapolated boundary distance d = 0.71λ_tr, point-source diffusion length L, Fermi age equation ∇²q = ∂q/∂τ, and migration area M²; self-sustaining chain reactions, the Four-Factor formula k_∞ = ϵ p η f, thermal reproduction factor η, and the Six-Factor formula k_eff = k_∞ P_FNL P_TNL; the one-group Helmholtz reactor equation ∇²ϕ + B²ϕ = 0, material vs geometric buckling B_m² = B_g², exact critical solutions for infinite slab, sphere, infinite cylinder, cuboid, and finite cylinder cores, minimum critical volume optimum H/D = 1.082, flux peaking factors, and two-region reflector savings δ; time-dependent point reactor kinetics PRKE, prompt criticality barrier ρ = β, prompt jump approximation, the Inhour equation relating reactivity to stable period T, control rod S-curves via perturbation theory, fuel Doppler broadening and moderator temperature feedback, and fission product poisoning dynamics including equilibrium Xenon-135 and the post-shutdown iodine pit). Accompanied by 16 real-time 60 FPS interactive canvas simulations and 24 multi-step solved honors examination problems.",
    "units": units
}

js_content = "window.COURSE_DATA = " + json.dumps(course_data, indent=2, ensure_ascii=False) + ";\n"
js_content += "window.RP_COURSE_DATA = window.COURSE_DATA;\n"

with open("reactor-physics-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("reactor-physics-data.js successfully assembled!")
print(f"Total units: {len(units)}")
total_secs = sum(len(u["sections"]) for u in units)
total_probs = sum(len(u["problems"]) for u in units)
total_sims = sum(1 for u in units for s in u["sections"] if "simulation" in s)
print(f"Total sections: {total_secs} (expected 56)")
print(f"Total problems: {total_probs} (expected 24)")
print(f"Total simulations: {total_sims} (expected 16)")
