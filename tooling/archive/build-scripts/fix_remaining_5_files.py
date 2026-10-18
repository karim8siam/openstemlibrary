import re

# 1. electricity-magnetism.html
with open("electricity-magnetism.html", "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace("\x0bec{E}", "\\vec{E}")
c = c.replace("\x0bec{l}", "\\vec{l}")
c = c.replace("\x0bec{F}", "\\vec{F}")
c = c.replace("\x0bec{B}", "\\vec{B}")
c = c.replace("\x0bec", "\\vec")
c = c.replace("\x0b", "")
with open("electricity-magnetism.html", "w", encoding="utf-8") as f:
    f.write(c)
print("Cleaned electricity-magnetism.html")

# 2. mechanics-data.js
with open("mechanics-data.js", "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace("\\u0007lpha", "\\alpha")
c = c.replace("\x07lpha", "\\alpha")
c = c.replace("\\u0007", "")
c = c.replace("\x07", "")
with open("mechanics-data.js", "w", encoding="utf-8") as f:
    f.write(c)
print("Cleaned mechanics-data.js")

# 3. optics-data.js
with open("optics-data.js", "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace("\\u0007lpha", "\\alpha")
c = c.replace("\x07lpha", "\\alpha")
c = c.replace("\\u0007", "")
c = c.replace("\x07", "")
with open("optics-data.js", "w", encoding="utf-8") as f:
    f.write(c)
print("Cleaned optics-data.js")

# 4. plasma-physics.html
with open("plasma-physics.html", "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace("\x07lpha", "\\alpha")
c = c.replace("\\u0007lpha", "\\alpha")
c = c.replace("\x07", "")
c = c.replace("\\u0007", "")
with open("plasma-physics.html", "w", encoding="utf-8") as f:
    f.write(c)
print("Cleaned plasma-physics.html")

# 5. solid-state-physics-2.html
with open("solid-state-physics-2.html", "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace("\x0bec{k}", "\\vec{k}")
c = c.replace("\x0bec", "\\vec")
c = c.replace("\x0b", "")
with open("solid-state-physics-2.html", "w", encoding="utf-8") as f:
    f.write(c)
print("Cleaned solid-state-physics-2.html")

