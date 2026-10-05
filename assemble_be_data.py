import json

units = []
for i in range(1, 9):
    with open(f"be_u{i}.json", "r") as f:
        data = json.load(f)
        units.append(data)

course_data = {
    "courseId": "basic-electronics",
    "courseTitle": "Basic Electronics: Semiconductor Devices, Analog Circuits & Systems",
    "courseDescription": "A rigorous university digital textbook covering semiconductor diodes, rectifiers, filters, bipolar and field-effect transistors, power thyristors, small-signal and power amplifiers, feedback oscillators, analog modulation, and operational amplifier systems.",
    "units": units
}

js_content = f"window.COURSE_DATA = {json.dumps(course_data, indent=2)};\n"

with open("basic-electronics-data.js", "w") as f:
    f.write(js_content)

print(f"basic-electronics-data.js successfully written with {len(units)} units!")
