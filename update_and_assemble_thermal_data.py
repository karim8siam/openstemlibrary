import json

sim_map = {
    1: {
        "unit_sims": ["ideal-gas-processes-sim"],
        "sec_sims": { "u1-sec5": "ideal-gas-processes-sim" }
    },
    2: {
        "unit_sims": ["carnot-engine-sim", "refrigerator-heat-pump-sim"],
        "sec_sims": { "u2-sec3": "carnot-engine-sim", "u2-sec4": "refrigerator-heat-pump-sim" }
    },
    3: {
        "unit_sims": ["entropy-mixing-sim"],
        "sec_sims": { "u3-sec3": "entropy-mixing-sim" }
    },
    4: {
        "unit_sims": ["adiabatic-demag-sim"],
        "sec_sims": { "u4-sec5": "adiabatic-demag-sim" }
    },
    5: {
        "unit_sims": ["clapeyron-phase-diagram-sim"],
        "sec_sims": { "u5-sec2": "clapeyron-phase-diagram-sim" }
    },
    6: {
        "unit_sims": ["fourier-conduction-sim", "radial-heat-pipe-sim"],
        "sec_sims": { "u6-sec3": "radial-heat-pipe-sim", "u6-sec4": "fourier-conduction-sim" }
    },
    7: {
        "unit_sims": ["blackbody-spectrum-sim", "solar-radiation-balance-sim"],
        "sec_sims": { "u7-sec4": "blackbody-spectrum-sim", "u7-sec5": "solar-radiation-balance-sim" }
    },
    8: {
        "unit_sims": ["mean-free-path-sim", "brownian-motion-sim", "vanderwaals-pv-sim", "joule-thomson-throttling-sim"],
        "sec_sims": {
            "u8-sec1": "mean-free-path-sim",
            "u8-sec3": "brownian-motion-sim",
            "u8-sec4": "vanderwaals-pv-sim",
            "u8-sec5": "joule-thomson-throttling-sim"
        }
    }
}

units = []
for i in range(1, 9):
    with open(f"tp_u{i}.json") as f:
        u = json.load(f)

    # Attach simulations
    cfg = sim_map.get(i, {})
    u["simulations"] = cfg.get("unit_sims", [])
    sec_sims = cfg.get("sec_sims", {})
    for sec in u.get("sections", []):
        sec_id = sec.get("id")
        if sec_id in sec_sims:
            sec["simulation"] = sec_sims[sec_id]
        if "heading" not in sec:
            sec["heading"] = sec.get("title", "")

    # Save back
    with open(f"tp_u{i}.json", "w") as f:
        json.dump(u, f, indent=2)

    units.append(u)

data = {
    "courseId": "thermal-physics",
    "courseTitle": "Thermal Physics",
    "courseSubtitle": "Classical Thermodynamics, Statistical Entropy, Thermodynamic Potentials, Heat Transfer & Kinetic Theory",
    "units": units
}

js_content = f"// Thermal Physics Complete Interactive Textbook Dataset\n// Pure client-side data architecture\nwindow.COURSE_DATA = {json.dumps(data, indent=2)};\n"

with open("thermal-physics-data.js", "w") as f:
    f.write(js_content)

print(f"thermal-physics-data.js updated with 14 simulations across 8 units. Total size: {len(js_content)} bytes.")
