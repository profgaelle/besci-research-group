import os

root_dir = "."  # current directory
# old_pattern = "publication_types:\n- '2'"
# new_pattern = 'publication_types: ["article-journal"]'
# old_pattern = "publication_types:\n- '1'"
# new_pattern = "publication_types: ['paper-conference']"
# old_pattern = "publication_types:\n- '6'"
# new_pattern = "publication_types: ['chapter']"
old_pattern = "- admin"
new_pattern = "- Gaëlle Vallée-Tourangeau"



changed_files = []

for dirpath, _, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename == "index.md":
            file_path = os.path.join(dirpath, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            if old_pattern in content:
                new_content = content.replace(old_pattern, new_pattern)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                changed_files.append(file_path)

print(f"Updated {len(changed_files)} files:")
for f in changed_files:
    print(f)