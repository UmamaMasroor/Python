# 5. Label the program written in problem 4 with comments. 

import os

# Specify the directory you want to list
directory = "/"

# Get the list of all files and directories in the specified directory
contents = os.listdir(directory)

print(f"Contents of the directory '{directory}':")
for item in contents:
    print(item)