import os
import re

root_dir = "content/publication"
changed_files = []

for dirpath, _, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename == "index.md":
            file_path = os.path.join(dirpath, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Remove author_notes section (including the list items)
            new_content = re.sub(r'# Author notes.*?\nauthor_notes:\n(?:- ".*?"\n)*', '', content, flags=re.DOTALL)
            
            if new_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                changed_files.append(file_path)

print(f"Updated {len(changed_files)} files:")
for f in changed_files:
    print(f)