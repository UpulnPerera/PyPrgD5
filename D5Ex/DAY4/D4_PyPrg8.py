import shutil
import os

# ---Setup: Create a dummy file and a traget directory ---
source_file = "source_doc.txt"

with open(source_file, "w") as f:
    f.write("This is the original content")
print(f"Created {source_file}' for copying.")

# ---Copy the file ---
destination_file = "copied_doc.txt"

try:
    shutil.copy(source_file, destination_file)
    print(f"'{source_file}' copied to '{destination_file}' successfully.")
    print(f"Contents of '{destination_file}': {open(destination_file).read()}")
except FileNotFoundError:
    print(f"Error: Source file '{source_file}' not found.")
except Exception as e:
    print(f"An error occurred during copy: {e}")

# --- Cleanup ---
if os.path.exists(source_file):
    os.remove(source_file) # Use rmtree as target_dir now contain
if os.path.exists(destination_file):
    os.remove(destination_file) # Use rmtree as target_dir now contain
print("Cleaned up dummy files.")