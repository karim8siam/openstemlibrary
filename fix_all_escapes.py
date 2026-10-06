import glob
import json
import re

def sanitize_string(s):
    if not isinstance(s, str):
        return s
    # Map raw ASCII control characters back to their escaped LaTeX equivalents
    # \x0c -> \f (e.g. \frac)
    # \x07 -> \a (e.g. \alpha, \arctan)
    # \x08 -> \b (e.g. \beta)
    # \x0b -> \v (e.g. \vert, \vec)
    s = s.replace('\x0c', '\\f')
    s = s.replace('\x07', '\\a')
    s = s.replace('\x08', '\\b')
    s = s.replace('\x0b', '\\v')
    return s

def sanitize_obj(obj):
    if isinstance(obj, str):
        return sanitize_string(obj)
    elif isinstance(obj, dict):
        return {k: sanitize_obj(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [sanitize_obj(x) for x in obj]
    return obj

json_files = sorted(glob.glob("calc1_u*.json") + glob.glob("calc2_u*.json") + glob.glob("geom2d_u*.json") + glob.glob("algebra_u*.json") + glob.glob("geom3d_u*.json") + glob.glob("calc3_u*.json") + glob.glob("la_u*.json"))
modified_count = 0

for f in json_files:
    with open(f, "r", encoding="utf-8") as fp:
        data = json.load(fp)
    cleaned = sanitize_obj(data)
    with open(f, "w", encoding="utf-8") as fp:
        json.dump(cleaned, fp, indent=2, ensure_ascii=False)
    modified_count += 1
    print(f"Sanitized: {f}")

print(f"Done sanitizing {modified_count} JSON files.")
