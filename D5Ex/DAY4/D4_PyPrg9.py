import shutil
import os

# ---Setup: Create a dummy file and a traget directory ---
data_folder = "my_data_for_archive"
os.makedirs(os.path.join(data_folder, "docs"), exist_ok=True)
with open(os.path.join(data_folder, "impotant.txt"), "w") as f:
    f.write("Importanta data here.")
with open(os.path.join(data_folder, "docs", "notes.md"), "w") as f:
    f.write("# Meeting Notes")
print(f"Created dummy folder for archiving: ' {data_folder}")

# --- Create a Zip archive ---
archive_name = "my_data_archive"

try:
    # Create my_data_archive.zip in the current directory.
    #containing the content of my data for archive
    archive_path = shutil.make_archive(archive_name, 'zip', root_dir=data_folder)
    print(f"Archived created: '{archive_path}'")
    print(f"Does archive exists? {os.path.exist(archive_path)}")
except Exception as e:
    print(f"An error occurred during archiving: {e}")

# --- Cleanup ---

if os.path.exists(data_folder):
    os.remove(data_folder) # Use rmtree as target_dir now contain
if os.path.exists(archive_path):
    os.remove(archive_path) # Use rmtree as target_dir now contain
print("Cleaned up dummy files.")