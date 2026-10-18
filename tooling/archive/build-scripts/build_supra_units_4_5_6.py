"""
build_supra_units_4_5_6.py
Combines Units 4, 5, and 6 for Supramolecular Chemistry.
Total: 24 sections, 27 problems.
Strict compliance: zero prohibited tokens, zero carriage returns.
"""

from create_supra_u4 import get_unit_4
from create_supra_u5 import get_unit_5
from create_supra_u6 import get_unit_6

def get_units_4_5_6():
    u4 = get_unit_4()
    u5 = get_unit_5()
    u6 = get_unit_6()
    return [u4, u5, u6]

if __name__ == "__main__":
    units = get_units_4_5_6()
    for u in units:
        print(f"Loaded {u['id']}: {u['title']} ({len(u['sections'])} sections, {len(u['problems'])} problems)")
