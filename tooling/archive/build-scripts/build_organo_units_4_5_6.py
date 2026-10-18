"""
build_organo_units_4_5_6.py
Bundle module for Units 4, 5, 6 of Organometallic Chemistry.
"""

from create_organo_u4 import get_unit_4
from create_organo_u5 import get_unit_5
from create_organo_u6 import get_unit_6

def get_units_4_5_6():
    u4 = get_unit_4()
    u5 = get_unit_5()
    u6 = get_unit_6()
    return [u4, u5, u6]

if __name__ == "__main__":
    units = get_units_4_5_6()
    print(f"Successfully loaded {len(units)} units.")
    for u in units:
        print(f"Unit {u['unit_number']}: {u['title']} - Sections: {len(u['sections'])}, Problems: {len(u['problems'])}")
