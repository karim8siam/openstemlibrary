# -*- coding: utf-8 -*-
"""
Bundle Units 4, 5, and 6 for Environmental Chemistry.
"""

import json
from create_env_u4 import get_unit_4
from create_env_u5 import get_unit_5
from create_env_u6 import get_unit_6

def build():
    u4 = get_unit_4()
    u5 = get_unit_5()
    u6 = get_unit_6()
    
    units = [u4, u5, u6]
    
    tot_sections = sum(len(u["sections"]) for u in units)
    tot_problems = sum(len(u["problems"]) for u in units)
    
    print(f"Loaded Units 4-6 successfully: {len(units)} units, {tot_sections} sections, {tot_problems} problems.")
    
    # Save bundle json
    with open("env_units_4_5_6.json", "w", encoding="utf-8") as f:
        json.dump(units, f, indent=2, ensure_ascii=False)
    print("Saved env_units_4_5_6.json.")

if __name__ == "__main__":
    build()
