import os
import glob

# Find all HTML files recursively in models/
html_files = glob.glob("models/**/*.html", recursive=True)
html_files.sort()

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Engineering Physics UI Components</title>
    <style>
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: #0d0d0d;
            color: #f1f1f1;
            margin: 0;
            padding: 40px;
        }
        h1 {
            font-weight: 300;
            letter-spacing: 2px;
            text-align: center;
            margin-bottom: 10px;
        }
        p.subtitle {
            text-align: center;
            color: #888;
            margin-bottom: 40px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        .discipline-section {
            margin-bottom: 40px;
        }
        .discipline-title {
            border-bottom: 1px solid #333;
            padding-bottom: 10px;
            margin-bottom: 20px;
            text-transform: capitalize;
            color: #aaa;
            font-weight: 400;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 15px;
        }
        .card {
            background-color: #1a1a1a;
            border: 1px solid #333;
            border-radius: 6px;
            padding: 15px 20px;
            transition: all 0.2s ease;
            text-decoration: none;
            color: #e0e0e0;
            display: flex;
            align-items: center;
            font-size: 14px;
        }
        .card:hover {
            border-color: #555;
            background-color: #222;
            transform: translateY(-2px);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>PHYSICS COMPONENT LIBRARY</h1>
        <p class="subtitle">348 Interactive UI Models</p>
"""

# Group by discipline
from collections import defaultdict
disciplines = defaultdict(list)
for f in html_files:
    discipline = os.path.basename(os.path.dirname(f))
    disciplines[discipline].append(f)

for discipline in sorted(disciplines.keys()):
    title = discipline.replace("_", " ").title()
    html_content += f"""        <div class="discipline-section">
            <h2 class="discipline-title">{title}</h2>
            <div class="grid">\n"""
    
    for filepath in sorted(disciplines[discipline]):
        filename = os.path.basename(filepath)
        display_name = filename.replace(".html", "").replace("_", " ").title()
        # strip prefix and numbers from display name for cleaner look
        parts = display_name.split()
        clean_name = " ".join([p for p in parts if not p.isdigit() and p.lower() != discipline.replace("_", " ")])
        
        html_content += f"""                <a href="{filepath}" target="_blank" class="card">
                    {display_name}
                </a>\n"""
                
    html_content += """            </div>
        </div>\n"""

html_content += """    </div>
</body>
</html>"""

with open("index.html", "w") as f:
    f.write(html_content)

print(f"Regenerated index.html with grouped paths.")
