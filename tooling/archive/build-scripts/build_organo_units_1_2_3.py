"""
build_organo_units_1_2_3.py
Bundle module for Units 1, 2, 3 of Organometallic Chemistry.
"""

from create_organo_u1 import get_unit_1
from create_organo_u2 import get_unit_2
from create_organo_u3 import get_unit_3

def get_units_1_2_3():
    u1 = get_unit_1()
    u2 = get_unit_2()
    u3 = get_unit_3()
    return [u1, u2, u3]

if __name__ == "__main__":
    units = get_units_1_2_3()
    print(f"Successfully loaded {len(units)} units.")
    for u in units:
        print(f"Unit {u['unit_number']}: {u['title']} - Sections: {len(u['sections'])}, Problems: {len(u['problems'])}")
