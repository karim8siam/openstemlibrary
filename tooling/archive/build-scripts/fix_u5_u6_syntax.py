with open("build_calc1_units_5_6.py", "r", encoding="utf-8") as f:
    text = f.read()

# Replace line 420 multiline r"..." with r"""..."""
text = text.replace(
    '''"math": r"\\begin{aligned}
y^{(10)} &= \\binom{10}{0} 2^{10} e^{2x} (x^3) + \\binom{10}{1} 2^9 e^{2x} (3x^2) + \\binom{10}{2} 2^8 e^{2x} (6x) + \\binom{10}{3} 2^7 e^{2x} (6) \\\\
&= e^{2x} 2^7 \\left[ 2^3 x^3 + 10(2^2)(3x^2) + 45(2)(6x) + 120(6) \\right] \\\\
&= 128 e^{2x} \\left[ 8x^3 + 120x^2 + 540x + 720 \\right] = 1024 e^{2x} \\left[ x^3 + 15x^2 + \\frac{135}{2}x + 90 \\right]
\\end{aligned}",''',
    '''"math": r"""\\begin{aligned}
y^{(10)} &= \\binom{10}{0} 2^{10} e^{2x} (x^3) + \\binom{10}{1} 2^9 e^{2x} (3x^2) + \\binom{10}{2} 2^8 e^{2x} (6x) + \\binom{10}{3} 2^7 e^{2x} (6) \\\\
&= e^{2x} 2^7 \\left[ 2^3 x^3 + 10(2^2)(3x^2) + 45(2)(6x) + 120(6) \\right] \\\\
&= 128 e^{2x} \\left[ 8x^3 + 120x^2 + 540x + 720 \\right] = 1024 e^{2x} \\left[ x^3 + 15x^2 + \\frac{135}{2}x + 90 \\right]
\\end{aligned}""",'''
)

with open("build_calc1_units_5_6.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed build_calc1_units_5_6.py syntax.")
