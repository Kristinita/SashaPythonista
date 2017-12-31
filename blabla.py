# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2017-12-31 15:43:57
# @Last Modified time: 2017-12-31 16:46:30
# Check, if blabla in OS

import os

# Get current directory
# https://stackoverflow.com/a/5137507/5951529
currentdirectory = os.getcwd()

# Get list all filenames in a directory
# https://stackoverflow.com/a/1120736/5951529
for filename in os.listdir(currentdirectory):

    # Check if string in a file
    # https://stackoverflow.com/a/4944929/5951529
    if 'blabla' in open(filename).read():
        print("true")
    else:
        print(filename + " false")
