import os

path_to_check_file = "C:/PytonTR2/my_existing_file.txt"
path_to_check_dir = "C:/PytonTR2"

# Create dummy for demostration
with open(path_to_check_file, 'w') as f:
    f.write("Hello")
os.makedirs(path_to_check_dir, exist_ok=True)

if os.path.exists(path_to_check_file):
    print(f"'{path_to_check_file}' exists.")
else:
    print(f"'{path_to_check_dir}' does not exist.")