"""
build_supra_units_7_8_9_10.py
Combines Units 7, 8, 9, and 10 for Supramolecular Chemistry.
Total: 32 sections, 36 problems.
Strict compliance: zero prohibited tokens, zero carriage returns.
"""

from create_supra_u7 import get_unit_7
from create_supra_u8 import get_unit_8
from create_supra_u9 import get_unit_9
from create_supra_u10 import get_unit_10

def get_units_7_8_9_10():
    u7 = get_unit_7()
    u8 = get_unit_8()
    u9 = get_unit_9()
    u10 = get_unit_10()
    return [u7, u8, u9, u10]

if __name__ == "__main__":
    units = get_units_7_8_9_10()
    for u in units:
        print(f"Loaded {u['id']}: {u['title']} ({len(u['sections'])} sections, {len(u['problems'])} problems)")
