import json

sim_map = {
    "u1-sec3": "pn-junction-diode-sim",
    "u1-sec4": "full-wave-bridge-rectifier-sim",
    "u1-sec5": "capacitor-filter-ripple-sim",
    "u1-sec6": "zener-diode-regulator-sim",
    "u2-sec1": "bjt-ce-characteristics-sim",
    "u2-sec3": "jfet-drain-characteristics-sim",
    "u3-sec2": "scr-phase-control-sim",
    "u3-sec3": "ujt-relaxation-oscillator-sim",
    "u4-sec1": "bjt-ce-amplifier-waveform-sim",
    "u4-sec4": "class-b-push-pull-sim",
    "u5-sec2": "colpitts-hartley-oscillator-sim",
    "u5-sec3": "wien-bridge-oscillator-sim",
    "u6-sec2": "am-modulation-envelope-sim",
    "u6-sec4": "superheterodyne-mixer-sim",
    "u7-sec2": "opamp-inverting-noninverting-sim",
    "u8-sec2": "schmitt-trigger-hysteresis-sim"
}

units = []
for i in range(1, 9):
    with open(f"be_u{i}.json", "r") as f:
        u = json.load(f)
    for sec in u.get("sections", []):
        sid = sec.get("id")
        if sid in sim_map:
            sec["simulation"] = sim_map[sid]
    with open(f"be_u{i}.json", "w") as f:
        json.dump(u, f, indent=2)
    units.append(u)

course_data = {
    "courseId": "basic-electronics",
    "courseTitle": "Basic Electronics: Semiconductor Devices, Analog Circuits & Systems",
    "courseDescription": "A rigorous university digital textbook covering semiconductor diodes, rectifiers, filters, bipolar and field-effect transistors, power thyristors, small-signal and power amplifiers, feedback oscillators, analog modulation, and operational amplifier systems.",
    "units": units
}

js_content = f"window.COURSE_DATA = {json.dumps(course_data, indent=2)};\n"
with open("basic-electronics-data.js", "w") as f:
    f.write(js_content)

print(f"Updated basic-electronics-data.js with {len(sim_map)} simulations assigned across 8 units!")
