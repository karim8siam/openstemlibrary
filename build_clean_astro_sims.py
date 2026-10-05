# build_clean_astro_sims.py
import build_astro_sims_part2 as p2
import build_astro_sims_part3 as p3

with open("build_astro_sims.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

ns = {}
exec("".join(lines[:769]), ns)

full_js = ns["sims_header"]
full_js += ns["sim1"]
full_js += ns["sim2"]
full_js += ns["sim3"]
full_js += ns["sim4"]
full_js += ns["sim5"]
full_js += p2.sim6
full_js += p2.sim7
full_js += p2.sim8
full_js += p2.sim9
full_js += p2.sim10
full_js += p3.sim11
full_js += p3.sim12
full_js += p3.sim13
full_js += p3.sim14
full_js += p3.sim15
full_js += p3.sim16

with open("astrophysics-sims.js", "w", encoding="utf-8") as f:
    f.write(full_js)

print(f"astrophysics-sims.js cleanly generated ({len(full_js)} bytes)")
