import os
import glob
import shutil

# Get all html files except index.html
html_files = [f for f in glob.glob("*.html") if f not in ("index.html", "generate_index.py", "organize_repo.py")]

# Create models directory
os.makedirs("models", exist_ok=True)

# Organize files into discipline folders based on prefix
disciplines = set()
for file in html_files:
    # Extract prefix (e.g. aero_026_... -> aero)
    parts = file.split('_')
    # Handle multi-word prefixes like chem_eng, computer_science
    prefix = ""
    for i, part in enumerate(parts):
        if part.isdigit():
            prefix = "_".join(parts[:i])
            break
    if not prefix:
        # fallback
        prefix = "misc"
        
    discipline_dir = os.path.join("models", prefix)
    os.makedirs(discipline_dir, exist_ok=True)
    
    # Move file
    shutil.move(file, os.path.join(discipline_dir, file))
    disciplines.add(prefix)

print(f"Organized {len(html_files)} files into {len(disciplines)} discipline folders inside /models.")
