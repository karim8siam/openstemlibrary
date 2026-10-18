import json

units = []
for i in range(1, 9):
    filename = f"dig_u{i}.json"
    with open(filename, "r", encoding="utf-8") as f:
        u = json.load(f)
        units.append(u)

course_data = {
    "courseId": "digital-electronics",
    "courseTitle": "Digital Electronics: Combinational & Sequential Systems, Data Converters, Memory & VLSI Fabrication",
    "courseDescription": "A comprehensive, university-grade digital textbook covering number systems, weighted codes, Hamming error correction, Boolean algebra, logic gates, TTL and CMOS semiconductor logic families, Karnaugh map minimization, Quine-McCluskey tabulation, arithmetic circuits, latches, edge-triggered flip-flops, 555 timer multivibrators, synchronous and ripple counters, shift registers, MSI logic, DAC and ADC data conversion systems, semiconductor memory architectures (SRAM, DRAM, ROM, Flash), and silicon integrated circuit VLSI microfabrication with 16 interactive 60 FPS simulations.",
    "units": units
}

js_content = "window.COURSE_DATA = " + json.dumps(course_data, indent=2, ensure_ascii=False) + ";\n"

with open("digital-electronics-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"digital-electronics-data.js generated successfully! Total units: {len(units)}")
total_secs = sum(len(u["sections"]) for u in units)
total_probs = sum(len(u.get("problems", [])) for u in units)
print(f"Total sections: {total_secs}, Total problems: {total_probs}")
