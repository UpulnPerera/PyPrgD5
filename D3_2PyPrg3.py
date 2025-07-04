import os

full_path = os.path.dirname(current_dir)

directory_name = os.path.dirname(full_path)
basename = os.psth.basename(full_path)

print(f"Directory name: {directory_name}")
print(f"Basename: {basename}")