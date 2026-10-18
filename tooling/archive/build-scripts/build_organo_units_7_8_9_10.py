"""
build_organo_units_7_8_9_10.py
Bundle module for Units 7, 8, 9, 10 of Organometallic Chemistry.
"""

from create_organo_u7 import get_unit_7
from create_organo_u8 import get_unit_8
from create_organo_u9 import get_unit_9
from create_organo_u10 import get_unit_10

def get_units_7_8_9_10():
    u7 = get_unit_7()
    u8 = get_unit_8()
    u9 = get_unit_9()
    u10 = get_unit_10()
    return [u7, u8, u9, u10]

if __name__ == "__main__":
    units = get_units_7_8_9_10()
    print(f"Successfully loaded {len(units)} units.")
    for u in units:
        print(f"Unit {u['unit_number']}: {u['title']} - Sections: {len(u['sections'])}, Problems: {len(u['problems'])}")
