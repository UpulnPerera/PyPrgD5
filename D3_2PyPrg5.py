import os

path1 = "C:/PytonTR2/myexisting_file.txt" # Using the one
path2 = "C:/PytonTR2" # Using the one created above
path3 = "non_existent_path"

print(f"'{path1}' is a file: {os.path.isfile(path1)}")
print(f"'{path1}' is a file: {os.path.isdir(path1)}")

print(f"'{path2}' is a file: {os.path.isfile(path2)}")
print(f"'{path2}' is a file: {os.path.isdir(path2)}")

print(f"'{path3}' is a file: {os.path.isfile(pat31)}")
print(f"'{path3}' is a file: {os.path.isdir(path3)}")