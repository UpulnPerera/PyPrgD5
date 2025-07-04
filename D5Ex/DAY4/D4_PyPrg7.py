import shutil
import os

# ---Setup: Create a dummy file and a traget directory ---
source_dir = "my_source_project"
os.makedirs(os.path.join(source_dir, "css"), exist_ok=True)
os.makedirs(os.path.join(source_dir, "js"), exist_ok=True)

with open(os.path.join(source_dir, "index.html"), "w") as f:
    f.write("<html></html>")
with open(os.path.join(source_dir, "css", "style.css"), "w") as f:
    f.write("body{}")
print(f"Created dummy source directory: '{source_dir}'.")

# ---Copy the directory tree ---
destination_dir = "my_backup_project"

try:
    # if destination_dir already exists and is not empty, copy tree will raise
    # To overwrite, you'd typically renmove the destination first or handle more 
    shutil.copytree(source_dir, destination_dir)
    print(f"'{source_dir}' copied to '{destination_dir}' successfully.")
    print("Contents of destination directory:")
    for root, dirs, files in os.walk(destination_dir):
        level = root.replace(destination_dir, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")
except FileNotFoundError:
    print(f"Error: Destination directory '{destination_dir}' already exists.")
except Exception as e:
    print(f"An error occurred during copytree: {e}")

# --- Cleanup ---
if os.path.exists(source_dir):
    shutil.rmtree(source_dir) # Use rmtree as target_dir now contain
if os.path.exists(destination_dir):
    shutil.rmtree(destination_dir) # Use rmtree as target_dir now contain
print("Cleaned up dummy diretories.")