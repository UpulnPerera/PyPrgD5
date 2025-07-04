import os

#List contents of the current directory
print("Content of current directory:")
for item in os.listdir('.'):
    print(item)

# You can also specify a path
# Foe example, to list contents of the /tmp directory:
# print("\nContents of /tmp directory:")
# for item in ob.listdir('/tmp')
#   print(item)