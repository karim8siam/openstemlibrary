# -*- coding: utf-8 -*-
"""
Bundle Units 7, 8, 9, and 10 for Environmental Chemistry.
"""

import json
from create_env_u7 import get_unit_7
from create_env_u8 import get_unit_8
from create_env_u9 import get_unit_9
from create_env_u10 import get_unit_10

def build():
    u7 = get_unit_7()
    u8 = get_unit_8()
    u9 = get_unit_9()
    u10 = get_unit_10()
    
    units = [u7, u8, u9, u10]
    
    tot_sections = sum(len(u["sections"]) for u in units)
    tot_problems = sum(len(u["problems"]) for u in units)
    
    print(f"Loaded Units 7-10 successfully: {len(units)} units, {tot_sections} sections, {tot_problems} problems.")
    
    # Save bundle json
    with open("env_units_7_8_9_10.json", "w", encoding="utf-8") as f:
        json.dump(units, f, indent=2, ensure_ascii=False)
    print("Saved env_units_7_8_9_10.json.")

if __name__ == "__main__":
    build()
