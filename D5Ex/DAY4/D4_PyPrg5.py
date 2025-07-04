import os

old_name = "old_file.txt"
new_name = "new_file.txt"

# Creat a dummy file for demonstration
with open(old_name, 'w') as f:
    f.write("Content of the old file.")

try:
    os.rename(old_name, new_name)
    print(f"Renamed: '{old_name}' to '{new_name}'.")
except FileNotFoundError:
    print(f"'{old_name}' does not exist.")
except FileExistsError:
    print(f"'{new_name}' already exists.")
except Exception as e:
    print(f"An error occurred: :{e}")