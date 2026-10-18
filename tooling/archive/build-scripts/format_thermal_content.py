# Script to convert raw markdown in tp_u1.json to tp_u8.json into clean semantic HTML
import json
import re

def convert_md_to_clean_html(md_text):
    if not md_text:
        return ""
    
    # If already mostly HTML, return
    if "<h4" in md_text and "<ul" in md_text:
        return md_text
        
    text = md_text.replace("\r\n", "\n").strip()
    
    # Isolate $$...$$ so they are on their own lines surrounded by blank lines
    def isolate_math(match):
        math_content = match.group(1).strip()
        return f"\n\n$${math_content}$$\n\n"
        
    text = re.sub(r'\$\$(.*?)\$\$', isolate_math, text, flags=re.DOTALL)
    
    # Split into lines
    lines = text.split("\n")
    output = []
    in_ul = False
    in_ol = False
    para_lines = []
    
    def flush_para():
        nonlocal para_lines
        if para_lines:
            p_content = " ".join(para_lines).strip()
            # If line is only bold header like 'Examples:' or 'Key Observations:'
            if p_content.startswith("<strong>") and p_content.endswith("</strong>") and len(p_content) < 60:
                output.append(f"<h5>{p_content.replace('<strong>', '').replace('</strong>', '')}</h5>")
            elif p_content:
                output.append(f"<p>{p_content}</p>")
            para_lines = []
            
    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul:
            output.append("</ul>")
            in_ul = False
        if in_ol:
            output.append("</ol>")
            in_ol = False

    for line in lines:
        s = line.strip()
        if not s:
            flush_para()
            close_lists()
            continue
            
        # Standalone Math line $$...$$
        if s.startswith("$$") and s.endswith("$$") and len(s) >= 4:
            flush_para()
            close_lists()
            output.append(f'<div class="math-display">{s}</div>')
            continue
            
        # Headings ###
        if s.startswith("### "):
            flush_para()
            close_lists()
            heading = s[4:].strip()
            output.append(f"<h4>{heading}</h4>")
            continue
            
        # Headings ####
        if s.startswith("#### "):
            flush_para()
            close_lists()
            heading = s[5:].strip()
            output.append(f"<h5>{heading}</h5>")
            continue
            
        # Headings like '1. **Searle\'s Bar Method...**'
        bold_head_match = re.match(r'^(?:([0-9]+\.\s+))?\*\*(.*?)\*\*$', s)
        if bold_head_match:
            flush_para()
            close_lists()
            prefix = bold_head_match.group(1) or ""
            title = bold_head_match.group(2)
            output.append(f"<h4>{prefix}{title}</h4>")
            continue

        # Bullet list item: - or *
        if s.startswith("- ") or s.startswith("* "):
            flush_para()
            if in_ol:
                output.append("</ol>")
                in_ol = False
            if not in_ul:
                output.append("<ul>")
                in_ul = True
            item_text = s[2:].strip()
            # Inline formatting
            item_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item_text)
            item_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', item_text)
            output.append(f"  <li>{item_text}</li>")
            continue
            
        # Ordered list items like '1. ', '2. '
        ol_match = re.match(r'^([0-9]+)\.\s+(.*)$', s)
        if ol_match:
            num = int(ol_match.group(1))
            body = ol_match.group(2).strip()
            
            # Check if this is a section heading like '1. The First Energy Equation...' or '1. Isolated Systems: ...'
            if not in_ol and (body.startswith("**") or "Method" in body or "Equation" in body or "Nature" in body or "Criteria" in body or "Equilibrium" in body or "Law" in body):
                flush_para()
                close_lists()
                # If it's a bold concept like '1. **Isolated Systems**: ...'
                if body.startswith("**") and "**:" in body:
                    m = re.match(r'^\*\*(.*?)\*\*:\s*(.*)$', body)
                    term = m.group(1)
                    desc = m.group(2)
                    output.append(f"<p><strong>{num}. {term}:</strong> {desc}</p>")
                else:
                    clean_title = re.sub(r'\*\*', '', body)
                    output.append(f"<h4>{num}. {clean_title}</h4>")
                continue
            else:
                flush_para()
                if in_ul:
                    output.append("</ul>")
                    in_ul = False
                if not in_ol:
                    output.append("<ol>")
                    in_ol = True
                body = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', body)
                body = re.sub(r'\*(.*?)\*', r'<em>\1</em>', body)
                output.append(f"  <li>{body}</li>")
                continue
                
        # Regular text line: apply bold/italics
        close_lists()
        formatted_line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', s)
        formatted_line = re.sub(r'\*(.*?)\*', r'<em>\1</em>', formatted_line)
        para_lines.append(formatted_line)
        
    flush_para()
    close_lists()
    
    return "\n\n".join(output)

# Process all 8 units
all_units = []
for i in range(1, 9):
    fname = f"tp_u{i}.json"
    with open(fname, "r", encoding="utf-8") as f:
        u = json.load(f)
        
    u["number"] = i
    u["unitNumber"] = i
    
    for s in u.get("sections", []):
        s["content"] = convert_md_to_clean_html(s.get("content", ""))
        
    for p in u.get("problems", []):
        if "question" in p:
            p["question"] = convert_md_to_clean_html(p["question"])
        if "statement" in p:
            p["statement"] = convert_md_to_clean_html(p["statement"])
        for step in p.get("steps", []):
            if "explanation" in step:
                step["explanation"] = convert_md_to_clean_html(step["explanation"])
            if "detail" in step:
                step["detail"] = convert_md_to_clean_html(step["detail"])
                
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(u, f, indent=2)
        
    all_units.append(u)
    print(f"Processed and cleaned {fname}")

# Rebuild thermal-physics-data.js
course_data = {
    "courseId": "thermal-physics",
    "courseTitle": "Thermal Physics",
    "courseSubtitle": "Classical Thermodynamics, Statistical Entropy, Thermodynamic Potentials, Heat Transfer & Kinetic Theory",
    "units": all_units
}

js_content = "// Thermal Physics Complete Interactive Textbook Dataset\n// Pure client-side data architecture\nwindow.COURSE_DATA = " + json.dumps(course_data, indent=2) + ";\n"

with open("thermal-physics-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("thermal-physics-data.js successfully rebuilt with clean semantic HTML!")
