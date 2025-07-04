import os

# Define the directory you want to change to
# Make sure this directory existson your system
new_directory = "./tmp" # Examle for Linux/macOS
# For Windows, it might be somthinglike "C:\\Users\YourUser\Document"
print(os.path.basename)
if os.path.exists(new_directory) and os.path.isdir(new_directory):
    os.chdir(new_directory)
    print(f"Changed directory to: {os.getcwd()}")
else:
    print(f"Directory {new_directory} does not exist or is not a directory")