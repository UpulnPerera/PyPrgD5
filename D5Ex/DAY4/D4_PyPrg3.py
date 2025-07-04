import os
folder_to_remove = "empty_folder_to_delete"

try:
    os.rmdir(folder_to_remove)
    print(f"Directory '{folder_to_remove}' removed successfully.")
except Exception as e:
    print(f"Error removing directory '{folder_to_remove}' :{e}")