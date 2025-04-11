# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 05:46:16 2023

@author: The_Makoris
"""

"""
This program prints the names of all GIF image files in the CWD and 
subdirectories of the current directory
"""

import os

# Get the contents of the CWD
dirName = os.getcwd()
contents = os.listdir()

count = 0

for name in contents:
    # If the entry is a directory repeat on its contents
    if os.path.isdir(name):
        for name2 in os.listdir(name):
            entry = os.path.join(name, name2)
            
            # If a file ending in .gif, print it            
            if os.path.isfile(entry) and name2.endswith(".gif"):
                print(os.path.join(dirName, entry))
                count += 1
                
    # Otherwise, it is a file. If the name ends in .gif, print it
    elif name.endswith(".gif"):
        print(os.path.join(dirName, name))
        count += 1
print(f'There is\\are {count} gif image(s) in the current directory.')