import json

units = []
for i in range(1, 9):
    with open(f"ssp2_u{i}.json", "r", encoding="utf-8") as f:
        u = json.load(f)
        unit_obj = {
            "id": f"unit{i}",
            "number": i,
            "unitNumber": i,
            "unitId": f"unit{i}-ssp2",
            "title": u["title"],
            "subtitle": u["subtitle"],
            "leadSummary": u["summary"],
            "sections": u["sections"],
            "problems": u["problems"]
        }
        units.append(unit_obj)

course_data = {
    "courseId": "solid-state-physics-2",
    "courseTitle": "Solid State Physics II: Quantum Theory of Solids, Semiconductors, Magnetism & Superconductivity",
    "courseDescription": "An advanced theoretical treatment of the quantum physics of solids: Bloch's theorem, crystal momentum, Kronig-Penney band model, nearly free electrons, tight binding, effective mass tensors, hole dynamics; intrinsic and extrinsic semiconductors, carrier statistics, Fermi level pinning, metal-semiconductor and p-n junctions, two-carrier Hall effect, quantum Hall effect; diamagnetism, Langevin and quantum Brillouin paramagnetism, crystal field splitting, Hund's rules, exchange interactions, superexchange, RKKY, ferromagnetism, Curie-Weiss law, Heisenberg model, spin waves (magnons), antiferromagnetism, ferrimagnetism, domains and hysteresis; phenomenological superconductivity, Meissner-Ochsenfeld effect, London equations, Pippard non-local electrodynamics, Ginzburg-Landau theory, Type-I and Type-II superconductors, Abrikosov flux vortex lattice; microscopic BCS theory, Cooper pairing, gap equation, quasiparticle density of states, Giaever tunneling, DC/AC Josephson effects, Shapiro steps, SQUIDs; optical properties of solids, complex dielectric function, Kramers-Kronig relations, excitons (Wannier-Mott and Frenkel), polaritons, polarons, point defects, color centers, and ionic diffusion; many-body electron-electron interactions, Hartree-Fock, dielectric screening (Thomas-Fermi, Lindhard, Friedel oscillations), Fermi liquid theory, and the Hubbard model with Mott metal-insulator transition, accompanied by 16 interactive 60 FPS numerical simulations and 24 honors examination problems.",
    "units": units
}

js_content = "window.COURSE_DATA = " + json.dumps(course_data, indent=2, ensure_ascii=False) + ";\nwindow.SSP2_COURSE_DATA = window.COURSE_DATA;\n"

with open("solid-state-physics-2-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("solid-state-physics-2-data.js written successfully! Size:", len(js_content))
