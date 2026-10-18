"""
build_supra_units_1_2_3.py
Combines Units 1, 2, and 3 for Supramolecular Chemistry.
Total: 24 sections, 27 problems.
Strict compliance: zero prohibited tokens, zero carriage returns.
"""

from create_supra_u1 import get_unit_1
from create_supra_u2 import get_unit_2
from create_supra_u3 import get_unit_3

def get_units_1_2_3():
    u1 = get_unit_1()
    u2 = get_unit_2()
    u3 = get_unit_3()
    return [u1, u2, u3]

if __name__ == "__main__":
    units = get_units_1_2_3()
    for u in units:
        print(f"Loaded {u['id']}: {u['title']} ({len(u['sections'])} sections, {len(u['problems'])} problems)")
