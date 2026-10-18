with open("build_calc1_units_1_2.py", "r", encoding="utf-8") as f:
    text = f.read()

# Replace any multiline r"..." with r"""..."""
import re
# Let's fix line 200 array table and line 410 array table
text = text.replace(
    '''"math": r"\\begin{array}{c|c|c|c|c|c}
\\text{Interval} & (-\\infty, -2) & (-2, -1) & (-1, 1) & (1, 2) & (2, \\infty) \\\\
\\hline
4 - x^2 & - & + & + & + & - \\\\
x^2 - 1 & + & + & - & + & + \\\\
\\hline
\\text{Quotient} & - & + & - & + & -
\\end{array}",''',
    '''"math": r"""\\begin{array}{c|c|c|c|c|c}
\\text{Interval} & (-\\infty, -2) & (-2, -1) & (-1, 1) & (1, 2) & (2, \\infty) \\\\
\\hline
4 - x^2 & - & + & + & + & - \\\\
x^2 - 1 & + & + & - & + & + \\\\
\\hline
\\text{Quotient} & - & + & - & + & -
\\end{array}""",'''
)

text = text.replace(
    '''"math": r"\\begin{aligned}
\\sinh(\\theta_1 + \\theta_2) &= \\sinh\\theta_1 \\cosh\\theta_2 + \\cosh\\theta_1 \\sinh\\theta_2 \\\\
\\cosh(\\theta_1 + \\theta_2) &= \\cosh\\theta_1 \\cosh\\theta_2 + \\sinh\\theta_1 \\sinh\\theta_2
\\end{aligned}",''',
    '''"math": r"""\\begin{aligned}
\\sinh(\\theta_1 + \\theta_2) &= \\sinh\\theta_1 \\cosh\\theta_2 + \\cosh\\theta_1 \\sinh\\theta_2 \\\\
\\cosh(\\theta_1 + \\theta_2) &= \\cosh\\theta_1 \\cosh\\theta_2 + \\sinh\\theta_1 \\sinh\\theta_2
\\end{aligned}""",'''
)

with open("build_calc1_units_1_2.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated build_calc1_units_1_2.py with triple quotes.")
