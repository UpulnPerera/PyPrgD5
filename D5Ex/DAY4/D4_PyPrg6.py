import shutil
import os

# ---Setup: Create a dummy file and a traget directory ---
file_to_move = "report.pdf"
target_dir = "archives"
with open(file_to_move, "w") as f:
    f.write("Confidential report data.")
os.makedirs(target_dir, exist_ok=True)
print(f"Created '{file_to_move}' and '{target_dir}'.")

# ---Move the file ---
try:
    shutil.move(file_to_move, target_dir)
    print(f"'{file_to_move}' moved to '{target_dir}' successfully.")
    print(f"New path: {os.path.join(target_dir, file_to_move)}")
except FileNotFoundError:
    print(f"Error: Source file '{file_to_move}' not found.")
except Exception as e:
    print(f"An error occurred during move: {e}")

# --- Cleanup ---
if os.path.exists(target_dir):
    shutil.rmtree(target_dir) # Use rmtree as target_dir now contain
print("Cleaned up dummy diretory.")
