import pathlib
import os

# --- 1. Creating Path Objects ---
print("\nCreating Path Objects")
#Current workingdirectory
print(pathlib.Path)
current_dir = pathlib.Path.cwd()
print(f"Current working directory (Path object): {current_dir}")

# A relative path
relative_file = pathlib.Path('my_document.txt')
print(f"Relative file path: {relative_file}")

# An absolute path (example, adjust for your os)
absolute_path = pathlib.Path('/tem/test_dir') # For Linux/macOS
# Absolute_path = pathlib.Path('C:/Users/Public/Documnets/test_dir')
print(f"Absolute path (example): {absolute_path}")

# Joining the paths using the / operator (very intuitive!)
joined_path = current_dir / 'data' / 'report' / 'report.csv'
print(f"Joined path using / operator: {joined_path}")

# --- 2. Accessing Path Components ----
print("\n--- 2. Accessing Path Components ----")
# Using the joined_path from above for demostration
print(f"Full Path: {joined_path}")
print(f"File/Folder name: {joined_path.name}") # 'report.csv'
print(f"Parent directory: {joined_path.parent}") # 'path/to/current/dir/data'
print(f"File stem (name without suffix): {joined_path.stem}") # 'report'
print(f"File suffix (extension): {joined_path.suffix}") # '.csv'
print(f"All_suffixes: {joined_path.suffixes}") # ['.csv']
print(f"Anchor (root of the path): {joined_path.anchor}") # '/' on Unix, 'C:\'
print(f"Path parts: {joined_path.parts}") # ('/', 'path', 'to', ..., 'report.c')

# ---3. Checking Patha (Existence and Type) ----
print("\n---3. Checking Patha (Existence and Type) ----")
test_file = pathlib.Path('test_file.txt')
test_dir = pathlib.Path('test_directory')